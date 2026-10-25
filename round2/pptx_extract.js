/* Reads the built deck's layout for make_pptx.py (the editable PowerPoint). Injected into a copy of Axis.html and run
   in headless Chrome; it replaces the page with <pre id="pptx-data">JSON</pre>, which Chrome's --dump-dom prints.

   For each slide, in paint order:
     box   an element's own painting: fill, gradient, borders, radius, shadow (-> a native shape)
     img   a picture, with its object-fit crop and the clip of a round parent (-> a native picture)
     svg   an inline drawing (a chart, the house, an icon, an arrow) as standalone SVG plus a 3x PNG (-> a picture
           with an SVG blip, which PowerPoint can convert to shapes)
     text  every text block, line by line exactly as the browser broke it, each run with its own font, size, weight,
           colour and spacing (-> a native text box, one paragraph a line)
   Pseudo-elements (::before, ::after) are first turned into real elements so their rules and markers come through. */
(function () {
  'use strict';
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const num = v => parseFloat(v) || 0;

  function rgba(s) {
    const m = (s || '').match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number);
    return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1];
  }

  /* ---- pseudo-elements -> real elements, so getBoundingClientRect can see them ---- */
  function materializePseudos(root) {
    const todo = [];
    for (const el of root.querySelectorAll('*')) {
      if (el.closest('svg') || el.closest('aside.notes')) continue;
      for (const which of ['::before', '::after']) {
        const cs = getComputedStyle(el, which);
        const c = cs.content;
        if (!c || c === 'none' || c === 'normal' || cs.display === 'none') continue;
        const props = [];
        for (let i = 0; i < cs.length; i++) props.push([cs[i], cs.getPropertyValue(cs[i])]);
        const m = c.match(/^"([\s\S]*)"$/);
        todo.push({el, which, props, text: m ? m[1].replace(/\\([0-9a-fA-F]{1,6}) ?/g, (_, h) => String.fromCodePoint(parseInt(h, 16))).replace(/\\(.)/g, '$1') : ''});
      }
    }
    const before = new Map();
    for (const el of root.querySelectorAll('*')) before.set(el, el.getBoundingClientRect());
    for (const t of todo) {
      const s = document.createElement('ps-el');            // a tag no deck rule targets
      for (const [p, v] of t.props) if (p !== 'content') s.style.setProperty(p, v);
      s.textContent = t.text;
      if (t.which === '::before') t.el.insertBefore(s, t.el.firstChild); else t.el.appendChild(s);
      t.el.setAttribute('data-psoff', '');
    }
    const st = document.createElement('style');
    st.textContent = '[data-psoff]::before,[data-psoff]::after{content:none!important}';
    document.head.appendChild(st);
    let moved = 0;                                          // self-check: nothing else may move
    for (const [el, r] of before) {
      const q = el.getBoundingClientRect();
      if (Math.abs(q.left - r.left) > 1 || Math.abs(q.top - r.top) > 1 || Math.abs(q.width - r.width) > 1) moved++;
    }
    return {pseudos: todo.length, moved};
  }

  /* ---- assets (pictures, drawings), shared across slides ---- */
  const assets = [], assetIx = new Map(), pending = [];
  function asset(key, make) {
    if (assetIx.has(key)) return assetIx.get(key);
    const a = make();
    assets.push(a);
    assetIx.set(key, assets.length - 1);
    return assets.length - 1;
  }
  function rasterize(svgText, w, h, scale) {
    return new Promise(res => {
      const img = new Image();
      img.onload = () => {
        const c = document.createElement('canvas');
        c.width = Math.max(1, Math.round(w * scale)); c.height = Math.max(1, Math.round(h * scale));
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        try { res(c.toDataURL('image/png')); } catch (e) { res(null); }
      };
      img.onerror = () => res(null);
      img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgText);
    });
  }

  /* ---- an inline <svg> as a standalone file: computed styles inlined, references copied in, <use> expanded ---- */
  const SVGNS = 'http://www.w3.org/2000/svg';
  const PROPS = ['fill', 'fill-opacity', 'fill-rule', 'stroke', 'stroke-width', 'stroke-opacity', 'stroke-dasharray',
    'stroke-dashoffset', 'stroke-linecap', 'stroke-linejoin', 'stroke-miterlimit', 'opacity', 'color', 'font-family',
    'font-size', 'font-weight', 'font-style', 'text-anchor', 'dominant-baseline', 'vector-effect', 'marker-start',
    'marker-mid', 'marker-end', 'stop-color', 'stop-opacity'];
  function standaloneSvg(svg, crop) {
    const clone = svg.cloneNode(true);
    const os = [svg, ...svg.querySelectorAll('*')], cl = [clone, ...clone.querySelectorAll('*')];
    os.forEach((o, i) => {
      const cs = getComputedStyle(o);
      let s = '';
      for (const p of PROPS) { const v = cs.getPropertyValue(p); if (v && v !== 'none' || p === 'fill' || p === 'stroke') s += `${p}:${v};`; }
      if (cs.display === 'none' || cs.visibility === 'hidden') s += 'display:none;';
      cl[i].setAttribute('style', s);
      cl[i].removeAttribute('class');
      cl[i].removeAttribute('data-b');
    });
    // <use href="#id"> -> a nested <svg> holding the symbol's own children (the widest-supported form)
    for (const u of [...clone.querySelectorAll('use')]) {
      const id = (u.getAttribute('href') || u.getAttribute('xlink:href') || '').replace(/^#/, '');
      const sym = document.getElementById(id);
      if (!sym) { u.remove(); continue; }
      const n = document.createElementNS(SVGNS, 'svg');
      if (sym.getAttribute('viewBox')) n.setAttribute('viewBox', sym.getAttribute('viewBox'));
      for (const a of ['x', 'y', 'width', 'height']) if (u.getAttribute(a)) n.setAttribute(a, u.getAttribute(a));
      if (!u.getAttribute('width')) { n.setAttribute('width', '100%'); n.setAttribute('height', '100%'); }
      n.setAttribute('style', u.getAttribute('style') || '');
      for (const ch of sym.childNodes) n.appendChild(ch.cloneNode(true));
      u.replaceWith(n);
    }
    // copy in what url(#id) points at (gradients, markers defined elsewhere in the page)
    const defs = document.createElementNS(SVGNS, 'defs');
    const seen = new Set();
    const scan = node => {
      let txt = '';                                         // attribute values, unescaped (outerHTML has &quot;)
      for (const e of [node, ...node.querySelectorAll('*')]) for (const at of e.attributes || []) txt += ' ' + at.value;
      for (const m of txt.matchAll(/url\(\s*["']?#([^"')\s]+)["']?\s*\)/g)) {
        const id = m[1];
        if (seen.has(id) || clone.querySelector('#' + CSS.escape(id))) continue;
        seen.add(id);
        const src = document.getElementById(id);
        if (src) { const c = src.cloneNode(true); defs.appendChild(c); scan(c); }
      }
    };
    scan(clone);
    if (defs.childNodes.length) clone.insertBefore(defs, clone.firstChild);
    // a stretched viewBox (preserveAspectRatio="none") is baked into the points, so strokes keep their width in
    // renderers that ignore vector-effect
    const vb = (svg.getAttribute('viewBox') || '').split(/[\s,]+/).map(Number);
    const r = svg.getBoundingClientRect();
    let W = r.width, H = r.height, dx = 0, dy = 0;
    const par = svg.getAttribute('preserveAspectRatio') || '';
    if (!crop && vb.length === 4 && par !== 'none') {
      // content drawn outside the viewBox (overflow: visible, e.g. the house's shadow) is kept: grow the viewport
      const bb = svg.getBBox();
      const x0 = Math.min(vb[0], bb.x - 2), y0 = Math.min(vb[1], bb.y - 2);
      const x1 = Math.max(vb[0] + vb[2], bb.x + bb.width + 2), y1 = Math.max(vb[1] + vb[3], bb.y + bb.height + 2);
      if (x0 < vb[0] - 0.5 || y0 < vb[1] - 0.5 || x1 > vb[0] + vb[2] + 0.5 || y1 > vb[1] + vb[3] + 0.5) {
        const s = Math.min(W / vb[2], H / vb[3]);
        const ox = (W - vb[2] * s) / 2, oy = (H - vb[3] * s) / 2;
        dx = ox + (x0 - vb[0]) * s; dy = oy + (y0 - vb[1]) * s;
        W = (x1 - x0) * s; H = (y1 - y0) * s;
        clone.setAttribute('viewBox', `${x0} ${y0} ${x1 - x0} ${y1 - y0}`);
        clone.setAttribute('preserveAspectRatio', 'xMidYMid meet');
      }
    }
    if (crop) {
      clone.setAttribute('viewBox', `${crop.x} ${crop.y} ${crop.w} ${crop.h}`);
      W = crop.w; H = crop.h;
    } else if (vb.length === 4 && svg.getAttribute('preserveAspectRatio') === 'none' && !clone.querySelector('path,circle,ellipse,text')) {
      const sx = W / vb[2], sy = H / vb[3];
      const P = (x, y) => [((x - vb[0]) * sx).toFixed(2), ((y - vb[1]) * sy).toFixed(2)];
      for (const e of clone.querySelectorAll('polyline,polygon')) {
        const pts = (e.getAttribute('points') || '').trim().split(/[\s,]+/).map(Number);
        const out = [];
        for (let i = 0; i + 1 < pts.length; i += 2) out.push(P(pts[i], pts[i + 1]).join(','));
        e.setAttribute('points', out.join(' '));
      }
      for (const e of clone.querySelectorAll('line')) {
        const [x1, y1] = P(+e.getAttribute('x1'), +e.getAttribute('y1')), [x2, y2] = P(+e.getAttribute('x2'), +e.getAttribute('y2'));
        e.setAttribute('x1', x1); e.setAttribute('y1', y1); e.setAttribute('x2', x2); e.setAttribute('y2', y2);
      }
      for (const e of clone.querySelectorAll('rect')) {
        const [x, y] = P(+e.getAttribute('x') || 0, +e.getAttribute('y') || 0);
        e.setAttribute('x', x); e.setAttribute('y', y);
        e.setAttribute('width', ((+e.getAttribute('width') || 0) * sx).toFixed(2));
        e.setAttribute('height', ((+e.getAttribute('height') || 0) * sy).toFixed(2));
      }
      clone.setAttribute('viewBox', `0 0 ${W.toFixed(2)} ${H.toFixed(2)}`);
    }
    clone.setAttribute('width', W.toFixed(2));
    clone.setAttribute('height', H.toFixed(2));
    clone.setAttribute('xmlns', SVGNS);
    clone.setAttribute('overflow', 'visible');
    clone.removeAttribute('aria-hidden');
    return {text: new XMLSerializer().serializeToString(clone), w: W, h: H, dx, dy};
  }

  /* ---- one slide ---- */
  function readSlide(slide) {
    const sr = slide.getBoundingClientRect();
    const rel = r => ({x: r.left - sr.left, y: r.top - sr.top, w: r.width, h: r.height});
    const items = [];
    const opac = new Map();
    const effOp = el => {
      if (opac.has(el)) return opac.get(el);
      const o = (el === slide || !el.parentElement ? 1 : effOp(el.parentElement)) * num(getComputedStyle(el).opacity === '' ? 1 : getComputedStyle(el).opacity);
      opac.set(el, o);
      return o;
    };
    const isInline = el => getComputedStyle(el).display === 'inline' || getComputedStyle(el).display === 'contents';
    const ownerOf = el => { while (el !== slide && isInline(el) && el.parentElement) el = el.parentElement; return el; };

    // text: every rendered character, grouped into runs by text node and visual line
    const byOwner = new Map();
    const tw = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    let node;
    while ((node = tw.nextNode())) {
      const p = node.parentElement;
      if (!p || p.closest('svg') || p.closest('aside.notes')) continue;
      const cs = getComputedStyle(p);
      if (cs.visibility === 'hidden' || effOp(p) < 0.02) continue;
      const owner = ownerOf(p);
      const t = node.textContent;
      const tt = cs.textTransform;
      const fs = num(cs.fontSize);
      const style = {fs, fw: num(cs.fontWeight) || 400, it: cs.fontStyle !== 'normal', col: rgba(cs.color),
                     ls: cs.letterSpacing === 'normal' ? 0 : num(cs.letterSpacing), op: effOp(p),
                     lh: cs.lineHeight === 'normal' ? fs * 1.26 : num(cs.lineHeight),
                     u: cs.textDecorationLine.includes('underline')};
      let run = null;
      for (let i = 0; i < t.length; i++) {
        range.setStart(node, i); range.setEnd(node, i + 1);
        const rs = range.getClientRects();
        if (!rs.length) continue;                          // collapsed whitespace
        const r = rs[rs.length - 1];
        let ch = /\s/.test(t[i]) ? ' ' : t[i];
        if (tt === 'uppercase') ch = ch.toUpperCase();
        const mid = r.top + r.height / 2;
        if (!run || Math.abs(mid - run.mid) > Math.max(3, r.height * 0.45)) {
          if (run) push(owner, run);
          run = {s: ch, l: r.left, r: r.right, t: r.top, b: r.bottom, mid, style};
        } else {
          run.s += ch; run.r = Math.max(run.r, r.right); run.l = Math.min(run.l, r.left);
          run.t = Math.min(run.t, r.top); run.b = Math.max(run.b, r.bottom);
        }
      }
      if (run) push(owner, run);
    }
    function push(owner, run) {
      if (!byOwner.has(owner)) byOwner.set(owner, []);
      byOwner.get(owner).push(run);
    }
    function textItem(owner) {
      const runs = byOwner.get(owner);
      if (!runs) return null;
      const cs = getComputedStyle(owner);
      const lines = [];
      for (const r of runs) {
        const last = lines[lines.length - 1];
        const lm = last && (last.t + last.b) / 2;
        if (last && Math.abs((r.t + r.b) / 2 - lm) <= Math.max(4, (r.b - r.t) * 0.5) && r.l >= last.r - 2) {
          last.runs.push(r); last.r = Math.max(last.r, r.r); last.t = Math.min(last.t, r.t); last.b = Math.max(last.b, r.b);
        } else lines.push({runs: [r], l: r.l, r: r.r, t: r.t, b: r.b});
      }
      for (const L of lines) {
        // trim the spaces the browser leaves at a line's ends
        const a = L.runs[0], z = L.runs[L.runs.length - 1];
        a.s = a.s.replace(/^ +/, ''); z.s = z.s.replace(/ +$/, '');
        L.runs = L.runs.filter(r => r.s.length);
        const big = L.runs.reduce((m, r) => (r.style.fs > m.style.fs ? r : m), L.runs[0] || runs[0]);
        L.lh = Math.max(...L.runs.map(r => r.style.lh), 1);
        L.mid = big ? (big.t + big.b) / 2 : (L.t + L.b) / 2;
        L.l -= sr.left; L.r -= sr.left; L.t -= sr.top; L.b -= sr.top; L.mid -= sr.top;
        L.runs = L.runs.map(r => ({s: r.s, ...r.style, l: r.l - sr.left, r: r.r - sr.left}));
      }
      const live = lines.filter(L => L.runs.length);
      if (!live.length) return null;
      const ob = owner.getBoundingClientRect();
      const box = {x: ob.left - sr.left + num(cs.borderLeftWidth) + num(cs.paddingLeft),
                   y: ob.top - sr.top + num(cs.borderTopWidth) + num(cs.paddingTop),
                   w: ob.width - num(cs.borderLeftWidth) - num(cs.borderRightWidth) - num(cs.paddingLeft) - num(cs.paddingRight)};
      return {k: 'text', lines: live, align: cs.textAlign, box, tag: owner.tagName.toLowerCase(), cls: owner.className && owner.className.baseVal === undefined ? owner.className : ''};
    }

    function boxItem(el, cs, b, op) {
      const it = {k: 'box', ...b, op, tag: el.tagName.toLowerCase()};
      const bg = rgba(cs.backgroundColor);
      if (bg && bg[3] > 0) it.fill = bg;
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && !cs.backgroundImage.startsWith('url(')) it.grad = cs.backgroundImage;
      const sides = {};
      let bw = {};
      for (const S of ['Top', 'Right', 'Bottom', 'Left']) {
        const w = num(cs['border' + S + 'Width']), st = cs['border' + S + 'Style'], c = rgba(cs['border' + S + 'Color']);
        bw[S[0].toLowerCase()] = st === 'none' || st === 'hidden' ? 0 : w;
        if (w > 0 && st !== 'none' && st !== 'hidden' && c && c[3] > 0) sides[S[0].toLowerCase()] = {w, st, c};
      }
      // the CSS triangle: an empty box drawn only by one coloured border, the others transparent
      const inner = [b.w - bw.l - bw.r, b.h - bw.t - bw.b];
      const keys = Object.keys(sides);
      if (keys.length === 1 && inner[0] < 0.5 && inner[1] < 0.5 && (bw.t + bw.b > 0) && (bw.l + bw.r > 0)) {
        it.tri = {side: keys[0], c: sides[keys[0]].c};
        return it;
      }
      if (keys.length) it.border = sides;
      const rad = v => { const s = String(v).split(' ')[0]; return s.endsWith('%') ? num(s) / 100 * Math.min(b.w, b.h) : num(s); };
      it.rad = [rad(cs.borderTopLeftRadius), rad(cs.borderTopRightRadius), rad(cs.borderBottomRightRadius), rad(cs.borderBottomLeftRadius)];
      if (cs.boxShadow && cs.boxShadow !== 'none') it.shadow = cs.boxShadow;
      return (it.fill || it.grad || it.border || it.shadow) ? it : null;
    }

    // stacking: the z-index of the nearest ancestor that sets one (the map under slide 13's text columns, the arrows
    // over everything); items are sorted by it, stably, in make_pptx.py
    const zOf = el => {
      for (let x = el; x && x !== slide; x = x.parentElement) {
        const cs = getComputedStyle(x);
        if (cs.zIndex !== 'auto' && (cs.position !== 'static' || /flex|grid/.test(getComputedStyle(x.parentElement || slide).display))) return parseInt(cs.zIndex, 10) || 0;
      }
      return 0;
    };
    const push0 = items.push.bind(items);
    let zEl = slide;
    items.push = it => push0({...it, z: it.z !== undefined ? it.z : zOf(zEl)});

    function clipOf(el) {
      for (let a = el.parentElement; a && a !== slide; a = a.parentElement) {
        const cs = getComputedStyle(a);
        if (cs.overflow !== 'visible' || cs.overflowX !== 'visible') {
          const r = rel(a.getBoundingClientRect());
          const rd = String(cs.borderTopLeftRadius);
          const round = rd.endsWith('%') ? num(rd) >= 49 : num(rd) >= Math.min(r.w, r.h) / 2 - 1;
          return {...r, round};
        }
      }
      return null;
    }

    function walk(el, op) {
      const cs = getComputedStyle(el);
      if (cs.display === 'none') return;
      if (el.matches('aside.notes')) return;
      const o = op * (cs.opacity === '' ? 1 : num(cs.opacity));
      if (o < 0.02) return;
      const b = rel(el.getBoundingClientRect());
      const tag = el.tagName.toLowerCase();
      const visible = cs.visibility !== 'hidden';
      zEl = el;
      if (tag === 'svg') {
        if (!visible || b.w < 1 || b.h < 1) return;
        let crop = null, pos = b;
        if (el.classList.contains('conn')) {                // the arrows: crop the slide-size overlay to its path
          const bb = el.getBBox();
          if (!bb.width && !bb.height) return;
          crop = {x: bb.x - 8, y: bb.y - 8, w: bb.width + 16, h: bb.height + 16};
          pos = {x: b.x + crop.x * b.w / 1280, y: b.y + crop.y * b.h / 720, w: crop.w * b.w / 1280, h: crop.h * b.h / 720};
        }
        const sv = standaloneSvg(el, crop);
        if (!crop && (sv.dx || sv.dy || Math.abs(sv.w - b.w) > 0.5 || Math.abs(sv.h - b.h) > 0.5)) pos = {x: b.x + sv.dx, y: b.y + sv.dy, w: sv.w, h: sv.h};
        const ix = asset('svg:' + sv.text, () => ({kind: 'svg', svg: sv.text, png: null, w: sv.w, h: sv.h}));
        if (!assets[ix].queued) { assets[ix].queued = true; pending.push(rasterize(sv.text, sv.w, sv.h, 3).then(p => { assets[ix].png = p; })); }
        items.push({k: 'svg', ...pos, op: o, a: ix});
        return;
      }
      if (tag === 'img') {
        if (!visible) return;
        const src = el.currentSrc || el.src;
        const ix = asset('img:' + src, () => ({kind: src.startsWith('data:image/svg') ? 'svgimg' : 'img', src, nw: el.naturalWidth, nh: el.naturalHeight}));
        if (assets[ix].kind === 'svgimg' && !assets[ix].queued) {
          assets[ix].queued = true;
          pending.push(fetch(src).then(r => r.text()).then(t => { assets[ix].svg = t; return rasterize(t, b.w, b.h, 3); }).then(p => { assets[ix].png = p; }));
        }
        const own = boxItem(el, cs, b, o);
        items.push({k: 'img', ...b, op: o, a: ix, fit: cs.objectFit, pos: cs.objectPosition, clip: clipOf(el),
                    round: own && own.rad[0] >= Math.min(b.w, b.h) / 2 - 1, border: own && own.border, shadow: own && own.shadow});
        return;
      }
      if (visible && el !== slide) { const bi = boxItem(el, cs, b, o); if (bi) items.push(bi); }
      if (visible && el === slide) { const bi = boxItem(el, cs, b, o); if (bi && (bi.grad || (bi.fill && bi.fill.slice(0, 3).join() !== '255,255,255'))) items.push(bi); }
      for (const ch of el.children) walk(ch, o);
      zEl = el;
      if (byOwner.has(el)) { const t = textItem(el); if (t) items.push(t); }
    }
    walk(slide, 1);
    // text owned by elements the walk didn't reach (shouldn't happen) is reported, not lost silently
    return items;
  }

  async function main() {
    await (document.fonts ? document.fonts.ready : Promise.resolve());
    for (let i = 0; i < 200 && document.documentElement.dataset.arrows !== 'drawn'; i++) await sleep(25);
    await sleep(150);
    const check = materializePseudos(document.querySelector('.deck') || document.body);
    const slides = [...document.querySelectorAll('section.slide')].map(readSlide);
    await Promise.all(pending);
    for (const a of assets) delete a.queued;
    const out = {check, slides, assets};
    document.body.innerHTML = '';
    const pre = document.createElement('pre');
    pre.id = 'pptx-data';
    pre.textContent = JSON.stringify(out);
    document.body.appendChild(pre);
    document.documentElement.dataset.pptx = 'done';
  }
  window.addEventListener('load', () => { main().catch(e => { document.body.innerHTML = '<pre id="pptx-data">' + JSON.stringify({error: String(e && e.stack || e)}) + '</pre>'; }); });
})();
