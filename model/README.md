# The model — read this first

## 20 seconds

**One spreadsheet, one script.** `wong_model.xlsx` holds every assumption and does the year-by-year
projection. `run_model.py` reads those same assumptions and runs the Monte Carlo.

**To change anything:** open the spreadsheet, `Inputs` tab, edit the **blue** cells. Nothing else.
Then look at the `Outputs` tab. For the Monte Carlo, run `python3 run_model.py` in this folder.

**Three yellow CHECK cells must always read 0.** If one doesn't, you broke something — undo.

**Never type a number into the proposal that isn't on the `Outputs` tab or in the script's printout.**

---

## Changes 29 Sep (Pete) — Fahtai, please review

Not committed. The workbook was rebuilt with `build_xlsx.py` and recalculated in Excel; the three CHECK cells
still read 0 and every pre-existing input is unchanged.

1. **Bug fix: the annuity was growing with inflation in the Monte Carlo.** `run_model.py` subtracted
   `(SPEND - ANN_INC) * (1+CPI)**i`, which turned the HKMC annuity into an inflation-linked one. HKMC pays a
   fixed HK$ amount for life, and the `Projection` tab already treated it that way. With the fix, mix 2
   annuitised falls from **91% to 73%** to Carmen's 89 (no medical line), and the annuity adds about 3 points,
   not 21. The claim "the annuity is the single biggest lever" no longer holds.
2. **New `Medical` tab** (methodology §1): the VHIS age curve × the medical trend path, both parents, from each
   one's retirement (when group cover ends), Adrian to his life expectancy. The part already inside the 780,000
   is netted off. It feeds a new `Medical` column in `Projection` and the Monte Carlo.
3. **New inputs** (all on `Inputs`, blue): medical plan tier, trend path, stress trend, premiums already in the
   780,000 · survivor spending after Adrian · business sale proceeds and year · reverse-mortgage income and first
   year · Adrian's life expectancy. Each backstop has a **"Use … in base (1/0)" switch, all 0 by default**, so the
   base case still holds the home and the business outside the plan.
4. **`Projection`**: new columns `Medical` and `Backstops`; survivor spending applies when its switch is on.
   Columns from `Net cash flow` onward moved two to the right (`Portfolio close` is now column U).
5. **`Outputs`**: "Funded ratio" removed. It divided the portfolio *after* the annuity purchase by a need that
   ignored the annuity's income and Carmen's last two salaries, so it didn't measure funding. Replaced by
   **first year the portfolio runs out** and **Carmen's age that year**, plus three medical outputs.
