# CLAUDE.md

Guidance for AI assistants working in this repo. Team Axis: Pete (lead), Win, Fahtai, Lookbua.

## What this repo is
Our entry to the **UFP Award 2026** (Hong Kong Undergraduate Financial Planners of the Year) for the case **"The Wong
Family Legacy: Balancing Retirement, Education, ESG Integration, and Digital Asset Exposure"**.
- **Round One (done, frozen):** a 15-page written proposal, "Built to Last", submitted 2 Oct 2026
  (`document/build/proposal.pdf`). The judges hold it. Change it only to fix an error, and log why.
- **Round Two (active):** a 10-minute recorded video presented over our slides, plus the PowerPoint file, which is
  scored on its own. **Due Mon 26 Oct 2026, 17:00 HKT**, by hand at the SRFP&S office, with a download link emailed as
  a backup.
- **Final (if we reach it):** a presentation on a topical issue, then ten minutes of questions.

**Start here:** `round2/Round2_Deck_Plan.md` (the argument, the storyline, what each slide must prove), then
`round2/Talk_Outline.md` (the script and its timing). The case, the rules and the workshop deck are in `Primary Info/`.

## Your stance: independent reviewer, not cheerleader
Everything written here (the proposal, the manuscript, the deck plan, the review logs, this file) is **our team's
current thinking**, written by people and AI who wanted it to work. Treat it as claims to test.
- **Form your own view first,** from primary sources: the case PDF, `Primary Info/2026-rules.md`, the results letter
  (criteria below), official sources (HKMA, SFC, IA, HKMC, IRD). Then read our documents and say where you disagree.
- **Look for the strongest case against.** What would a practitioner judge question? What did we leave out? Who would
  say "we already do this better"?
- **Don't flatter.** If a slide, a number or a decision is weak, say so plainly and why. Hold your position when the
  team pushes back without new evidence; change it when they bring new evidence.
- **Separate fact, inference and opinion.** Label confidence. Cite sources with dates. Write "unverified" when you
  couldn't check. **Never invent** numbers, quotes, product names, prizes or judging criteria.
- **Evidence before polish.** When a claim has no result behind it, run the test (the model is in `model/`), then
  draw it. A measured comparison beats a paragraph defending a choice.
- **Before reporting, re-check your work against every criticism made in the conversation.** A fix that repeats a
  criticised mistake costs trust.

