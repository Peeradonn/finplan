# Brief: number check

**Your job:** confirm that every number in the proposal is correct, traceable and consistent. You do not edit the page
sources, the manuscript or the model: write findings to `reviews/numbers-findings.md` in the format below. If a check
needs a model run, run it read-only (import `model/run_model.py`; do not change inputs on disk).

## Read

1. `CLAUDE.md` (the numbers rule, how the build works, decisions already made).
2. `document/build/proposal.pdf` (rebuild first: `cd document && ../.venv/Scripts/python.exe assemble.py &&
   ../.venv/Scripts/python.exe render.py proposal.html`). Extract text per page with PyMuPDF.
3. Sources of truth: `figures/numbers.json` (model numbers used in text) · `figures/figure-data.md` (every chart's numbers)
   · `model/wong_model.xlsx` (`Inputs`, `Tax`, `BalanceSheet`, `Outputs` tabs; open with openpyxl `data_only=True`) ·
   the case PDF in `Primary Info/` · `Pete/assumptions-methodology.md` and `Pete/macro-snapshot-2026-09-23.md`
   (external rates and rules) · `Updated_Investment_Win.md` (fund data).

## Check every number on every page, and classify it

| Type | How to check |
|---|---|
| **Model** (filled from a `{{key}}`) | Matches `numbers.json`; the model logic behind it is sound (read the function in `run_model.py`). |
| **Case fact** | Matches the case PDF exactly (ages, salaries, balances, costs). |
| **Derived by hand** (a sum, a share, a present value typed into text) | Recompute it. Record your arithmetic. |
| **Published fact** (tax bands, HKMC rates, fees, quotas, dates) | Matches the cited source; note the source and date. |
| **Chart value** | Matches `figure-data.md` and the text that quotes it. |

Then check **consistency**: the same quantity must have the same value everywhere (cover, page 2, body, roadmap,
register, appendix), with the same rounding and units (today's money vs nominal; a year vs once).

## Leads to start with

1. **Carmen's business: HK$5.0M or HK$2.5M?** Page 2 (Figure 2) lists "Carmen's business 5.00" in net worth; page 10
   calls her "50% stake" HK$2.5M; page 12 says "HK$3.0M of its HK$5.0M value". Find what the case says and whether net
   worth (HK$24.41M) and the sale proceeds (HK$3.0M in the model) are consistent with it.
2. Page 3: savings rate 41%, reserve 30.5 months, debt 10%, mortgage 8.5% of income, 61% in home and business.
3. Page 6: education budget HK$2.57M present value of HK$2.85M; destination costs; "≈HK$90K" currency shortfall;
   "about HK$100K" per point of fee inflation.
4. Page 8: ESG table sums (0.83 + 0.97 + 0.84 = 2.63 = 25% of 10.47) and each row's sleeve arithmetic.
5. Page 10: protection premiums sum to ≈HK$100K; HK$157K shortfall; "14% of the surplus".
6. Page 11: intestacy shares (HK$1.1M, HK$11.9M); mortgage ≈HK$0.46M in 2037.
7. Page 12: roadmap savings (≈HK$39K = HK$14K + HK$25K; HK$59K fees).
8. Page 15: every appendix row against the `Inputs` tab.

## Findings format (`reviews/numbers-findings.md`)

```
### N1 · Page 10 · severity: wrong | inconsistent | untraceable | rounding
Quote: "exact words from the page"
Found: what the number should be, with the source or your arithmetic.
Fix: the corrected wording, or "add key X to export_numbers()" if it should come from the model.
```

Write in batches: after each group of findings add a line `## Batch N ready`, so the builder can start while you
continue. Only append; never rewrite earlier findings (add a correction as a new finding). Rank wrong numbers first. End with a table of every number you **confirmed**, by page, so the integrator knows what
was covered.
