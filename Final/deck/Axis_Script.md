# PRISM: the script (Team Axis)

Generated 2026-11-13 by `Final/deck/make.py` from the slides' speaker notes. Edit the words in `Final/deck/src/*.html`, not here.

147 spoken words (the budget is about 1,200 for 9:20). Slides allotted 8:55. Speech: 1:00 at 145 words a minute (1:20 with names and handovers); 1:05 at 135 words a minute (1:25 with names and handovers); 1:10 at 125 words a minute (1:30 with names and handovers). Over 10:30 disqualifies the team.

Speaking time at 135 words a minute: Pete 0:57, Lookbua 0:02, Fahtai 0:02, Win 0:02.

## 1 · Limits first. A budget for values. One measure for every decision.
*Pete · 1:05 · 117 spoken words (≈52 s at 135)*

**Pete:** Good morning, we're Team Axis. I'm Pete. What makes a family's whole plan sustainable? Meet the Wongs. Adrian wants capital preservation and a safe retirement. Carmen wants their money to reflect her values, and together they've asked for twenty to twenty-five per cent in ESG. Choosing those funds is one decision. Their plan is far bigger: a home, Carmen's packaging business, their savings and their retirement. Suppose sudden carbon rules arrive in 2030. In our model, nearly half of what they lose lands on their home and business, where no fund choice reaches. So we don't start with products. We start with three rules: limits first, a budget for values, and one measure for every decision.

> Notes: DRAFT, 13 Nov; Pete to make it his own. Reveal order: the question; the parents' wants; the 20-25% ask and the whole plan; the scenario chart; the thesis. Sources: the case, p.2 (Adrian's "capital preservation, retirement adequacy and healthcare protection"; Carmen's ESG "reflecting both her personal values and her belief in the long-term economic opportunities"; objective 5, "at least 20% to 25% of investable assets"). Chart: Final/final_model.py label_storm_path() through fin-label-path; fin_lab_gap32 (by 2032), fin_lab_gap89 (at the model's end), and fin_lab_homebiz, the home's and the business's share of the loss in the children's median inheritance, each channel (portfolio, flat, business) run alone. Same baseline with and without the shock, not two competing plans; shock sizes ILLUSTRATIVE (model_runs.md M7, M8; area4_property_scenario.md §5.1). Don't promise to recover the loss: our plan loses about the same in this shock (M8). The payoff is the limit: in the downturn the plan stays above 85%, and the limit, not the price, picks the flat's route (slides 3 and 6). No climate protection is attributed to ESG funds. The baseline's fee still awaits the purchasable-fund re-base; rerun the chart before submission.

## 2 · PRISM
*Pete · 1:00 · 3 spoken words (≈1 s at 135)*

**Pete:** [script to write]

> Notes: Pete says his simple name before his part. What it must prove: Final/Final_Plan.md §4.5, slide 2, and §4.2 "five letters, five twists". Evidence status per claim in §4.5.

## 3 · Put every decision on one measure, green or not
*Our answer, first · the Wongs, from this year's competition case · Pete · 0:25 · 3 spoken words (≈1 s at 135)*

**Pete:** [script to write]

> Notes: the answer before the steps, drawn as the thesis (Pete, 13 Nov). Each bar is one decision against its ordinary choice, in the children's median inheritance at Carmen's 89 (today's HK$, including the flat), in a normal future against the base (switch_89); keys fin_dot_*_n (Final/final_model.py export_final, 13 Nov). The vans: B1 through the sale price, diesel HK$31/L (M2). Recycled plastic: B4 at today's price parity (US$1,240/t, S&P Platts, 7 Oct 2026), not a model run. Carbon data: its cost at HK$54K a year through the sale price; what it protects is a customer worth 10% of sales, −HK$1.55M (M3). ESG funds: the price of values in fees against all-plain twins, HK$5,107 a year (M4); kept as Carmen's values, not called impact. The scholarship: G1's 20-year fund, ≈HK$0.48M in 2027–28 (M5; Final_Plan.md §5.3 open). The flat: the reverse mortgage against downsizing in 2037 (M6); under the 2030–31 scenario downsizing falls to 82.7% against the reverse mortgage's 89.5% (M7), and still leaves the median more (−HK$2.68M for keeping it), so the limit, not the median, decides. The downturn barely moves the other bars (fin_dot_*_s: +HK$0.47M, −HK$0.07M, −HK$0.48M, −HK$0.73M). Paying out Carmen's share of the van saving (B8, +HK$1.09M) needs the co-founder: slide 8. Tonnes: Decision_List.md (vans 19.3 + LED 4.1 + air-con 2.8; recycled PET 108.1), ESTIMATED on an ILLUSTRATIVE business. Capital: Decision_List.md §2 (ESTIMATED); the data's ≈HK$54–73K a year is the business's running cost. The limit (95 in 100 normally, 85 under the scenario) is ours, ILLUSTRATIVE. The headline against the label approach joins this slide once §5.1 is settled.

## 4 · Settle the family's disagreements once, before any option is priced
*Pete · 0:30 · 3 spoken words (≈1 s at 135)*

**Pete:** [script to write]

> Notes: wants: the case's words (Award2026Case, background). Limits ours (Final_Plan.md §4.2): the floors of 95 and 85 in 100 (Pete, 10 Nov); the family values budget (≈HK$1.4M expected, ≈HK$1.7M at worst: Carmen's ESG funds against plain twins and the funded scholarship; MODEL, EXPLORATORY); tracking-error limits (Adrian ≤0.5% a year, Carmen ≤3%); the education reserve (HK$2.57M, Round One). The values budget is a mental account used on purpose, to lock the choice in advance (§4.2, biases).

