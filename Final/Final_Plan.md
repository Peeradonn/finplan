# Final Round: plan

**Status:** draft, 5 Nov 2026. Decided: the client is the Wongs (Pete, 4 and 5 Nov). Open: the thesis, the framework and
storyline v2 (§4, agreed by messages, §4.6); the research split (§5). Everyone starts on work that waits for nobody.
**What it is:** a 10-minute live presentation in English, then 10 minutes of questions from the panel. Sat 21 Nov 2026,
FellowSPACE, 28/F Tower A, Southmark, Wong Chuk Hang. Arrive by 09:30 (registration, ballot for the order, machine test).
**Slides due:** before **17:00 Mon 16 Nov 2026** to **info@srfpns.org** (finalist guidelines, p.1; **confirmed by Pete, 5
Nov**). The older rules page's 11 Nov date no longer applies.
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
| Innovation, independent thinking (40) | Conclusions that differ from the easy answer, each with a number: what we refuse, where the brief's tools don't fit this client, what the framework changes against the label approach | 3, 6, 7, 10, 11 |
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

**The thesis (to test, not yet a finding):** the label approach puts 25% in SFC-listed ESG funds and stops there. The
sustainability decisions that move their money are in Carmen's business (what a buyer pays in 2035–39) and the flat
(what it is worth when they leave it), not in the 25%.

**The baseline is the label approach, not our Round One plan (Pete, 5 Nov: "we don't want to be confined by our past
submission ... not all judges might remember").** The brief's "the advice you would otherwise give" is the advice a
careful planner gives by default: funds picked from the SFC's ESG list to hit the 20–25% target, the green mortgage and
green loan the banks offer, a pledge to a charity, and nothing on the business or the flat. Our Round One did exactly
that, which is the proof it isn't a strawman: say so once, in one line ("we did this ourselves in Round One"), never as
the spine. Every comparison on screen is framework vs label approach, and stands alone for a judge who never saw
Rounds One or Two. In the model, the label approach is Round One as written (`Final/model_runs.md`).

**Free of Rounds One and Two, what we'd do differently (5 Nov):**
1. **The before:** the label approach (above), not "October".
2. **The hook:** "One of the few global equity index funds on the SFC's ESG list holds US$0." It needs no history; "we
   know because we recommended it" is optional, one line.
3. **The family's plan, in plain words:** retire at 65 and 62 on HK$780K a year, sell the business in stages, release
   the flat's value at retirement. None of Round One's machinery on screen (annuity ladders, "their own way").
4. **The 20–25% ESG target is the case's, not a fixed goal:** the framework treats the share as an output of each
   person's budgets, landing at 24.8% or 27.7% (`Decision_List.md` P6). We say why we're near the family's wish, not
   that we hit a number.
5. **The look:** not Round Two's by default. "Built to Last" and the house belonged to that plan; this talk's idea is
   the label against what it does, so a label or price-tag motif may say more (§3, "Look").
6. **Round One's choices are open:** where the framework disagrees with them (the fund, Adrian's green bonds, the
   unfunded pledge, "decide the flat in 2037"), the new advice wins without apology.

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
  as plastic under HK law (Cap. 603 s.3A), and the food-waste bins turn away packaging and utensils: Carmen's own
  label is a greenwashing risk. The value lever is
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
  HK$0–3K rebate on HK$1.8M, and only if the building (or, for HKMC, the flat) is BEAM Plus certified; SC and HSBC
  exclude refinancing (`hook_fact_checks.md`). The flat's retrofit saves about HK$1,900 a
  year. Tai Kok Tsui is on no official flood or storm-surge list; heat is here now (52–53 very hot days in 2024–25 vs a
  baseline of 14). An old-building discount hits downsizing about five times harder than the reverse mortgage (HKMC counts
  only half the value above HK$8M): at 10% less, downsizing loses about 6 points, the reverse mortgage about 1.4. Release
  by the building's 50th year (HKMC goes case by case above 50). One scenario, a late and sudden transition in 2030–31:
  82.6% → 66.7%, of which about 10 points come through the portfolio as market and inflation risk that the ESG label
  doesn't change, 2.7 through the business and 2.2 through the flat. A green lease for the warehouse is worth more as a
  secure lease to the 2035–39 sale than for its kWh. *Check:* the building's age (1996 is our assumption), HKMC payouts
  by age, CLP's 2026 tariffs.