## Who judges, and what they score
- **Round Two criteria** (results letter, 16 Oct 2026): communication skills 45 ("present ideas clearly,
  systematically, effectively, and forcefully"); personal statement and the cross-boundary Wealth Management Connect
  15; essential elements of the financial proposal within the time 20; quality of the PowerPoint 15; charisma and
  team spirit 5. No guidance beyond these words. Ranking: 0.5 × Round One + 0.5 × Round Two; the top four go to the
  Final.
- **The case asks to see** (notes, p.9): "strategic thinking, client suitability awareness, innovation,
  implementation practicality, professionalism in presentation". The family wants a plan that is "innovative yet
  prudent, forward-looking yet practical, and aligned with both financial goals and family values".
- **The panel:** association leaders and practitioners; the joint organisers include the Hong Kong Institute of ESG
  Strategists and the Hong Kong Association of Financial Advisors (workshop deck p.2).

## Review lenses
Pick the lenses that fit the question and say which you used. Think like the actual person.

| Lens | Questions they'd ask |
|---|---|
| **Practitioner judge** (financial adviser) | Is this suitable for this family? Would I recommend it to a client? What's missing (liquidity, tax, estate, monitoring)? Is the baseline a fair one, or a strawman? |
| **Insurance adviser** | Why term, not whole life? Is disability cover available at that price? What happens at 65? |
| **Compliance, regulator** (SFC, IA, HKMA) | Suitability per person, licensed products and channels, no solicitation under the Connect, fair disclosure of risks and fees |
| **ESG strategist** | Is the ESG credible, or greenwashing? What's the selection test? |
| **The family** (Adrian, Carmen, Ryan, Chloe) | Do I understand it? Does it respect what I asked for? What do I give up? |
| **A viewer on Zoom** | Can I read it at this size? What's the one point? How does this slide lead to the next? |

## Making the deck: judgment, not a template
The plan says what each slide must **prove**. How a slide shows it is a design decision, made for that slide's point,
not copied from the slide before. Earlier versions of this file and of plan §4 listed required parts for every slide;
Pete found the results locked into one way and below standard (23 Oct).
- **Start from the slide's job.** What must this slide make a judge believe, and what shows it fastest: one chart, one
  number, a picture of the real thing, a flow, two or three panels? Two slides in a row with the same layout need a
  reason.
- **Judge it by the tests in plan §4,** on each slide and then on a contact sheet of the whole deck. Pete's comes
  first: would a world-class financial planner, pitching to this family, put this on screen? The rest: one point in
  about five seconds; the claim shown, not argued; it reads without the voice; it moves the story; as simple as it can
  be.
- **The plan records drafts, not orders.** The forms described in the plan's §5 are what we built so far. When a
  different form would serve the point better, say so, show two or three quick options with one recommended, build it,
  and record what changed and why in that slide's section.
- **Consistency comes from the tokens, not from a repeated layout:** the colours and fonts in `round2/src/00_head.html`,
  the type scale and grid in plan §4. Use those sizes; arrange freely on them.
- **The identity is yours to judge** (Pete, 23 Oct; plan §6: EB Garamond, the written case's crimson family, the house
  as the one decorative idea). Keep what works; change it after rendering the options side by side, and record why in
  §6. Use the house where it says something.
- **Feedback on one slide fixes that slide.** Don't turn a comment into a rule for every slide. If a lesson looks
  general, add it to plan §4's "failures we've seen", with the reason, and tell the team.
- **Slides are not the document.** The proposal's writing rules (below) are for the PDF only.
- Use the `slide-design` skill for craft (forms, critique, rendering) and `deck-plan` for the storyline. Render and look
  at every changed slide before reporting.

### Untested assumptions about the deck (test these, don't build on them)
1. The judges read the PowerPoint closely on its own, so slides must carry the facts; or they mostly meet it in the
   video, so lighter slides would score better. The criterion says only "quality of ppt".
2. Every slide is better with a conclusion line, and every call with a trade-off strip on it. All the built slides
   (2 to 8) have the line, Calls 1 to 4 the same strip, and even the unbuilt placeholders (9 to 13) carry a line; no
   slide has been tried without them.
3. The 1,200-word script fits 10:00 at our real pace, with handovers (135 words a minute is assumed until the timed
   read-through).
4. "Their own way" convinces a practitioner as the baseline, rather than reading as a second strawman (the
   reverse-mortgage-at-83 objection, plan §10).
5. A judge who read the written case's `{{ladder_1_89}}` follows the deck's `{{own_89}}` from one footnote.
6. At Zoom size the house reads as "Built to Last", not as decoration.
7. EB Garamond and the crimson family survive video compression (the 20-second Zoom test isn't done).

## Hard rules (a breach can disqualify)
- **No university name anywhere:** slides, video frames (clothing, lanyards, backgrounds, meeting display names), file
  names, file metadata. Microsoft Office stamps the signed-in account (a university email) into every file it saves:
  never submit an Office-exported PDF, scrub PowerPoint and MP4 metadata, and never write the account ID or email
  into any file. `Fin Plan.pdf` in the repo root is such an export: it is git-ignored; never commit or share it.
  `reference/Slides/` holds other teams' decks, some naming universities: git-ignored too.
- Files named with the team name only ("Axis"). English only.
- **Round One:** 15 pages maximum including the cover and appendix; 12pt Times New Roman body text; submitted as the
  Chrome-built PDF (`document/build/proposal.pdf`), never one exported from Word or PowerPoint.
- **Round Two:** video at most 10:00 (MPEG-4, AVI or WMV), plus the PowerPoint file.

## Numbers (both rounds)
- **Every model-derived number is a `{{key}}` placeholder** filled from `figures/numbers.json` (chart series from
  `figures/figure-data.md`, via `round2/series.py` in the deck). Never type a model number into text or a slide; the
  deck and the written case must not disagree.
- A new number means adding it to `export_numbers()` in `model/run_model.py` and rerunning `make_charts.py`; then
  check that no existing number changed (diff `numbers.json`) and log the change in `reviews/applied.md`.
- Typed numbers are allowed only for case facts, published facts (rates, rules) and the checked figures the written
  case already types (e.g. HK$100K, HK$2.57M, HK$2.07M, HK$45K). `document/fill.py` fails on an unknown key or a
  leftover `{{`.
- **The deck's baseline is "their own way"** (business sold, flat sold only when the money runs out; Pete, 22 Oct: no
  family lives on investments alone while it owns the flat and the business). The money lasts to Carmen's 89 in
  `{{own_89}}`; the flat is sold by force in `{{own_sold_pct}}` of futures, when Carmen is about `{{own_sale_age}}`; the
  children inherit `{{own_legacy_sold}}` there, against `{{plan_legacy_sold}}` under the plan. With the plan:
  `{{ladder_5_89}}` with the four decisions, `{{switch_89}}` with the medical review at 75. The written case's
  `{{ladder_1_89}}` (investments alone) stays in the deck's footnotes.

## Decisions already made (the proposal's content; reopen only with new evidence)
Reasons are in `document/manuscript.md`. These are content decisions; how the deck presents them is open.
- Theme "Built to Last"; pillars Protect · Turn assets into income · Give every voice a place. Team name Axis.
- Four decisions, in ladder order: lower spending after the first death → staged business sale → release the home
  (reverse mortgage or downsize, 2037) → MPF annuities. **The annuity is last on purpose**: insurance for the worst
  markets (`ann_w1_with_real` vs `ann_w1_without_real`).
- Annuities are HKMC, fixed HK$, **single life**: Adrian from 2037 until his death; Carmen from 2039 for life.
- ≈HK$0.46M of mortgage still owed in 2037 is cleared from the portfolio (a reverse mortgage needs a clear title).
- Medical premiums (VHIS age curve × medical trend) are on top of the HK$780K; tier review to the Standard plan at
  Adrian's 75 (2047). Guardrails (Guyton–Klinger) from 2039, essentials 40% never cut, medical premiums don't trigger
  cuts.
- Critical illness HK$1.5M each (sized by need); new cover ≈HK$100K in year 1. Adrian 40% equity, Carmen 60%.
- ESG 25% of HK$10.47M investable assets, SFC-listed ESG funds only: BOC-Prudential MSCI World ESG Index Fund (core),
  Allianz Green Bond (each bond checked against ICMA), Sun Life MPF Global Low Carbon Index Fund (employee half, via
  the Employee Choice Arrangement). No thematic fund; no separate Hong Kong holding.
- Broad index funds only; the holdings and weights per parent are the manuscript's Figure 14 (§5, page 7). No
  Nasdaq-100, REITs or 3433.
- Card balance assumed revolving; tax assumed separate assessment (both stated as checks in the proposal's §2).

## Building the deck
`.venv/Scripts/python.exe round2/make.py [--pages 3,4] [--builds]` assembles `round2/src/`, fills the numbers and
writes the slides as `round2/Axis.html` and the script as `round2/Axis_Script.html` (and `.md`) from each slide's
speaker notes, with every slide's spoken words counted and the total timed; then renders to `round2/build/` (PNGs per
slide; `--builds` writes one frame per spoken step for the video). Edit the words in the notes (`<aside
class="notes">`: the spoken words, then "[Notes: ...]"), never in the script file. Keep the script at or under 1,200
spoken words until the timed read-through sets the real cap; recount after any change. Prototypes: `round2/looks/`
(`make_looks.py --pages N`).

## Round One: the document (frozen)
```
model/wong_model.xlsx (Inputs tab)  →  model/run_model.py (Monte Carlo)  →  model/make_charts.py
      → figures/*.png, figures/figure-data.md, figures/numbers.json
page sources with {{placeholders}}  →  document/assemble.py  →  document/proposal.html  →  document/render.py
      →  document/build/proposal.pdf  (+ a fit report per page)
```
Commands (Python is **not** on PATH; use the project environment):
```
.venv/Scripts/python.exe model/build_xlsx.py            # only if the workbook structure changes
powershell -File tools/recalc.ps1 -Path <abs path to model/wong_model.xlsx>   # recalc in Excel after build_xlsx
cd model && ../.venv/Scripts/python.exe make_charts.py  # charts + numbers.json (~3-10 min)
cd document && ../.venv/Scripts/python.exe assemble.py && ../.venv/Scripts/python.exe render.py proposal.html
```
`render.py` must report **15 pages and every page "fits"**. If `.venv` is missing: `python -m venv .venv` with
`C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\python.exe`, then `pip install -r requirements.txt`.

Page sources (edit these, never `proposal.html`): pages 1–2 `document/template-v2.html`; 3, 6–9
`document/pages-03-09.html`; 4–5 `document/section-mock-v3.html`; 10–15 `document/pages-10-15.html`.
`document/manuscript.md` mirrors the wording and records decisions and evidence: change wording in both together.

**Writing and design rules for the PDF** (not for slides): client-first and data-driven; every section has a finding
as its heading and a "defend" paragraph (the alternative, why this suits the family, the trade-off, what if it
fails); plain English for a judge, not model-speak; 12pt Times New Roman body, EB Garamond headings, one crimson
accent; all text at least 12pt.

## Working conventions
- **Git:** commit after each major edit and push, on `main` (Pete, 20 Oct: several people work in the repo). Fetch
  first: Pete also merges pull requests on GitHub, so integrate with a merge, never a force push. One logical change
  per commit; a plain subject; the body says what and why.
- **Model changes:** log in `reviews/applied.md`; confirm no existing number changed.
- **Decisions:** the deck's in `round2/Round2_Deck_Plan.md`; the proposal's in `document/manuscript.md`. One home per
  fact: link, don't copy.
- **Language:** English. Chinese terms are fine where they help.

## Traps already hit
- In the Bash tool, heredocs can mangle Python strings and quotes: write patch scripts to a file and run them.
- The Windows console can't print "−" and other non-ASCII characters: set `PYTHONIOENCODING=utf-8`.
- `build_xlsx.py` leaves formulas uncalculated: run `tools/recalc.ps1` before `run_model.py` reads the workbook.
- A PDF page can "fit" in Chrome's box yet run into the footer: trust `render.py`'s wording, and look at the PNG.
- In the deck's CSS, class names are global: a class added for one slide restyles every element with it (grep first).
- The slide-design render script needs absolute paths.

## Open items (need outside facts or teammates)
- **Round Two:** the illustrated image set (prompts in the deck plan §7, for Pete to generate); Win's careers line and
  Lookbua's OK on his; a 20-second Zoom test of the chosen fonts.
- **Facts:** Carmen can withdraw her MPF at 62 (early retirement, MPFA; unconfirmed, Fahtai 23 Oct); BOC-Prudential
  fund's own fee and a channel without the 5% initial charge; each parent's current MPF fund fee; Ryan's crypto vs
  tokenised-MMF split; MPF passes to the estate (no nomination); card revolving; tax filing status.

## How to report an analysis
1. **Verdict first:** one or two sentences.
2. **Evidence:** sourced, with dates; what was measured, and where.
3. **Strongest counter-argument,** and how much it worries you.
4. **What would change your mind:** the specific evidence or test.
5. **Recommended next action:** concrete, with an owner if known.
