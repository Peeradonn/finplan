# Win: Select for the savings, and Monitor (slides 10, 11, 12)

Read [`00_foundation.md`](00_foundation.md) first (the framework, the verdicts, the comparisons, the tags, the words we
never say, cross-cutting questions). Slide numbers are the **submitted deck's**: talk 1–13, end card 14, backups 15–33,
index 34. Your earlier summaries (`research/win_framework_summary.md`, `portfolio_summary_for_team.md`) and the 12 Nov
specs in `Final_Plan.md` §4.5b are superseded (27.7%, Adrian at 30%, "EDMW SFC-authorised"): don't drill from them.

---

## 1. Your job on stage

| Slide | Title | What a judge must believe after it |
|---|---|---|
| 10 | Pass a product only if its rule binds and it fits its owner's limit | A label is a yes or no. Three checks decide. The fund on the SFC's list with US$0 shows the label let it through and the check stopped it. |
| 11 | The sustainable share is an output of the limits, paid from the room | Nobody chose 26.6%. Two personal limits produced it. What it costs is priced in HK$ and paid from the room above the limit. |
| 12 | Label the plan, not the product | The plan gets its own label: one line per test, each with a number and a trigger. It's read every year against a plain twin. |

**The method, for any client** (explain it without the Wongs):

1. **Check each product:** a published rule binds the outcome its label implies; it's measured every year; it fits its
   owner's limit (cost against its plain twin, tracking, and whether this client may be offered it). Fail one and it
   doesn't count.
2. **Size it by each owner's limit:** weight = tracking-error budget ÷ the product's tracking error against its plain
   twin, capped at the owner's equity. Add across owners: the share is an output.
3. **Price it against its plain twin in HK$,** paid from the room, and name it: footprint or alignment, never impact
   without a measured change.
4. **Label the plan:** one line per test, each with a number and a trigger, read yearly against a plain twin.

**If you have ten seconds:** "A product gets in only if a rule binds it, it's measured every year, and it fits its
owner's limit. Each owner's limit then decides how much. And the plan, not the product, carries the label."

---

## 2. Your words

Your spoken words, with click marks, are in [`Script_Cards.md`](Script_Cards.md), generated from the speaker notes.
Rehearse from that file, not from this one.

---

## 3. Every number on your slides

Every value here was checked against the source named in its row. "Model" means `Final/final_model.py`: 10,000
futures, median, today's HK$, at Carmen's 89 (2066).

**Slide 10**

| On screen | What it is | Tag | Source | How it was made |
|---|---|---|---|---|
| ~~20–25% of their savings in ESG products~~ | What the family asked for | ILLUSTRATIVE (our client definition) | `Final_Plan.md` §2 | The family's wish as we defined it; struck through because the share becomes an output |
| 30% less carbon, −7% a year | The EU Climate Transition Benchmark (CTB) rule the index must follow | SOURCED | Reg. (EU) 2020/1818, Arts 7 and 9 (retained text read 8 Nov; `portfolio_final_round_EN.md` F7) | Carbon intensity ≥30% below the parent universe (Scope 3 phased in); falls ≥7% a year |
| 0.20%, its plain twin's fee | EDMW's total expense ratio, the same as IWDA's | SOURCED | BlackRock factsheets (EDMW Oct 2026; IWDA 30 Sep 2026) | Read off both |
| 90.8 (world index) | Weighted average carbon intensity (WACI) of MSCI World: tonnes CO2e per US$1M of sales | SOURCED | MSCI data, 23 Oct 2026 (90.76, 99.56% covered), read on a fund tracking MSCI World because IWDA's factsheet doesn't print it (`portfolio_summary_for_team.md` §5, F8) | Read |
| 63.4 (−30%) | EDMW's WACI | SOURCED; the % is ESTIMATED | BlackRock/MSCI, Oct 2026 (63.39) | 1 − 63.39 ÷ 90.76 = 30.2% |
| 99.8% covered | Share of EDMW's holdings with carbon data | SOURCED | Same (99.82%) | Read |
| US$0.00 at all 23 filings, Sep 2024 to Sep 2026 | The fund's reported size at every monthly filing | SOURCED | HKEX fund platform (fund ID BUM645), read 4, 9 and 14 Nov 2026 (`area3_portfolio.md` §2A; `boc_fund_call.md`) | Read; 23 records |

