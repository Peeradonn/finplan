# Claims audit before continuing slides 1 and 3

**12 Nov 2026 · Codex intake review.** Lenses: practitioner, ESG strategist, family, judge at the back of the room.
Read the three Final PDFs, case, rules snapshot, both local slide skills, the plan, decision list, model-run tables,
relevant model/export code, industry brief and the two supplied industry PDFs. Inspected existing slide 1 and 3 PNGs;
these are existing renders, not newly built or validated slide revisions. Integrated team commits through `14ce0ec`.
External checks below were made on 12 Nov. This is an evidence review, not a new financial recommendation or model run.

## Verdict

PRISM is defensible as a worked decision process for the Wongs. The evidence does **not** establish that other
advisers consider only ESG labels, ignore household climate exposure, or fail to price values. Several statements in
`industry_practice.md` turn an omission in a document into an assertion about practice. Those statements should not
be used as evidence for the opening or the framework's “instead of” lines.

**Recommended positioning (editorial proposal):** “Choosing ESG funds is one decision. We also test what climate means
for this family's home, business and retirement, and what their decisions change in the world.” Show the resulting
choices and their costs. No industry-wide absence or first-ever claim is needed.

## What the evidence establishes

| Source | Established fact | Limit on the inference |
|---|---|---|
| J.P. Morgan Asset Management, supplied *ESG integration*, April 2023, pp. 1, 3–6 | For strategies it deems integrated, financially material ESG factors enter investment analysis, with research, documentation and monitoring. Integration alone does not require exclusions or an environmental objective. | This is a fund-manager process document, not a description of all private-bank financial planning. It contradicts a claim that ordinary investment analysis ignores ESG. |
| Same, pp. 3–5 | JPMAM does not separately measure integration's contribution to performance. | Attribution difficulty is not proof of zero benefit, no outcome monitoring, or a deficiency our scenario model solves. A modelled counterfactual is not measured real-world causal attribution. |
| Morgan Stanley, supplied *2025 Sustainability Report*, pp. 13–14 | Wealth Management provides profiling, portfolio alignment analytics, manager due diligence, stewardship-related approaches and donor-advised philanthropy. | “Only a label” understates the described service. A sustainability report cannot establish the limits of bespoke advice. |
| Same, pp. 28–29 | The firm's climate risk work includes physical and transition scenarios, collateral and insurance channels. The described scenarios assess the firm's risk. | It does not follow that clients never receive climate advice or that a household scenario service does not exist. |
| J.P. Morgan Private Bank, 16 May 2025, live primary article linked below | Explicitly connects home vulnerability, insurance choices and climate risk to long-term wealth goals, and offers team support for property decisions. | US context; it does not prove delivery of our exact joint household model in Hong Kong. It does defeat “advisers only look at funds.” |

