# Applied findings (HTML builder)

**Last batch taken:** numbers-findings.md **Batch 5** (N1–N33) · story-findings.md **Batch 12** (S1–S17, Pete's 1 Oct decisions).

**Where the edits live.** Pete asked for the edits in a copy: `document/proposal-v3.html` = v2 (his direct edits) + every
change below. v3 is a *built* copy, so its numbers are typed, not `{{placeholders}}`. **Still to do before the final
build:** carry v3 into the page sources and the manuscript (the v2 edits too), and add model keys for the numbers flagged
"needs a key" below. Until then, `assemble.py` would rebuild `proposal.html` without any of this.

Render of v3 (1 Oct): 15 pages, every page fits. Free space: p2 7.6 · p3 0.9 · p4 8.1 · p5 2.4 · p6 3.5 · p7 7.4 ·
p8 5.6 · p9 4.0 · p10 6.1 · p11 9.4 · p12 17.4 · p13 4.8 · p14 48.2 · p15 8.9 mm.
Note: v2 itself overflowed on p3, p5, p13 and p15. The first render of the session misreported the free space (fonts
not yet loaded); later renders were stable and match the story reviewer's figures.

## Numbers (batches 1–3)

N1 · Applied · p2, p4, p5, p13 · basis fixed (option a + real money where exact). p2 "the worst year stays above HK$546K" → "spending never falls below 70% of the budget"; p4 "leaving HK$108K … never falls below HK$546K" → "leaving Carmen HK$76K … her spending never falls below HK$382K"; Fig 11 typical/worst columns now shares of the budget (100/100/95%, 20/20/70%), note says "to Carmen's 95"; p5 "HK$546K … HK$159K" → "Carmen's spending falls no lower than HK$382K a year, 70% of her budget, rather than … HK$111K", "HK$41K" → "about 5% of it (≈HK$41K a year while both live)"; p13 "HK$670K" → "about 86% of the budget". **Needs keys:** 76K, 382K, 111K are the checker's read-only rerun values (option b: `levels × SPEND × (SURV if y > ALE else 1)`).
N2 · Applied · p10 · "that is HK$1.75M" → "she would need HK$3.75M, of which his existing policy pays HK$2.0M, leaving HK$1.75M to cover"
N3 · Applied · p8 · "about 0.92" → "0.99 between Moody's and S&P". Win's notes line 187 still says 0.92 (Win to fix).
N4 · Applied · p5 · "the HK$65K a year the parents pay today" → "about HK$65K a year of premiums (both parents' Flexi premiums at 65, at today's prices)"
N5 · Applied · p15 · A1 life-expectancy stress "Both 95" → "Carmen 95"
N6 · Applied, then superseded by S15 · p8 · "19%" → "12%" → (S15) "11%, where it is today"
N7 · Applied · p2 hero, p2 rec 1, p3, p12 · "a year" → "in year 1"; rec 1 adds "≈HK$114K a year on average until retirement"
N8 · Applied · p10 · "Of fifteen ways the plan could fail" → "Of the protection risks we ranked"
N9 · Applied · p4 Fig 7 · "from 2056" → "from 2057"
N10 · Applied · p12 · roadmap split: "2032 · Managers built up; Chloe starts work, own plan" and "2034–36 · Adrian to 35% equity"
N11 · Applied · p13 chart · `make_charts.py` label "C. Long life + medical" → "Medical 8.5% a year" (both stress charts). Charts rerun; `numbers.json` unchanged (diffed).
N12 · Deferred · p5 · 64% and 91% confirmed (63.9%, 90.6%) and kept typed in v3. **Needs keys** `no_med_1_89`, `med45_89` when carried to sources.
N13 · Deferred · p10 · HK$157K working: Lookbua to supply.
N14 · Applied · p6 · "about HK$0.4M" → "HK$0.4–0.7M"
N15 · Superseded by S15 · p8 · total is now 2.64 and the rounded rows add up; no "rows rounded" note
N16 · Applied · p3 Fig 4 · "30.5 mo." → "30 mo."
N17 · Applied (via S1) · p2 · "61% of their wealth" → "61% of the family's assets"
N18 · Applied (via N1) · p2
N19 · Applied · p8 · "idle-cash and tax measures" → "cash, card and tax measures"
N20 · Rejected · claim holds (57%, ≥55.7% at the low bonus); p3 has 0.9 mm free
N21 · Applied · p9 Fig 19 note · + "Crypto held at today's value; before the parents' match." (also covers S12's "prices held flat")
N22 · Applied · p10 · "the HK$3.0M a forced sale might fetch" → "more than the HK$3.0M the plan counts on from a sale" (p12 carries S6's prudence wording, Pete's decision)
N23 · Applied · p10 sidebar · "paid only until retirement" → "all but medical cover ends at retirement"
N24 · Applied · p4 · "what a 2% real return needs for HK$780K a year" → "close to the HK$17.5M a 2% real return needs for HK$780K a year to 89". **Needs a key** for 17.5M (pv, 30 years).
N25 · No change needed (checker agrees)
N26 · No change needed ("about" stays)
N27 · Applied · p4 · "only the MPF is annuitised" → "only the MPF's mandatory balance is annuitised"
N28 · Applied · p15 · mortgage source "Case" → "Case; derived"

## Story (batches 1–10)

S1 · Applied · p2, p3 · the business pays Carmen only while she runs it (reviewer's wording)
S2 · Applied · p4, p12 · p12 new "Why sell rather than keep the shares for dividends" (co-founder, manager's pay, ranks behind the loan, no tax either way, dividend a bonus); p4 "Without the business sale it still reaches 66%" → "With no business sale at all, it still reaches 66%". Optional dividend break-even run: not done.
S3 / S8 · Applied (S3 wording) · p10 · "so her pay stays a salary until the business is sold"; p15 A1 new row "Carmen's pay · All HK$720K as salary · Case; assumed". S8's ≈HK$30K saving sentence not used: unchecked by the number checker, and p10 had no room.
S4 · Applied · p2 quote · "…and wealth that pays nothing in retirement, are why the money falls short."
S5 · Applied (moved) · p11, not the Fig 10 note (p5 had no room): "the ≈HK$4.5M released before costs joins the portfolio, and the income floor becomes the annuities plus the cash reserve"
S6 · Applied · p12 · "the price a forced sale might fetch, so the plan does not depend on a good sale" (Pete approved)
S7 · Deferred · personal-statement career paragraphs: each member (parked)
S9–S11 · Superseded by S12
S12 · Applied in full · p2 (Fig 1 "From 18", rec 5, rec 6), p6 "After graduation", p7 heading and Fig 15, p9 Fig 18, Ryan's three pots, trim rule, match to 2037, new defence, p12 roadmap, p13 B1. Fig 19 not rerun for the 80% equity split (note says crypto held flat, before the match).
S13 + S14 + S15 · Applied (S15's combined table) · p7: green bond fund excepted from "index fund or ETF"; no separate Hong Kong holding; MPF half in an ESG fund. p8: Fig 17 by holding (BOC-Prudential 35%/37% 1.49, green bond fund 0.31, MPF ESG fund 0.84, total 2.64), note "11%, where it is today", "index-tracking where possible", "Why not higher" cut, two-rating test for equity funds and ICMA principles for green bonds, MPF route and the 20% fallback. Decision record updated: CLAUDE.md ESG line, manuscript Decisions row 6, Win's allocation tables (Adrian ESG core 10% row, Carmen 37%, 3039 rows removed). Open for people: Win confirms BOC-Prudential index, fee and retail access; existing green bond product; which MPF schemes' ESG funds are on the SFC list.

## Cuts made for fit (v2 already overflowed; the additions needed room)

- p3: Fig 5 measures "83% of markets, to Carmen's 89", "Saves 30%; cover; crypto ≤ 20%"; dropped "whose allowances the tax model claims".
- p4: "It barely moves the odds (+1 point)" → "It adds only 1 point to the odds"; dropped ", 70% of her budget" (said on p5); "below its target share" → "below target"; "when Adrian retires" → "in 2037".
- p5: h3 "What the guardrails cost, and what they buy" became a lead-in; dropped "a choice to make with their health in view", ", fixed", "protected by the rules below"; "fixed payments lose value" → "prices rise".
- p10: Fig 20 note "quotes replace them before purchase" → "quotes replace these"; dropped "not a dividend," (S3).
- p11: dropped "and the model counts that cost"; Fig 23 column widths and shorter cells ("Estate and MPF", "Property, money", "Medical care", "Staged trusts at 25, 30, 35").
- p12: roadmap cells shortened so no row wraps.
- p13: heading drops "Agreed rules answer each."; Fig 27 note one line ("Our rules" definition moved to the Fig 26 note); compliance paragraph shortened (offering-document check and the product list dropped; "regulated products only" kept).
- p15: heading "Every number traces to a stated assumption."; source cells shortened ("HK CPI 2006–25", "Family choice").

## Round 2 (1 Oct): numbers batches 4–5, story batches 11–12

Base: the story reviewer's tested copy (`proposal-v3.reviewed.html` = v3 at commit b5b5176 + S16 + S17), diffed line by
line against v3 before adoption (only the S16/S17 rows changed), then the number checker's refinements on top.
Render: 15 pages, every page fits. Changed pages: p7 7.4 · p8 5.8 · p12 17.4 mm free.

S16 · Applied · p8 · Fig 17 rows named: "Allianz Green Bond (hedged class) · Each bond checked against ICMA and Climate Bonds Initiative rules"; "Sun Life MPF Global Low Carbon Index Fund · Low-carbon ESG index; underlying fund on the SFC list" (shortened from S16 for fit); note "Counted as ESG: funds on the SFC's list of ESG funds"; green-bond test "checks every bond against the ICMA Green Bond Principles" (drops the "externally reviewed" overclaim); "at almost no extra cost" → "at a small extra cost in fees"; MPF route: each parent moves the employee half to the Sun Life scheme under the Employee Choice Arrangement. Records: Win's tables (green bond vehicle, BOC fee and Sun Life fallback, MPF fund), CLAUDE.md ESG line, manuscript Decisions row 6.
S17 · Applied · p7 · "SFC-authorised or HKEX-listed" overclaim fixed: "SFC-authorised or, for the bond ETFs, an Irish-domiciled UCITS fund, which avoids US estate tax" (later sentence deleted). p8 and p12 fee line: see N29.
N29 · Applied (the checker's more robust option) · p8 "to index funds near 0.15% saves ≈HK$59K … ≈HK$120K" → "to funds averaging about 0.5% saves ≈HK$45K … ≈HK$105K"; p12 roadmap "Saves ≈HK$45K". Reason: BOC-Prudential's full ongoing charge is above its 0.775% management + trustee fee, and the bottom-up count gives HK$46K; 45 + 14 + 25 + 20 = 104. CLAUDE.md open item and Win's value-of-advice note updated.
N30 · No change needed · the "about HK$4K" figure is not on the page
N31 · Applied · p8 · "Rows rounded." added to the Fig 17 note (rows add to 2.64; exact 2.6326). Fallback 20.2% → 20.1% in the manuscript (the page says "above 20%"). Fig 17 note tail "where it is today" → "at today's 11%" (fit).
N32 · No change needed · page claim "a small extra cost in fees" stays true
N33 · No page change · Sun Life FER ≈1.19% (not the 1.02% fee) recorded in Win's notes; open item: each parent's current MPF fund and FER (Pete or Win)

## Round 3 (1 Oct): merge fix and Fahtai's model review (reviews/model-review-fahtai.md, Batch 1)

**Merge fix.** Fahtai's merge into main (bc51065) committed unresolved conflict markers in `model/run_model.py` and
`.gitignore`, so the model could not run. Resolved (Pete approved): `run_model.py` restored exactly as at b5b5176 (the
"HEAD" side was the superseded simple version; Fahtai's own review confirms the current model and keeps its rebuild in
`model/plan_model.py`, which stays); `.gitignore` keeps both sides. `make_charts.py` rerun: `numbers.json` identical.

Each finding checked against the code before applying:
M1 · Applied · confirmed: `sim()` applies `r_eq=ST_EQ`, `r_bd=ST_BD` to every year (run_model.py line 168), not a decade. Option a (relabel, no number change): p13 heading "a low-return decade" → "low returns"; Fig 27 F3 → "Low returns every year"; Fig 26 note "In a low-return decade" → "With low returns every year"; Fig 25 tick "Low returns, every year"; A1 equities stress "4.0%, all years".
M2 · Applied · confirmed: Fig 25 B is `stressB_89` (CPI 3.5% + medical stress), F1 is CPI alone. Fig 25 tick "Inflation + medical"; scenario name in `make_charts.py` "B. Inflation + medical costs".
M3 · Applied · confirmed: `pot += biz` once in 2039 (line 199), HK$3.0M unindexed ≈ HK$2.2M today. A1 new row "Business sale · HK$3.0M in 2039, one payment · Not sold · Case, less 40%".
M4 · Applied · confirmed: no cash rate in the simulation; 3% is the education discount. A1 cash row stress "0.5%" → "—", source "HIBOR; Fed" → "Education fund".
Fit on p15: "Flexi for life" → "No review"; new-cover cell "≈HK$100K year 1; HK$114K average". Render: 15 pages, all fit (p13 4.8, p15 6.6 mm free).

## Round 4 (1 Oct): v3 carried into the page sources, the manuscript and the model

The page sources now hold every v2 and v3 edit, with model numbers as `{{placeholders}}`; `proposal.html` (built by
`assemble.py`) is the document again, and `build/proposal.pdf` is the file to submit. Check: the new sources, filled,
reproduce v3 line for line except two sentences changed on purpose (below). Render: 15 pages, every page fits.

- New keys in `export_numbers()` (all match the number checker's reruns; no existing number changed):
  `ann_w1_with_real` HK$382K, `ann_w1_without_real` HK$76K, `*_worst5_real` (HK$111K, HK$382K), Figure 11 shares
  `*_typical_pct` / `*_worst5_pct` (100/100/95%, 20/20/70%), `rec_*_typical_pct` (86% low returns), `guard_cost_pct` 5%,
  `no_med_1_89` 64%, `med45_89` 91%. Typed in v3 → keys now: p2 33%, HK$114K; p4 +1 point, HK$76K, HK$382K; p5 64%, 33%,
  91%, Figure 11, 5%, HK$382K, 70%, HK$111K; p13 86%.
- N24 revisited: the model simulates 29 years of retirement spending (2037–2065; `sim` stops at the start of Carmen's 89),
  so `need_2037` = HK$17.0M matches it and v3's typed HK$17.5M (30 years) did not. p4 now reads "what a 2% real return
  needs to pay HK$780K a year until Carmen's 89" (the checker's first option).
- p4 "It adds only 1 point to the odds" → "It barely moves the odds ({{step_annuity}} point)" so the number is a key.
  p4 now 3.2 mm free.
- A bug caught in review: re-keying by value put `{{guardswitch_89}}` (100%) into Figure 11's typical-spending column;
  fixed with the `*_typical_pct` keys.
- Manuscript: every page's wording regenerated from its page source (with placeholders), keeping the header lines and
  the real notes (§3 decisions and checks, p8 fee and ESG notes, p13 stress notes, p14 career brief and WMC check, p15
  A1 detail). The old manuscript had drifted beyond v3 (e.g. a HK$2.5M key-person stake, five recommendations).
  `fill.py manuscript.md`: 103 placeholders, none unknown. Page map free space updated.
- CLAUDE.md: the annuity decision line now quotes HK$382K vs HK$76K in today's money.
- `proposal-v2.html` (document/ and the repo root) and `proposal-v3.html` are now superseded copies; not deleted (Pete to
  decide). Reviewers should review `document/proposal.html` from now on.

## Round 5 (1 Oct): story batch 14 (Pete's decisions on batch 13: S19 approved; keep v2 and v3)

**Last batch taken:** story-findings.md **Batch 14** (S18 is review-only; S19 applied). Numbers: Batch 5 (unchanged).

S18 · No action (review of a teammate's PowerPoint `Fin Plan.pdf`, 6–9 pt text and a university email in its metadata). The file is untracked in the repo root and was **not committed**; it must never be submitted or built from.
S19 · Applied (`s19.patch`, `git apply --check` clean) · p7 restructured: "From today to the target", new Figure 14 "What each parent buys" (eight named holdings, Adrian/Carmen %), "Own the market, not chosen stocks" (Bessembinder 2018), shortened "Why not all Treasuries", Figure 15 rules (HK-inflation row dropped; §11 F1 still answers it). Allocation chart and bucket table removed; figures 16–27 renumbered 15–26; p9 "(Figure 18)" and Ryan's pot "the same world index ETF as his parents (IWDA)".
  Checked before applying: both portfolios sum to 100% (40/60, 60/40); Bessembinder and MSCI World facts; ESG fallback ≈21.7% = (1.49 + 0.31 + 0.476) / 10.47; no placeholders in the replaced region; every in-text figure reference points to the right figure.
  Builder corrections on top: (1) "HK$3.9M … sits in equity funds charging about 1.5%" → "is in equities, most of it in funds charging about 1.5%" (HK$0.8M of it is listed stocks and REITs, which carry no fund fee); (2) Figure 14 note "the rest are SFC-authorised" → "Treasury notes held directly; the rest SFC-authorised" (a directly held bond is not an authorised fund), shortened to fit.
  Render: 15 pages, all fit (p7 5.3 mm free).
  Records: manuscript p7 regenerated with an S19 note, Layout lines and the Charts table renumbered (`allocation-half.png` still drawn, not placed); Win's tables (IWDA replaces the Nasdaq-100 slice and REITs; 3450 not 3433; Carmen's AGGU 20% so she sums to 100; Ryan's pots); CLAUDE.md vehicles line and the keep-v2/v3 decision. `[CHECK: Win]` 3450's name and fee, IWDA's ongoing charge. Pete tells Win.

## Round 6 (2 Oct, deadline day): story batches 15–16 (S20–S29), applied by the story session at Pete's request

**Last batch taken:** story-findings.md **Batch 16**. Pete asked the story session to apply its own findings (builder
role for this round), keeping 15 pages and the "Built to Last" spine. Render: 15 pages, every page fits
(p2 7.6 · p3 0.9 · p4 3.2 · p5 2.4 · p9 4.0 · p10 1.3 · p12 6.9 · p13 5.7 · p14 33.6 · p15 1.3 mm free).

S20 · Applied · `Fin Plan.pdf` (PowerPoint, university email in its metadata) is **not** to be submitted. Its text that
the sources lacked is carried in: p10 "5.0M full, company pays"; p12 heading "Close every gap within the first year;
after that, dates and events trigger each decision."; p14 career paragraphs (S21). The Chrome cover keeps its date and
contents. The PowerPoint's dropped contents list is not followed.
S21 · Applied in part · p14:
- Pete's and Fahtai's paragraphs are in (Fahtai: "casflow" → "cash-flow", label "Fahtai.").
- Lookbua's is the reviewer's edit of his draft, which keeps his goal and adds the Connect link.
  **Needs Lookbua's OK.** His original is quoted in the manuscript.
- **Win's is still a placeholder (deferred: Win).**
S22 · Applied · p9 · "His HK$180K MPF moves to the lowest-fee global equity index fund in his scheme; a set monthly
contribution…" (fit: "such as a flat deposit," cut).
S23 · Applied · p7 · "Adrian's Treasuries pay his first five years of retirement" → "Adrian's Treasury notes mature one
a year from 2037 to 2041, a known sum each year whatever markets do".
S24 · Applied · p4 · "the money runs out without it, leaving Carmen {{ann_w1_without_real}} … never falls below
{{ann_w1_with_real}}, the rules' floor"; p5 "…{{guardswitch_worst5_pct}} of her budget; without them it falls to
guaranteed income alone, {{fixswitch_worst5_real}}". Fit: "worst one simulation in twenty" → "worst one in twenty",
"agreed next steps" → "agreed steps", "cannot be reversed" → "is irreversible", "about … typical spending" →
"≈… spending".
S25 · Applied · p4 · Figure 7 "Plan for one person's spending · after the first death · agreed now, in writing" (no
2057). "Why these four": "The first plans for one person at 70% of the couple's budget (the OECD scale implies
two-thirds); the other three use assets the family owns, at the cost of a smaller legacy." This replaces the no-sale
66% sentence, which is still on p12 and p13.
S26 · Applied, with a model change · p13:
- New key in `export_numbers()`: Adrian's job ends at 60. His after-tax pay and both sides of his MPF stop for
  2032–36; nothing else changes. `adrian60_89` = **30%** fixed spending, `rec_adrian60_89` = **83%** with the rules.
  `numbers.json` diff: only these two keys added, nothing changed.
- Register row F6 "Adrian's job ends at 60 · 30% · 83% · Reserve; guardrails; full review".
- Old F6 (base case) dropped: Figure 24 shows it. B2 dropped: p7's Figure 15 note shows it.
- P3 "Care needs late in life · Costs outside the budget · Home equity: downsize or sell".
- F2 defence "Tier review at 75; terms checked".
- Matrix: F6 high/medium, P3 medium/high. Figure 25 note shortened for fit.
S27 · Applied · p12 · Month 12 "First family meeting: charter, Ryan's plan, one-person budget · {{step_survivor}}
points" (+9); "investment policy signed"; typed "66%" → `{{biz_not_sold_89}}`.
S28 · Applied · p10 "The whole-life policies (HK$420K cash value) stay in force; home cover is checked for owners'
liability."; p3 "but the plan counts only the low bonus and invests any more."
S29 · Applied in part · p2 "Adrian 40% equity with a Treasury ladder, Carmen 60% ESG-led"; p15 A1 model mix "40% equity
(the plan holds ≈50%; more adds legacy, not security) · Team model, §5". Not done: Figure 6 label (redraw for a cosmetic
change) and the blue in Figures 8/24.
Unsure items (Fig 21 59% vs ladder; HKMC lump-sum purposes; Connect marketing rules) left for the number checker.

### Round 6b (2 Oct): the job-loss stress woven into the story; Figure 26 restructured (Pete asked)
Pete's points: the new stress sat only in the register; Figure 26 was unclear and repeated p10.
- **Model** · `run_model.job_loss()` is shared by the number keys and the chart. Charts rerun; `numbers.json` is
  unchanged.
- **Figure 24** · the "Medical 8.5% a year" bar (the F4 row shows it) is replaced by "Job ends at 60" (30% / 83%).
- **p13 heading** · was "Before retirement the largest risk is lost income; after it, low returns and inflation.", which
  repeated p10. Now: "A lost job is the hardest test; the spending rules hold the plan at {{rec_adrian60_89}} or better."
  This is true of every measured row.
- **Figure 26**:
  - title: "Every risk has a named defence; six are measured in the model";
  - two group rows: "Measured: chance the money lasts to Carmen's 89, worst first" and "Managed by process: what each
    risk threatens";
  - measured rows renumbered worst first: F1 job, F2 low returns, F3 inflation, F4 medical, F5 Carmen to 95, F6
    business;
  - P1 cell "Highest ranked" → "Income stops" (a pointer to §8, not a repeat);
  - "Irreversible choices" dropped (p4 says it), and late-life care renumbered P2;
  - the compliance paragraph became rows: R1 defence "Licensed channels; crypto test", new E3 "Conflicts of interest ·
    Biased advice · Fees disclosed; no commission";
  - the matrix follows the new codes.
- **Figure 25 note** · now carries the test's caveat: "The lost-job test is harsh: no pay from 60 to 65, no severance."
  The low-returns 86% detail moved to the manuscript notes.
- **p10** · "…as they rise with age; wills and powers of attorney cost under HK$25K once (§9)." (already on p2 and p12) →
  "A lost job cannot be insured: at 54, in a regional role exposed to restructuring and technology change, Adrian's pay
  is the largest risk no policy covers, so §11 tests it."
- **p2 rec 04** · "…and the plan still reaches {{rec_adrian60_89}} if Adrian's job ends at 60 (§3, §11)."
- **Render** · 15 pages, all fit (p2 7.6 · p10 0.6 · p13 3.3 mm free).
  - Note: `render.py` can misreport when a chart loads late. One run showed p6 at 34.5 mm and p13 "fits"; the true p13
    was 4.2 mm over.
  - Trust a run where p6 reads 3.5 mm and p11 9.4 mm.
- **Manuscript** · p2, p10 and p13 synced; p13 notes record the reasons and the dropped rows.

### Round 6c (2 Oct): §8 and §11 given separate lenses (Pete: they still carried the same idea)
**§8 (p10): what could happen to the family, and what insurance pays.** The intro's job sentence becomes the boundary:
"Two risks stay uninsured: long-term care, for which the home's equity is the reserve (§9), and a lost job, which §11
tests."

**§11 (p13): the plan's assumptions and the advice itself** (the case's §11 list). Changes:
- Heading: "The riskiest assumption is Adrian working to 65; if he cannot, the rules still hold the plan at
  {{rec_adrian60_89}}."
- The reason sits here, under the figures: "Why test a lost job. At 54, in a regional role open to restructuring and the
  technology disruption the case names, with part of his pay a bonus, Adrian has the plan's least certain income; no
  policy covers it."
- Figure 25 note: "F1 is harsh by design: no pay from 60 to 65, no severance."
- Register groups renamed "The plan's assumptions, tested: …" and "People, products and our advice: …".
- P1 and P2 removed (and from the matrix); legend adds "Protection risks: §8."
- Fit: Figure 24's caption folded into its title "Lasts to Carmen's 89, under stress".

**Render:** 15 pages, all fit, from a run where every image loaded (p6 3.5, p11 9.4; p10 1.3, p13 1.4 mm free).
Manuscript synced.

### Round 6d (2 Oct): p10 A–E made parallel (Pete asked why C, D, E shared a paragraph)
C, D and E had been run together to save space. Changes:
- Each now has its own paragraph, like A and B.
- D and E lead-ins end with a full stop, like A–C (were colons).
- Room came from the heading, which drops to two lines: "Before retirement, the largest gap is income, not
  death: …" → "The largest gap is income, not death: neither parent could replace their salary if disabled." The body says
  the cover runs to retirement.

Render: 15 pages, all fit, from a run where every image loaded (p10 1.1 mm free). Manuscript synced.

### Round 6e (2 Oct): p3 strengths and risks split (Pete asked)
- "Strong, liquid and lightly borrowed." and "Two risks sit behind the strength." each get a paragraph, matching the heading's
  two halves.
- Fit:
  - Figure 3 caption "Parents only, low bonus. Source: case; team tax model (2026/27, separate assessment)." → "Parents
    only, low bonus; case and team tax model." Separate assessment is in the text; 2026/27 is in A2.
  - "Debt is 10% of assets, and the mortgage costs about 8.5%" → "Debt is 10% of assets; the mortgage costs 8.5%".
- Render: all fit (p3 4.0 mm free). Manuscript synced.

### Round 6f (2 Oct): run-in lead-ins that answer separate case questions get their own paragraphs (Pete: split all)
Each "X: text" run-in became a paragraph "X. Text":
- p6: "Why not an education savings policy";
- p8: "Selection criteria";
- p9: "Implementation, in order of preference";
- p11: "Ownership", "Another district";
- p12: "Family governance", "Legacy with purpose".

Kept as run-ins on purpose:
- p5's four medical-premium steps (one topic);
- p12's "Why sell rather than keep the shares for dividends" (part of the business paragraph).

Fit trims:
- p9: "would cost Ryan about HK$350K" → "would cost Ryan HK$350K"; "to about HK$29K" → "to ≈HK$29K".
- p11: "The HK$7M replacement need not be in Tai Kok Tsui; a cheaper district buys more space, or releases more money." →
  "The HK$7M flat need not be in Tai Kok Tsui; elsewhere buys more space or cash."

Render: 15 pages, all fit, two runs agree (p6 1.1 · p8 3.4 · p9 1.6 · p11 4.6 · p12 2.1 mm free). Manuscript synced.

### Round 6g (2 Oct): Chloe gets Ryan's framework with her own settings; Singapore's grant is an option, not the path
Pete asked whether Ryan's plan truly fits Chloe, and why Singapore was emphasised. Singapore is one of the case's four
destinations; the Tuition Grant (a three-year work bond) was only our suggestion.
- **p6 costs:** "Singapore costs HK$224–271K with the Tuition Grant, which requires three years' work in Singapore after graduation."
  → "Singapore costs HK$332–400K, or HK$224–271K if she takes the Tuition Grant, which ties her to three years' work
  there." The ranges are from make_charts EDU.
- **p6 "After graduation":** was "follows Ryan's plan … with the Singapore grant, that plan starts in Singapore". Now
  "Chloe gets Ryan's framework (§7): three pots, cover bought young and the parents' match to 2037. The settings are her
  own: equity from her risk profile at 18, no crypto unless that profile allows it, and a savings rate set on her first
  salary. If she first works abroad, MPF does not apply, so her retirement saving starts in that country's scheme."
- **Fit trims:**
  - Figure 12 source → "Source: fee schedules (A3); team FX analysis."
  - A3 "fee schedules" → "university fee schedules, Statistics Canada, IRCC, Save the Student".
  - "If Chloe studies locally, about HK$1.5M returns to the retirement portfolio." → "A local degree returns about
    HK$1.5M to retirement."
- Figure 12 keeps both Singapore bars.

Render: 15 pages, all fit, two runs agree (p6 1.7, p15 1.3 mm free). Manuscript synced.