The clean-energy fund and the green deposit have no numbers on screen. Their supporting numbers are in §4.4.

**Slide 11**

| On screen | What it is | Tag | Source | How it was made |
|---|---|---|---|---|
| Adrian HK$2.07M · 0.13% a year, ≈HK$2.6K | His portfolio, its weighted fee | ESTIMATED | `area3_portfolio.md` §3 | 24% and 16% at 0.20%, 30% of Treasuries (ladder 20% at 0, IBTA 10% at 0.07%), 25% AGGU at 0.10%, 5% 3053 at 0.31% = 0.128% → HK$2,639 |
| Carmen HK$2.07M · 0.29%, ≈HK$5.9K | Her portfolio, its weighted fee | ESTIMATED | Same | 60% at 0.20%, 5% 3450 at 0.30%, 20% AGGU at 0.10%, 10% green bond fund at 1.14%, 5% 3053 at 0.31% = 0.285% → HK$5,889 |
| Adrian: climate 24%, world 16%, Treasuries 30%, global bonds 25%, 5% | His weights | ILLUSTRATIVE (our allocation); 24% ESTIMATED | Backup 21; `Decision_List.md` P1 | 40% equity, as his profile allows |
| Carmen: climate 60%, 5%, global bonds 20%, green 10%, 5% | Her weights (the two 5% blocks are US Treasuries via 3450 and HKD money market via 3053) | ILLUSTRATIVE; 60% ESTIMATED | Backup 21 | All her equity goes to the climate fund |
| 0.5% a year from the market | Adrian's tracking-error limit | ILLUSTRATIVE | Our client definition (slide 3) | Set in Profile, before any product |
| 2.09% | Tracking error of the **MSCI World CTB index** against MSCI World | SOURCED | MSCI factsheet, 31 Oct 2026 (`Final_Plan.md` §4.5a) | Read. **It's a proxy:** EDMW tracks a different CTB index (ESG Enhanced Focus), whose own tracking error is OPEN |
| 24% | Adrian's cap on the climate fund | ESTIMATED | `Decision_List.md` P1, P6 | 0.5 ÷ 2.09 = 23.9% → 24%; 24% × 2.09 = 0.50% |
| 3% a year, "no wall" | Carmen's limit; it covers all her shares | ILLUSTRATIVE | Slide 3 | 60% × 2.09 = 1.25%, under 3% |
| HK$10.47M | The family's liquid and investment assets | ILLUSTRATIVE (our client definition) | `document/manuscript.md` decision 1 | Includes Ryan's HK$0.68M and policy cash values: the stricter base |
| 0.50 · 1.24 · 0.21 · 0.84 (HK$M) | What counts: Adrian's climate fund, Carmen's, her green bonds, the MPF's low-carbon fund | ESTIMATED | Slide 11; `area3_portfolio.md` §3 | 0.24 × 2.07; 0.60 × 2.07; 0.10 × 2.07; **half of each parent's MPF**, HK$0.835M |
| HK$2.78M ÷ HK$10.47M = 26.6% | The share | ESTIMATED | `Decision_List.md` P6 | 0.497 + 1.242 + 0.207 + 0.835 = 2.781 → 26.56% |
| −HK$0.62M at Carmen's 89 | What the green bond and MPF low-carbon funds' extra fees cost the children | MEASURED (model) | `fin_val_esg_n` | The fee gap against plain twins (HK$5,107 a year: green bond fund HK$2,153 + MPF fund HK$2,954) run through the model. See §4.7 |
| HK$0.28M of the room, in today's giving | The same choice as a share of the room | MEASURED (model) | `fin_room_esg_hk` | Room with plain funds HK$1.74M − room with these funds HK$1.46M |
| 30% less carbon; temperature rise as a band | The climate fund's footprint | SOURCED | As slide 10; ITR >2.0–2.5°C vs the index's >2.5–3.0°C (MSCI, 23 Oct 2026) | Read |
| Duration 1.9–6.0 | Bond durations | SOURCED | iShares factsheets, 30 Sep 2026 | IBTA 1.85; AGGU 6.02 (green bond fund 5.95) |

