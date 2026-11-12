# Area 5: Risk, Regulation and Greenwashing (Lookbua)

**What the Final asks, in one line:** take the Wongs' normal financial plan and add the environment as a factor. Two directions: (A) how the environment could hit their money, (B) how their money could affect the environment. Area 5 checks the risks in both directions, the rules around them, and whether our own green claims are honest.

**Tags:** SOURCED (a named source) · ESTIMATED (our arithmetic) · ILLUSTRATIVE (our assumption) · MODEL (exploratory model run, not a slide number until Pete exports it) · CHECK (not confirmed).
Sources are repo files in `finplan/Final`. I added no new research here; this re-organises what the briefs already contain.

---

## 1. The three levels

| Level | Question | Contains |
|---|---|---|
| **1. Sustainability-specific** | What is new because of the environment? | **1A** Environment → Wongs' money · **1B** Wongs' money → world |
| **2. Plan risks that sustainability makes bigger** | Where does it land in the plan? | Liquidity, valuation, liability, data |
| **3. Rules, conduct, greenwashing** | Are we allowed, and are we honest? | HKMA, SFC, HKEX, IRD, laws, our own claims |

The brief's eight risk types fit like this: transition and physical → 1A; reputational → 1B and 3; liquidity, valuation, liability, data → 2; conduct → 3.

---

## 2. LEVEL 1A: Environment → the Wongs' money