- **Supply chain, PLA, the green premium** (`area2_supply_chain.md`, 5 Nov; area 2's owner). Bank supply-chain finance
  doesn't reach Carmen: her purchases (about US$3.4M a year, ILLUSTRATIVE) are about 1/30 of one bank's published guide
  for an anchor (US$100M of trade spend); the Hong Kong programmes found are anchored by CLP Power, Towngas and Sanfield,
  none by a food-and-beverage or packaging buyer; no programme publishes its ESG discount, and at an assumed 10–25bp it
  is worth HK$600–1,500 a year against HK$3.9–23K for an ESG rating. What works instead: one rating used several ways,
  early payment from her own cash in return for supplier data, and recycled-content options priced to customers per
  tonne. **The green premium has collapsed:** recycled PET traded at the same price as virgin in Southeast Asia in Oct
  2026 (search extracts of S&P and Argus), so the biggest cut (about 108 t a year) costs HK$0–1,395 a tonne, about 1.4 HK
  cents a cup even at the 2023 peak; the earlier 10% (HK$328K a year) was too high. PLA is regulated plastic (EPD
  guidance; its Sep 2025 packaging guide calls compostables "premature"); Phase 2 has no date; food-waste collectors
  reject loads over 20% packaging. *Check:* the ordinance text itself (not read), the resin prices, certification costs.

**What this does to the thesis.** It holds for what sustainability can *change*: the business (data, vans, its own
label) and the flat (how and when to leave) move the money more than the ESG label does. It needs one refinement: in a
climate scenario most of the loss comes through ordinary market and inflation risk, which no green label hedges; the
plan's defences there are diversification, the guardrails and the reserve. Say both.

**Two Round One issues found (Round One is frozen; the Final must not repeat either):**
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

**Reviewed 5 Nov: keep the Wongs** (area 2's owner confirms by Sat 7). The test was: no bank supply-chain finance at her
scale *and* no customer willing to pay a premium. The first failed (it doesn't reach her); the second mostly dissolved
(recycled PET at about the same price as virgin, so there is little premium to pay). Area 2's story is now: **Carmen's
transition is cheap, and the finance products the brief lists aren't built for her size; what she needs is data.** The
structure compares all five instruments and picks: a plain equipment loan for the vans (HKMC guarantee), recycled
content on supplier terms, supplier data bought with early payment from her own cash, a green lease at the 2027
renewal; it refuses the green-loan label and finds no bank supply-chain programme. That covers the brief's bullets with
numbers. The remaining worry (moderate): it can read as dodging "Financing the Transition". Insurance: one backup slide
running the same framework on a factory owner exporting to the EU, where CBAM and a sustainability-linked loan do apply
and the verdicts change.

**Why the Wongs, against a client built to fit the brief (5 Nov):** a "before" that isn't a strawman (the label
approach, which our own Round One followed); the core figures are the organiser's own case, so we can tag "case figure" vs "our
assumption", where an invented client is all assumption; the US$0 fund; four of the six areas fit strongly; Hong Kong
has about 12 import/export and wholesale SMEs for every manufacturing one (TID, June 2025). **Correction (5 Nov):** we
don't know who the Final judges are (the guidelines name none; the rules page's list is "under construction"), so don't
assume any judge read Round One or the case. A judge new to the case meets the Wongs as any client would be met; the
advantages above survive that, as long as the talk stands alone (§3).

## 3. Rules for every slide
- **Numbers:** every model number is a `{{key}}` from `figures/numbers.json` (CLAUDE.md "Numbers"). New Final numbers go
  through `export_numbers()`, then diff `numbers.json` (no Round One number may change) and log in `reviews/applied.md`.
- **Tags on screen:** each number carries MEASURED (our model), SOURCED (named source), ESTIMATED (our arithmetic on
  sourced inputs) or ILLUSTRATIVE (our assumption). The brief asks for "measured, estimated and illustrative"; showing
  the tags is itself an answer to it.
- **HK dollars only.** Sources on the slide, dated.
- **Look:** decided in the build (the slide-design skill), for this talk, not inherited (5 Nov). Round Two's house said
  "Built to Last"; this talk's idea is the label against what it does, so render a label or price-tag motif beside a
  plain option and choose. Keep Plus Jakarta Sans if it tests well on a projector. This is a projector in a room, not
  Zoom: check contrast. Don't depend on Morph (the venue notebook's PowerPoint version is unknown); embed the font.
