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
