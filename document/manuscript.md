# Built to Last — Manuscript (page by page)

**What this is:** the exact words, figures and tables for every page of the Round One proposal, in page order.
The HTML document is assembled from this file; edit wording here, not in the HTML.
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
  `[DRAW]` a chart still to be made.

## Page map

| Page | Section | Owner | Status |
|---|---|---|---|
| 1 | Cover | Pete | Final |
| 2 | Executive summary | Pete | Draft, finalise last |
| 3 | §2 Cash flow and net worth; goals | Pete | Draft |
| 4–5 | §3 Retirement | Pete, Fahtai | Final (from mock-up v3) |
| 6 | §4 Education | Pete | Draft |
| 7 | §5 Investment and allocation | Win | Draft, HK$ sizes to confirm |
| 8 | §5 cont. · §6 ESG | Win | Draft |
| 9 | §7 Digital assets · Ryan's own plan | Win, Pete | Draft |
| 10 | §8 Protection | Lookbua | Draft |
| 11 | §9 Property · succession | Lookbua, Pete | Draft |
| 12 | §9 cont. legacy · §10 Roadmap | Pete, Lookbua | Draft |
| 13 | §11 Risk and compliance | Lookbua, Win | Draft |
| 14 | Personal statement | All | Placeholders |
| 15 | Appendix | Fahtai | Draft |

## Decisions (resolved 30 Sep, from data)

Each was settled by what serves the family best, then checked against what the judges can verify from the case.

| # | Decision | Resolved as | Evidence |
|---|---|---|---|
| 1 | ESG base | **HK$10.47M**, the case's liquid + investment assets | The case sets the 20–25% target on "investable assets", and its statement totals HK$10.47M. It is also the stricter test: it includes Ryan's non-ESG HK$0.68M and the policy cash values. The plan passes on either base (24% on HK$10.47M; 21% on the freely allocable HK$7.70M), so we state the base a judge can check. |
| 2 | Critical-illness cover | **HK$1.5M each** | Sized by need: treatment not covered by VHIS (HK$0.80M) + three months' pay before disability cover starts (Adrian HK$0.30M, Carmen HK$0.18M) + home and recovery costs (HK$0.25M) = HK$1.35M and HK$1.23M. The HK$2.75M draft also counted two years' spending, which disability cover and the reserve already provide. Saves ≈HK$46K a year (HK$0.45M over ten years) with no gap. Year-1 cost of all new cover: ≈HK$100K. |
| 3 | Portfolio sizes and equity | **Emergency HK$1.0M · education HK$2.57M · long-term HK$4.13M, split 50:50; Adrian 40% equity, Carmen 60%** | Emergency: 12 months, the top of the 6–12 month benchmark, because Carmen's income depends on her business and she guarantees its loan. Education: the present value of the top-of-range overseas budget. In the model, household equity above 40% adds legacy, not security (40%: 100% to 89, worst year −10%; 54%: 99.6%, −15%), so Carmen's portfolio is set at 60% rather than 68%, keeping the family objective of "moderate growth with controlled downside". Her ESG sleeves are unchanged. `[OWNER: Win]` move 8 points of Carmen's growth and HK equity to bonds. |
| 4 | The HK$85K card balance | **Assume revolving** (the case says "credit card and revolving balance") | Clearing it is right either way: it costs nothing but 0.2% on idle savings, against ≈30% card interest. §2 states the assumption and the saving (≈HK$25K a year if it revolves). |
| 5 | Tax assessment | **Assume separate** (the default in Hong Kong) | §2 presents the HK$18K as a check: if the family has elected joint assessment, revoking it saves HK$18K a year. |

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

**Layout:** OPENER · number band (4) · sidebar (pull quote, Figures 1–2) + main text · five recommendations.
**Budget:** ≈330 words. **Owner:** Pete. **Status:** draft; finalise after all sections.

