"""Build the look checkpoint (round2/looks): assemble, fill the model's numbers, render to build/."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL = os.path.join(os.path.expanduser("~"), ".claude", "skills", "slide-design", "scripts")
sys.path.insert(0, os.path.join(ROOT, "document"))
import fill  # noqa: E402
raw, out = os.path.join(HERE, "_raw.html"), os.path.join(HERE, "Looks.html")
subprocess.run([sys.executable, os.path.join(SKILL, "build.py"), HERE, "--out", raw], check=True)
text = fill.fill_text(open(raw, encoding="utf-8").read())
open(out, "w", encoding="utf-8", newline="\n").write(text)
os.remove(raw)
for f in ("_raw_notes.md",):
    p = os.path.join(HERE, f)
    if os.path.exists(p):
        os.remove(p)
subprocess.run([sys.executable, os.path.join(SKILL, "render.py"), out, "--out", os.path.join(HERE, "build"), "--pages", "1,2,3,4,5"], check=True)
