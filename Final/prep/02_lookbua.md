# Lookbua: Risk (slides 5 and 6)

Your deep dive for the Final. Read `00_foundation.md` first: it covers the thesis and the three tests, PRISM, what's
ours, the four verdicts, the three comparisons and the +HK$1.05M headline, the number tags, the words never to say, how
we run the questions, and the questions anyone may get. This file is only your part: areas 4 (the flat and the
warehouse) and 5 (the scenario and the risk register).

Numbers come from the submitted deck (talk 1–13, end card 14, backups 15–33, index 34). Every model number below was
checked against `figures/numbers.json` on 16 Nov. **"Our client"** facts are ones we set ourselves (ILLUSTRATIVE as
facts). Say "our client's", never "the case says".

---

## 1. Your job on stage

**Slide 5: "Check everything they own and earn, not just what a label covers"** (1:00). The judge must leave believing
three things. The limit is tested on the whole household (home, business, savings, Adrian's pay), not only the funds.
Nearly half of a climate downturn's loss lands on the flat and the business, where no fund label looks. And the plan
still holds its downturn limit: 90 futures in 100, against 85.

**Slide 6: "The limit decides before preferences do"** (0:45). The judge must leave believing that the limit, not the
family's taste, picks the flat's route once climate moves prices. Downsizing pays more, until older flats fall about 7%
behind newer ones. Past that, it breaks the limit and is out. The HKMA's research puts that gap within reach by 2037,
so we check it every year and decide by 2046. The green mortgage is refused: it's a label with no money behind it.

**The method, for any client** (so you can explain the step without the Wongs):
1. **List what they own and earn:** the home, a business, the savings, the job.
2. **Trace each route to HK$:** each thing they own, against the brief's eight kinds of risk (transition, physical,
   liability, reputation, liquidity, valuation, data, conduct).
3. **Drop what can't reach them,** and test the ordinary risks too (a market fall, a lost job).
4. **Price what's left against the limit:** cut what the plan can cut; carry the rest, and say so.

Then, for a decision with two routes (slide 6): price both against the limit. A route that breaks it is out, however
much it pays. If both pass, the client's preference decides. Find the **switch point** (where the verdict flips) and
watch it every year.

---

## 2. Your words

Your spoken words, with click marks, are in `Final/prep/Script_Cards.md` (generated from the slides' notes). Rehearse
from there, not from the PowerPoint's presenter view: the notes inside the submitted file are frozen at 16 Nov.

---

## 3. Every number on your slides

**Slide 5.** "The plan" means our recommended plan (the vans, our fees, the scholarship funded now). Each loss is what
the children inherit at Carmen's 89 (median of 10,000 futures, today's HK$), for that part hit alone, against the plan
in a normal future.

| On screen | What it is | Tag | Source | How it was made |
|---|---|---|---|---|
| The flat HK$11.5M · 42% | The flat, as a share of everything they own (HK$27.19M) | Our client; % ESTIMATED | `Final_Plan.md` §2 | 11.5 ÷ 27.19 |
| Her business: her half, HK$5.0M | Carmen's 50% of a company worth HK$10.0M | Our client (ILLUSTRATIVE) | `Final_Plan.md` §2 | Set by us, 9 Nov |
| Savings, deposits, MPF HK$10.5M · 39% | Investable assets | Our client; % ESTIMATED | `Final_Plan.md` §2 | 10.47 ÷ 27.19 |
| Adrian's pay HK$1.2–1.35M a year, to 2036 | Salary HK$1.05M plus a HK$150–300K bonus; retires 2037 | Our client | `model_runs.md` M10 | The model counts the low bonus |
| −HK$1.44M (the flat) | The flat alone takes the downturn | MEASURED | `fin_pstorm_flat_leg` | −10% in 2030, −15% from 2031, plus a 0.15% a year drag |
| −HK$0.81M (her business) | The business alone | MEASURED | `fin_pstorm_biz_leg` | Sale −10%; Carmen draws HK$100K a year less in 2030–31 |
| −HK$2.52M (savings) | The savings alone | MEASURED | `fin_pstorm_port_leg` | Shares 10% then 5% below normal; bonds 5%, 1%; prices +3% |
| 47% lands where no fund label looks | The flat's and business's share of the three | MEASURED | `fin_pstorm_homebiz` | (1.44 + 0.81) ÷ (1.44 + 0.81 + 2.52) |
| −HK$0.54M if his bonus goes too | Adrian's 2030–31 bonus lost, on top of the downturn | MEASURED | `fin_pstorm_bonus_leg` | Against the plan in the downturn |
| 90 futures in 100 (97 without it) | Chance the money lasts to Carmen's 89: downturn / normal | MEASURED | `fin_plan_sodds100`, `fin_plan_odds100` | 10,000 futures, same seed |
| −HK$0.22M; the limit holds (96.8%) | Weather bills: a storm levy plus dearer cover and cooling | MEASURED on ILLUSTRATIVE sizes | `fin_phys_bills_leg`, `_odds`; M12 | HK$50K levy in 2033 + HK$2K a year from 2027 |
| 22 routes (not on screen; cut from the spoken words on 16 Nov, so say it only if asked) | Register cells checked: 3 priced, 19 small or handled | ESTIMATED (our scan) | Backup 16's notes | 3 assets × 8 kinds of risk |

