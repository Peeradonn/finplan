"""The deck's one decorative idea (Pete, 23 Oct): "Built to Last" drawn as a house from the written case's pillars.

  the roof        what passes on (slide 12)
  the rooms       a place for every voice: Call 4 (left), Call 5 (right)
  the walls       income that lasts: Call 2 (left), Call 3 (right)
  the foundation  protected first: Call 1

house(state, size, labels) returns inline SVG. state maps a part ("1".."5", "roof") to "on" (the accent: this slide's
part), "done" (wine: built on an earlier slide) or "todo" (dashed rose: still to come); parts not named are "todo".
The slides carry the generated markup; rerun this file's main to print it after a change.
"""

PARTS = {  # viewBox 0 0 440 400
    "roof": ("poly", "30,150 220,18 410,150"),
    "4": ("rect", (46, 156, 171, 86)), "5": ("rect", (223, 156, 171, 86)),
    "2": ("rect", (46, 248, 171, 86)), "3": ("rect", (223, 248, 171, 86)),
    "1": ("rect", (24, 340, 392, 44)),
}
NAMES = {"1": ("1", "Insure the income"), "2": ("2", "Home and business"), "3": ("3", "Fix the cost"),
         "4": ("4", "A plan each"), "5": ("5", "Values and crypto"), "roof": ("", "What passes on")}
FILL = {"on": ("#A81E2D", "none", "#fff"), "done": ("#7D1D2A", "none", "#fff"), "todo": ("#fff", "#D3A6AD", "#B5979D"),
        "all": ("#7D1D2A", "none", "#fff")}
# the small title houses, in slide 4's line style (23 Oct): this call solid crimson, built parts rose, the rest dashed
LINE = {"on": ("#A81E2D", "#A81E2D", "solid"), "done": ("#E8DEDC", "#A81E2D", "solid"), "todo": ("#FFFFFF", "#D3A6AD", "dash")}


def house(state=None, w=72, labels=False, cls="house", steps=None):
    """steps maps a part to its build step: the part and its labels appear in that step (data-b)."""
    state, steps = state or {}, steps or {}
    out = [f'<svg class="{cls}" viewBox="0 0 440 400" width="{w}" height="{round(w * 400 / 440)}" aria-hidden="true">']
    for part, (kind, geo) in PARTS.items():
        fill, stroke, ink = FILL[state.get(part, "todo")]
        out.append(f'<g data-b="{steps[part]}">' if part in steps else "<g>")
        dash = ' stroke-dasharray="10 8"' if stroke != "none" else ""
        sw = 6 if stroke != "none" else 0
        if kind == "poly":
            out.append(f'<polygon points="{geo}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
            cx, cy = 220, 112
        else:
            x, y, ww, hh = geo
            out.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>')
            cx, cy = x + ww / 2, y + hh / 2
        if labels:
            num, name = NAMES[part]
            if part == "1":   # the foundation is shallow: number and name on one line
                out.append(f'<text x="{cx}" y="{cy + 7}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}"><tspan font-family="Plus Jakarta Sans, Arial, sans-serif" '
                           f'font-size="24">{num}</tspan>   {name}</text>')
            elif num:
                out.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" '
                           f'font-weight="600" font-size="30" fill="{ink}">{num}</text>')
                out.append(f'<text x="{cx}" y="{cy + 24}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}">{name}</text>')
            else:
                out.append(f'<text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" '
                           f'font-weight="600" font-size="17" fill="{ink}">{name}</text>')
        out.append("</g>")
    out.append("</svg>")
    return "".join(out)


def progress(call, w=76):
    """The small house beside a call slide's title: earlier calls built (rose), this one lit (crimson), the rest to come
    (dashed), drawn in slide 4's line style."""
    st = {str(k): "done" for k in range(1, call)}
    st[str(call)] = "on"
    o = [f'<svg class="house mini" viewBox="0 0 440 400" width="{w}" height="{round(w * 400 / 440)}" aria-hidden="true">']
    for part, (kind, geo) in PARTS.items():
        fill, stroke, style = LINE[st.get(part, "todo")]
        extra = ' stroke-dasharray="14 10"' if style == "dash" else ""
        attrs = f'fill="{fill}" stroke="{stroke}" stroke-width="10" stroke-linejoin="round"{extra}'
        if kind == "poly":
            o.append(f'<polygon points="{geo}" {attrs}/>')
        else:
            x, y, ww, hh = geo
            o.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" {attrs}/>')
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    for c in range(1, 6):
        print(c, progress(c)[:80], "...")


