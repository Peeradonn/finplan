# Built to Last — UFP Award 2026 proposal (Team Axis)

Round One written proposal for the case "The Wong Family Legacy". Lead: Pete (the user). Team: Win, Fahtai, Lookbua.
**Due Fri 2 Oct 2026, 23:59 (HKT), as a PDF.** Case and rules: `Primary Info/` (case PDF, workshop deck, `2026-rules.md`).

## Hard rules (a breach can disqualify)

- **15 pages maximum**, including the cover and appendix. 12pt Times New Roman body text, single-spaced, English.
- **No university name anywhere**, including file metadata. Microsoft Office stamps the signed-in account (a university
  email) into files it saves, so **submit the Chrome-built PDF** (`document/build/proposal.pdf`), never a PDF exported from
  Word or PowerPoint. Never write the account ID or email into any file.
- Round One scoring: financial proposal 25 · presentation 20 · client information 15 · risk analysis 15 · personal
  statement 15 · financial goals 10.

## How the document is built

```
model/wong_model.xlsx (Inputs tab)  →  model/run_model.py (Monte Carlo)  →  model/make_charts.py
      → figures/*.png, figures/figure-data.md, figures/numbers.json
page sources with {{placeholders}}  →  document/assemble.py  →  document/proposal.html (numbers filled in)
      →  document/render.py  →  document/build/proposal.pdf  (+ a fit report per page)
```

Commands (Python is **not** on PATH; use the project environment):

```
.venv/Scripts/python.exe model/build_xlsx.py            # only if the workbook structure changes
powershell -File tools/recalc.ps1 -Path <abs path to model/wong_model.xlsx>   # recalc in Excel after build_xlsx
cd model && ../.venv/Scripts/python.exe make_charts.py  # charts + numbers.json (~3-10 min)
cd document && ../.venv/Scripts/python.exe assemble.py && ../.venv/Scripts/python.exe render.py proposal.html
```

`render.py` must report **15 pages and every page "fits"**; "OVERFLOWS" (including "into the footer") means text is cut.
Page previews land in `document/build/page-N.png`. If `.venv` is missing: `python -m venv .venv` with
`C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\python.exe`, then `pip install -r requirements.txt`.

**Page sources** (edit these, never `proposal.html`):

| Pages | File |
|---|---|
| 1 cover, 2 executive summary | `document/template-v2.html` (only its first two pages are used) |
| 3, 6, 7, 8, 9 | `document/pages-03-09.html` |
| 4–5 (§3 retirement) | `document/section-mock-v3.html` |
| 10–15 | `document/pages-10-15.html` |

`document/manuscript.md` mirrors the wording page by page and records decisions and evidence. **Change wording in the
page source and the manuscript together.** `drafts/` are superseded source material. `Updated_Investment_Win.md` is Win's
investment notes (fund choices, rules). `document/export_pptx.py` makes a PowerPoint copy — only when Pete asks.

## Numbers: the rule

- **Every model-derived number is a `{{key}}` placeholder** filled from `figures/numbers.json`. Never type a model number
  into text. A new number means adding it to `export_numbers()` in `model/run_model.py` and rerunning `make_charts.py`.
- Typed numbers are allowed only for case facts, published facts (rates, rules) and a few checked figures listed in the
  manuscript's §3 notes. `fill.py` fails on an unknown key or a leftover `{{`.
- The headline: money lasts to Carmen's 89 in **33% → 83%** of 10,000 simulations; with the tier review at 75, 97%; with
  guardrails too, ~100%. These move whenever the model changes: always quote placeholders.

## Decisions already made (do not reopen without new evidence; reasons in `document/manuscript.md`)