**Slide 6.** On the recommended plan. "The gap" = how far older flats like theirs fall behind newer ones by 2037.

| On screen | What it is | Tag | Source | How it was made |
|---|---|---|---|---|
| Keep it, 97 in 100 | Keep the flat (reverse mortgage in 2037) | MEASURED | `fin_pflipn_rmp_0` (97.0%) | — |
| Downsize to a HK$7M newer flat, 97 in 100 | Sell and buy newer in 2037, no gap | MEASURED; HK$7M ILLUSTRATIVE | `fin_pdown_odds100` (96.7%); `Decision_List.md` H4 | — |
| HK$4.17M more for the children | Downsizing against keeping, no gap | MEASURED | `fin_pdown_more_n` | Median at 89, flat included |
| ≈7% | Downsizing crosses 95, normal future | MEASURED | `fin_pflipn_cross` (7.39%) | Gap 0–15% in 1% steps |
| ≈13% (downturn) | Downsizing crosses 85 in the downturn | MEASURED | `fin_pflip_cross` (12.67%) | The same, inside the 2030–31 scenario |
| keeping the flat holds (90 in 100) | Keep, in the downturn | MEASURED | `fin_plan_sodds100` | — |
| 2%–9% by 2037 (HKMA) | Where a hotter Hong Kong could put the gap | ESTIMATED on SOURCED | `fin_phys_gap_lo/hi` (1.64%, 9.47%); HKMA RM 05/2023 | §4.3 |
| decide by 2046 | The building's 50th year | SOURCED rule, ILLUSTRATIVE date | HKMC rules; built 1996 (ours) | 1996 + 50 |
| green mortgage, ≤HK$1,000 once | The most a green transfer could earn | SOURCED | `Decision_List.md` H2; `research/hook_fact_checks.md` | Hang Seng's rebate, which needs a Gold or Platinum building |

---

## 4. The detail underneath

### 4.1 The scenario, and how it was sized

**The story.** Climate policy waits until 2030, then arrives hard: the NGFS "Delayed Transition" shape (a carbon price
near zero to 2030, about US$100 a tonne by 2035; NGFS Phase V, Nov 2024, read from a chart). The shock plays out like
the NGFS "Sudden Wake-Up Call" and the HKMA's short-term scenario: a Hong Kong recession and "a substantial correction"
in home prices. With no local carbon price, it reaches the family through markets, prices, rates (the peg follows US
policy), a recession and home prices.

**The sizes** (`area4_property_scenario.md` §5.1; ILLUSTRATIVE, each set between published bounds):

| Part | Shock | Bounded by |
|---|---|---|
| Shares | 10% below normal in 2030, 5% in 2031, no catch-up | Floor: CISL 2015 "Two Degrees", the ECB 2022 test. Ceiling: Bank of England 2021 (shares 20–25% lower over 30 years), CISL "No Mitigation". About one standard deviation, two years running |
| Bonds | −5 points in 2030, −1 in 2031 | Yields up about 1 point on about 5 years' duration |
| Prices | +2 points, then +1 (+3% for good) | Between NGFS Delayed Transition (+0.7) and the Sudden Wake-Up Call's Asian spike (about +5) |
| The flat | −10% in 2030, −15% from 2031, plus a 0.15% a year drag | HKMA's second stress test ("substantial correction", **no % published**); the drag is RM 05/2023's low end |
| The business | Sale −10%; Carmen's draw −HK$100K a year in 2030–31 | Recession; a carbon cost on imported paper |
| ESG funds | Same shock as other shares | Nothing measured, so no credit |

