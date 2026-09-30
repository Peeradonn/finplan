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

| Page | Section | Owner | Status (built 30 Sep; free space at the foot) |
|---|---|---|---|
| 1 | Cover | Pete | Built |
| 2 | Executive summary | Pete | Built, 5mm |
| 3 | §2 Cash flow and net worth; goals | Pete | Built |
| 4–5 | §3 Retirement | Pete, Fahtai | Built, 3–4mm |
| 6 | §4 Education | Pete | Built |
| 7 | §5 Investment and allocation | Win | Built; HK$ sizes to confirm |
| 8 | §5 cont. · §6 ESG | Win | Built |
| 9 | §7 Digital assets · Ryan's own plan | Win, Pete | Built |
| 10 | §8 Protection | Lookbua | Built |
| 11 | §9 Property · succession | Lookbua, Pete | Built, 4mm |
| 12 | §9 cont. · §10 Roadmap | Pete, Lookbua | Built |
| 13 | §11 Risk and compliance | Lookbua, Win | Built |
| 14 | Personal statement | All | Built; four career paragraphs still placeholders |
| 15 | Appendix | Fahtai | Built |

## Decisions (resolved 30 Sep, from data)

Each was settled by what serves the family best, then checked against what the judges can verify from the case.

| # | Decision | Resolved as | Evidence |
|---|---|---|---|
| 1 | ESG base | **HK$10.47M**, the case's liquid + investment assets | The case sets the 20–25% target on "investable assets", and its statement totals HK$10.47M. It is also the stricter test: it includes Ryan's non-ESG HK$0.68M and the policy cash values. The plan passes on either base (25% on HK$10.47M; 23% on the freely allocable HK$7.70M), so we state the base a judge can check. |
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

> A HK$24.4M balance sheet, over 40% of after-tax income saved and only 10% leverage: the Wongs have done the hard
> part. What is new here: a decision ladder that prices each choice in points of security, an income floor built from
> the MPF and the home rather than from more risk, and spending rules agreed now that hold the plan at {{guardswitch_89}} for about
> {{guard_cost}} a year.

**Protect what has been built.** Close the disability and critical-illness gaps, and sign wills, a guardian nomination
and powers of attorney this quarter (§8, §9).

**Turn assets into lifelong income.** On their investments alone, the money lasts to Carmen's 89 in {{ladder_1_89}} of 10,000
simulated markets. An MPF annuity, lower spending after the first death, a staged sale of Carmen's business and a
planned use of the home raise it to {{ladder_5_89}}; moving to the Standard medical plan at 75 raises it to {{switch_89}} (Figure 6).

**Give every voice a place.** Adrian keeps a 40/60 portfolio; ESG rises from 11% to 25% of investable assets, the top of
the family's 20–25% target, in SFC-listed funds only; Ryan keeps his digital assets on a glide path; Chloe chooses her university freely (§4–§7).

**Five recommendations**

1. **Close the protection gaps** for disability, life and critical illness: ≈HK$100K a year until retirement.
2. **Sign wills, a guardian nomination and powers of attorney** within three months, for under HK$25K.
3. **Both parents buy individual medical cover now**, before group cover ends at 65 and 62.
4. **At retirement, turn the MPF and the home into income**: annuities in 2037 and 2039; reverse mortgage or downsizing.
5. **Adopt one written family policy**: a portfolio per person, rebalancing bands, spending guardrails.

---

## Page 3 · §2 Cash flow and net worth · goals

**Layout:** OPENER · ANNOT (Figure 3 cash-flow chart + Figure 4 health check) · PROSE · DEFEND · TABLE (Figure 5 goals).
**Budget:** ≈330 words + two tables. **Owner:** Pete. **Status:** draft.
**Case asks for:** financial health, liquidity, leverage, debt servicing, emergency reserve, wealth concentration.

- Label: 02 CASH FLOW AND NET WORTH
- Finding-heading: **The Wongs start from strength; the risks are concentration and costs outside the budget.**

**ANNOT**

- Left: **Figure 3 · Where each year's income goes** `figures/cashflow-half.png` (waterfall, parents only, low bonus):
  income 1,920,000 → salaries tax −181,770 → MPF −36,000 → household spending −984,000 → surplus **718,230**.
  Source: case; team tax model (2026/27, separate assessment).