- Label: EXECUTIVE SUMMARY
- Finding-heading: **The Wongs have done the hard part. Four decisions they control make it last.**
- Number band:
  - **HK$24.4M** net worth, with only 10% leverage
  - **HK$718K** saved each year: 41% of after-tax income
  - **{{ladder_1_89}} → {{ladder_5_89}}** chance the money lasts to Carmen's 89, before and after
  - **HK$100K** a year closes every protection gap

**Sidebar**

- Pull quote: *Medical premiums, not markets, are the largest threat to the family's retirement.*
- **Figure 1 · The family**

  | Member | Risk profile |
  |---|---|
  | Adrian, 54 | Low–medium |
  | Carmen, 49 | Medium–high |
  | Ryan, 24 | High |
  | Chloe, 16 | — |

- **Figure 2 · Where the wealth sits, HK$M**

  | | |
  |---|---|
  | Home, Tai Kok Tsui | 11.50 |
  | Carmen's business | 5.00 |
  | Investments incl. MPF | 7.97 |
  | Cash and deposits | 2.50 |
  | Other | 0.22 |
  | Less liabilities | (2.79) |
  | **Net worth** | **24.41** |

**Main text**

> The Wongs have already done the hard part: a HK$24.4M balance sheet, over 40% of after-tax income saved each year
> (parents only, HK$718K of HK$1.74M), and only 10% leverage. Our plan makes it last, for four people with four
> different views of risk.

**Protect what has been built.** Close the disability and critical-illness gaps, and sign wills, a guardian nomination
and powers of attorney this quarter (§8, §9).

**Turn assets into lifelong income.** On their investments alone, the money lasts to Carmen's 89 in {{ladder_1_89}} of 10,000
simulated markets. An MPF annuity, lower spending after the first death, a staged sale of Carmen's business and a
planned use of the home raise it to {{ladder_5_89}}; moving to the Standard medical plan at 75 raises it to {{switch_89}} (Figure 6).

**Give every voice a place.** Adrian keeps a 40/60 portfolio; the family reaches 24% ESG; Ryan keeps his digital assets on a
glide path; Chloe chooses her university freely (§4–§7).

**Five recommendations**

1. **Close the protection gaps** for disability, life and critical illness: ≈HK$100K a year until retirement.
2. **Sign wills, a guardian nomination and powers of attorney** within three months, for under HK$25K.
3. **Both parents buy individual medical cover now**, before group cover ends at 65 and 62.
4. **At 2037, turn the MPF and the home into income**: annuity plus reverse mortgage or downsizing.
5. **Adopt one written family policy**: a portfolio per person, rebalancing bands, spending guardrails.

---

## Page 3 · §2 Cash flow and net worth · goals

**Layout:** OPENER · ANNOT (Figure 3 cash-flow chart + Figure 4 health check) · PROSE · DEFEND · TABLE (Figure 5 goals).
**Budget:** ≈330 words + two tables. **Owner:** Pete. **Status:** draft.
**Case asks for:** financial health, liquidity, leverage, debt servicing, emergency reserve, wealth concentration.

- Label: 02 CASH FLOW AND NET WORTH
- Finding-heading: **The Wongs start from strength. Their risks are concentration and the costs the budget leaves out.**

**ANNOT**

- Left: **Figure 3 · Where each year's income goes** `[DRAW]` half-width waterfall, parents only, low bonus:
  income 1,920,000 → salaries tax −181,770 → MPF −36,000 → household spending −984,000 → surplus **718,230**.
  Source: case; team tax model (2026/27, separate assessment).
- Right: **Figure 4 · Health check**

  | Measure | Wongs | Verdict |
  |---|---|---|
  | Savings rate | 41% of after-tax income | Strong |
  | Emergency reserve | 30.5 months of spending | Excess (benchmark 6–12) |
  | Leverage | 10% debt to assets | Low |
  | Mortgage service | ≈8.5% of gross income | Comfortable |
  | Concentration | 61% in home and business | High |