**Refused:** NGFS Phase V's GDP damage figures (their damage function, Kotz, Levermann and Wenz 2024, was retracted by
*Nature* on 3 Dec 2025), and the HKMA pilot's "more than 50%" devaluation, which is for "some properties in vulnerable
areas" in 2051–60.

### 4.2 Reading slide 5, and the 22 routes

- **Each part is run alone,** then together. Alone they sum to −HK$4.77M; together the children lose −HK$4.70M
  (HK$13.4M → HK$8.7M), because a future can only run out of money once. Hence "nearly half", not an exact split.
- **The flat's loss barely moves the odds** (0.7 points alone on the base plan, M7). Most of it is a smaller house left
  to the children: the reverse mortgage counts only half the value above HK$8M and is fixed once signed.
- **The savings' loss is an ordinary market fall** any cash-flow planner tests. We say so.
- **Backups 16 and 18 show the plan before our changes** (savings −HK$2.48M, business −HK$0.71M, together −HK$4.60M,
  89.5%). Slide 5 shows the recommended plan. Same scenario, two plans.
- **The grid** (backup 16): the flat, the business and the savings against eight kinds of risk. Three routes priced
  (on the plan before our changes): older flats 10% behind from 2037 (−HK$0.71M); a customer worth 10% of sales leaving
  over carbon data (−HK$1.55M, a sensitivity); the savings in the downturn (−HK$2.48M). Nineteen checked and small or
  already handled: heat, typhoon damage, surge after 2050, repair levies, building notices, energy prices, the plastics
  rules, her "compostable" claims, warehouse flooding, data and conduct gaps.
- **CBAM doesn't reach her.** The EU's carbon border tax covers cement, iron and steel, aluminium, fertilisers,
  electricity and hydrogen, not packaging (Reg. (EU) 2023/956; definitive since 1 Jan 2026).
- **Hong Kong's reporting does, through her customers.** HKEX Appendix C2 makes the climate section, Scope 3 included,
  mandatory from FY2026 for constituents of the Hang Seng Composite LargeCap Index (first reports 2027). That her
  customers include such companies is part of our illustrative business.

### 4.3 The flat: two routes, one switch point

- **Keep it** with an HKMC reverse mortgage in 2037. HKMC counts 100% of the value up to HK$8M and 50% above, then pays
  a fixed sum for life; the loan is non-recourse. Today's table (two borrowers, life, fixed, youngest 60): HK$1,810 a
  month per HK$1M counted (HKMC, Mar 2026), about HK$234K a year on the model's 2037 price (ESTIMATED; the model uses
  HK$230K).
- **Downsize** to a newer HK$7M flat. The cash released is the gap between two prices, so a fall in the old flat alone
  hits it with leverage: at a 10% fall, downsizing releases about 30% less, the reverse mortgage pays about 6% less
  (`area4_property_scenario.md` §3.4). The model includes stamp duty, agents' and legal fees, and moving costs.
- **Where "2%–9%" comes from.** HKMA Research Memorandum 05/2023: prices "could be 4% to 21% lower by around 2050"
  under the Observatory's high scenario, warming acting "alongside ageing properties"; "the older the property, the
  larger the expected adverse impact". Not a forecast. **Our reading** (ESTIMATED; the paper is district-wide): a yearly
  drag of old flats against new of 0.15% to 0.9%, compounded to 2037, gives about 2% to 9%. The switch point sits
  inside: at the low end both routes pass (keep 96.9, downsize 96.3); at the high end downsizing falls to 94.3. It would
  still leave the children more (HK$15.8M against HK$12.7M), but the limit says no.
- **The yearly check** (`Decision_List.md` H1): each year, compare the flat's price per sq ft with a flat about 10 years
  old nearby. Past about 7%, decide that year. Verdict: **do it, but don't call it green.**