- Right: **Figure 4 · Health check**

  | Measure | Wongs | Verdict |
  |---|---|---|
  | Savings, after tax | 41% | Strong |
  | Reserve, months | 30.5 | Excess |
  | Debt to assets | 10% | Low |
  | Mortgage to pay | 8.5% | Easy |
  | Home and business | 61% | High |

  Line under it: *Benchmarks: reserve 6–12 months; debt under 50% of assets; mortgage under 30% of pay.*

**PROSE**

**Strong, liquid and lightly borrowed.** The parents save HK$718K a year after tax and MPF and hold HK$2.5M in cash:
30 months of spending, against the 6–12 months a household needs. Debt is 10% of assets, and the mortgage costs about
8.5% of gross income. **Two risks sit behind the strength.** First, concentration: the home and Carmen's business are
61% of the family's assets, and neither pays an income until it is sold or borrowed against. Second, the HK$82K a
month excludes profits tax, travel, renovation and medical emergencies, and new cover (§8) takes ≈HK$100K a year.

**DEFEND — Put idle money to work before taking more risk.** The easiest gains need no extra risk. Moving HK$500K from
savings accounts at 0.2% into deposits and a money-market fund at about 3% adds ≈HK$14K a year; clearing the HK$85K card
balance saves ≈HK$25K of interest if it revolves `[CHECK]`; tax-deductible voluntary MPF and deferred-annuity
contributions of HK$60K each save ≈HK$20K of tax. If the family has elected joint assessment, separate assessment
saves a further HK$18K `[CHECK: filing status]`. The reserve falls to twelve months (≈HK$1.0M) in a joint account both parents can reach.

**TABLE · Figure 5 · The family's goals, ranked**

| Priority | Goal | Measure of success | When |
|---|---|---|---|
| Need | Retire at 65 and 62 on HK$780K | Lasts to Carmen's 89: {{ladder_5_89}} | 2037, 2039 |
| Need | Protect income and health | Gaps in §8 closed; wills signed | 3 months |
| Need | Fund Chloe's degree without debt | HK$2.57M fund ring-fenced | 2028–32 |
| Want | 20–25% of investable assets in ESG | 25%, in SFC-listed funds | 2027 |
| Want | Ryan financially independent | Crypto ≤ 20% of his wealth by 35 | By 2037 |
| Wish | Legacy with purpose | Staged trusts; a scholarship | Ongoing |

---

## Pages 4–5 · §3 Retirement

**Status:** final. Source of truth: `document/section-mock-v3.html` (pages 1–2). Owner: Pete; numbers Fahtai.
**Case asks for:** on track at 65/62? accumulation, drawdown and liquidity strategies.

Figures on these pages: **6** decision ladder (`decision-ladder-half.png`) · **7** when each decision is taken (table) ·
**8** medical premiums (`medical-premiums-half.png`) · **9** portfolio fan chart (`fan-chart-half.png`, labelled
"annuity bought, mortgage cleared" at 2037) · **10** income floor (table) · **11** tier review and guardrails (table: fixed
spending {{fixflex_89}} → tier review {{fixswitch_89}} → guardrails {{guardswitch_89}}; typical spending {{fixswitch_typical}} → {{guardswitch_typical}}; worst-5% lowest
year {{fixswitch_worst5}} → {{guardswitch_worst5}}).

Paragraphs, in order: *Why these four, and not more investment risk* (by 2037 the portfolio is {{portfolio_2037_today}} in today's money,
about what a 2% real return needs for HK$780K a year, {{need_2037}}; the medical premiums break the plan; the annuity is longevity
insurance, neutral at the case's life expectancies but {{annuity_longlife_pts}} points if Adrian lives to 95, so only the MPF is
annuitised) · *Saving to 2037* (the {{surplus}} surplus less new cover is invested each year, new money to whichever sleeve is below
target; HK$60K each through tax-deductible voluntary MPF, the tax saved not counted) · *Medical premiums* (buy now; review
the tier at 75 `[CHECK: that the insurer allows a move to its Standard plan without new underwriting]`; the public
floor) · *An income floor* (HK$268K a year from 2039: {{annuity_adrian}} for Adrian until his death, {{annuity_carmen}} for Carmen for life; single-life,
fixed) · *Drawdown* · *What the guardrails cost, and what they buy* ({{guard_cost}} a year for the typical family; pre-agreed steps).

The model clears the ≈HK$0.46M of mortgage still owed in 2037 from the portfolio (§9); every §3 number includes it.

---

## Page 6 · §4 Education

**Layout:** OPENER · ANNOT (Figure 12 costs by destination + Figure 13 funding timeline) · PROSE · DEFEND.
**Budget:** ≈330 words. **Owner:** Pete. **Status:** draft.
**Case asks for:** local and overseas scenarios, timing, funding vehicles, contingency.