6. **`run_model.py`**: reads the new inputs and the Medical tab (it stops if its medical line differs from the
   workbook's) · new **§5 decision ladder** (what each decision adds, and the alternatives) · new §6 medical line
   by year · Carmen's tax is read from the `Tax` tab instead of a typed-in 71,335 · UTF-8 output on Windows.
7. **`build_xlsx.py`** saves next to itself (it had a hard-coded Linux path); set `WONG_XLSX` to save elsewhere.
8. **Protection premiums entered: 159,000 a year** (Lookbua's sizing; critical-illness rates from Bowtie's
   published table, 31 Aug 2026; see `drafts/08-protection.md`). They are paid only until Adrian retires, in both
   the `Projection` tab and the Monte Carlo.
9. **Bug fix: premiums were set to be deducted twice.** The script read the Outputs surplus, which already nets
   off premiums, then subtracted them again. Harmless while premiums were 0. It now reads the Tax tab's surplus.
10. **New inputs and sections**: stress-scenario values and property options (`Inputs`); `run_model.py` §7 stress
   scenarios, §8 property options (keep / reverse mortgage / downsize, with legacy), §9 Win's rebalancing rules
   against hold-the-target. Its printing now sits in `main()`, so other scripts can import it.
12. **Bug fix (30 Sep): MPF contributions were never added to the pool.** The surplus is after the employees'
   contributions and the employers' match was ignored, yet the MPF balances sit inside the simulated pool. Now both
   sides (HK$18K each, per working parent) are added in the `Projection` tab (net cash flow uses +MPF) and in
   `run_model.py` (`mpf_in`). Effect: portfolio alone 26% → 32%; full plan 80% → 85% to Carmen's 89.
13. **Guardrails modelled** (`sim(..., guard=True)`): Guyton–Klinger on the discretionary 60% of spending from 2039,
   no cuts in the last 15 years, essentials never cut, cuts stop at half of discretionary (`Inputs`). New `Inputs`
   row: medical-tier review year (2047). `run_model.py` §10 reports what happens when the plan falls short.
14. **Guardrail trigger excludes medical premiums** (`GK_MED = False`). The planned rise in premiums is budgeted,
   not a market signal; letting it trigger cuts trimmed spending in good markets too (typical family HK$744K vs
   HK$749K now; Flexi-for-life case far worse). Premiums are still paid in full. §10 also prints how the family
   lives: typical and worst-case spending, including the lowest year in the worst 5% of paths to Carmen's 95.
11. **`make_charts.py`** (new): seven charts to `../figures/` at 300 dpi, plus `figure-data.md` with every
   number behind them. Needs `matplotlib`.

**Still hard-coded in `run_model.py`** (left alone, worth moving to `Inputs` later): the 3% discount rate for
the education reserve, and the 2% real rate and 29 years in the retirement-need formula.

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
| Protection premiums (Lookbua's cover) | 159,000 a year average to 2036; surplus after them 559,230 |
| Deterministic: portfolio runs out | 2063 (Carmen 86), with medical and protection premiums, no backstops |
| Education reserve (overseas, conservative) | 2,567,698 |
| Medical line at Carmen 89 (nominal, net) | 872,123 |
| Monte Carlo, mix 2, annuitised, base case | 26% to 89 · 11% to 95 |
| **Decision ladder, all four decisions (mix 2)** | **80% to 89 · 58% to 95** |
| Same, Standard plan instead of Flexi | 98% to 89 · 93% to 95 |
| Stress scenarios A / B / C on the full plan (to 89) | 29% · 24% · 53% |

**The headline (29 Sep):** medical premiums are the binding constraint. On the portfolio alone the money
lasts to Carmen's 89 in 26% of paths. Lower spending after Adrian's life expectancy, a staged business sale and
a reverse mortgage take it to 80%; the Standard medical plan instead of Flexi takes it to 98%. The annuity adds
nothing on its own but 5 points once the other decisions are in. Downsizing in 2037 matches the reverse mortgage
(81%) and leaves ≈HK$4M more to the heirs. In the base case mix 3 (60/40) edges mix 2 (35% vs 26%).

## Known limits — state these in the proposal

- Returns are drawn from a **normal distribution** with **zero correlation** between equities and
  bonds. Real markets have fatter tails, and correlations rise in crises. The success percentages are
  therefore optimistic in the tail. Use them **comparatively** (mix 2 beats mix 3; the annuity adds
  ~21pp), not as absolute probabilities.
- Child allowance is indexed for all years rather than stopping when Chloe graduates. Small, but it
  slightly understates later tax.
- Insurance premiums are a **placeholder of 0** until Lookbua's figures arrive. Every number above
  will move when they land.
- Property, the reverse mortgage and Carmen's business are **not** in the base projection. They are
  deliberate backstops held outside the plan; switch them on in `Inputs`, and `run_model.py` §5 shows what
  each one is worth.
- The Standard-plan option uses the male Standard median for both parents (the dataset summary has no
  female Standard column). Premiums beyond 80 grow at each column's 75→80 slope.
- The part of the premiums already inside the 780,000 is netted off in full even after Adrian's death, when
  only Carmen's premium remains. Small, and conservative.
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
from Pete's lock table in `Pete/working-brief.md` §4, derived in `Pete/assumptions-methodology.md`. Tax
parameters are 2026/27 per the IR (Amendment) Ordinance 2026. Annuity and reverse-mortgage figures are
HKMC, verified 23 Sep 2026. The one deviation from Pete's table is the equity return: this model uses
6.0% where the table says 7.0%, as the conservative choice — the plan succeeds at both, so the lower
figure costs nothing and is more defensible.

### Open work
Medical cost path and VHIS ageing curve · declining cash-rate path · FX stress on overseas education ·
Win's rules M1–M9 tested against hold-the-target · Lookbua's premiums · the six charts ·
property and reverse-mortgage NPV.
