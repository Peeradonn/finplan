# Built to Last — Manuscript (page by page)

**What this is:** the exact words, figures and tables for every page of the Round One proposal, in page order.
The printed pages mirror this file. **To build the PDF:** edit the page sources (`template-v2.html` pages 1–2,
`pages-03-09.html`, `section-mock-v3.html` pages 4–5, `pages-10-15.html`), then from `document/` run
`python assemble.py` and `python render.py proposal.html` (→ `build/proposal.pdf`, with a fit report per page).
Change wording here and in the page source together.
**Owner:** Pete (integration). Section owners edit their own pages. **Due:** Fri 2 Oct, 23:59.

## How to read and edit this file

- `##` = one A4 page. Each page lists its layout, word budget, owner and status, then its blocks in order.
- **Layout patterns** (agreed 30 Sep, see `document/section-mock-v3.html`):
  - `OPENER` label + finding-heading (one per section).
  - `ANNOT` half-width chart (left) + companion table (right) that adds facts the chart can't show.
  - `PAIR` two half-width charts at equal height.
  - `PROSE` full-width text. `TABLE` full-width table.
- **Every section has one `DEFEND` paragraph**: the alternative considered, why this suits the family, the trade-off,
  and what happens if it fails.
- **Word budgets** at 12pt: full text page ≈ 550 words; page with one ANNOT or PAIR ≈ 300; opener page ≈ 275.
- **Numbers** come from the model (`model/run_model.py`, `figures/figure-data.md`) or the case. Do not type new numbers.
- **Flags:** `[CHECK]` a fact to verify · `[DECISION]` a team decision · `[OWNER: name]` text the owner must write ·
  (all charts are drawn: see the list at the end).

## Page map

| Page | Section | Owner | Status (built 1 Oct; free space at the foot) |
|---|---|---|---|
| 1 | Cover | Pete | Built |
| 2 | Executive summary | Pete | Built, 7.6mm |
| 3 | §2 Cash flow and net worth; goals | Pete | Built, 0.9mm |
| 4–5 | §3 Retirement | Pete, Fahtai | Built, 3.2 / 2.4mm |
| 6 | §4 Education | Pete | Built, 3.5mm |
| 7 | §5 Investment and allocation | Win | Built, 7.4mm; HK$ sizes to confirm |
| 8 | §5 cont. · §6 ESG | Win | Built, 5.8mm |
| 9 | §7 Digital assets · Ryan's own plan | Win, Pete | Built, 4.0mm |
| 10 | §8 Protection | Lookbua | Built, 6.1mm |
| 11 | §9 Property · succession | Lookbua, Pete | Built, 9.4mm |
| 12 | §9 cont. · §10 Roadmap | Pete, Lookbua | Built, 17.4mm |
| 13 | §11 Risk and compliance | Lookbua, Win | Built, 4.8mm |
| 14 | Personal statement | All | Built; four career paragraphs still placeholders |
| 15 | Appendix | Fahtai | Built, 6.6mm |

## Decisions (resolved 30 Sep, from data)

Each was settled by what serves the family best, then checked against what the judges can verify from the case.

| # | Decision | Resolved as | Evidence |
|---|---|---|---|
| 1 | ESG base | **HK$10.47M**, the case's liquid + investment assets | The case sets the 20–25% target on "investable assets", and its statement totals HK$10.47M. It is also the stricter test: it includes Ryan's non-ESG HK$0.68M and the policy cash values. The plan passes on either base (25% on HK$10.47M; 23% on the freely allocable HK$7.70M), so we state the base a judge can check. |
| 2 | Critical-illness cover | **HK$1.5M each** | Sized by need: treatment not covered by VHIS (HK$0.80M) + three months' pay before disability cover starts (Adrian HK$0.30M, Carmen HK$0.18M) + home and recovery costs (HK$0.25M) = HK$1.35M and HK$1.23M. The HK$2.75M draft also counted two years' spending, which disability cover and the reserve already provide. Saves ≈HK$46K a year (HK$0.45M over ten years) with no gap. Year-1 cost of all new cover: ≈HK$100K. |
| 3 | Portfolio sizes and equity | **Emergency HK$1.0M · education HK$2.57M · long-term HK$4.13M, split 50:50; Adrian 40% equity, Carmen 60%** | Emergency: 12 months, the top of the 6–12 month benchmark, because Carmen's income depends on her business and she guarantees its loan. Education: the present value of the top-of-range overseas budget. In the model, household equity above 40% adds legacy, not security (40%: 100% to 89, worst year −10%; 54%: 99.6%, −15%), so Carmen's portfolio is set at 60% rather than 68%, keeping the family objective of "moderate growth with controlled downside". Her ESG sleeves are unchanged. `[OWNER: Win]` move 8 points of Carmen's growth and HK equity to bonds. |
| 4 | The HK$85K card balance | **Assume revolving** (the case says "credit card and revolving balance") | Clearing it is right either way: it costs nothing but 0.2% on idle savings, against ≈30% card interest. §2 states the assumption and the saving (≈HK$25K a year if it revolves). |
| 5 | Tax assessment | **Assume separate** (the default in Hong Kong) | §2 presents the HK$18K as a check: if the family has elected joint assessment, revoking it saves HK$18K a year. |
| 6 | Hong Kong equity holding (3039) | **Dropped (Pete, 1 Oct; story S14, S15)**: its 5% (Adrian) and 2% (Carmen) move into the BOC-Prudential MSCI World ESG Index Fund, now 35% and 37% | The home, Carmen's business and three incomes already depend on Hong Kong; HK and China are ≈3% of world equity, so 5% for Adrian was overweight; "tax-free dividends" is untrue for H-shares (10% mainland withholding); it was the holding most likely to fail the two-rating test. ESG stays at 25% (HK$2.64M of HK$10.47M); a plain fund in the core's place would leave 11%. Without MPF ESG funds, moving Carmen's 15% plain global holding to the ESG fund keeps 20.1% (N31). Vehicles (S16, 1 Oct): Allianz Green Bond hedged class; Sun Life MPF Global Low Carbon Index Fund via the Employee Choice Arrangement; fallback core Sun Life AM Global Low Carbon Index Fund. Fee saving ≈HK$45K, total ≈HK$105K (S17, N29). Applied in the page sources and below (1 Oct). |

**Numbers in this file** are placeholders such as `{{ladder_5_89}}`, filled from the model (`figures/numbers.json`).
To read them filled in, run `python document/fill.py document/manuscript.md` and open `manuscript.filled.md`.

---

## Page 1 · Cover

**Layout:** photograph top 118mm (desaturated 55%) · title block · headline number with pillars · contents · footer.
**Status:** final (built in `template-v2.html`).

- Label: FINANCIAL PLANNING PROPOSAL · 2 OCTOBER 2026
- Title: **Built to Last**
- Subtitle: A financial plan for Adrian, Carmen, Ryan and Chloe Wong
- Headline number: **{{ladder_1_89}} → {{ladder_5_89}}**
  - Caption: The chance the parents' money lasts to Carmen's 89th birthday: on their investments alone, and with
    the four decisions in this plan.
