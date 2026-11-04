# Final Round: plan

**Status:** draft v0, 4 Nov 2026 (Pete: the client is the Wongs; the four-way split is agreed; everyone starts now on
work that waits for nobody). The storyline in §4 is a draft for the team meeting on Fri 6 Nov.
**What it is:** a 10-minute live presentation in English, then 10 minutes of questions from the panel. Sat 21 Nov 2026,
FellowSPACE, 28/F Tower A, Southmark, Wong Chuk Hang. Arrive by 09:30 (registration, ballot for the order, machine test).
**Slides due:** before **17:00 Mon 16 Nov 2026** to **info@srfpns.org** (finalist guidelines, p.1). Our 14 Sep copy of the
rules page says 23:59 Wed 11 Nov to info@hkrfp.org (`Primary Info/2026-rules.md`). **Unconfirmed which holds: Pete asks
the organiser today** (WhatsApp 9078 1829 or info@srfpns.org). Until they answer, keep the 11 Nov date in sight.
**No slide can change after submission** (guidelines, rule 7): the deck must survive two timed run-throughs before we send it.
**Sources:** `Final/2026 UFP Final Round Topic.pdf` (the brief), `Final/2026 UFP Final Round Topic Key Areas.pdf` (what
the ten minutes must contain), `Final/2026 UFP Final 4teams + Guidelines for Finalists.pdf` (criteria, rules).
**Research briefs:** `Final/research/` (one per owner, written 4 Nov; read your own first).

---

## 1. What the judges score

**Criteria** (guidelines, p.1, word for word): "Knowledge of the topic 20 marks · Logical thinking 20 marks · Presentation
skills 20 marks · Innovations, independent thinking 40 marks". The Key Areas sheet repeats: "Innovation and independent
thinking carry 40 of the 100 marks in the Final Round."
**Ranking:** "0.15 x Round 1 score + 0.15 x Round 2 score + 0.7 x Final Round score". Earlier leads count for little.

**What the ten minutes must contain** (Key Areas §7, word for word):
- "Lead with a recommendation, the capital required and the expected financial and sustainability outcomes."
- "Include a quantified structure, a portfolio with weights and costs, a scenario, a dashboard, a trade-off and a refusal."
- "Show your assumptions and sources, and defend them under questioning."

**How evidence is judged** (Key Areas, "Evidence and Assessment"): "Cite authoritative sources and distinguish measured,
estimated and illustrative data." "Use Hong Kong dollars, state all assumptions, and avoid fabricated or unverifiable
statistics."
**What distinguishes a strong answer** (Key Areas): "A clear recommendation with a number attached to it." "An honest
treatment of trade-offs, data limits and what you would not do." "Evidence that the sustainable finance element changes
the client's financial outcome, not just the vocabulary."
**The task** (brief, p.2): "present a decision-ready sustainable finance framework ... Demonstrate the framework on one
representative Hong Kong client. Define the client's circumstances and every figure yourself, state your assumptions,
and show how the framework changes the advice you would otherwise give. Address the six areas below."

| Criterion | What it rewards here (our reading, not the organisers') | Where we answer it (§4) |
|---|---|---|
| Innovation, independent thinking (40) | Conclusions that differ from the easy answer, each with a number: what we refuse, where the brief's tools don't fit this client, what changed since October | 3, 6, 7, 10, 11 |
| Knowledge of the topic (20) | Precise terms (green vs sustainability-linked vs transition; greenium vs green premium); the rules that really touch the client, and the ones that don't | 4, 5, 6, 9 |
| Logical thinking (20) | One chain: values → mandate → decisions ranked by money → structure → scenario → dashboard; never six mini-talks | the order of §4 |
| Presentation skills (20) | Live delivery by four, on time, the Q&A | §11 |

**Our reading of the brief** (inference): "Beyond Green Labels" warns against the answer most teams will give, buying ESG
funds and calling the plan integrated. Our own Round One ESG section was that answer. The panel includes ESG strategists
(the HK Institute of ESG Strategists is a joint organiser): expect hard greenwashing questions. The six areas hold about
24 bullets, which can't all fit in ten minutes: the six required items above go on screen; every area gets at least a
line on the framework slide; the rest goes into backup slides for the questions (§7).

## 2. The client and the thesis

**The client is the Wong family** (the competition's own case, `Primary Info/Award2026Case20260919.pdf`; our Round One
plan, `document/manuscript.md`). Every area of the brief has a hook in the case: Carmen co-founded a "sustainable
packaging distribution business" (HK$5.0M, a HK$0.9M loan, our staged sale 2035–39); the Tai Kok Tsui flat (HK$11.5M,
released in 2037); three decision-makers who disagree (Adrian prudent, Carmen values, Ryan tech); ESG 11% → 25% of
HK$10.47M; the HK$30K-a-year design scholarship. What the case doesn't give (the warehouse, the vans, the customers,
emissions, the building's age) we define and tag ILLUSTRATIVE. We say in the first minute which figures are the case's
and which are ours.