**Slide 12 (Climate Facts)**

| On screen | What it is | Tag | Source | How it was made |
|---|---|---|---|---|
| 97 in 100 (limit 95) | Odds the money lasts to Carmen's 89, our plan, normal future | MEASURED; the limit ILLUSTRATIVE | `fin_plan_odds` 97.0% | Model |
| 90 in 100 (limit 85) | The same in the 2030–31 downturn | MEASURED; the scenario ILLUSTRATIVE | `fin_plan_sodds` 90.0% | Model |
| Equities under ≈5.3% a year | Below this expected equity return the plan stops holding 95 (the model assumes 6%) | MEASURED (a sensitivity) | `fin_ret_hold_n` (5.27); in the downturn 5.2% | Bisection on the equity return (backup 26) |
| Older flats ≈7% behind | Past it, downsizing breaks 95 | MEASURED | `fin_pflipn_cross` | Lookbua's slide 6 |
| ≈134 t a year, from 2027 | Carbon the business could cut | ESTIMATED, ILLUSTRATIVE business | `Decision_List.md` B1, B4 | Vans 19.3 + LED 4.1 + air-con 2.8 + PET 108.1; potential |
| Recycled plastic above new → 108 t re-priced | Trigger on the biggest cut | SOURCED price | S&P Platts, 7 Oct 2026 | Fahtai's B4 |
| HK$1.7M | Room: the most giving funded today, plain choices, before a limit breaks | MEASURED | `fin_room_gift_plain` (1.74) | Model |
| ≈HK$0.72M | Still free after Carmen's funds and the scholarship | ESTIMATED | `fin_room_free_hk` | HK$1.46M − HK$0.742M fund |
| Mar 2028 · 2046 | Vans before the tax waiver ends; the building turns 50 | SOURCED / ILLUSTRATIVE | Budget 2026–27 para 207; 1996 + 50 (our client definition) | — |

---

## 4. The detail underneath

**4.1 The climate index fund (EDMW).** An Irish UCITS ETF: USD 6.36bn, 1,081 holdings, TER 0.20%, SFDR Article 8
(BlackRock, Oct 2026). About as concentrated as the market (top 10: 27.65% against 26.58%). Against the **plain** world
index it lagged **1.43 points a year** over five years to 31 Oct 2026 (9.13% against 10.56%). The long-run "≈0" (+0.03
a year, 2007–2026) is a different index, MSCI Selection. The CTB rule measures carbon per enterprise value; the slide's
WACI is per US$ of sales. Two measures that agree at about 30%: "measured 30% lower, and a rule that keeps it there."

**4.2 Who may hold it.** EDMW and the plain twins IWDA, IBTA and AGGU are **not SFC-authorised** (SFC product list,
4 Nov 2026). Suitability for each parent (Code of Conduct 5.2); offering an unauthorised fund to the public is
restricted (SFO s.103), except to professional investors (HK$8M portfolio, Cap. 571D), which neither parent probably is
alone. Whether a one-to-one recommendation is "to the public" is **UNVERIFIED**. If they can't be offered it, the
authorised route (Sun Life AM Global Low Carbon Index Fund, Class B, KFS Apr 2026) costs **1.1–2.45%**, ≈HK$16–39K a
year more on HK$1.74M (ESTIMATED). Adrian's 24% goes plain; Carmen pays from the room if she still wants it; the plain
side is re-priced too (backup 32). We wouldn't pool their money to reach HK$8M: it breaks "own money, own limits".

