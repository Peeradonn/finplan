# Final Round model runs (EXPLORATORY)

Written by `Final/final_model.py` from the Round One model (`model/run_model.py`, unchanged). **Not slide numbers** until Pete moves them into `export_numbers()` and logs them. 10,000 futures, the same seed as Round One, so each row differs from its base only by the change named. Inheritance: the portfolio left at Carmen's 89 plus home equity, today's money, HK$M; median and the worst 10% (10th percentile).

Check: `sim_x()` reproduces `run_model.sim()` exactly on four cases, and the base inheritance matches `property_options()` (HK$8.15M = `legacy_rmp`).

Inputs (ILLUSTRATIVE unless the brief says otherwise): Carmen's share 50%; equity value 5.6× net profit; profits kept after tax 83.5%; the plan counts 60% of the business value; the pool is HK$7.22M, equity 40% of the mix.


## Base: The family's plan without the medical review at 75 (`ladder_5_89`, the briefs' base)

Odds 82.6%; inheritance median HK$8.15M, worst 10% HK$1.46M.

### M2. B1 the vans, LED and air-con, through the sale price

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Diesel at HK$31/L, the government's after-discount average (base): saving HK$303K a year, sale +HK$0.43M | 84.4% | +1.8 | 8.65 | +0.50 | 1.46 | +0.00 |
| Diesel at HK$37.93/L, the pump list price: saving HK$372K a year, sale +HK$0.52M | 84.7% | +2.1 | 8.77 | +0.62 | 1.46 | +0.00 |
| Diesel at HK$25/L, the low case: saving HK$243K a year, sale +HK$0.34M | 84.1% | +1.5 | 8.54 | +0.40 | 1.46 | +0.00 |
| HK$31/L, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound) | 89.6% | +7.0 | 10.87 | +2.72 | 1.46 | +0.00 |
| Diesel at HK$31/L, the government's after-discount average (base), plus Carmen's half paid out once the van loan is repaid (2033-38) | 87.1% | +4.4 | 9.72 | +1.58 | 1.46 | +0.00 |
| Diesel at HK$37.93/L, the pump list price, plus Carmen's half paid out once the van loan is repaid (2033-38) | 87.9% | +5.3 | 10.10 | +1.96 | 1.46 | +0.00 |
| Diesel at HK$25/L, the low case, plus Carmen's half paid out once the van loan is repaid (2033-38) | 86.3% | +3.7 | 9.42 | +1.28 | 1.46 | +0.00 |

### M3. B3 emissions data: what a lost customer would cost (a sensitivity, not a forecast)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| A customer worth 5% of sales leaves: sale −HK$0.63M | 79.6% | -3.0 | 7.42 | -0.72 | 1.46 | +0.00 |
| A customer worth 10% of sales leaves: sale −HK$1.25M | 76.4% | -6.2 | 6.69 | -1.46 | 1.46 | +0.00 |
| Per HK$1M off the sale price | 77.8% | -4.8 | 6.98 | -1.16 | 1.46 | +0.00 |

### M4. P1-P5 the portfolio

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Fees: label-approach funds → candidate A (HK$9,647 a year saved) | 85.3% | +2.7 | 9.18 | +1.04 | 1.46 | +0.00 |
| Price of values in fees vs an all-plain twin (HK$5,107 a year) | 81.0% | -1.7 | 7.63 | -0.52 | 1.46 | +0.00 |
| Tracking: a bad five years, 2027-31, at the last five years' lag (HK$26,600 a year) | 81.3% | -1.3 | 7.80 | -0.35 | 1.46 | +0.00 |
| Tracking, if that lag repeated every year to 89 (a stress) | 72.8% | -9.8 | 5.59 | -2.56 | 1.46 | +0.00 |

### M5. G1 the scholarship

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Label approach (Round One as written): ≈HK$30K a year for life, from cash flow | 75.7% | -6.9 | 6.55 | -1.59 | 1.46 | +0.00 |
| Funded: a 20-year fund, 2 × HK$240K in 2027-28, with relief | 80.0% | -2.6 | 7.37 | -0.77 | 1.46 | +0.00 |

