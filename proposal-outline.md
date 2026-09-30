# Proposal Outline — Round One

**For:** the whole team. This is the outline we write against from 30 Sep. Owner: Pete.
**Due:** Fri 2 Oct, 23:59. **Hard rules:** 15 single-sided pages *including* cover and appendices · 12-pt Times
New Roman, single-spaced · English · HK$ throughout · no university name anywhere, including file metadata.
**Numbers:** every figure in the text is a `{{placeholder}}` until 1 Oct, when it is filled from the model
(`model/wong_model.xlsx` Outputs tab or `run_model.py` printout). The register is in §6 below.

---

## 1. The storyline

**Title:** *Built to Last — A Financial Plan for the Wong Family*

**Thesis** (agreed 24 Sep, working brief §1; savings figure set to HK$718K on 29 Sep; opens the executive
summary word for word):
> *The Wongs have already done the hard part: a HK$24.4M balance sheet, over 40% of after-tax income saved each
> year (parents only, HK$718K of HK$1.74M), and only 10% leverage. Our plan makes it last, for four people with
> four different views of risk.*

**What "makes it last" means, now that the model includes medical costs.** Their investments alone cannot carry
a HK$780K retirement *and* medical premiums that rise with both age and medical inflation: on those alone, the
chance the money lasts to Carmen's 89 is {{ladder_1_89}}. Four decisions they control lift it to {{ladder_5_89}}:
an income floor from the MPF, lower spending after the first death, a staged sale of Carmen's business, and a
planned use of the home. Choosing the Standard medical plan in later life lifts it to 98%. This is the evidence
behind pillar 2; the theme is unchanged.

**One savings figure: HK$718K** (`{{surplus}}`): after tax, MPF contributions and the HK$82K a month; 41.3% of the
parents' after-tax income of HK$1.74M. It is the model's figure and the only one the proposal uses. The older
HK$754K (before MPF) is retired.

**The three pillars** (working brief §1), presented as the report's three theses, each with A/B/C sub-points
and bold lead-ins.

| Thesis | Claim | Evidence (figure) | Sections |
|---|---|---|---|
| **1. Protect what has been built** | A) disability and critical-illness gaps first · B) wills, EPAs and a guardian for Chloe · C) liquidity that survives a death | Protection gap table; intestacy flow | §8, §9 |
| **2. Turn assets into lifelong income** | A) medical costs are the binding constraint · B) the decision ladder: annuity floor, survivor spending, business sale, home · C) the medical-plan choice is worth {{std_vs_flexi_pp}} points | **Decision ladder (hero chart)**; medical cost curve; fan chart | §3, §9 |
| **3. Give every voice a place** | A) Adrian: a floor and a 40/60 portfolio · B) Carmen: 20–25% ESG with anti-greenwashing checks · C) Ryan: conviction with structure · D) Chloe: freedom of destination, funded in HKD until she chooses | Allocation chart; per-person digital policy; education scenarios | §4–§7 |

**Tone rules** (from the working brief): lead with strengths; risks in numbers, not alarm words; digital assets get
structure, not a lecture; every recommendation quantified and traced to an assumption.

---

## 2. Style: adapting the reference report to our rules

Reference: `Pete/rc-2025-winning-written-report-kozminski-university.pdf` (CFA Research Challenge winner).

**Borrow directly:**
- **Page 1 is an executive summary with a fact box**: a shaded panel showing net worth, surplus, "on track?",
  headline recommendation, and success rate before → after. The headline sits above it in bold.
- **CAPS section banners**, full width, one accent colour. Sub-headings in caps with a thin rule underneath.
- **Verdict tags on assessments**, e.g. "LIQUIDITY — STRONG", "PROTECTION — GAP", "MEDICAL COSTS — KEY RISK".
  One colour for strengths, one for gaps.
- **Numbered figures with sources**: "Figure 7: Decision ladder" / "Source: Team analysis, HKMC, VHIS dataset".
  The text refers to them as **(Figure 7)** and **(Appendix A2)**. Every claim points somewhere.
- **Bold the key number** in each paragraph, and only that one.
- **Risk register in their format**: a probability × impact matrix with codes (F1 financial, P1 protection,
  B1 behavioural, R1 regulatory, M1 market). Each risk gets three bold lead-ins: **Risk:** · **Impact:** (quantified
  from the model) · **Mitigation:**.
- **Scenario table** (bear / base / bull becomes our stress scenarios A/B/C) and **one two-way sensitivity heatmap**
  (e.g. equity return × medical trend → success rate).
- **Appendix: key assumptions, methodology, sources, and an AI-use disclosure line**, as the reference report does.