**The thesis (to test, not yet a finding):** in October we gave the Wongs the label answer, 25% in SFC-listed ESG funds.
The sustainability decisions that move their money are in Carmen's business (what a buyer pays in 2035–39) and the flat
(what it is worth when they leave it), not in the 25%.

**First evidence: exploratory runs, 4 Nov** (the Round One model, `model/run_model.py`; script `Final/explore_runs.py`).
EXPLORATORY: not for slides until added to `export_numbers()` and logged. Each row changes one input; the rest is the
Round One full plan (82.6% to Carmen's 89; median pot at 89 HK$6.68M in today's money).

| Change | To 89 | Median pot at 89 (today) |
|---|---|---|
| Business sale proceeds HK$2.0M / **3.0M (plan)** / 4.0M | 77.8% / 82.6% / 86.4% | 5.52M / 6.68M / 7.90M |
| Equity return 10bp lower / 50bp lower (equity is 40% of the mix, so about 4bp / 20bp on the whole pot) | 81.6% / 77.8% | 6.39M / 5.26M |
| Downsize in 2037 (no reverse mortgage), flat worth 0% / 10% / 20% less than the model's path | 83.1% / 76.8% / 69.5% | 7.51M / 5.80M / 4.02M |
| A HK$300K / HK$600K endowment paid in 2027 | 80.5% / 78.3% | 6.09M / 5.50M |

What it suggests: each HK$1M of sale price is worth about 4 points; a 10% discount on the old flat at the exit, about 6
points (the release is the gap between two prices, so it moves faster than the flat); a cost of about 10bp a year on
the whole pot, about 2.5 points. **The open question is the link:** whether sustainability actually moves the sale price
or the flat's value. If the evidence is thin, we say "if", show the sensitivity, and don't claim a premium (as Round One
did for ESG returns).

**What the research found (4 Nov; the four briefs in `Final/research/`).** Each brief tags its numbers; the model runs
in them are EXPLORATORY. Headlines, with the claim to check before it goes on a slide:

- **Business** (`area2_business.md`, Fahtai). On an illustrative HK$35M-revenue distributor, Scope 3 is about 98% of
  2,760–3,250 t a year; vans (28 t) and warehouse power (20 t) are the rest. Four electric vans, LED and air-con: HK$1.91M,
  saving about HK$0.37M a year, cutting about 26 t, and they pay without green finance (the vans' tax waiver ends 31 Mar
  2028). A 25bp green discount on HK$1.5M is worth about HK$12K a year, about the cost of the cheapest green review, and
  the HKMA grant needs at least HK$100M (read in the HKMA guideline of 24 Apr 2026). PLA "compostable" packaging counts
  as plastic under HK law and nothing here composts it: Carmen's own label is a greenwashing risk. The value lever is
  customer data: each 1% of sales lost to a rival with better data costs her stake about HK$209K. CBAM doesn't apply.
  *Check:* the diesel price used (HK$37.93/L is a list price; fleets pay less; at HK$25/L the vans still pay); the
  sustainability-linked loan ratchet and review fees; any evidence that emissions data raises SME sale prices.
- **Portfolio** (`area3_portfolio.md`, Win). **Round One's ESG core appears never to have launched:** the BOC-Prudential
  MSCI World ESG Index Fund (BUM645) is on the SFC's ESG list (authorised 2 May 2024) with no offering document, and its
  fund size on HKEX's fund platform is US$0.00 every month from Sep 2024 to Sep 2026; its S&P 500 sibling holds US$67.27M
  (both checked again by us, 4 Nov). It was about 56% of our ESG total. The cost of ESG equity comes from index
  construction, not the fee: MSCI's best-in-class index 7.88% a year since 2007 vs 7.85% for the parent, but 0.20% UCITS
  ESG ETFs trailed IWDA by 0.4–2.9 points a year over five years (state-dependent). Greenium 0–8bp, against a green bond
  fund that trails its own benchmark by about 1 point a year. Candidate refusals with numbers: the SFC-listed clean-energy
  ETF (−31% in 2023), sustainability-linked bonds (about 80% fail CBI alignment), a personal green deposit at 0.001%.
  Candidate allocation: ESG 27.7% (24.8% variant) via a climate-benchmark ETF (EDMW) at IWDA's fee; fees about HK$5.1K a
  year. *Check:* measured carbon intensity (none yet), EDMW beyond justETF.