- Pillars: 01 **Protect** what has been built · 02 **Turn assets** into lifelong income · 03 **Give every voice** a place
- Contents (page numbers set at assembly)
- Footer: Prepared by Team Axis · All amounts in Hong Kong dollars · CONFIDENTIAL

---

## Page 2 · Executive summary

**Layout:** OPENER · number band (4) · sidebar (pull quote, Figures 1–2) + main text · six recommendations under three aims.
**Budget:** ≈330 words. **Owner:** Pete. **Status:** draft; finalise after all sections.
**Wording:** generated from `template-v2.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: Executive summary

- Finding-heading: **The Wongs own enough to retire on. The plan turns it into income that lasts.**

- **HK$24.4M** net worth, with only 10% leverage

- **HK$718K** saved a year by the parents: 41% of after-tax income

- **{{ladder_1_89}} → {{ladder_5_89}}** chance the money lasts to Carmen's 89, before and after

- **HK$100K** in year 1 closes every protection gap

- Pull quote: *Medical premiums the budget leaves out, and wealth that pays nothing in retirement, are why the money falls short.*

**Figure 1 · The family**

| Member | Risk profile |
|---|---|
| Adrian, 54 | Low–med |
| Carmen, 49 | Med–high |
| Ryan, 24 | High |
| Chloe, 16 | From 18 |

**Figure 2 · Where the wealth sits, HK$M**

|  |  |
|---|---|
| Home, Tai Kok Tsui | 11.50 |
| Carmen's business | 5.00 |
| Investments incl. MPF | 7.97 |
| Cash and deposits | 2.50 |
| Other | 0.22 |
| Less liabilities | (2.79) |
| Net worth | 24.41 |

The Wongs save 41% of after-tax income and borrow little, yet on their investments alone the money lasts to Carmen's 89 in only {{ladder_1_89}} of 10,000 simulated markets. Two findings explain why. The home pays nothing until it is sold or borrowed against, and the business pays Carmen only while she runs it; together they are 61% of the family's assets. And medical premiums outside the HK$780K budget rise to about HK$375K a year in today's money. The plan answers both, in six recommendations under three aims.

**Protect what has been built**

1. **Close the protection gaps**: disability, life and critical-illness cover, and individual medical cover before group cover ends at 65 and 62; ≈HK$100K in year 1, ≈{{premiums_avg}} a year on average until retirement (§8).

2. **Sign wills, a guardian nomination and powers of attorney** within three months, for under HK$25K, and a buy-sell agreement for Carmen's business (§9).

**Turn assets into lifelong income**

3. **Four decisions, agreed now**: lower spending after the first death, a staged business sale, releasing the home's value and annuitising the MPF. **The plan: {{ladder_5_89}}** (§3).

4. **Review the medical plan at Adrian's 75** ({{switch_89}}) and adopt spending guardrails, so spending never falls below 70% of the budget (§3).

**Give every voice a place**

5. **One family policy, a portfolio for each person**: Adrian 40/60 with a Treasury ladder, Carmen 60/40 ESG-led; ESG from 11% to 25%; Ryan mainly equity, his crypto capped on a glide path (§5–§7).

6. **Ring-fence HK$2.57M for Chloe now**, in HK dollars until she accepts an offer, so she chooses freely; her own plan starts with her first job (§4).

---

## Page 3 · §2 Cash flow and net worth · goals

**Layout:** OPENER · ANNOT (Figure 3 cash-flow chart + Figure 4 health check) · PROSE · DEFEND · TABLE (Figure 5 goals).
**Budget:** ≈330 words + two tables. **Owner:** Pete. **Status:** draft.
**Case asks for:** financial health, liquidity, leverage, debt servicing, emergency reserve, wealth concentration.
**Wording:** generated from `pages-03-09.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 02 Cash flow and net worth

- Finding-heading: **The Wongs start from strength; the risks are concentration and costs outside the budget.**

**Figure 3 · Where each year's income goes**

`figures/cashflow-half.png`

*Parents only, low bonus. Source: case; team tax model (2026/27, separate assessment).*

**Figure 4 · Health check**

| Measure | Wongs | Verdict |
|---|---|---|
| Savings rate | 41% | Strong |
| Cash reserve | 30 mo. | Too high |
| Debt to assets | 10% | Low |
| Mortgage cost | 8.5% | Low |
| In home, business | 61% | High |

*Savings: share of after-tax income. Mortgage cost: share of gross income. Benchmarks: reserve 6–12 months; debt under 50% of assets; mortgage under 30% of income.*

**Strong, liquid and lightly borrowed.** The parents save HK$718K a year after tax and MPF, 41% of after-tax income; with Ryan's pay and a mid-range bonus, before tax, it is over 55%, but the plan uses the lower figure. They hold HK$2.5M in cash: 30 months of spending, against the 6–12 months a household needs. Debt is 10% of assets, and the mortgage costs about 8.5% of gross income. **Two risks sit behind the strength.** First, concentration: the home and Carmen's business are 61% of the family's assets. The home pays nothing until it is sold or borrowed against, and the business pays Carmen's HK$720K only while she works in it. Second, the HK$82K a month excludes profits tax, travel, renovation and medical emergencies, and new cover (§8) takes ≈HK$100K in its first year. It does include support for two parents over 60; if they need care, the reserve pays first, and residential-care costs are tax-deductible.

**Put idle money to work before taking more risk.** Moving HK$500K from savings accounts at 0.2% into deposits and a money-market fund at about 3% adds ≈HK$14K a year; clearing the HK$85K card balance saves ≈HK$25K of interest if it revolves; voluntary MPF contributions of HK$60K each save ≈HK$20K of tax. If the family has elected joint assessment, separate assessment saves a further HK$18K. The reserve falls to twelve months (≈HK$1.0M) in a joint account both parents can reach.

**Figure 5 · The family's goals, ranked**

| Priority | Goal | Measure of success | When |
|---|---|---|---|
| Need | Retire at 65 and 62 on HK$780K | {{ladder_5_89}} of markets, to Carmen's 89 | 2037, 2039 |
| Need | Protect income and health | Gaps in §8 closed; wills signed | 3 months |
| Need | Fund Chloe's degree without debt | HK$2.57M fund ring-fenced | 2028–32 |
| Want | 20–25% of investable assets in ESG | 25%, in SFC-listed funds | 2027 |
| Want | Ryan financially independent | Saves 30%; cover; crypto ≤ 20% | By 2037 |
| Wish | Legacy with purpose | Staged trusts; a scholarship | Ongoing |

---

## Pages 4–5 · §3 Retirement