**Adapt, because of our rules:**
- Their body text is ~9-pt sans in a narrow two-column layout. **Ours must be 12-pt Times New Roman.** Use a single
  body column with figures set beside the text (text wrap) or full width. Budget ~450 words per full page of text.
- Their annexes run to ~10 pages. **Ours share the 15.** One appendix page, dense tables only.
- **Text inside charts and tables:** the rules state 12-pt without saying whether it covers figures. Decision for
  the team (§5): keep figure text ≥ 10 pt and say nothing, or keep everything at 12 pt to be safe.
- **No logos, no university name**, no team-member photos. The team name goes on the cover only.
- **Palette:** navy + teal + one warm accent for gaps; greys for context. It must not resemble any university's colours.

---

## 3. Page plan (15.0 pages)

Changes from the working-brief budget: adds a **goals block** (10 marks, previously had no page) and a **one-page
appendix** (assumptions must be "clearly stated and justified"). Paid for by trimming §5, §8, §9 and §10–11
by 0.25 page each.

| Pages | Section | Owner | Scoring criterion it feeds |
|---|---|---|---|
| 1.0 | Cover (title, client, date, team name, confidentiality line, contents) | Lookbua | Presentation 20 |
| 1.0 | Executive summary | Pete (last) | all |
| 1.5 | §2 Client position + **financial goals** | Pete | Client information 15 · Financial goals 10 |
| 1.75 | §3 Retirement | Pete + Fahtai | Proposal 25 |
| 1.0 | §4 Education | Pete | Proposal 25 |
| 1.5 | §5 Investment and allocation | Win | Proposal 25 |
| 1.75 | §6 ESG · §7 Digital assets | Win | Proposal 25 |
| 1.25 | §8 Protection | Lookbua | Risk analysis 15 |
| 1.25 | §9 Property, succession, legacy | Pete (succession) · Lookbua (property) | Proposal 25 |
| 1.25 | §10 Roadmap · §11 Risk and compliance | Lookbua | Risk analysis 15 |
| 0.75 | Personal statement | all, Pete integrates | Personal statement 15 |
| 1.0 | Appendix: assumptions, method, sources, AI disclosure | Fahtai | Proposal 25 (justification) |

---

## 4. Section by section

Each section has: **the claim** (its first sentence, drafted), **must cover** (the case's own list, so nothing
is missed), **figures**, and **numbers**.

### Executive summary — 1.0 page · Pete · written last
- **Claim:** the agreed thesis from §1, word for word, then the "makes it last" paragraph.
- **Must cover** (case §1): financial position · major issues · planning priorities · strategic direction.
- **Figures:** Fig 1 fact box · Fig 2 decision ladder (small version).
- **Top five recommendations**, each with its number: ① protection gaps closed ({{protection_cost}} a year) ·
  ② wills + EPAs + guardian, within 3 months · ③ both parents buy individual VHIS now · ④ income floor from the MPF
  at retirement · ⑤ the 40/60 portfolio with rebalancing bands.

### §2 Client position and goals — 1.5 pages · Pete
- **Claim:** "The Wongs start from strength: {{savings_rate}} of after-tax income saved, {{reserve_months}} months
  of spending in cash, and 10% leverage. The risks sit in concentration and in what the HK$82K excludes."
- **Must cover** (case §2): financial health · liquidity · leverage · debt-servicing capacity · emergency reserve
  adequacy · wealth-concentration risk.
- **Verdict tags:** SAVINGS — STRONG · LIQUIDITY — EXCESS · LEVERAGE — LOW · CONCENTRATION — HIGH (61% in home + business).
- **Figures:** Fig 3 balance sheet composition · Fig 4 cash-flow waterfall (income → tax → MPF → spending →
  {{surplus}}) · Fig 5 goals table.
- **Goals table** (needs / wants / wishes, each SMART): retire at 65/62 on HK$780K · Chloe's degree without debt ·
  ESG 20–25% · protection gaps closed · Ryan independent · legacy structured.
- **Watch:** present the HK$18K separate-assessment point as a *mistake avoided*, not value created (pass-on §2).

### §3 Retirement — 1.75 pages · Pete + Fahtai
- **Claim:** "On their investments alone the Wongs have a {{ladder_1_89}} chance of their money lasting to Carmen's
  89. Medical premiums are the reason, and four decisions the family controls raise it to {{ladder_5_89}}."
- **Must cover** (case §3): on track at 65/62? · accumulation · drawdown · liquidity strategy.
- **Figures:** **Fig 6 decision ladder (hero chart)** · Fig 7 medical-premium curve by age with the levers marked ·
  Fig 8 fan chart (Monte Carlo percentiles).