def _mix(hex_, other, f):
    a = [int(hex_[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(other[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * f):02X}" for x, y in zip(a, b))


# slide 4's exploded house (24 Oct): each layer a colour, darkest at the base, shaded top / front-left / front-right
LAYER = {"1": "#7D1D2A", "2": "#A35560", "3": "#A35560", "4": "#C48C93", "5": "#C48C93", "roof": "#D9C3C6"}
# the same house in light tones, for slide 4 drawn on a dark wine stage (24 Oct): the base a little deeper, the roof white
LAYER_LIGHT = {"1": "#D9AEB4", "2": "#E9CDD1", "3": "#E9CDD1", "4": "#F3E2E4", "5": "#F3E2E4", "roof": "#FFFFFF"}
ICON = {"1": "shield-check", "2": "house", "3": "heart-pulse", "4": "users", "5": "leaf", "roof": "gift"}
CALLOUTS = {   # part: (side, title, line)
    "roof": ("r", "What passes on", "the inheritance kept, passed on in stages"),
    "5": ("r", "Values and crypto, with guardrails", "ESG at 25%; crypto sized per person"),
    "3": ("r", "Fix the cost the budget ignores", "a medical review at 75; spending rules"),
    "4": ("l", "A plan for each person", "Chloe funded; HK$45K a year less in fees"),
    "2": ("l", "The home and the business", "decided at 65, not forced at {{own_sale_age}}"),
    "1": ("l", "Insure the income, not the life", "about HK$100K a year closes every gap"),
}


def exploded(W=176, D=132, hf=18, hw=58, rh=52, gap=24, gx=6, ov=12, c=0.90, s=0.34, low=362, box=(1184, 372),
             palette="deck"):
    """Slide 4 (Pete, 24 Oct: the elevation was too simple): the house as an exploded 3D model, the foundation, two
    floors of two blocks and the roof pulled apart, so it reads as built from parts. A flat dimetric view (x to the
    right-front, y to the left-front, z up) keeps the walls tall; each floating layer casts a soft shadow on the one below;
    windows and a door make it a house; the roof overhangs. Each part is a group (class "hq", its build step in data-b:
    Call 1 = 2 ... Call 5 = 6, the roof = 7) with shaded faces (classes t, l, r), so the frame where it is named can light it
    crimson in CSS while windows keep their tone. Returns the markup for slide 4's .x4e box (drawing, leader lines,
    callouts: calls 1, 2, 4 left; 3, 5 and the roof right) and the anchors."""
    zf = (0, hf)
    z2 = (hf + gap, hf + gap + hw)
    z3 = (z2[1] + gap, z2[1] + gap + hw)
    zr = z3[1] + gap
    half = W / 2
    cx = box[0] / 2 - (W - D) * c / 2
    # centre the drawing vertically: from the roof's ridge (at the back) to the foundation's front corner
    top = (half - ov) * s - (zr + rh)
    bottom = (W + D + 16) * s
    base = (box[1] - 26 - (bottom - top)) / 2 - top

    def XY(x, y, z):
        return cx + (x - y) * c, base + (x + y) * s - z

    def P(*pts):
        return " ".join(f"{XY(*q)[0]:.1f},{XY(*q)[1]:.1f}" for q in pts)

    layer = LAYER_LIGHT if palette == "light" else LAYER

    def edge(col):
        return _mix(col, "#000000", .32 if palette != "light" else .30)

    steps = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "roof": 7}
    blocks = {"1": (-8, W + 8, -8, D + 8, zf), "2": (0, half - gx / 2, 0, D, z2), "3": (half + gx / 2, W, 0, D, z2),
              "4": (0, half - gx / 2, 0, D, z3), "5": (half + gx / 2, W, 0, D, z3)}
    # windows: (face, u0, u1, v0, v1) in metres-like units along the face; "L" = the front-left face (y = y1), "R" =
    # the front-right face (x = x1); a door is a window that starts at the floor
    holes = {"2": [("L", 30, 46, 0, 36), ("L", 56, 80, 20, 42)],
             "3": [("L", 14, 42, 20, 42), ("R", 20, 48, 20, 42), ("R", 64, 92, 20, 42)],
             "4": [("L", 30, 52, 20, 42), ("L", 60, 80, 20, 42)],
             "5": [("L", 14, 42, 20, 42), ("R", 20, 48, 20, 42), ("R", 64, 92, 20, 42)]}
    o = [f'<svg class="hx" viewBox="0 0 {box[0]} {box[1]}" aria-hidden="true">']
    gx0, gy0 = XY(W / 2, D / 2, 0)
    o.append(f'<ellipse cx="{gx0:.1f}" cy="{gy0 + 14:.1f}" rx="{(W + D) * c * 0.62:.1f}" ry="{(W + D) * s * 0.5:.1f}" fill="#1B1716" opacity=".07"/>')
    anchors = {}
    below = {"2": "1", "3": "1", "4": "2", "5": "3"}
    for part in ("1", "2", "3", "4", "5"):
        x0, x1, y0, y1, (za, zb) = blocks[part]
        col = layer[part]
        o.append(f'<g class="hq" data-b="{steps[part]}">')
        if part in below:      # the soft shadow this floating block casts on the layer below
            lz = blocks[below[part]][4][1]
            o.append(f'<polygon points="{P((x0, y0, lz), (x1, y0, lz), (x1, y1, lz), (x0, y1, lz))}" fill="#1B1716" opacity=".16"/>')
        e = edge(col)
        o.append(f'<polygon class="t" points="{P((x0, y0, zb), (x1, y0, zb), (x1, y1, zb), (x0, y1, zb))}" fill="{_mix(col, "#FFFFFF", .30)}" stroke="{e}" stroke-width=".8"/>')
        o.append(f'<polygon class="l" points="{P((x0, y1, za), (x1, y1, za), (x1, y1, zb), (x0, y1, zb))}" fill="{col}" stroke="{e}" stroke-width=".8"/>')
        o.append(f'<polygon class="r" points="{P((x1, y0, za), (x1, y1, za), (x1, y1, zb), (x1, y0, zb))}" fill="{_mix(col, "#000000", .20)}" stroke="{e}" stroke-width=".8"/>')
        for face, u0, u1, v0, v1 in holes.get(part, []):
            if palette == "light":   # on light walls the windows read darker, like glass at dusk
                glass = _mix(col, "#7D1D2A", .42) if face == "L" else _mix(col, "#7D1D2A", .52)
            else:
                glass = _mix(col, "#FFFFFF", .62) if face == "L" else _mix(col, "#FFFFFF", .42)
            if face == "L":
                q = ((x0 + u0, y1, za + v0), (x0 + u1, y1, za + v0), (x0 + u1, y1, za + v1), (x0 + u0, y1, za + v1))
            else:
                q = ((x1, y1 - u0, za + v0), (x1, y1 - u1, za + v0), (x1, y1 - u1, za + v1), (x1, y1 - u0, za + v1))
            o.append(f'<polygon class="w" points="{P(*q)}" fill="{glass}" stroke="{e}" stroke-width=".8"/>')
        # the number at the face's outer edge, so its leader line leaves the model at once
        if part == "1":
            ax, ay = XY(x0 + 22, y1, (za + zb) / 2)
        elif part in ("2", "4"):
            ax, ay = XY(x0 + 14, y1, za + hw * 0.5)
        else:
            ax, ay = XY(x1, 16, za + hw * 0.5)
        anchors[part] = (ax, ay)
        r, fs = (10, 13) if part == "1" else (13, 16)
        o.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="{r}" fill="#FFFFFF" stroke="{e}" stroke-width=".8"/>'
                 f'<text x="{ax:.1f}" y="{ay + fs * 0.36:.1f}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" '
                 f'font-weight="700" font-size="{fs}" fill="#1B1716">{part}</text></g>')
    # the roof: a gable along the depth, overhanging the walls, its triangle facing front-left; it casts a shadow too
    col, e = layer["roof"], edge(layer["roof"])
    lz = z3[1]
    x0, x1, y0, y1 = -ov, W + ov, -ov, D + ov
    o.append(f'<g class="hq" data-b="7">'
             f'<polygon points="{P((0, 0, lz), (W, 0, lz), (W, D, lz), (0, D, lz))}" fill="#1B1716" opacity=".16"/>'
             f'<polygon class="t" points="{P((x0, y0, zr), (x0, y1, zr), (half, y1, zr + rh), (half, y0, zr + rh))}" fill="{_mix(col, "#FFFFFF", .40)}" stroke="{e}" stroke-width=".8"/>'
             f'<polygon class="r" points="{P((half, y0, zr + rh), (half, y1, zr + rh), (x1, y1, zr), (x1, y0, zr))}" fill="{_mix(col, "#000000", .16)}" stroke="{e}" stroke-width=".8"/>'
             f'<polygon class="l" points="{P((x0, y1, zr), (x1, y1, zr), (half, y1, zr + rh))}" fill="{col}" stroke="{e}" stroke-width=".8"/>'
             f'<polygon class="w" points="{P((half - 14, y1, zr + 10), (half + 14, y1, zr + 10), (half + 14, y1, zr + 30), (half - 14, y1, zr + 30))}" fill="{_mix(col, "#7D1D2A", .40) if palette == "light" else _mix(col, "#FFFFFF", .55)}" stroke="{e}" stroke-width=".8"/>'
             f'</g>')
    tr = 0.55                     # a point on the right slope, between the ridge and the eave, near the back
    anchors["roof"] = XY(half + tr * (W + ov - half), 4, zr + rh * (1 - tr))
    edgex = {"l": 362, "r": 822}
    for part, (side, _, _) in CALLOUTS.items():
        ax, ay = anchors[part]
        x2 = edgex[side]
        o.append(f'<g class="ld" data-b="{steps[part]}"><line x1="{ax:.1f}" y1="{ay:.1f}" x2="{x2}" y2="{ay:.1f}" stroke="#D3A6AD" stroke-width="1.5"/>'
                 f'<circle cx="{x2}" cy="{ay:.1f}" r="3" fill="#A81E2D"/></g>')
    o.append("</svg>")
    for part, (side, title, line) in CALLOUTS.items():
        ay = anchors[part][1]
        pos = "right:834px" if side == "l" else "left:834px"
        num = "" if part == "roof" else f'<em>{part}</em>'
        icon = f'<span class="ci"><svg class="ic"><use href="#i-{ICON[part]}"/></svg></span>'
        text = f'<div><b>{num}{title}</b><p>{line}</p></div>'
        inner = text + icon if side == "l" else icon + text      # the icon sits nearest the leader line
        o.append(f'<div class="co {side}" data-b="{steps[part]}" style="{pos};top:{ay:.0f}px">{inner}</div>')
    return "\n    ".join(o), anchors


def progress3d(call, w=66, W=176, D=132, hf=18, hw=58, rh=52, gap=12, gx=6, ov=12, c=0.90, s=0.34):
    """The small house beside a call slide's title, as slide 4's 3D model in miniature (24 Oct, Pete): earlier calls built
    in the house's colours, this call crimson, the calls still to come (and the roof, slide 12) as dashed ghosts. White
    seams between the faces keep it crisp at icon size. call=6 is slide 12: every call built, the roof
    (what passes on) crimson."""
    st = {str(k): "done" for k in range(1, call)}
    st[str(call)] = "on"
    zf = (0, hf)
    z2 = (hf + gap, hf + gap + hw)
    z3 = (z2[1] + gap, z2[1] + gap + hw)
    zr = z3[1] + gap
    half = W / 2

    def XY(x, y, z):
        return (x - y) * c, (x + y) * s - z

    blocks = {"1": (-8, W + 8, -8, D + 8, zf), "2": (0, half - gx / 2, 0, D, z2), "3": (half + gx / 2, W, 0, D, z2),
              "4": (0, half - gx / 2, 0, D, z3), "5": (half + gx / 2, W, 0, D, z3)}
    CRIMSON = ("#C9505D", "#A81E2D", "#7A1622")
    faces = []        # (points, fill, stroke, dashed)

    def add(pts, state, shade, col):
        if state == "todo":
            faces.append((pts, "#FFFFFF", "#D3A6AD", True))
        elif state == "on":
            faces.append((pts, CRIMSON[shade], "#FFFFFF", False))
        else:
            fill = (_mix(col, "#FFFFFF", .30), col, _mix(col, "#000000", .20))[shade]
            faces.append((pts, fill, "#FFFFFF", False))

    for part in ("1", "2", "3", "4", "5"):
        x0, x1, y0, y1, (za, zb) = blocks[part]
        state, col = st.get(part, "todo"), LAYER[part]
        add([(x0, y0, zb), (x1, y0, zb), (x1, y1, zb), (x0, y1, zb)], state, 0, col)
        add([(x0, y1, za), (x1, y1, za), (x1, y1, zb), (x0, y1, zb)], state, 1, col)
        add([(x1, y0, za), (x1, y1, za), (x1, y1, zb), (x1, y0, zb)], state, 2, col)
    x0, x1, y0, y1 = -ov, W + ov, -ov, D + ov
    roof = "on" if call >= 6 else "todo"
    add([(x0, y0, zr), (x0, y1, zr), (half, y1, zr + rh), (half, y0, zr + rh)], roof, 0, LAYER["roof"])
    add([(half, y0, zr + rh), (half, y1, zr + rh), (x1, y1, zr), (x1, y0, zr)], roof, 2, LAYER["roof"])
    add([(x0, y1, zr), (x1, y1, zr), (half, y1, zr + rh)], roof, 1, LAYER["roof"])
    pts2 = [[XY(*q) for q in f[0]] for f in faces]
    xs = [p[0] for f in pts2 for p in f]
    ys = [p[1] for f in pts2 for p in f]
    pad = 6
    vx, vy = min(xs) - pad, min(ys) - pad
    vw, vh = max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad
    o = [f'<svg class="house mini" viewBox="{vx:.0f} {vy:.0f} {vw:.0f} {vh:.0f}" width="{w}" height="{round(w * vh / vw)}" aria-hidden="true">']
    for (pts, fill, stroke, dashed), q in zip(faces, pts2):
        dash = ' stroke-dasharray="12 8"' if dashed else ""
        sw = 4 if dashed else 3
        o.append(f'<polygon points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in q)}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sw}" stroke-linejoin="round"{dash}/>')
    o.append("</svg>")
    return "".join(o)


def elevation(w=360):
    """Slide 4: the house drawn as an architect's elevation (Pete chose it, 23 Oct): fine crimson lines, light rose fills,
    the foundation hatched like concrete, one ground line, each part numbered. Each part is a group with its build step
    (data-b: Call 1 = step 2 ... Call 5 = step 6, the roof = 7) and class "hq", so the frame where it is named can fill it
    crimson (CSS), and the final slide shows it whole."""
    steps = {"1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "roof": 7}
    o = [f'<svg class="house elev" viewBox="-60 0 560 410" width="{w}" height="{round(w * 410 / 560)}" aria-hidden="true">',
         '<defs><pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<rect width="12" height="12" fill="#F8EFF0"/><line x1="0" y1="0" x2="0" y2="12" stroke="#D3A6AD" stroke-width="3"/>'
         '</pattern></defs>',
         '<line x1="-10" y1="386" x2="450" y2="386" stroke="#80606A" stroke-width="2.5"/>']
    for part, (kind, geo) in PARTS.items():
        fill = "url(#hatch)" if part == "1" else ("#F8EFF0" if part == "roof" else "#FBF4F5")
        o.append(f'<g class="hq" data-b="{steps[part]}">')
        if kind == "poly":
            o.append(f'<polygon points="{geo}" fill="{fill}" stroke="#A81E2D" stroke-width="3" stroke-linejoin="round"/>')
            cx, cy = 220, 108
        else:
            x, y, ww, hh = geo
            o.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{fill}" stroke="#A81E2D" stroke-width="3"/>')
            cx, cy = x + ww / 2, y + hh / 2
        num = "" if part == "roof" else part
        if num:
            o.append(f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" font-weight="600" '
                     f'font-size="{30 if part == "1" else 40}" fill="#A81E2D">{num}</text>')
        o.append("</g>")
    o.append("</svg>")
    return "".join(o)