**PROSE**

**Strong, liquid and lightly borrowed.** The parents save HK$718K a year after tax and MPF, and hold HK$2.5M in cash
and deposits: 30 months of spending, far above the 6–12 months a household needs. Debt is 10% of assets, and the
mortgage costs about 8.5% of gross income.

**Two risks sit behind the strength.** First, concentration: the home and Carmen's business are 61% of the family's
assets, and neither pays an income until it is sold or borrowed against. Second, the HK$82K a month excludes profits
tax on Carmen's business, overseas travel, renovation and medical emergencies; the surplus must cover these before it
is invested. New protection cover (§8) will take a further ≈HK$100K a year until retirement.

**DEFEND — Put idle money to work before taking more risk.** The easiest gains need no extra risk. Moving HK$500K from
savings accounts at 0.2% into deposits and a money-market fund at about 3% adds ≈HK$14K a year; clearing the HK$85K card
balance saves ≈HK$25K of interest if it revolves `[CHECK]`; tax-deductible voluntary MPF and deferred-annuity
contributions of HK$60K each save ≈HK$20K of tax. Separate assessment already beats joint by HK$18K; we confirm the
family files that way `[CHECK]`. The reserve falls to twelve months (≈HK$1.0M) in a joint account both parents can reach.

**TABLE · Figure 5 · The family's goals, ranked**

| Priority | Goal | Measure of success | When |
|---|---|---|---|
| Need | Retire at 65 and 62 on HK$780K a year | Money lasts to Carmen's 89 in {{ladder_5_89}} of markets | 2037, 2039 |
| Need | Protect income, health and the family | All gaps in §8 closed; wills and EPAs signed | Within 3 months |
| Need | Fund Chloe's degree without debt | HK$2.57M education fund ring-fenced | 2028–2032 |
| Want | Align 20–25% of investable assets with ESG | 24% on a HK$10.47M base | 2027 |
| Want | Ryan financially independent | Crypto ≤20% of his wealth by 35; own cover | By 2037 |
| Wish | Legacy with purpose | Staged trusts; an education scholarship | Ongoing |

---

## Pages 4–5 · §3 Retirement

**Status:** final. Source of truth: `document/section-mock-v3.html` (pages 1–2). Owner: Pete; numbers Fahtai.
**Case asks for:** on track at 65/62? accumulation, drawdown and liquidity strategies.

Figures on these pages: **6** decision ladder (`decision-ladder-half.png`) · **7** when each decision is taken (table) ·
**8** medical premiums (`medical-premiums-half.png`) · **9** portfolio fan chart (`fan-chart-half.png`) ·
**10** income floor (table) · **11** tier review and guardrails (table: fixed spending {{fixflex_89}} → tier review {{fixswitch_89}} →
guardrails {{guardswitch_89}}; typical spending {{fixswitch_typical}} → {{guardswitch_typical}}; worst-5% lowest year {{fixswitch_worst5}} → {{guardswitch_worst5}}) · subsection
*What the guardrails cost, and what they buy* (≈HK$31K a year for the typical family; pre-agreed steps). Figures after 11 renumber at assembly.

`[CHECK]` Add a small "annuity bought" label at 2037 on Figure 9, where the median dips.

---

## Page 6 · §4 Education

**Layout:** OPENER · ANNOT (Figure 11 costs by destination + Figure 12 funding timeline) · PROSE · DEFEND.
**Budget:** ≈330 words. **Owner:** Pete. **Status:** draft.
**Case asks for:** local and overseas scenarios, timing, funding vehicles, contingency.

- Label: 04 EDUCATION PLANNING
- Finding-heading: **Chloe's choice should not depend on the exchange rate. The fund is already there; it stays in HK
  dollars until she accepts an offer.**

**ANNOT**