- **Content:** the ladder; the medical line and its levers (methodology §1d); the annuity as a *longevity floor*,
  not a success-rate booster (+{{annuity_pp}} points); bucket strategy; guardrails (Guyton–Klinger); drop the old
  "97% funded" ratio.

### §4 Education — 1.0 page · Pete
- **Claim:** "Chloe's choice should not be made by the exchange rate. The fund stays in HKD until she accepts an
  offer, then converts one year at a time."
- **Must cover** (case §4): local and overseas scenarios · timing · funding vehicles · contingency.
- **Figures:** Fig 9 scenario A/B bars · destination cost table (methodology §3d, 2028/29 prices).
- **Numbers:** {{edu_total}} total overseas (the model's reading of the case band); FX buffer per destination.

### §5 Investment and allocation — 1.5 pages · Win
- **Claim:** "One disciplined portfolio in five buckets, sized to when the money is needed."
- **Must cover** (case §5): cash and deposits · bonds · equities and funds · ESG · digital; target allocation ·
  rationale · product suitability · risk management · monitoring and rebalancing.
- **Figures:** Fig 10 current vs target allocation · bucket table (working brief §5).
- **Numbers:** mix comparison from the model ({{mix1_89}} / {{mix2_89}} / {{mix3_89}}); idle cash moved: +HK$14K a year.

### §6 ESG — §7 Digital assets — 1.75 pages · Win
- **§6 claim:** "ESG rises from 11% to {{esg_target}} of the investable pool, chosen by evidence, not labels."
  Must cover: strategic role · selection criteria · benefits and limitations · greenwashing mitigation.
  **Decide the denominator first** (§5 below).
- **§7 claim:** "Digital assets keep their place, with a written policy per person." Must cover: suitability ·
  volatility and downside · regulation and platform risk · custody and security · allocation limits ·
  implementation options.
- **Figures:** Fig 11 ESG selection funnel · Fig 12 digital-asset policy table (Adrian 0% · Carmen ≤2% via ETFs ·
  Ryan's glide path).

### §8 Protection — 1.25 pages · Lookbua
- **Claim:** "The largest gap is income, not death: neither parent can replace their salary if disabled."
- **Must cover** (case §8): mortality · medical and hospitalisation · critical illness · disability and income ·
  business continuity and key person · family emergency plan.
- **Figures:** Fig 13 needs vs existing cover vs gap, per person.
- **Numbers:** {{protection_cost}} a year total, which feeds the model's premium input and lowers {{surplus}}.

### §9 Property, succession, legacy — 1.25 pages · Pete + Lookbua
- **Claim:** "Keep the home now; decide at 65 between a reverse mortgage and downsizing; put the paperwork in place
  this quarter so the choice stays open."
- **Must cover** (case §9): retain · refinance · partially monetise · downsize; wills · trusts · succession ·
  powers of attorney · philanthropy.
- **Figures:** Fig 14 intestacy vs will (who gets what) · reverse mortgage vs downsizing comparison.
- **Numbers:** reverse-mortgage start year worth {{rmp_timing_pp}} points; business sale {{biz_pp}} points.

### §10 Roadmap · §11 Risk and compliance — 1.25 pages · Lookbua
- **§10 claim:** "Twelve actions in twelve months, then three reviews that each have a trigger."
  Must cover: next 12 months · 3–5 years · long term.
- **§11 claim:** "The plan's largest risk is one the family controls: how they choose to pay for medical care."
  Must cover: financial planning · suitability · ethical · product · regulatory · behavioural risks.
- **Figures:** Fig 15 timeline · Fig 16 risk matrix · Fig 17 stress scenarios A/B/C (methodology §5).

### Personal statement — 0.75 page · everyone
- The rules define it as a "discussion of personal career goal and opportunities under the cross-boundary wealth
  management connect scheme".
- One paragraph from each member on their own career goal; Pete writes the Wealth Management Connect section.
  **Overdue:** paragraphs due 30 Sep.

### Appendix — 1.0 page · Fahtai
- A1 assumptions table (methodology summary) · A2 model and Monte Carlo method, with its limits · A3 sources ·
  A4 AI-use disclosure (one line, as in the reference report).

---

## 5. Decisions for today's call

| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | How medical premiums are treated | fully on top of HK$780K · net of ~HK$65K already inside it | Net of HK$65K, stated in one sentence |
| 2 | Survivor spending after Adrian's life expectancy | 100% · 70% | 70%, the usual planning convention |
| 3 | Backstops (business sale, reverse mortgage) | in the base case · shown as recommendations on the ladder | On the ladder: they are decisions, not assumptions |
| 4 | Equity return | 6% · 7% | 6%, settled; it matters less than any ladder step |
| 5 | ESG denominator | 10.47M · 8.2M · 7.7M | Decide in 5 minutes and use it everywhere |
| 6 | Value-of-advice figure (HK$5.16M) | keep · rebuild as the ladder | Rebuild; drop the card-compounding claim |
| 7 | Text size inside figures | ≥ 10 pt · 12 pt | Team call; 12 pt is the safe reading of the rules |

---

## 6. Placeholder register

> **Superseded (30 Sep):** model numbers are now filled automatically from `figures/numbers.json`
> (keys listed there); see `document/manuscript.md`.

Fill on 1 Oct from the model after the decisions above. "Now" is the model on 29 Sep: medical premiums on (Flexi,
net of HK$65K), Lookbua's protection premiums in (HK$159K a year average, to retirement), 6% equities. Every chart
number is also in `figures/figure-data.md`.

| Placeholder | Meaning | Source | Now |
|---|---|---|---|
| `{{surplus}}` | Today's annual surplus after tax and MPF | Tax tab: SURPLUS | 718,230 |
| `{{surplus_after_protection}}` | Surplus once the new cover is bought | Outputs: Annual surplus | 559,230 (year-1 premiums ≈135K; average 159K) |
| `{{reserve_months}}` | Liquid assets ÷ monthly spending | Outputs: Emergency reserve | 30.5 |
| `{{savings_rate}}` | Surplus ÷ after-tax income | 718,230 ÷ 1,738,230 (Outputs surplus; Tax tab) | 41.3% |
| `{{ladder_1_89}}` | Portfolio alone, premiums on top | run_model §5, row 1 | 32% (15% to 95) |
| `{{ladder_5_89}}` | All four decisions | run_model §5, row 5 | 85% (64% to 95) |
| `{{annuity_pp}}` | Points added by the annuity | run_model §5, row 2 − row 1 | 0 alone; −5 if removed from the full plan |
| `{{biz_pp}}` | Points added by the business sale | run_model §5, row 4 − row 3 | +19 |
| `{{rmp_timing_pp}}` | Reverse mortgage from 2037 vs 2045 | figure-data: tornado | 8 (85% vs 77%) |
| `{{std_vs_flexi_pp}}` | Standard plan from 75 vs Flexi | run_model §5, alternatives | +13 (98% vs 85%) |
| `{{mix1_89}}` etc. | Mix comparison, base case, annuitised | run_model §3 | 0% / 33% / 40%: mix 3 leads in the base case; recheck with the decisions on |
| `{{edu_total}}` | Overseas education, nominal | Outputs: Total education cost | 2,851,148 |
| `{{protection_cost}}` | New premiums, year 1 | `drafts/08-protection.md`, Figure 13 | ≈135,000 |
| `{{esg_target}}` | ESG share at target | Win, after decision 5 | pending |

## 6b. Figures ready

Generated by `model/make_charts.py` (rerun after any model change). Captions go in the document, not the image.

| Figure | File | Section |
|---|---|---|
| Fig 6 · Decision ladder | `figures/decision-ladder.png` | §3 (small version in the executive summary) |
| Fig 7 · Medical premiums, Flexi vs Standard | `figures/medical-premiums.png` | §3 |
| Fig 8 · Portfolio fan chart | `figures/fan-chart.png` | §3 |
| Fig 9 · Education cost by destination | `figures/education-costs.png` | §4 |
| Fig 14b · Property options | `figures/property-options.png` | §9 |
| Fig 17 · Stress scenarios | `figures/stress-scenarios.png` | §11 |
| Fig 18 · Sensitivity (one change at a time) | `figures/sensitivity-tornado.png` | §11 |
| Still to make | Fig 3 balance sheet · Fig 4 cash-flow waterfall · Fig 10 allocation (needs Win's HK$ sizes) · Fig 16 risk matrix | |

Drafts ready in `drafts/`: §8 protection, §9 property, §10–11 roadmap and risk, appendix. Each opens with notes
for its owner.

---

## 7. Timeline

| When | What |
|---|---|
| **29 Sep** | Call: storyline + decisions §5 · Fahtai reviews the model fix (`model/README.md`, "Changes 29 Sep") |
| **30 Sep** | Everyone drafts their section against this outline, with placeholders · Fahtai: charts, appendix |
| **1 Oct** | Fill placeholders from the model · four-eyes check · cut to 15 pages · strip file metadata |
| **2 Oct** | Buffer · submit early |
