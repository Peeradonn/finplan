"""The prism strips: slide 13's beam (Pete chose option B, 15 Nov) and the same picture at the foot of every step slide
(Pete, 15 Nov, later: "the prism like slide 13"; "still show [the other bands], just highlight different parts").
The close: the five rays recombine through an apex-down prism into one white beam that carries the verdict, the
reverse of slide 2. A step slide: the same prism and beam, all five bands coming in, its own step's band lit and the
others dimmed.

  .venv/Scripts/python.exe Final/looks/close_beam_art.py
  # writes Final/deck/img/close-beam.png (all five lit, transparent: it sits on slide 13's stage; 1280 x 84 CSS px,
  #        the beam at y = 43) and Final/deck/img/strip-<P|R|I|S|M>.png (one band lit, opaque: the stage colour baked
  #        in for the white slides; 1280 x 104 CSS px, the prism 10 px lower so the verdict above the beam and the
  #        sources below it are balanced: verdict 14-42, beam 53, sources 70-84)

PNGs, not inline SVG, because PowerPoint drops SVG filters (the glow). The colours are slide 2's rays
(prism_stage_art.py ROWS). The beam ends at x = 1190, short of the page number.
"""
import os
import subprocess
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), "deck", "img")
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
COL = ["#F4B740", "#FF4A57", "#3CC8E6", "#9B7BFF", "#E6E9EE"]     # P R I S M, as slide 2
W, SCALE = 1280, 3
BEAM_TO = 1190
DIM = .26                                                        # the other bands on a step slide: present, not lit
STAGE = ("#2C2378", "#1A1550")   # the step strip, top to bottom: the deck's deep indigo (--brand-deep #231C5E, the
                                 # conclusion bar's colour, Pete 14 Nov), so it belongs to the white slide; the navy
                                 # ("#101B36", "#080E1E") read as a separate slab (15 Nov, rendered side by side)