- Left: **Figure 11 · Annual cost by destination, 2028/29 prices** `[DRAW]` half-width version of
  `education-costs.png`. Source: Statistics Canada, UBC, IRCC, NTU, Save the Student; team FX analysis.
- Right: **Figure 12 · Funding timeline**

  | When | Action |
  |---|---|
  | Now | Ring-fence HK$2.57M from deposits and bond funds |
  | Early 2028 | Offers arrive: convert years 1–2 that month |
  | 2029–2031 | Convert each later year 12 months ahead |
  | Any time | Unused money returns to retirement |

**PROSE**

**The budget.** We plan on the family's own top figure, HK$600K a year in today's money, rising 5% a year: HK$662K in
2028/29 and HK$2.85M over four years. Set aside today at a 3% deposit rate, that needs **HK$2.57M**, which the family
already holds in time deposits, a money-market fund and bond funds. No new saving is required.

**What each choice costs.** At 2028/29 prices the UK costs HK$335–555K a year and Canada HK$400–554K, both inside the
budget even after a severe currency move (+10% for sterling, +14% for the Canadian dollar). Singapore costs HK$224–271K
with the Tuition Grant, which requires three years' work in Singapore after graduation. A Hong Kong degree costs
HK$150–250K; tuition itself is HK$49,500 in 2027/28, set by the government.

**DEFEND — Deposits, not equities, and HK dollars until an offer.** Money needed in two to six years cannot wait out
a market fall, so the fund stays in deposits, a money-market fund and short bonds. Buying foreign currency early would
cost 0.5–2 points a year of interest for a destination not yet chosen. If Chloe studies locally, about HK$1.5M returns
to the retirement portfolio. If a currency moves against the family on years 3–4, the shortfall is at most ≈HK$90K a
year, paid from surplus. Chloe's choice is hers; the plan funds all four.

---

## Page 7 · §5 Investment and allocation

**Layout:** OPENER · ANNOT (Figure 13 current vs target allocation + Figure 14 buckets) · PROSE · TABLE (Figure 15).
**Budget:** ≈300 words + tables. **Owner:** Win. **Status:** draft; sizes and equity per decision 3.
**Case asks for:** cash and deposits, bonds, equities and funds, ESG, digital; target allocation, rationale,
product suitability, risk management, monitoring and rebalancing.

- Label: 05 INVESTMENT PLANNING
- Finding-heading: **One family policy, three portfolios: each sized to its owner's risk and to when the money is needed.**

**ANNOT**

- Left: **Figure 13 · From today's holdings to the target** `[DRAW]` half-width stacked bars, current vs target, by
  cash · bonds · Treasury ladder · equity · ESG · digital. Source: case; team allocation.
- Right: **Figure 14 · Five buckets** `[OWNER: Win]` confirm sizes

  | Bucket | HK$ | Held in |
  |---|---|---|
  | Emergency (12 months) | 1.00M | Joint account, deposits, MMF |
  | Chloe's education | 2.57M | Deposits, short bonds |
  | Adrian's portfolio | 2.07M | 40/60, Treasury ladder |
  | Carmen's portfolio | 2.07M | 60/40, ESG-led |
  | Ryan's own | his own | See §7 |

**PROSE**

**Match each portfolio to its owner.** One blended household portfolio would be too risky for Adrian and too cautious
for Ryan. Adrian's is 40% equity and 60% bonds and cash, anchored by US Treasuries maturing each year from 2037 to 2041
that pay his first five years of retirement whatever markets do. Carmen's is 60% equity, led by ESG funds (§6): in our model, equity above 40% of the household total adds
legacy but not security, so her share stays within the family's objective of moderate growth. Every
holding is a low-cost index fund or ETF, SFC-authorised or HKEX-listed; Irish-domiciled funds avoid US estate tax.