- Label: 04 EDUCATION PLANNING
- Finding-heading: **Chloe's choice should not depend on the exchange rate. The fund is already there; it stays in HK
  dollars until she accepts an offer.**

**ANNOT**

- Left: **Figure 12 · Every destination fits the budget, even after a currency shock** `figures/education-costs-half.png`. Source: Statistics Canada, IRCC, Save the Student, published university fee schedules; team FX analysis.
- Right: **Figure 13 · Funding timeline**

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

**Contingencies.** Each extra point of fee inflation adds about HK$100K over the degree, and a one-year master's abroad
about HK$0.4M in 2032; both are paid from the surplus, which by then no longer carries Chloe. If a parent dies or is
disabled before 2032, the fund is already set aside, the wills earmark it for her education, and the new cover (§8)
protects the rest of the plan. **Why not an education savings policy:** its surrender charges in the early years would
lock up money needed from 2028, for a guaranteed return below what deposits pay today.

---

## Page 7 · §5 Investment and allocation

**Layout:** OPENER · ANNOT (Figure 14 current vs target allocation + Figure 15 buckets) · PROSE · TABLE (Figure 16).
**Budget:** ≈300 words + tables. **Owner:** Win. **Status:** draft; sizes and equity per decision 3.
**Case asks for:** cash and deposits, bonds, equities and funds, ESG, digital; target allocation, rationale,
product suitability, risk management, monitoring and rebalancing.

- Label: 05 INVESTMENT PLANNING
- Finding-heading: **One family policy, three portfolios: each sized to its owner's risk and to when the money is needed.**

**ANNOT**

- Left: **Figure 14 · From today's holdings to the target** `figures/allocation-half.png` (cash · bonds · equity,
  today HK$2.5M · 1.4M · 3.9M → target 2.5M · 3.1M · 2.1M). Line under it: *Parents' freely allocable money. Equity
  falls because HK$3.57M is set aside for the reserve and Chloe's fees. Source: case; team allocation.*
- Right: **Figure 15 · Five buckets** `[OWNER: Win]` confirm sizes

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
holding is a low-cost index fund or ETF, SFC-authorised or HKEX-listed. Both parents' global equity core is the
BOC-Prudential MSCI World ESG Index Fund, which picks the better-rated companies within each sector and so stays close
to the world market. The family's home, business and incomes already depend on
Hong Kong, so the equity core is global; a small Hong Kong sleeve, held in an HSI ESG index ETF (3039), is kept for
its tax-free dividends and low cost. The bond ETFs are Irish-domiciled, which avoids US estate tax. Inside the MPF,
each parent holds half in the scheme's ESG or global equity index fund and half in its bond fund until the annuity is
bought, so the balance does not fall sharply just before it is converted.

**DEFEND — Why not all Treasuries for Adrian.** Treasuries at about 5% look sufficient, but after 3.5% inflation they
leave 1.5% real, below what the plan needs, and bonds bought today mature by 2041 while the money must last to 2066.
In our simulation an all-Treasury ladder fails almost every time once medical costs are included. So the ladder
provides the floor and the equity provides the growth.

