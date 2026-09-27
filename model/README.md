# The model — read this first

## 20 seconds

**One spreadsheet, one script.** `wong_model.xlsx` holds every assumption and does the year-by-year
projection. `run_model.py` reads those same assumptions and runs the Monte Carlo.

**To change anything:** open the spreadsheet, `Inputs` tab, edit the **blue** cells. Nothing else.
Then look at the `Outputs` tab. For the Monte Carlo, run `python3 run_model.py` in this folder.

**Three yellow CHECK cells must always read 0.** If one doesn't, you broke something — undo.

**Never type a number into the proposal that isn't on the `Outputs` tab or in the script's printout.**

---

## What it is

A function: assumptions in, answers out. It answers four questions.

1. How much do the Wongs need at retirement, and will they have it?
2. What does Chloe's education cost, and what must be set aside?
3. How likely is the money to last — to Carmen's 89th birthday, and to 95?
4. What changes if an assumption is wrong?

## Files

| File | What it does |
|---|---|
| `wong_model.xlsx` | Assumptions, balance sheet, tax engine, 2026–2072 projection, outputs |
| `run_model.py` | Reads the spreadsheet's assumptions; runs goal funding, Monte Carlo, sensitivity |
| `build_xlsx.py` | Rebuilds the spreadsheet from scratch. Only needed if the structure changes |

## The spreadsheet, tab by tab

**`Inputs`** — every assumption, one per row, in blue, with its source in column D. This is the only
tab anyone should edit. Grouped: economic, returns, tax 2026/27, family, model levers, dates.

**`BalanceSheet`** — the case's assets and liabilities. Recomputes net worth from components.
*CHECK cell must read 0* (net worth = 24,405,000). Also derives the parents' investable pool,
9,790,000, which excludes Ryan's MPF and his digital assets.

**`Tax`** — Hong Kong salaries tax 2026/27, four columns: Adrian, Carmen, joint, Ryan. Reads top to
bottom as a calculation you could show a judge: income, less MPF, less half the mortgage interest,
less allowances, apply the bands, compare with the standard rate. *Two CHECK cells must read 0*
(separate 181,770, joint 199,770). Ends with the annual surplus, 718,230.

**`Projection`** — 2026 to 2072, one row per year, 19 columns. Income, allowances indexed to CPI, tax
each year, MPF, living expenses, education, retirement spending, annuity, net cash flow, portfolio
open/return/close. Highlighted rows: 2037 Adrian retires, 2039 Carmen retires, 2066 Carmen 89,
2072 Carmen 95. **Formula-driven end to end — do not type in it.**

**`Outputs`** — the numbers that go in the proposal. Green means pulled from another tab.

## The script

```bash
cd model
python3 run_model.py        # about 30 seconds
```

It prints the assumptions it read (always check these look right), the goal-funding numbers, the
Monte Carlo for three mixes with and without the MPF annuitised, and an equity-return sensitivity.

**It has no assumptions of its own.** Everything comes from the spreadsheet's `Inputs` tab. If you
find yourself editing a number inside `run_model.py`, stop — it belongs in the spreadsheet.

One dependency: the script reads *cached* values from the spreadsheet. If you edit inputs in Excel or
LibreOffice, **save before running the script**, or it will read stale numbers.

## Where the numbers currently land

