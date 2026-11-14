"""Build the Final deck (storyline v5, Final/Final_Plan.md §4.5): the slides as HTML, and the script.

  .venv/Scripts/python.exe Final/deck/make.py                 # the deck and the script
  .venv/Scripts/python.exe Final/deck/make.py --pages 2,3     # ... and full-size PNGs of those pages
  .venv/Scripts/python.exe Final/deck/make.py --builds        # ... and one frame per click, in build/frames/

Then the PowerPoint: .venv/Scripts/python.exe Final/deck/make_pptx.py (one file, the one we submit and present from).

1. slide-design build.py: Final/deck/src/*.html -> _raw.html (icons inlined, images embedded, notes collected)
2. series.py: [[tokens]] -> chart series from figures/figure-data.md (slide 5's lines); then
   document/fill.py: {{key}} placeholders -> values from figures/numbers.json (AGENTS.md "Numbers"; the Final's runs
   are EXPLORATORY until Pete moves them into export_numbers()) -> Final/deck/Axis.html
3. The script: each slide's <aside class="notes"> (the spoken words, each turn opened by PETE:, FAHTAI:, WIN: or
   LOOKBUA:, then "[Notes: ...]" for background) -> Axis_Script.html and Axis_Script.md, each slide's spoken words
   counted (a figure counts as it is said, so "84.1%" is several words) against its data-time, and the total
   timed at 125, 135 and 145 words a minute. The budget is about 1,300 words for 10:00 (Pete, 14 Nov) until a timed run sets it.
4. slide-design render.py: PDF, PNGs and contact sheets in Final/deck/build/
Adapted from round2/make.py (10 Nov). Files carry the team name only (AGENTS.md).
"""
import datetime, html as H, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL = os.path.join(os.path.expanduser("~"), ".claude", "skills", "slide-design", "scripts")
sys.path.insert(0, os.path.join(ROOT, "document"))
import fill  # noqa: E402
sys.path.insert(0, HERE)
import series  # noqa: E402

PY = sys.executable
raw = os.path.join(HERE, "_raw.html")
out = os.path.join(HERE, "Axis.html")
subprocess.run([PY, os.path.join(SKILL, "build.py"), HERE, "--out", raw], check=True)
with open(raw, encoding="utf-8") as f:
    deck = fill.fill_text(series.fill(f.read()))
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(deck)
for tmp in (raw, os.path.join(HERE, "_raw_notes.md")):
    if os.path.exists(tmp):
        os.remove(tmp)
print("filled numbers from figures/numbers.json ->", out)

# ---------- the script ----------
SEC = re.compile(r'<section class="slide([^"]*)"([^>]*)>(.*?)</section>', re.S)
WHO = re.compile(r"\b(PETE|FAHTAI|WIN|LOOKBUA|ALL):\s*")
plain = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


def said(tok):
    """Spoken words in one written token: a figure counts as it is said."""
    if not re.search(r"\d", tok):
        return 1
    w = 2 if len(re.sub(r"[^\d]", "", tok.split(".")[0])) >= 2 else 1
    w += 2 if "HK$" in tok else 0
    w += 2 if "%" in tok else 0
    w += 2 if "." in tok.strip(".") else 0
    w += 1 if re.search(r"\d[KM]\b", tok) else 0
    return w


def secs(t):
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def mmss(x):
    return f"{int(x) // 60}:{int(x) % 60:02d}"


slides, people = [], {}
for i, m in enumerate(SEC.finditer(deck), 1):
    attrs, body = m.group(2), m.group(3)
    if "data-backup" in attrs:                       # backup slides for the questions: not spoken, not timed
        continue
    time = (re.search(r'data-time="([^"]+)"', attrs) or [None, "0:00"])[1]
    speaker = (re.search(r'data-speaker="([^"]+)"', attrs) or [None, ""])[1]
    kick = re.search(r'<p class="kick(?:er)?">(.*?)</p>', body, re.S)
    kick = plain(kick.group(1)) if kick else ""
    title = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S)
    title = plain(title.group(1)) if title else ""
    note = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
    note = plain(note.group(1)) if note else ""
    spoken, extra = (note.split("[Notes:", 1) + [""])[:2]
    extra = extra.strip().rstrip("]").strip()
    turns, who = [], None
    for piece in WHO.split(spoken.strip()):
        if piece in ("PETE", "FAHTAI", "WIN", "LOOKBUA", "ALL"):
            who = piece
        elif piece.strip():
            turns.append((who, piece.strip()))
    n = 0
    for who, text in turns:
        k = sum(said(t) for t in text.split())
        n += k
        if who and who != "ALL":
            people[who] = people.get(who, 0) + k
    slides.append(dict(i=i, time=time, speaker=speaker, kick=kick, title=title, turns=turns, extra=extra, words=n))

total = sum(s["words"] for s in slides)
allotted = sum(secs(s["time"]) for s in slides)
paces = [(w, total / w * 60) for w in (145, 135, 125)]
today = datetime.date.today().isoformat()
summary = (f"{total} spoken words (the budget is about 1,300 for 10:00). Slides allotted {mmss(allotted)}. Speech: "
           + "; ".join(f"{mmss(t)} at {w} words a minute ({mmss(t + 20)} with names and handovers)" for w, t in paces)
           + ". Over 10:30 disqualifies the team.")