- **Why 2046:** the building (1996, our assumption) turns 50. Above 50, HKMC is "case by case" and may want an inspection
  report; under HKMC mortgage insurance a buyer's loan term plus the building's age may not pass 75 years (30 years in
  2037, 26 in 2045). The rule for any client: decide by the building's 50th year. Compulsory sale for redevelopment
  (80%, 70% in designated areas, at 50–59 since 6 Dec 2024) is a weak option for a 1996 high-rise: don't count on it.
- **The green mortgage: don't pay for the label.** No bank publishes a lower green rate (the Consumer Council, Apr 2023:
  "basically no different"); banks need the whole building rated BEAM Plus Gold or Platinum, and theirs isn't; the best
  transfer rebate is HK$1,000 once, and they'd pay the solicitor.

### 4.4 Weather and insurance

- **Flood and surge:** Tai Kok Tsui is not on CEDD's 26 coastal areas at risk to 2050, DSD's blackspots, the Observatory's
  Mangkhut or Hato lists, or the Ragasa warning list. Absent from lists; not a site survey.
- **Heat:** 14 very hot days a year in 1995–2014; 52 in 2024, 53 in 2025 (HKO). It lands on cooling and health, not
  the flat's price.
- **Priced (M12):** a HK$50K storm levy in 2033 (sized to Operation Building Bright 2.0's HK$40K-a-flat subsidy cap) and
  HK$2K a year more for cover and cooling: −HK$0.22M (about half the levy); 96.8 normally, 89.5 in the downturn. A
  cost, not a broken limit.
- **Insurance:** large insured losses (Mangkhut 2018: HK$3.69bn); no evidence of insurers withdrawing flood cover found
  (a search, not proof). The owners' corporation's compulsory policy is liability only; whether it holds property cover
  is unknown.

### 4.5 Adrian, and what the plan cuts or carries

- **His bonus in the downturn:** −HK$0.54M more for the children. On an earlier version of the plan it cost about 1.3
  points in the downturn, still above 85 (M10a); the recommended plan's own figure isn't exported.
- **His job** (backup 19, recommended plan, a sensitivity): lost at the end of 2030 with no work again, the money lasts
  in 44 futures in 100 normally, 21 in the downturn; re-hired at half pay, 79 and 55; with a response agreed now (half
  pay again, HK$200K a year less spending to 2036, Carmen working to 65), 96 and 87. Every odds figure assumes he works
  to 65. Neither parent has long-term disability income cover: the insurable form of this risk.
- **Cuts:** the wrong exit for the flat (slide 6); her customers' data requests met (slides 8–9; the benefit isn't
  quantified). **Carries:** the market, flat and business falls, inside the limit. Nothing hedges climate; in this
  downturn our plan loses about as much as the plan without the test (M8). Its defences are the limits, the reserve and
  the flat's route.

---

## 5. Questions you'll get

Answer first, then the reason, then the source. Stop at 30 seconds. "Show" = the backup slide number to type.

