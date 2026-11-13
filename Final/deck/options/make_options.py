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
    html = fill.fill_text(f.read())
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
pairs = (("v4 slide 1", os.path.join(DECK, "build", "slide-01.png"), "v5 slide 1", "slide-01.png", "compare-1.png"),
         ("v4 slide 2", os.path.join(DECK, "build", "slide-02.png"), "v5 slide 2", "slide-02.png", "compare-2.png"),
         ("v4 slide 4 (Profile)", os.path.join(DECK, "build", "slide-04.png"), "v5 slide 3", "slide-03.png", "compare-3.png"),
         ("Option 4A, as chosen", os.path.join(od, "prev-4A.png"), "v5 slide 4, the step first", "slide-04.png", "compare-4.png"))
for cap0, p0, cap1, p1, name in pairs:
    if not os.path.exists(p0):
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
