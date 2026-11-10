# AGENTS.md

Guidance for every AI assistant in this repo: Codex reads this file, and Claude Code loads it through `CLAUDE.md`. Edit
this file, not `CLAUDE.md`. Team Axis: Pete (lead), Win, Fahtai, Lookbua.

## What this repo is
Our entry to the **UFP Award 2026** (Hong Kong Undergraduate Financial Planners of the Year) for the case **"The Wong
Family Legacy: Balancing Retirement, Education, ESG Integration, and Digital Asset Exposure"**.
- **Round One (done, frozen):** a 15-page written proposal, "Built to Last", submitted 2 Oct 2026
  (`document/build/proposal.pdf`). The judges hold it. Change it only to fix an error, and log why.
- **Round Two (done, frozen):** a 10-minute recorded video over our slides, plus the PowerPoint file (`round2/`),
  submitted 26 Oct 2026. We reached the Final.
- **Final (active):** a 10-minute live presentation in English, then 10 minutes of questions from the judges; Sat 21 Nov
  2026, FellowSPACE, Wong Chuk Hang (arrive by 09:30). Topic: "Beyond Green Labels: Integrating Sustainable Finance and
  Green Finance into Financial Planning — Financing the Transition, Pricing Climate Risk and Measuring Real Impact".
  **Slides due before 17:00 Mon 16 Nov 2026**; none can change after that. Our client is the Wong family (Pete, 4 Nov).