**DEFEND — Why not all Treasuries for Adrian.** Treasuries at about 5% look sufficient, but after 3.5% inflation they
leave 1.5% real, below what the plan needs, and bonds bought today mature by 2041 while the money must last to 2066.
In our simulation an all-Treasury ladder fails almost every time once medical costs are included. So the ladder
provides the floor and the equity provides the growth.

**TABLE · Figure 15 · Rules agreed in advance** (Win's M1–M9; test result from `run_model.py` §9)

| If | Then |
|---|---|
| Global equities fall 20% or more | Rebalance to target by selling bonds; never sell equities |
| Any holding drifts 5 points from target | Rebalance, using new money first |
| 5-year Treasury ≥ 4.5% | Lock yields in the ladder (triggered Sep 2026) |
| HK inflation > 3.5% for two quarters | Shorten bond maturities |
| Chloe accepts an offer | Convert years 1–2 of fees that month |

Line under the table: *In our test, 5-point bands did as well as rebalancing every year ({{rebal_bands_89}}); never rebalancing
gave {{rebal_drift_89}}.*

---

## Page 8 · §5 continued · §6 ESG

**Layout:** PROSE (§5 close) · OPENER (§6) · TABLE (Figure 16) · PROSE · DEFEND.
**Budget:** ≈420 words + table. **Owner:** Win. **Status:** draft; base per decision 1.
**Case asks for (§6):** strategic role, selection criteria, benefits and limitations, greenwashing mitigation.

**§5 close — PROSE**

**Value added without extra risk.** Moving about HK$4.4M of fund holdings from typical fees near 1.5% a year to index
funds near 0.15% saves ≈HK$59K a year `[CHECK: current-fee assumption]`; with the idle-cash and tax measures in §2 the
family gains ≈HK$120K a year before any change in risk. The portfolios are reviewed each quarter and at an annual family
meeting.

**§6 OPENER**

- Label: 06 ESG INTEGRATION
- Finding-heading: **Carmen's values, invested with evidence: from 11% to 24% ESG, with no return premium assumed.**

**TABLE · Figure 16 · How the family reaches 24%** (base HK$10.47M, decision 1; Win to confirm)

| Source | HK$M |
|---|---|
| Today: ESG equity funds 0.70 + green bonds 0.45 | 1.15 (11%) |
| Adrian: ESG-screened global core 25%, ESG equity 5%, green bonds 5% | 0.72 |
| Carmen: ESG equity 35%, green bonds 10% | 0.93 |
| MPF: 50% of each parent's balance in its ESG constituent fund | 0.84 |
| **Total at target** (the "today" row is for comparison, not added) | **2.49 (24%)** `[CHECK: Win]` |

**PROSE**

**Four layers, one standard.** Exclusions remove thermal coal, controversial weapons and tobacco; best-in-class funds
hold the highest-rated companies in each sector; a thematic slice in circular economy echoes Carmen's own packaging
business; green bonds with checked use of proceeds add direct impact. Every fund must be on the SFC's list of ESG funds.

**Greenwashing, tested not trusted.** ESG ratings from different agencies agree far less than credit ratings: their
correlation is about 0.54, against about 0.92 (Berg, Kölbel and Rigobon, 2022). A fund therefore enters only if it
passes two ratings (MSCI A or better and Sustainalytics risk below 20) and a holdings check; a downgrade triggers
replacement within three months.

**DEFEND — No return premium assumed.** The evidence for higher returns from ESG is mixed, so ESG funds are modelled
at the same returns as their asset class. The case for them is Carmen's values and lower exposure to stranded-asset
risk, at almost no extra cost. The limitation is a smaller universe of funds in Hong Kong; government tokenised green
bonds stay on a watch-list until retail investors can buy them.

---

## Page 9 · §7 Digital assets · Ryan's own plan

**Layout:** OPENER · TABLE (Figure 17 suitability by person) · PROSE · ANNOT-style box for Ryan (Figure 18 glide path).
**Budget:** ≈380 words + tables. **Owner:** Win (§7), Pete (Ryan). **Status:** draft.
**Case asks for:** suitability, volatility and downside, regulation and platform risk, custody and security,
allocation limits, implementation options. **Family goal 3:** Ryan's savings, investment, protection, retirement.

- Label: 07 DIGITAL ASSETS
- Finding-heading: **Not yes or no: form, size and custody, set for each person.**

**TABLE · Figure 17 · Digital assets by family member**

| Person | Crypto exposure | Vehicle | Why |
|---|---|---|---|
| Adrian | 0% | Tokenised money-market fund only, counted as cash | Capital preservation |
| Carmen | Optional, ≤ 2% of her portfolio | HKEX spot bitcoin ETF | Removes custody and fraud risk |
| Ryan | Glide path to ≤ 20% by 35 | HKEX spot ETFs or SFC-licensed platforms | Long horizon, strong conviction |
| Chloe | None | — | Education money must be safe |

**PROSE**

**Size limits the damage; regulation limits the channels.** Bitcoin fell about 24% in the year to September 2026 and
has fallen more than 70% in past cycles, so exposure is set by what each person can lose. All holdings sit with
SFC-licensed platforms or in HKEX-listed ETFs; if a platform loses its licence, holdings move to an ETF within 30 days.
Self-custody requires a documented key-recovery plan: without it, digital assets cannot be inherited.

**Ryan's own plan.** Ryan earns HK$300K and saves 30% (HK$90K a year) after keeping three months' spending in cash.
New savings go to a global equity portfolio, and none to crypto while he is above his glide path, so his crypto share
falls without any forced selling (Figure 18). He adds term life and critical-illness cover for about HK$900 a year,
starts voluntary MPF contributions, and his parents match 50% of his savings up to HK$24K a year.

**Figure 18 · Ryan's crypto share of his wealth, by savings rate**

| Ryan saves | at 30 | at 35 |
|---|---|---|
| 20% (HK$60K) | 37% | 24% |
| **30% (HK$90K)** | **32%** | **20%** |
| 40% (HK$120K) | 28% | 17% |

Line under the table: *Today about 74% if all HK$500K is crypto; the tokenised money-market share is to be confirmed
`[CHECK: Ryan's split]`.*

**DEFEND — Why keep any digital assets.** Selling Ryan's holdings would ignore his stated conviction and his high risk
profile; doubling down would breach the family's objective of moderate growth with controlled downside. The glide path
respects both: it is his money, but its share of his wealth falls as he builds everything else.

---

## Page 10 · §8 Risk management and protection

**Source:** `drafts/08-protection.md` (Lookbua), with critical-illness cover at HK$1.5M each (decision 2). **Status:** draft.
**Layout:** OPENER · sidebar numbers (2) + intro · TABLE (Figure 19 protection needs) · PROSE (A–E) · DEFEND.
**Case asks for:** mortality, medical, critical illness, disability, business continuity, family emergency plan.

- Label: 08 RISK MANAGEMENT AND PROTECTION
- Finding-heading: **The largest gap is income, not death: neither parent could replace their salary if disabled.**
- Sidebar: **HK$100K** a year closes every gap: 14% of the surplus, paid only until retirement ·
  **< HK$25K** once, for wills, a guardian for Chloe and powers of attorney
- Intro: as in the draft (failure-mode ranking of fifteen risks; disability ranks first and second).
- **Figure 19**: the protection table from the draft, with critical illness at **HK$1.5M each** (row: *treatment gap +
  3 months' pay*; year-1 premium ≈HK$41K) and the total at **≈HK$100K**. Add one line under it: *Sized by need;
  a larger lump sum would duplicate the disability cover and the emergency reserve.*
- A) Disability first · B) Life cover fills a defined gap · C) Medical cover now, not at retirement ·
  D) The business survives Carmen · E) Ryan starts small — text as in the draft, cut to fit.
