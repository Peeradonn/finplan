# Pete: the deep dive (slides 1–4 and 13; areas 1 and 6; the Q&A lead)

Read `00_foundation.md` first. This file goes one level down on the same ideas, because the panel will aim its first
and hardest questions at the framework, the headline and the family's limits, and you take those. Slide numbers are the
submitted deck's: talk 1–13, end card 14, backups 15–33, index 34. Numbers come from `figures/numbers.json` (the
`fin_*` keys, written by `Final/final_model.py`), `Final/model_runs.md` and `Final/Decision_List.md`. Where this file
and those disagree, they win.

## 1. Your job on stage

| Slide | What a judge must believe after it | The method, for any client |
|---|---|---|
| 1 · What makes a plan sustainable? | A share of ESG products is a target, not a test. We have a test with three conditions, and it changed real advice for one family, with a number on it. | Ask the question before the products: does the plan last when climate hits, what does the money change, what can values afford? |
| 2 · PRISM | The five steps are ordinary planning steps. What's new is what goes inside them: the limit on everything they own, only changes we can show, values priced in HK$, every verdict with what flips it. | Run the steps in order. Each checks one or more of the three conditions. |
| 3 · Own money, own limits; shared money follows the more prudent | Profiling each decision-maker alone turns a family argument into a rule. | Ask each person alone (need, would risk, value) before any product. Write the disagreement rules into the policy. |
| 4 · Set the limit first; values spend only the room above it | Values have a budget, and the limit sets its size before anyone picks a product. The scholarship is paid for knowingly, from that budget. | Set how sure the money must be. Measure the room above it in HK$. Let values spend only that, once, both parents agreeing. |
| 13 · The claim, filled in | Every decision lands in one of four corners. The label never decides. The outcome is a number with a source. | Price every decision for the children and for the world against its plain alternative; the limit first, then the corner. |

## 2. Your words