Base for points: plan **with** medical review (96.8% odds to Carmen's 89). Source for all points: `Final/model_runs.md`. **Agree one base with Pete.** On the older base (82.6%) the scenario costs −15.9 points.

| # | Risk | Hits | Size | Plan response |
|---|---|---|---|---|
| T1 | Late, sudden policy 2030–31: markets fall, inflation rises, HK recession | Portfolio, flat, business | **−7.3 pts** (96.8% → 89.5%): portfolio −3.8, flat −0.7, business −0.8 (MODEL) | Diversified funds, Treasury ladder, guardrails, medical review at 75 |
| T2 | Customers' Scope 3 reporting (LargeCap from FY2026) → buyer discounts a business without data | Business sale | About −1.8 pts per HK$1M off the sale price; a 5% customer lost = −0.9 pts (MODEL; links ILLUSTRATIVE) | Emissions baseline (Fahtai) |
| T3 | Plastics Phase 2 (no date); "compostable" PLA counts as plastic | Carmen's stock | PLA stock about HK$0.77M (ILLUSTRATIVE) | Stop the claim; short tableware stock |
| T4 | Energy prices (CLP fuel charge 39.4 → 47.4 ¢ in 2026) | Household, warehouse | About HK$1K a year household (ESTIMATED) | LED, Grade 1 air-con at replacement |
| P1 | Heat: 52–53 very hot days in 2024–25 vs 14 baseline | Health, cooling cost | About +HK$700 a year cooling (ILLUSTRATIVE); health is the real cost | Medical cover, tier review |
| P2 | Typhoon or flood damage to building's common parts | Flat (OC levies, insurance) | Repair size not found (CHECK) | Check OC has property cover (compulsory policy is liability only) |
| P3 | Warehouse flooding | Business stock | Not sized | Upper floor, racking, business-interruption cover, lease clause |
| P4 | Storm surge at Tai Kok Tsui | Flat | Remote to 2050: not on CEDD's 26 areas or DSD blackspots (SOURCED) | Release by 2045 |
| V1 | Old-building discount on the flat (HKMA RM05: 4–21% by about 2050, "older = larger impact"; not a forecast) | Flat exit | At −10%: reverse mortgage −0.5 pts, downsizing −3.2 pts (MODEL) | Yearly price-gap trigger; route chosen on the gap |

**Simple finding:** most of the loss in a climate scenario comes through ordinary market and inflation risk, which no green label hedges. The flat route is the decision that changes the result (89.5% vs 82.7% if they downsize and only the old flat falls).

---

## 3. LEVEL 1B: The Wongs' money → the world

For each action: does it change something real, or only change who owns it? (additionality)

| # | Action | World effect | Real or label? | Money cost | Source |
|---|---|---|---|---|---|
| W1 | **Listed ESG funds** (Carmen's portfolio, ~25–28% of investable) | Lower carbon intensity of what they hold, not new emissions cut. Shares bought on the market fund nothing new. | **Alignment, not impact.** Carbon intensity not yet measured (CHECK, Win). | About HK$5.1K a year in fees vs plain twins; tracking up to about HK$26.6K a year in a bad five years | `area3_portfolio.md` §4 |
| W2 | **Green bond fund** (Allianz, Carmen 10%) | Funds green projects, but no impact report found. Greenium only 0–8bp. | Partly real, unproven | Fee gap HK$2,153 a year; trails its benchmark about 1 point a year | `area3_portfolio.md` §1 |
| W3 | **Scholarship** | Students funded (about HK$30K a year for 20 years) | **Real and additional** | Unfunded for life: −2.8 pts. Funded 20-year fund (HK$0.48M): −0.7 pts (MODEL) | `Decision_List.md` G1 |
| W4 | **Carmen's business: vans, LED, recycled PET** | About 26 t a year (vans 19.3, LED 4.1, air-con 2.8) plus about 108 t from recycled PET. About 134 t total. Her own operations are only 48 t of a 2,760–3,250 t footprint. | **Real**, and it pays | Vans save about HK$0.37M a year; HK$1.91M capex | `area2_business.md` §3d |
| W5 | **Green mortgage** | None: a one-off rebate only | **Label** | HK$0–3K once; no lower rate | `hook_fact_checks.md` §3 |
| W6 | **Flat retrofit** | Tiny | Small real effect | About HK$1,900 a year saved | `area4_property_scenario.md` §3.2 |
| W7 | **Carbon credits** (e.g. Adrian's flights, if raised) | Real only if verified and additional | Usually label | Costs money | `Final_Plan.md` §4.6 |

**Simple finding:** the real world impact sits in Carmen's business and the scholarship. The portfolio buys alignment. The mortgage buys a label.

---

## 4. LEVEL 2: Where it lands in the plan

| Risk | Why sustainability makes it worse | Number | Defence |
|---|---|---|---|
| **Liquidity** | Flat is 42% of assets (HK$11.5M of HK$27.19M). Above building age 50, HKMC reverse mortgage is "case-by-case" and buyers' loans shrink (age + term ≤ 75 years). | In 2045 a buyer gets 26 years, not 30: about 9% higher repayments (ESTIMATED) | Release by completion year + 49 (2045 for a 1996 building) |
| **Valuation** | Old-building discount; sale price depends on data and lease security | See V1 and T2 above | Yearly trigger; green lease with renewal option to 2039 |
| **Liability** | Ignored MBIS/MWIS notice (proposed fines up to HK$200K, HK$300K if injury); false green claim to a customer (Trade Descriptions Ordinance, up to HK$500K and 5 years, our inference) | Not sized | Comply with notices; no unproven claims |
| **Data** | Building age, ground level, OC insurance, repair costs unknown; HKMA price shock unpublished; NGFS damage figures retracted; Scope 3 of holdings unreliable | — | Tag every number; ranges; "can't measure yet" column |

---

## 5. LEVEL 3: Rules (who must do what)

Key point: **most of these rules bind banks, fund managers and listed companies, not the Wongs.** They matter because they change what the Wongs' bank, funds and customers do.

| Rule | Who it binds | What it says | Effect on the Wongs |
|---|---|---|---|
| **HK Taxonomy** (HKMA; Phase 2A 22 Jan 2026, 25 activities; 2B prototype 39) | Voluntary, for banks, issuers, corporates | Classifies green and transition activities | Vans, LED, solar = "Green". No packaging or wholesale activity. |
| **HKMA GS-1** (30 Dec 2021) | Banks | Manage climate risk; scenario analysis; collateral may lose value | Their mortgage and Carmen's loan are assessed |
| **HKMA GS-2** (22 Sep 2026) | Banks | Transition-plan documentation by 1 Jul 2030 (CHECK "must" vs "should") | Carmen's lender will ask for her emissions data |
| **HKMA stress tests** | Banks | Pilot: 32% of property lending in "vulnerable areas"; second: "substantial correction" in prices, no % published | Source of our flat scenario, not a forecast |
| **HKMA sales rules** (29 Nov 2023) | Banks selling green products | Asking sustainability preferences is "not a mandatory requirement" | We ask anyway, voluntarily |
| **SFC circular 21EC27** (29 Jun 2021, in force 1 Jan 2022) | ESG funds | ESG must be a key focus; names can't overstate; annual assessment; failing funds removed. The SFC list is not an endorsement. | The US$0 BOC fund is on the list |
| **HKEX App. C2** | Listed companies | Scope 1+2 mandatory FY2025; full Part D incl. Scope 3 mandatory for LargeCap FY2026 (reports 2027) | Carmen's listed customers will ask for data |
| **HKFRS S1/S2** (12 Dec 2024) | Large public entities by 2028 | ISSB-aligned disclosure | Indirect |
| **IRD charity rules** | Donors | Deduction for cash to an s.88 charity, up to 35% of income, only while earning | Fund the scholarship in 2027–28; say "tax-exempt charity under s.88", not "registered charity" |
| **Cap. 603 s.3A** | Anyone selling plastic items | Plastic = any polymer, no "compostable" exemption | PLA is regulated plastic |
| **Trade Descriptions Ordinance** | Sellers | False description of goods is an offence (no green-claims case found) | Carmen's claims |
| **MBIS/MWIS** | Building owners | Inspections from age 30 (MBIS) and 10 (MWIS); tougher penalties proposed | The flat |
| **Climate Action Plan 2050** | Policy direction | Carbon-neutral before 2050; halve (vs 2005) before 2035 | Direction of grid factor and buyers' expectations |
| **EU CBAM / PPWR** | EU importers / EU packaging | Paper and plastic are outside CBAM; PPWR only for EU-bound packaging | **Do not apply** (say so) |
| **MiFID / ESMA** | EU only | Not HK law | We borrow the structure voluntarily |

**Our own conduct:** advice on funds, mortgages and insurance goes through SFC-licensed, HKMA-registered and IA-licensed parties. We coordinate, charge no commission, and use one risk profile per person. (`area4_property_scenario.md` §6, C1 and C2)

---

## 6. GREENWASHING DEFENCE

**Fact:** Hong Kong has no specific greenwashing law and we found no enforcement case. Rules exist for ESG funds (SFC) and banks' sales (HKMA). The EU's SFDR is the reference framework (CHECK: the text has not been read in the repo).

**Four controls** (the brief's list):

| Control | Rule we use | Example |
|---|---|---|
| **Baseline** | Fix a plain twin in writing and compare to it | ESG funds vs plain funds; flat price vs a ~10-year-old flat |
| **Third-party verification** | A named outside source for every claim; check a product exists before its label; two-rating test for equity ESG funds | BOC fund: US$0 in every filing; ESG ratings from different agencies correlate only about 0.54 |
| **Conservative claims** | "Aligned", never "impact", for listed funds; never net avoided emissions against footprint; count HK$3.0M of the HK$5.0M business; no price premium claimed | Refuse green mortgage; no "compostable"; no 4.4% label premium on the next flat |
| **Restatement** | If a source or number changes, show old and new and say why | Round One 2045 reverse mortgage: about −2 pts, not −9 |

**Greenwashing risks in our own plan (check each before the talk):**

| Our claim or choice | Problem | Fix |
|---|---|---|
| "25% ESG" counted by SFC list | The list is a label; an unbuyable fund counted for 56% | Count by measured outcome (carbon intensity ≥30% below parent, coverage ≥80%) |
| Green bond fund | No impact report; fee 10–50× the greenium | Keep only with impact report and no entry charge, or move to plain bonds |
| "Impact" from listed funds | No additionality | Say "alignment" |
| Scholarship "through a registered charity" | Loose wording | "A tax-exempt charity under s.88" |
| Carmen's "sustainable packaging" | PLA is plastic; no composting route | Stop "compostable" claims |
| Implied temperature rise | Opaque methods | Show a range or nothing |
| Any carbon number for holdings | Scope 3 data inconsistent | Mark "not measured yet" |

**Claims audit (reusable by any planner):** one table, one row per green claim: claim · source · date · tag · confidence · checked by. Start with the four hook claims already checked in `hook_fact_checks.md`: HKMA grant minimum HK$100M; PLA is plastic; green mortgage HK$0–3K; Scope 3 for LargeCap from FY2026.

---

## 7. A reusable screen for any client (the framework piece)

Five questions a planner can ask about any sustainability decision:
1. **Environment → client:** which climate or transition risk hits this asset, and by how much?
2. **Client → world:** does this action change something real, or only change who owns it?
3. **Plan:** does it hit liquidity, valuation, liability or data?
4. **Rules:** which rule binds whom, and does it apply to this client?
5. **Claims:** is every green word backed by a source, a baseline and a conservative claim?

---

## 8. What changed in our earlier advice (for the "[N] decisions")

My area's contribution (see `Decision_List.md` for the full list):
- **H2** green mortgage: not considered → refuse.
- **H1** flat: "decide in 2037" → yearly trigger plus a deadline (the building's 50th year).
- **P2/P6** counting rule: SFC list → measured outcome.
- **G1** scholarship: unfunded promise → funded 20-year fund.
- **R-new** claims audit and restatement policy.

Pete settles the final count. Only decisions that change money or tonnes should be counted.

---

## 9. To fix or check

**Fix:**
1. Warehouse: align to Fahtai's 7,500 sq ft and 60,000 kWh a year.
2. Use HK$0–3K for the green mortgage.
3. Agree one scenario base with Pete.
4. Verify the 2045 reverse mortgage payout in HKMC's calculator.

**Check:**
- GS-2: "must" or "should" by 1 Jul 2030; issue date.
- SFDR text before quoting.
- SFC circular 24EC58 and Consumer Council 11 Jul 2025 wording.
- MBIS/MWIS bill status.
- Building facts (completion year, OC insurance); Tai Kok Tsui ground level; CLP 2026 tariff.
- Heat and health source.
- NGFS Phase VI; HKMA second stress test price path (say "unpublished" if not found).
- Hot-house and tail scenarios on the recommended base (ask Pete).