- **Family emergency plan** (add, 2 lines, required by the case): a joint account with twelve months' spending, a
  one-page list of policies, accounts and contacts, and named emergency contacts for Chloe.
- **DEFEND** `[OWNER: Lookbua]` two sentences: why term cover plus disability income, rather than more whole-life
  cover (cost per dollar of cover; the need ends at retirement).

---

## Page 11 · §9 Property · succession

**Source:** `drafts/09-property.md` (Lookbua) + working brief §3.6 (Pete).
**Layout:** OPENER · ANNOT (Figure 20 property options chart + Figure 21 options table) · DEFEND · PROSE (succession).
**Budget:** ≈380 words + figures. **Status:** draft.
**Case asks for:** retain, refinance, partially monetise or downsize; wills, trusts, succession, powers of attorney,
philanthropy.

- Label: 09 PROPERTY, SUCCESSION AND LEGACY
- Finding-heading: **Keep the home now, decide at 65, and sign the papers this quarter so the choice stays open.**

**ANNOT**

- Left: **Figure 20 · Security and legacy by property option** `[DRAW]` half-width version of `property-options.png`.
- Right: **Figure 21 · The options at 2037**

  | Option | Money lasts to 89 | Left to heirs |
  |---|---|---|
  | Keep, no release | {{prop_keep_89}} | {{legacy_keep}} |
  | Reverse mortgage | {{prop_rmp_89}} | {{legacy_rmp}} |
  | Downsize to HK$7M | {{prop_down_89}} | {{legacy_down}} |

  Note: today's money; with annuity, lower survivor spending and the business sale.