- **Live talk:** about 1,200 spoken words for 9:20. A slide carries one point and its number; the reasoning is spoken.
- **Assume no judge has read anything** (5 Nov):
  1. Every slide stands alone. Never "as you'll remember" or "you hold our proposal".
  2. Introduce the family on screen in one picture: four people, what they own (flat HK$11.5M, business HK$5.0M, savings
     and investments HK$10.5M), what each wants, who disagrees (slide 3, with where the money is).
  3. Show the label approach as the concrete "before" beside each change (e.g. "Label approach: 25% in funds from the
     SFC's ESG list"), never "October" or "our Round One plan".
  4. Say where the client comes from in one line: "the family in this year's competition case". Round One appears at
     most once, as proof that the label approach is what careful planners do ("we did it ourselves").
  5. Cold read before submitting: two or three people who've never seen the case watch it without explanation; if they
     can't say who the family is and what changed within a minute, fix the introduction.
- **Every decision carries the same two-sided price tag** (Pete, 5 Nov): what it does to the family's money, in the
  brief's own four words ("cash flow, balance sheet, risk profile or estate ... by how much, over what horizon"), and
  what it does in the world (the brief's title: "Measuring Real Impact"; its dashboard: "sustainability outcomes,
  impact outcomes"):

  | Side | Line | What we report | Source |
  |---|---|---|---|
  | Money | Cash flow | HK$ a year, and from when | Research briefs (ESTIMATED) |
  | Money | Balance sheet | HK$ of net worth (e.g. Carmen's stake) | Research briefs (ESTIMATED) |
  | Money | Risk | Odds the money lasts to Carmen's 89, and the worst 10% of futures | Model (MEASURED) |
  | Money | Estate | HK$ left to Ryan and Chloe, today's money, **including the flat** | Model (MEASURED) |
  | World | Emissions | Tonnes CO2e a year, tagged measured (meters, fuel receipts), estimated or modelled | Research briefs |
  | World | Other real effects | E.g. students the scholarship funds | Framework brief |
  | World | Would it happen anyway? | Additionality: does this decision cause the change, or only own it? (Shares bought on the market fund nothing new: alignment, not impact) | Framework brief |

  The verdict comes from the four corners in §4.2. Where the odds and the estate move in opposite directions (downsizing
  leaves more to the children; the reverse mortgage protects the odds if old flats lose value), the family chooses, and
  the slide says so: that is the trade-off the brief requires.
- **Two model fixes before any price tag goes on a slide (Pete):**
  1. The estate line must include the flat (home equity after any reverse-mortgage loan, or the smaller flat), as
     `property_options()` already does. The exploratory tables in §2 show only the portfolio left at 89: don't quote
     them as the inheritance.
  2. The business's savings need a route into the family's numbers. The Round One model counts only the HK$3.0M sale and
     no dividends, so the vans' saving changes nothing today. Simplest honest route: extra profit × the sale multiple ×
     Carmen's share raises the sale proceeds (ESTIMATED; the multiple from Fahtai's brief, the share from the team's
     decision in §5).

## 4. Thesis, framework and storyline v2 (workshop draft, 5 Nov)

**Why v2:** the brief asks us to "present a decision-ready sustainable finance framework" and to "demonstrate" it on one
client. v1 was a client plan with a framework slide in it; v2 makes the framework the product and the Wongs the proof.
Every option below is a draft for the team workshop (§4.6): pick, rewrite or reject. Bracketed titles wait for the
model's numbers. Titles are short, because this is a live talk.

### 4.1 The thesis (one sentence everyone can say in one breath)

| Option | Thesis | For | Against |
|---|---|---|---|
| **A′. What it does** (recommended, 5 Nov) | "A green label tells you what something is called. We show what it does, to the family's money and to the world, so the family can choose with open eyes." | Keeps A's punch, hook and callback; adds the world side an ESG strategist looks for; leaves the choice with the family, which is where suitability puts it | One more idea to carry than A (money *and* world) |
| A. Price, not label (first draft) | "A green label tells you what something is called; a price tells you what it does. We price every sustainability decision in the family's own money, and decide on the price." | Answers the title "Beyond Green Labels" head-on; a phrase judges can repeat | Sounds as if money is all that counts: an ESG strategist could say "you turned sustainability into finance and lost the sustainability"; the people disappear behind HK$ |
| B. Follow the money | "A family's sustainability sits where its money sits. For the Wongs that is a business and a flat, not a fund, so that is where the plan acts." | The sharpest insight about the Wongs; concrete | It's a finding about one client, not a framework |
| C. A planning decision, not a product | "Sustainability is a planning decision, not a product: each choice must show what it does to the family's cash, wealth, security and legacy, or it stays out of the plan." | Closest to the brief's own words | Every team will echo the brief; least memorable |

B can live inside A′: it is what the framework's first step (Map) finds. "Price tag" stays as the name of the tool inside
the framework.

### 4.2 The framework

| Option | Shape | For | Against |
|---|---|---|---|
| **F1. Map → Price → Decide → Govern** (recommended) | Four plain verbs, done in order | Covers all six areas by construction (below), so a judge with the brief's checklist sees every box ticked; gives the talk its spine | Four steps to explain (about 45 seconds) |
| F2. The price tag alone | One tool: the two-sided tag and the four corners | Simplest | Leaves out mapping and governance, so reads as a tool, not a framework |
| F3. Three questions | "Where is the money? What does this do to it? What do we do now?" | Very plain | Hard to show as a system; weak on governance |

**F1 in full:**

| Step | What it does | Brief areas | Output for the Wongs |
|---|---|---|---|
| **Map** | Where sustainability touches this family's money; who decides what, and how disagreement is settled | 1, 2 (baseline), 4 | The balance sheet by exposure; four profiles; the mandate |
| **Price** | The two-sided price tag on each decision (§3: the money side and the world side), with its evidence tag and horizon | 2 (cost curve), 3 (evidence), 5 (scenario) | The centrepiece chart (§4.4) |
| **Decide** | Each decision's corner (below), then the instrument and the date | 2 (instrument), 3 (allocation), 4 | The decisions; the refusals |
| **Govern** | Dashboard, triggers, restating when data improves, giving that is funded | 5 (controls), 6 | One page, checked yearly |

**The four corners** (rules, so the framework decides, not us; 5 Nov). Each decision lands in one corner by its two-sided
price tag:

| | **Changes something real** | **Changes nothing real** |
|---|---|---|
| **Good for their money** | **Do it.** No choice needed: both win. E.g. the vans; recycled content; customer emissions data protecting the sale | **Do it, but don't call it green.** Good finance or risk management. E.g. the reverse mortgage as a hedge against old flats losing value |
| **Costs them money** | **The only real choice: pay for it knowingly,** within a values budget the family set in advance. E.g. the scholarship | **Refuse it.** It costs and changes nothing; the label is all it offers. E.g. the green-loan label at HK$0.9M; the clean-energy fund; "compostable" claims for packaging the food-waste bins turn away |

- **We are not asking the family to choose between their money and the world.** Most of the time they don't have to; where
  they do, the cost is small, visible and theirs to decide. Line for the talk: *"Most of the time, the family doesn't
  have to choose. Where it does, the cost is small, visible, and theirs to decide."* This is the brief's "quantify the
  price of values ... and the evidence that it need not give up much".
- **The choice is made once, in the mandate, not decision by decision:** Carmen's values budget (up to HK$… a year, or …
  points of the odds) covers the "pay for it knowingly" corner; Adrian's portion isn't touched. That is also the brief's
  "how disagreement between decision-makers is resolved".
- **Carmen's ESG funds** cost a little and change nothing real (shares bought on the market fund nothing new). The
  framework doesn't block them: she can choose them from her values budget, labelled honestly as alignment, not impact.
  Line for the talk: *"We don't refuse Carmen's values. We refuse the label."*
- **Two caveats to keep:** (1) "most of the Wongs' real impact sits in the top-left corner" is EXPECTED until the model
  prices each decision (§10); (2) win-wins have dates: the vans pay partly because of today's fuel prices and a tax
  waiver that ends 31 Mar 2028, and recycled-PET prices swing (well above virgin in 2023). Saying when "green pays" and
  acting before the window closes is more credible than saying it always pays, and it is what "decision-ready" means.

**The five kinds of finance, placed** (a small picture on the framework slide, not spoken): green finance → the vans and
LED; sustainability-linked → refused at this size; transition finance → Carmen's business plan; impact → the funded
scholarship (and the business's own cuts); ESG integration → the portfolio.

### 4.3 What the judges should remember, the hook and the close

**Three takeaways:**
1. Labels mislead (the opening).
2. Show what every decision does, to the family's money and to the world: most of the time they don't have to choose.
3. For the Wongs, pricing changed [N] decisions: the sustainability that matters was in the business and the flat,
   and they end up [HK$…] better off and [… t] a year lower.

**Hook options:**
- **H1, labels vs reality** (recommended, combined with H3's first line): four labels, each with its reality, one line
  each. An ESG fund on the SFC's list: US$0 in assets. "Compostable": legally plastic, and the food-waste bins turn it away. A
  green mortgage: no lower rate, a one-off HK$0–3K here. A green grant: starts at a HK$100M loan, and pays for the
  review, not the interest. (Wording checked at primary sources: `research/hook_fact_checks.md`.)
- **H2, the cup:** hold up a "compostable" cup. "Sold as sustainable. Hong Kong's law counts it as plastic, and the food-waste
  bins turn it away." (Don't say "landfilled" unless EPD confirms it.) Strong in a room; a gimmick if delivered nervously.
- **H3, the fund alone:** "One of the few global equity index funds on the SFC's official ESG list holds US$0." Stands
  alone for any judge; optionally one more line: "We know, because we recommended it ourselves." Call BOCI-Prudential
  first (Win).

**Close options:**
- **C1, the callback** (recommended): "A label tells you what something is called. We showed what it does. For the Wongs,
  that changed [N] decisions, cut [… t] a year and left Ryan and Chloe [HK$…] more."
- **C2, the family's voice:** "Carmen asked for her values in the plan. We didn't refuse her values; we refused the
  label." Can follow C1.

**Land positive:** the opening montage can read as cynical about ESG. The close must show the Wongs doing *more* real
sustainability (about 127 t a year from the vans and recycled content, ESTIMATED; a scholarship actually funded) and
ending up better off.

### 4.4 The centrepiece chart (slide 5)

Every sustainability decision for the Wongs on one chart, ranked by what it is worth to the family, coloured by verdict,
with tonnes on each bar where they apply: the brief's abatement cost curve, applied to the whole family rather than one
business. No other team can draw it without a model like ours.
- **About 8–12 decisions:** vans and LED; customer emissions data; recycled content; the green-loan label (refused);
  Carmen's ESG portion; the clean-energy fund (refused); the green bond fund; reverse mortgage vs downsizing; the green
  mortgage (refused); the warehouse green lease; the funded scholarship.
- **One measure on the axis** (Pete decides in the build): the change in the inheritance (HK$, today's money) or points
  of the odds; the other as a label on each bar.
- **Alternative form (5 Nov):** plot each decision as a dot on the four corners (across: what it does to the family's
  money; up: what it changes in the world, in tonnes or another real effect). It shows the framework and the result in
  one picture, and makes "most of what's real also pays" visible at a glance, if the numbers bear it out. Render both
  and choose (the slide-design skill).
- **Needs** the two model fixes in §3 and a price tag per decision. **By Tue 10 (Pete).**
- The business's own abatement cost curve (the brief's area 2 asks for one) goes on slide 6 or in the backup.

### 4.5 Storyline v2 (about 9:05 spoken; about 9:20 with names and handovers)

Evidence status: **HAVE** (in a brief, checked) · **CHECK** (in a brief; confirm at a primary source before it goes on a
slide) · **MODEL** (Pete's runs) · **CALL** (ask someone) · **CASE** (the case's figures).

| # | Step | Time | Title (draft) | Must prove | Evidence | Required item |
|---|---|---|---|---|---|---|
| 1 | Hook | 0:45 | A green label says what it's called, not what it does | ESG fund on the SFC list holds US$0; "compostable" is legally plastic and the food-waste bins turn it away; green mortgage: no lower rate, HK$0–3K; grant from a HK$100M loan, for the review, not the interest | Fund: HAVE + CALL; PLA, mortgage, grant: HAVE (primary sources, `hook_fact_checks.md`) | — |
| 2 | Answer | 0:40 | [N decisions, HK$… capital: odds … → …, HK$… more to the children, … t less a year] | The recommendation, the capital, both outcomes | MODEL; vans HK$1.9M ESTIMATED; scholarship fund ≈HK$0.48M ESTIMATED | Recommendation, capital, outcomes |
| 3 | Framework | 0:45 | Four steps show what a decision does, not what it's called | Map, Price, Decide, Govern; the two-sided price tag; the four corners; the five kinds of finance placed | Framework brief (definitions) | The framework |
| 4 | Map | 0:50 | The Wongs' sustainability sits where their money sits: a flat and a business | Four people and what each wants; flat HK$11.5M, business HK$5.0M, investments HK$10.5M; their plan in plain words (retire at 65 and 62, sell the business in stages, release the flat at retirement); the label approach touches only the HK$2.6M in ESG funds; "the family in this year's competition case" | CASE | Profiles (area 1) |
| 5 | Price | 0:50 | [Most of what's real also pays: … of … decisions in the top-left corner] (if the numbers bear it out; §10, 7) | The centrepiece chart (§4.4): every decision's money side and world side | MODEL; tonnes ESTIMATED | Trade-off visible |
| 6 | Decide: business | 1:00 | Carmen's transition is cheap; the finance products don't fit her size | ≈98% of emissions upstream; vans and LED HK$1.9M pay without green finance; green-loan label refused (discount ≈ review cost); grant HK$100M+; supply-chain finance anchors ≈US$100M; customer data protects the sale (≈HK$209K per 1% of sales) | Baseline ESTIMATED on an ILLUSTRATIVE business; vans: CHECK diesel price; grant, HKEX Scope 3: HAVE (`hook_fact_checks.md`); data → sale: ESTIMATED | Quantified structure; a refusal |
| 7 | Decide: mandate | 0:40 | Carmen's values get a budget; Adrian's money stays his | Separate portions; a cost limit in HK$ a year; Hong Kong doesn't require asking about sustainability preferences, we do | Fees: CHECK (Win, fund documents); HKMA FAQ: CHECK; price of values: MODEL | Mandate; price of values |
| 8 | Decide: portfolio | 0:50 | [The portfolio is measured, not labelled: weights, HK$… a year, carbon …% lower] | Weights per parent; fees; a carbon figure; refusals (clean-energy fund −31% in 2023; ≈80% of sustainability-linked bonds fail CBI alignment); greenium 0–8bp | Weights and fees: CHECK; carbon: none measured yet; refusals: CHECK | Portfolio with weights and costs; a refusal |
| 9 | Decide: home | 0:50 | [The reverse mortgage protects the odds; downsizing leaves the children more] | If old flats lose value, downsizing loses … points, the reverse mortgage …; leave by the building's 50th year; green mortgage refused; warehouse green lease at the 2027 renewal | MODEL (inheritance must include the flat); HKMC rules HAVE; payouts by age CHECK | A trade-off; a refusal |
| 10 | Stress | 0:50 | [A sudden transition costs … points; most of it is market risk no label hedges] | The scenario's effect on business, flat and portfolio; the defences | MODEL (Lookbua's shocks); NGFS/HKMA sources CHECK | A scenario; risk register (one line, full in backup) |
| 11 | Govern | 0:45 | One page, checked every year, with triggers that force a decision | Money, carbon, impact, milestones; a "can't measure yet" column; restating when data improves; the scholarship funded in 2027–36 while tax relief applies | Framework brief; IRD relief HAVE; cost MODEL | A dashboard; governance; funded giving |
| 12 | Close | 0:20 | [From a label to what it does: N decisions changed, … t a year, HK$… more] | The callback; "we don't refuse Carmen's values, we refuse the label" | MODEL | — |

**Backup slides** (after slide 12; §7): the business's abatement cost curve; the five instruments compared (tenor,
covenants, review cost, subsidy); fund-by-fund fees and carbon; the full risk register; the scenario's inputs; the
sustainability annex to the investment policy; the model's assumptions; the rules map; **the same framework on a factory
owner exporting to the EU** (CBAM and a sustainability-linked loan apply; the verdicts change).

**Speakers** (decide at the workshop; rule 9: each member presents his or her own part):

| Option | Pete | Fahtai | Win | Lookbua | Note |
|---|---|---|---|---|---|
| **B (recommended)** | 1–3, 12 (2:30) | 4–6 (2:40) | 7–8 (1:30) | 9–11 (2:25) | Balanced; four handovers; Fahtai presents the chart, so he needs the model fluently (he reviewed it in Round One) |
| A | 1–5, 12 (4:10) | 6 (1:00) | 7–8 (1:30) | 9–11 (2:25) | Pete carries the whole spine; Fahtai's part is short |

Under the 5 Nov research split (Pete: areas 1, 2 and 4), Pete would be presenting slides 1–6 and 9 as well, about 6
minutes of 9: someone else must present the business and the home, and own their questions.

**Old slide numbers → new (v1 → v2):** 1 → 1 · 2 → 2 · 3 → 4 · 4 → 3 · 5 → 7 · 6, 7 → 8 · 8, 9, 10 → 6 (detail to backup) ·
11 → 9 · 12 → 10 · 13 → 11 · 14 → 12 · new: 5 (the chart). §8's slide numbers are still v1's until v2 is agreed.

### 4.6 Agreeing it: by messages, not a meeting (Pete, 5 Nov)

Pete sends the team his defaults for §4 (thesis A′, framework F1, storyline v2, speakers, the open facts) and locks them
on **Sat 7 Nov, morning**, unless someone objects. Silence in a chat can look like agreement, so the message asks for
replies only a reader of §4 can give:
1. Any objection (by **Fri 6, 21:00**).
2. The thesis in their own words, one sentence: the check that everyone owns the argument.
3. **The live test:** "Adrian wants to buy carbon credits to offset the family's flights. Which corner, and why?" If the
   answers land in about the same place, the framework works; if they scatter, fix the framework, not the example.
   *Expected answer:* it costs money, and changes something real only if the credits are verified and additional (would
   the cut have happened anyway?). Cheap avoidance credits mostly fail that test: refuse the label ("carbon-neutral
   flights"). High-quality removal credits could be "pay for it knowingly" from Carmen's values budget. And the family's
   own cuts (the vans, recycled content) give measured tonnes and pay.
4. By **Sun 8**: each owner's list of the claims their slides must prove, marked have or need to check (§4.5's "Must
   prove" column). That list is the remaining research; anything no slide needs goes to backup or nowhere.

If the replies show real disagreement (on the thesis, the client or the split), hold a 15-minute call rather than
argue it out in the chat.

**Then:** an outside critic (a lecturer or practitioner) hears the agreed storyline before the build; the script is
written before the slides; rehearsals are recorded and watched back.

### Storyline v1 (5 Nov, superseded if v2 is agreed)

v1 ran 14 slides in order of asset size (the funds → the business → the flat) with the framework as one slide; v2 keeps
its content and makes the framework the spine. v1's full table is in this file's git history (commit "Final:
supply-chain brief; keep the Wongs; assume no judge read Round One").

### How we stand out (5 Nov; inference about the other teams, not fact)

**What most teams will probably do:** walk the six areas in order (a checklist talk); open with definitions; present
the grant, green mortgages and CBAM as benefits or threats without checking whether they reach the client; invent a
factory owner who exports to the EU; repeat "the greenium is small" (the brief hands everyone that line); claim "impact"
from ESG funds. The brief's hints (a refusal, a trade-off, honesty about the greenium) are table stakes.

**Our moves, strongest first:**
1. **One tag for every decision:** the two-sided price tag (§3) and its four corners (§4.2), the money side from our
   model. Nobody else can show sustainability in the family's odds and inheritance beside its tonnes.
2. **Check the brief's toolkit against the client:** one slide, tool by tool, with checked numbers (grant: HK$100M
   minimum; green mortgage: no lower rate, HK$0–3K, BEAM Plus certified only; CBAM: doesn't apply; the Taxonomy: no packaging or
   wholesale activity), then what does reach her (the e-van tax waiver to 31 Mar 2028, the HKMC loan guarantee, her
   customers' FY2026 reporting). The brief: "Plumbing, however, does not tell a client what to do."
3. **The framework catching a real failure:** a fund on the SFC's ESG list that holds US$0 (§2). It is the brief's
   "difference between a label and a financed outcome", and it lands with any judge without history. That the label
   approach (our own Round One included) recommended it is one optional line, not the point. Call BOCI-Prudential first
   (Win).
4. **Our client is the representative one:** Hong Kong has 84,395 import/export and wholesale SMEs against 7,208 in
   manufacturing (TID, as at June 2025, https://success.tid.gov.hk/english/aboutus/what_are_sme.html). Say it when we
   introduce the business.
5. **The client's own label as the risk:** Carmen's "compostable" products count as plastic under HK law (Cap. 603
   s.3A), and the food-waste bins turn away packaging and utensils (`research/hook_fact_checks.md`).
6. **Dates, not just weights:** e-van tax waiver ends 31 Mar 2028; warehouse lease renews 2027; customers report from
   FY2026; solar feed-in tariff ends 2033; HKMC case by case above building age 50; the sale 2035–39.

**What most teams will miss, and where we cover it:** ESG funds bought on the market are alignment, not impact (slide
4); a sudden transition raises inflation, which hurts fixed-HK$ retirement income (slide 12); here the physical risk is
heat, not flood (slide 11; a heat-and-health source would strengthen it, Lookbua); only the family's own emissions are
measured, the rest estimated or modelled (slide 13, a column); a restatement policy when the data improves (slide 13);
tax relief on gifts only while earning, so fund the scholarship in 2027–36 (slide 13); half the business's savings are
Carmen's if she owns half (§5 decision); Hong Kong doesn't require advisers to ask about sustainability preferences (slide
5); a "can't measure yet" column on the dashboard (slide 13).

**Options for the day (Pete to decide):** hold up a "compostable" cup in the first 30 seconds ("sold as sustainable; the
law counts it as plastic, and the food-waste bins turn it away"); a one-page price card for the questions, so any "what about X?" is
answered in the framework's own terms; backup slides numbered so the speaker can type the number and press Enter to jump.

**The strongest case against:** too many refusals read as "these students just say no" (pair each with what we do
instead and its money: the vans save ≈HK$0.37M a year); "points of the odds" feel abstract (always pair with HK$); the
US$0 reveal backfires if the fund is on sale somewhere we didn't check (hence the call).

## 5. Who does what, starting now

Each person researches, builds, presents and answers questions on the same part (rule 9: each member presents his or
her own part). The only hand-offs between people are listed under "Gives"; everything else starts today.

**Team meeting, 5 Nov:** everyone first researches the overall context, then the brief's key areas; Pete takes areas 1,
2 and 4; who takes 3, 5 and 6 is not recorded here yet. **Open (review, 5 Nov):** that split puts the two heaviest areas,
the model, the deck and the lead on one person, and rule 9 means whoever presents the business or the flat answers the
judges' follow-ups on it. Suggested instead: Pete owns the argument (area 1, area 6, the model, the storyline, final say
on what each slide proves) and pairs with Fahtai on area 2 and Lookbua on area 4, who research and present them; Win
area 3; area 5 split by subject (the business's rules and greenwashing to Fahtai, the scenario and risk register to
Lookbua, fund checks to Win). If Pete keeps 1, 2 and 4, hand the model runs to Fahtai. Pete decides; the table below is
the 4 Nov split until then.

**Research, time-boxed:** shared context is one afternoon each (the brief, the Key Areas sheet, this plan, a skim of
all four briefs in `Final/research/`; the judges can ask anyone anything). After that, research answers a question a
slide asks: start from your brief's "check" items and open items (the research agents ran out of web searches). **Research
closes Tue 10 Nov;** after that, fact checks only, so the build and the rehearsals get their days.

**Team decisions still open** (the briefs had to assume these; every number downstream depends on them):
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
| Thu 5 Nov | Team meeting held: research first (§5). Slide deadline confirmed: 17:00 Mon 16 Nov |
| Fri 6 | Shared context done (one afternoon each); **replies due 21:00 (§4.6)**; Pete locks thesis, framework, storyline v2 and speakers on Sat 7 morning; the split settled (§5); the open decisions (Carmen's share, the warehouse, the building, the fund) made. Pete starts the model price tags now (they gate slides 2 and 5) |
| Sat 7 | Go / no-go on the business structure (the Wongs stay or we switch); area 2's owner decides |
| Sat 7 – Tue 10 | Targeted research to numbers; inputs to the model (Mon 9); model numbers and price tags out (Tue 10); first slides. **Research closes Tue 10** |
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

## 8. Hard questions (first list; owners add to it; slide numbers from storyline v1)

| Who asks | Question | Answered on | Weak? |
|---|---|---|---|
| ESG strategist | Is "sustainable packaging" itself a green label? Compostable packaging in a city without industrial composting? | 8 | EPD guidance: PLA is regulated plastic, compostables "premature"; ordinance text to read |
| Practitioner | Why not a sustainability-linked loan? Why not the Grant Scheme? Why no supply-chain finance? | 9 | Grant: HK$100M minimum (HKMA guideline, 24 Apr 2026); supply-chain finance: anchors ~US$100M of trade spend; the ESG discount unpublished |
| Practitioner | You reused the case: what's new? | 1, 4, 12 | The framework, and its verdicts against the label approach; the case only supplies the family's facts |
| A judge who read Round One | Your Round One recommended that fund. Why should we trust this plan? | Q&A | Own it: the framework's product check (assets, documents, tracking) caught it; the label didn't. That is the argument of the talk |
| Any judge new to the case | Who are these people, and why them? | 3 | One-line origin + the family picture (§3) |
| Practitioner | Your financing part is thin: isn't "Financing the Transition" the topic? | 9; backup | The five instruments compared with numbers; the factory-owner backup slide |
| ESG strategist | How do you know your ESG fund is better than the plain index? Carbon intensity, coverage? | 6 | Open (Win): no measured carbon figure yet |
| Banker | Would a bank lend for the vans? Coverage, collateral? | 9 | Open (area 2's owner) |
| Regulator | Are you licensed to advise on the loan or the funds? Suitability per person? | 5, 13 | Draft: we coordinate with the bank and licensed parties |
| The family | What does Adrian give up for Carmen's values? | 5 | Price of values in HK$ (Win, Pete) |
| Practitioner | Your scenario: why those shocks, from where? | 12 | Sources from NGFS / HKMA (Lookbua) |
| Anyone | What would you not do? | 7, 9, 11 | Refusals with numbers: clean-energy ETF, green-loan label, green mortgage |

## 9. Facts to check before they go on a slide

Each research brief has its own full list (its last section). The ones the storyline leans on:

| Fact | Problem |
|---|---|
| Grant Scheme (GSF): loans use Track II only, "at least HK$100 million", up to 75% subsidy if Taxonomy-aligned, caps HK$800K | **Confirmed** at the HKMA guideline (24 Apr 2026): caps are per loan; the grant pays for the review, not interest (`research/hook_fact_checks.md`) |
| BOC-Prudential MSCI World ESG Index Fund: US$0.00 every month Sep 2024 – Sep 2026; no offering document | Checked twice (agent and us, 4 Nov, HKEX fund platform and SFC data file). Ask BOCI-Prudential before saying "never launched": the record shows zero assets, not the reason |
| Van saving HK$86K a year each | Rests on a HK$37.93/L diesel list price; find a fleet price; at HK$25/L the saving is smaller and the vans still pay |
| Green-loan discount 25bp; sustainability-linked ratchet size; external review fees | ILLUSTRATIVE: no HK bank publishes an SME green discount; find a bank quote or a published range |
| HKMC reverse mortgage pays about 36% more per HK$1M at 68 than at 60 | From HKMC's 2026 examples (single borrower, ages 60 and 70); check the joint-borrower table |
| ESG ETFs trailed IWDA by 0.4–2.9 points a year over five years | Window-dependent; quote with the period and the long-run figure beside it |
| Scope 3 about 98% of the business's footprint | ILLUSTRATIVE business, published factors (UK DESNZ 2025): say "on our assumptions" |
| Recycled PET at the same price as virgin, Southeast Asia, Oct 2026 | Read from search extracts of S&P Global and Argus (the sites refused automated fetches); find a readable source and date it. Prices swing: quote the 2023 peak beside it |
| PLA counts as regulated plastic; compostables "premature" | **Confirmed** in Cap. 603 s.3A and EPD to LegCo (30 May 2023). Don't say "O·PARK rejects PLA" or "landfilled": say the food-waste bins turn away packaging and utensils. Phase 2: no date as of 7 May 2025 |
| Supply-chain finance anchor guide US$100M of trade spend | One bank's published guide; no Hong Kong bank states a minimum |
| EU CBAM: definitive from 1 Jan 2026; importers under 50 t a year exempt; ~180 downstream products proposed from 2028, not adopted | Law-firm and press summaries; check the Official Journal and the Commission's CBAM pages |
| HKEX: Scope 3 mandatory for LargeCap issuers from financial years starting 1 Jan 2026; comply-or-explain for the rest | **Confirmed** in Appendix C2 (paras 16–17, 28(c)): FY2026 reports, published in 2027, with a data relief |
| Hong Kong Taxonomy Phase 2A in 2026 (transition and adaptation) | From the brief; confirm with HKMA |

## 10. Untested assumptions (test, don't build on)
1. Judges accept the competition's own family as a "representative Hong Kong client" rather than marking it down as
   recycled (the talk introduces them from scratch and compares against the label approach, not our Round One).
2. Naming the label approach, and saying in one line that we followed it in Round One, reads as independent thinking,
   not as admitting a weak plan.
3. A distributor's transition story is rich enough for "Financing the Transition" (Fahtai's go / no-go, Sat 7).
4. Sustainability moves the business's sale price or the flat's value enough to matter. The research found no
   published evidence that emissions data raises an SME's sale price, and one old study of BEAM Plus price premiums
   (+4.4%, one district, 2012–14). Present these as sensitivities ("if a buyer discounts it by HK$1M, the family loses
   about 4 points"), not as findings.
5. About 1,200 words fit 9:20 live, with four speakers each saying their name.
6. The venue notebook shows our font, and the file needs nothing newer than its PowerPoint.
7. Most of the Wongs' real impact sits in the corner that also pays (vans, recycled content, customer data), and the
   corner that costs money for real impact is small (5 Nov). EXPECTED until the model prices each decision; if it comes
   out the other way, the talk says so and the values budget carries more of the plan.

## 11. On the day (guidelines, rules 4–14)
- Dress formally; name tags visible. Say "Team Axis" before the first speaker; each speaker says their simple name before
  their part (there is a best presenter award). Never say the university's name.
- Warnings at 3 minutes and 1 minute left. **Over 10:30 disqualifies the team.** Aim for 9:20.
- Teams that haven't presented wait outside, so we won't see the others before our turn.
- One member checks the machine and the slides at 09:30. No slide can change after 16 Nov.
