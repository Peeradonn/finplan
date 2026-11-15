"""The step strip (Pete, 15 Nov): slide 13's prism at the foot of every step slide, the verdict on the stage above it.
Slide 2 splits the label's beam into five; each step slide's strip lights only its own ray, carried across the slide
under the verdict; the close (slide 13, close_beam_art.py) recombines all five.

  .venv/Scripts/python.exe Final/looks/step_strip_art.py      # writes Final/deck/img/strip-<P|R|I|S|M>.png (3x, opaque)

Same prism as slide 13 (64 x 72 CSS px, x 112-176), apex up because the light splits here. The unlit rays fade out
instead of stopping; the lit ray fades at the right edge. The verdict sits above y = 34; every ray stays below it.
Opaque (the stage colour baked in), so the strip is one picture in PowerPoint and the glow survives.
"""
import os
import subprocess
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "deck", "img")
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
COL = {"P": "#F4B740", "R": "#FF4A57", "I": "#3CC8E6", "S": "#9B7BFF", "M": "#E6E9EE"}   # slide 2's rays
W, H, SCALE = 1280, 84, 3
A, BL, BR = (144, 6), (112, 78), (176, 78)            # slide 13's prism, apex up
Y0 = 52                                               # where the beam crosses the glass
t = (Y0 - A[1]) / (BL[1] - A[1])
E = (A[0] + (BL[0] - A[0]) * t, Y0)                   # the beam meets the left face
X = (A[0] + (BR[0] - A[0]) * t, Y0)                   # the rays leave the right face
FAN_X, FAN = 290, [38, 45, 52, 59, 66]                # where each ray (P to M) reaches before the lit one runs on
FADE_X = 340                                          # the unlit rays are gone by here
RUN_END = 1250
pt = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)
chrome = next(c for c in CHROME if os.path.exists(c))

for lit in "PRISM":
    d = [f'<filter id="g" filterUnits="userSpaceOnUse" x="-40" y="-40" width="{W + 80}" height="{H + 80}"><feGaussianBlur stdDeviation="3.2" '
         'result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
         '<linearGradient id="stage" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#101B36"/><stop offset="1" stop-color="#080E1E"/></linearGradient>',
         '<linearGradient id="in" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".3"/>'
         '<stop offset="1" stop-color="#FFFFFF"/></linearGradient>',
         '<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".22"/>'
         '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".04"/></linearGradient>',
         f'<linearGradient id="lit" gradientUnits="userSpaceOnUse" x1="{X[0]}" y1="0" x2="{RUN_END}" y2="0"><stop offset="0" stop-color="{COL[lit]}"/>'
         f'<stop offset=".55" stop-color="{COL[lit]}" stop-opacity=".9"/><stop offset="1" stop-color="{COL[lit]}" stop-opacity="0"/></linearGradient>']
    g = [f'<rect width="{W}" height="{H}" fill="url(#stage)"/>',
         f'<polygon points="{pt((0, E[1] - 4), (E[0], E[1] - 2.5), (E[0], E[1] + 2.5), (0, E[1] + 4))}" fill="url(#in)" filter="url(#g)"/>',
         f'<polygon points="{pt(A, BL, BR)}" fill="url(#glass)"/>',
         f'<polygon points="{pt((E[0], E[1] - 2.5), (X[0], X[1] - 1.5), (X[0], X[1] + 1.5), (E[0], E[1] + 2.5))}" fill="#FFFFFF" fill-opacity=".85" filter="url(#g)"/>']
    for i, L in enumerate("PRISM"):
        y = FAN[i]
        if L == lit:                                  # the step's ray: out of the glass, then on under the verdict
            g.append(f'<polygon points="{pt((X[0], X[1] - 1.5), (FAN_X, y - 3.2), (RUN_END, y - 1.2), (RUN_END, y + 1.2), (FAN_X, y + 3.2), (X[0], X[1] + 1.5))}" '
                     'fill="url(#lit)" filter="url(#g)"/>')
        else:                                         # the others: straight on, fading to nothing
            ye = X[1] + (y - X[1]) * (FADE_X - X[0]) / (FAN_X - X[0])
            d.append(f'<linearGradient id="u{L}" gradientUnits="userSpaceOnUse" x1="{X[0]}" y1="0" x2="{FADE_X}" y2="0">'
                     f'<stop offset="0" stop-color="{COL[L]}" stop-opacity=".65"/><stop offset="1" stop-color="{COL[L]}" stop-opacity="0"/></linearGradient>')
            g.append(f'<polygon points="{pt((X[0], X[1] - 1), (FADE_X, ye - 2.6), (FADE_X, ye + 2.6), (X[0], X[1] + 1))}" fill="url(#u{L})"/>')
    g.append(f'<polygon points="{pt(A, BL, BR)}" fill="none" stroke="#FFFFFF" stroke-opacity=".85" stroke-width="2" stroke-linejoin="round"/>')
    g.append(f'<ellipse cx="{X[0]}" cy="{X[1]}" rx="4" ry="8" fill="#FFFFFF" fill-opacity=".7" filter="url(#g)"/>')
    svg = f'<svg width="{W}" height="{H}" style="display:block"><defs>{"".join(d)}</defs>{"".join(g)}</svg>'
    page = os.path.join(tempfile.mkdtemp(prefix="strip_"), "strip.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>html,body{{margin:0;overflow:hidden}}</style></head><body>{svg}</body></html>')
    shot = page.replace(".html", ".png")
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={SCALE}",
                    f"--window-size={W},{H + 40}", f"--screenshot={shot}", "file:///" + page.replace("\\", "/")],
                   check=True, capture_output=True, timeout=120)
    im = Image.open(shot).convert("RGB").crop((0, 0, W * SCALE, H * SCALE))
    out = os.path.join(OUT, f"strip-{lit}.png")
    im.save(out, optimize=True)
    print(f"{out}: {os.path.getsize(out) // 1024} KB")