**PROSE — property**

**Refinance? Not now.** The mortgage costs about 3.5%, close to what cash earns, and its interest is tax-deductible.
We compare it each year with new H-plans, capped at 3.25%, and switch only if the saving clears the fees.

**DEFEND — Downsizing is the stronger financial answer; the reverse mortgage buys the right to stay.** Downsizing
matches the reverse mortgage on security and leaves about {{legacy_down_vs_rmp}} more to Ryan and Chloe. HKMC's reverse mortgage pays
a fixed income for life and lets both parents stay in the home, at the cost of a smaller legacy. The choice depends on
how much staying in Tai Kok Tsui matters to them, so we set the decision for 2037 and keep both options open.

**PROSE — succession**

**Control, not tax.** Estate duty was abolished in 2006, so succession planning here is about control, liquidity and
staging. Without wills, the intestacy rules would pass about HK$1.1M each to Ryan and Chloe on Adrian's death, and on
both deaths about HK$11.9M each, unstructured, with no guardian named for Chloe.

---

## Page 12 · §9 continued · §10 Roadmap

**Layout:** TABLE (Figure 22 three documents) · PROSE (trusts, business, philanthropy) · OPENER (§10) · TABLE (Figure 23).
**Budget:** ≈220 words + two tables. **Status:** draft.

**TABLE · Figure 22 · The three documents the family needs**

| Document | Covers | Key point |
|---|---|---|
| Mirror wills | The estate | Staged trusts for the children at 25, 30 and 35; a guardian for Chloe |
| Enduring powers of attorney | Property and money | Needed before any reverse mortgage or sale; signed before a solicitor and a doctor |
| Advance directives | Medical treatment | New statutory form, in force since 31 July 2026 |

**PROSE**

**The business, passed on in stages.** A shareholders' and buy-sell agreement funded by key-person cover now; managers
built up from 55; a staged sale between 58 and 62, with no capital gains tax. We count only HK$3.0M of its HK$5.0M value
in the plan. **Family governance:** a short family charter and one annual meeting where all four review the plan.
**Legacy with purpose:** a named scholarship in sustainable design, about HK$30K a year through an existing registered
charity, joins Carmen's mission to Chloe's interest in design; donations are tax-deductible.

- Label: 10 IMPLEMENTATION ROADMAP
- Finding-heading: **Twelve actions in twelve months, then reviews that events trigger.**