## 5 · Check every way risk can reach the family; price only the few that matter
*Lookbua · 0:55 · 3 spoken words (≈1 s at 135)*

**Lookbua:** [script to write]

> Notes: Lookbua says her simple name before her part. The scan (Pete, 11 Nov): 22 routes checked, three priced (the flat × valuation, V1; the business × valuation, V2 with the customers' carbon reporting; savings × transition, T1); one that doesn't reach them (the EU's border carbon tax: paper and plastic are outside it). The grey dots, by register ID (area4_property_scenario.md §6; area2_business.md): flat × Transition: T3 energy prices; flat × Physical: P1 heat; flat × Physical: P2 typhoon damage; flat × Physical: P4 storm surge after 2050; flat × Liability: L1 building notices; flat × Reputation: R1 green claims on the flat; flat × Liquidity: Q1 hard to sell after 50; flat × Liquidity: Q2 repair levy; flat × Data: D1 building age, insurance unknown; flat × Data: D2 future payouts; flat × Conduct: C1 two parents disagree; flat × Conduct: C2 licences; business × Transition: T2 plastics rules; business × Physical: P3 warehouse flooding; business × Liability: L2 compostable claims; business × Reputation: L2 compostable claims, reputation; business × Data: no carbon data yet; savings × Reputation: ESG labels on funds; savings × Data: ESG funds under stress: unmeasured. Must prove: Final_Plan.md §4.5, slide 5. Money: change in the children's median inheritance at Carmen's 89, each on its own (our model, M3, M6, M7: MEASURED, exploratory runs). Customers: HKEX Listing Rules App. C2 (LargeCap Scope 3 from FY2026, first reports 2027). Tonnes: area2_business.md §3b (ESTIMATED, ILLUSTRATIVE business). Older flats, if asked "isn't that just ageing?": HKMA Research Memorandum 05/2023 finds that in a hotter Hong Kong (HKO's "High" scenario) average prices could be 4% to 21% lower by about 2050, and "the older the property, the larger the expected adverse impact". Ageing would lower an old flat's price anyway; the climate part is the extra the HKMA finds. Our −10% by 2037 is a test, not the HKMA's number (ILLUSTRATIVE); area4_property_scenario.md §3.3. The packaging share (98%) is on slide 7; shares as a footprint, not a change, on slide 9. Customers, if asked "reporting is only disclosure, why would anyone leave?": what is sourced is that LargeCap issuers must report Scope 3 from FY2026 and HKEX tells them to request supplier data; her packaging is their Category 1. Our inference from how Scope 3 is counted: a supplier without data is counted at an industry average, which a customer with a target can't show falling, so the account can go to a rival who shows lower numbers. That a customer leaves, and the 10%, are our assumptions (M3, a sensitivity, not a forecast; her customers are ILLUSTRATIVE). The answer is cheap: data at about HK$50K a year pays for itself if it keeps 0.6% of sales (slide 8). "Why wouldn't she just report it?": nothing makes her (SMEs are outside the rules; HKICPA only "encourages" them), it costs money, and the label approach gives no advice on the business, so by default she has none. The lane is the risk if nobody acts; slide 8 is where the plan acts. Sowhat, if asked about the portfolio route: low-carbon funds may lose less in a carbon shock; that isn't measured, so we give it no credit and claim only the flat and the business.

## 6 · The guardrails decide before preferences
*Lookbua · 0:45 · 3 spoken words (≈1 s at 135)*

**Lookbua:** [script to write]

> Notes: Lookbua says their simple name before their part. Evidence status per claim in §4.5.

## 7 · Most effect per HK$ first
*Fahtai · 0:55 · 3 spoken words (≈1 s at 135)*

**Fahtai:** [script to write]

> Notes: Fahtai says their simple name before their part. Evidence status per claim in §4.5.

## 8 · The kind of finance sets the test: judge a green loan as a loan
*Fahtai · 0:55 · 3 spoken words (≈1 s at 135)*

**Fahtai:** [script to write]

> Notes: Fahtai says their simple name before their part. Evidence status per claim in §4.5.

## 9 · The sustainable share is an output of the budgets, not a target
*Win · 1:00 · 3 spoken words (≈1 s at 135)*

**Win:** [script to write]

> Notes: Win says their simple name before their part. Evidence status per claim in §4.5.

## 10 · Every missing price is a decision, and the plan knows when it's wrong
*Win · 0:45 · 3 spoken words (≈1 s at 135)*

**Win:** [script to write]

> Notes: Win says their simple name before their part. Evidence status per claim in §4.5.

## 11 · [Same storm, our plan: above the floor, because the framework took out what didn't work]
*The replay · 2031, the same storm · Pete · 0:40 · 3 spoken words (≈1 s at 135)*

**Pete:** [script to write]

> Notes: Pete says their simple name before their part. Evidence status per claim in §4.5.