Live primary checks:
- [Morgan Stanley 2025 report](https://www.morganstanley.com/content/dam/msdotcom/en/assets/pdfs/Morgan_Stanley_2025_Sustainability_Report.pdf)
  matches the supplied report's scope (pp. 13–14, 28–29 read locally).
- [JPMAM governance and oversight](https://am.jpmorgan.com/us/en/asset-management/institutional/investment-strategies/sustainable-investing/sustainability-oversight-and-monitoring/)
  describes approval, ongoing monitoring and stewardship. The page contains older dated material; use the supplied
  2023 PDF as a dated description, not proof that all details remain current.
- [J.P. Morgan Private Bank: climate risk and home insurance](https://privatebank.jpmorgan.com/nam/en/insights/markets-and-investing/ideas-and-insights/how-climate-risk-and-losses-are-creating-high-prices-for-home-insurance),
  published 16 May 2025, especially “What you can do”.

Confidence: **high** on these document contents; **unverified** on prevalence of the exact PRISM service among advisers.
The broader regulatory and survey claims in `industry_practice.md` were not all re-verified in this intake.

## Wording requiring revision

| Current wording or implication | Verdict | Safer direction |
|---|---|---|
| “Today, ESG in a family's plan usually comes down to” an ESG-fund allocation question (slide 1 notes) | Unsupported prevalence claim. Our own earlier proposal is one example. | Ask the allocation question directly without claiming it represents the profession; then show why it is insufficient for this family. |
| “Nobody asks what climate does to the client's money” (plan §4.1) | Contradicted by the supplied integration document and private-bank article. | “We ask what climate does to the Wongs' entire plan.” |
| Industry brief §5: slide 2's “instead of” lines are “now sourced” | Not established. Reporting impact does not prove confusion of footprint with impact; silence does not prove annual-only monitoring or no values budget. | Describe what PRISM does. Use a contrast only against a specifically defined baseline with evidence. |
| “The best firms make ESG part of the portfolio; PRISM makes climate part of the plan” | False either/or implication. | Acknowledge existing integration and planning work; show our particular application and decision rules. |
| ESG integration “should never” sacrifice returns means clients' values are assumed free | Category error: financial-materiality integration is not a client mandate with costly exclusions. | Price the actual mandate against suitable alternatives; do not infer other advisers' values-budget practice. |
| “A label tells you ... not what it does” | Too absolute: labels and disclosures can specify meaningful constraints. | “A label alone does not tell us whether the whole plan works.” Proposed wording, not an agreed new title. |
| “No effect shown” becomes zero effect or shares “change nothing” | Not supported. Ownership, engagement and financing channels must be considered. | “No additional impact quantified for this allocation”; distinguish that from its footprint and alignment. |

## Slide 1: what its chart proves

- It compares the **same baseline** with and without our assumed climate shock. That illustrates exposure; it does
  **not** show that following labels caused the loss, or that another plan would avoid it.
- The exported `fin_lab_*` keys exist: `model/run_model.py` calls `Final/final_model.py`'s exports. The remaining
  concern is the assumptions and comparator, not a blanket assertion that these particular keys are unexported.
- The normal/stress paths are year-by-year medians plus property and business accounting, not a single realised
  future. “Never catches up” must be limited to the displayed model horizon and scenario. Model results based on
  illustrative shocks are not forecasts or observed losses, even under the repo's MEASURED convention.
- The two ESG ticks are our graphic. The footnote contrasts index methodologies; do not imply identical formal
  certification or two identified purchasable funds without checking those products. Conventional oil holdings do
  not by themselves make a financial-materiality ESG strategy misleading.
- A declining portfolio carbon-intensity rule is not a guarantee that underlying companies reduce absolute emissions
  each year. Confirm the exact benchmark's metric and method before simplifying it for speech.
- The promised improvement remains bracketed pending the baseline re-run specified in the plan. Do not promote it.

## Slide 3: what must reconcile before its headline is final

- **Financial headline:** the plan already calls for a purchasable comparison fund with a verified fee. The current
  package gain cannot be final while it relies on the unverified fee of the zero-assets fund. Selecting a fund that
  can be bought is ordinary due diligence; failure there is not evidence that ESG labels generally fail.
- **Complete package:** the seven changes include emissions data, while the headline run excludes its ongoing cost
  (a separate M8 variant includes it). Decide and document exactly what the package contains, then price that package.
- **Capital:** `Decision_List.md` §2 includes business working capital and recurring data/rating expenditure beyond
  the equipment capex shown on slide 3. Distinguish total project capital, borrowing, company cash, working capital
  and recurring cost. Equipment capex alone is not the full implementation funding requirement.
- **Tonnes:** the combined estimate includes vans, LED, air-con and recycled PET; it is not all from electric vans.
  Recycled PET dominates and depends on illustrative volumes and substitution assumptions. Spot resin parity is not
  a delivered supplier quote for Carmen's specification. State the counterfactual and reprice on supplier evidence.
- **Claim boundary:** “all the carbon cut comes from the business” should refer to the reductions quantified in this
  proposal. It does not establish zero effects elsewhere. Keep estimated project reductions separate from portfolio
  carbon intensity and avoid claiming already achieved outcomes.

These are checks against the existing decision list and plan, not new estimates. No numbers were changed here.

## Strongest objection and next action

**Objection:** a practitioner can reasonably say this combines familiar suitability, ESG integration, scenario analysis
and implementation work, while much of the apparent gain is ordinary planning. This worries me substantially more
than whether the framework has a novel name. The answer is a fair comparator, explicit costs and demonstrable decisions,
not a claim that those practices do not exist elsewhere.

**What would change my view:** representative evidence of adviser practice could support a prevalence claim; a
documented equivalent client-level service could narrow our originality claim further. Neither is necessary to
demonstrate a useful framework. Reconciled, exported package runs against a suitable baseline would clear the money
headline, while activity data and supplier quotes would strengthen the carbon estimate.

**Next:** Pete revises slide 1's question and narration without the profession-wide claim; Win verifies the purchasable
baseline fund and fee; Pete reruns the fully specified package; Fahtai confirms working capital, supplier terms and
the emissions counterfactual. Then revise slide 3 and render both slides and their builds. Layouts and source HTML
were left intact during this intake.

**Slide 1 follow-through, 12 Nov:** after Pete authorised the argument revision, the source and notes were updated;
see `Final_Plan.md` §4.3 for the current four beats and the render check. The two-index comparison and provisional
gain promise were removed. The chart is explicitly one baseline with/without an illustrative shock, not evidence of
loss caused by labels. Model outputs were unchanged; the baseline re-run and slide 3 work remain open.
