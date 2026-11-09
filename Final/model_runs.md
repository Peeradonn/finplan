# Final Round model runs (EXPLORATORY)

Written by `Final/final_model.py` from the Round One model (`model/run_model.py`, unchanged). **Not slide numbers** until Pete moves them into `export_numbers()` and logs them. 10,000 futures, the same seed as Round One, so each row differs from its base only by the change named. Inheritance: the portfolio left at Carmen's 89 plus home equity, today's money, HK$M; median and the worst 10% (10th percentile).

Check: `sim_x()` reproduces `run_model.sim()` exactly on four cases, and the base inheritance matches `property_options()` (HK$8.15M = `legacy_rmp`).

Inputs (ILLUSTRATIVE unless the brief says otherwise): Carmen's share 50%; equity value 5.6× net profit; profits kept after tax 83.5%; the plan counts 60% of the business value; the pool is HK$7.22M, equity 40% of the mix.


## Base: The family's plan without the medical review at 75 (`ladder_5_89`, the briefs' base)

Odds 82.6%; inheritance median HK$8.15M, worst 10% HK$1.46M.

### M2. B1 the vans, LED and air-con, through the sale price

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Saving at the diesel list price (HK$372K a year): sale +HK$0.52M | 84.7% | +2.1 | 8.77 | +0.62 | 1.46 | +0.00 |
| Saving at HK$25/L diesel (HK$240K a year): sale +HK$0.34M | 84.1% | +1.5 | 8.54 | +0.39 | 1.46 | +0.00 |
| List price, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound) | 90.8% | +8.2 | 11.48 | +3.33 | 1.79 | +0.33 |
| Diesel at list price, plus Carmen's half paid out once the van loan is repaid (2033-38) | 87.9% | +5.3 | 10.10 | +1.95 | 1.46 | +0.00 |
| Diesel at HK$25/L, plus Carmen's half paid out once the van loan is repaid (2033-38) | 86.3% | +3.7 | 9.41 | +1.27 | 1.46 | +0.00 |

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
| Tracking: a bad five years, 2027-31, at the worst five-year lag (HK$26,600 a year) | 81.3% | -1.3 | 7.80 | -0.35 | 1.46 | +0.00 |
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
| New plan: vans (list diesel) + portfolio fees + funded scholarship | 85.0% | +2.4 | 9.00 | +0.85 | 1.46 | +0.00 |
| New plan, diesel at HK$25/L | 84.4% | +1.8 | 8.76 | +0.61 | 1.46 | +0.00 |
| New plan + dividends once the van loan is repaid (2033-38) | 88.3% | +5.7 | 10.38 | +2.23 | 1.46 | +0.00 |
| Label approach (Round One as written: list funds, unfunded lifelong pledge) | 75.7% | -6.9 | 6.55 | -1.59 | 1.46 | +0.00 |

Against the label approach, the framework's plan changes the odds by +9.3 points and the median inheritance by HK$+2.44M.


## Base: The family's plan with the medical review at 75 (`switch_89`, the base: Pete, 9 Nov)

Odds 96.8%; inheritance median HK$13.01M, worst 10% HK$3.97M.

### M2. B1 the vans, LED and air-con, through the sale price

| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |
|---|---|---|---|---|---|---|
| Saving at the diesel list price (HK$372K a year): sale +HK$0.52M | 97.4% | +0.7 | 13.64 | +0.63 | 4.47 | +0.50 |
| Saving at HK$25/L diesel (HK$240K a year): sale +HK$0.34M | 97.2% | +0.5 | 13.42 | +0.41 | 4.30 | +0.33 |
| List price, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound) | 98.8% | +2.0 | 16.34 | +3.33 | 6.21 | +2.24 |
| Diesel at list price, plus Carmen's half paid out once the van loan is repaid (2033-38) | 98.4% | +1.6 | 14.95 | +1.95 | 5.32 | +1.35 |
| Diesel at HK$25/L, plus Carmen's half paid out once the van loan is repaid (2033-38) | 97.9% | +1.1 | 14.27 | +1.26 | 4.88 | +0.91 |

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
| Tracking: a bad five years, 2027-31, at the worst five-year lag (HK$26,600 a year) | 96.5% | -0.3 | 12.64 | -0.37 | 3.76 | -0.21 |
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
| New plan: vans (list diesel) + portfolio fees + funded scholarship | 97.5% | +0.8 | 13.95 | +0.94 | 4.58 | +0.61 |
| New plan, diesel at HK$25/L | 97.3% | +0.5 | 13.71 | +0.70 | 4.40 | +0.43 |
| New plan + dividends once the van loan is repaid (2033-38) | 98.4% | +1.6 | 15.30 | +2.29 | 5.49 | +1.52 |
| Label approach (Round One as written: list funds, unfunded lifelong pledge) | 94.0% | -2.8 | 11.38 | -1.63 | 2.72 | -1.25 |

Against the label approach, the framework's plan changes the odds by +3.6 points and the median inheritance by HK$+2.57M.


## What is not in these runs

- Tonnes (the world side) are not model outputs: ≈134 t a year from the business (vans 19.3, LED 4.1, air-con 2.8, recycled PET 108.1; ESTIMATED on an ILLUSTRATIVE business), from `Final/Decision_List.md`.
- The vans' effect assumes a buyer pays for the higher profit at the same multiple; no green premium on the multiple.
- The scenario's shocks are the property brief's (§5.1); the ESG sleeve takes the same equity shock.
- Guardrails are off, as in `ladder_5_89` and `switch_89`.