**4.3 The fund on the SFC's list with US$0.** The record: on the SFC's ESG list (authorised 2 May 2024; still listed,
9 Nov); US$0.00 at all 23 HKEX filings, Sep 2024 to Sep 2026 (its S&P 500 sibling holds US$67.27M); no offering
document; its series' audited report (31 Mar 2026) counts seven sub-funds, not this one. The records don't say why.
Our earlier proposal held it as its ESG core: we trusted the list and didn't check its assets. The talk doesn't say so
(the Final is judged on its own, Pete, 17 Nov). Only if a judge raises it: "Yes, we named it then. We trusted the list
and didn't check its assets. That's the mistake this test is built to stop." Never "the label misled us" or "the
SFC's list got it wrong": the list never said it had assets, and checking a product is the adviser's job.

**4.4 The two refusals.**
- **Clean-energy fund:** fails check 3 (the owner's limit). It's a one-sector bet: ICLN fell 61.5% from Jan 2021 to
  Oct 2023, and 2809, which is on the SFC's own ESG list, lost 30.95% in 2023 (`area3_portfolio.md` §2F). That breaks
  Adrian's 0.5%. For Carmen, a small slice might fit her 3% arithmetically, but her income and business already sit in
  that theme. If she insists, it's her money, paid from the room and called alignment.
- **Green deposit:** fails check 1. There's no rule on what the bank finances with the money. The only personal one we
  found (Standard Chartered's Sustainable Savings Account) "will reference qualified green and sustainable activities"
  and paid HKD 0.001% (board rate as at 5 Jun 2026).

**4.5 Integration, alignment, impact** (CFA/GSIA/PRI 2023). *ESG integration*: ESG factors used "to improve
risk-adjusted returns", judged on cost and risk; that's how EDMW passes. *Alignment*: holdings that match values (Carmen's
green bond and MPF funds, from the room). *Impact investing*: intention, a measured effect and the investor's
contribution. Shares bought on the market give a company no new money, so no additional impact is quantified. That's
not zero: price, voting and engagement effects may exist, unmeasured. Also unmeasured, so never credited: implied
temperature rise (a model output, shown as a band, never a target) and HK Taxonomy alignment (voluntary; no HK retail
fund reports it).

**4.6 Greenium against the green bond fund's fee.** Greenium ≈−2bp (Zerbib 2019): HK$41–207 a year on Carmen's
HK$207K. The Allianz Green Bond fund's fee gap over AGGU is **104bp, HK$2,153 a year**, and it has trailed its own
benchmark ≈0.98 points a year since 2017 (ESTIMATED). The fee buys bond-by-bond ICMA checks (≥85% green bonds; SFDR
Article 9). No impact report found, so Carmen keeps it only with one and the entry charge (up to 5%) waived; otherwise it
moves to AGGU and the share falls to ≈24.6% (ESTIMATED). Not the **green premium**: that's the van over diesel (Fahtai).

**4.7 One choice, three units.** HK$5,107 a year in fees (green bond fund HK$2,153 + MPF low-carbon fund HK$2,954
against the cheapest MPF global equity fund), which is −HK$0.62M for the children at Carmen's 89, which is HK$0.28M of
today's giving room. The model turns HK$5,107 into a lower equity return on the whole pool every year to 2066 (our reading of
`final_model.py` `r_eq_for`). That's conservative, since the MPF part stops when the MPF buys annuities in 2037–39.
**Watch:** the slide says "her green bond and MPF funds", but the MPF fund is half of **each** parent's MPF. Adrian's
half (≈HK$525K) carries ≈HK$1.9K of the HK$2,954 (`area3_portfolio.md` §4). See Q19.