| # | Question | Answer | Show | Strength |
|---|---|---|---|---|
| 1 | Hong Kong has no carbon price. How does "carbon policy" hit this family? | Through markets and a recession, not a local tax. Shares reprice, prices rise 3%, rates follow the US through the peg, and Hong Kong goes into recession, so her business sells for less and home prices correct. The shape is NGFS Delayed Transition; the recession is the HKMA's short-term scenario. | 18 | Strong |
| 2 | Where do your shock sizes come from? | They're ours, labelled ILLUSTRATIVE, each set between published bounds: CISL and the ECB 2022 test below, the Bank of England 2021 exercise and CISL's worst case above. No regulator publishes a Hong Kong home-price shock. It's a test, not a forecast. | 18 | Strong on method |
| 3 | Isn't this a market crash with a green label on it? | Partly, and we say so: the biggest piece, the savings, is an ordinary market fall any planner tests. What a fund label never sees is the other 47%, the flat and the business falling in the same years. The climate-only routes are the old-flat gap and her customers' carbon reporting. | 16, 18 | Moderate |
| 4 | Is the flat's −HK$1.44M climate, or a property correction? | Mostly a correction, set off by the recession in our scenario. The climate part is the slow drift of older buildings in a hotter Hong Kong. That drift changes a decision, so we watch it every year. | 23 | Moderate: say it fast |
| 5 | Why does the flat lose HK$1.44M but the odds barely move? | Most of it is a smaller house left to the children. The parents' income is a reverse mortgage fixed at signing, on only half the value above HK$8M. | 23 | Strong |
| 6 | Your three losses add to HK$4.77M; together it's HK$4.70M. Which? | Both: each run alone, then together. They overlap, because a future can only run out of money once. That's why we say "nearly half". | 18 | Strong |
| 7 | Slide 5 says the savings lose HK$2.52M; your backup says HK$2.48M. | Same downturn, two plans: slide 5 is our recommended plan, backups 16 and 18 the plan before our changes. | 16, 18 | Strong, said calmly |
| 8 | Wouldn't ESG funds fall less in a carbon shock? | Maybe, but it isn't measured for these funds, so they take the same shock as other shares. Claiming protection we can't show would break our own rule. | 21 | Strong |
| 9 | Why one scenario? What about a hot-house world? | The brief asks for a scenario we can explain. We tested a hot-house drift and a sharper crash in research, on an earlier version of the plan, so we won't quote them. The yearly review re-tests the limits. | — | Weak: no current numbers |
| 10 | Older flats falling behind is just ageing. Where's the climate? | The HKMA's own research links them: in a hotter Hong Kong prices could be 4–21% lower by about 2050, more for older property. Reading that as 2–9% by 2037 is our arithmetic, labelled ESTIMATED. | 23 | Moderate: the reading is ours |
| 11 | So you recommend the reverse mortgage, which leaves the children HK$4.17M less? | No. With no gap both pass, and the family chooses; downsizing leaves more. The rule removes it only once older flats fall about 7% behind. The yearly check tells them when. | 25 | Strong |
| 12 | 94.3 against 95: isn't that noise? | The runs share the same 10,000 futures, so the difference is measured precisely. But 95 is the family's rule, not a cliff: crossing it means "decide now", not "disaster". | 25 | Moderate |
| 13 | Why 2046? What if the building is older? | The rule is: decide by the building's 50th year, because then HKMC goes case by case and buyers' loans shorten. 1996 is our assumption; a 1986 building would bring the decision before Adrian retires. | 23 | Strong |
| 14 | Did downsizing include stamp duty and fees? | Yes: stamp duty, agents' and legal fees on both sides, and moving costs are in the model. | — | Strong |
| 15 | Why not a green mortgage? | Their building isn't rated, and banks need the whole building at Gold or Platinum. No bank publishes a lower green rate; the best transfer rebate is HK$1,000 once, against the solicitor's bill. Don't pay for the label. | 23 | Strong |
| 16 | Is Tai Kok Tsui a flood risk? Typhoons, heat? | It's on no official flood or surge list, which isn't a site survey. Weather reaches their money as levies and insurance: priced at −HK$0.22M, and no limit breaks. The exit is where it bites: slide 6. | 23 | Moderate: sizes ILLUSTRATIVE |
| 17 | Will insurers pull out of home cover? | We found no evidence of it. Losses are large, so premiums are likelier to rise; we read them at each renewal. We'd check the owners' corporation holds property cover: the compulsory policy is liability only. | 23 | Moderate |
| 18 | Which climate rules reach this family? | Mostly indirectly. HKEX makes Scope 3 mandatory for its largest listed companies from FY2026, so listed customers ask her for data. CBAM doesn't reach her: it covers steel, aluminium, cement and the like, not packaging. | 17 | Strong |
| 19 | Your odds assume Adrian keeps his job? | Yes, all of them. Lost in 2030 with no response: 44 futures in 100. With a response agreed now: 96. Not a climate risk, but the biggest one, so it's on file; disability cover is the gap to quote for. | 19 | Strong |
| 20 | (Only if a judge read Round One) Delaying the reverse mortgage to 2045 cost about 9 points? | That run kept the 2037 payout. HKMC pays more at an older entry age; at Carmen's 68 the delay costs about 0.4 points (M6). The case against waiting is the building turning 50. | — | Strong; never raise it yourself |

---

## 6. Traps on your topic