**Status:** final. Source of truth: `document/section-mock-v3.html` (pages 1–2). Owner: Pete; numbers Fahtai.
**Case asks for:** on track at 65/62? accumulation, drawdown and liquidity strategies.
**Wording:** generated from `section-mock-v3.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 03 Retirement planning

- Finding-heading: **Four decisions the family controls raise the chance their money lasts from {{ladder_1_89}} to {{ladder_5_89}}.**

**Figure 6 · What each decision adds**

`figures/decision-ladder-half.png`

*Source: team model, 10,000 simulations.*

**Figure 7 · When each decision is taken**

**Spend less after the first death**: from 2057 · agreed now, in writing

**Sell the business in stages**: 2035–39 · buy-sell agreement signed now

**Release the home's value**: 2037 · reverse mortgage or downsizing (§9)

**Annuitise the MPF**: 2037–39 · through HKMC, as each retires

**Why these four, and not more investment risk.** By 2037 the parents' investments reach about {{portfolio_2037_today}} in today's money, what a 2% real return needs to pay HK$780K a year until Carmen's 89; what breaks the plan is the medical premiums that figure leaves out. More equity would breach Adrian's low-to-medium risk profile, and even a 7% equity return only reaches {{eq7_89}}. The decisions use assets the family already owns; their cost is a smaller legacy. With no business sale at all, it still reaches {{biz_not_sold_89}}.

**The annuity is insurance, not a return.** It barely moves the odds ({{step_annuity}} point), but in the worst 1% of markets the money would otherwise run out, leaving Carmen {{ann_w1_without_real}} a year; with it and the spending rules in Figure 11, her spending never falls below {{ann_w1_with_real}}. It costs about {{ann_typ_cost}} a year of typical spending and {{ann_legacy_cost}} of legacy and cannot be reversed, so only the MPF's mandatory balance is annuitised.

**Saving to 2037.** After the new cover, ≈{{surplus_invest}} a year is invested: HK$60K each into tax-deductible voluntary MPF, the rest to whichever holding is below target, so rebalancing needs few sales. In 80% of markets the portfolio holds {{port2037_p10}} to {{port2037_p90}} in today's money in 2037.

**Medical premiums: the cost the budget leaves out**

**Figure 8 · Premiums by plan, both parents**

`figures/medical-premiums-half.png`

*Source: VHIS data; team model.*

**Figure 9 · The portfolio with all four decisions**

`figures/fan-chart-half.png`

*Source: team model, 10,000 simulations.*

- Label: 03 Retirement planning · continued

The HK$780K target predates individual cover, so only about HK$65K a year of premiums (both parents' Flexi premiums at 65, at today's prices) is counted inside it. From retirement they pay their own premiums, which rise with medical inflation (10% in 2027, easing to 6% by 2036) and with age (about 4.6% a year from 65 to 80), reaching HK$375K a year in today's money by 2056, close to half the budget (Figure 8). **This assumption drives the result:** if every premium sat inside the HK$780K, investments alone would last in {{no_med_1_89}} of markets, not {{ladder_1_89}}; if medical costs settle at 4.5% a year rather than 6%, the plan reaches {{med45_89}}. **Buy now, while healthy:** cover bought at 54 and 49 is renewable to 100; cover bought later may exclude conditions found by then (§8). **Review the tier at 75:** the Standard plan costs about a third as much, and switching at Adrian's 75 lifts the plan from {{ladder_5_89}} to {{switch_89}}, at the price of lower limits and fewer private-hospital choices. **Use the public floor:** Hospital Authority fees are capped at HK$10,000 a year per patient; critical-illness cover pays for what the cap excludes.

**An income floor: essentials paid for life**

On the spending pattern of Hong Kong's top-quartile households (2024/25 survey), essentials are about 40% of spending: HK$312K a year today. The MPF annuities pay {{annuity_adrian}} for Adrian until his death and {{annuity_carmen}} for Carmen for life; with the reverse mortgage they cover every essential in 2039. Cover then falls as Adrian's annuity stops and prices rise (Figure 10); the portfolio pays the rest.

**Figure 10 · Guaranteed income covers every essential at first, and less as prices rise**

| HK$ a year, as paid | 2039 | 2057, Carmen alone | 2066, Carmen 89 |
|---|---|---|---|
| Essentials (40% of spending) | {{floor_2039_ess}} | {{floor_2057_ess}} | {{floor_2066_ess}} |
| MPF annuities (fixed, single life) | {{floor_2039_ann}} | {{floor_2057_ann}} | {{floor_2066_ann}} |
| Reverse mortgage (§9) | HK$230K | HK$230K | HK$230K |
| Share of essentials covered | {{floor_2039_pct}} | {{floor_2057_pct}} | {{floor_2066_pct}} |

**Drawdown: rules agreed in advance**

Two to three years of spending sits in cash and short bonds, refilled in good years, so a market fall never forces a sale. Discretionary spending follows the Guyton–Klinger guardrails, triggered by markets rather than by the planned rise in premiums: no inflation increase after a year of negative returns; a 10% cut if the withdrawal rate rises more than 20% above its starting level; a 10% raise if it falls 20% below.

**Figure 11 · The tier review protects the money; the guardrails protect the worst case**

| With all four decisions | Lasts to 89 | To 95 | Typical spending | Worst 1 in 20 |
|---|---|---|---|---|
| Fixed spending, Flexi for life | {{fixflex_89}} | {{fixflex_95}} | {{fixflex_typical_pct}} | {{fixflex_worst5_pct}} |
| + tier review at 75 | {{fixswitch_89}} | {{fixswitch_95}} | {{fixswitch_typical_pct}} | {{fixswitch_worst5_pct}} |
| + guardrails | {{guardswitch_89}} | {{guardswitch_95}} | {{guardswitch_typical_pct}} | {{guardswitch_worst5_pct}} |

*Spending as a share of the year's budget (HK$780K; 70% of it for Carmen alone). Worst 1 in 20: lowest year in the worst 5% of simulations, to Carmen's 95.*

**What the guardrails cost, and what they buy.** The tier review does most of the work: with it, the typical family spends its full budget. The guardrails cost the typical family about {{guard_cost_pct}} of it (≈{{guard_cost}} a year while both live), taken from discretionary spending; essentials are never cut. What they buy is the worst case: in the worst one simulation in twenty, Carmen's spending falls no lower than {{guardswitch_worst5_real}} a year, {{guardswitch_worst5_pct}} of her budget, rather than to guaranteed income alone, {{fixswitch_worst5_real}}. A shortfall shows years ahead in the annual review, with agreed next steps: the tier review, then selling the home.

**Why the annuity comes last in Figure 6 (decided 30 Sep, from data).** Added first, onto a plan that is failing, its
premium showed as −2 points. Added to the full plan it is {{step_annuity}}. Its job is the worst case: on the recommended plan, in
the worst 1% of markets, Carmen's spending never falls below {{ann_w1_with_real}} a year in today's money with it; without it the money
runs out and spending falls to {{ann_w1_without_real}}. (As shares of the year's budget: {{ann_w1_with}} and {{ann_w1_without}} × HK$780K;
number check N1.) Cost: about {{ann_typ_cost}} a year of typical spending and {{ann_legacy_cost}} of legacy. It also holds if Adrian lives
to 95. Annuitising only one parent was tested and is weaker in the worst case (Carmen only: worst 1% HK$123K if Adrian lives to 95).

**Notes.** "What a 2% real return needs to pay HK$780K a year until Carmen's 89" is {{need_2037}}: 29 years, 2037–2065, the
model's horizon (`sim` runs to the start of 2066; number check N24 resolved this way). Figure 11 shows spending as a share of
the year's budget because the target is 70% of HK$780K once Carmen is alone (N1); the text quotes today's money
(`*_worst5_real`, `ann_w1_*_real`). The {{no_med_1_89}} and {{med45_89}} are keys since 1 Oct (N12).
Hard-typed figures checked against the model on 30 Sep: HK$375K of premiums by 2056 (Flexi, today's money); premiums
rise ≈4.6% a year from 65 to 80; Standard ≈0.30 of Flexi at 75; essentials HK$312K today.
The model clears the ≈HK$0.46M of mortgage still owed in 2037 from the portfolio (§9); every §3 number includes it.
`[CHECK: that the insurer allows a move to its Standard plan without new underwriting]`

---

## Page 6 · §4 Education

**Layout:** OPENER · ANNOT (Figure 12 costs by destination + Figure 13 funding timeline) · PROSE · DEFEND.
**Budget:** ≈330 words. **Owner:** Pete. **Status:** draft.
**Case asks for:** local and overseas scenarios, timing, funding vehicles, contingency.
**Wording:** generated from `pages-03-09.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 04 Education planning