| | |
|---|---|
| Net worth | 24,405,000 |
| Parents' investable pool | 9,790,000 |
| Annual surplus | 718,230 |
| Emergency reserve | 30.5 months (benchmark 6–12) |
| Salaries tax, separate / joint | 181,770 / 199,770 |
| Retirement need at 2037 (today's money) | 17,038,620 |
| Projected at 2037 (today's money) | 16,457,803 |
| **Funded ratio** | **97%** |
| Education reserve (overseas, conservative) | 2,567,698 |
| Monte Carlo, mix 2, portfolio alone | 70% to 89 · 49% to 95 |
| Monte Carlo, mix 2, MPF annuitised | **91% to 89 · 80% to 95** |

**The headline:** deterministically they are 97% funded, which looks survivable; under volatility the
portfolio alone only lasts to 89 about 70% of the time. Annuitising the MPF lifts that to 91%. That
gap is the quantified case for the income floor, and it is the most useful thing the model says.

## Known limits — state these in the proposal

- Returns are drawn from a **normal distribution** with **zero correlation** between equities and
  bonds. Real markets have fatter tails, and correlations rise in crises. The success percentages are
  therefore optimistic in the tail. Use them **comparatively** (mix 2 beats mix 3; the annuity adds
  ~21pp), not as absolute probabilities.
- Child allowance is indexed for all years rather than stopping when Chloe graduates. Small, but it
  slightly understates later tax.
- Insurance premiums are a **placeholder of 0** until Lookbua's figures arrive. Every number above
  will move when they land.
- Property, the reverse mortgage and Carmen's business are **not** in the projection. They are
  deliberate backstops held outside the plan, which makes the funded ratio conservative.
- The mortgage sits inside the 984,000 of living expenses and is not modelled separately, so the
  drop in expenses when it clears (about 2040) is not captured.

## If you change one thing, change these

| Want to test | Edit |
|---|---|
| A worse market | `Equities` and `Bonds / IG` |
| Higher inflation | `CPI inflation` |
| Local instead of overseas study | `Education — overseas annual (today)` → 250,000 |
| Insurance affordability | `Insurance premiums (Lookbua, TBC)` |
| A different retirement age | `Adrian retires (age 65)` |
| No annuity | `Annuity income` → 0 and `Annuity purchase cost` → 0 |

---

## Detailed reference

### Ownership and the one-source-of-truth rule
Fahtai owns this model. The rule the team agreed: one assumptions file, one model, one allocation
table. In practice that means every figure quoted in the proposal traces to the `Outputs` tab or to
`run_model.py`'s printout. If two sections disagree, the model is right and the section is wrong.

### Dependency chain
`Inputs` → `Tax` (surplus) → `Projection` (year by year) → `Outputs` → `run_model.py` (Monte Carlo).
Breaking any link silently produces wrong numbers that still look fine, which is why the CHECK cells
exist. They are regression tests: each asserts a result that was verified by hand against Pete's
independent workings.

### Rebuilding
`build_xlsx.py` regenerates the whole workbook. After running it the formulas have no cached values,
so the script must be followed by a recalculation (LibreOffice, or opening and saving in Excel)
before `run_model.py` can read anything.

### Monte Carlo method, for the proposal's methodology note
10,000 paths. Each year an equity return and a bond return are drawn independently from normal
distributions parameterised by the `Inputs` tab (equities 6.0% / 17% volatility; Treasury ladder
4.0% / 2%, reflecting hold-to-maturity; bond funds 4.0% / 5%). Returns are applied to the opening
portfolio, then that year's cash flow is added or withdrawn. During accumulation the surplus grows
with wage growth; from Adrian's retirement, spending of 780,000 in today's money is withdrawn,
indexed to CPI, less any annuity income, with Carmen's net salary still arriving until she retires.
A path "succeeds" if the portfolio is above zero at the horizon. Reported success is the share of
paths that succeed.

### Assumption sources
Every input carries a source in column D of the `Inputs` tab. The economic and return assumptions come
from Pete's lock table in `working-brief.md` §4, derived in `assumptions-methodology.md`. Tax
parameters are 2026/27 per the IR (Amendment) Ordinance 2026. Annuity and reverse-mortgage figures are
HKMC, verified 23 Sep 2026. The one deviation from Pete's table is the equity return: this model uses
6.0% where the table says 7.0%, as the conservative choice — the plan succeeds at both, so the lower
figure costs nothing and is more defensible.

### Open work
Medical cost path and VHIS ageing curve · declining cash-rate path · FX stress on overseas education ·
Win's rules M1–M9 tested against hold-the-target · Lookbua's premiums · the six charts ·
property and reverse-mortgage NPV.