**TABLE · Figure 16 · Rules agreed in advance** (Win's M1–M9; test result from `run_model.py` §9)

| If | Then |
|---|---|
| Global equities fall 20% or more | Rebalance to target by selling bonds; never sell equities |
| Any holding drifts 5 points from target | Rebalance, using new money first |
| 5-year Treasury ≥ 4.5% | Lock yields in the ladder (triggered Sep 2026) |
| HK inflation > 3.5% for two quarters | Shorten bond maturities |

Line under the table: *In our test, 5-point bands did as well as rebalancing every year ({{rebal_bands_89}}); never rebalancing
gave {{rebal_drift_89}}.*

---

## Page 8 · §5 continued · §6 ESG

**Layout:** PROSE (§5 close) · OPENER (§6) · TABLE (Figure 17) · PROSE · DEFEND.
**Budget:** ≈420 words + table. **Owner:** Win. **Status:** draft; base per decision 1.
**Case asks for (§6):** strategic role, selection criteria, benefits and limitations, greenwashing mitigation.

**§5 close — PROSE**

**Value added without extra risk.** Moving about HK$4.4M of fund holdings from typical fees near 1.5% a year to index
funds near 0.15% saves ≈HK$59K a year `[CHECK: current-fee assumption]`; with the idle-cash and tax measures in §2 the
family gains ≈HK$120K a year before any change in risk. The portfolios are reviewed each quarter and at an annual family
meeting.

**§6 OPENER**

- Label: 06 ESG INTEGRATION
- Finding-heading: **The family's 20–25% ESG goal, met with evidence: from 11% today to 25%, with no return premium
  assumed.**

**TABLE · Figure 17 · How the plan reaches 25% of investable assets** (base HK$10.47M, decision 1; Win to confirm)

| Source | HK$M |
|---|---|
| Today: ESG equity funds 0.70 + green bonds 0.45 | 1.15 (11%) |
| Adrian: BOC-Prudential MSCI World ESG Index Fund 30%, HSI ESG ETF (3039) 5%, green bonds 5% | 0.83 |
| Carmen: the same ESG index fund 35%, HSI ESG ETF (3039) 2%, green bonds 10% | 0.97 |
| MPF: 50% of each parent's balance in its ESG constituent fund `[CHECK: each parent's scheme offers one]` | 0.84 |
| **Total at target** (the "today" row is for comparison, not added) | **2.63 (25%)** `[CHECK: Win]` |

Line under the table: *Counted as ESG: funds on the SFC's list of ESG funds, and green bonds with verified use of
proceeds. Adrian's global core is the BOC-Prudential MSCI World ESG Index Fund, one of only two global equity index
funds on that list; a plain index fund would leave the family at 19%, below its goal.* `[CHECK: fee and retail
access; fallback in Win's notes]`

**PROSE**

**Strategic role.** ESG is not a separate bet. It replaces the global equity core and part of the bonds with
like-for-like funds, so each parent's risk and expected return stay where §5 sets them. **Selection criteria:** on the
SFC's list of ESG funds; index-tracking, so the method is published; low ongoing charges; daily dealing in Hong Kong
dollars; and the two-rating test below.

**Three layers, one standard.** Exclusions remove thermal coal, controversial weapons and tobacco; best-in-class funds
hold the highest-rated companies in each sector; green bonds with checked use of proceeds add direct impact. Every fund must be on the SFC's list of ESG funds.
**Why not higher:** the plan reaches the top of the family's range through choices that suit each person; going
further would mean ESG in Adrian's Treasury ladder, which has no ESG equivalent, or more equity for Carmen, which the
family objective rules out.

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

**Layout:** OPENER · TABLE (Figure 18 suitability by person) · PROSE · ANNOT-style box for Ryan (Figure 19 glide path).
**Budget:** ≈380 words + tables. **Owner:** Win (§7), Pete (Ryan). **Status:** draft.
**Case asks for:** suitability, volatility and downside, regulation and platform risk, custody and security,
allocation limits, implementation options. **Family goal 3:** Ryan's savings, investment, protection, retirement.

- Label: 07 DIGITAL ASSETS
- Finding-heading: **Not yes or no: form, size and custody, set for each person.**

**TABLE · Figure 18 · Digital assets by family member**

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

**Downside in numbers.** A 70% fall today would cost Ryan about HK$350K, more than a year's pay; at his 20% cap at 35
it would cost 14% of his wealth. Carmen's 2% cap limits the same fall to about HK$29K. **Implementation, in order of
preference:** HKEX-listed spot ETFs (bitcoin 3439, ether 3009), which need only a securities account; SFC-licensed
platforms for direct holdings, in their regulated custody; self-custody only with the recovery plan. Lending, leverage
and unlicensed exchanges are excluded.

**Ryan's own plan.** Ryan earns HK$300K and saves 30% (HK$90K a year) after keeping three months' spending in cash.
New savings go to a global equity portfolio, and none to crypto while he is above his glide path, so his crypto share
falls without any forced selling (Figure 19). He adds term life and critical-illness cover for about HK$900 a year,
starts voluntary MPF contributions, and his parents match 50% of his savings up to HK$24K a year.

**Figure 19 · Ryan's crypto share of his wealth, by savings rate**

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

**Layout:** OPENER · sidebar numbers (2) + intro · TABLE (Figure 20) · PROSE (A–E) · family emergency plan · DEFEND.
**Budget:** ≈420 words + table. **Owner:** Lookbua. **Status:** draft; critical illness per decision 2.
**Source:** `drafts/08-protection.md`, re-sized. **Case asks for:** mortality, medical, critical illness, disability,
business continuity, family emergency plan.

- Label: 08 RISK MANAGEMENT AND PROTECTION
- Finding-heading: **The largest gap is income, not death: neither parent could replace their salary if disabled.**
- Sidebar: **HK$100K** in year 1 closes every gap: 14% of the surplus, paid only until retirement

**Intro.** Of fifteen ways the plan could fail, ranked by severity, likelihood and warning time (Appendix A2),
disability ranks first for both parents: the gap the family itself reported. The existing whole-life policies already
meet most of the life need. Premiums average {{premiums_avg}} a year to retirement as they rise with age; wills and powers of
attorney cost under HK$25K once (§9).

**TABLE · Figure 20 · Disability and critical illness are the gaps; life cover needs only a top-up**

| New cover | Adrian (54) | Carmen (49) | Year 1 |
|---|---|---|---|
| **Disability income** | HK$65K a month to 65 | HK$39K a month to 62 | HK$37K |
| **Term life** | +1.75M (need 3.75M) | +1.05M (need 2.85M) | HK$7K |
| **Critical illness** | 1.5M | 1.5M | HK$41K |
| **Medical (VHIS)** | Flexi, deductible = group | Flexi, deductible = group | HK$15K |
| **Key person, buy-sell** | — | 2.5M, company pays | — |
| **Total** | | | **≈HK$100K** |

Source line: *None of this cover exists today. Sized by need: critical illness = treatment outside VHIS + 3 months'
pay. Source: Bowtie rate cards (2026); market range for disability cover; quotes replace them before purchase.*

**A) Disability first.** A benefit of 65% of pay to each parent's retirement age replaces the income the plan depends
on. Carmen's cover is written on her salary, so it must be in place before any change to how she draws income from the
business.