- Finding-heading: **Chloe's degree is already funded: HK$2.57M set aside today covers every destination, and stays in HK dollars until she accepts an offer.**

**Figure 12 · Every destination fits the budget, even after a currency shock**

`figures/education-costs-half.png`

*Source: Statistics Canada, IRCC, Save the Student, published university fee schedules; team FX analysis.*

**Figure 13 · Funding timeline**

| When | Action |
|---|---|
| Now | Ring-fence HK$2.57M from deposits and bond funds |
| Early 2028 | Offers arrive: convert years 1–2 that month |
| 2029–31 | Convert each later year 12 months ahead |
| Any time | Unused money returns to retirement |

**The budget.** We plan on the family's own top figure, HK$600K a year in today's money, rising 5% a year: HK$662K in 2028/29 and HK$2.85M over four years. Set aside today at a 3% deposit rate, that needs **HK$2.57M**, which the family already holds in time deposits, a money-market fund and bond funds. No new saving is required.

**What each choice costs.** At 2028/29 prices the UK costs HK$335–555K a year and Canada HK$400–554K, both inside the budget even after a severe currency move (+10% for sterling, +14% for the Canadian dollar). Singapore costs HK$224–271K with the Tuition Grant, which requires three years' work in Singapore after graduation. A Hong Kong degree costs HK$150–250K; tuition itself is HK$49,500 in 2027/28, set by the government.

**Deposits, not equities, and HK dollars until an offer.** Money needed in two to six years cannot wait out a market fall, so the fund stays in deposits, a money-market fund and short bonds. Buying foreign currency early would cost 0.5–2 points a year of interest for a destination not yet chosen. If Chloe studies locally, about HK$1.5M returns to the retirement portfolio. If a currency moves against the family for years 3–4, the shortfall is at most ≈HK$90K a year, paid from surplus. Chloe's choice is hers; the plan funds all four.

**Contingencies.** Each extra point of fee inflation adds about HK$100K over the degree, and a one-year master's abroad HK$0.4–0.7M in 2032; both are paid from the surplus, which by then no longer pays for Chloe. If a parent dies or is disabled before 2032, the fund is already set aside, the wills earmark it for her education, and the new cover (§8) protects the rest of the plan. **Why not an education savings policy:** its surrender charges in the early years would lock up money needed from 2028, for a guaranteed return below what deposits pay today.

**After graduation.** Chloe's own risk profile is set at 18. When she starts work in 2032 she follows Ryan's plan (§7), with the same parental match to 2037; with the Singapore grant, that plan starts in Singapore.

---

## Page 7 · §5 Investment and allocation

**Layout:** OPENER · PROSE · TABLE (Figure 14 what each parent buys) · PROSE · DEFEND · TABLE (Figure 15 rules).
**Budget:** ≈300 words + tables. **Owner:** Win. **Status:** draft; sizes and equity per decision 3.
**Case asks for:** cash and deposits, bonds, equities and funds, ESG, digital; target allocation, rationale,
product suitability, risk management, monitoring and rebalancing.
**Wording:** generated from `pages-03-09.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 05 Investment planning

- Finding-heading: **One family policy, a portfolio for each person: each sized to its owner's risk and to when the money is needed.**

**From today to the target.** About HK$3.9M of the family's money outside the MPF is in equities, most of it in funds charging about 1.5% a year: more risk than Adrian's profile allows. Once the HK$1.0M reserve and Chloe's HK$2.57M are set aside, each parent's portfolio holds HK$2.07M, with about HK$2.1M of equity between them, all in index funds (Figure 14).

**Figure 14 · What each parent buys, HK$2.07M each**

| Holding | Its job | Adrian | Carmen |
|---|---|---|---|
| BOC-Prudential MSCI World ESG Index Fund | ESG equity core | 35% | 37% |
| iShares Core MSCI World ETF (IWDA) | Equity, lower cost | 5% | 23% |
| US Treasury notes maturing 2037–41 | Retirement years 1–5 | 20% | — |
| iShares $ Treasury Bond 1–3yr ETF (IBTA) | Short bonds | 10% | — |
| Global X US Treasury 3–5 Year ETF (3450) | Medium bonds | — | 5% |
| iShares Core Global Aggregate Bond ETF (AGGU) | Core bonds | 20% | 20% |
| Allianz Green Bond, hedged class | Green bonds | 5% | 10% |
| CSOP HKD Money Market ETF (3053) | Cash | 5% | 5% |
| Equity / bonds and cash |  | 40/60 | 60/40 |

*IWDA, IBTA, AGGU: Irish UCITS ETFs (no US estate tax); Treasury notes held directly; the rest SFC-authorised. Adrian's equity eases to 35% from 2034; the MPF holds half ESG, half bonds (§6).*

**Own the market, not chosen stocks.** Adrian's Treasuries pay his first five years of retirement whatever markets do; Carmen's 60% equity is led by ESG funds (§6), because in our model equity above 40% of the household total adds legacy but not security. Equity here means about 1,400 large companies in 23 developed markets, held at their market weight. From 1926 to 2016, 4% of US-listed companies created all of the market's net gains and most did worse than Treasury bills (Bessembinder, 2018): an index owns the few winners by construction. No sector, country or Hong Kong bets: the family's home, business and incomes already depend on Hong Kong.

**Why not all Treasuries for Adrian.** After 3.5% inflation, 5% Treasuries leave 1.5% real, and they mature by 2041 while the money must last to 2066: in our simulation an all-Treasury plan fails almost every time. The ladder is the floor; equity is the growth.

**Figure 15 · Rules agreed in advance**

| If | Then |
|---|---|
| Global equities fall 20% or more | Rebalance to target by selling bonds; never sell equities |
| Any holding drifts 5 points from target | Rebalance, using new money first |
| 5-year Treasury ≥ 4.5% | Lock yields in the ladder (triggered Sep 2026) |

*Money lasts to Carmen's 89: 5-point bands {{rebal_bands_89}}, yearly rebalancing {{rebal_target_89}}, never rebalancing {{rebal_drift_89}}.*

**Notes (S19, approved by Pete 1 Oct).** Vehicles named, broad index funds only: Win's Nasdaq-100 slice
(Adrian 5%, Carmen 3%) and Asia REITs (3447, Carmen 5%) replaced by iShares Core MSCI World (IWDA, ≈0.20%), because the
world index already holds US technology at market weight and the home is already 47% of net worth; Carmen's
medium Treasuries are 3450 (3–5 years), not 3433 (20+ years, fell ≈30% in 2022). Carmen now sums to 100%. ESG share
unchanged; the p8 fallback now gives ≈21.7%. The "HK inflation > 3.5%" rule was dropped from the table for space; §11 F1
still answers it ("shorter bonds"). The old allocation chart (`allocation-half.png`) and bucket table were removed;
figures 16–27 became 15–26. `[CHECK: Win]` 3450's name and fee, and IWDA's ongoing charge.

---

## Page 8 · §5 continued · §6 ESG

**Layout:** PROSE (§5 close) · OPENER (§6) · TABLE (Figure 16) · PROSE · DEFEND.
**Budget:** ≈420 words + table. **Owner:** Win. **Status:** draft; base per decision 1.
**Case asks for (§6):** strategic role, selection criteria, benefits and limitations, greenwashing mitigation.
**Wording:** generated from `pages-03-09.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 05 Investment planning · continued

