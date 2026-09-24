# Pass-on numbers — v1

Owner: Tech 1. Compiled 2026-09-24 from `Award2026Case20260919.pdf`.

**These are the numbers the rest of the team builds on.** Nothing goes into the proposal that is not
on this page or derived from the model. If you need a figure that is not here, ask — do not invent one.

Status: **v1, provisional.** Tax parameters are on a 2025/26 basis and are pending confirmation
(see [Pending](#pending-before-v2)). Everything else is computed directly from the case.

---

## 0. Headline, for the group chat

> Base case: Ryan's income excluded, bonus at 150k, dependent parent allowance claimed.
> **After-tax surplus ≈ HK$700,000/yr.** Investable base = **HK$10,470,000** — use this denominator
> everywhere. ESG is **11.0%** today, so **+944,000** to reach 20%. Digital is **4.8%**.
> Emergency reserve **30.5 months** against a 6–12 benchmark.
> Property + business = **60.7%** of assets — that is our headline diagnosis.

---

## 1. Balance sheet validation

The model reproduces the case exactly. If your numbers disagree with these, the error is yours.

| Item | Model | Case | |
|---|---|---|---|
| Total current / liquid assets | 2,500,000 | 2,500,000 | ok |
| Total investment assets | 7,970,000 | 7,970,000 | ok |
| Total fixed / other assets | 16,720,000 | 16,720,000 | ok |
| **Total assets** | **27,190,000** | **27,190,000** | ok |
| Total liabilities | 2,785,000 | 2,785,000 | ok |
| **Net worth** | **24,405,000** | **24,405,000** | ok |

---

## 2. After-tax annual surplus

Gross income − salaries tax − MPF employee mandatory − household expenses (984,000).

| Scenario | Gross | Tax | MPF | Expenses | **Surplus** | Save rate |
|---|---|---|---|---|---|---|
| **BASE — Ryan out, bonus 150k** | 1,920,000 | 200,300 | 36,000 | 984,000 | **699,700** | 36.4% |
| Ryan out, bonus 300k | 2,070,000 | 225,800 | 36,000 | 984,000 | 824,200 | 39.8% |
| Ryan in, bonus 150k | 2,220,000 | 209,720 | 51,000 | 984,000 | 975,280 | 43.9% |
| Ryan in, bonus 300k | 2,370,000 | 235,220 | 51,000 | 984,000 | 1,099,780 | 46.4% |

**Use 699,700 as the base case.** Report the Ryan-in figure as a sensitivity only.

Tax by person, base case: Adrian 121,400 · Carmen 78,900 · Ryan 9,420 (excluded from base).
MPF employee mandatory: Adrian 18,000 · Carmen 18,000 · Ryan 15,000 (below the 30,000/mth cap).

> Note for Finance 2: new insurance premiums you recommend come **out of this 699,700**, and are
> additional to the 82,000/month. Send me the premium figures and I will re-run it.

---

## 3. Net worth ratios

| Ratio | Value | Benchmark | Read |
|---|---|---|---|
| Emergency reserve | **30.5 months** | 6–12 | Heavily over-reserved |
| Liquid / total assets | 9.2% | — | |
| Debt-to-asset | 10.2% | <50% | Very low; borrowing capacity unused |
| Debt-to-net-worth | 11.4% | — | |
| Property / total assets | 42.3% | — | |
| **Property + business / total assets** | **60.7%** | — | **Concentration + illiquidity** |
| Investment assets / net worth | 32.7% | — | |
| Savings rate | 36.4% | — | Strong |

**The diagnosis these support:** the Wongs are not short of money, they are badly structured —
idle cash, two illiquid lumps, and an 85,000 revolving card balance sitting next to 620,000 of savings.
That sentence belongs in the Executive Summary.

---

## 4. Investable-asset base — DECISION LOCKED

**Base = HK$10,470,000** (total liquid 2,500,000 + total investment 7,970,000).

One denominator, used for the ESG target, the digital asset cap, and every allocation percentage
in the proposal. Do not use a different base in your own section.

Why the widest base, when narrower ones make the target easier:

1. It is the literal reading of "investable assets" in the case.
2. It is the hardest target, so we cannot be accused of shrinking the denominator to hit 20%.
3. It puts MPF in scope, which unlocks a recommendation most teams will miss —
   **switch part of Adrian's and Carmen's 1,670,000 of MPF into their schemes' ESG fund options.**
   Free, implementable, and scores under "innovation."

Footnote to disclose in the report: the base includes 420,000 of insurance cash value, which is not
freely investable (4% of base). We disclose it rather than adjust for it.

Bases we considered and rejected, for the record:

| Base | Size | ESG % | Gap to 20% |
|---|---|---|---|
| **A — liquid + all investment (CHOSEN)** | **10,470,000** | **11.0%** | **+944,000** |
| B — A less MPF and insurance cash value | 8,200,000 | 14.0% | +490,000 |
| C — B less Ryan's own assets | 7,700,000 | 14.9% | +390,000 |
| D — investment assets only | 7,970,000 | 14.4% | +444,000 |

---

## 5. ESG and digital assets against the locked base

| | Amount | % of 10,470,000 |
|---|---|---|
| ESG / sustainable equity funds | 700,000 | 6.7% |
| Green / sustainable bond products | 450,000 | 4.3% |
| **ESG total, today** | **1,150,000** | **11.0%** |
| Digital assets (BTC, ETH, VA spot ETFs, tokenized MMF) | 500,000 | **4.8%** |

Gap to the case's 20–25% ESG goal:

| Target | Required | **Additional needed** |
|---|---|---|
| 20% | 2,094,000 | **+944,000** |
| 25% | 2,617,500 | **+1,467,500** |

> For Tech 2: digital is at 4.8%, already inside a typical 5% cap, and **all 500,000 is Ryan's**.
> That supports "keep, cap, ring-fence in his own name" rather than a forced sale.

---

## 6. Locked assumptions (v1)

| # | Assumption | Value | Rationale |
|---|---|---|---|
| A1 | Ryan's income in household cash flow | **Excluded** | Case Goal 3 treats him separately; pooling flatters the plan |
| A2 | Adrian's discretionary bonus | **150,000** (low end) | A discretionary bonus should not fund a plan |
| A3 | Dependent parent allowance | **Claimed**, 2 parents aged 60+, not co-residing | Case lists "support for elderly parents" in monthly expenses |
| A4 | Child allowance | Claimed by Adrian | Higher earner |
| A5 | Spouse assessment | Separate assessment | Both have income; joint assessment to be tested in v2 |
| A6 | Investable-asset base | **10,470,000** | See section 4 |
| A7 | Carmen's 720,000 | Treated as employment income, MPF-contributing | Case says "salary / dividend"; to be revisited |

**Known inconsistency, to be disclosed in a footnote rather than hidden:** we exclude Ryan's income
(A1) but his living costs are almost certainly inside the 82,000/month. This makes the base case
conservative. Say so in the report — judges reward teams that spot it.

---

## 7. Two findings in the case that change how we model

**7.1 The 82,000/month is not a clean "living expenses" figure.** It explicitly includes the mortgage
repayment, Chloe's current tuition and extracurriculars, Adrian and Carmen's medical insurance
premiums, and support for elderly parents. Three consequences:

- When the mortgage clears, household expenses **drop**. Retirement gets easier and we must model it.
- Chloe's current school fees **stop** when she starts university, partly offsetting the new cost.
  Do not double-count — most teams will.
- Existing medical premiums are already inside the 82,000. Only *new* cover is additional.

**7.2 "Support for elderly parents" makes the dependent parent allowance claimable**, worth roughly
17,000/yr of tax. Assumption A3 covers it; the amounts need confirming.

---

## 8. Correction to earlier working

An earlier estimate put the family's salaries tax at about 290,000. That ignored allowances.
The correct figure is **200,000–235,000** depending on the bonus. Use the table in section 2.

An earlier note also had the retirement order backwards. **Adrian retires first** — he is 54 and
retires at 65, i.e. in 11 years; Carmen is 49 and retires at 62, in 13 years. Carmen works for two
years after Adrian stops. Any section assuming the reverse is wrong.

---

## 9. Pending before v2

| Item | Owner | Blocks |
|---|---|---|
| Confirm salaries tax bands, allowances, dependent parent amounts, 2026/27 rebate | Tech 1 | Section 2 |
| Confirm MPF caps and early-withdrawal-at-60 rule (Carmen retires at 62) | Tech 1 | Retirement model |
| Inflation, education inflation, wage growth, FX | Finance 1 | Everything downstream |
| Return, volatility and correlation by asset class; medical inflation | Finance 2 | Monte Carlo |
| Insurance premium estimates | Finance 2 | Surplus, section 2 |
| Mortgage rate and remaining term (not in the case — we must assume) | Finance 1 | Expense path |
| ESG and digital slice sizes and vehicles | Tech 2 | Allocation table |

---

## 10. Change log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-24 | First issue. Balance sheet validated; surplus, ratios, base and ESG/digital gaps computed. |