**B) Life cover fills a defined gap.** If Adrian dies, Carmen's income leaves a shortfall of about HK$157K a year until
she is 62; with the mortgage and final costs that is HK$1.75M. If Carmen dies, Adrian's income covers the household;
her gap is the mortgage, the business-loan guarantee and final costs.

**C) Medical cover now, not at retirement.** Group cover ends at 65 and 62. VHIS bought while both are healthy is
renewable to 100 with no new underwriting; a deductible matched to the group benefit keeps the overlap cheap, and
premiums are tax-deductible up to HK$8,000 each. **D) The business survives Carmen:** a buy-sell agreement funded by
company-owned key-person cover realises her full HK$2.5M stake. **E) Ryan starts small:** HK$0.5M life and HK$0.3M
critical-illness cover for ≈HK$900 a year.

**Family emergency plan.** A joint account pays every bill for twelve months (≈HK$1.0M) while an estate is settled; a
one-page family file lists every policy, account and recovery route; Chloe has two named emergency contacts and a
guardian (§9).

**DEFEND — Term cover, not more whole-life.** The need ends at retirement, when the mortgage is cleared, Chloe has
graduated and the annuities begin. Term cover prices that window; whole-life cover of the same amount costs many times
more, because most of its premium buys savings the family already holds. The trade-off: the new cover lapses at 65 and
62, after which the existing policies and the portfolio carry the risk. If a claim is disputed, the emergency reserve
carries the family while it is settled.

---

## Page 11 · §9 Property · succession

**Source:** `drafts/09-property.md` (Lookbua) + working brief §3.6 (Pete).
**Layout:** OPENER · ANNOT (Figure 21 property options chart + Figure 22 options table) · PROSE · DEFEND · PROSE (succession) · TABLE (Figure 23).
**Budget:** ≈400 words + figures; fits with ≈4mm to spare (test render 30 Sep). **Status:** draft.
**Case asks for:** retain, refinance, partially monetise or downsize; wills, trusts, succession, powers of attorney,
philanthropy. **Family concern 8:** relocating to another district.

- Label: 09 PROPERTY, SUCCESSION AND LEGACY
- Finding-heading: **Keep the home now, decide at 65, and sign the papers this quarter so the choice stays open.**

**ANNOT**

- Left: **Figure 21 · Security and legacy by property option** `figures/property-options-half.png`.
- Right: **Figure 22 · The options at 2037**

  | Option | Money lasts to 89 | Left to heirs |
  |---|---|---|
  | Keep, no release | {{prop_keep_89}} | {{legacy_keep}} |
  | Reverse mortgage | {{prop_rmp_89}} | {{legacy_rmp}} |
  | Downsize to HK$7M | {{prop_down_89}} | {{legacy_down}} |

  Note: today's money; with annuity, lower survivor spending and the business sale.

**PROSE — property**