- **Framework** (`area1_6_framework.md`, Pete). By the CFA/GSIA/PRI definitions (Nov 2023) Round One's ESG is screening:
  alignment, not impact; only the business transition and a funded scholarship can pass an additionality test. Hong Kong
  doesn't require advisers to ask about sustainability preferences (HKMA FAQ, Nov 2023: "not a mandatory requirement");
  we borrow the EU structure voluntarily. Adrian vs Carmen: separate sleeves plus a cost test, not an average. Round
  One's ESG funds cost about HK$11.9K a year more than plain twins (3.8–6.2 points); the green bond fee gap (about 104bp)
  is about 50 times the greenium. A lifelong HK$30K-a-year scholarship costs about 6.9 points; a funded 20-year fund
  (about HK$0.48M in 2027–28) about 2.6. *Check:* every fee (Win's documents), GIIN wording, HK donor-advised funds.
- **Flat, warehouse, scenario** (`area4_property_scenario.md`, Lookbua). Refuse the green mortgage: banks give a one-off
  HK$0–4K rebate on HK$1.8M, and only for BEAM Plus Gold/Platinum buildings. The flat's retrofit saves about HK$1,900 a
  year. Tai Kok Tsui is on no official flood or storm-surge list; heat is here now (52–53 very hot days in 2024–25 vs a
  baseline of 14). An old-building discount hits downsizing about five times harder than the reverse mortgage (HKMC counts
  only half the value above HK$8M): at 10% less, downsizing loses about 6 points, the reverse mortgage about 1.4. Release
  by the building's 50th year (HKMC goes case by case above 50). One scenario, a late and sudden transition in 2030–31:
  82.6% → 66.7%, of which about 10 points come through the portfolio as market and inflation risk that the ESG label
  doesn't change, 2.7 through the business and 2.2 through the flat. A green lease for the warehouse is worth more as a
  secure lease to the 2035–39 sale than for its kWh. *Check:* the building's age (1996 is our assumption), HKMC payouts
  by age, CLP's 2026 tariffs.

**What this does to the thesis.** It holds for what sustainability can *change*: the business (data, vans, its own
label) and the flat (how and when to leave) move the money more than the ESG label does. It needs one refinement: in a
climate scenario most of the loss comes through ordinary market and inflation risk, which no green label hedges; the
plan's defences there are diversification, the guardrails and the reserve. Say both.

**Two Round One issues found (Round One is frozen and the judges hold it; the Final must not repeat either):**
1. The BOC-Prudential ESG fund above. The Final names a fund only after checking it has assets and an offering document.
   **Pete to decide** whether to say it on stage ("a fund on the SFC's ESG list that holds US$0": a label is not a
   product) or keep it for the questions. Either way, be ready if a judge asks.
2. "Delaying the reverse mortgage to 2045 lowers the plan to `{{rmp2045_89}}`" kept the HK$230K payout set for 2037
   (`model/run_model.py`, line 386). HKMC pays by the younger borrower's age (Carmen 60 in 2037, 68 in 2045), about 36%
   more per HK$1M at 68 (Lookbua's brief, from HKMC's 2026 payout examples): about 80.7%, not a 9-point loss. **Pete to
   confirm** against HKMC's payout table and log in `reviews/applied.md`.

**What would change our mind about the Wongs:** if by Sat 7 Nov Fahtai can't build one financing structure for Carmen's
business worth a slide (a real project, an instrument, a number), the transition-finance part will look thin beside a
team whose client runs a factory. Fallback: a new client whose factory exports steel or aluminium goods to the EU, at the
cost of building a client and a baseline from scratch.

## 3. Rules for every slide
- **Numbers:** every model number is a `{{key}}` from `figures/numbers.json` (CLAUDE.md "Numbers"). New Final numbers go
  through `export_numbers()`, then diff `numbers.json` (no Round One number may change) and log in `reviews/applied.md`.
- **Tags on screen:** each number carries MEASURED (our model), SOURCED (named source), ESTIMATED (our arithmetic on
  sourced inputs) or ILLUSTRATIVE (our assumption). The brief asks for "measured, estimated and illustrative"; showing
  the tags is itself an answer to it.
- **HK dollars only.** Sources on the slide, dated.
- **Look:** decided in the build (the slide-design skill). Default: keep the Round Two identity (Plus Jakarta Sans, the
  crimson family, the house) unless a projector test says otherwise. This is a projector in a room, not Zoom: check
  contrast. Don't depend on Morph (the venue notebook's PowerPoint version is unknown); embed the font.
