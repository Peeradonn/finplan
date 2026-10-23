"""Build the Round Two deck (v9): the slides as HTML, and the script as a separate file.

  .venv/Scripts/python.exe round2/make.py                 # the deck and the script (every slide in its final state)
  .venv/Scripts/python.exe round2/make.py --pages 2,3     # ... and full-size PNGs of those pages
  .venv/Scripts/python.exe round2/make.py --builds        # ... and the builds: one frame per step, in build/frames/

1. slide-design build.py: round2/src/*.html -> round2/_raw.html (icons inlined, images embedded, notes collected)
2. round2/series.py: [[tokens]] -> chart series read from figures/figure-data.md (the premium line);
   document/fill.py: placeholders -> values from figures/numbers.json (the same numbers as the written proposal)
   -> round2/Axis.html (the slides)
3. The script: each slide's <aside class="notes"> (the spoken words, then "[Notes: ...]" for background) ->
   round2/Axis_Script.html and round2/Axis_Script.md, with each slide's spoken words counted (a figure counts as said:
   "83%" is three words, "HK$230K" four) against its time, and the total timed at 125, 135 and 145 words a minute.
4. slide-design render.py: PDF, PNGs and contact sheets in round2/build/
5. --builds: round2/Axis_builds.html repeats each slide once per step (class upto-k hides data-b > k), rendered to
   round2/build/frames/: what the video shows as the speaker reaches each step.
Files carry the team name only (CLAUDE.md).
"""
import datetime, html as H, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
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
    time = (re.search(r'data-time="([^"]+)"', attrs) or [None, "0:00"])[1]
    speaker = (re.search(r'data-speaker="([^"]+)"', attrs) or [None, ""])[1]
    kick = re.search(r'<p class="kick">(.*?)</p>', body, re.S)
    kick = plain(re.sub(r'<span class="gb">.*?</span>', "", kick.group(1))) if kick else ""
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
summary = (f"{total} spoken words (the budget is 1,200). Slides allotted {mmss(allotted)}. Speech: "
           + "; ".join(f"{mmss(t)} at {w} words a minute ({mmss(t + 15)} with handovers)" for w, t in paces) + ".")
who_line = "Speaking time at 135 words a minute: " + ", ".join(
    f"{w.title()} {mmss(c / 135 * 60)}" for w, c in sorted(people.items(), key=lambda kv: -kv[1])) + "."

md = [f"# Built to Last: the script (Team Axis)\n",
      f"Generated {today} by `round2/make.py` from the slides' speaker notes; numbers from `figures/numbers.json`. "
      "Edit the words in `round2/src/*.html`, not here.\n", summary, "", who_line, ""]
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
<title>Built to Last: the script</title>
<style>
@font-face{{font-family:"ArchN";src:url("fonts/ArchivoNarrow-600.ttf");font-weight:600}}
@font-face{{font-family:"Inter";src:url("fonts/Inter-400.ttf");font-weight:400}}
@font-face{{font-family:"Inter";src:url("fonts/Inter-600.ttf");font-weight:600}}
:root{{--ink:#121212;--slate:#545454;--rule:#D9D9D9;--accent:#A81E2D}}
body{{margin:0;background:#fff;color:var(--ink);font:400 16px/1.55 "Inter",Arial,sans-serif}}
main{{max-width:860px;margin:0 auto;padding:40px 24px 64px}}
h1{{font:600 40px/1.1 "ArchN","Arial Narrow",sans-serif;margin:0 0 12px}}
.sum{{color:var(--slate);margin:4px 0}}
section{{display:grid;grid-template-columns:48px 1fr;gap:16px;border-top:1.5px solid var(--ink);padding:18px 0 10px;break-inside:avoid}}
.n{{font:600 28px/1 "ArchN","Arial Narrow",sans-serif;color:var(--accent);margin:2px 0 0}}
h2{{font:600 22px/1.2 "ArchN","Arial Narrow",sans-serif;margin:0 0 4px}}
.m{{font-size:14px;color:var(--slate);margin:0 0 10px}}
.m.over{{color:#B42318;font-weight:600}}
section p{{margin:0 0 8px}}
section p b{{display:inline-block;min-width:76px;font-weight:600;font-size:14px;letter-spacing:.3px;color:var(--accent)}}
.x{{font-size:14px;color:var(--slate);border-left:3px solid var(--rule);padding-left:10px}}
@media print{{main{{padding:0}}}}
</style></head><body><main>
<h1>Built to Last: the script</h1>
<p class="sum">Team Axis · generated {today} from the slides' speaker notes; numbers from the team model.</p>
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