**TABLE · Figure 23 · Roadmap** — from `drafts/10-11-roadmap-risk.md`, grouped by the case's three horizons:
*Next 12 months* · *3–5 years* · *Into retirement and legacy*. Columns: When · Action · Owner · Effect.
Close with: *Full reviews follow a death, a disability, a business sale, a 20% market fall or a 1.5-point rate move.*

---

## Page 13 · §11 Risk and compliance

**Source:** `drafts/10-11-roadmap-risk.md` + Win's regulatory matrix. **Status:** draft.
**Layout:** OPENER · ANNOT (Figure 24 risk matrix + intro) · TABLE (Figure 25 register) · PAIR (Figures 26–27) `[DRAW]`
half-width stress-scenario and sensitivity charts, if space allows; otherwise cite them in the register.
**Case asks for:** financial planning, suitability, ethical, product, regulatory and behavioural risks.

- Label: 11 RISK AND COMPLIANCE
- Finding-heading: **Inflation and medical costs are the largest risks; spending discipline defends against both.**
- Register: the nine rows in `template-v2.html` (F1–F5, B1, B2, R1, E2) plus **F6 the portfolio runs down**
  (the markets where fixed spending fails; answered by the tier review and guardrails, §3 Figure 11), **E1 suitability** (joint clients;
  risk profile set at the lowest of tolerance, capacity and need) and **P2 product** (annuity irreversible;
  reverse-mortgage costs).
- Compliance line: every product is SFC-authorised or HKMC-issued; insurance figures are published rates, to be
  replaced by quotes; no commission is earned on any recommendation.

---

## Page 14 · Personal statement

**Layout:** OPENER · four paragraphs · WMC analysis. **Budget:** ≈500 words.
**Rules:** "discussion of personal career goal and opportunities under the cross-boundary wealth management connect
scheme". No names of universities; first names optional `[DECISION]`.

- Label: PERSONAL STATEMENT
- Finding-heading: **Four planners, one question: how Hong Kong's advisers serve families across the Greater Bay Area.**

**The opportunity: Wealth Management Connect** (Pete, ≈200 words)

> The Cross-boundary Wealth Management Connect lets residents of Hong Kong, Macao and nine mainland cities in the
> Greater Bay Area invest across the boundary through their banks and, since 2024, licensed securities firms. Each
> individual may invest up to RMB 3 million, within an aggregate quota of RMB 150 billion each way. For a family like
> the Wongs, with business across the Greater Bay Area, it widens the choice of funds; for advisers it creates demand
> for people who understand both markets' products, rules and tax. A further expansion is under discussion.
> `[CHECK: quota figures and 2024 securities-firm admission against HKMA's current page]`

**Our career goals** `[OWNER: each member, ≈70 words each, first person plural or singular]`

- Pete — `[OWNER: Pete]`
- Win — `[OWNER: Win]`
- Fahtai — `[OWNER: Fahtai]`
- Lookbua — `[OWNER: Lookbua]`

---

## Page 15 · Appendix

**Source:** `drafts/appendix.md` and the appendix page in `template-v2.html` (already cut to fit at 12pt).
**Status:** draft. **Owner:** Fahtai.

- A1 Key assumptions (table) · A2 Model and method · A3 Sources (add: cover photograph credit) · A4 Use of AI tools.
- `[CHECK]` Every A1 row against the `Inputs` tab of `model/wong_model.xlsx`.

---

## Charts still to draw (all half width, 95mm, drawn at print size)

| Figure | Chart | Data |
|---|---|---|
| 3 | Cash-flow waterfall | Tax tab: income, tax, MPF, spending, surplus |
| 11 | Education cost by destination | `figure-data.md`, education table |
| 13 | Current vs target allocation | case holdings; Win's targets |
| 20 | Property options | `run_model.py` §8 |
| 26–27 | Stress scenarios · sensitivity | `figure-data.md` |