**Start here:** `Final/Final_Plan.md` (what the judges score, the client and thesis, rules for every slide, the framework
and storyline, who does what, the schedule, hard questions, facts to check, untested assumptions); then
`Final/Decision_List.md` (each decision against the label approach, with its price tag and capital),
`Final/model_runs.md` (the model's price tags) and the research briefs in `Final/research/`. Primary sources: the three
PDFs in `Final/` (the topic, its key areas, the finalist guidelines); the case, the rules and the workshop deck in
`Primary Info/`.

**How the Final differs from Rounds One and Two** (Pete, 5 Nov; details in `Final_Plan.md` §2–3):
- **No judge is assumed to have read Rounds One or Two.** The talk introduces the family from scratch; every slide stands
  alone.
- **The "before" is the label approach:** what a careful planner does by default (funds from the SFC's ESG list to hit
  the target, the banks' green mortgage and loan, a pledge to a charity, nothing on the business or the flat). Our Round
  One did exactly that, which shows it isn't a strawman: say so at most once, never as the spine. Never "October" or "our
  Round One plan" on a slide.
- **Round One's choices are open.** Where the framework disagrees, the new advice wins without apology. Round Two's look
  (the house, "Built to Last") isn't the default either.

## Your stance: independent reviewer, not cheerleader
Everything written here (the plans, the briefs, the decision list, the proposal, the review logs, this file) is **our
team's current thinking**, written by people and AI who wanted it to work. Treat it as claims to test.
- **Form your own view first,** from primary sources: the Final's three PDFs, the case PDF, `Primary Info/2026-rules.md`,
  official sources (HKMA, SFC, HKEX, EPD, HKMC, IRD, IA). Then read our documents and say where you disagree.
- **Look for the strongest case against.** What would a practitioner or an ESG strategist question? What did we leave
  out? Who would say "we already do this better"?
- **Don't flatter.** If a slide, a number or a decision is weak, say so plainly and why. Hold your position when the
  team pushes back without new evidence; change it when they bring new evidence.
- **Separate fact, inference and opinion.** Label confidence. Cite sources with dates. Write "unverified" when you
  couldn't check. **Never invent** numbers, quotes, product names, prizes or judging criteria.
- **Evidence before polish.** When a claim has no result behind it, run the test (the model is in `model/`; the Final's
  runs in `Final/final_model.py`), then draw it. A measured comparison beats a paragraph defending a choice.
- **Before reporting, re-check your work against every criticism made in the conversation.** A fix that repeats a
  criticised mistake costs trust.

## Who judges, and what they score
- **Final** (finalist guidelines, p.1): knowledge of the topic 20, logical thinking 20, presentation skills 20,
  innovations and independent thinking 40. Ranking: 0.15 × Round One + 0.15 × Round Two + 0.7 × Final, so earlier
  leads count for little.
- **What the ten minutes must contain** (Key Areas §7, word for word): "Lead with a recommendation, the capital required
  and the expected financial and sustainability outcomes." "Include a quantified structure, a portfolio with weights and
  costs, a scenario, a dashboard, a trade-off and a refusal." "Show your assumptions and sources, and defend them under
  questioning."
- **How evidence is judged** (Key Areas): "Cite authoritative sources and distinguish measured, estimated and
  illustrative data." "Use Hong Kong dollars, state all assumptions, and avoid fabricated or unverifiable statistics." A
  strong answer has "a clear recommendation with a number attached to it", "an honest treatment of trade-offs, data
  limits and what you would not do", and "evidence that the sustainable finance element changes the client's financial
  outcome, not just the vocabulary".
- **The panel:** not named (the guidelines name no judges). The joint organisers include the Hong Kong Institute of ESG
  Strategists and the Hong Kong Association of Financial Advisors (workshop deck p.2): expect greenwashing questions and
  suitability questions.
- **The case asks to see** (notes, p.9): "strategic thinking, client suitability awareness, innovation, implementation
  practicality, professionalism in presentation". The family wants a plan that is "innovative yet prudent,
  forward-looking yet practical, and aligned with both financial goals and family values".
- Earlier rounds: Round One's criteria are in `Primary Info/2026-rules.md`; Round Two's in `round2/Round2_Deck_Plan.md` §1.

## Review lenses
Pick the lenses that fit the question and say which you used. Think like the actual person.

| Lens | Questions they'd ask |
|---|---|
| **Practitioner judge** (financial adviser) | Is this suitable for this family? Would I recommend it to a client? Does the sustainable part change the advice, or only the words? What's missing (liquidity, tax, insurance, estate, monitoring)? Is the label approach a fair "before", or a strawman? |
| **ESG strategist** | Alignment or impact? Would it happen anyway (additionality)? Is each figure measured, estimated or modelled? Where is our own greenwashing, Carmen's "compostable" products included? |
| **Banker** | Would a bank lend for this? Cover, collateral, covenants; the cost of verification against the discount? |
| **Compliance, regulator** (SFC, HKMA, HKEX) | Suitability per person; SFC ESG fund rules and product due diligence; are we licensed to advise on the loan or the funds; fair disclosure of risks and fees |
| **The family** (Adrian, Carmen, Ryan, Chloe) | Do I understand it? Does it respect what I asked for? What do I give up, and who decides when we disagree? |
| **A judge at the back of the room** | Can I read it on a projector? What's the one point? Does it stand alone if I never saw Rounds One and Two? |

## Making the deck: judgment, not a template
The plan says what each slide must **prove** (`Final_Plan.md` §4.5, "Must prove"). How a slide shows it is a design
decision, made for that slide's point, not copied from the slide before. In Round Two, a list of required parts for
every slide locked the results into one way and below standard (Pete, 23 Oct).
- **Start from the slide's job.** What must this slide make a judge believe, and what shows it fastest: one chart, one
  number, a picture of the real thing, a flow, two or three panels? Two slides in a row with the same layout need a
  reason.
- **Judge it by these tests,** on each slide and then on a contact sheet of the whole deck. Pete's comes first: would a
  world-class financial planner, pitching to this family, put this on screen? The rest: one point in about five
  seconds; the claim shown, not argued; it reads without the voice; it stands alone for a judge who never saw Rounds One
  and Two; it moves the story; as simple as it can be.
- **The plan records drafts, not orders.** When a different form or title would serve the point better, say so, show two
  or three quick options with one recommended, build it, and record what changed and why in `Final_Plan.md`.
- **The look is decided for this talk, not inherited** (`Final_Plan.md` §3, "Look"): render the options side by side and
  choose; keep Plus Jakarta Sans if it tests well on a projector. Consistency comes from tokens (colours, fonts, a type
  scale and grid in the deck's head file), not from a repeated layout. Record the choice and why in the plan.
- **Feedback on one slide fixes that slide.** Don't turn a comment into a rule for every slide. If a lesson looks
  general, add it to `Final_Plan.md` §3 with the reason, and tell the team. Round Two's lessons are in
  `round2/Round2_Deck_Plan.md` §4, "Failures we've seen".
- **Slides are not the document.** The proposal's writing rules (below) are for the PDF only.
- **Untested assumptions** about the Final are in `Final_Plan.md` §10: test them, don't build on them.
- In Claude Code, use the `slide-design` skill for craft (forms, critique, rendering) and `deck-plan` for the storyline.
  Render and look at every changed slide before reporting.

## Hard rules (a breach can disqualify)
- **No university name anywhere:** slides, file names, file metadata, anything said on stage (guidelines rule 11),
  clothing, lanyards or anything shown. Microsoft Office stamps the signed-in account (a university email) into every
  file it saves: never submit an Office-exported PDF, scrub PowerPoint metadata, and never write the account ID or email
  into any file. `Fin Plan.pdf` in the repo root is such an export: it is git-ignored; never commit or share it.
  `reference/Slides/` holds other teams' decks, some naming universities: git-ignored too.
- Files named with the team name only ("Axis"). English only.
- **Final** (finalist guidelines, rules 1–13):
  - The PowerPoint goes **before 17:00 Mon 16 Nov 2026** by email to `info@srfpns.org`; a later file isn't accepted.
    SRFP&S acknowledges receipt: wait for it.
  - No slide can change after submission.
  - Over 10 minutes by more than 30 seconds disqualifies the team. Warnings come at 3 minutes and 1 minute left; aim for
    9:20.
  - Every member presents their own part of the slides. Say "Team Axis" before the first speaker; each speaker says their
    simple name before their part (there is a best presenter award).
- **Round One:** 15 pages maximum including the cover and appendix; 12pt Times New Roman body text; the Chrome-built PDF
  (`document/build/proposal.pdf`), never one exported from Word or PowerPoint.

## Numbers
- **Every model-derived number is a `{{key}}` placeholder** filled from `figures/numbers.json` (chart series from
  `figures/figure-data.md`). Never type a model number into text or a slide. `document/fill.py`, which both builds use,
  fails on an unknown key or a leftover `{{`.
- A new number means adding it to `export_numbers()` in `model/run_model.py` and rerunning `make_charts.py`; then check
  that no existing number changed (diff `numbers.json`) and log the change in `reviews/applied.md`.
- **The Final's runs** (`Final/final_model.py`, which imports `model/run_model.py` and never changes it) write
  `Final/model_runs.md`. They are EXPLORATORY: no slide quotes them until the chosen ones are in `export_numbers()`.
- **The Final's base** (Pete, 9 Nov): the family's plan with the medical review at 75 (`{{switch_89}}`), compared with
  the label approach (Round One as written, in the model). Near 97% the odds barely move, so lead each price tag with the
  inheritance in HK$ (today's money, including the flat). Round Two's baseline, "their own way", belongs to that deck
  only.
- **Every number on a Final slide carries its tag** and is in HK$: MEASURED (our model), SOURCED (a named source,
  dated), ESTIMATED (our arithmetic on sourced inputs) or ILLUSTRATIVE (our assumption) (`Final_Plan.md` §3). What the
  case doesn't give (the business's revenue, vans, warehouse, customers and emissions; the building's age) is
  ILLUSTRATIVE.
- Typed numbers are allowed only for case facts, published facts (rates, rules) and the research briefs' figures, with
  their tag and source. Where `Final/Decision_List.md` has the figure, take it from there, so a slide and the list never
  disagree.

## Decisions
- **The Final's:** `Final/Final_Plan.md` (thesis, framework, storyline; the team's decisions in §5) and
  `Final/Decision_List.md` (each decision: the label approach's advice, ours, its corner, price tag and capital). Reopen
  one only with new evidence. Where they differ from Round One, they win.
- **Round One's** (reasons in `document/manuscript.md`): what the written proposal recommended, and the label approach
  in the Final's model. The Final changes several (`Decision_List.md` P1, P3, P4, P6, G1, H1).
  - The retirement plan the model runs on: lower spending after the first death → staged business sale → release the
    home (reverse mortgage or downsize, 2037) → MPF annuities (HKMC, fixed HK$, single life; last on purpose, as
    insurance for the worst markets). Medical premiums on top of the HK$780K, with a tier review at Adrian's 75 (2047);
    guardrails from 2039. Critical illness HK$1.5M each. Adrian 40% equity, Carmen 60%.
  - ≈HK$0.46M of mortgage still owed in 2037 is cleared from the portfolio. The proposal's reason, that a reverse
    mortgage needs a clear title, is wrong: HKMC's lump sum can repay an existing mortgage (`Final_Plan.md` §9).
    Clearing it may still be right.
  - ESG 25% of HK$10.47M investable assets via SFC-listed ESG funds: BOC-Prudential MSCI World ESG Index Fund (core),
    Allianz Green Bond, Sun Life MPF Global Low Carbon Index Fund. The BOC-Prudential fund shows US$0.00 of assets at
    every filing since Sep 2024 (`Final_Plan.md` §9): **name no fund in the Final without checking its assets and its
    offering document.**
  - Broad index funds only (manuscript Figure 14); no Nasdaq-100, REITs or 3433. Card balance assumed revolving; tax
    assumed separate assessment.

## Building the deck
**The Final deck is in `Final/deck/`** (set up 11 Nov from Round Two's tools): `src/` holds one placeholder slide per
row of storyline v4 (`Final_Plan.md` §4.5), each pointing at what it must prove; the look's tokens are placeholders
until §3's look is chosen (build.py warns about the one `LOOK:` marker on purpose).
```
.venv/Scripts/python.exe Final/deck/make.py [--pages 3,4] [--builds]   # Axis.html, the script (Axis_Script.md), PNGs in build/
.venv/Scripts/python.exe Final/deck/make_pptx.py                       # Axis.pptx: the one file, via PowerPoint (font, metadata)
.venv/Scripts/python.exe Final/deck/make_pptx.py --no-office           # a quick draft without PowerPoint: never send it
.venv/Scripts/python.exe Final/deck/make_pptx.py --check Final/deck/Axis.pptx
```
Speaker notes open each turn with `PETE:`, `FAHTAI:`, `WIN:` or `LOOKBUA:`; build steps are `data-b="2"`, `"3"`…;
a slide with class `reveal` shows its steps from nothing instead of grey; backup slides carry `data-backup` (not timed).
The full PowerPoint step (`tools/pptx_office.ps1`) hasn't run on the Final deck yet: run it once the first real slides
exist, and check the file on a PC without our font.

What changes for a live talk on the venue's notebook and projector (`Final_Plan.md` §3, §6):
- **One file.** The PowerPoint we submit is the only one we can use on the day, so it holds the talk and, after the
  close, the backup slides for the questions (numbered, so a speaker can type the number and press Enter). No separate
  presenting copy.
- **Nothing that needs a recent PowerPoint:** the notebook's version is unknown, so don't depend on Morph; embed the
  font; check contrast on a projector. Before sending, open the file on a PC without our font and with an older
  PowerPoint.
- **The script:** about 1,200 spoken words for 9:20, four speakers, until a timed run sets the real cap.

**Round Two's tools.** `.venv/Scripts/python.exe round2/make.py [--pages 3,4] [--builds]` fills the numbers into
`round2/src/`, writes the slides (`round2/Axis.html`) and the script (`round2/Axis_Script.md`) from each slide's speaker
notes, counts and times the spoken words, and renders a PNG per slide to `round2/build/`. Edit the words in the notes
(`<aside class="notes">`: the spoken words, then "[Notes: ...]"), never in the script file. `round2/make_pptx.py` then
rebuilds every slide as an editable PowerPoint (native text, shapes, SVG drawings via `round2/pptx_extract.js`), renders
it in PowerPoint (`tools/pptx_office.ps1`) to `round2/build/pptx/` for checking, embeds Plus Jakarta Sans, sets the
metadata to "Team Axis" and stops if an email address or university name is left. Edit the HTML, never the .pptx.
Round Two's Zoom copy (`Axis_present.pptx`, Morph, `--only present|submit`) isn't needed for the Final. **Don't open
and re-save a deck in PowerPoint while signed in** (Office stamps the account into the file); if someone must, scrub it
and check with `make_pptx.py --check <file>`.

## Round One: the model and the document
```
model/wong_model.xlsx → model/run_model.py (Monte Carlo) → model/make_charts.py → figures/*.png, figure-data.md, numbers.json
page sources with {{placeholders}} → document/assemble.py → proposal.html → document/render.py → document/build/proposal.pdf
```
Python is **not** on PATH: use `.venv/Scripts/python.exe` (if `.venv` is missing: `python -m venv .venv` with
`C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\python.exe`, then `pip install -r requirements.txt`).
- **Model:** `cd model && ../.venv/Scripts/python.exe make_charts.py` (charts and `numbers.json`, 3–10 min). Only if
  the workbook's structure changes: `model/build_xlsx.py`, then `powershell -File tools/recalc.ps1 -Path <abs path to
  model/wong_model.xlsx>` to recalculate in Excel.
- **Document** (only to fix an error): `cd document && ../.venv/Scripts/python.exe assemble.py &&
  ../.venv/Scripts/python.exe render.py proposal.html` must report **15 pages and every page "fits"** (then look at the
  PNG). Edit the page sources, never `proposal.html`: pages 1–2 `template-v2.html`; 3, 6–9 `pages-03-09.html`; 4–5
  `section-mock-v3.html`; 10–15 `pages-10-15.html` (all in `document/`), and the same wording in `manuscript.md`.
- **PDF rules** (not for slides): a finding as each heading and a "defend" paragraph; plain English for a judge; 12pt
  Times New Roman body, EB Garamond headings, one crimson accent; all text at least 12pt.

## Working conventions
- **Git:** commit after each major edit and push, on `main` (Pete, 20 Oct: several people work in the repo). Fetch
  first: Pete also merges pull requests on GitHub, so integrate with a merge, never a force push. One logical change per
  commit; a plain subject; the body says what and why.
- **Model changes:** log in `reviews/applied.md`; confirm no existing number changed.
- **Decisions:** the Final's in `Final/Final_Plan.md` and `Final/Decision_List.md`; Round Two's deck in
  `round2/Round2_Deck_Plan.md`; the proposal's in `document/manuscript.md`. One home per fact: link, don't copy.
- **Language:** English. Chinese terms are fine where they help.

## Traps already hit
- In the Bash tool, heredocs can mangle Python strings and quotes: write patch scripts to a file and run them.
- The Windows console can't print "−" and other non-ASCII characters: set `PYTHONIOENCODING=utf-8`.
- `build_xlsx.py` leaves formulas uncalculated: run `tools/recalc.ps1` before `run_model.py` reads the workbook.
- A PDF page can "fit" in Chrome's box yet run into the footer: trust `render.py`'s wording, and look at the PNG.
- In the deck's CSS, class names are global: a class added for one slide restyles every element with it (grep first).
- The slide-design render script needs absolute paths.
- In this file, an `@` followed by a path outside backticks makes Claude Code import that file: keep email addresses and
  `@` mentions in backticks.

## Open items
- **The Final:** facts to check in `Final_Plan.md` §9 (and each brief's last section); open team decisions in §5 and
  `Decision_List.md` §5; hard questions in §8.
- **Unconfirmed since Round One** (a judge may still ask): Carmen can withdraw her MPF at 62 (early retirement, MPFA;
  Fahtai 23 Oct); each parent's current MPF fund fee; Ryan's crypto vs tokenised-MMF split; MPF passes to the estate (no
  nomination); card balance revolving; tax filing status.

## How to report an analysis
1. **Verdict first:** one or two sentences.
2. **Evidence:** sourced, with dates; what was measured, and where.
3. **Strongest counter-argument,** and how much it worries you.
4. **What would change your mind:** the specific evidence or test.
5. **Recommended next action:** concrete, with an owner if known.