pt = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)
along = lambda p, q, t: (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
chrome = next(c for c in CHROME if os.path.exists(c))


def draw(lit, opaque, H=84, dy=0, stage=STAGE):
    """lit: the bands at full strength (0-4, P to M), the others dimmed; opaque: bake the stage in; dy: move the
    prism and rays down (the close's geometry has dy = 0)."""
    lit = list(lit)
    a = lambda i: 1 if i in lit else DIM
    YS = [y + dy for y in (12, 27, 42, 57, 72)]                  # where each ray enters from the slide's edge
    TL, TR, AP = (112, 6 + dy), (176, 6 + dy), (144, 78 + dy)    # the prism, apex down (slide 2's is apex up)
    XIN = [along(TL, AP, t) for t in (.22, .34, .46, .58, .70)]  # each colour meets the left face
    EX = along(TR, AP, .52)                                      # one beam leaves the right face
    d = [f'<filter id="g" filterUnits="userSpaceOnUse" x="-40" y="-40" width="{W + 80}" height="{H + 80}">'
         '<feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
         f'<linearGradient id="beam" gradientUnits="userSpaceOnUse" x1="{EX[0]}" y1="0" x2="{BEAM_TO}" y2="0">'
         '<stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/><stop offset=".35" stop-color="#FFFFFF" stop-opacity=".85"/>'
         '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".3"/></linearGradient>',
         '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".22"/>'
         '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".04"/></linearGradient>',
         f'<linearGradient id="stage" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{stage[0]}"/>'
         f'<stop offset="1" stop-color="{stage[1]}"/></linearGradient>']
    for i in range(5):
        c, k = COL[i], a(i)
        d.append(f'<linearGradient id="r{i}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{XIN[i][0]}" y2="0">'
                 f'<stop offset="0" stop-color="{c}" stop-opacity="{.25 * k:.3f}"/><stop offset=".5" stop-color="{c}" stop-opacity="{.85 * k:.3f}"/>'
                 f'<stop offset="1" stop-color="{c}" stop-opacity="{k:.3f}"/></linearGradient>')
        d.append(f'<linearGradient id="f{i}" gradientUnits="userSpaceOnUse" x1="{XIN[i][0]}" y1="{XIN[i][1]}" x2="{EX[0]}" y2="{EX[1]}">'
                 f'<stop offset="0" stop-color="{c}" stop-opacity="{.95 * k:.3f}"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="{.9 * k:.3f}"/></linearGradient>')
    g = [f'<defs>{"".join(d)}</defs>']
    if opaque:
        g.append(f'<rect width="{W}" height="{H}" fill="url(#stage)"/>')
    rw = 84 / 16
    order = [i for i in range(5) if i not in lit] + [i for i in range(5) if i in lit]   # lit bands drawn last
    glow = lambda i: ' filter="url(#g)"' if i in lit else ""     # only the lit bands glow
    for i in order:                                              # the rays, in from the left
        y, p = YS[i], XIN[i]
        g.append(f'<polygon points="{pt((0, y - rw), (p[0], p[1] - rw * .45), (p[0], p[1] + rw * .45), (0, y + rw))}" '
                 f'fill="url(#r{i})"{glow(i)}/>')
    g.append(f'<polygon points="{pt(TL, TR, AP)}" fill="url(#glass)"/>')
    for i in order:                                              # inside the glass: each colour narrows to white
        p = XIN[i]
        g.append(f'<polygon points="{pt((p[0], p[1] - 1.6), (EX[0], EX[1] - 1), (EX[0], EX[1] + 1), (p[0], p[1] + 1.6))}" '
                 f'fill="url(#f{i})"{glow(i)}/>')
    g.append(f'<polygon points="{pt(TL, TR, AP)}" fill="none" stroke="#FFFFFF" stroke-opacity=".85" stroke-width="2" stroke-linejoin="round"/>')
    g.append(f'<polygon points="{pt((EX[0], EX[1] - 3.5), (BEAM_TO, EX[1] - 1), (BEAM_TO, EX[1] + 1), (EX[0], EX[1] + 3.5))}" '
             'fill="url(#beam)" filter="url(#g)"/>')
    g.append(f'<ellipse cx="{EX[0]}" cy="{EX[1]}" rx="5" ry="9" fill="#FFFFFF" fill-opacity=".8" filter="url(#g)"/>')
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="display:block">{"".join(g)}</svg>', EX[1]


def shoot(svg, out, opaque, H):
    page = os.path.join(tempfile.mkdtemp(prefix="beam_"), "beam.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:transparent;'
                f'overflow:hidden}}</style></head><body>{svg}</body></html>')
    shot = page.replace(".html", ".png")
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={SCALE}",
                    f"--window-size={W},{H + 40}", "--default-background-color=00000000", f"--screenshot={shot}",
                    "file:///" + page.replace("\\", "/")], check=True, capture_output=True, timeout=120)
    im = Image.open(shot).convert("RGBA").crop((0, 0, W * SCALE, H * SCALE))
    if not opaque and im.getpixel((W * SCALE - 2, 2))[3] != 0:
        raise SystemExit("the screenshot's background isn't transparent: check Chrome's --default-background-color")
    (im if not opaque else im.convert("RGB")).save(out, optimize=True)
    print(f"{out}: {im.size[0]} x {im.size[1]} px, {os.path.getsize(out) // 1024} KB")


if __name__ == "__main__":
    svg, y = draw(range(5), opaque=False)
    shoot(svg, os.path.join(IMG, "close-beam.png"), opaque=False, H=84)
    print(f"close: beam at y={y:.1f}")
    for i, L in enumerate("PRISM"):
        svg, y = draw([i], opaque=True, H=104, dy=10)
        shoot(svg, os.path.join(IMG, f"strip-{L}.png"), opaque=True, H=104)
    print(f"steps: beam at y={y:.1f}")