**Refinance? Not now; clear it at 65.** The mortgage costs about 3.5%, close to what cash earns, and its interest is
tax-deductible. We compare it each year with new H-plans, capped at 3.25%, and switch only if the saving clears the
fees. About HK$0.46M will still be owed in 2037; it is repaid from the portfolio then, because the reverse mortgage
needs a home free of other loans, and the model counts that cost. **Ownership:** we assume the parents hold the flat as
joint tenants, so it passes to the survivor outside the will; a land search in month 1 confirms it `[CHECK]`.
**Another district:** the HK$7M replacement need not be in Tai Kok Tsui; a cheaper district buys more space, or
releases more money.

**DEFEND — Downsizing is the stronger financial answer; the reverse mortgage buys the right to stay.** Downsizing
matches the reverse mortgage on security and leaves about {{legacy_down_vs_rmp}} more to Ryan and Chloe. HKMC's reverse mortgage
pays a fixed income for life, lets both parents stay in the home and is non-recourse, at the cost of a smaller legacy.
The choice depends on how much staying in Tai Kok Tsui matters to them, so we set the decision for 2037 and keep both
options open; delaying the reverse mortgage to 2045 would lower the plan from {{ladder_5_89}} to {{rmp2045_89}}.

**PROSE — succession**

**Control, not tax.** Estate duty was abolished in 2006, so succession planning here is about control, liquidity and
staging. Without wills, the intestacy rules would pass about HK$1.1M each to Ryan and Chloe on Adrian's death, and on
both deaths about HK$11.9M each, unstructured, with no guardian named for Chloe. MPF balances have no beneficiary
nomination: before 2037 they are paid to the estate once probate is granted `[CHECK: MPFA]`, so the wills cover them
and the joint account bridges the wait.

**TABLE · Figure 23 · The three documents the family needs** (moved here from page 12 to fit)

| Document | Covers | Key point |
|---|---|---|
| Mirror wills | The estate, including MPF | Staged trusts for the children at 25, 30 and 35; a guardian for Chloe |
| Enduring powers of attorney | Property and money | Needed before any reverse mortgage or sale |
| Advance directives | Medical treatment | New statutory form, in force since 31 July 2026 |

---

## Page 12 · §9 continued · §10 Roadmap

**Layout:** PROSE (business, governance, philanthropy) · OPENER (§10) · TABLE (Figure 24).
**Budget:** ≈90 words + table; ≈33mm to spare (test render 30 Sep). **Status:** draft.

**PROSE**

**The business, passed on in stages.** A shareholders' and buy-sell agreement funded by key-person cover now; managers
built up from 55; a staged sale between 58 and 62, with no capital gains tax. We count only HK$3.0M of its HK$5.0M value.
**Family governance:** a short family charter and one annual meeting where all four review the plan. **Legacy with
purpose:** a named scholarship in sustainable design, about HK$30K a year through a registered charity, joins Carmen's
mission to Chloe's interest in design; donations are tax-deductible.

- Label: 10 IMPLEMENTATION ROADMAP
- Finding-heading: **Every gap closes in the first year; after that, dates and events trigger each decision.**

**TABLE · Figure 24 · Roadmap** (three group rows)

| When | Action | Owner | Effect |
|---|---|---|---|
| ***Next 12 months*** | | | |
| Month 1 | Wills, guardian, powers of attorney; land search | Parents | < HK$25K once |
| Month 1 | Joint account; idle cash to deposits; clear the card | Parents | +≈HK$39K a year |
| Months 1–3 | Disability, life, CI and VHIS cover; Ryan's cover | Family | ≈HK$100K a year |
| Months 1–3 | Buy-sell agreement; key-person cover | Carmen | Company pays |
| Months 1–6 | Three portfolios; policy signed; voluntary MPF | Family | Fees ≈HK$59K lower |
| Month 12 | First family meeting; Ryan's plan; family charter | All four | — |
| ***3–5 years*** | | | |
| Early 2028 | Chloe accepts an offer: convert years 1–2 of fees | Parents | No currency risk |
| Every year | Rebalance by bands; review mortgage, cover, ESG list | Adviser | — |
| ***Into retirement and legacy*** | | | |
| 2034–36 | Adrian to 35% equity; business managers in place | Parents | — |
| 2037 | Clear the mortgage; Adrian's annuity; release the home | Parents | {{ladder_4_89}} → {{ladder_5_89}} |
| 2039 | Carmen's annuity; business sold; guardrails begin | Carmen | Sale: {{step_business}} points |
| 2047 | Adrian 75: review the medical tier | Parents | {{ladder_5_89}} → {{switch_89}} |

