# Model review: findings (Fahtai)

**Reviewed (1 Oct):** `model/run_model.py`, `model/wong_model.xlsx` and `figures/numbers.json` on
`pete/model-fix-drafts-figures` @ b5b5176, against `document/proposal-v3.html`. This answers "Changes 29–30 Sep
(Pete) — Fahtai, please review" in `model/README.md`. Read-only: nothing in the model or document was changed.

**Verdict: the model is sound.** `run_model.py` runs clean (the Medical tab check passes) and reproduces every
value in `numbers.json`. Separately, an independent rebuild written from the proposal's stated assumptions alone
(`model/plan_model.py` on Fahtai's side, not on this branch) lands within 3 points of every retirement figure:
ladder 34/31/42/57/81/96 against 33/31/41/59/83/97 (the v2 chart's order, annuity second; the end points do not
depend on the order); to-95 rungs within 3 points; stress F1/F2/F4/F5 within 3 points; guardrail floor 70% exact; medical line
HK$376K against HK$375K in 2056. Fixes 1–18 in the README check out, including the annuity (fixed HK$) and the
premium double-count; both were also found independently.

Four findings for the builder, one note.

---

### M1 · Page 13 (Fig 25, Fig 27 F3, note) and A1 · severity: wrong label
Quote: Fig 25 bar "Low-return decade" · Fig 27 "F3 · A low-return decade · 32% · 95%" · note "In a low-return
decade they trim spending to about 86% of the budget" · heading "after it, a low-return decade and inflation".
Found: `stressA_89` and `rec_lowret_*` pass `r_eq=ST_EQ` and `r_bd=ST_BD` to `sim()`, which applies them to **every
year 2026–2066**, not to a decade. Read-only rerun with the stress returns for ten years only (same seed):

| Low returns (equities 4.0%, ladder 2.5%) | Fixed spending | Recommended plan |
|---|---|---|
| Every year 2026–2066 (what the page shows) | 32% | 95% |
| 2026–35 only | 69% | 100% |
| 2037–46 only (the decade after Adrian retires) | 66% | 100% |

Fix (option a, no number changes): call it what it is: "Low returns for 40 years" (Fig 25 tick label in
`make_charts.py` line 381 and the scenario name at line 192; Fig 27 F3; the p13 note and heading; A1 equities and
bonds stress rows "for the whole horizon"). Option b: model a true decade (2037–46) and quote 66% / 100%, but that
needs new keys and drops the strongest stress on the page. **Recommend option a.**

### M2 · Page 13 · severity: confusing
Quote: Fig 25 "Inflation shock" **28% / 92%**; Fig 27 "F1 · Inflation 3.5%, not 2.5% · **49% / 96%**".
Found: both are right but they are different scenarios. Fig 25 B is CPI 3.5% **plus** medical 8.54% flat
(`stressB_89`); F1 is CPI 3.5% alone (`cpi_stress_89`). On one page a judge sees two numbers for "inflation".
Fix: Fig 25 tick label "Inflation and medical shock" (`make_charts.py` lines 193 and 381), or a figure note
"B: CPI 3.5% with medical costs 8.5% a year". `numbers.json` unchanged.

### M3 · Page 15 (A1) and page 4 (Fig 7) · severity: missing
The business sale is worth +17 points (`step_business`), the second-largest decision, but A1 has no row for it.
The model counts **HK$3.0M as one payment in 2039, in 2039 dollars** (`biz` added once at `BIZ_Y`), ≈HK$2.2M in
today's money, while Fig 7 says "Sell the business in stages, 2035–39" and p12 "We count only HK$3.0M of its
HK$5.0M value".
Fix: A1 row "Business sale · HK$3.0M in 2039 (of HK$5.0M today) · Not sold · Case; 40% discount". The
single-payment, unindexed treatment is conservative; no number change needed.

### M4 · Page 15 (A1) · severity: minor
The A1 "Cash · 3.0% → 2.5% by 2031 · stress 0.5%" row is not used by the simulation: the pool is 40/60
equities/ladder, the education reserve is discounted at a flat 3%, and no run uses 0.5%. Fix: source note
"Education fund and reserve; not in the simulation", or drop the stress cell.

### Note (no text change) · model details, all small and conservative
- The pre-retirement surplus grows at the wage rate (3%) as a whole, so expenses implicitly grow at 3% rather
  than CPI 2.5%. Understates saving slightly.
- Carmen's net salary in 2037–38 uses her 2026 tax grown at 3%; real tax would grow faster. Overstates by a few
  thousand a year for two years.
- Still hard-coded (README already notes it): 3% education discount rate; 2% real and 29 years in the need formula.

## Batch 1 ready