- **Live talk:** about 1,200 spoken words for 9:20. A slide carries one point and its number; the reasoning is spoken.

## 4. Storyline v0 (titles only; for the Fri 6 meeting)

Bracketed titles wait for results: they are not to be written until the numbers exist.

| # | Speaker | Time | Draft title | Required item |
|---|---|---|---|---|
| 1 | Pete | 0:15 | Beyond the label: what sustainability is worth to the Wongs (team name said first) | — |
| 2 | Pete | 0:45 | [The recommendation: N decisions, capital HK$__, odds the money lasts __ → __, about __ t CO2e a year less] | Recommendation, capital, outcomes |
| 3 | Pete | 0:40 | In October we gave the Wongs the label answer, 25% in ESG funds; the money that climate and the transition touch is elsewhere, in a HK$5.0M business and an HK$11.5M flat | The gap |
| 4 | Pete | 0:50 | One test for every sustainability decision: what it changes in cash flow, assets, risk or estate, by how much, by when, on what evidence | The framework; five kinds of finance placed |
| 5 | Pete | 0:45 | [Three decision-makers, one mandate: Carmen's values get a budget of __, Adrian's floor is untouched] | Profile, mandate, price of values |
| 6 | Fahtai | 0:45 | [Carmen's business emits about __ t a year, most of it in what it buys; listed customers will ask for that number] | Baseline |
| 7 | Fahtai | 0:50 | [The structure: these projects, financed this way, save HK$__ a year; the sustainability-linked loan refused at HK$0.9M because __] | Quantified structure, a refusal |
| 8 | Fahtai | 0:40 | [A business that can show its numbers protects the 2035–39 sale: each HK$1M of price is about __ points] | Enterprise value, succession |
| 9 | Win | 0:50 | [The portfolio stays __% sustainable, measured not labelled: weights, HK$__ a year in costs, carbon intensity __% below the plain index] | Portfolio with weights and costs |
| 10 | Win | 0:30 | [What we won't buy: __, because __] | A refusal |
| 11 | Lookbua | 0:50 | [The flat: its value against the new flat decides the 2037 exit; the warehouse: a green lease shares the savings] | A trade-off |
| 12 | Lookbua | 0:45 | [In a disorderly transition the business, flat and portfolio lose __; the plan still lasts in __%] | A scenario; risk register |
| 13 | Pete | 0:40 | One page the family reviews each year: money, carbon, impact and milestones, with triggers that force a decision | A dashboard; governance; funded giving |
| 14 | Pete | 0:20 | [What changed since October, in one line] | — |

**What the research suggests for the titles (4 Nov, for Friday):** slide 3 could open on the Round One fund (on the
SFC's ESG list, US$0 in assets) if Pete decides to say it on stage; slide 7's refusal is the green label on a loan this
small (the discount is worth about the review's cost; the vans pay on their own); slide 10's candidates are the
clean-energy ETF, sustainability-linked bonds and the green bond fund's fee against a 0–8bp greenium; slide 11's
trade-off is downsizing (larger legacy) against the reverse mortgage (the hedge against an old-building discount); slide
12 must say that most of the scenario's loss comes through ordinary market risk, which no label hedges.

Total 9:25 (cut 5 seconds in the build). Handovers: Pete → Fahtai → Win → Lookbua → Pete (four). Speaking: Pete 4:15,
Fahtai 2:15, Win 2:05, Lookbua 1:35. **Open for Friday:** Pete's share is heavy; slide 5 (the mandate) could move to
Win, since the price of values is portfolio evidence. Test the titles by reading them aloud in order.

## 5. Who does what, starting now

Each person researches, builds, presents and answers questions on the same part (rule 9: each member presents his or
her own part). The only hand-offs between people are listed under "Gives"; everything else starts today.

**Everyone, by Fri 6 Nov:** read the brief and the Key Areas sheet (20 minutes), then your research brief. Write one page:
"in my area, what would change our October advice, and by roughly how much". Bring it to Friday's meeting. Each brief
ends with its open items and what is unverified (the research agents ran out of web searches): those are your first
checks.

**Team decisions for Friday** (the briefs had to assume these; every number downstream depends on them):
1. **Carmen's share of the business.** Fahtai's brief assumes 50% (the company worth HK$10.0M); Round One treated the
   case's HK$5.0M as her interest. If she owns 100%, the business's HK$ and tonnes halve; the conclusions stand.
2. **The warehouse.** Fahtai's brief: leased, 7,500 sq ft in a Kwai Chung industrial building, 60,000 kWh a year.
   Lookbua's brief used a 3,000 sq ft placeholder: align to Fahtai's.
3. **The flat's building:** completed 1996 (30 years old now, 50 in 2046), about 900 sq ft, not certified (Lookbua's
   assumption).
4. **The Round One fund:** say it on stage or keep it for the questions (§2).

| Who | Owns | Starts now (needs no one) | Gives (to whom, by when) |
|---|---|---|---|
| **Pete** | The recommendation, framework, profiles and mandate (brief area 1); dashboard and governance (area 6); the close. Storyline, model, deck build, submission | Confirm the deadline with the organiser today. Model: add Final runs to `export_numbers()` (business sale sensitivity, price of values, the flat's relative value and exit year, funded giving, and a one-year shock function for the scenario, with placeholder sizes). Set up the Final deck folder from the Round Two build. Read `research/area1_6_framework.md` | Model numbers to everyone (Tue 10) |
| **Fahtai** | Carmen's business (area 2): emissions, abatement curve, instruments and grant, bankability, the 2035–39 sale; the map of rules (area 5). Fact-check lead | Read `research/area2_business.md`. Define the business's illustrative facts (warehouse size and lease, vans, revenue, customers, suppliers). Baseline and abatement curve. Confirm the grant scheme's rules from the HKMA guideline itself | Business facts to Lookbua and Pete (**Fri 6**); go / no-go on a financing structure (**Sat 7**) |
| **Win** | The portfolio (area 3): allocation with weights and costs, the evidence on greenium, fees and tracking error, carbon measurement, fund checks, the portfolio refusal; anti-greenwashing controls | Read `research/area3_portfolio.md`. Pull each fund's latest fees and carbon figures from its own documents; draft the allocation table; compute the price of values in HK$ a year | Fee and tracking-error figures to Pete for the model (**Mon 9**) |
| **Lookbua** | The flat and the warehouse (area 4): green mortgage, retrofit, BEAM Plus, typhoon, flood and heat, insurance, downsizing, the split incentive; the scenario and risk register (area 5). Logistics and Q&A drills | Read `research/area4_property_scenario.md`. The flat: physical risk, what a green mortgage is worth on HK$1.8M, the building's age and the 2037 exit. Ask the organiser about the venue's PowerPoint version, presenter view and a clicker | Scenario shocks, with sources, to Pete (**Mon 9**) |

## 6. Schedule (assuming 16 Nov)

| When | What |
|---|---|
| Wed 4 – Thu 5 Nov | Deadline confirmed; everyone reads; one-page notes |
| Fri 6 | Meeting: thesis, storyline (titles only), speaker order; Fahtai's business facts handed over |
| Sat 7 | Fahtai's go / no-go on the business structure (the Wongs stay or we switch) |
| Sat 7 – Tue 10 | Research to numbers; Win's and Lookbua's inputs to the model (Mon 9); model numbers out (Tue 10); first slides |
| Wed 11 | Full draft deck; first timed run (the submission itself if 11 Nov is the deadline) |
| Thu 12 – Sat 14 | Revise; two timed runs; first Q&A drill; open the file on a PC without our font and with an older PowerPoint |
| Sun 15 | Freeze; build the PowerPoint; metadata check (`make_pptx.py --check`) |
| Mon 16, morning | Submit; wait for the organiser's acknowledgement |
| Tue 17 – Fri 20 | Rehearsal only: one full run a day with a timer, then ten minutes of hostile questions |
| Sat 21 | 09:30 at the venue; one member checks the machine and the file |

## 7. Backup slides for the questions (after the closing slide)
Put in the submitted file, since it is the only one we can use. Draft list: the emissions method and factors; the
abatement curve in full; the instrument comparison (tenor, covenants, verification cost, subsidy); fund-by-fund fees and
carbon figures; the risk register in full; the scenario's inputs and sources; the sustainability annex to the
investment policy; the model's assumptions; the rules map (what applies to the Wongs, what doesn't).

## 8. Hard questions (first list; owners add to it)

| Who asks | Question | Answered on | Weak? |
|---|---|---|---|
| ESG strategist | Is "sustainable packaging" itself a green label? Compostable packaging in a city without industrial composting? | 6–7 | Open (Fahtai) |
| Practitioner | Why not a sustainability-linked loan? Why not the Grant Scheme? | 7 | Grant scheme starts at HK$100M (secondary sources; confirm) |
| Practitioner | You reused the case: what's new? | 3, 14 | The before / after must be explicit |
| ESG strategist | How do you know your ESG fund is better than the plain index? Carbon intensity, coverage? | 9 | Open (Win) |
| Banker | Would a bank lend for this? Coverage, collateral? | 7 | Open (Fahtai) |
| Regulator | Are you licensed to advise on the loan or the funds? Suitability per person? | 5, 13 | Draft: we coordinate with the bank and licensed parties |
| The family | What does Adrian give up for Carmen's values? | 5 | Price of values in HK$ (Win, Pete) |
| Practitioner | Your scenario: why those shocks, from where? | 12 | Sources from NGFS / HKMA (Lookbua) |
| Anyone | What would you not do? | 7, 10 | Need two clear refusals with numbers |

## 9. Facts to check before they go on a slide

Each research brief has its own full list (its last section). The ones the storyline leans on:

| Fact | Problem |
|---|---|
| Grant Scheme (GSF): loans use Track II only, "at least HK$100 million", up to 75% subsidy if Taxonomy-aligned, caps HK$800K | Read by the business brief's agent in HKMA's guideline effective 24 Apr 2026; Fahtai to re-read the PDF before quoting |
| BOC-Prudential MSCI World ESG Index Fund: US$0.00 every month Sep 2024 – Sep 2026; no offering document | Checked twice (agent and us, 4 Nov, HKEX fund platform and SFC data file). Ask BOCI-Prudential before saying "never launched": the record shows zero assets, not the reason |
| Van saving HK$86K a year each | Rests on a HK$37.93/L diesel list price; find a fleet price; at HK$25/L the saving is smaller and the vans still pay |
| Green-loan discount 25bp; sustainability-linked ratchet size; external review fees | ILLUSTRATIVE: no HK bank publishes an SME green discount; find a bank quote or a published range |
| HKMC reverse mortgage pays about 36% more per HK$1M at 68 than at 60 | From HKMC's 2026 examples (single borrower, ages 60 and 70); check the joint-borrower table |
| ESG ETFs trailed IWDA by 0.4–2.9 points a year over five years | Window-dependent; quote with the period and the long-run figure beside it |
| Scope 3 about 98% of the business's footprint | ILLUSTRATIVE business, published factors (UK DESNZ 2025): say "on our assumptions" |
| EU CBAM: definitive from 1 Jan 2026; importers under 50 t a year exempt; ~180 downstream products proposed from 2028, not adopted | Law-firm and press summaries; check the Official Journal and the Commission's CBAM pages |
| HKEX: Scope 3 mandatory for LargeCap issuers from financial years starting 1 Jan 2026; comply-or-explain for the rest | Law-firm summaries; check Appendix C2 Part D itself |
| Hong Kong Taxonomy Phase 2A in 2026 (transition and adaptation) | From the brief; confirm with HKMA |

## 10. Untested assumptions (test, don't build on)
1. Judges reward building on the case and our own October plan, rather than marking it down as recycled.
2. Calling our Round One ESG answer "the label answer" reads as independent thinking, not as admitting a weak plan.
3. A distributor's transition story is rich enough for "Financing the Transition" (Fahtai's go / no-go, Sat 7).
4. Sustainability moves the business's sale price or the flat's value enough to matter. The research found no
   published evidence that emissions data raises an SME's sale price, and one old study of BEAM Plus price premiums
   (+4.4%, one district, 2012–14). Present these as sensitivities ("if a buyer discounts it by HK$1M, the family loses
   about 4 points"), not as findings.
5. About 1,200 words fit 9:20 live, with four speakers each saying their name.
6. The venue notebook shows our font, and the file needs nothing newer than its PowerPoint.

## 11. On the day (guidelines, rules 4–14)
- Dress formally; name tags visible. Say "Team Axis" before the first speaker; each speaker says their simple name before
  their part (there is a best presenter award). Never say the university's name.
- Warnings at 3 minutes and 1 minute left. **Over 10:30 disqualifies the team.** Aim for 9:20.
- Teams that haven't presented wait outside, so we won't see the others before our turn.
- One member checks the machine and the slides at 09:30. No slide can change after 16 Nov.