**Value added without extra risk.** Moving about HK$4.4M of fund holdings from typical fees near 1.5% a year to funds averaging about 0.5% saves ≈HK$45K a year; with the cash, card and tax measures in §2 the family gains ≈HK$105K a year before any change in risk. The portfolios are reviewed each quarter and at an annual family meeting.

- Label: 06 ESG integration

- Finding-heading: **The family's 20–25% ESG goal, met with evidence: from 11% today to 25%, with no return premium assumed.**

**Figure 16 · How the plan reaches 25% of investable assets**

| Holding | Role (Adrian, Carmen) | What makes it ESG | HK$M |
|---|---|---|---|
| BOC-Prudential MSCI World ESG Index Fund | Global equity (35%, 37%) | The highest-rated companies in each sector of the world index | 1.49 |
| Allianz Green Bond (hedged class) | Bonds (5%, 10%) | Each bond checked against ICMA and Climate Bonds Initiative rules | 0.31 |
| Sun Life MPF Global Low Carbon Index Fund | Half of each parent's MPF | Low-carbon ESG index; underlying fund on the SFC list | 0.84 |
| Total at target, of HK$10.47M (today: 1.15, or 11%) |  |  | 2.64 (25%) |

*Rows rounded. Counted as ESG: funds on the SFC's list of ESG funds. The global core is one of only two global equity index funds on it; a plain index fund instead would leave the family at today's 11%.*

**Strategic role.** ESG is not a separate bet. It replaces the global equity core and part of the bonds with like-for-like funds, so each parent's risk and expected return stay where §5 sets them. **Selection criteria:** on the SFC's list of ESG funds; index-tracking where possible, so the method is published; low ongoing charges; daily dealing in Hong Kong dollars; and the two-rating test below.

**Three layers, one standard.** Exclusions remove thermal coal, controversial weapons and tobacco; best-in-class funds hold the highest-rated companies in each sector; green bonds with checked use of proceeds add direct impact.

**Greenwashing, tested not trusted.** ESG ratings from different agencies agree far less than credit ratings: their correlation is about 0.54, against 0.99 between Moody's and S&P (Berg, Kölbel and Rigobon, 2022). An equity fund enters only if it passes two ratings (MSCI A or better, Sustainalytics risk below 20); a green bond fund only if it checks every bond against the ICMA Green Bond Principles. Each gets a holdings check; a downgrade means replacement within three months.

**No return premium assumed.** The evidence for higher returns from ESG is mixed, so ESG funds are modelled at the same returns as their asset class. The case for them is Carmen's values and lower exposure to stranded-asset risk, at a small extra cost in fees. The limitation is a smaller universe of funds in Hong Kong. Few MPF funds are on the SFC's list, so each parent moves the half built from their own contributions to the Sun Life scheme under the Employee Choice Arrangement; if not, Carmen's plain global holding moves to the ESG fund and the family stays above 20%. Tokenised government green bonds stay on a watch-list until retail investors can buy them.