### M6. H1 the flat: the route, if the old flat loses value (newer flats hold)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Reverse mortgage, old flat 0% lower from 2037 | 82.6% | +0.0 | 8.15 | +0.00 | 1.46 | +0.00 |
| Downsize in 2037, old flat 0% lower | 83.1% | +0.5 | 12.24 | +4.10 | 4.73 | +3.27 |
| Reverse mortgage, old flat 10% lower from 2037 | 81.2% | -1.4 | 7.47 | -0.68 | 1.08 | -0.38 |
| Downsize in 2037, old flat 10% lower | 76.9% | -5.7 | 10.57 | +2.42 | 4.73 | +3.27 |
| Reverse mortgage, old flat 20% lower from 2037 | 79.9% | -2.7 | 6.78 | -1.37 | 0.70 | -0.76 |
| Downsize in 2037, old flat 20% lower | 69.8% | -12.8 | 8.81 | +0.66 | 4.73 | +3.27 |
| Reverse mortgage from 2045 instead, 2037's payout kept (Round One's `rmp2045_89` run: understated) | 73.5% | -9.1 | 8.78 | +0.63 | 4.11 | +2.65 |
| Reverse mortgage from 2045 instead, at the 2045 flat value and Carmen's age 68 (HKMC 2026 table) | 80.5% | -2.1 | 8.53 | +0.39 | 2.50 | +1.04 |

