# Number check: findings

**Reviewed:** `document/proposal-v2.html` (built copy holding direct edits, 30 Sep 19:58), page by page, against
`figures/numbers.json`, `figures/figure-data.md`, `model/wong_model.xlsx` (Inputs, BalanceSheet, Tax, Medical, Outputs),
the case PDF, `Pete/assumptions-methodology.md`, `Pete/macro-snapshot-2026-09-23.md`, `Pete/working-brief.md`,
`Updated_Investment_Win.md`, plus read-only model runs (`import run_model`, seed 42, 10,000 paths, nothing on disk
changed). v2's numbers match the current build (`proposal.html`) except where v2 edited the text. Quotes below are
v2 wording: carry fixes into the page sources together with the v2 edits.

**Lead 1 (Carmen's business) is resolved in v2:** the case lists "Carmen's business value (going concern estimate)
5,000,000" as a family asset, with no 50% stake. v2 now says HK$5.0M on p2, p10 and p12, and HK$3.0M (a 40% discount)
is the model's sale proceeds. Net worth 24.41 is consistent with it.

---

### N1 · Pages 2, 4, 5, 13 · severity: wrong
Quote: "spending never falls below HK$546K" (p4) · "in the worst one simulation in twenty, spending falls to HK$546K
a year rather than to guaranteed income alone, HK$159K" (p5) · "leaving HK$108K a year" (p4) · Figure 11 note
"Spending a year in today's money" · "the worst year stays above HK$546K" (p2)
Found: `export_numbers()` reports *share of that year's target × HK$780K* (`levels × SPEND`). After Adrian's death the
target is already 70% of HK$780K, so in Carmen's years alone these figures overstate real spending by 1/0.7. Read-only
rerun, real money (level × target, today's money):

| Key | Quoted | Real spending, today's money | Year of the minimum |
|---|---|---|---|
| guardswitch_worst5 / ann_w1_with | HK$546K | **HK$382K** | median 2058 (Carmen alone) |
| fixflex_worst5 / fixswitch_worst5 | HK$159K | **HK$111K** | median 2071 |
| ann_w1_without | HK$108K | **HK$76K** | — |
| guardswitch_typical (average over the years) | HK$739K | HK$672K (couple and survivor years mixed) | — |

HK$546K is exactly the guardrail floor (40% essentials + half of the 60% discretionary = 70% of *target*). Carmen's
target alone is HK$546K, so her floor is HK$382K. The worst-year figures are also measured to Carmen's **95**, not 89
(`life()` uses `b`, the C95 run), which Figure 11's note does not say.
Fix: pick one. (a) Keep the keys and relabel them as a share of the budget: "spending never falls below 70% of the
agreed budget (HK$546K a year for the couple, HK$382K for Carmen alone)"; Figure 11 note: "Worst 1 in 20: lowest
year's spending as a share of the planned budget, × HK$780K, in the worst 5% of simulations to Carmen's 95." (b) Add
real-money keys to `export_numbers()` (`levels × SPEND × (SURV if y > ALE else 1)`) and quote those. Either way, the
p5 comparison "HK$546K rather than HK$159K" keeps its ratio. The rec_*_typical keys (HK$670K on p13, etc.) share the
same basis, so the label applies to them too.

### N2 · Page 10 · severity: wrong
Quote: "If Adrian dies, Carmen's income leaves a shortfall of about HK$157K a year until she is 62; with the mortgage
and final costs that is HK$1.75M."
Found: the mortgage alone is HK$1.8M. Figure 20 shows the **need is HK$3.75M**, and the existing HK$2.0M policy leaves
the HK$1.75M top-up. My arithmetic: 157K × PV(13 years, 2%) = 157 × 11.35 = HK$1.78M, + mortgage 1.80 + final costs
≈0.17 = HK$3.75M, less 2.0M = HK$1.75M.
Fix: "…until she is 62; with the mortgage and final costs she would need HK$3.75M, of which his existing policy pays
HK$2.0M, leaving HK$1.75M to cover."

### N3 · Page 8 · severity: wrong
Quote: "their correlation is about 0.54, against about 0.92 (Berg, Kölbel and Rigobon, 2022)"
Found: the paper compares ESG ratings with **credit ratings from Moody's and S&P, which are correlated at 0.99**
(MIT Sloan's summary of the Aggregate Confusion project; the paper's R² values of 0.92–0.99 are a different
statistic and are probably where 0.92 came from). 0.54 is the paper's average; the published version gives the range
0.38–0.71. The same 0.92 is in `Updated_Investment_Win.md` line 187.
Fix: "about 0.54, against 0.99 for credit ratings (Berg, Kölbel and Rigobon, 2022)".

### N4 · Page 5 · severity: wrong
Quote: "so only the HK$65K a year the parents pay today is counted inside it"
Found: Inputs, "Premiums already inside the 780,000 (today money)" = 65,000, note: "~ both parents' Flexi median at 65.
TEAM TO AGREE". That is 32,542 + 31,599 = HK$64K, the VHIS Flexi premiums at age 65 at today's prices, **not what they
pay today**. The case does not state today's premiums; the parents are on group cover.
Fix: "so only about HK$65K a year of premiums (both parents' Flexi premiums at 65, at today's prices) is counted
inside it."

### N5 · Page 15 · severity: wrong
Quote: A1 "Life expectancy | Adrian 84, Carmen 89 | Both 95 | Case"
Found: the to-95 runs keep Adrian's death at 2056 (`ALE`): his annuity stops and survivor spending starts. Only
Carmen's horizon moves to 95. The single exception is `annuity_longlife_pts` (Adrian to 2067), which the text does not
quote. Figure 27 F5 correctly says "Carmen lives to 95".
Fix: stress column "Carmen 95".

## Batch 1 ready

### N6 · Page 8 · severity: inconsistent
Quote: "The global core, the BOC-Prudential MSCI World ESG Index Fund, is one of only two global equity index funds on
that list; a plain index fund would leave the family at 19%."
Found: 19% holds only if **Adrian's** core were plain: 2.633 − 0.620 (30% of 2.066) = 2.01 → 19.2% of 10.47. The
manuscript (line 368) says "Adrian's global core", but p7 and this page now make it both parents' core. If both
parents' cores were plain: 2.633 − 0.620 − 0.723 = 1.29 → **12%**.
Fix: "a plain index fund in both portfolios would leave the family at 12%", or restore "Adrian's global core… 19%".

### N7 · Pages 2, 3, 12 · severity: inconsistent
Quote: p2 hero "HK$100K a year closes every protection gap"; p2 rec 1 "≈HK$100K a year until retirement (§8)"; p3
"new cover (§8) takes ≈HK$100K a year"; p12 roadmap "≈HK$100K a year"
Found: HK$100K is **year 1** (37 + 7 + 41 + 15 = 100). The average to retirement is HK$114K (`premiums_avg`, Inputs
113,600), which p10 and the appendix state correctly ("HK$100K in year 1 … HK$114K a year on average").
Fix: p2 hero "HK$100K in year 1 closes every protection gap"; rec 1 "≈HK$100K in year 1, ≈{{premiums_avg}} a year on
average until retirement"; p3 "≈HK$100K in its first year"; roadmap "≈HK$100K in year 1".

### N8 · Page 10 · severity: inconsistent
Quote: "Of fifteen ways the plan could fail, ranked by severity, likelihood and warning time"
Found: the 15 comes from Lookbua's FMEA register (`Risks & Mitigation.md`, 15 rows). The document's own register
(Figures 26 and 27) shows **14** risks (F1–F6, B1–B2, P1–P2, R1–R2, E1–E2), and a judge will count them.
Fix: "Of the protection risks we ranked by severity, likelihood and warning time, disability ranks first for both
parents", or make Figure 27 show 15.

### N9 · Page 4 · severity: inconsistent
Quote: Figure 7 "Spend less after the first death from 2056"
Found: the model applies survivor spending for `y > ALE`, i.e. **from 2057**. Figure 10 labels it "2057, Carmen
alone", the sensitivity data (`figure-data.md`) says "after 2056", and the appendix says "after Adrian's 84".
Fix: "after 2056" (or "from 2057").

### N10 · Pages 7, 12 · severity: inconsistent (new in v2)
Quote: p7 "Adrian's is 40% equity, easing to 35% in the three years before he retires"; p12 roadmap "2032–36 |
Business managers built up; Adrian to 35% equity"
Found: three years before 2037 is 2034–36. v2 widened the row to 2032–36 (Carmen's 55 = 2032, for the managers), so the
row now says Adrian's shift starts in 2032.
Fix: split the row ("2032 | Business managers built up (Carmen 55)" · "2034–36 | Adrian to 35% equity"), or word it
"2032–36 | Business managers built up from 2032; Adrian to 35% equity from 2034".

### N11 · Page 13 · severity: inconsistent
Quote: Figure 25 (stress chart) row "C. Long life + medical costs"; note "Chance the money lasts to Carmen's 89."
Found: `figure-data.md` says scenario C is "medical 8.54% flat (read the **95** column)", but the chart plots the
to-89 value (58% → 99%), which is the medical stress alone, identical to F2 in Figure 27. Its long-life figure is 26%
to 95.
Fix: label the bar "C. Medical costs 8.5% a year" (it matches F2), or plot the to-95 values and say so in the note.

### N12 · Page 5 · severity: untraceable (values confirmed)
Quote: "if every premium sat inside the HK$780K, investments alone would last in 64% of markets, not 33%; if medical
costs settle at 4.5% a year rather than 6%, the plan reaches 91%" (new in v2)
Found: both are model numbers typed into the text. Rerun: ladder step 1 with `med={}` = **63.9%**; full plan with
the long-run medical trend at 4.5% (10% in 2027, graded to 4.5% by 2036) = **90.6%**. Both correct today, but they
will not move when the model changes.
Fix: add to `export_numbers()`: `N["no_med_1_89"] = P(s89(dict(annuity=False, med={})))` and a `med45_89` key
(`med_path(1)` with `M_LR = 0.045`, restored afterwards, as the RMP_Y override already does); quote
`{{no_med_1_89}}` and `{{med45_89}}`. Also consider a key for HK$375K (p2, p5): it is on the manuscript's list of
checked hard-typed figures (rerun: 375,179), so it is allowed, but a key would keep it in step.

### N13 · Page 10 · severity: untraceable
Quote: "a shortfall of about HK$157K a year until she is 62"
Found: no working in the manuscript, `drafts/08-protection.md` or `Risks & Mitigation.md`. My closest reconstruction:
spending without the mortgage (984 − 163 = 821K) minus Carmen's after-tax pay claiming the child allowance (720 − 18
− 47.5 = 654.5K) = ≈HK$166K. That is the right size, but I cannot reproduce 157K.
Fix: Lookbua to supply the working, and add it to the manuscript's §8 notes.

### N14 · Page 6 · severity: untraceable
Quote: "a one-year master's abroad about HK$0.4M in 2032"
Found: no source. On the plan's own UK band (HK$335–555K a year at 2028/29 prices, +5% a year), a year abroad costs
HK$0.41–0.67M in 2032. HK$0.4M is the bottom of that range.
Fix: "HK$0.4–0.7M in 2032", or cite a source for 0.4M.

## Batch 2 ready

### N15 · Page 8 · severity: rounding
Quote: Figure 17 rows 0.83 + 0.97 + 0.84 → "2.63 (25%)"
Found: the displayed rows sum to 2.64. Exact: Adrian 2.0662 × 40% = 0.8265; Carmen 2.0662 × 47% = 0.9711; MPF
(1.05 + 0.62) / 2 = 0.835 → total 2.6326 = 25.1% of 10.47. Every row is right; 0.835 rounds up.
Fix: show the MPF row as 0.83 (0.835, rounded to keep the total), or add "rows rounded" to the note.

### N16 · Page 3 · severity: rounding
Quote: Figure 4 "Cash reserve | 30.5 mo." vs text "HK$2.5M in cash: 30 months of spending"
Found: 2,500,000 / 82,000 = 30.49 months.
Fix: use "30 months" in both, or "30.5" in both.

### N17 · Page 2 · severity: rounding
Quote: "The home and Carmen's business, 61% of their wealth"
Found: 16.5 / 27.19 = 60.7% of **assets**; of net worth (24.405) it is 67.6%. Page 3 says "61% of the family's assets".
Fix: "61% of their assets".

### N18 · Page 2 · severity: inconsistent (small)
Quote: "so the worst year stays above HK$546K"
Found: 546K is the floor itself, so spending reaches it but does not stay above it. Page 4 says "never falls below".
See N1 for the basis.
Fix: "never falls below" + the N1 wording.

### N19 · Page 8 · severity: rounding (wording)
Quote: "with the idle-cash and tax measures in §2 the family gains ≈HK$120K a year"
Found: 59 (fees) + 14 (idle cash) + 20 (voluntary MPF tax) = 93K; reaching ≈120K needs the card saving too (+25 =
118K). Adding the HK$18K joint-assessment check would make it 136K.
Fix: "with the cash, card and tax measures in §2".

### N20 · Page 3 · severity: rounding (confirmed; note only)
Quote: "with Ryan's pay and a mid-range bonus, before tax, it is over 55%" (new in v2)
Found: (1,050 + 225 + 720 + 300 − 984) / 2,295 = 57.1% before tax and MPF. Even at the low bonus it is 55.7%, so the
claim holds. If MPF is deducted (36K + Ryan's 15K) it is 54.9%.
Fix: optional: "about 57%, before tax and MPF".

### N21 · Page 9 · severity: untraceable (assumptions unstated)
Quote: Figure 19 "Ryan's crypto share of his wealth" (37/24, 32/20, 28/17) and "his parents match 50% of his savings
up to HK$24K a year"
Found: I reproduce every cell with: crypto held at HK$500K (no growth), MPF 180K at 5% + HK$30K a year, savings at 6%,
no pay rise and **no parental match**. For example, at 35 with 30% saving: 500 / (500 + 734 + 1,347) = 19.4%. With the
HK$24K match the share at 35 falls to ≈17%.
Fix: note "crypto held at today's value; before the parents' match".

### N22 · Page 10 vs 12 · severity: inconsistent (small)
Quote: p10 "not the HK$3.0M a forced sale might fetch"; p12 "We count only HK$3.0M … allowing a 30–40% discount on
selling a private company"
Found: p12 applies HK$3.0M to the planned, staged sale, so calling it a *forced*-sale price on p10 contradicts it.
HK$3.0M = a 40% discount on 5.0M (Inputs: "realisable 3.0–3.5M, low end"), which is consistent.
Fix: p10 "not the HK$3.0M the family could expect from a sale".

### N23 · Page 10 · severity: inconsistent (small)
Quote: sidebar "HK$100K in year 1 closes every gap: 14% of the surplus, paid only until retirement"
Found: 100 / 718 = 13.9% ✓. But the HK$15K VHIS part continues for life: from retirement it becomes the medical line
in §3.
Fix: "…; all but the medical cover stop at retirement".

### N24 · Page 4 · severity: rounding
Quote: "By 2037 the parents' investments reach about HK$17.0M in today's money, what a 2% real return needs for
HK$780K a year"
Found: `need_2037 = pv(780K, 2%, 29)` = 17.04M: 29 payments (2037–2065). To Carmen's 89 inclusive is 30 years →
HK$17.47M. The portfolio (16.97M) then falls short of the need by ≈0.5M, which weakens the sentence's point that
investments alone meet the budget.
Fix: state "29 years of HK$780K" or use 30 years (HK$17.5M) and say "about what a 2% real return needs".

### N25 · Page 6 · severity: rounding
Quote: "Set aside today at a 3% deposit rate, that needs HK$2.57M"
Found: correct at 3% flat (2,567,698). The appendix's own cash path is 3.0% falling to 2.5% by 2031; at 2.8% flat it
needs HK$2.59M (+HK$18K). The bond half of the fund earns more, so the total is fine.
Fix: none needed. Optional: "at about 3% (deposits and short bonds)".

### N26 · Page 11 · severity: rounding (note)
Quote: "on both deaths about HK$11.9M each"
Found: traced to `Pete/working-brief.md` (Cap. 73; ≈ net worth less Ryan's own 0.68M = 23.7M ÷ 2). It counts the
whole-life policies at cash value (0.42M). If both policies pay their death benefits (2.0 + 1.8M) into the estates,
each child gets ≈HK$13.5M.
Fix: none needed if the "about" stays; optional "about HK$12–13.5M each".

### N27 · Pages 5, 15 · severity: untraceable (model logic, note)
Quote: "HK$60K each into tax-deductible voluntary MPF" (p4) with "only the MPF is annuitised" and annuity premium
HK$2.31M (Inputs)
Found: the 2.31M projected MPF counts mandatory contributions only (1.05M × 1.05^11 + 36K × 14.21 = 2.31M ✓). If the
HK$60K a year of voluntary contributions sits in Adrian's MPF, his balance at 65 is ≈HK$3.2M. Annuitising "the MPF"
would then buy ≈HK$220K a year, not 161K. The model treats the voluntary money as portfolio, which is fine but unstated.
Fix: say "the MPF's mandatory balance is annuitised" or "HK$2.3M of the MPF", or note in A1.

### N28 · Page 15 · severity: rounding (source label)
Quote: A1 "Mortgage | ≈HK$0.46M still owed, cleared in 2037 | — | Case"
Found: 0.46M is derived, not in the case: HK$1.8M at 3.5% with 14 years left → HK$13,568 a month; 36 payments left in
2037, PV = HK$463K ✓. The same payment gives the "8.5% of gross income" on p3 (162.8K / 1.92M = 8.48% ✓).
Fix: source "Case; team calculation".

## Batch 3 ready

---

## Confirmed numbers, by page

| Page | Number | Type | Check |
|---|---|---|---|
| 1 | 33% → 83% | Model | ladder_1_89, ladder_5_89 |
| 2 | HK$24.4M; 10% leverage | Case / derived | 24,405,000; 2.785 / 27.19 = 10.2% |
| 2 | HK$718K; 41% | Tax tab / derived | 718,230; 718,230 / (1,920,000 − 181,770) = 41.3% |
| 2 | Fig 1 ages and risk profiles | Case | 54/49/24/16; Low–Med, Med–High, High |
| 2 | Fig 2: 11.50, 5.00, 7.97, 2.50, 0.22, (2.79), 24.41 | Case | Sums to 27.19 − 2.785 = 24.405 |
| 2 | 33% of 10,000; HK$780K; HK$375K | Model / case | ladder_1_89; case; rerun 375,179 (2056 net Flexi ÷ 1.025^30) |
| 2 | 65 and 62; under HK$25K; 83%; 97%; 40/60, 60/40; 11% → 25%; HK$2.57M | Mixed | Case; estimate; keys; allocation; ESG table; edu PV |
| 3 | Fig 3 waterfall: 1,920,000 / −181,770 / −36,000 / −984,000 / 718,230 | Tax tab | Tax recomputed by hand: Adrian 110,435 + Carmen 71,335 |
| 3 | Fig 4: 41%, 30.5 mo., 10%, 8.5%, 61% | Derived | See N16, N28, N17 |
| 3 | HK$82K a month; two parents over 60 | Case / Inputs | Allowances 145 + 140 + 2 × 55 = 395K (Adrian) |
| 3 | ≈HK$14K idle cash | Derived | 500K × (3% − 0.2%) = 14,000 |
| 3 | ≈HK$25K card | Derived | 85K × ≈30% (manuscript decision 4) |
| 3 | ≈HK$20K voluntary MPF tax | Derived | 2 × 60K × 17% = 20.4K (TVC cap 60K, working brief) |
| 3 | HK$18K joint vs separate | Tax tab | 199,770 − 181,770 |
| 3 | twelve months ≈HK$1.0M | Derived | 12 × 82K = 984K |
| 3 | Fig 5: 83%; HK$2.57M; 2028–32; ≤ 20% by 35 = 2037 | Model / derived | Ryan 24 + 11 = 35 in 2037 |
| 4 | Figure 6 ladder 33 / 43 / 60 / 82 / 83 (97) | Model | figure-data = numbers.json |
| 4 | Fig 7: 2035–39 (Carmen 58–62), 2037, 2037–39 | Derived | Ages from the case (2056: see N9) |
| 4 | HK$17.0M; 89%; 66% | Model | portfolio_2037_today, eq7_89, biz_not_sold_89 (see N24) |
| 4 | +1 point; HK$10K; HK$0.2M | Model | step_annuity, ann_typ_cost, ann_legacy_cost |
| 4 | HK$605K; HK$60K each; HK$14.1M–21.5M | Model | surplus_invest = 718,230 − 113,600; P10/P90 2037 |
| 5 | 10% → 6% by 2036; ≈4.6% a year 65–80 | Inputs / Medical tab | (63,644 / 32,542)^(1/15) = 4.57%; female 4.68% |
| 5 | HK$375K by 2056, close to half | Model | 375 / 780 = 48% |
| 5 | 64%; 91% | Model (typed) | Rerun 63.9%, 90.6% (see N12) |
| 5 | Standard ≈ a third; 83% → 97% | Medical tab / model | 10,452 / 32,542 = 32% at 65; 30% at 75 |
| 5 | HA cap HK$10,000 | Published | Methodology §1d, HA fee reform from 1 Jan 2026 |
| 5 | Essentials 40% = HK$312K | Inputs / derived | 0.4 × 780K |
| 5 | Annuities HK$161K, HK$107K | Inputs / HKMC | 2.31M × 5,800 × 12 = 160,776; 1.81M × 4,940 × 12 = 107,297; MPF projections reproduced |
| 5 | Fig 10: 430 / 470 / 586; 268 / 107 / 107; 230; 116 / 72 / 58% | Model | 312 × 1.025^13; 218.4 × 1.025^31; 218.4 × 1.025^40; (inc + 230) / ess |
| 5 | Guardrail rules ±10%, 20%, from 2039 | run_model.sim | Match code (plus a no-cut rule in the last 15 years, not stated) |
| 5 | Fig 11: 83/61/780/159; 97/89/780/159; 100/99/739/546; HK$41K | Model | numbers.json (basis: see N1) |
| 6 | HK$600K, 5%, HK$662K, HK$2.85M, HK$2.57M at 3% | Inputs / derived | 600 × 1.05²; sum of 4 years 2,851,148; PV 2,567,698 |
| 6 | UK 335–555; Canada 400–554; Singapore 224–271; HK 150–250 | figure-data / case | Methodology §3d |
| 6 | +10% sterling, +14% CAD; all under budget | Methodology §3 | Stressed highs 610 and 632 < 662 |
| 6 | HK$49,500 in 2027/28 | Published | Government announcement 20 Jun 2024: 44,500 / 47,000 / 49,500 |
| 6 | 0.5–2 points | Methodology §3 | GBP ≈0.5pp, CAD ≈2pp, SGD ≥1.3pp |
| 6 | ≈HK$1.5M returns if local | Derived | 2.57 × (1 − 250/600) = 1.50M |
| 6 | ≈HK$90K currency shortfall | Methodology §3 rec. 4 | "HK$60–90K a year" |
| 6 | ≈HK$100K per point of fee inflation | Derived | 600 × Σ1.06^k − 2,851 = 2,949 − 2,851 = 98K |
| 7 | HK$3.57M; buckets 1.00 / 2.57 / 2.07 / 2.07 | figure-data | Sum 7,700,000 = cash 2.5 + bonds 1.35 + equity 3.85 |
| 7 | 2037–2041 ladder, five years; Treasuries ≈5%, 1.5% real at 3.5% | Win / published | US 5y 5.00% on 23 Sep 2026 (Win's source) |
| 7 | Fig 16: ≥ 4.5% triggered; > 3.5%; 20% fall; 5 points | Win's rules | M5 triggered at 5.00% |
| 7 | 82% / 83% / 78% | Model | rebal_bands, rebal_target, rebal_drift |
| 8 | HK$4.4M, 1.5% → 0.15%, ≈HK$59K | Case / derived | 1.0 + 1.35 + 0.9 + 0.7 + 0.45 = 4.40M × 1.35% = 59.4K |
| 8 | Fig 17 rows; 10.47; 1.15 = 11%; 25% | Case / derived | See N15 |
| 8 | 0.54 | Published | Berg et al.; see N3 for 0.92 |
| 9 | Bitcoin −24% y/y; > 70% past falls | Snapshot | ~US$86,000, 22 Sep 2026 (Fortune) |
| 9 | HK$350K; 14%; HK$29K | Derived | 70% × 500K; 20% × 70%; 2% × 2.066M × 70% = 28.9K |
| 9 | ETF codes 3439 (bitcoin), 3009 (ether) | Published | Harvest Bitcoin Spot ETF; Bosera HashKey Ether ETF |
| 9 | HK$300K, 30% = HK$90K; HK$900; HK$24K | Case / estimates | Consistent with p10 |
| 9 | Fig 19 all cells; 74% today | Derived | See N21; 500 / 680 = 73.5% |
| 10 | 14%; HK$114K; under HK$25K | Derived / model | 100 / 718; premiums_avg |
| 10 | Disability HK$65K and HK$39K a month | Derived | 65% × 1.2M / 12; 65% × 720K / 12 |
| 10 | Term life 3.75 − 2.0 = 1.75; 2.85 − 1.8 = 1.05 | Case / derived | Carmen: 1.8 mortgage + 0.9 loan + 0.15 final = 2.85 |
| 10 | Year 1 37 + 7 + 41 + 15 = ≈100 | Derived | ✓ |
| 10 | CI 1.5M each; HK$8,000 VHIS deduction | Decision / published | Working brief deduction caps |
| 10 | Key person 5.0M | Case | Going-concern value |
| 10 | Ryan 0.5M / 0.3M ≈HK$900 | Estimate | Consistent with p9 |
| 11 | Fig 22: 59% / 9.5M; 83% / 8.1M; 83% / 12.2M; HK$7M; +4.1M; 73% | Model | property keys; 12.2 − 8.1 |
| 11 | Mortgage 3.5%; H-plan cap 3.25%; ≈HK$0.46M | Inputs / snapshot / derived | See N28 |
| 11 | Estate duty 2006; HK$1.1M; HK$11.9M | Published / derived | Working brief (Cap. 73: 500K + half residue); see N26 |
| 11 | Advance directives 31 July 2026 | Published | Cap. 651, working brief |
| 12 | 55; 58–62; 3.0M of 5.0M = 40% discount | Derived | Carmen 55 = 2032; 58–62 = 2035–39 |
| 12 | ≈HK$39K = 14 + 25; HK$59K; +22 / +17; 83% → 97% | Derived / model | step_home, step_business, switch_89 |
| 13 | Fig 27: 49/96, 58/99, 32/95, 66/100, 61/99, 83/100, 78 | Model | numbers.json (F5 = ladder_5_95 / guardswitch_95) |
| 13 | Fig 25: 83/100, 32/95, 28/92, 58/99 | figure-data | See N11 for the C label |
| 13 | HK$670K | Model | rec_lowret_typical (basis: see N1) |
| 14 | 2021; 2024; RMB 1M → 3M; RMB 150bn each way; nine cities | Published | Snapshot (HKMA) |
| 15 | A1 CPI 2.5 / 3.5; medical 10 → 6, 8.5; equities 6.0 / 17 / 4.0; ladder 4.0 / 2.5; cash 3.0 → 2.5 / 0.5; mix 40% (plan ≈50%); annuities; RMP 230K / 2045; cover 100K / 114K; Standard 2047; guardrails; 70% after 84 | Inputs / methodology | All match (see N5, N28) |
| 15 | HK$181,770; 2026–2072; 10,000 | Tax tab / model | Reproduced by hand |