**Notes.** Fee saving ≈HK$45K (S17, N29): BOC-Prudential ≈0.78% (Index Fund Series brochure, Retail Class: 0.65% +
0.125% trustee; the ESG sub-fund's own addendum may differ), Allianz Green Bond 1.14%, the rest ≈0.15%; total 45 + 14 + 25
+ 20 ≈ HK$105K. Figure 16 rows exact: 1.4876 + 0.3099 + 0.8350 = 2.6326 (rows rounded, 2.64 shown). Fallback if no MPF
ESG fund: 20.1%. `[CHECK: Win]` the ESG sub-fund's fee, a channel that waives the 5% initial charge, each parent's MPF fund
and its expense ratio.

---

## Page 9 · §7 Digital assets · Ryan's own plan

**Layout:** OPENER · TABLE (Figure 17 suitability by person) · PROSE · ANNOT-style box for Ryan (Figure 18 glide path).
**Budget:** ≈380 words + tables. **Owner:** Win (§7), Pete (Ryan). **Status:** draft.
**Case asks for:** suitability, volatility and downside, regulation and platform risk, custody and security,
allocation limits, implementation options. **Family goal 3:** Ryan's savings, investment, protection, retirement.
**Wording:** generated from `pages-03-09.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 07 Digital assets

- Finding-heading: **Not yes or no: form, size and custody, set for each person.**

**Figure 17 · Digital assets by family member**

| Person | Crypto exposure | Vehicle | Why |
|---|---|---|---|
| Adrian | 0% | Tokenised money-market fund only, counted as cash | Capital preservation |
| Carmen | Optional, ≤ 2% of her portfolio | HKEX spot bitcoin ETF | No custody or fraud risk |
| Ryan | Glide path to ≤ 20% by 35 | HKEX spot ETFs or SFC-licensed platforms | Long horizon, strong conviction |
| Chloe | None while studying | — | Education money must be safe |

**Size limits the damage; regulation limits the channels.** Bitcoin fell about 24% in the year to September 2026 and has fallen more than 70% in past cycles, so exposure is set by what each person can lose. All holdings sit with SFC-licensed platforms or in HKEX-listed ETFs; if a platform loses its licence, holdings move to an ETF within 30 days. Self-custody requires a documented key-recovery plan: without it, digital assets cannot be inherited.

**Downside in numbers.** A 70% fall today would cost Ryan about HK$350K, more than a year's pay; at his 20% cap at 35 it would cost 14% of his wealth. Carmen's 2% cap limits the same fall to about HK$29K. **Implementation, in order of preference:** HKEX-listed spot ETFs (bitcoin 3439, ether 3009), which need only a securities account; SFC-licensed platforms for direct holdings, in their regulated custody; self-custody only with the recovery plan. Lending, leverage and unlicensed exchanges are excluded.

**Ryan's own plan**

Ryan earns HK$300K and saves 30% (HK$90K a year) in three pots: three months' spending in cash, where his tokenised money-market fund counts; goals within ten years, such as a flat deposit, in deposits and short bonds; and the rest, about 80%, in the same world index ETF as his parents (IWDA). His HK$500K of digital assets stays, but gets no new money while above his glide path, so its share falls without selling; a rally more than 10 points above the path is trimmed back (Figure 18). He adds term life and critical-illness cover for about HK$900 a year; his parents match 50% of his savings, up to HK$24K a year, until 2037. A set monthly contribution to the household builds the habit.

**Figure 18 · Ryan's crypto share of his wealth**

| Ryan saves | at 30 | at 35 |
|---|---|---|
| 20% (HK$60K) | 37% | 24% |
| 30% (HK$90K) | 32% | 20% |
| 40% (HK$120K) | 28% | 17% |

*Today about 74%, if all HK$500K is crypto. Crypto held at today's value; before the parents' match.*

**Why not sell now, or trim to 20% at once.** It is his own money, about 2% of the family's wealth, and his risk profile is high; a forced sale would override his conviction and could push him to unregulated channels. Doubling down would breach the family's objective of controlled downside. The glide path respects both: it is his money, but its share of his wealth falls as he builds everything else.

---

## Page 10 · §8 Risk management and protection

**Layout:** OPENER · sidebar numbers (2) + intro · TABLE (Figure 19) · PROSE (A–E) · family emergency plan · DEFEND.
**Budget:** ≈420 words + table. **Owner:** Lookbua. **Status:** draft; critical illness per decision 2.
**Source:** `drafts/08-protection.md`, re-sized. **Case asks for:** mortality, medical, critical illness, disability,
business continuity, family emergency plan.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 08 Risk management and protection

- Finding-heading: **Before retirement, the largest gap is income, not death: neither parent could replace their salary if disabled.**

- **HK$100K** in year 1 closes every gap: 14% of the surplus; all but medical cover ends at retirement

Of the protection risks we ranked by severity, likelihood and warning time, disability ranks first for both parents: the gap the family itself reported. The existing whole-life policies already meet most of the life need. Premiums average {{premiums_avg}} a year to retirement as they rise with age; wills and powers of attorney cost under HK$25K once (§9).

**Figure 19 · Disability and critical illness are the gaps; life cover needs only a top-up**

| New cover | Adrian (54) | Carmen (49) | Year 1 |
|---|---|---|---|
| **Disability income** | HK$65K a month to 65 | HK$39K a month to 62 | HK$37K |
| **Term life** | +1.75M (need 3.75M) | +1.05M (need 2.85M) | HK$7K |
| **Critical illness** | 1.5M | 1.5M | HK$41K |
| **Medical (VHIS)** | Flexi, deductible = group | Flexi, deductible = group | HK$15K |
| **Key person, buy-sell** | — | 5.0M, company pays | — |
| Total |  |  | ≈HK$100K |

*None of this cover exists today. Sized by need: critical illness = treatment outside VHIS + 3 months' pay. Source: Bowtie rate cards (2026); market range for disability cover; quotes replace these.*

**A) Disability first.** A benefit of 65% of pay to each parent's retirement age replaces the income the plan depends on. Carmen's cover is written on her salary, so her pay stays a salary until the business is sold.

**B) Life cover fills a defined gap.** If Adrian dies, Carmen's income leaves a shortfall of about HK$157K a year until she is 62; with the mortgage and final costs she would need HK$3.75M, of which his existing policy pays HK$2.0M, leaving HK$1.75M to cover. If Carmen dies, Adrian's income covers the household; her gap is the mortgage, the business-loan guarantee and final costs.

**C) Medical cover now, not at retirement.** Group cover ends at 65 and 62. VHIS bought while both are healthy is renewable to 100 with no new underwriting; a deductible matched to the group benefit keeps the overlap cheap, and premiums are tax-deductible up to HK$8,000 each. **D) The business survives Carmen:** a buy-sell agreement funded by company-owned key-person cover realises the full HK$5.0M going-concern value of her interest, more than the HK$3.0M the plan counts on from a sale. **E) Ryan starts small:** HK$0.5M life and HK$0.3M critical-illness cover for ≈HK$900 a year.

**Family emergency plan.** A joint account pays every bill for twelve months (≈HK$1.0M) while an estate is settled; a one-page family file lists every policy, account and recovery route; Chloe has two named emergency contacts and a guardian (§9).

**Term cover, not more whole-life.** The need ends at retirement, when the mortgage is cleared, Chloe has graduated and the annuities begin. Term cover prices that window; whole-life cover of the same amount costs many times more, because most of its premium buys savings the family already holds. The trade-off: the new cover lapses at 65 and 62, after which the existing policies and the portfolio carry the risk. If a claim is disputed, the emergency reserve carries the family while it is settled.

---

## Page 11 · §9 Property · succession

**Source:** `drafts/09-property.md` (Lookbua) + working brief §3.6 (Pete).
**Layout:** OPENER · ANNOT (Figure 20 property options chart + Figure 21 options table) · PROSE · DEFEND · PROSE (succession) · TABLE (Figure 22).
**Budget:** ≈400 words + figures; fits with ≈4mm to spare (test render 30 Sep). **Status:** draft.
**Case asks for:** retain, refinance, partially monetise or downsize; wills, trusts, succession, powers of attorney,
philanthropy. **Family concern 8:** relocating to another district.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 09 Property, succession and legacy

- Finding-heading: **Keep the home now, decide at 65, and sign the papers this quarter so the choice stays open.**

**Figure 20 · Security and legacy by property option**

`figures/property-options-half.png`

*Source: team model, 10,000 simulations; HKMC terms.*

**Figure 21 · The options at 2037**

| Option | Lasts to 89 | To heirs |
|---|---|---|
| Keep, no release | {{prop_keep_89}} | {{legacy_keep}} |
| Reverse mortgage | {{prop_rmp_89}} | {{legacy_rmp}} |
| Downsize to HK$7M | {{prop_down_89}} | {{legacy_down}} |

*Today's money; with the annuity, lower survivor spending and the business sale.*

**Refinance? Not now; clear it at 65.** The mortgage costs about 3.5%, close to what cash earns, and its interest is tax-deductible. We compare it each year with new H-plans, capped at 3.25%, and switch only if the saving clears the fees. About HK$0.46M will still be owed in 2037; it is repaid from the portfolio then, because the reverse mortgage needs a home free of other loans. **Ownership:** we assume the parents hold the flat as joint tenants, so it passes to the survivor outside the will; a land search in month 1 confirms it. **Another district:** the HK$7M replacement need not be in Tai Kok Tsui; a cheaper district buys more space, or releases more money.

**Downsizing is the stronger financial answer; the reverse mortgage buys the right to stay.** Downsizing matches the reverse mortgage on security and leaves about {{legacy_down_vs_rmp}} more to Ryan and Chloe; the ≈HK$4.5M released before costs joins the portfolio, and the income floor becomes the annuities plus the cash reserve. HKMC's reverse mortgage pays a fixed income for life, lets both parents stay in the home and is non-recourse, at the cost of a smaller legacy. The choice depends on how much staying in Tai Kok Tsui matters to them, so we set the decision for 2037 and keep both options open; delaying the reverse mortgage to 2045 would lower the plan from {{ladder_5_89}} to {{rmp2045_89}}.

**Succession: control, not tax**

Estate duty was abolished in 2006, so succession planning here is about control, liquidity and staging. Without wills, the intestacy rules would pass about HK$1.1M each to Ryan and Chloe on Adrian's death, and on both deaths about HK$11.9M each, unstructured, with no guardian named for Chloe. MPF balances have no beneficiary nomination: before 2037 they are paid to the estate once probate is granted, so the wills cover them and the joint account bridges the wait.

**Figure 22 · The three documents the family needs**

| Document | Covers | Key point |
|---|---|---|
| Mirror wills | Estate and MPF | Staged trusts at 25, 30, 35; a guardian for Chloe |
| Enduring powers of attorney | Property, money | Needed before any reverse mortgage or sale |
| Advance directives | Medical care | New statutory form, in force since 31 July 2026 |

---

## Page 12 · §9 continued · §10 Roadmap

**Layout:** PROSE (business, governance, philanthropy) · OPENER (§10) · TABLE (Figure 23).
**Budget:** ≈90 words + table; ≈33mm to spare (test render 30 Sep). **Status:** draft.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 09 Property, succession and legacy · continued

**The business, passed on in stages.** A shareholders' and buy-sell agreement funded by key-person cover now; managers built up from 55; a staged sale between 58 and 62 to her co-founder and managers. **Why sell rather than keep the shares for dividends:** most of the HK$720K Carmen draws is pay for running the company. Once a manager is paid, the dividend left is uncertain, depends on a firm built around her, and ranks behind the business loan; a sale turns it into money the plan can count on. Hong Kong taxes neither dividends nor capital gains, so tax does not decide it. We count only HK$3.0M of the HK$5.0M value, the price a forced sale might fetch, so the plan does not depend on a good sale; with no sale at all it still reaches 66%, and any dividend is a bonus. **Family governance:** a short family charter and one annual meeting where all four review the plan. **Legacy with purpose:** a named scholarship in sustainable design, about HK$30K a year through a registered charity, joins Carmen's mission to Chloe's interest in design; donations are tax-deductible.

- Label: 10 Implementation roadmap

- Finding-heading: **Every gap closes in the first year; after that, dates and events trigger each decision.**

**Figure 23 · Roadmap**

| When | Action | Owner | Effect |
|---|---|---|---|
| Next 12 months |  |  |  |
| Month 1 | Wills, guardian, powers of attorney; land search | Parents | < HK$25K once |
| Month 1 | Joint account; idle cash to deposits; clear the card | Parents | ≈HK$39K a year |
| Months 1–3 | Disability, life, CI and VHIS cover; Ryan's cover | Family | HK$100K, year 1 |
| Months 1–3 | Buy-sell agreement; key-person cover | Carmen | Company pays |
| Months 1–6 | A portfolio each; policy signed; voluntary MPF | Family | Saves ≈HK$45K |
| Month 12 | First family meeting; Ryan's plan; family charter | All four | — |
| 3–5 years |  |  |  |
| Early 2028 | Chloe accepts an offer: convert years 1–2 of fees | Parents | No currency risk |
| Every year | Rebalance; review mortgage, cover, ESG list | Adviser | — |
| Into retirement and legacy |  |  |  |
| 2032 | Managers built up; Chloe starts work, own plan | Family | — |
| 2034–36 | Adrian to 35% equity | Adrian | — |
| 2037 | Clear mortgage; Adrian's annuity; release home | Parents | {{step_home}} points |
| 2039 | Carmen's annuity; business sold; guardrails begin | Carmen | {{step_business}} points |
| 2047 | Adrian 75: review the medical tier | Parents | {{ladder_5_89}} → {{switch_89}} |

*Effect: the saving a year, or the change in the chance the money lasts to Carmen's 89. Full reviews follow a death, a disability, a business sale, a 20% market fall or a 1.5-point rate move.*

---

## Page 13 · §11 Risk and compliance

**Source:** `drafts/10-11-roadmap-risk.md` + Win's regulatory matrix; stress results from `run_model.py` (`rec_*`).
**Layout:** OPENER · ANNOT (Figure 24 stress chart `figures/stress-half.png` + Figure 25 likelihood-impact matrix) ·
TABLE (Figure 26 register, compliance in its source line). The sensitivity chart is not placed; its numbers are in the register.
**Case asks for:** financial planning, suitability, ethical, product, regulatory and behavioural risks.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: 11 Risk and compliance

- Finding-heading: **Before retirement the largest risk is lost income; after it, low returns and inflation.**

**Figure 24 · The plan holds under stress**

`figures/stress-half.png`

*Chance the money lasts to Carmen's 89.*

**Figure 25 · Likelihood and impact**

Matrix (likelihood low → high, left to right): High impact: P1 | F1F3F6 | F2; Medium impact: E1P2 | F4F5B2 | ·; Low impact: · | R1R2E2 | B1

*Our rules: tier review at 75 plus guardrails (§3). With low returns every year they trim spending to about {{rec_lowret_typical_pct}} of the budget, not let it run out.*

**Figure 26 · Every risk has a measured impact and a named defence**

|  | Risk | Fixed spending | Our rules | Defence |
|---|---|---|---|---|
| **F1** | Inflation 3.5%, not 2.5% | {{cpi_stress_89}} | {{rec_cpi_89}} | Guardrails; shorter bonds |
| **F2** | Medical costs 8.5% a year | {{med_stress_89}} | {{rec_med_89}} | Tier review at 75 |
| **F3** | Low returns every year | {{stressA_89}} | {{rec_lowret_89}} | Guardrails; Treasury ladder |
| **F4** | Business not sold | {{biz_not_sold_89}} | {{rec_biz_89}} | Buy-sell agreement now |
| **F5** | Carmen lives to 95 | {{ladder_5_95}} | {{guardswitch_95}} | Annuities pay for life |
| **F6** | Money runs out, base case | {{fixflex_89}} | {{guardswitch_89}} | Annual review; agreed steps |
| **B2** | Selling in a crash | {{rebal_drift_89}} | — | 5-point rebalancing bands |
| **P1** | Disability before retirement | Highest ranked |  | Disability income cover (§8) |
| **P2** | Irreversible choices | Smaller legacy |  | Annuitise only the MPF |
| **B1** | Different risk appetites | Family conflict |  | One portfolio per person |
| **R1** | Crypto rules or licences | Ryan's holdings |  | Regulated channels only |
| **R2** | Greenwashing | ESG goal missed |  | Two ratings; replace in 3 months |
| **E1** | Suitability, joint clients | Unsuitable advice |  | One risk profile per person |
| **E2** | Model risk | False precision |  | Compare decisions; not forecasts |

*F financial · P protection · B behavioural · R regulatory · E ethical. Lasts to Carmen's 89 (F5: 95).*

**Compliance before any purchase.** A risk profile for each person; Ryan's crypto knowledge test; fees and conflicts disclosed; no policy surrendered for new cover; regulated products only; no commission.

**Notes.** F3 and Figure 24 "low returns every year": the stress applies to every year to 2066, not a decade
(Fahtai M1); a true decade 2037–46 gives 66% / 100%. Figure 24 B is inflation plus medical costs (M2); F1 is inflation alone.
Other stress numbers for the text if space allows: typical spending under the plan {{rec_cpi_typical}} (inflation),
{{rec_stressB_typical}} and {{rec_stressB_89}} (inflation + medical together).

---

## Page 14 · Personal statement

**Layout:** OPENER · WMC analysis · four career paragraphs. **Budget:** ≈520 words.
**Rules:** "discussion of personal career goal and opportunities under the cross-boundary wealth management connect
scheme". No names of universities; first names only.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: Personal statement

- Finding-heading: **Four planners, one question: how Hong Kong's advisers serve families across the Greater Bay Area.**

**The opportunity: Wealth Management Connect**

Since 2021 the Cross-boundary Wealth Management Connect has let residents of Hong Kong, Macao and nine mainland cities of the Greater Bay Area invest across the boundary through their banks, and since 2024 through licensed securities firms as well. The 2024 changes raised each investor's limit from RMB 1 million to RMB 3 million, within an aggregate quota of RMB 150 billion in each direction, and widened the funds on offer; a further round is under discussion. It is a growing market for advisers in both directions. Southbound, mainland investors buy Hong Kong funds and deposits, and need advisers who can explain those products, and their risks, to clients used to a different system. Northbound, Hong Kong families who live and work across the boundary can hold renminbi wealth products through banks in the Greater Bay Area. The Wongs are such a family: Adrian's work spans Hong Kong, the Greater Bay Area and Southeast Asia. We kept Northbound products out of today's plan, because the family's income, home and business already sit in one region and renminbi products would add to that concentration. If Adrian's role moves across the boundary, or the parents choose to retire there, it becomes the natural tool, and the annual review is where that decision sits. That is the skill this proposal needed: knowing two markets' products, rules and tax well enough to say when to use them, and when not to.

**Our career goals** (≈70 words each, first person; first names only. The test render has ≈58mm spare with four
70-word paragraphs, so each may run to ≈100 words.)

Each member answers three questions in one paragraph:
1. What role do you want in five years, and in which market (Hong Kong, the Greater Bay Area, elsewhere)?
2. Which part of this proposal did you lead, and what did it teach you about advising a family?
3. What will you learn next to do that role across the boundary (a licence, a qualification, a market)?

- **Pete** `[OWNER: Pete]` — lead adviser; led the model and integration.
- **Win** `[OWNER: Win]` — investment and ESG; fund selection, digital assets.
- **Fahtai** `[OWNER: Fahtai]` — retirement numbers and the appendix.
- **Lookbua** `[OWNER: Lookbua]` — protection, property and the risk register.

---

## Page 15 · Appendix

**Source:** `drafts/appendix.md`, updated to the model. **Status:** draft. **Owner:** Fahtai.
`[CHECK]` every A1 row against the `Inputs` tab of `model/wong_model.xlsx`.
**Wording:** generated from `pages-10-15.html` on 1 Oct (builder). Edit the page source, then this file.

- Label: Appendix

- Finding-heading: **Every number traces to a stated assumption.**

**A1 · Key assumptions**

| Assumption | Base | Stress | Source |
|---|---|---|---|
| CPI | 2.5% | 3.5% | HK CPI 2006–25 |
| Medical costs | 10% → 6% by 2036, plus VHIS age curve | 8.5% flat | Getzen; WTW |
| Equities | 6.0%, 17% volatility | 4.0%, all years | Long-run history |
| Bonds, ladder | 4.0% | 2.5% | US 5-year 5.0% |
| Cash | 3.0% → 2.5% by 2031 | — | Education fund |
| Model mix | 40% equity for all the parents' money | — | Plan holds ≈50% |
| MPF annuities | Single life: {{annuity_adrian}} Adrian 2037, {{annuity_carmen}} Carmen 2039 | — | HKMC rates |
| Business sale | HK$3.0M in 2039, one payment | Not sold | Case, less 40% |
| Mortgage | ≈HK$0.46M still owed, cleared in 2037 | — | Case; derived |
| Reverse mortgage | HK$230K a year for life from 2037 | From 2045 | HKMC |
| New cover | ≈HK$100K year 1; {{premiums_avg}} average | — | Rate cards |
| Medical tier | Standard plan from 2047, same insurer | No review | Insurer terms |
| Guardrails | From 2039: ±10% when withdrawals drift 20%; never below 70% of target | Fixed | Guyton–Klinger |
| After a death | 70% of HK$780K after Adrian's 84 | 100% | Family choice |
| Life expectancy | Adrian 84, Carmen 89 | Carmen 95 | Case |
| Carmen's pay | All HK$720K as salary | — | Case; assumed |

**A2 · Model and method**

One spreadsheet projects income, 2026/27 salaries tax (reproduced to the dollar: HK$181,770), MPF, spending, education, medical premiums and the portfolio for 2026–2072; a Monte Carlo simulation runs 10,000 simulations of annual returns. **Limits:** returns are normal and uncorrelated, which understates crashes; inflation is fixed within each scenario; each mix is held constant. Results compare decisions; they are not forecasts.

**A3 · Sources · A4 · Use of AI tools**

Case study (SRFP&S, 2026) · Inland Revenue Ordinance, Budget 2026/27 · HKMC · Health Bureau VHIS data · WTW, Mercer Marsh Benefits, Aon 2026 · SOA Getzen model · Federal Reserve SEP · HKAB · ECB · fee schedules · insurer rate cards · SFC list of ESG funds · Berg, Kölbel and Rigobon (2022) · Guyton and Klinger (2006) · cover photograph: Peter Steinhauer, *Cocoons*. AI tools were used to check calculations, review the model code and edit text; the analysis and recommendations are the team's own.

**Notes.** Detail the printed A1 leaves out: annuity premiums HK$2.31M and HK$1.81M (mandatory MPF balances only);
critical illness HK$1.5M each; guardrails: essentials 40% never cut, the rest never below half, no cuts in the last 15 years;
the business sale is one unindexed payment in 2039 (≈HK$2.2M today; Fahtai M3); the cash rate is used only for the
education fund (M4). `[CHECK]` every A1 row against the `Inputs` tab of `model/wong_model.xlsx`.

---

## Charts (all drawn by `model/make_charts.py`; rerun after any model change)

| Figure | File | Width |
|---|---|---|
| 3 · Cash flow | `cashflow-half.png` | half |
| 6 · Decision ladder | `decision-ladder-half.png` | half |
| 8 · Medical premiums | `medical-premiums-half.png` | half, paired |
| 9 · Portfolio fan chart | `fan-chart-half.png` | half, paired |
| 12 · Education cost by destination | `education-costs-half.png` | half |
| 20 · Property options | `property-options-half.png` | half |
| 24 · Stress: fixed spending vs the recommended plan | `stress-half.png` | half |
| — · Sensitivity (not placed; numbers in Figure 26) | `sensitivity-half.png` | half |

Tables and diagrams built in the page: Figures 1, 2, 4, 5, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26.
`allocation-half.png` is still drawn but no longer placed (S19).
Every chart's numbers are in `figures/figure-data.md`.