### M7. The scenario: late and sudden (2030-31)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Portfolio only (returns and inflation) | 72.2% | -10.4 | 5.73 | -2.41 | 1.46 | +0.00 |
| Flat only (smaller reverse mortgage, lower equity) | 80.4% | -2.2 | 6.75 | -1.39 | 0.56 | -0.90 |
| Business only (sale −10%, Carmen's draw −HK$100K in 2030-31) | 79.9% | -2.7 | 7.45 | -0.70 | 1.46 | +0.00 |
| **All together** | 66.7% | -15.9 | 3.63 | -4.51 | 0.56 | -0.90 |
| All together, downsizing instead (only the old flat falls) | 58.0% | -24.6 | 6.28 | -1.86 | 4.73 | +3.27 |

### The recommendation: the framework's plan against the label approach

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship | 84.7% | +2.1 | 8.87 | +0.73 | 1.46 | +0.00 |
| New plan, diesel at the HK$37.93/L list price | 85.0% | +2.4 | 9.00 | +0.85 | 1.46 | +0.00 |
| New plan, diesel at HK$25/L | 84.4% | +1.8 | 8.76 | +0.62 | 1.46 | +0.00 |
| New plan + dividends once the van loan is repaid (2033-38) | 87.4% | +4.8 | 10.00 | +1.86 | 1.46 | +0.00 |
| Label approach (Round One as written: list funds, unfunded lifelong pledge) | 75.7% | -6.9 | 6.55 | -1.59 | 1.46 | +0.00 |

Against the label approach, the framework's plan changes the odds by +9.0 points and the median inheritance by HK$+2.32M.

### M8. The whole household under stress (2030-31, all channels)

Every row runs M7's **All together** scenario (portfolio returns and inflation, the flat, the business at once; reverse-mortgage route). **Change is against row 1**, the plan as it stands under the scenario. A decision that moves the sale price takes the scenario's 10% cut with the rest of the sale; a decision's own flows are added to the scenario's (Carmen's draw −HK$100K in 2030-31).

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| The plan as it stands, under the scenario (reproduces M7's All together exactly) | 66.7% | +0.0 | 3.63 | +0.00 | 0.56 | +0.00 |
| Label approach (list funds, unfunded lifelong pledge), under the scenario | 57.9% | -8.7 | 1.99 | -1.64 | 0.56 | +0.00 |
| New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship, under the scenario | 69.5% | +2.8 | 4.23 | +0.60 | 0.56 | +0.00 |
| New plan + dividends once the van loan is repaid (2033-38), under the scenario | 73.9% | +7.2 | 5.34 | +1.70 | 0.56 | +0.00 |
| Vans, LED and air-con alone (HK$31/L): sale +HK$0.43M before the 10% cut | 69.0% | +2.4 | 4.07 | +0.43 | 0.56 | +0.00 |
| Dividends 2033-38 alone (Carmen's half of the HK$31/L saving; no sale uplift) | 71.5% | +4.8 | 4.68 | +1.05 | 0.56 | +0.00 |
| Fees alone: label-approach funds → candidate A (HK$9,647 a year saved) | 70.5% | +3.8 | 4.52 | +0.89 | 0.56 | +0.00 |
| Price of values in fees vs an all-plain twin (HK$5,107 a year) | 64.5% | -2.2 | 3.17 | -0.46 | 0.56 | +0.00 |
| Funded scholarship alone: 2 × HK$240K in 2027-28, with relief | 63.0% | -3.7 | 2.90 | -0.74 | 0.56 | +0.00 |
| The label approach's lifelong pledge alone: ≈HK$30K a year from cash flow | 57.9% | -8.7 | 1.99 | -1.64 | 0.56 | +0.00 |

**Stress minus normal:** each decision's change under the scenario (against row 1) minus its change in a normal future (against the base, as in M2-M5 and the recommendation). Odds in points, inheritance in HK$M. Positive: the decision is worth more when climate hits; negative: it adds value mainly in calm times.

- Vans: odds +2.4 under stress, +1.8 normal (**+0.6**); median +0.43 under stress, +0.50 normal (**-0.07**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- Dividends: odds +4.8 under stress, +3.2 normal (**+1.6**); median +1.05 under stress, +1.07 normal (**-0.03**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- Fees: odds +3.8 under stress, +2.7 normal (**+1.1**); median +0.89 under stress, +1.04 normal (**-0.15**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- Price of values: odds -2.2 under stress, -1.7 normal (**-0.5**); median -0.46 under stress, -0.52 normal (**+0.06**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- Funded scholarship: odds -3.7 under stress, -2.6 normal (**-1.0**); median -0.74 under stress, -0.77 normal (**+0.04**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- Lifelong pledge: odds -8.7 under stress, -6.9 normal (**-1.8**); median -1.64 under stress, -1.59 normal (**-0.05**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- New plan (the package): odds +2.8 under stress, +2.1 normal (**+0.7**); median +0.60 under stress, +0.73 normal (**-0.13**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).
- New plan + dividends (the package): odds +7.2 under stress, +4.8 normal (**+2.4**); median +1.70 under stress, +1.86 normal (**-0.15**); worst 10% +0.00 under stress, +0.00 normal (**+0.00**).

**Headline under stress:** against the label approach, both under the scenario, the new plan changes the odds by +11.5 points, median HK$+2.24M, worst 10% HK$+0.00M (normal future: +9.0 points, median HK$+2.32M, worst 10% HK$+0.00M). With the dividends: +15.9 points, median HK$+3.34M, worst 10% HK$+0.00M under stress (normal: +11.7 points, median HK$+3.45M, worst 10% HK$+0.00M).

**The carbon data's cost in the new plan** (≈HK$54-73K a year, paid by the business from 2027; `Decision_List.md` B3). It goes through the sale price as the vans' saving does: × 83.5% kept after tax × 5.6 × Carmen's 50% × the 60% counted, so the buyer is assumed to keep paying it; like the saving, the cost before the sale is not taken from Carmen's draw. Change against the base in a normal future, against row 1 above under the scenario.

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Normal future: new plan + carbon data at HK$54K a year (sale −HK$0.08M) | 84.4% | +1.8 | 8.77 | +0.63 | 1.46 | +0.00 |
| Normal future: new plan + carbon data at HK$73K a year (sale −HK$0.10M) | 84.3% | +1.7 | 8.74 | +0.60 | 1.46 | +0.00 |
| Under the scenario: new plan + carbon data at HK$54K a year (sale −HK$0.08M before the 10% cut) | 69.1% | +2.4 | 4.15 | +0.52 | 0.56 | +0.00 |
| Under the scenario: new plan + carbon data at HK$73K a year (sale −HK$0.10M before the 10% cut) | 69.0% | +2.3 | 4.12 | +0.49 | 0.56 | +0.00 |

- At HK$54K a year, the carbon data costs the new plan -0.3 points, median HK$-0.10M, worst 10% HK$+0.00M in a normal future and -0.4 points, median HK$-0.08M, worst 10% HK$+0.00M under the scenario. The new plan with it, against the label approach: +8.7 points, median HK$+2.22M, worst 10% HK$+0.00M normal; +11.2 points, median HK$+2.16M, worst 10% HK$+0.00M under stress.
- At HK$73K a year, the carbon data costs the new plan -0.4 points, median HK$-0.13M, worst 10% HK$+0.00M in a normal future and -0.5 points, median HK$-0.11M, worst 10% HK$+0.00M under the scenario. The new plan with it, against the label approach: +8.6 points, median HK$+2.19M, worst 10% HK$+0.00M normal; +11.1 points, median HK$+2.13M, worst 10% HK$+0.00M under stress.

Notes on M8:
- The scenario does not raise diesel prices, so the vans' saving is not larger under stress; and the ESG sleeve takes the same shock as other equity (M7), so the fee change and the price of values get no stress-specific credit. Any difference between stress and normal for them comes only from the model's arithmetic (a fixed sum or return on a pot that is smaller or empty in more futures).
- Under the scenario the worst-10% future has already run out of money (its inheritance is the flat's equity only): a cost cannot lower it further, and a gain moves it only if it keeps that future solvent. So the positive worst-10% gaps of the costs above are a floor, not risk removed; read the odds.
- The label approach is the plan as it stands plus the lifelong pledge (the plan's fees are already the list funds'), so its row and the pledge's are the same by construction.
- The carbon data's benefit (customers kept, M3) is not in these rows: they price its cost only.
- Dividends start in 2033, after the shock; the scenario's draw cut in 2030-31 is unchanged.
- Not run: the median share of net worth in the flat and the business in 2033 and 2039. The model has no business value before the 2039 sale and no mortgage balance before 2037, and `sim_x()` keeps only the end pot, so it would need new ILLUSTRATIVE paths; in 2039 the business is sold in the year, so its share is nil by construction. In 2026 (the case's balance sheet; no decision acts before 2027, so the same for both plans) the flat and the business are HK$16.50M of HK$27.19M of assets (61%); net of the mortgage and the business loan, HK$13.80M of HK$24.41M net worth (57%).


## Base: The family's plan with the medical review at 75 (`switch_89`, the base: Pete, 9 Nov)

Odds 96.8%; inheritance median HK$13.01M, worst 10% HK$3.97M.

### M2. B1 the vans, LED and air-con, through the sale price

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Diesel at HK$31/L, the government's after-discount average (base): saving HK$303K a year, sale +HK$0.43M | 97.3% | +0.6 | 13.52 | +0.51 | 4.38 | +0.41 |
| Diesel at HK$37.93/L, the pump list price: saving HK$372K a year, sale +HK$0.52M | 97.4% | +0.7 | 13.64 | +0.63 | 4.47 | +0.50 |
| Diesel at HK$25/L, the low case: saving HK$243K a year, sale +HK$0.34M | 97.2% | +0.5 | 13.42 | +0.41 | 4.30 | +0.33 |
| HK$31/L, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound) | 98.6% | +1.8 | 15.73 | +2.72 | 5.77 | +1.80 |
| Diesel at HK$31/L, the government's after-discount average (base), plus Carmen's half paid out once the van loan is repaid (2033-38) | 98.1% | +1.3 | 14.61 | +1.60 | 5.08 | +1.12 |
| Diesel at HK$37.93/L, the pump list price, plus Carmen's half paid out once the van loan is repaid (2033-38) | 98.4% | +1.6 | 14.96 | +1.95 | 5.32 | +1.35 |
| Diesel at HK$25/L, the low case, plus Carmen's half paid out once the van loan is repaid (2033-38) | 97.9% | +1.1 | 14.29 | +1.28 | 4.89 | +0.92 |

### M3. B3 emissions data: what a lost customer would cost (a sensitivity, not a forecast)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| A customer worth 5% of sales leaves: sale −HK$0.63M | 95.8% | -0.9 | 12.24 | -0.77 | 3.40 | -0.57 |
| A customer worth 10% of sales leaves: sale −HK$1.25M | 94.4% | -2.4 | 11.46 | -1.55 | 2.88 | -1.09 |
| Per HK$1M off the sale price | 95.0% | -1.8 | 11.79 | -1.22 | 3.09 | -0.88 |

### M4. P1-P5 the portfolio

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Fees: label-approach funds → candidate A (HK$9,647 a year saved) | 97.5% | +0.7 | 14.14 | +1.13 | 4.60 | +0.63 |
| Price of values in fees vs an all-plain twin (HK$5,107 a year) | 96.3% | -0.5 | 12.43 | -0.57 | 3.66 | -0.31 |
| Tracking: a bad five years, 2027-31, at the last five years' lag (HK$26,600 a year) | 96.5% | -0.3 | 12.64 | -0.37 | 3.76 | -0.21 |
| Tracking, if that lag repeated every year to 89 (a stress) | 93.7% | -3.1 | 10.23 | -2.78 | 2.48 | -1.49 |

### M5. G1 the scholarship

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Label approach (Round One as written): ≈HK$30K a year for life, from cash flow | 94.0% | -2.8 | 11.38 | -1.63 | 2.72 | -1.25 |
| Funded: a 20-year fund, 2 × HK$240K in 2027-28, with relief | 96.0% | -0.7 | 12.20 | -0.80 | 3.48 | -0.49 |

### M6. H1 the flat: the route, if the old flat loses value (newer flats hold)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Reverse mortgage, old flat 0% lower from 2037 | 96.8% | +0.0 | 13.01 | +0.00 | 3.97 | +0.00 |
| Downsize in 2037, old flat 0% lower | 96.2% | -0.6 | 17.08 | +4.07 | 7.18 | +3.21 |
| Reverse mortgage, old flat 10% lower from 2037 | 96.3% | -0.5 | 12.29 | -0.71 | 3.32 | -0.65 |
| Downsize in 2037, old flat 10% lower | 93.6% | -3.2 | 15.32 | +2.32 | 5.95 | +1.98 |
| Reverse mortgage, old flat 20% lower from 2037 | 95.8% | -1.0 | 11.59 | -1.42 | 2.66 | -1.30 |
| Downsize in 2037, old flat 20% lower | 89.8% | -6.9 | 13.57 | +0.56 | 4.73 | +0.76 |
| Reverse mortgage from 2045 instead, 2037's payout kept (Round One's `rmp2045_89` run: understated) | 93.1% | -3.7 | 13.54 | +0.54 | 5.06 | +1.09 |
| Reverse mortgage from 2045 instead, at the 2045 flat value and Carmen's age 68 (HKMC 2026 table) | 96.3% | -0.4 | 13.34 | +0.33 | 4.71 | +0.74 |

### M7. The scenario: late and sudden (2030-31)

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Portfolio only (returns and inflation) | 92.9% | -3.8 | 10.53 | -2.48 | 2.30 | -1.67 |
| Flat only (smaller reverse mortgage, lower equity) | 96.1% | -0.7 | 11.56 | -1.44 | 2.62 | -1.35 |
| Business only (sale −10%, Carmen's draw −HK$100K in 2030-31) | 96.0% | -0.8 | 12.30 | -0.71 | 3.47 | -0.50 |
| **All together** | 89.5% | -7.3 | 8.40 | -4.60 | 0.56 | -3.41 |
| All together, downsizing instead (only the old flat falls) | 82.7% | -14.1 | 11.08 | -1.93 | 4.73 | +0.76 |

### The recommendation: the framework's plan against the label approach

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship | 97.4% | +0.6 | 13.82 | +0.81 | 4.48 | +0.51 |
| New plan, diesel at the HK$37.93/L list price | 97.5% | +0.8 | 13.95 | +0.95 | 4.58 | +0.61 |
| New plan, diesel at HK$25/L | 97.3% | +0.5 | 13.71 | +0.71 | 4.41 | +0.44 |
| New plan + dividends once the van loan is repaid (2033-38) | 98.2% | +1.4 | 14.93 | +1.92 | 5.23 | +1.27 |
| Label approach (Round One as written: list funds, unfunded lifelong pledge) | 94.0% | -2.8 | 11.38 | -1.63 | 2.72 | -1.25 |

Against the label approach, the framework's plan changes the odds by +3.4 points and the median inheritance by HK$+2.44M.

### M8. The whole household under stress (2030-31, all channels)

Every row runs M7's **All together** scenario (portfolio returns and inflation, the flat, the business at once; reverse-mortgage route). **Change is against row 1**, the plan as it stands under the scenario. A decision that moves the sale price takes the scenario's 10% cut with the rest of the sale; a decision's own flows are added to the scenario's (Carmen's draw −HK$100K in 2030-31).

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| The plan as it stands, under the scenario (reproduces M7's All together exactly) | 89.5% | +0.0 | 8.40 | +0.00 | 0.56 | +0.00 |
| Label approach (list funds, unfunded lifelong pledge), under the scenario | 84.1% | -5.4 | 6.83 | -1.58 | 0.56 | +0.00 |
| New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship, under the scenario | 91.0% | +1.5 | 9.07 | +0.67 | 0.84 | +0.28 |
| New plan + dividends once the van loan is repaid (2033-38), under the scenario | 93.5% | +4.0 | 10.17 | +1.77 | 1.61 | +1.05 |
| Vans, LED and air-con alone (HK$31/L): sale +HK$0.43M before the 10% cut | 90.8% | +1.3 | 8.87 | +0.47 | 0.81 | +0.25 |
| Dividends 2033-38 alone (Carmen's half of the HK$31/L saving; no sale uplift) | 92.2% | +2.7 | 9.47 | +1.07 | 1.21 | +0.64 |
| Fees alone: label-approach funds → candidate A (HK$9,647 a year saved) | 91.4% | +1.9 | 9.38 | +0.97 | 0.97 | +0.41 |
| Price of values in fees vs an all-plain twin (HK$5,107 a year) | 88.3% | -1.2 | 7.92 | -0.48 | 0.56 | +0.00 |
| Funded scholarship alone: 2 × HK$240K in 2027-28, with relief | 87.5% | -2.0 | 7.67 | -0.73 | 0.56 | +0.00 |
| The label approach's lifelong pledge alone: ≈HK$30K a year from cash flow | 84.1% | -5.4 | 6.83 | -1.58 | 0.56 | +0.00 |

**Stress minus normal:** each decision's change under the scenario (against row 1) minus its change in a normal future (against the base, as in M2-M5 and the recommendation). Odds in points, inheritance in HK$M. Positive: the decision is worth more when climate hits; negative: it adds value mainly in calm times.

- Vans: odds +1.3 under stress, +0.6 normal (**+0.8**); median +0.47 under stress, +0.51 normal (**-0.04**); worst 10% +0.25 under stress, +0.41 normal (**-0.16**).
- Dividends: odds +2.7 under stress, +0.9 normal (**+1.7**); median +1.07 under stress, +1.09 normal (**-0.02**); worst 10% +0.64 under stress, +0.76 normal (**-0.11**).
- Fees: odds +1.9 under stress, +0.7 normal (**+1.1**); median +0.97 under stress, +1.13 normal (**-0.16**); worst 10% +0.41 under stress, +0.63 normal (**-0.22**).
- Price of values: odds -1.2 under stress, -0.5 normal (**-0.7**); median -0.48 under stress, -0.57 normal (**+0.09**); worst 10% +0.00 under stress, -0.31 normal (**+0.31**).
- Funded scholarship: odds -2.0 under stress, -0.7 normal (**-1.2**); median -0.73 under stress, -0.80 normal (**+0.07**); worst 10% +0.00 under stress, -0.49 normal (**+0.49**).
- Lifelong pledge: odds -5.4 under stress, -2.8 normal (**-2.6**); median -1.58 under stress, -1.63 normal (**+0.05**); worst 10% +0.00 under stress, -1.25 normal (**+1.25**).
- New plan (the package): odds +1.5 under stress, +0.6 normal (**+0.9**); median +0.67 under stress, +0.81 normal (**-0.14**); worst 10% +0.28 under stress, +0.51 normal (**-0.23**).
- New plan + dividends (the package): odds +4.0 under stress, +1.4 normal (**+2.6**); median +1.77 under stress, +1.92 normal (**-0.15**); worst 10% +1.05 under stress, +1.27 normal (**-0.22**).

**Headline under stress:** against the label approach, both under the scenario, the new plan changes the odds by +6.9 points, median HK$+2.25M, worst 10% HK$+0.28M (normal future: +3.4 points, median HK$+2.44M, worst 10% HK$+1.76M). With the dividends: +9.4 points, median HK$+3.35M, worst 10% HK$+1.05M under stress (normal: +4.2 points, median HK$+3.55M, worst 10% HK$+2.52M).

**The carbon data's cost in the new plan** (≈HK$54-73K a year, paid by the business from 2027; `Decision_List.md` B3). It goes through the sale price as the vans' saving does: × 83.5% kept after tax × 5.6 × Carmen's 50% × the 60% counted, so the buyer is assumed to keep paying it; like the saving, the cost before the sale is not taken from Carmen's draw. Change against the base in a normal future, against row 1 above under the scenario.

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Normal future: new plan + carbon data at HK$54K a year (sale −HK$0.08M) | 97.3% | +0.5 | 13.72 | +0.71 | 4.41 | +0.44 |
| Normal future: new plan + carbon data at HK$73K a year (sale −HK$0.10M) | 97.3% | +0.5 | 13.69 | +0.68 | 4.39 | +0.43 |
| Under the scenario: new plan + carbon data at HK$54K a year (sale −HK$0.08M before the 10% cut) | 90.8% | +1.3 | 8.99 | +0.59 | 0.78 | +0.21 |
| Under the scenario: new plan + carbon data at HK$73K a year (sale −HK$0.10M before the 10% cut) | 90.7% | +1.2 | 8.96 | +0.56 | 0.75 | +0.19 |

- At HK$54K a year, the carbon data costs the new plan -0.1 points, median HK$-0.10M, worst 10% HK$-0.07M in a normal future and -0.2 points, median HK$-0.08M, worst 10% HK$-0.07M under the scenario. The new plan with it, against the label approach: +3.3 points, median HK$+2.34M, worst 10% HK$+1.69M normal; +6.7 points, median HK$+2.17M, worst 10% HK$+0.21M under stress.
- At HK$73K a year, the carbon data costs the new plan -0.1 points, median HK$-0.13M, worst 10% HK$-0.09M in a normal future and -0.3 points, median HK$-0.11M, worst 10% HK$-0.09M under the scenario. The new plan with it, against the label approach: +3.3 points, median HK$+2.31M, worst 10% HK$+1.68M normal; +6.6 points, median HK$+2.14M, worst 10% HK$+0.19M under stress.

Notes on M8:
- The scenario does not raise diesel prices, so the vans' saving is not larger under stress; and the ESG sleeve takes the same shock as other equity (M7), so the fee change and the price of values get no stress-specific credit. Any difference between stress and normal for them comes only from the model's arithmetic (a fixed sum or return on a pot that is smaller or empty in more futures).
- Under the scenario the worst-10% future has already run out of money (its inheritance is the flat's equity only): a cost cannot lower it further, and a gain moves it only if it keeps that future solvent. So the positive worst-10% gaps of the costs above are a floor, not risk removed; read the odds.
- The label approach is the plan as it stands plus the lifelong pledge (the plan's fees are already the list funds'), so its row and the pledge's are the same by construction.
- The carbon data's benefit (customers kept, M3) is not in these rows: they price its cost only.
- Dividends start in 2033, after the shock; the scenario's draw cut in 2030-31 is unchanged.
- Not run: the median share of net worth in the flat and the business in 2033 and 2039. The model has no business value before the 2039 sale and no mortgage balance before 2037, and `sim_x()` keeps only the end pot, so it would need new ILLUSTRATIVE paths; in 2039 the business is sold in the year, so its share is nil by construction. In 2026 (the case's balance sheet; no decision acts before 2027, so the same for both plans) the flat and the business are HK$16.50M of HK$27.19M of assets (61%); net of the mortgage and the business loan, HK$13.80M of HK$24.41M net worth (57%).


## What is not in these runs

- Tonnes (the world side) are not model outputs: ≈134 t a year from the business (vans 19.3, LED 4.1, air-con 2.8, recycled PET 108.1; ESTIMATED on an ILLUSTRATIVE business), from `Final/Decision_List.md`.
- The vans' effect assumes a buyer pays for the higher profit at the same multiple; no green premium on the multiple.
- The scenario's shocks are the property brief's (§5.1); the ESG sleeve takes the same equity shock.
- Guardrails are off, as in `ladder_5_89` and `switch_89`.