| Never say | Say instead |
|---|---|
| "Our plan protects them from the downturn." | "It carries the downturn inside its limit: 90 in 100 against 85. It hedges nothing, and loses about as much as the plan without our test." |
| "The HKMA says the flat falls 15%." | "15% is our test size. The HKMA assumes a substantial correction but publishes no percentage." |
| "The HKMA says older flats fall 2–9% behind." | "The HKMA finds prices 4–21% lower by about 2050, more for older property. 2–9% by 2037 is our arithmetic." |
| "Only a climate check can find this." / "Other planners ignore the home." | "A fund label never looks there; a whole-household check does." |
| "The plan is climate-resilient." | "It holds its limits in the downturn we tested." |
| "Tai Kok Tsui is safe from floods." | "It's on no official flood or surge list. That isn't a site survey." |
| "Over 50% of value could be lost"; any NGFS GDP-damage figure | Don't use them (§4.1). |
| "The carbon data protects HK$1.55M." | "If a customer worth 10% of sales left, the sale would lose HK$1.55M. What the data protects isn't quantified." |
| "Downsizing is the wrong choice." | "Downsizing pays more. It's out only past the switch point." |

---

## 7. What we don't know

| Unknown | How to say it |
|---|---|
| The building's real age and size | "We set 1996. The rule (decide by its 50th year) holds for any age." |
| The owners' corporation's property cover | "Unknown: the first thing we'd ask for." |
| The site's own flood risk; Tai Kok Tsui's ground level | "Not surveyed. Absence from official lists isn't a survey." |
| A real repair levy; an age discount per year | "No published figure. We sized the levy to the subsidy cap, and we watch the gap instead of forecasting it." |
| The HKMA's property shock | "Not published. Ours is a test size." |
| HKMC's payouts in 2037 or 2045 | "They depend on future rates; today's table is our basis." |
| The recommended plan's odds with Adrian's bonus lost; a hot-house variant on this plan | "Not re-run on this plan. On an earlier version the bonus cost about a point, still above 85." |
| Warehouse flood risk; Adrian's employer's climate exposure | "Checked, not priced." / "A missing price: we'd ask him." |
| NGFS Phase VI | "We sized against Phase V (Nov 2024)." Check before Saturday whether Phase VI is out. |

---

## 8. Self-test

<details><summary>1. What share of the downturn's loss lands on the flat and business, and why "nearly half"?</summary>
47% of the three losses run one at a time. Together they overlap, so it isn't an exact split of the total.
</details>

<details><summary>2. Futures in 100 the money lasts, normally and in the downturn; the limits?</summary>
97 normally (limit 95); 90 in the downturn (limit 85).
</details>

<details><summary>3. At what gap does downsizing break each limit?</summary>
About 7% against 95 normally; about 13% against 85 in the downturn. The normal limit binds first.
</details>

<details><summary>4. Why does the gap hurt downsizing far more than the reverse mortgage?</summary>
HKMC counts only half the value above HK$8M and fixes the income at signing. Downsizing's cash is the gap between two
prices, so the old flat's fall alone hits it with leverage.
</details>

<details><summary>5. Where does "2%–9% by 2037" come from, and whose number is it?</summary>
HKMA RM 05/2023 (prices 4–21% lower by about 2050, more for older property). Reading it as a 0.15–0.9% yearly drag of
old flats against new, compounded to 2037, is ours (ESTIMATED).
</details>

<details><summary>6. Why 2046, and the rule for any client?</summary>
The building (1996, ours) turns 50; then HKMC is case by case and buyers' loans shorten. Decide by the 50th year.
</details>

<details><summary>7. Why doesn't CBAM reach Carmen, and what does?</summary>
CBAM covers cement, steel, aluminium, fertilisers, electricity and hydrogen, not packaging. HKEX Appendix C2 reaches
her through listed customers (Scope 3 mandatory for LargeCap issuers from FY2026).
</details>

<details><summary>8. What does the plan cut, and what does it carry?</summary>
Cuts routes: the wrong exit, customers' data requests met. Carries the market, flat and business falls inside the
limit; hedges nothing.
</details>

<details><summary>9. The green mortgage: verdict and number?</summary>
Don't pay for the label: the building isn't rated; at most HK$1,000 once, against legal costs; no lower rate published.
</details>

<details><summary>10. Adrian's job lost at the end of 2030, no response: futures in 100? With the agreed response?</summary>
44 normally, 21 in the downturn; with the response, 96 and 87.
</details>
