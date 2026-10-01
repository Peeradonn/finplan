# Story findings

**Reviewed:** `document/proposal-v2.html` (built copy with Pete's direct edits, uncommitted, 30 Sep), against the case
(`Primary Info/Award2026Case20260919.pdf`) and the model (`model/run_model.py`, `model/build_xlsx.py`).
Numbers are not checked here (see `numbers-findings.md`; the HK$546K / worst-1%-vs-1-in-20 issue is its N1, not repeated).

---

### S1 · Pages 2 and 3 · severity: high
Quote (p2): "The home and Carmen's business, 61% of their wealth, pay no income until sold or borrowed against."
Quote (p3): "the home and Carmen's business are 61% of the family's assets, and neither pays an income until it is sold or
borrowed against."
Issue: Wrong about the business, and a judge will notice. The case's income table lists "Carmen's annual salary /
dividend from business: 720,000", and the model counts that HK$720K (after tax and MPF) every year until she retires at
62 (`run_model.py` line 178: `CARMEN_NET ... if y < RETC`). The business already provides income. What is true is
narrower: it pays only while Carmen runs it. After 2039 the model gives it no income, only the HK$3.0M sale. Page 2
is the first page a judge reads closely, and this is the second of the "two findings" the plan is built on.
Fix (p2, same length): "The home pays nothing until it is sold or borrowed against, and the business pays Carmen only
while she runs it; together they are 61% of the family's assets."
Fix (p3): "...61% of the family's assets. The home pays nothing until it is sold or borrowed against, and the business
pays Carmen's HK$720K only while she works in it."

### S2 · Pages 4 and 12 (§3, §9) · severity: high
Quote (p12): "a staged sale between 58 and 62, with no capital gains tax. We count only HK$3.0M of her interest's
HK$5.0M going-concern value"
Quote (p4): "Without the business sale it still reaches 66%."
Issue: The proposal never says why Carmen should sell rather than keep her shares and pay herself dividends in
retirement. That is the obvious question (Pete asked it), and case concern 7 asks "whether Carmen should gradually
restructure, reduce, or monetize part of her business interest". The business section has no defence paragraph: no
rejected alternative, no trade-off, nothing on what happens if the sale fails. Two further gaps:
- The model's "not sold" case (66%) sets the business to **zero** after 2039, with no sale and no dividends
  (`biz_not_sold_89 = s89(full, biz=0)`). It is the worst case, not the "keep and take dividends" option, and the
  text reads as if it were the alternative.
- The case calls Carmen a **co-founder**. The proposal never mentions the co-founder, the natural buyer in a buy-sell
  agreement and a staged sale.
The reasons to sell, all from the case, so no new facts are needed:
1. Most of the HK$720K is pay for running the company as managing director. After she retires a manager must be paid;
   what is left as a dividend depends on profit, which the case does not give, so no dividend can be planned on.
2. Key-person risk: the case asks about it. A firm built around its founder may earn less without her.
3. Dividends are discretionary and variable, rank behind the HK$900K business loan (which Carmen guarantees, p10), and
   are the opposite of the fixed floor that suits Adrian's low-to-medium risk profile.
4. Concentration: 20% of net worth in one private company in one sector, in the same economy as the home and both
   incomes (the §5 argument for a global core applies here too).
5. Succession: neither child works in the business, and an unlisted stake is hard to split fairly between Ryan and Chloe.
Hong Kong taxes neither dividends nor capital gains, so tax does not decide it either way. Say so, because a judge may
assume it does.
Fix (p12, replaces "We count only HK$3.0M ... private company."; about 75 words against about 25; manuscript recorded
≈33mm spare on p12, recheck on the v2 layout):
"**Why sell rather than keep the shares for dividends.** Most of the HK$720K Carmen draws is pay for running the
company. Once a manager is paid, the dividend left is uncertain, depends on a firm built around her, and ranks behind
the business loan. A sale to her co-founder and managers turns it into money the plan can count on. We count only
HK$3.0M of the HK$5.0M value, allowing 30–40% for selling a private company; if no sale happens the plan still
reaches 66%, and any dividend is a bonus."
Model (optional, builder): a "keep, dividend of HK$X a year from 2039" sensitivity, or the break-even dividend at
which keeping matches the sale, would turn this from an argument into a number. As a rough guide, HK$3.0M in the
portfolio supports about HK$120–150K a year, so keeping wins only if a reliable dividend after a manager's pay beats
that. Add it as a new key in `export_numbers()` if used.

### S3 · Page 10 (§8 A) · severity: medium
Quote: "Carmen's cover is written on her salary, so it must be in place before any change to how she draws income from
the business."
Issue: This refers to a recommendation that is no longer in the proposal. The earlier draft (`drafts/08-protection.md`)
had a salary-to-dividend restructuring; the body no longer recommends one. A judge reads it as a hint at a change the
plan never makes. It connects to S2: if the plan keeps her pay as salary until the sale, say so.
Fix: "Carmen's cover is written on her salary, so her pay stays a salary, not a dividend, until the business is sold."
Or cut the sentence.

## Batch 1 ready

### S4 · Page 2 · severity: medium
Quote: "Medical premiums the budget leaves out, not markets, are why the money falls short." (pull quote) against
"Two findings explain why. The home and Carmen's business ... And medical premiums ..." (body)
Issue: The pull quote names one cause and the paragraph under it names two. The illiquid-assets finding is what three
of the four decisions answer (business sale, home, and, less directly, annuities), so the quote undersells the plan's
own logic.
Fix: "Medical premiums the budget leaves out, and wealth that pays nothing in retirement, are why the money falls
short." Or keep the quote and make the medical premiums the first of the two findings, so the quote leads into it.

### S5 · Pages 5 and 11 · severity: medium
Quote (p5, Figure 10): "Reverse mortgage (§9) HK$230K ... with the reverse mortgage they cover every essential in 2039"
Quote (p11): "Downsizing is the stronger financial answer; the reverse mortgage buys the right to stay ... we set the
decision for 2037"
Issue: The income-floor story rests on the reverse mortgage, yet §9 says downsizing is financially stronger and leaves
the choice open. A judge will ask what the floor looks like if they downsize. The floor then comes from annuities plus a
portfolio that is HK$4.5M larger, not from a lifelong payment.
Fix: add to the Figure 10 note: "If the family downsizes instead, the released HK$4.5M joins the portfolio; the floor
is then the annuities plus the cash reserve." (Check the HK$4.5M with the number checker: 11.5M less 7M, before costs.)

### S6 · Pages 10 and 12 · severity: low
Quote (p10): "realises the full HK$5.0M going-concern value of her interest, not the HK$3.0M a forced sale might fetch"
Quote (p12): "We count only HK$3.0M of her interest's HK$5.0M going-concern value, allowing a 30–40% discount"
Issue: Page 10 calls HK$3.0M the forced-sale price; page 12 then plans a staged, unforced sale at the same HK$3.0M. A
careful reader asks why a planned sale fetches no more than a forced one. The answer is prudence, but the text does not
say so.
Fix (p12): "...we count only HK$3.0M, the price a forced sale might fetch, so the plan does not depend on a good sale."
(Folds into the S2 wording.)

### S7 · Page 14 · severity: high (known, open item)
Quote: "Placeholder of about seventy words for the career paragraph..." (four times)
Issue: The personal statement is 15 points and a quarter of its page is placeholder. Listed as parked in CLAUDE.md;
repeated here so it is not lost.
Fix: each member writes ~70 words. Suggest that one of them (Carmen's business is the natural hook) ties the member's
goal to advising owner-managers on succession, which uses S2.

## Batch 2 ready

---

## What works well (keep)
- **Three aims, six recommendations** on page 2 are a clear spine: each aim has two numbered actions with a section
  reference, and every body section maps to one aim. Nothing belongs to no pillar.
- The ladder of four decisions is described the same way, in the same order, on pages 2, 4 and 12.
- The annuity framed as insurance, not return (p4), is the plan's most original argument and is well defended.
- Every section from §3 to §9 now has a "why not" paragraph, except the business (S2).

## Unsure
- Whether Carmen's HK$720K is mostly salary or mostly dividend today. The case says "salary / dividend" and page 10
  assumes salary (disability cover). If it is mostly dividend, the disability cover sizing in Figure 20 needs a check,
  because insurers cover earned income, not dividends.
- Whether "her interest" (p10, p12) is right: the case gives HK$5.0M as "Carmen's business value" with no stake stated,
  though she is a co-founder (numbers reviewer took it as the family's asset at 100%).

---

### S8 · Pages 3, 10, 15 · severity: medium (resolves the "Unsure" item on Carmen's pay; Pete asked for a choice)
Evidence in `Primary Info/`:
- Case income table: "Carmen's annual salary / dividend from business: 720,000". Workshop slide 11: "Carmen — salary
  and dividends", plus "Profits tax on Carmen's business is excluded". So a judge may expect the split to be named.
- She is the company's "managing director" and has "employer-provided group medical coverage". Both mean she is on the
  company's payroll, so at least part of the HK$720K is salary. Her HK$620K MPF balance fits that, but does not prove it,
  because the self-employed also contribute.
- The case gives no split, and no profit figure for the company.
What the model does: all HK$720K as salary (`build_xlsx.py` input "case; treated as all salary"). Carmen's salaries
tax is HK$71,335, inside the HK$181,770 couple total.
The alternative, costed: HK$360K salary (HK$30K a month, which still hits the MPF ceiling, so MPF is unchanged) and
HK$360K dividend. Her salaries tax falls to about HK$11K (saving ≈HK$60K). The company pays profits tax of 8.25% on
the HK$360K it can no longer deduct (≈HK$30K). Net gain ≈HK$30K a year. Hong Kong does not tax dividends.
Recommendation: **keep all salary, and state it as an assumption.** Reasons:
1. It is the cautious choice: salary is taxed more, so the plan does not count on a saving.
2. It protects her income. Disability cover insures earned income only. On HK$360K of salary her benefit would halve,
   from HK$39K to about HK$19.5K a month, to save ≈HK$30K a year. Disability is ranked the family's top risk (§8).
3. No rerun: tax, surplus, savings rate and every model number stay as they are, two days before the deadline.
Fix (p15, A1, new row): "Carmen's pay | All HK$720K as salary | — | Case: managing director on the payroll".
Fix (p10, replaces the S3 sentence): "Carmen's cover is written on her HK$720K salary. Paying part as a dividend
would save about HK$30K of tax a year but halve her disability cover, so her pay stays a salary until the business is
sold."
(Check the ≈HK$30K and ≈HK$60K with the number checker. They assume separate assessment, her current deductions and
company profits under HK$2M, so the 8.25% first tier applies.)

## Batch 3 ready

---

### S9 · Pages 2 and 9 (§7, Ryan) · severity: medium-high
Quote (p9): "New savings go to a global equity portfolio, and none to crypto while he is above his glide path, so his
crypto share falls without any forced selling (Figure 19)."
Quote (p2): "Ryan's crypto on a glide path"
Issue: Pete read this as "keeps his crypto" versus "invests in global equity" and asked which one it is. The answer
is both: what he holds stays, and new money goes to equity. A judge will be just as confused. Four further gaps:
1. **"Without any forced selling" reads as "never sell".** Win's rules (`Updated_Investment_Win.md` §3, D2) include
   "a rally puts him >10 points above the path → trim back to the path". That rule was dropped from the page. Without
   it the glide path depends on the price: Figure 19 holds his crypto at a flat HK$500K, so if bitcoin doubles, his
   share goes back above 50% and nothing brings it down. With D2 the 20% becomes a real cap, which answers the case's
   "risk-controlled structure" and "allocation limits".
2. **The rejected alternative is "sell it all", not "trim now".** The defence ("Selling Ryan's holdings would ignore
   his stated conviction") answers the extreme, not the middle option a judge will think of: trim to 20% today.
   Hong Kong has no capital gains tax, so trimming costs only fees. The real reasons not to trim now are: it is his
   money, it is about 2% of the family's net worth so the parents' plan does not depend on it, and a forced sale
   invites him to rebuy outside regulated channels. Say that.
3. **Figure 19 assumes crypto prices stay flat.** Say so in the note.
4. **The parents' 50% match (up to HK$24K a year) is not in the model and has no end date.** It is small against the
   ≈HK$605K invested each year, but it is money out of the parents' plan. End it when Adrian retires in 2037, when
   Ryan is 35 and the glide path ends.
Fix (p9, replaces the quoted sentence; about the same length):
"His HK$500K of digital assets stays, but is capped by a glide path to 20% of his wealth by 35. All new savings go to
a global equity portfolio, so the share falls without selling; if a rally lifts it more than 10 points above the path,
he trims back (Figure 19, prices held flat)."
Fix (p9 defence, replaces "Selling Ryan's holdings would ignore his stated conviction and his high risk profile;"):
"Selling now, or trimming to 20% at once, would override his conviction on money that is his own and about 2% of the
family's wealth, and could push him to unregulated channels;"
Fix (p9, Ryan's plan): "...his parents match 50% of his savings up to HK$24K a year until 2037."
Fix (p2): "Ryan's crypto capped on a glide path to 20% by 35".

### S10 · Pages 6, 9, 12 (Chloe after graduation) · severity: medium
Issue: The plan treats Chloe only as a cost: her degree is funded, then she disappears in 2032. The pillar "Give every
voice a place" gives Ryan a full plan and Chloe only a university choice. Case concern 6 ("financial responsibility
between parents and children") covers both children, and a judge will notice the asymmetry. She graduates at 22,
when Adrian is 60, five years before he retires, so her first working years fall inside this plan. What is missing:
- Her own start: cash buffer, saving habit, first cover, MPF. The same template as Ryan's.
- Her own risk profile when she turns 18 or starts work (§11 E1 already promises "one risk profile per person").
- Page 6 names the Singapore Tuition Grant's three-year work bond in Singapore, but does not say what it means for her
  plan: her first job and savings would be in Singapore dollars.
- Whether the parental match applies to her (and for how long; see S9 point 4).
No model change is needed if the match ends in 2037 and the household budget is unchanged to retirement (the model
keeps HK$984K a year of spending to 2037 and does not cut it when Chloe graduates, which is cautious).
Fix (p9, one sentence after "Ryan's own plan", retitled "The children's own plans" if the heading fits):
"Chloe follows the same plan when she starts work in 2032: her own risk profile, three months' cash, a 30% saving
habit, her own cover, and the same parental match to 2037."
Fix (p12 roadmap, fold into the 2032–36 row): "2032 | Chloe starts work: her own plan, as Ryan's".
Optional (p6, the Singapore sentence): "...requires three years' work in Singapore after graduation, which her own
plan (§7) would then start in Singapore dollars."

## Batch 4 ready

---

### S11 · Page 9 (Ryan's own plan) · severity: medium-high (Pete's question)
Quote: "New savings go to a global equity portfolio"
Issue: Every new dollar Ryan saves goes into equity, on top of a holding that is about 74% crypto today. Four problems
a judge can raise:
1. **His whole portfolio is risky assets.** Apart from three months' cash, everything he owns is crypto or equity. A
   2022-type year (crypto −65%, global equity −18%) would take about half his wealth. The family's objective is
   "moderate growth with controlled downside", and §5 argues for one portfolio per owner. Ryan's is the only one with
   no bonds.
2. **It ignores what he is saving for.** The case says he "wishes to build his own financial independence". For a
   24-year-old in Hong Kong that usually means moving out or a flat deposit, and perhaps further study, all within 5–10
   years. Money needed in 5–10 years is the same case §4 makes for Chloe's fund: it cannot wait out a market fall. The
   plan never asks what his goals are.
3. **The family's own rules do not work for him.** Figure 16 says "rebalance by selling bonds; never sell equities" after
   a 20% fall. With no bonds he has nothing to rebalance from, except crypto or new savings.
4. **Voluntary MPF locks his money to 65.** At his tax rate (10% top band) the deduction saves at most about HK$6K a
   year, against money he may need for independence much sooner.
What does justify a high equity share, and should be kept: a 40-year horizon, a "High" risk profile, and his salary,
which acts like a large bond holding (standard lifecycle funds hold about 90% equity at 24). So the fix is not "make
him moderate". It is to give him a goal pot and let the rest be equity.
Fix (p9, replaces "New savings go to a global equity portfolio, and none to crypto while he is above his glide path"):
"His savings go into three pots: three months' cash (his tokenised money-market fund counts); money for goals within ten
years, such as a flat deposit, in deposits and short bonds; and the rest, for retirement, in a global equity index fund,
about 80% of the total. None goes to crypto while he is above his glide path"
The same sentence can also carry the S9 wording. Drop "starts voluntary MPF contributions", or keep it only for money
he will not need before 65.
Why this suits him: it keeps his equity share high and his crypto untouched, uses the tokenisation he already likes for
cash, and gives the family rules something to rebalance from.
Model: Figure 19 changes slightly. Bonds grow more slowly, so the crypto share at 35 rises by about a point
(estimated, not computed). The number checker should rerun Figure 19 with an 80/20 split of new savings.

## Batch 5 ready

---

### S12 · Pages 2, 6, 7, 9, 12, 13 · severity: medium-high · TESTED WORDING (Pete approved the direction)
Supersedes the wording in S9, S10 and S11. Covers: Ryan's three pots and the crypto trim rule, Chloe's plan and risk
profile, and the slogan. Pete asked for "one family, three portfolios" to be reconsidered. "Three portfolios" leaves
Chloe out, and clashes with "Five buckets" (Figure 15) and "Four risk appetites" (p13 B1). The new line is **"One
family policy, a portfolio for each person"**, which echoes "Give every voice a place" and counts Chloe: her portfolio
is the education fund now, and her own plan from her first job.
Fit: applied to a scratchpad copy of `proposal-v2.html` and rendered. p2 20.8 mm free · p6 3.5 · p7 7.4 · p9 4.0 ·
p12 21.0. p13 is unchanged (its 15.3 mm overflow, like p3, p5 and p15, was already in v2 before these edits).
Page PNGs checked for p6 and p9. Apply to `proposal-v2.html` or straight into the page sources, and mirror in the
manuscript.

| Page | Old | New |
|---|---|---|
| 2, Fig 1 | Chloe, 16 · "—" | Chloe, 16 · "From 18" |
| 2, rec 5 | "**One family policy, three portfolios**: … Ryan's crypto on a glide path (§5–§7)." | "**One family policy, a portfolio for each person**: … Ryan mainly equity, his crypto capped on a glide path (§5–§7)." |
| 2, rec 6 | "…so she chooses freely (§4)." | "…so she chooses freely; her own plan starts with her first job (§4)." |
| 6, new paragraph after Contingencies | — | "**After graduation.** Chloe's own risk profile is set at 18. When she starts work in 2032 she follows Ryan's plan (§7), with the same parental match to 2037; with the Singapore grant, that plan starts in Singapore." |
| 7, heading | "One family policy, three portfolios: each sized…" | "One family policy, a portfolio for each person: each sized…" |
| 7, Fig 15 title | "Five buckets" | "Whose money, held where" |
| 7, Fig 15 rows | "Emergency" · "Education" | "Family reserve" · "Chloe (fees)" |
| 9, Fig 18 Chloe | "None" | "None while studying" |
| 9, Ryan's plan | (whole paragraph) | "Ryan earns HK$300K and saves 30% (HK$90K a year) in three pots: three months' spending in cash, where his tokenised money-market fund counts; goals within ten years, such as a flat deposit, in deposits and short bonds; and the rest, about 80%, in a global equity index fund. His HK$500K of digital assets stays, but gets no new money while above his glide path, so its share falls without selling; a rally more than 10 points above the path is trimmed back (Figure 19). He adds term life and critical-illness cover for about HK$900 a year; his parents match 50% of his savings, up to HK$24K a year, until 2037. A set monthly contribution to the household builds the habit." |
| 9, Fig 19 note | "Today about 74%, if all HK$500K is crypto." | "Today about 74%, if all HK$500K is crypto. Crypto prices held flat." |
| 9, defence | "**Why keep any digital assets.** Selling Ryan's holdings would ignore … The glide path respects both: it is his money, but its share…" | "**Why not sell now, or trim to 20% at once.** It is his own money, about 2% of the family's wealth, and his risk profile is high; a forced sale would override his conviction and could push him to unregulated channels. Doubling down would breach the family's objective of controlled downside. The glide path respects both: its share of his wealth falls as he builds everything else." |
| 12, roadmap | "Months 1–6 · Three portfolios; policy signed; voluntary MPF" | "Months 1–6 · A portfolio for each person; policy signed; voluntary MPF" |
| 12, roadmap, new row before 2032–36 | — | "2032 · Chloe starts work: her own plan, as Ryan's · Chloe · —" |
| 13, B1 | "Four risk appetites" | "Different risk appetites" |

Dropped on purpose: Ryan's voluntary MPF (locks goal money to 65 for ≈HK$6K of tax; S11), and "His salary stays his
own; … agreed at the first family meeting" (shortened for space; the family meeting is on the roadmap).
Number checker: Figure 19 assumed all new savings in equity. With about 80% in equity the crypto share at 35 is
probably a point higher. Rerun it, or add "(all new savings in equity)" to the note if there is no time.

## Batch 6 ready

---

### S13 · Pages 7 and 8 (§5, §6 ESG) · severity: medium-high · TESTED WORDING
Quote (p8, Fig 17): "Adrian: ESG index fund 30%, HSI ESG ETF (3039) 5%, green bonds 5%"
Quote (p7): "a small Hong Kong holding in an HSI ESG index ETF (3039) is kept for its tax-free dividends and low cost."
Issue (Pete's question): Figure 17 lists "ESG index fund" without naming it. The name appears only in the note below
and on p7. The table also does not say what kind of ESG each holding is, and a judge sees two ESG equity funds side by
side without knowing why. The reason is in Win's notes (30 Sep): 3039 **is** the plan's small Hong Kong equity
holding, the ESG version of the Hang Seng Index. It replaced the Tracker Fund (2800) because it is the same market, at a
0.20% fee, and adds ≈1.4 points to the ESG share. It is not a second ESG bet. The p7 reason given ("tax-free
dividends") is shaky: mainland Chinese companies in the index (H-shares) pay dividends after a 10% mainland
withholding tax. The stronger reason: the global core tracks a developed-markets (World) index, which leaves out
mainland Chinese companies, and the Hang Seng holding adds them, kept small because the family already depends on
Hong Kong.
Fit: applied to the scratchpad copy on top of S12. p7 2.5 mm free · p8 2.5 mm free (it overflowed by 2.8 mm with the
first draft, so the columns were compacted). PNGs checked.

| Page | Old | New |
|---|---|---|
| 8, Fig 17 table | Source · HK$M, three rows by person | Four columns: **Holding · Role (Adrian, Carmen) · What makes it ESG · HK$M** (col widths 33/23/35/9%). Rows: "BOC-Prudential MSCI World ESG Index Fund · Global equity (30%, 35%) · The highest-rated companies in each sector of the world index · 1.35" / "E Fund HSI ESG Enhanced Index ETF (3039) · Hong Kong equity (5%, 2%) · The Hang Seng Index minus its ten worst ESG-risk companies · 0.14" / "Green bond fund · Bonds (5%, 10%) · Money raised pays for verified green projects · 0.31" / "MPF ESG fund · Half of each parent's MPF · On the SFC's list of ESG funds · 0.84" / total row unchanged, label spanning three columns |
| 8, Fig 17 note | "The global core, the BOC-Prudential MSCI World ESG Index Fund, is one of only two…" | "The global core is one of only two…" |
| 7, §5 prose | "a small Hong Kong holding in an HSI ESG index ETF (3039) is kept for its tax-free dividends and low cost." | "a small Hong Kong holding, the ESG version of the Hang Seng Index (3039, fee 0.20%), adds the mainland Chinese companies that the world index leaves out." |

Checks before submission (each could embarrass the ESG section):
1. **Which MSCI index the BOC-Prudential fund tracks.** "Highest-rated companies in each sector" assumes MSCI's
   best-in-class (ESG Leaders-type) method, as Win's notes say. Confirm in the fund's key facts statement (SFC ceref
   BUM645). If it tracks a "Screened" index (exclusions only), change the cell to "The world index without excluded
   industries".
2. **3039's index:** confirmed from its product documents that it starts from the Hang Seng Index and applies three ESG
   screens, including removing the ten constituents with the highest Sustainalytics ESG risk ratings. "Minus its ten
   worst ESG-risk companies" simplifies that; add "and other screens" if space allows.
3. **Our own two-rating test** (p8: "MSCI A or better and Sustainalytics risk below 20") must be checked **on 3039
   and the BOC-Prudential fund**. Hong Kong and China equity portfolios often score around 20 or above on
   Sustainalytics. If 3039 fails our own entry test, the section contradicts itself. Then either loosen the test for
   index funds ("or the index itself applies an ESG-risk screen") or drop 3039 for 2800 (ESG share falls ≈1.4 points,
   to about 24%).
4. **The green bond fund is never named** anywhere in the proposal (Win's table: "SFC-authorised green bond fund").
   It is 12% of the ESG total. Name one from the SFC's ESG list. Also, p7's "Every holding is a low-cost index fund or
   ETF" is probably untrue for it, because most green bond funds are actively managed.
5. **The MPF row (0.84, a third of the ESG total) assumes each parent's scheme offers an SFC-listed ESG fund.** The case
   does not name the schemes. Without it, ESG is ≈1.79 of 10.47 = 17%, **below the family's 20% minimum**. State it as an
   assumption, or say what happens if a scheme has none (for example, "if a scheme has no ESG fund, Carmen's ESG index
   holding rises to 40%").
6. Number checker: the row values sum to 2.64 (1.3455 + 0.1449 + 0.3105 + 0.835), against "2.63" in the total.

## Batch 7 ready

---

### S14 · Pages 7 and 8 · severity: medium · REOPENS A RECORDED DECISION (Pete asked) · TESTED WORDING
Question: should the plan hold the Hang Seng (3039) at all? **Recommendation: no.** Move its 5% (Adrian) and 2%
(Carmen) into the global ESG core. This **supersedes S13's p7 wording and the 3039 row of S13's Figure 17.**
Correction to S13: there I offered "it adds the mainland Chinese companies the world index leaves out" as the reason
to keep it. On reflection that reason works against us. The family is already heavily exposed to Hong Kong and the
mainland through everything that is not the portfolio.
Why drop it (the new evidence for reopening the CLAUDE.md decision):
1. **It contradicts §5's own argument.** Page 7 says "the family's home, business and incomes already depend on Hong
   Kong, so the core is global", then adds Hong Kong equity anyway. The home (HK$11.5M), Carmen's business (HK$5.0M),
   Adrian's job (Hong Kong and the Greater Bay Area) and Ryan's job all fall in the same downturn as the Hang Seng
   (2019–22 hit all of them). The portfolio is the family's only place to diversify that.
2. **It is overweight even by market size.** Hong Kong and China together are about 3% of world equity markets. 5% of
   Adrian's portfolio is double that, for the most cautious person in the family.
3. **The stated reasons do not hold.** "Tax-free dividends" is untrue for the H-shares (10% mainland withholding).
   "Low cost" is no reason to own a market. The Hong Kong dollar match means little, because the HKD is pegged to the
   US dollar that dominates the global core anyway.
4. **It is the holding most likely to fail our own ESG entry test** (S13 check 3).
5. **It costs nothing to drop.** About HK$145K, 0.6% of net worth. Moving it into the BOC-Prudential ESG fund keeps the
   ESG share at **25%**, so pages 2, 3 and 8 do not change. The model uses asset-class returns, not funds, so there is
   no rerun. One less product to explain.
What it gives up: a small holding of mainland Chinese companies, which the family already has through its home,
business and jobs; and familiarity. A family used to Hong Kong stocks may want some. The annual review can add it back
if Adrian asks, inside the global equity share.
Fit: scratchpad copy with S12 + S13 + S14: p7 7.4 mm free · p8 15.3 mm free.

| Page | Old (current v2) | New |
|---|---|---|
| 7, §5 prose | "The family's home, business and incomes already depend on Hong Kong, so the core is global; a small Hong Kong holding in an HSI ESG index ETF (3039) is kept for its tax-free dividends and low cost." | "No separate Hong Kong holding: the family's home, business and three incomes already rise and fall with Hong Kong, so the portfolio is where they spread that risk." |
| 8, Fig 17 | (S13 table) BOC-Prudential row "Global equity (30%, 35%) · 1.35" and the 3039 row | BOC-Prudential row "Global equity (35%, 37%) · 1.49"; **delete the 3039 row**. Total unchanged at 2.63 (rows sum to 2.64, see S13 check 6). |

Also update: CLAUDE.md "Decisions already made" (ESG line: drop "HSI ESG ETF 3039 (Hong Kong)"), the manuscript's
decision record, and Win's allocation tables (Adrian: ESG core 25% + 5% + 5% = 35%; Carmen: 35% + 2% = 37%). Tell
Win, since it reverses his 30 Sep switch.

## Batch 8 ready
S14 addendum, for the number checker: the Fig 17 note says "a plain index fund would leave the family at 19%". If S14
is applied, more sits in the BOC-Prudential fund, so that counterfactual falls. Recompute it, along with what "19%"
was measured on (replacing the whole fund gives (2.63 − 1.35) / 10.47 ≈ 12% even before S14).

---

## Pete's decisions (1 Oct)
- **S14 approved: drop the Hang Seng holding (3039).** Apply S14: the p7 sentence, Fig 17 without the 3039 row,
  BOC-Prudential at Adrian 35% / Carmen 37%, HK$1.49M. Update CLAUDE.md "Decisions already made", the manuscript's
  decision record and Win's allocation tables. Pete tells Win.
- **S5, S6, S13 approved.** For S13 apply the table layout (Holding · Role (Adrian, Carmen) · What makes it ESG · HK$M),
  the shortened Figure 17 note, and the green bond and MPF rows. S14 replaces the 3039 row and the p7 sentence. S13's
  checks 1, 4, 5 and 6 still stand; check 3 now applies only to the BOC-Prudential fund.
- S6: use the wording folded into S2 ("…we count only HK$3.0M, the price a forced sale might fetch, so the plan does
  not depend on a good sale"), adapted to v3's existing "Why sell rather than keep" paragraph.
- **Base for all edits: `document/proposal-v3.html` (30 Sep 21:01) is the latest direct-edit copy, not v2.** It
  already contains S1–S4, S8 and most of S12. Still missing from S12: "Crypto prices held flat" in the Figure 19 note.
- v3 overflows on pages 11 (6.5 mm), 12 (9.0 mm) and 13 (14.4 mm), from a scratchpad render on 1 Oct. S14 frees about
  16 mm on p8, which does not help those pages.

## Batch 9 ready

---

### S15 · Pages 7 and 8 · DECISIONS on the open ESG checks (Pete asked me to choose) · TESTED on v3
Pete asked for the most reasonable, data-driven choice on each open item from S13 and S14. Applied to a scratchpad
copy of **`proposal-v3.html`** together with S13 and S14. Fit: p7 7.4 mm free, p8 5.6 mm free; every other page is
unchanged (pages 11–13 still overflow as in v3). The p8 PNG has been checked.

**Decisions and evidence**
1. **The BOC-Prudential fund's method: keep "the highest-rated companies in each sector".** Evidence: Win read the
   fund documents on 30 Sep and recorded "MSCI's best-in-class ESG selection" (`Updated_Investment_Win.md`). My web
   search found no public key facts statement, so Win's primary reading is the best evidence we have. Win confirms
   against the key facts statement (SFC ceref BUM645) before submission. Fallback cell if it tracks a screened-only
   index: "The world index without excluded industries".
2. **The two-rating test is scoped by asset type.** Fund-level Sustainalytics risk scores are an equity measure. The
   market standard for green bonds is the ICMA Green Bond Principles with an external review, which the HKSAR
   government's own green bond framework follows. Equity funds: two ratings. Green bond fund: ICMA principles plus
   external review. All funds: a holdings check.
3. **The green bond fund stays generic on the page; we name the rule, not the product.** We could not verify a
   specific SFC-authorised green bond fund in time, and naming an unchecked product is worse than naming the rule.
   Implementation (roadmap months 1–6, no page change needed): keep up to HK$0.31M of the family's **existing**
   HK$0.45M green and sustainable bond holding if it passes the ICMA test, which saves switching costs. Otherwise use
   a fund from the SFC's ESG list. p7 now says "every holding except the green bond fund is a low-cost index fund or
   ETF", because most green bond funds are actively managed.
4. **The MPF third of the ESG total gets a stated route and a computed fallback.** Evidence: the SFC reported that only
   four of its authorised ESG funds were underlying funds of MPF schemes (Dec 2024). Win's notes name one, the Sun Life
   AM Global Low Carbon Index Fund. Under the Employee Choice Arrangement (MPFA), an employee can move the MPF from
   their own mandatory contributions, about half the balance, to a scheme of their choice once a year.
   Route: Carmen, as the employer, picks a scheme with a qualifying ESG fund. Adrian moves his employee half there and
   holds it in the ESG fund, while the employer half stays in his scheme's bond fund. That still gives half and half.
   Fallback, computed: without any MPF ESG fund, ESG = (1.49 + 0.31) / 10.47 = **17.2%**, below the 20% minimum.
   Moving Carmen's 15% plain global equity (≈HK$0.31M) into the BOC-Prudential fund gives 2.11 / 10.47 = **20.2%**,
   with the same risk because the swap is equity for equity in the same world index. If only Carmen's MPF qualifies,
   the result is also 20.2%, with no fallback needed.
5. **The total is 2.64, not 2.63.** The exact rows are 1.4904 + 0.3105 + 0.835 = 2.6359. "Rows rounded" is dropped,
   because the rounded rows now add up.
6. **The counterfactual in the Fig 17 note:** with a plain index fund instead of the BOC-Prudential fund,
   (2.64 − 1.49) / 10.47 = **11%, exactly today's level**. That is a stronger line than v3's "12%" (which was computed
   before S14).
7. **Cut "Why not higher" on p8.** The fallback in point 4 shows that more ESG is possible at the same risk, so the old
   sentence ("going further would mean … more equity for Carmen") was no longer true. The heading already says the
   plan reaches the top of the family's range.

**Exact replacements on v3** (S13 + S14 + S15 combined; this supersedes the S13 and S14 tables)

| Page | Old (v3) | New |
|---|---|---|
| 7 | "Every holding is a low-cost index fund or ETF, SFC-authorised or HKEX-listed." | "Every holding except the green bond fund is a low-cost index fund or ETF, SFC-authorised or HKEX-listed." |
| 7 | "The family's home, business and incomes already depend on Hong Kong, so the core is global; a small Hong Kong holding in an HSI ESG index ETF (3039) is kept for its tax-free dividends and low cost." | "No separate Hong Kong holding: the family's home, business and three incomes already rise and fall with Hong Kong, so the portfolio is where they spread that risk." |
| 7 | "Inside the MPF, each parent holds half in the scheme's ESG or global index fund and half in its bond fund until the annuity is bought." | "Inside the MPF, each parent holds half in an ESG fund and half in a bond fund until the annuity is bought (§6)." |
| 8, Fig 17 head | `<th>Source</th><th class="n">HK$M</th>` | colgroup 33/23/35/9%; `Holding · Role (Adrian, Carmen) · What makes it ESG · HK$M` |
| 8, Fig 17 rows | the three rows by person, and the total 2.63 | "BOC-Prudential MSCI World ESG Index Fund · Global equity (35%, 37%) · The highest-rated companies in each sector of the world index · 1.49" / "Green bond fund · Bonds (5%, 10%) · Bonds whose proceeds fund verified green projects · 0.31" / "MPF ESG fund · Half of each parent's MPF · Its underlying fund is on the SFC's list · 0.84" / total (label colspan 3) "…(today: 1.15, or 11%) · 2.64 (25%)" |
| 8, Fig 17 note | "Rows rounded. Counted as ESG: … The global core, the BOC-Prudential MSCI World ESG Index Fund, is one of only two global equity index funds on that list; a plain index fund in both portfolios would leave the family at 12%." | "Counted as ESG: … The global core is one of only two global equity index funds on that list; a plain index fund in its place would leave the family at 11%, where it is today." |
| 8, Strategic role | "index-tracking, so the method is published;" | "index-tracking where possible, so the method is published;" |
| 8, Three layers | "… add direct impact. **Why not higher:** the plan reaches … rules out." | "… add direct impact." (delete the Why not higher sentence) |
| 8, Greenwashing | "A fund enters only if it passes two ratings (MSCI A or better and Sustainalytics risk below 20) and a holdings check; a downgrade triggers replacement within three months." | "An equity fund enters only if it passes two ratings (MSCI A or better, Sustainalytics risk below 20); a green bond fund only if its bonds follow the ICMA Green Bond Principles, externally reviewed. Each gets a holdings check; a downgrade means replacement within three months." |
| 8, No return premium | "The limitation is a smaller universe of funds in Hong Kong; government tokenised green bonds stay on a watch-list until retail investors can buy them." | "The limitation is a smaller universe of funds in Hong Kong. Few MPF schemes offer an ESG fund on the SFC's list: Carmen, as the employer, picks one that does, and Adrian moves the half built from his own contributions to one under the Employee Choice Arrangement. If neither can, Carmen's plain global holding moves to the ESG fund and the family stays above 20%. Tokenised government green bonds stay on a watch-list until retail investors can buy them." |

Still for people, before submission: Win confirms the BOC-Prudential index, fee and retail access (point 1) and
identifies the family's existing green bond product (point 3). Someone checks which MPF schemes' ESG funds are on the
SFC list today (point 4; the Dec 2024 count is the latest found). Manuscript §6 and CLAUDE.md's ESG decision line
should be mirrored.

## Batch 10 ready
