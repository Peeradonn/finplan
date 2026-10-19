"""Build the Round Two deck: assemble the slides, fill the model's numbers, render and check.

  .venv/Scripts/python.exe round2/make.py                 # the deck (every slide in its final state)
  .venv/Scripts/python.exe round2/make.py --pages 2,3     # ... and full-size PNGs of those pages
  .venv/Scripts/python.exe round2/make.py --builds        # ... and the builds: one frame per step, in build/frames/

1. slide-design build.py: round2/src/*.html -> round2/_raw.html (icons inlined, images embedded, notes collected)
2. round2/series.py: [[tokens]] -> chart series read from figures/figure-data.md (the premium line);
   document/fill.py: placeholders -> values from figures/numbers.json (the same numbers as the written proposal)
   -> round2/Built_to_Last.html and round2/Built_to_Last_notes.md
3. slide-design render.py: PDF, PNGs and contact sheets in round2/build/
4. --builds: round2/Built_to_Last_builds.html repeats each slide once per step (class upto-k hides data-b > k), rendered
   to round2/build/frames/: what the video shows as the speaker reaches each [▶] in the script.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL = os.path.join(os.path.expanduser("~"), ".claude", "skills", "slide-design", "scripts")
sys.path.insert(0, os.path.join(ROOT, "document"))
import fill  # noqa: E402
sys.path.insert(0, HERE)
import series  # noqa: E402

PY = sys.executable
raw = os.path.join(HERE, "_raw.html")
out = os.path.join(HERE, "Built_to_Last.html")
subprocess.run([PY, os.path.join(SKILL, "build.py"), HERE, "--out", raw], check=True)
for src, dst in ((raw, out), (os.path.join(HERE, "_raw_notes.md"), os.path.join(HERE, "Built_to_Last_notes.md"))):
    if os.path.exists(src):
        with open(src, encoding="utf-8") as f:
            text = fill.fill_text(series.fill(f.read()))
        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        os.remove(src)
print("filled numbers from figures/numbers.json ->", out)

args = sys.argv[1:]
render = [PY, os.path.join(SKILL, "render.py"), out, "--out", os.path.join(HERE, "build")]
if "--pages" in args:
    render += ["--pages", args[args.index("--pages") + 1]]
subprocess.run(render, check=True)

if "--builds" in args:
    html = open(out, encoding="utf-8").read()
    SEC = re.compile(r'<section class="slide([^"]*)"(.*?)</section>', re.S)
    def expand(m):
        steps = [int(s) for s in re.findall(r'data-b="(\d+)"', m.group(0))]
        if not steps:
            return m.group(0)
        frames = []
        for k in range(1, max(steps) + 1):
            frames.append(f'<section class="slide{m.group(1)} upto-{k}"{m.group(2)}</section>')
        return "\n".join(frames)
    builds = SEC.sub(expand, html)
    bpath = os.path.join(HERE, "Built_to_Last_builds.html")
    open(bpath, "w", encoding="utf-8", newline="\n").write(builds)
    n = len(SEC.findall(builds))
    print(f"builds: {bpath}: {n} frames")
    subprocess.run([PY, os.path.join(SKILL, "render.py"), bpath, "--out", os.path.join(HERE, "build", "frames")], check=True)