Source line: *Effect: chance the money lasts to Carmen's 89. Full reviews follow a death, a disability, a business
sale, a 20% market fall or a 1.5-point rate move.*

---

## Page 13 · §11 Risk and compliance

**Source:** `drafts/10-11-roadmap-risk.md` + Win's regulatory matrix; stress results from `run_model.py` (`rec_*`).
**Layout:** OPENER · ANNOT (Figure 25 stress chart `figures/stress-half.png` + Figure 26 likelihood-impact matrix) ·
TABLE (Figure 27 register, compliance in its source line). The sensitivity chart is not placed; its numbers are in the register.
**Case asks for:** financial planning, suitability, ethical, product, regulatory and behavioural risks.

- Label: 11 RISK AND COMPLIANCE
- Finding-heading: **The largest risks are inflation, markets and medical costs; agreed rules answer all three.**

**ANNOT**

- Left: **Figure 25 · The plan holds under stress** `figures/stress-half.png` (chance the money lasts to Carmen's 89;
  fixed spending vs the recommended plan with the tier review and guardrails).
- Right: **Figure 26 · Likelihood and impact** (3 × 3 matrix). High impact: P1 (low likelihood) · F1 F3 F6 (medium) ·
  F2 (high). Medium impact: E1 P2 (low) · F4 F5 B2 (medium). Low impact: R1 R2 E2 (medium) · B1 (high).
  Line under it: *With the rules, stress costs spending, not solvency: {{rec_lowret_typical}} a year in a low-return decade.*

**TABLE · Figure 27 · Every risk has a measured impact and a named defence**

| | Risk | Fixed | Plan | Defence |
|---|---|---|---|---|
| **F1** | Inflation 3.5%, not 2.5% | {{cpi_stress_89}} | {{rec_cpi_89}} | Guardrails; shorter bonds |
| **F2** | Medical costs 8.5% a year | {{med_stress_89}} | {{rec_med_89}} | Tier review at 75 |
| **F3** | A low-return decade | {{stressA_89}} | {{rec_lowret_89}} | Guardrails; Treasury ladder 2037–41 |
| **F4** | Business not sold | {{biz_not_sold_89}} | {{rec_biz_89}} | Buy-sell agreement now |
| **F5** | Money must last to 95 | {{ladder_5_95}} | {{guardswitch_95}} | Annuities pay for life |
| **F6** | Portfolio runs down | {{fixflex_89}} | {{guardswitch_89}} | Annual review; pre-agreed steps (§3) |
| **B2** | Selling in a crash; drift | {{rebal_drift_89}} | — | 5-point rebalancing bands |
| **P1** | Disability before retirement | Top-ranked | | Disability income cover (§8) |
| **P2** | Irreversible products | Legacy | | Annuitise only the MPF; downsizing open |
| **B1** | Four risk appetites | Conflict | | One portfolio per person |
| **R1** | Crypto rules or licence change | Ryan | | Regulated channels only |
| **R2** | Greenwashing | Values | | Two ratings; replace in 3 months |
| **E1** | Suitability, joint clients | Fit | | One risk profile per person |
| **E2** | Model risk | Confidence | | Compare decisions; not forecasts |

Source line: *Fixed = fixed spending; Plan = Standard plan from Adrian's 75 plus guardrails; F5 to Carmen's 95, others
to 89. Every product is SFC-authorised, HKEX-listed or HKMC-issued; we earn no commission.*

Other stress numbers for the text if space allows: typical spending under the plan {{rec_cpi_typical}} (inflation),
{{rec_stressB_typical}} and {{rec_stressB_89}} (inflation + medical together). Fits with ≈11mm to spare (test render 30 Sep).

---

## Page 14 · Personal statement

**Layout:** OPENER · WMC analysis · four career paragraphs. **Budget:** ≈520 words.
**Rules:** "discussion of personal career goal and opportunities under the cross-boundary wealth management connect
scheme". No names of universities; first names only.

- Label: PERSONAL STATEMENT
- Finding-heading: **Four planners, one question: how Hong Kong's advisers serve families across the Greater Bay Area.**

**The opportunity: Wealth Management Connect** (Pete, ≈230 words)

