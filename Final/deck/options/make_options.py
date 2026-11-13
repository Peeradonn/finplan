"""Render storyline v5's option slides (Final/deck/options/01_options.html) with the deck's own head and tail (one home
for the tokens), fill the {{keys}} as the deck does, and set each option beside the v4 slide it would replace.

  .venv/Scripts/python.exe Final/deck/options/make_options.py

Writes Final/deck/v5_options.html (next to the deck, so its fonts/ path resolves) and Final/deck/build/options/:
the option PNGs and compare-4.png, compare-9.png (v4's slide, then the options). Run make.py first so v4's PNGs exist.
"""
import glob, os, shutil, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(DECK))
SKILL = os.path.join(os.path.expanduser("~"), ".claude", "skills", "slide-design", "scripts")
sys.path.insert(0, os.path.join(ROOT, "document"))
import fill  # noqa: E402
sys.path.insert(0, DECK)
import series  # noqa: E402  (slide 5's flip chart: [[tokens]] from figures/figure-data.md and numbers.json)

PY = sys.executable
tmp = tempfile.mkdtemp(prefix="v5opt_")
src = os.path.join(tmp, "src")
os.makedirs(src)
for name in ("00_head.html", "99_tail.html"):
    shutil.copy(os.path.join(DECK, "src", name), src)
shutil.copy(os.path.join(HERE, "01_options.html"), src)
shutil.copytree(os.path.join(DECK, "src", "lucide"), os.path.join(src, "lucide"))
shutil.copytree(os.path.join(DECK, "img"), os.path.join(tmp, "img"))               # the prism stage (slide 2)

raw = os.path.join(DECK, "_v5_options_raw.html")
subprocess.run([PY, os.path.join(SKILL, "build.py"), tmp, "--out", raw], check=True)
for icon in glob.glob(os.path.join(src, "lucide", "*.svg")):        # keep any icon build.py fetched
    dest = os.path.join(DECK, "src", "lucide", os.path.basename(icon))
    if not os.path.exists(dest):
        shutil.copy(icon, dest)
with open(raw, encoding="utf-8") as f:
    html = fill.fill_text(series.fill(f.read()))
out = os.path.join(DECK, "v5_options.html")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)
for t in (raw, os.path.join(DECK, "_v5_options_raw_notes.md")):
    if os.path.exists(t):
        os.remove(t)
shutil.rmtree(tmp, ignore_errors=True)

od = os.path.join(DECK, "build", "options")
subprocess.run([PY, os.path.join(SKILL, "render.py"), out, "--out", od], check=True)

# comparison sheets: what each new slide replaces, then the new one (v5 slides 1-4; 9A is already chosen)
font = ImageFont.truetype(os.path.join(DECK, "fonts", "PlusJakartaSans-Bold.ttf"), 30)
v4b = lambda n: os.path.join(DECK, "build", "slide-%02d.png" % n)
pairs = (("v4 slide 1", v4b(1), "v5 slide 1", "slide-01.png", "compare-1.png"),
         ("v4 slide 2", v4b(2), "v5 slide 2", "slide-02.png", "compare-2.png"),
         ("v4 slide 4 (Profile)", v4b(4), "v5 slide 3", "slide-03.png", "compare-3.png"),
         ("Option 4A, as chosen", os.path.join(od, "prev-4A.png"), "v5 slide 4, the step first", "slide-04.png", "compare-4.png"),
         ("v4 slide 6 (the flat)", v4b(6), "v5 slide 5", "slide-05.png", "compare-5.png"),
         ("v4 slide 7 (cost curve)", v4b(7), "v5 slide 6", "slide-06.png", "compare-6.png"),
         ("v4 slide 8 (finance)", v4b(8), "v5 slide 7", "slide-07.png", "compare-7.png"),
         ("v4 slide 9 (savings)", v4b(9), "v5 slide 8", "slide-08.png", "compare-8.png"),
         ("v4 slide 10 (Monitor)", v4b(10), "v5 slide 9", "slide-09.png", "compare-9.png"),
         ("v4 slide 3 (the corners)", v4b(3), "v5 slide 10, the close", "slide-10.png", "compare-10.png"))
for cap0, p0, cap1, p1, name in pairs:
    if not (os.path.exists(p0) and os.path.exists(os.path.join(od, p1))):
        continue
    ims = [Image.open(p0), Image.open(os.path.join(od, p1))]
    w, h = 1280, 720
    sheet = Image.new("RGB", (2 * (w + 30) + 30, h + 90), "#E2E2DF")
    d = ImageDraw.Draw(sheet)
    for i, (im, cap) in enumerate(zip(ims, (cap0, cap1))):
        x = 30 + i * (w + 30)
        sheet.paste(im.convert("RGB").resize((w, h)), (x, 70))
        d.text((x, 20), cap, fill="#0F1E3D", font=font)
    sheet.save(os.path.join(od, name))
print("options ->", out, "and", od)

# the whole v5 talk on one sheet, five across
names = sorted(f for f in os.listdir(od) if f.startswith("slide-") and f.endswith(".png"))
if names:
    tw, th, gap = 512, 288, 16
    cols, rows = 5, (len(names) + 4) // 5
    sheet = Image.new("RGB", (cols * (tw + gap) + gap, rows * (th + gap) + gap), "#E2E2DF")
    for i, n in enumerate(names):
        im = Image.open(os.path.join(od, n)).convert("RGB").resize((tw, th))
        sheet.paste(im, (gap + (i % cols) * (tw + gap), gap + (i // cols) * (th + gap)))
    sheet.save(os.path.join(od, "v5-contact.png"))
