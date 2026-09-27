# Context handoff — Fahtai's thread

Updated 27 Sep 2026, 18:30. For picking this thread up cold, in a new session or by a teammate.

## The situation in six lines

- UFP Award 2026 (SRFP&S/HKRFP), case **"The Wong Family Legacy"**. Round One: a **15-page written PDF**, due **Fri 2 Oct 23:59**. No slides in Round One — slides are Round Two (26 Oct) and the Final (21 Nov).
- Team of four. **Pete** (lead): exec summary, §2 cash flow, §3 retirement, §4 education, §9 succession, personal statement, integration. **Win**: §5 allocation, §6 ESG, §7 digital, §11 regulatory. **Lookbua**: §8 protection, §9 property NPV, §10 roadmap, §11, layout. **Fahtai**: the model, tax engine, Monte Carlo, sensitivity, charts, assumptions.
- Shared git repo: `D:\finplan` on device "wishdxm". Pete's working files in `Pete/`, case PDFs in `Primary Info/`, the model in `model/`.
- Fahtai owns no written section. The model feeds §§2,3,4,5,6,7 and 11.
- Round One scoring: financial proposal 25 · presentation 20 · client information 15 · risk analysis 15 · **personal statement 15** · financial goals 10.
- Judging is anonymous — no university name anywhere, including file metadata.

## What Fahtai has delivered

| File | Status |
|---|---|
| `tech1_pass-on.md` | v2, 27 Sep. The team's number sheet. v1 had wrong tax parameters and was corrected. |
| `model/wong_model.xlsx` | Inputs · BalanceSheet · Tax · Projection (2026–2072) · Outputs. 905 formulas, 0 errors. |
| `model/run_model.py` | Reads assumptions from the spreadsheet. Goal funding, Monte Carlo, sensitivity. |
| `model/README.md` | How to use it. |

## The numbers that matter

Net worth 24,405,000 · parents' investable pool 9,790,000 · annual surplus 718,230 ·
emergency reserve 30.5 months (benchmark 6–12) · property+business 60.7% of assets ·
salaries tax separate 181,770 vs joint 199,770 (separate wins by exactly 18,000) ·
retirement need at 2037 17,038,620 · projected 16,457,803 · **funded ratio 97%** ·
education reserve 2,567,698 · ESG 11.0% of the 10,470,000 base, needs +944,000 to reach 20% ·
digital 4.8%, all of it Ryan's.

**The key finding:** deterministically 97% funded, which looks fine. Under volatility the portfolio
alone lasts to Carmen's 89 only **70%** of the time. Annuitising the MPF lifts that to **91%**. That
gap is the quantified case for Pete's income-floor innovation, and it is the most valuable output so far.

## Decisions taken, and the ones still open

Settled: Ryan's income excluded from the base case (his assets stay on the balance sheet but outside
the parents' pool) · bonus at the low end, 150,000 · dependent parent allowance claimed, two parents
aged 60+ · separate assessment · equity return 6.0% (Fahtai) where Pete's lock table says 7.0%.

Open, needing the team: **the ESG denominator** — Fahtai's pass-on locks 10,470,000, Pete's brief works
toward 8,200,000 or 7,700,000, and both documents are in the repo disagreeing · the equity 6 vs 7
difference · the status-quo return assumption of 4.2% that drives the 5.16M value-of-advice figure ·
whether the 85,000 credit card actually revolves at ~30% · whether "financial goals" (10 marks) has a
page and an owner, since it is missing from Pete's page budget.

## Fahtai's outstanding work

Rules M1–M9 tested against hold-the-target (Win, 29 Sep) · medical path, VHIS ageing curve, cash path,
FX stress loaded into the model (Pete, 29 Sep) · six charts (30 Sep) · the assumptions appendix
(unclaimed, Fahtai should take it) · the Monte Carlo methodology note · a personal statement paragraph
(overdue) · four-eyes numbers check on 1 Oct.

Blocked on: Lookbua's insurance premiums, which reduce the 718,230 surplus and move every number.

## Corrections made along the way, worth not repeating

- Pass-on v1 used 2025/26 tax parameters. The 2026/27 figures are basic 145,000, married 290,000,
  child 140,000, dependent parent 60+ 55,000, and half the mortgage interest is deductible per spouse.
- Adrian retires **first** (2037, age 65); Carmen works two more years to 2039. An earlier note had
  this backwards.
- Carmen can likely access MPF at 62 under the early-retirement ground from 60 — not locked to 65.
- The separate-vs-joint 18,000 is a **mistake avoided**, not value created: separate assessment is
  Hong Kong's default. Do not present it as advice value without checking what the Wongs currently do.