Your spoken words, with click marks, are in [`Script_Cards.md`](Script_Cards.md) (generated from the slides' notes).
Don't learn them from this file.

## 3. Every number on your slides

MEASURED = our model (10,000 futures, the median, today's HK$, the flat included). Keys in `figures/numbers.json`.

| On screen | What it is, in plain words | Tag | Source | How it was made |
|---|---|---|---|---|
| **+HK$1.05M** (slides 1, 13) | What the children inherit at Carmen's 89 (2066), median future, today's money: our plan minus the reasonable planner's plan | MEASURED | `fin_fair_gain`; `model_runs.md` M9b, fairest row | Ours HK$13.36M (`fin_plan_leg89x`) against HK$12.32M (`fin_fair_lab_leg89`) |
| **up to 134 t** (1, 13) | CO2e a year the business could cut, if verified and delivered | ESTIMATED, on an ILLUSTRATIVE business | `Decision_List.md` B1, B4; `model_runs.md`, "What is not in these runs" | Vans 19.3 + LED 4.1 + air-con 2.8 + recycled PET 108.1, published factors (DESNZ). Not a model output |
| **HK$0.74M** (1, 4, 13) | The family's capital: the scholarship fund, the same awards for life | ESTIMATED | `fin_plan_gift_hk`; `Decision_List.md` §2, G1 | HK$30K a year in today's money for 39 years at 2.5% real = HK$742K; two halves of ≈HK$371K, 2027 and 2028; ≈HK$0.62M after ≈HK$126K tax relief |
| **HK$1.91M** (1, 13) | The business's capital: 4 electric vans, chargers, LED, office air-con | ESTIMATED | `Decision_List.md` §2, B1 | HK$1.5M five-year loan (5.5%, ILLUSTRATIVE) + HK$0.41M company cash |
| **≈HK$0.27M** working capital (13 only) | Early payment to the PET supplier, for its data and terms | ILLUSTRATIVE | `Decision_List.md` §2, B4 | Not on slide 1's capital line: know it's there |
| **10,000 futures** (1) | Model runs, same seed, so rows differ only by the change named | — | `model/run_model.py` (n = 10,000, seed 42) | Round One's model, unchanged; the Final's runs import it |
| **0.5% / 3% a year** (3, 4) | How far Adrian's / Carmen's funds may stray from the market (tracking error) | ILLUSTRATIVE (our client definition) | Backups 27, 33; `Decision_List.md` P6 | Set in the profile; it sizes Adrian's climate fund at 24% (0.5% ÷ 2.09%, Win's slide 11) |
| **95 in 100; 85 in a downturn** (4) | The limit: the money lasts to Carmen's 89 in at least 95 futures normally, 85 in the 2030–31 downturn | ILLUSTRATIVE (ours, Pete, 10 Nov) | `model_runs.md` M9c | A choice, written into the policy annex (backup 27) |
| **2037, 2039** (4) | Adrian retires (at 65), Carmen (at 62) | Client definition | `model/run_model.py` | — |
| **HK$1.7M** (4, 12) | The room: the most they could give today, funded now, before either limit breaks, starting from plain choices | MEASURED | `fin_room_gift_plain` (1.74); M11 | Plain funds, no giving, no vans: 97.7% normally, 92.2% in the downturn. Gifts in pieces within both parents' 35% caps, with relief. The normal limit binds first |
| **HK$0.28M** (4) | Carmen's ESG funds' use of the room, in today's giving | MEASURED | `fin_room_esg_hk` | Room with plain funds (1.74) minus room with her ESG funds (1.46) |
| **≈HK$0.72M still free** (4, 12) | What's left after her funds and the scholarship | ESTIMATED | `fin_room_free_hk` | 1.46 − 0.742. "≈" because giving isn't exactly additive |
| **HK$1.48M** (4) | Both causes (education, environment) for life, funded now | Fund size ESTIMATED; its odds MEASURED | `fin_room_both39_hk`; `fin_room_both39_odds` 94.9%; M11 | 2 × HK$742K. 94.9% is at the limit within sampling error |
| **91.6%** (4) | Both causes pledged from yearly cash flow instead: odds normally (79.8% in the downturn) | MEASURED | `fin_room_pledge2_odds`, `_sodds`; M11 | Breaks both limits |
| **HK$0.94M at 5.5%; HK$0.15M at 5%** (4) | The room if equities return less than the model's 6% | MEASURED, a sensitivity | `fin_room_ret55`, `fin_room_ret50`; backup 26 | Only the equity return changed; no room at all below ≈4.9% (`fin_room_zero_ret`) |
| **≈7%** (13) | The gap behind newer flats where downsizing breaks the limit of 95 | MEASURED | `fin_pflipn_cross` (7.39) | Lookbua's slide 6; 13% in the downturn (`fin_pflip_cross`) |
| **+HK$0.51M · 26 t** (13) | Vans, LED, air-con against new diesel vans | HK$ MEASURED; t ESTIMATED | `fin_dot_vans_n`; M2 | Through the sale price, diesel HK$31/L. Not the same as the headline's +HK$0.54M (§4) |
| **≈HK$0 · 108 t** (13) | Recycled plastic at today's resin price | Price SOURCED (S&P Platts, 7 Oct 2026); t ESTIMATED | `Decision_List.md` B4 | Resin, not finished packaging: a supplier quote is still needed |
| **−HK$0.09M** (13) | Customer carbon data: its cost through the sale price; benefit not quantified | MEASURED (cost) | `fin_dot_data_n` | HK$54K a year (`model_runs.md` M8 note) |
| **−HK$1.32M · HK$0.74M** (13) | Scholarship: what the children inherit less / what is given now | MEASURED / ESTIMATED | `fin_val_gift_n`; `fin_plan_gift_hk` | Measured from plain choices with Carmen's funds. On the family's own base it is −HK$1.25M (`fin_plan_gift_n`) |
| **−HK$0.62M** (11, 13) | The green bond fund's and the MPF low-carbon fund's fee gap, for the children. The slides say "her", but half of *each* parent's MPF is in the low-carbon fund, so ≈HK$1.9K a year of it is Adrian's (see `04_win.md`, Q19) | MEASURED | `fin_val_esg_n`; M9c (14.75 → 14.14) | From plain choices. Older figure −HK$0.57M is the same fee gap on the family's base (M4) |
| **26.6%** (13) | The family's share in ESG funds: an output | ESTIMATED | `Decision_List.md` P6 | Win's slide 11 |
| **97 in 100, 90 in a downturn** (13, spoken) | Our plan's odds | MEASURED | `fin_plan_odds` 97.0%, `fin_plan_sodds` 90.0% | The reasonable planner's plan: 95 and 86 (`fin_fair_lab100`, `_s100`) |

## 4. The detail underneath

**The model.** Round One's Monte Carlo (`model/run_model.py`), unchanged; the Final's runs import it. Main assumptions
(`document/manuscript.md`'s table): equities 6% a year, 17% volatility; bonds 4%; inflation 2.5%; spending HK$780K a
year in today's money, 70% after Adrian's death; medical premiums on top, reviewed at Adrian's 75 (the base
`switch_89`); a reverse mortgage of HK$230K a year from 2037; Carmen's half of the business counted at 60%, sold for
HK$3.0M in 2039. Spending is fixed (no guardrails), so every cost or saving shows up in what the children inherit: the
portfolio at Carmen's 89 plus home equity, median, today's money. **Every odds figure assumes Adrian works to 65.**

**Sampling error** (our arithmetic, ESTIMATED): at 10,000 futures and odds near 95%, one standard error is about
0.2 points. So 97.0 against 95.1 is a real gap. 94.9 against 95 is not, and the slide 4 notes say so. Because every
run uses the same seed, the *difference* between two runs is more precise than either run alone.

**Why HK$, not points.** Near 97 the odds barely move: the room in points is about 3 (98 with plain choices, limit 95;
`fin_room_plain`, `fin_room_pts`), and the family uses about 1. That's too blunt to price a decision. So the limit stays a
probability (the goals-based planners' floor) and every price tag is in HK$ of what the children inherit.

**How the room is measured** (M9c, M11). Start from plain choices: plain funds, no giving, no vans. That plan holds
97.7% normally and 92.2% in the downturn. The room is the most giving they could fund now before either limit breaks:
HK$1.7M. The normal limit (95) binds first, because 97.7 − 95 = 2.7 points is smaller than 92.2 − 85 = 7.2. Carmen's
ESG funds use HK$0.28M of it, the scholarship HK$0.74M, ≈HK$0.72M is free. Pledging both causes from cash flow
breaks both limits (91.6%; 79.8%). **The room moves with markets:** HK$0.94M if equities return 5.5%, HK$0.15M at 5%,
none below ≈4.9%. Our plan holds 95 down to equities at ≈5.3% a year and 85 in the downturn down to ≈5.2%
(`fin_ret_hold_n`, `_s`; backup 26). This is a sensitivity, not a forecast, and it's why the room is measured every year.

**The scholarship** (`Decision_List.md` G1; `research/area1_6_framework.md` §7). A named fund at an existing tax-exempt
charity under s.88, paying the same awards the family pledged (HK$30K a year in today's money) for 39 years. Fund
≈HK$742K at 2.5% real, given in two halves, 2027 and 2028, so each half (≈HK$371K) sits under Adrian's cap: deductions
can't exceed 35% of assessable income, ≈HK$420K on ≈HK$1.2M (IRD *Tax Guide for Charitable Institutions*, June 2023,
¶54). The gift is deducted at his 17% top rate: ≈HK$126K of relief. Relief only exists while they earn: after
retirement, gifts get none. Only gifts of money count: sell units first, then give cash. **Chloe is never a
beneficiary:** the IRD says beneficiaries "must not be defined by a personal connection like family relationship"
(¶11). She has a voice in the criteria. **The environment cause waits** for the yearly review (G2): both causes for
life now sit at the limit (94.9%), so it is funded once the room covers it with margin. Her business's cuts are not
a substitute, and we don't say they are. **Open:** a gate on the scholarship's second half (pay 2028 only if the 2027
review still shows room) is your call, not yet made.

**Funding vs pledging.** With labelled funds as cheap as ours, a lifelong pledge of *one* cause stays above both
limits (95.1%; 86.2%; M9b). So never argue "the pledge breaks the limit": that's true only for both causes (slide 4).
The case for funding is question 11 in §5. A tax-aware planner might fund it too, and we say so.

**The headline's construction** (`final_model.py` `export_final`; M9b's fairest row). The reasonable planner's plan
is Round One's choices with a labelled ESG core at 0.20% (as cheap as ours) and the lifelong HK$30K-a-year pledge. Add
our changes in order, so the parts sum: the vans **+HK$0.54M** (`fin_fair_vans`), funding the gift instead of pledging
it **+HK$0.39M** (`fin_fair_gift`), the rest of the fee gap **+HK$0.12M** (`fin_fair_fees`, mostly Adrian's plain
bonds instead of a green bond fund). Total **+HK$1.05M**; **+HK$1.03M** in the downturn (`fin_fair_gain_s`). Odds 97
and 90 against 95 and 86. **Only the vans are the framework's**, and they rest on an ILLUSTRATIVE business reaching
the family through the sale price. Against a planner who also buys the vans and funds the gift, the money effect is
about zero (our reading of the parts, not a separate run; `Final_Plan.md` §4.4). Then the case rests on what only the
test adds: the cuts at no cost (recycled plastic at parity, the climate index fund at its plain twin's fee), the
flat's route set by the limit with its switch point, the customer route guarded, and what may be claimed.

**Profiles and decision rights** (slide 3; backup 33; `area1_6_framework.md` §3). The brief's seven dimensions,
grouped as need, would risk, value. Taken following ESMA's suitability
guidelines (ESMA35-43-3172, 23 Sep 2022): ¶81, the financial profile first, sustainability preferences "in a second
step"; ¶65–70, for a group client "adopt the most prudent approach", an "average profile … would unlikely be
compliant"; ¶84, a mismatch is recorded. These are EU guidelines, not Hong Kong law: we borrow the order as good
practice. Hong Kong's HKMA says asking about sustainability preferences "is not a mandatory requirement" (FAQ, 29 Nov
2023; `industry_practice.md` §6; re-check the wording before quoting). Ryan decides his own money only; his values are
"to ask". Chloe decides nothing yet. **The profiles are our client definition, not interviews**: say "our client", never
"Carmen told us".

**"Isn't this standard?"** Partly, and we say so first. Goals-based planning puts a floor before risk-taking: Chhabra,
"Beyond Markowitz", *Journal of Wealth Management* 7 (2005), pp. 8–34; Das, Markowitz, Scheid and Statman, "Portfolio
Optimization with Mental Accounts", *JFQA* 45(2) (2010), pp. 311–334. Our room is their aspirational surplus, applied to
values. Checked bibliographically only: quote the idea, not a page. One search (13 Nov) found nobody pricing ESG
preferences as surplus above a goal floor; that is not proof, so never say "first". PRISM's two directions are double
materiality, the EU's principle for company reporting, applied to a family's balance sheet: slide 2's footer says so.

**Governance** (area 6). The policy annex (backup 27) has ten clauses both parents sign: the limit first, the room, no
share target, cost (shared money at most its plain twin + 0.05%), tracking (0.5% / 3%), disagreement, claims
("aligned", never "impact"), restatement (old, new, why), a yearly review plus one at any switch point. Structure: CFA
Institute, *Elements of an Investment Policy Statement for Individual Investors* (May 2010) §3e. Thresholds
ILLUSTRATIVE. **Licensing** (`new_Risk_Regulation_Greenwashing.md` §7, our opinion): the planner coordinates; funds go
through SFC-licensed or HKMA-registered intermediaries, insurance through IA licensees.

## 5. Questions you'll get

Answer first, then the reason, then the source. Stop. "Show" is the backup to type.

1. **"What's your recommendation, in one line?"** Seven changes, each priced; the main ones: the business buys electric
   vans on a plain loan and switches to recycled plastic at today's price. The savings go into a climate index fund at the plain fund's
   fee. The family keeps the flat with a yearly price check, and funds the scholarship now. Capital HK$0.74M the
   family's, HK$1.91M the business's; +HK$1.05M for the children; up to 134 t a year. *Show 13.* **Strong.**
2. **"Where's the innovation? Isn't this what every good planner does?"** The steps, yes: slide 2 says so, and the
   tools are known (goals-based planning, core and excess capital, double materiality). We change three things inside
   them: values spend only the room above the limit, priced in HK$; the limit covers the home and business; every
   decision, vans to scholarship, on one measure with the number that flips it. And it found what a fund screen can't:
   almost half the downturn's loss outside the funds, the biggest carbon cut in purchases at about zero cost, labels
   that didn't earn their cost, the flat's route. *Show 25, 28.* **Moderate:** it needs slides 4 and 13 behind it.
   Lead with the findings, not with PRISM: the acronym is how we order the steps, not the claim.
3. **"Your reasonable planner's plan is a strawman: it ignores the business."** It's our defined comparison, not a
   claim about advisers. Fair point on the business: against a planner who also buys the vans and funds the gift, the
   money effect is about zero. What's left is what only the test adds: free tonnes, the flat's switch point, what may
   be claimed. *Show 15.* **Moderate:** say it first, in 20 seconds.
4. **"Take the HK$1.05M apart."** Vans +HK$0.54M: the framework's, on an illustrative business. Funding the gift
   +HK$0.39M: good planning a tax-aware planner might do too. Fees +HK$0.12M: ordinary planning. In the downturn,
   +HK$1.03M. We say which part is green. *Show 15.* **Strong**, because we split it ourselves.
5. **"Why 95 and 85?"** They're the family's limits as we set them, ILLUSTRATIVE, written into the annex. The rules
   don't depend on the level: each verdict that leans on a limit shows where it flips. A family can lower its limit,
   explicitly, both parents signing. *Show 25, 27.* **Moderate.**
6. **"97 against 95: is that even significant?"** Yes. At 10,000 futures one standard error is about 0.2 points, and
   every run uses the same seed. Where it isn't, we say so: both causes funded at 94.9% is at the limit within error,
   which is why the second cause waits. *Show 26.* **Strong.**
7. **"What if markets return less than 6%?"** The plan holds 95 down to equities at ≈5.3% a year, 85 in the downturn
   to ≈5.2%. The room shrinks fast: HK$0.94M at 5.5%, HK$0.15M at 5%, gone below 4.9%. That's why values spend only
   what's measured each year. *Show 26.* **Moderate:** the margin is thin, and we say so.
8. **"My values aren't discretionary. Why must Carmen wait for Adrian's limit?"** Her values aren't waiting: the family
   spends HK$1.02M of the room on them now, her funds and the scholarship. The limit protects shared money: retirement and essentials.
   If the family values a cause above that safety, they can lower the limit, explicitly, both signing. We price the
   choice; we don't make it. *Show 27.* **Moderate:** the room is the claim a competent person could argue with.
9. **"You fund the scholarship but not the environment cause. Did you drop it?"** No. Both for life would sit at the
    limit (94.9%), so the second is funded at a yearly review once the room covers it with margin. Her business's cuts
    are not a substitute, and we don't say they are. *Show 4.* **Moderate.**
10. **"HK$0.74M on slide 4, −HK$1.32M on slide 13. Which?"** Both. HK$0.74M is the fund given now. −HK$1.32M is what
    the children inherit less at Carmen's 89, in today's money, because money given away stops growing. Slide 13
    labels its axis. **Strong.**
11. **"Why lock up HK$0.74M now when HK$30K a year is cheaper?"** The pledge isn't cheaper: like for like, funding is
    worth +HK$0.39M. It holds the limit to a lower return (5.3% against 5.7%), uses the 17% relief while Adrian earns,
    and the charity holds the money, so the promise survives a bad year. *Show 26.* **Strong.**
12. **"Is the scholarship additional?"** Only if the awards wouldn't exist otherwise. The gift agreement with the
    charity says so, and the charity holds the money. We count students funded, not tonnes, and claim nothing more.
    **Moderate:** the charity and its terms aren't chosen yet.
13. **"Can Chloe benefit? Can the family pick the students?"** No to both. The IRD says beneficiaries can't be defined
    by family relationship; a gift that buys a material advantage isn't a donation. The family can advise on criteria,
    like academic merit; the charity awards. **Strong.**
14. **"Did you interview the family? Are those quotes?"** No. They're our client, defined by us, as the brief asks
    ("define the client's circumstances and every figure yourself"). The profiles are our characterisation, ILLUSTRATIVE.
    In practice, step 1 is that interview, each person alone. *Show 33.* **Strong**, if said plainly.
15. **"Why cite EU guidelines in Hong Kong?"** Hong Kong doesn't require sustainability preferences to be asked: the
    HKMA calls it "not a mandatory requirement". We borrowed ESMA's order, financial profile first, values second, and
    its rule that a joint decision follows the more prudent person, as good practice. Suitability per person follows
    the SFC's code. **Moderate:** re-read the HKMA wording before quoting it.
16. **"Isn't PRISM just double materiality, or goals-based planning, renamed?"** Built on both, on purpose. Double
    materiality is a company-reporting principle; we apply it to a family's home, business and savings. The room is
    goals-based planning's surplus, applied to values. What's ours is the three conditions together, with decision
    rules. *Show 28.* **Moderate.**
17. **"Is your plan climate-resilient?"** We don't claim that. Nothing in it hedges climate. In the downturn it loses
    about as much as the reasonable planner's plan. Its defences are the limits, the reserve and the flat's route. It
    holds 90 in 100 in that downturn, above 85. *Show 18.* **Strong**, because it's honest.
18. **"Your 134 tonnes are on an illustrative business. Isn't that greenwashing your own plan?"** It's why we say "up
    to" and "if delivered", and tag it ESTIMATED. 108 t rests on recycled plastic at one day's resin price: a supplier
    quote decides it. Nothing is claimed until measured from 2027. **Moderate.** Hand detail to Fahtai.
19. **"What if Adrian loses his job?"** Every odds figure assumes he works to 65, and slide 12 says so. If he lost it at
    58 and never worked again, the plan falls to 44 in 100, 21 in the downturn. A response agreed in advance restores
    both: half his pay again, HK$200K a year less spending, Carmen working to 65 (96 and 87). Not a climate risk; the
    largest one. *Show 19.* **Strong.**
20. **"Is this practical? How long does it take?"** A few more fact-find inputs, one scenario across everything, one page
    a year. The accountant supplies the ledger; licensed parties place the products. We haven't timed it; timing it on
    real clients is its first test. *Show 28.* **Moderate:** no hours measured.
21. **"Are you licensed? Who's liable?"** The planner coordinates. Funds go through SFC-licensed or HKMA-registered
    intermediaries, insurance through IA licensees, and the bank prices the loan. Fees and conflicts are disclosed, and
    each person gets their own risk profile. The non-authorised fund needs a compliance check before we implement.
    *Show 32.* **Moderate:** practise the wording.
22. **"Slide 1 says three green products refused. I count more."** The close names three refused outright: the green
    mortgage, the green deposit and a sustainability-linked loan. The clean-energy fund also fails Adrian's limit, and
    the van loan's green label we'd take only if free. **Moderate:** the count differs by slide.
23. **"What would you not do?"** Pay for a label that changes nothing: a green mortgage worth at most HK$1,000 once; a
    green-loan review that costs what the discount saves; a sustainability-linked loan at her size; claiming impact for
    listed shares. We don't refuse Carmen's values. We refuse the label. **Strong.**

## 6. Traps on your topic

| Never say | Say instead |
|---|---|
| "Advisers usually / never …" | "Our plan's comparison is the advice we'd give without the test." |
| "The first framework to …" | "We didn't find it published; we show it worked, priced." |
| "The case says …" / "Carmen told us …" | "Our client …" / "We defined …" |
| "October", "our Round One plan", "the label approach" | "Without the test" or "the reasonable planner's plan" |
| "The labelled plan falls below the floor" | It doesn't: 95 and 86, above both limits. "It's poorer, and claims tonnes it doesn't cut." |
| "HK$2.4M" | Never. That was against an unverified fee. |
| "The children *will* get HK$1.05M more" | "In the model's middle future, in today's money, about HK$1.05M more." |
| "Our plan is climate-resilient" / "protects them from climate" | "Nothing in it hedges climate; the limits, the reserve and the flat's route are its defences." |
| "Nothing hedges climate", said as a confession | Say it as the finding: "the green products don't protect them; the limits do." |
| "Safety first" | "A limit: how sure the money must be." |
| "Carmen's money cuts 134 t" | "Her business could cut up to 134 t", co-owned with a partner who must agree |
| "A registered charity" | "A tax-exempt charity under s.88" |
| "Held nothing" (of the fund) | "Reported zero assets at every filing for two years." Never name the manager aloud |
| "We recover the downturn's loss" | We don't; we hold the limit through it. |

## 7. What we don't know

- **Whether the zero-asset fund is still on the SFC's ESG list.** Last checked on the list 6 Nov; its filings read to
  14 Nov. Re-check Fri 20 Nov. If it's gone: "it was on the list until …".
- **The limits (95, 85) and the 6% equity return** are assumptions: the limits ours, the return Round One's
  (long-run history). "Each verdict shows where it flips."
- **The profiles** are our characterisation. "Step 1 is that conversation, each person alone."
- **The charity and its terms** (minimum gift, admin fee) aren't chosen. "A named fund at an existing s.88 charity, terms
  to agree."
- **The 2028 gate** on the scholarship's second half: not decided. Decide before Saturday or don't mention it.
- **Hours PRISM adds per client:** not measured. "Timing it is the first test in practice."
- **The planner's own fee** is not in the model (not found in our files). If asked: "not modelled; it's the same with or
  without the test."
- **Adrian's employer's climate exposure:** a missing price. "We'd ask Adrian."
- **"The EU requires double materiality of companies"** (slide 2's footer): our files hold no source for it, and the EU's
  rules for which companies report have been changing. If pushed: "the EU's reporting standards for large companies
  are built on it; we cite the principle, not the scope." UNVERIFIED in our files.
- **The HKMA's "not a mandatory requirement"**: flagged CHECK in `Final_Plan.md` §9. Re-read before quoting.
- **Is a one-to-one recommendation of a non-authorised fund an offer "to the public"?** UNVERIFIED (Win's area).

## 8. Self-test

<details><summary>1. The headline's three parts, and which is the framework's?</summary>
Vans +HK$0.54M (the framework's, on an illustrative business); funding the gift +HK$0.39M; fees +HK$0.12M (ordinary
planning). Total +HK$1.05M; +HK$1.03M in the downturn.</details>

<details><summary>2. The reasonable planner's plan's odds, and ours?</summary>
95 and 86 (above both limits); ours 97 and 90.</details>

<details><summary>3. How is the room measured, and which limit binds?</summary>
From plain choices (plain funds, no giving, no vans: 97.7%, 92.2%), the most giving funded now before either limit
breaks: HK$1.7M. The normal limit binds (2.7 points above 95, against 7.2 above 85).</details>

<details><summary>4. The room at 5.5% and 5% equity returns; where it's gone?</summary>
HK$0.94M; HK$0.15M; gone below ≈4.9%.</details>

<details><summary>5. Why fund the scholarship if one pledge passes the limits?</summary>
Like for like it's worth +HK$0.39M; holds to 5.3% returns against 5.7%; uses the relief while Adrian earns; the charity
holds the money, so the promise survives a bad year.</details>

<details><summary>6. HK$0.74M or −HK$1.32M?</summary>
The fund given now; what the children inherit less at 89 because it no longer grows.</details>

<details><summary>7. +HK$0.51M or +HK$0.54M for the vans?</summary>
Alone against diesel on the family's base; their step inside the headline's sequence.</details>

<details><summary>8. What do ESMA ¶81 and ¶65–70 say?</summary>
Financial profile first, sustainability preferences in a second step; a group client follows the most prudent
approach, not an average.</details>

<details><summary>9. Why can't Chloe benefit from the scholarship?</summary>
IRD: beneficiaries can't be defined by family relationship; a gift that buys a material advantage isn't a donation.</details>

<details><summary>10. If he loses his job at 58 with no response, the odds? And with the agreed response?</summary>
44 and 21 in 100; 96 and 87 (half pay again, HK$200K a year less spending, Carmen to 65).</details>

## Running the Q&A

- **Route in one phrase:** "Fahtai priced the business: Fahtai?" Route the business, the loan, the tonnes and the rules
  that reach her to Fahtai; the flat, the scenario and weather to Lookbua; the funds, the US$0 fund, 26.6%, the
  dashboard and SFC authorisation to Win. Keep the framework, the headline, the limit and the room, the scholarship,
  profiles, governance and licensing.
- **Take it back** when an answer drifts into the headline or into "is this new?", when it reaches 45 seconds, or when
  a teammate says something the traps table forbids: "To add one line: …", then the safe wording.
- **Close a long answer:** "So, in one line: …" Then stop and look at the judge.
- **If nobody knows:** "We didn't test that. Here's how we would: …" Never guess a number.
- **Backups to have in your head:** 15 the headline taken apart · 25 every switch point · 26 if returns fall · 27 the
  annex · 28 PRISM in practice · 19 Adrian's job · 18 the whole household in the downturn · 22 every decision on one
  measure · 33 the seven dimensions · 34 the index. In slide show, type the number and press Enter; go back to 13 after.