who_line = "Speaking time at 135 words a minute: " + ", ".join(
    f"{w.title()} {mmss(c / 135 * 60)}" for w, c in sorted(people.items(), key=lambda kv: -kv[1])) + "."

md = [f"# PRISM: the script (Team Axis)\n",
      f"Generated {today} by `Final/deck/make.py` from the slides' speaker notes. "
      "Edit the words in `Final/deck/src/*.html`, not here.\n", summary, "", who_line, ""]
cards = []
for s in slides:
    over = s["words"] / 135 * 60 > secs(s["time"]) + 3
    meta = (f"{s['kick'] + ' · ' if s['kick'] else ''}{s['speaker']} · {s['time']} · {s['words']} spoken words "
            f"(≈{round(s['words'] / 135 * 60)} s at 135){' · over its time' if over else ''}")
    md += [f"## {s['i']} · {s['title']}", f"*{meta}*", ""]
    for w, t in s["turns"]:
        md += [f"**{w.title()}:** {t}" if w else t, ""]
    if s["extra"]:
        md += [f"> Notes: {s['extra']}", ""]
    lines = "".join(f'<p><b>{H.escape(w.title()) if w else ""}</b>{H.escape(t)}</p>' for w, t in s["turns"])
    ex = f'<p class="x">Notes: {H.escape(s["extra"])}</p>' if s["extra"] else ""
    cards.append(f'<section><p class="n">{s["i"]}</p><div><h2>{H.escape(s["title"])}</h2>'
                 f'<p class="m{" over" if over else ""}">{H.escape(meta)}</p>{lines}{ex}</div></section>')
with open(os.path.join(HERE, "Axis_Script.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(md))
page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PRISM: the script</title>
<style>
@font-face{{font-family:"PJS";src:url("fonts/PlusJakartaSans-Regular.ttf");font-weight:400}}
@font-face{{font-family:"PJS";src:url("fonts/PlusJakartaSans-SemiBold.ttf");font-weight:600}}
@font-face{{font-family:"PJS";src:url("fonts/PlusJakartaSans-Bold.ttf");font-weight:700}}
:root{{--ink:#0F1E3D;--slate:#566173;--rule:#DCE1E8;--accent:#C80E1E}}
body{{margin:0;background:#fff;color:var(--ink);font:400 16px/1.55 "PJS",Arial,sans-serif}}
main{{max-width:860px;margin:0 auto;padding:40px 24px 64px}}
h1{{font:700 36px/1.1 "PJS",Arial,sans-serif;margin:0 0 12px}}
.sum{{color:var(--slate);margin:4px 0}}
section{{display:grid;grid-template-columns:48px 1fr;gap:16px;border-top:1.5px solid var(--ink);padding:18px 0 10px;break-inside:avoid}}
.n{{font:700 26px/1 "PJS",Arial,sans-serif;color:var(--accent);margin:2px 0 0}}
h2{{font:700 20px/1.25 "PJS",Arial,sans-serif;margin:0 0 4px}}
.m{{font-size:14px;color:var(--slate);margin:0 0 10px}}
.m.over{{color:#B42318;font-weight:600}}
section p{{margin:0 0 8px}}
section p b{{display:inline-block;min-width:76px;font-weight:600;font-size:14px;letter-spacing:.3px;color:var(--accent)}}
.x{{font-size:14px;color:var(--slate);border-left:3px solid var(--rule);padding-left:10px}}
@media print{{main{{padding:0}}}}
</style></head><body><main>
<h1>PRISM: the script</h1>
<p class="sum">Team Axis · generated {today} from the slides' speaker notes.</p>
<p class="sum">{H.escape(summary)}</p>
<p class="sum">{H.escape(who_line)}</p>
{"".join(cards)}
</main></body></html>
"""
with open(os.path.join(HERE, "Axis_Script.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(page)
print("script ->", os.path.join(HERE, "Axis_Script.html"), "|", summary)

# ---------- render ----------
args = sys.argv[1:]
render = [PY, os.path.join(SKILL, "render.py"), out, "--out", os.path.join(HERE, "build")]
if "--pages" in args:
    render += ["--pages", args[args.index("--pages") + 1]]
subprocess.run(render, check=True)

if "--builds" in args:
    def expand(m):
        steps = [int(s) for s in re.findall(r'data-b="(\d+)"', m.group(0))]
        if not steps:
            return m.group(0)
        return "\n".join(f'<section class="slide{m.group(1)} upto-{k}"{m.group(2)}>{m.group(3)}</section>'
                         for k in range(1, max(steps) + 1))
    builds = SEC.sub(expand, deck)
    bpath = os.path.join(HERE, "Axis_builds.html")
    open(bpath, "w", encoding="utf-8", newline="\n").write(builds)
    print(f"builds: {bpath}: {len(SEC.findall(builds))} frames")
    subprocess.run([PY, os.path.join(SKILL, "render.py"), bpath, "--out", os.path.join(HERE, "build", "frames")], check=True)
