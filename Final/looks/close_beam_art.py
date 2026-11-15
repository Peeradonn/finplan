"""The prism strips: slide 13's beam (Pete chose option B, 15 Nov) and the same picture at the foot of every step slide
(Pete, 15 Nov, later: "the prism like slide 13 ... instead of slide 3 showing every color, just show the first band").
The close: the five rays recombine through an apex-down prism into one white beam that carries the verdict, the
reverse of slide 2. A step slide: the same prism and beam, with only its own step's band coming in.

  .venv/Scripts/python.exe Final/looks/close_beam_art.py
  # writes Final/deck/img/close-beam.png (all five, transparent: it sits on slide 13's stage) and
  #        Final/deck/img/strip-<P|R|I|S|M>.png (one band, opaque: the stage colour baked in, for the white slides)

PNGs, not inline SVG, because PowerPoint drops SVG filters (the glow). The colours are slide 2's rays
(prism_stage_art.py ROWS). The strip is 1280 x 84 CSS px; the beam leaves the prism at y = 43 and ends at x = 1190,
short of the page number; the verdict sits above it.
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
W, H, SCALE = 1280, 84, 3
YS = [12, 27, 42, 57, 72]                                        # where each ray enters from the slide's edge
TL, TR, AP = (112, 6), (176, 6), (144, 78)                       # the prism, apex down (slide 2's is apex up)
BEAM_TO = 1190
pt = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)
along = lambda p, q, t: (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
XIN = [along(TL, AP, t) for t in (.22, .34, .46, .58, .70)]     # each colour meets the left face
EX = along(TR, AP, .52)                                          # one beam leaves the right face
chrome = next(c for c in CHROME if os.path.exists(c))


def draw(lit, opaque):
    """lit: the indexes of the bands that come in (0-4, P to M); opaque: bake the stage colour in."""
    d = [f'<filter id="g" filterUnits="userSpaceOnUse" x="-40" y="-40" width="{W + 80}" height="{H + 80}">'
         '<feGaussianBlur stdDeviation="3.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
         f'<linearGradient id="beam" gradientUnits="userSpaceOnUse" x1="{EX[0]}" y1="0" x2="{BEAM_TO}" y2="0">'
         '<stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/><stop offset=".35" stop-color="#FFFFFF" stop-opacity=".85"/>'
         '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".3"/></linearGradient>',
         '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".22"/>'
         '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".04"/></linearGradient>',
         '<linearGradient id="stage" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101B36"/>'
         '<stop offset="1" stop-color="#080E1E"/></linearGradient>']
    for i in lit:
        c = COL[i]
        d.append(f'<linearGradient id="r{i}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{XIN[i][0]}" y2="0">'
                 f'<stop offset="0" stop-color="{c}" stop-opacity=".25"/><stop offset=".5" stop-color="{c}" stop-opacity=".85"/>'
                 f'<stop offset="1" stop-color="{c}" stop-opacity="1"/></linearGradient>')
        d.append(f'<linearGradient id="f{i}" gradientUnits="userSpaceOnUse" x1="{XIN[i][0]}" y1="{XIN[i][1]}" x2="{EX[0]}" y2="{EX[1]}">'
                 f'<stop offset="0" stop-color="{c}" stop-opacity=".95"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".9"/></linearGradient>')
    g = [f'<defs>{"".join(d)}</defs>']
    if opaque:
        g.append(f'<rect width="{W}" height="{H}" fill="url(#stage)"/>')
    rw = H / 16
    for i in lit:                                                 # the rays, in from the left
        y, p = YS[i], XIN[i]
        g.append(f'<polygon points="{pt((0, y - rw), (p[0], p[1] - rw * .45), (p[0], p[1] + rw * .45), (0, y + rw))}" '
                 f'fill="url(#r{i})" filter="url(#g)"/>')
    g.append(f'<polygon points="{pt(TL, TR, AP)}" fill="url(#glass)"/>')
    for i in lit:                                                 # inside the glass: each colour narrows to white
        p = XIN[i]
        g.append(f'<polygon points="{pt((p[0], p[1] - 1.6), (EX[0], EX[1] - 1), (EX[0], EX[1] + 1), (p[0], p[1] + 1.6))}" '
                 f'fill="url(#f{i})" filter="url(#g)"/>')
    g.append(f'<polygon points="{pt(TL, TR, AP)}" fill="none" stroke="#FFFFFF" stroke-opacity=".85" stroke-width="2" stroke-linejoin="round"/>')
    g.append(f'<polygon points="{pt((EX[0], EX[1] - 3.5), (BEAM_TO, EX[1] - 1), (BEAM_TO, EX[1] + 1), (EX[0], EX[1] + 3.5))}" '
             'fill="url(#beam)" filter="url(#g)"/>')
    g.append(f'<ellipse cx="{EX[0]}" cy="{EX[1]}" rx="5" ry="9" fill="#FFFFFF" fill-opacity=".8" filter="url(#g)"/>')
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="display:block">{"".join(g)}</svg>'


def shoot(svg, out, opaque):
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


shoot(draw(range(5), opaque=False), os.path.join(IMG, "close-beam.png"), opaque=False)
for i, L in enumerate("PRISM"):
    shoot(draw([i], opaque=True), os.path.join(IMG, f"strip-{L}.png"), opaque=True)
print(f"beam at y={EX[1]:.1f}")