Since 2021 the Cross-boundary Wealth Management Connect has let residents of Hong Kong, Macao and nine mainland cities
of the Greater Bay Area invest across the boundary through their banks, and since 2024 through licensed securities
firms as well. The 2024 changes raised each investor's limit from RMB 1 million to RMB 3 million, within an aggregate
quota of RMB 150 billion in each direction, and widened the funds on offer; a further round is under discussion.
Two flows matter to advisers. Southbound, mainland investors buy Hong Kong funds and deposits, and need advisers who
can explain those products, and their risks, to clients used to a different system. Northbound, Hong Kong residents
such as the Wongs can hold mainland wealth products in renminbi through banks in the Greater Bay Area. We did not use it
for this family: their income, home and business are already in one region, and renminbi products would add to that
concentration. For a family that retires across the boundary, it may be the right tool. Either way the skill is the
one this proposal needed: knowing two markets' products, rules and tax well enough to say when not to use them.
`[CHECK: quotas, the 2024 changes and securities-firm admission against HKMA's current page]`

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

- Finding-heading: **Every number traces to one model and a stated assumption.**

**A1 · Key assumptions**

| Assumption | Base | Stress | Source |
|---|---|---|---|
| CPI | 2.5% | 3.5% | HK 2006–25; Fed |
| Medical costs | 10% → 6% by 2036, plus VHIS age curve | 8.5% flat | Getzen; WTW |
| Equities | 6.0%, 17% volatility | 4.0% | Equity premium |
| Bonds, ladder | 4.0% | 2.5% | US 5-year 5.0% |
| Cash | 3.0% → 2.5% by 2031 | 0.5% | HIBOR; Fed |
| Model mix | 40/60, whole pool (plan: 40%, 60%) | — | Conservative |
| MPF annuities | Single life: {{annuity_adrian}} Adrian 2037, {{annuity_carmen}} Carmen 2039 (premiums HK$2.31M, HK$1.81M) | — | HKMC rates |
| Mortgage | ≈HK$0.46M still owed, cleared in 2037 | — | Case |
| Reverse mortgage | HK$230K a year for life from 2037 | From 2045 | HKMC |
| New cover | ≈HK$100K year 1; {{premiums_avg}} average; critical illness HK$1.5M each | — | Rate cards |
| Medical tier | Standard plan from 2047, same insurer `[CHECK: no new underwriting]` | Flexi | Insurer terms |
| Guardrails | From 2039: ±10% if withdrawals move 20%; floor 70% (essentials 40% never cut; the rest never below half; no cuts in the last 15 years) | Fixed | Guyton–Klinger |
| Survivor | 70% of HK$780K after Adrian's 84 | 100% | Convention |
| Life expectancy | Adrian 84, Carmen 89 | Both 95 | Case |

(The printed table drops the premiums and the bracketed guardrail detail to fit; both are in §3 and §8.)

**A2 · Model and method.** One spreadsheet projects income, 2026/27 salaries tax (reproduced to the dollar:
HK$181,770), MPF, spending, education, medical premiums and the portfolio for 2026–2072; a Monte Carlo simulation runs
10,000 paths of annual returns. **Limits:** returns are normal and uncorrelated, which understates crashes; inflation is
fixed within each scenario; each mix is held constant. Results compare decisions; they are not forecasts.

**A3 · Sources · A4 · Use of AI tools.** Case study (SRFP&S, 2026) · Inland Revenue Ordinance, Budget 2026/27 · HKMC ·
Health Bureau VHIS data · WTW, MMB, Aon 2026 · SOA Getzen model · Federal Reserve SEP · HKAB · ECB · fee schedules ·
insurer rate cards · SFC list of ESG funds · Berg, Kölbel and Rigobon (2022) · Guyton and Klinger (2006) · cover
photograph: Peter Steinhauer, *Cocoons*. AI tools were used to check calculations, review the model code and edit
text; the analysis and recommendations are the team's own.

Fits with ≈18mm to spare (test render 30 Sep).

---

## Charts (all drawn by `model/make_charts.py`; rerun after any model change)

| Figure | File | Width |
|---|---|---|
| 3 · Cash flow | `cashflow-half.png` | half |
| 6 · Decision ladder | `decision-ladder-half.png` | half |
| 8 · Medical premiums | `medical-premiums-half.png` | half, paired |
| 9 · Portfolio fan chart | `fan-chart-half.png` | half, paired |
| 12 · Education cost by destination | `education-costs-half.png` | half |
| 14 · Today vs target allocation | `allocation-half.png` | half |
| 21 · Property options | `property-options-half.png` | half |
| 25 · Stress: fixed spending vs the recommended plan | `stress-half.png` | half |
| — · Sensitivity (not placed; numbers in Figure 27) | `sensitivity-half.png` | half |

Tables and diagrams built in the page: Figures 1, 2, 4, 5, 7, 10, 11, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 26, 27.
Every chart's numbers are in `figures/figure-data.md`.