- Theme "Built to Last"; pillars Protect · Turn assets into income · Give every voice a place. Team name Axis.
- Four decisions, in ladder order: lower spending after the first death → staged business sale → release the home
  (reverse mortgage or downsize, 2037) → MPF annuities. **The annuity is last on purpose**: it is insurance for the worst
  markets (+1 point, but in the worst 1% Carmen's spending stays above HK$382K a year with it vs HK$76K without, in
  today's money: `ann_w1_with_real`, `ann_w1_without_real`).
- Annuities are HKMC, fixed HK$, **single life**: Adrian from 2037 until his death; Carmen from 2039 for life.
- ≈HK$0.46M of mortgage still owed in 2037 is cleared from the portfolio (a reverse mortgage needs a clear title).
- Medical premiums (VHIS age curve × medical trend) are on top of the HK$780K; tier review to the Standard plan at
  Adrian's 75 (2047). Guardrails (Guyton–Klinger) from 2039, essentials 40% never cut, medical premiums don't trigger cuts.
- Critical illness HK$1.5M each (sized by need); new cover ≈HK$100K in year 1. Adrian 40% equity, Carmen 60%.
- ESG 25% of HK$10.47M investable assets, SFC-listed ESG funds only: BOC-Prudential MSCI World ESG Index Fund (core,
  Adrian 35%, Carmen 37%), Allianz Green Bond (each bond checked against ICMA), Sun Life MPF Global Low Carbon Index Fund (employee half, via
  the Employee Choice Arrangement). No thematic fund. No
  separate Hong Kong holding: 3039 dropped 1 Oct (story S14), the family already depends on Hong Kong.
- Vehicles (S19, 1 Oct): broad index funds only. Adrian / Carmen: BOC-Prudential ESG 35/37, IWDA 5/23, Treasury notes
  2037–41 20/—, IBTA 10/—, 3450 (3–5 yr) —/5, AGGU 20/20, Allianz Green Bond 5/10, 3053 5/5. No Nasdaq-100, REITs or 3433.
- `proposal-v2.html` and `proposal-v3.html` are kept as records (Pete, 1 Oct); everyone edits the page sources, and
  `document/proposal.html` is the document.
- Card balance assumed revolving; tax assumed separate assessment (both stated as checks in §2).

## Writing and design rules (Pete's standing preferences)

- Client-first, data-driven: every recommendation backed by the model or a source; every section has a finding as its
  heading and a "defend" paragraph (the alternative, why this suits the family, the trade-off, what if it fails).
- **Plain English for a judge, not model-speak**: no "sleeve", "path", "Fixed/Plan" shorthand, unexplained percentages.
- Design: body 12pt Times New Roman; EB Garamond for headings and figure titles (fonts in `document/fonts/`); one accent
  colour (crimson); left-aligned text; no text wrapping around figures; dense but not cramped. All text ≥ 12pt.
- Commit only when Pete asks. Branch: `pete/model-fix-drafts-figures`.

## Traps already hit

- In the Bash tool, heredocs turn `\n` inside Python strings into real newlines: write patch scripts to a file instead.
- `build_xlsx.py` leaves formulas uncalculated: run `tools/recalc.ps1` before `run_model.py` reads the workbook.
- A page can "fit" in Chrome's box yet run into the footer: trust `render.py`'s wording, and look at the PNG.

## Open items (need outside facts or teammates)

Personal statement career paragraphs (parked) · Wealth Management Connect figures vs HKMA · MPF passes to the estate
(no nomination) · HKMC annuity death benefit · insurer allows Flexi → Standard without underwriting · BOC-Prudential
fund's own addendum fee (brochure ≈0.78%) and a channel waiving the 5% initial charge · each parent's current MPF
fund fee · Ryan's crypto vs tokenised-MMF split ·
card revolving · tax filing status.

## Parallel sessions

Three roles, each with a brief in `reviews/`: story reviewer (`brief-story.md`), number checker (`brief-numbers.md`) and
**HTML builder** (`brief-builder.md`). Reviewers only append findings to their own file and never edit the document. The
builder is the only session that edits page sources, the manuscript, the model and `figures/`, and the only one that
commits; it logs what it did in `reviews/applied.md`. If you have not been given a role, ask Pete which one you are.