**4.8 What the limit doesn't do.** A tracking-error budget limits how far returns stray from the twin, either way; it
doesn't cap underperformance (`area6_measurement_update.md` §1). The −HK$0.62M is fees only. Tracking was a separate
sensitivity: the last five years' lag repeated in 2027–31 cost ≈−HK$0.37M (M4, on the earlier HK$1.86M sleeve; not
re-run). Adrian's share depends on the proxy: 35% at the earlier 1.42%, 24% at 2.09%.

**4.9 Reading against a plain twin.** At signing, fix in writing the same weights with each ESG fund swapped for its
plain twin. Each year show both returns, then split the gap: (a) markets (the twin's return); (b) the ESG tilt
(Brinson–Fachler sector allocation and selection); (c) implementation (fees, tracking); (d) our decisions, plus a
residual. It's our design, not a standard (`area1_6_framework.md` §6b), and hasn't been run on real returns.

**4.10 Five biases (the brief's list), each with its design choice.** Loss aversion: limits set before options. Present
bias: the gift funded now. Ambiguity aversion: the same tags on every option. Social desirability: each parent profiled
alone. Mental accounting: one balance sheet. Sources: `area1_6_framework.md` §5. They guard the advice process, not
defects in the family; no study was run on a family like this one.

---

## 5. Questions you'll get

The backup slide to show is in brackets: type the number and press Enter.

1. **"Is 26.6% inside their 20–25% ask?"** No, it's above it, and that's the point. Their limits produced it: Carmen's 3%
   lets all her shares go to a fund that costs what the plain one does. Capping at 25% would save nothing and would put
   the target back. [21] *Strong.*
2. **"Why doesn't Ryan's money appear?"** His money is his own: the policy covers the parents' portfolios and MPF
   (backup 27, clause 1). His HK$0.68M is still in the HK$10.47M denominator as non-ESG, so it lowers our share. That's
   the stricter base. [27] *Strong.*
3. **"Is your climate fund better than the plain index?"** On carbon, yes: measured 63.4 against 90.8 tonnes per US$1M
   of sales, 30% lower, 99.8% covered (MSCI, Oct 2026), and an EU rule keeps it at least 30% lower. That's a
   footprint, not a change in the world, and we claim none. [21] *Strong.*
4. **"It lagged the plain index by about 1.4 points a year for five years. How does it cost 'nothing'?"** Its fee is
   the same; its return isn't guaranteed to be. The model assumes no premium and no penalty. Adrian's limit caps how
   much he holds, and the last five years repeated would cost the children ≈HK$0.37M (a sensitivity). It's re-checked
   every year. [25] *Moderate:* the long-run evidence of ≈0 is a different index.
5. **"What if EDMW tracks worse than 2.09%?"** Then Adrian's share falls: it's 0.5 ÷ the fund's tracking error. 2.09%
   is the CTB index's, a proxy; EDMW's own figure is open and is measured over rolling three years. The rule sets the
   number. [25] *Moderate.*
6. **"Can you even recommend EDMW to them?"** Not yet confirmed. It isn't SFC-authorised. Each parent needs a
   suitability check, and offering it to the public is restricted. Before we buy, a compliance check with the licensed
   broker. If it fails, the authorised route costs up to 2.45%, Adrian's 24% goes plain, and the verdict flips. [32]
   *Moderate:* the one-to-one point is UNVERIFIED.
7. **"Are you saying that fund is fraudulent?"** No. We say only what the record shows: on the SFC's ESG list, US$0.00
   at all 23 HKEX filings over two years, no offering document. Why, we don't know. The label couldn't tell you; the
   check did. [10] *Strong, if you keep to the record.*
8. **"Wouldn't any careful planner catch that fund?"** Yes, careful due diligence would. Our point isn't that planners
   are careless. It's that a label passes it, so "on the list" can't be the test. The framework writes the check in as a
   rule. [24] *Strong.*
9. **"You say 'don't pay for the label', yet Carmen pays HK$0.62M for green bond and MPF funds. Contradiction?"** No.
    We refuse the label, not her values. She may buy them from the room, priced at HK$0.62M for the children, and we call
    them alignment, never impact. [22] *Strong.*
10. **"−HK$0.62M here, HK$0.28M of the room, HK$5.1K a year. Which is it?"** All three: one choice in three units. Fees a
    year; what the children inherit at Carmen's 89; and what it uses of today's giving room. [22] *Strong.*
11. **"The greenium is about 2bp. Why pay 104bp for a green bond fund?"** We don't pay for the greenium. Carmen pays
    HK$2,153 a year for bond-by-bond checks. It's kept only if the manager gives an impact report and waives the entry
    charge; otherwise it moves to plain bonds. Adrian holds none. [21] *Moderate:* no impact report found yet.
12. **"Clean energy fits Carmen's values. Why refuse it?"** It breaks Adrian's limit: one sector, down 61.5% from 2021 to
    2023 (ICLN), and 31% in 2023 for one on the SFC's own list. For Carmen, her business already ties her income to that
    theme. If she insists, it's her money, from the room, called alignment. [21] *Moderate.*
13. **"So shares change nothing?"** We don't say that. We say no additional impact is quantified for this allocation.
    Price, voting and engagement effects may exist; we haven't measured them, so we don't claim them. [21] *Strong.*
14. **"Does the climate fund protect them in a downturn?"** Unmeasured, so no credit. The carbon underweight points the
    right way, but no published study sizes it for this index. The plan's defence is its limits, not the fund. [18]
    *Strong (honest).*
15. **"Isn't 'Climate Facts' just another label?"** It's a label on the plan, not a product. It must be earned again
    every year against stated limits, each line with a trigger, and a restatement shows the old figure. A product label
    is passed once. [25] *Strong.*
16. **"Who reads this, who signs, and what happens when a trigger fires?"** The adviser prepares it once a year and when
    a switch point is crossed. Adrian and Carmen sign the policy annex, with the adviser. A crossed trigger means they
    decide that year, and if the room falls short both re-sign. [27] *Strong.*
17. **"How do you separate what the plan did from what markets did?"** With a plain twin fixed at signing. Each year we
    show both returns, then split the gap: markets, the ESG tilt, fees and tracking, our decisions. [27] *Moderate:*
    the method is stated but not yet run on real returns.
18. **"Doesn't your fee cost double-count the tracking lag?"** No. The lag compares two funds' returns after their own
    fees, and both charge 0.20%. The fee price is only the green bond and MPF funds. [21] *Strong.*
19. **"Adrian is 'values low'. Why is half his MPF in a low-carbon fund?"** Fair point. Half of each parent's MPF sits
    in it; Adrian's half carries ≈HK$1.9K a year. It's cheaper than the average MPF fund but 0.35 points above the
    cheapest, and it hasn't been tested against his 0.5% limit. It's on the first yearly review; if it fails, his half
    goes plain. [27] *Weak until the team decides (§7).*

---

## 6. Traps on your topic

| Don't say | Say instead |
|---|---|
| "Shares change nothing" / "zero impact" | "No additional impact quantified for this allocation" |
| "EDMW is cleared / approved for them" | "A compliance check with the licensed broker before we buy" |
| "EDMW is SFC-authorised" (an old spec said so) | "An Irish UCITS ETF, not SFC-authorised" |
| "The fund never launched" / "fraud" / "fake" / naming its manager aloud | "On the SFC's ESG list; US$0.00 at every filing for two years" |
| "A careful planner would buy it" | "The label lets it through; the check stops it" |
| "ESG funds protect in a downturn" | "Unmeasured, so we give it no credit" |
| "Our fund is green" / "impact" | "A footprint: 30% less carbon than the market" |
| "Values cost nothing" | "The climate fund costs what its twin does; her green bond and MPF funds cost the children HK$0.62M" |
| "The limit caps how much we can lose" | "The limit caps how far it can stray, either way" |
| "The worst five years cost HK$27K a year" | "If the last five years repeat" (nobody has measured the worst window) |
| "The 25% target" / "we aimed for 26.6%" | "Nobody set it: the limits did" |
| "Planners usually / never…" | Say what we do; never claim what others do |

---

## 7. What we don't know

- **EDMW's own tracking error against MSCI World.** "We use the CTB index's 2.09% as a proxy; the fund's own figure is
  measured in the first year."
- **Whether EDMW may be offered to each parent** (the one-to-one point; whether MPF counts toward HK$8M; whether Ireland
  and London are on the SFC's specified-jurisdiction list). "Checked with the licensed broker before we buy."
- **Why the listed fund reports US$0.** "The records show zero; they don't say why."
- **The green bond fund's impact report and EU Taxonomy share.** "We haven't found one; without it, it moves to plain
  bonds."
- **The MPF low-carbon fund's measured carbon and tracking** against a plain MPF fund, and **which funds the Wongs'
  schemes offer.** The cheapest MPF global equity fund may not be in their scheme (MPF choices sit inside a scheme; our
  inference). "Checked at the first yearly review."
- **Adrian's MPF half and his limit** (§5, Q19). **Before Saturday, Pete and Win should decide** whether to answer as
  in Q19 or to say his half is plain. The slide says "her green bond and MPF funds", and the −HK$0.62M includes his half.
- **ESG funds under climate stress.** "No published study sizes it; we give no credit."
- **The SFC list count today.** "179 in the SFC's 23 Oct file." The planned re-count wasn't recorded.
- **Whether the five-year gap is the worst five years.** "Nobody has measured every window."

---

## 8. Self-test

<details><summary>1. Name the three product checks.</summary>
A binding, published rule on the outcome; measured and reported every year; within the owner's limit (cost, tracking,
and whether this client may be offered it).</details>

<details><summary>2. Where does 24% come from?</summary>
Adrian's 0.5% a year ÷ 2.09% (the CTB index's tracking error against MSCI World, a proxy) = 23.9%.</details>

<details><summary>3. Build 26.6%.</summary>
0.50 (Adrian's climate fund) + 1.24 (Carmen's) + 0.21 (her green bonds) + 0.84 (the MPF's low-carbon fund, half of each
MPF) = HK$2.78M ÷ HK$10.47M.</details>

<details><summary>4. What is −HK$0.62M, and what is HK$0.28M?</summary>
The same choice, the green bond and MPF funds' fee gap of HK$5,107 a year. −HK$0.62M is what the children inherit at
Carmen's 89; HK$0.28M is what it uses of today's giving room.</details>

<details><summary>5. Why does the climate fund sit in "Do it, but don't call it green"?</summary>
It costs what its plain twin costs (0.20%), so ≈nothing for the children, and its lower carbon is a footprint, not a
change in the world.</details>

<details><summary>6. The exact words for the US$0 fund?</summary>
"On the SFC's ESG list; US$0.00 at every filing for two years (23 HKEX filings, Sep 2024 to Sep 2026)." Never "never
launched"; never name the manager aloud.</details>

<details><summary>7. If EDMW can't be offered to them, what changes?</summary>
The authorised route costs 1.1–2.45%; the climate fund stops being free; Adrian's 24% goes plain; Carmen pays from the
room if she wants it; the plain side is re-priced. The verdict flips; the rule doesn't.</details>

<details><summary>8. Greenium or green premium: which is the 2bp?</summary>
The greenium (a bond's yield discount, Zerbib 2019). The green premium is a real-economy cost gap, like the van over
diesel.</details>

<details><summary>9. The three Climate Facts triggers?</summary>
Equities under ≈5.3% a year or older flats ≈7% behind (limits); recycled plastic quoted above new (change); the room
measured short (both parents re-sign).</details>

<details><summary>10. How do you read the plan against markets?</summary>
A plain twin fixed at signing; show both returns; split the gap into markets, the ESG tilt, implementation, and our
decisions.</details>
