# Built to Last, Round Two: Deck Plan (v10, "Their own way, then five calls", the house we build)

**Status:** v10, 23 Oct 2026. The story is v9's (agreed 22 Oct: the problem before the answer, "their own way" as the
baseline, Lookbua reads slide 11); v10 is the design pass (Pete, 23 Oct: "the story is ok, the pages are not"): the
house as the deck's idea, and a picture that portrays each slide's point (§6, §5). The talk, timed, with the full draft script: `round2/Talk_Outline.md`. Look B chosen (20 Oct, §6).
v8 ("Five calls", 20 Oct) is in git (commit 0b0a985 and before); v1 to v7 in `archive/Round2_Deck_Plan_v1-v7.md`.
**Deck type:** a 10-minute recorded video presented over these slides, and the PowerPoint file scored on its own
("Quality of ppt"). Pete chose **hybrid** (20 Oct): every slide is presented, and also makes sense read alone.
**Due:** Mon 26 Oct 2026, 17:00 HKT (results letter, 16 Oct). Recording was planned Thu 22 to Fri 23 Oct; realistic
now: build Thu to Fri, rehearse and record Sat, edit Sun, deliver Mon morning.
**Limits:** 10:00 of video, English; MPEG-4, AVI or WMV, plus the PowerPoint file; files named with the team name
only; no university name, logo, campus or account anywhere, including file metadata (CLAUDE.md).
**Related:** the written case as submitted (`document/build/proposal.pdf`; sources `document/*.html`, wording
`document/manuscript.md`); model numbers `figures/numbers.json` and `figures/figure-data.md`; the case
`Primary Info/Award2026Case20260919.pdf`; rules `Primary Info/2026-rules.md`.

**How to use it:** build each slide from its section in §5. The deck is `round2/src/` (v9, set up 22 Oct: slides 1,
3, 6 and 7 built, the rest titled placeholders); `make.py` writes the slides as `Axis.html` and the script, from each
slide's speaker notes, as a separate file, `Axis_Script.html` (Pete, 22 Oct). Change the plan first, then the slide. Every model number on a slide is a `{{key}}` from `figures/numbers.json` (or a series from
`figure-data.md` via `series.py`), so the deck and the written case cannot disagree. Commit and push after each major
step (CLAUDE.md).

---

## 1. What the audience scores, and where the deck answers it
Round Two criteria (results letter 16 Oct 2026; rules page captured 14 Sep 2026), weights as given:

| Criterion | What they need to see | Slides |
|---|---|---|
| Communication skills (45): "Present ideas clearly, systematically, effectively, and forcefully" | A problem they feel, the answer by 1:30, five calls in one order, each defended; confident delivery; time kept | All; 4 is the map |
| Content delivery, personal statement (15): "Presentation of personal statement and coverage of the cross boundary wealth management connect scheme" | What the Connect is now, both directions, the advice rule; what it means for the Wongs and for us; each member's goal | 13, 14 |
| Content delivery, financial proposal (20): "Presentation of essential elements of a financial proposal within the time constrain provided" | Position, goals, a recommendation in every area, quantified impact, implementation, risks | 2 to 12 |
| Powerpoint (15): "Quality of ppt" | A designed, consistent deck; one claim a slide; charts that read; works without the voice | All |
| Others (5): "Charisma and team spirit" | Four faces, warm handovers, a shared close | 1, handovers, 14, 15 |

**What the case itself asks to see** (case p.9, notes 4): "strategic thinking, client suitability awareness,
innovation, implementation practicality, professionalism in presentation". The family's brief (case p.5): a plan that
is "innovative yet prudent, forward-looking yet practical, and aligned with both financial goals and family values".
The case's title: "The Wong Family Legacy: Balancing Retirement, Education, ESG Integration, and Digital Asset
Exposure". The deck's argument is built to show each of these.

**Ranking:** Round Two = 0.5 × Round One + 0.5 × Round Two; the top four go to the Final.

## 2. The argument
**In one sentence:** left to manage it their own way, the Wongs would sell the home where they raised their children
late, under pressure, and still leave them little; five calls (insure the incomes, put the home and the business to
work at 65, fix the cost the budget ignores, give each person a plan of their own, and add their values and Ryan's
crypto with guardrails) make the home their choice and keep the inheritance, without taking more risk.

**Why the problem comes first now (v9, Pete 22 Oct):** v8 led with the answer, on the reasoning that the judges have
read the written case and know the numbers. But they have not seen "their own way": it is new evidence, so it carries
real tension, and Pete wants the talk to build slide by slide. The answer still arrives at 1:30.

**Why "their own way", not "investments alone" (Pete, 22 Oct):** no reasonable family lives on its investments alone
while it owns an HK$11.5M flat and a HK$5M business; a practitioner would call the proposal's 33% a strawman. A
sensible family would sell the business, and the flat if it had to. We tested exactly that (`reviews/applied.md`,
22 Oct): the flat is sold by force in {{own_sold_pct}} of futures, when Carmen is about {{own_sale_age}} and usually
alone; the money still lasts to 89 in only {{own_89}}; and Ryan and Chloe inherit {{own_legacy_sold}} where the flat is
sold, against {{plan_legacy_sold}} under the plan in the same markets. A late sale buys two to three years: at 83 the
flat releases less, the money has little time to grow, and the medical premiums are at their peak.

**What the audience must believe:**
1. The family is strong, and the risk is not the markets but when and how their wealth is used (2, 3).
2. Each call is the right one for this family, better than the obvious alternative (5 to 9).
3. The plan survives the worst and is honest about its limits (10).
4. It can start this month, and it is reviewed as life changes (11).
5. It keeps the inheritance their own way would spend (12), and we are planners who could do this across the boundary
   (13, 14).

**The strongest objections:** "They could take a reverse mortgage at 83 instead of selling" and "they could rent, or
buy cheaper". Both are in §10; the inheritance line holds either way.

## 3. The storyline (titles only)
Read the titles aloud in order: they make the whole argument. Times and words are measured on the draft script
(`Talk_Outline.md`): 1,200 spoken words, 9:08 at 135 words a minute with handovers, 9:51 at 125.

| # | Kicker | Title | Speaker | Time |
|---|---|---|---|---|
| 1 | — | Built to Last: five calls that make the Wong family's wealth last | Pete, all | 0:20 |
| 2 | Meet the Wongs | On paper, the Wongs are secure, for a plan that must last forty years | Pete | 0:30 |
| 3 | Will it last? | Their own way, Carmen sells the family home at about {{own_sale_age}}, and the children's inheritance pays the bills | Pete | 0:45 |
| 4 | Our answer | The family asked for innovative yet prudent: five calls make the home their choice and their wealth last | Pete | 0:45 |
| 5 | Call 1 · Protection | Insure the income, not the life: about HK$100K a year closes every gap | Lookbua | 0:40 |
| 6 | Call 2 · The home and the business | Decide now, not at {{own_sale_age}}: four decisions on what they own and spend lift the odds from {{own_89}} to {{ladder_5_89}} | Fahtai | 0:45 |
| 7 | Call 3 · Retirement | Fix the cost the budget ignores: in that same future, the money now lasts to 89 and the home stays theirs | Fahtai | 0:40 |
| 8 | Call 4 · Each person | One family policy, a plan for each person: every dollar gets a job | Win | 0:50 |
| 9 | Call 5 · Values and innovation | Values and innovation, with guardrails: ESG at 25%, crypto sized for each person | Win | 0:45 |
| 10 | Will it hold? | Tested against the worst: even if Adrian loses his job at 60, the plan holds | Lookbua | 0:30 |
| 11 | What happens when | It starts this month; after that, dates trigger each step | Lookbua | 0:30 |
| 12 | What passes on | In the very futures where their own way sells the home, the plan leaves Ryan and Chloe {{plan_legacy_sold}}, not {{own_legacy_sold}} | Pete | 0:25 |
| 13 | Wealth Management Connect | The Connect is growing both ways: for the Wongs a tool for later, for us the market we want to serve | Pete | 0:40 |
| 14 | Who we want to become | Four planners, one aim: families like the Wongs, on both sides of the boundary | All | 1:10 |
| 15 | — | Built to last | Pete, all | 0:15 |
| | | | | **9:30** |

Handovers: Pete (1 to 4) → Lookbua (5) → Fahtai (6, 7) → Win (8, 9) → Lookbua (10, 11) → Pete (12, 13) → all (14) →
Pete (15). Speaking time at 135 words a minute: Pete 3:40, Lookbua 1:54, Win 1:40, Fahtai 1:37, including each one's
share of 14.

**Threads that tie it together** (the flow has to be on the page, not only in the script):
- **The home:** sold at about {{own_sale_age}} by force (3) → their choice at 65, stay or move (6) → none of the ten
  futures sells it (7) → the inheritance kept (12).
- **The ten futures:** {{own_fut_sold_n_word}} carry a "sold" mark and {{own_fut_short_n_word}} still stop (3) → all
  {{plan_fut_lasts_n_word}} reach 89, no marks (7). The same picture, redrawn.
- **The inheritance:** {{own_legacy_sold}} where the home is sold (3) → {{plan_legacy_sold}} in the same markets (12).
- **The odds:** {{own_89}} their own way (3, 4) → {{ladder_5_89}} (6) → {{switch_89}}, almost every future with the
  spending rules (7) → still {{rec_adrian60_89}} if Adrian loses his job at 60 (10).

**Coverage.** The family's eight questions (case p.5): 1 retire on track (3, 6, 7, 10), 2 Chloe (8), 3 crypto (9), 4
ESG (9), 5 insurance (5), 6 wealth and responsibility between generations (3, 5, 8, 12), 7 Carmen's business (3, 6), 8
the home (3, 6, 12). The case's eleven sections: summary (4), cash flow and net worth (2, 3), retirement (6, 7),
education (8), investment (8), ESG (9), digital assets (9), protection (5), property, succession and legacy (6, 12),
roadmap (11), risk and compliance (10).

## 4. Rules for every slide (the system)
These rules hold on every slide. They exist because v7 had 40 font sizes, about ten navigation items a slide, and a
different grid on every slide.

**Anatomy of a content slide (3 to 13):**
- kicker (the section: "Call 2 · The home and the business"), then the title, two lines at most;
- **panels whose headings read as one sentence across the slide** ("What they own…" / "…what each becomes…" /
  "…and what it achieves"); **each panel is one step of the argument and adds a new fact**: no panel restates another
  panel or an earlier slide (Pete, 20 Oct: v8's first Call 2 spent a third of the slide repeating 33%);
- **every claim gets a shape, not a paragraph.** The defence of a call is **measured** where it can be: run the
  obvious alternative in the model and draw it beside the call (Call 2: their own way, `own_*`); where it can't, a
  ledger with one figure a row. Each panel opens with its hero number or object;
- one **conclusion bar**: the slide's point in one sentence, worded to lead into the next slide;
- **the hierarchy inside a panel** (23 Oct, from Pete's own decks and Nordea's; Pete: "missing a lot of icons", "so
  many things to focus on", "a document put into a powerpoint slide format"): heading (Inter bold 19 px on an ink rule)
  → a one-line lede (15 px, its key phrase bold) → the content. **Taken only where a planner would use it** (Pete,
  23 Oct: "take the good parts, and apply it where it is reasonable"; would a world-class planner pitching put this on
  screen?): a plain **reading** under a chart that needs one (a dashed box, the key phrase bold; it says what the
  picture shows, never restates the title); one dashed **ring** on the moment that matters; **icons that name a real
  thing** (the home, the pension, the business, the chance the money lasts), neutral except the focal row's (crimson
  on tint); the same result rows wherever the same kind of result appears (slides 3 and 7). The focal number is the
  largest type in the body and the only crimson number. **Not taken:** chevrons, numbered discs with no legend,
  lightbulbs, a crimson punch-line in every box, a takeaway under a shape that already speaks (the house, the flow,
  the blocks);
- **navigation:** the kicker (the section) and a quiet **section tracker in the footer** (The problem · The answer ·
  The five calls · Will it hold · What next · Us; the current one in ink). **Back on trial, pending Pete:** it was
  dropped on 23 Oct on my recommendation (titles needed the width; three signals for one fact), but both winning
  references (Nordea's, Pete's Banyan) carry one, and in the footer it costs the titles nothing. Footer: the source
  (two lines at most; the detail goes to the notes), the tracker, the page number.
- Not used (v7 lessons): a second tracker, question pills, "slide 5's…" references, tags inside sentences.

**Grid:** 1280 × 720; margins 48 px left and right, 34 px top; 12 columns, 24 px gutters. Panels are 4 + 4 + 4,
5 + 4 + 3 or 7 + 5 columns. **One top line, one baseline** (Pete, 20 Oct): every panel's content starts 20 px under its
heading rule and ends on one baseline; spare space is spread inside the content, never left as a gap at one end.
Measure it on the render, don't eyeball it.

**Text on a slide (Pete, 20 Oct: "many disconnected text, we're just pushing out text everywhere"):** say each thing
once (the title is the claim, the picture the evidence, the bar the so-what; cut any caption that repeats one of
them); attach every label to what it explains (a result carries its own qualifier, a segment its own name; no
floating sentences, legends or notes that restate); one block per idea. The reasons are spoken and live in the
speaker notes, which the PowerPoint carries for anyone reading the file. **But not empty** (Pete, 20 Oct, on Call 2
v6): a slide needs enough on it to tell its story read alone; the fix for clutter is fewer, connected pieces, not
fewer facts.

**Hierarchy inside a panel:** rank items by what the evidence says matters (the biggest contributions lead; small ones
go to a note). Never list unlike things (a cost, a safety margin, a legacy) as equal rows.

**Type (23 Oct):** EB Garamond for the title and big numbers; **Inter** for everything else, panel headings (bold 19,
from Pete's decks) and bold labels included. **Scale:** title 35 · panel heading 19 · bold label and body 16 (Inter) · small 14 (Inter) · tag and
source 12 · numbers 40 and 72 (76 on slide 2's net worth). Nothing meant to be read is under 14 px.

**The slides are scored on their own** (Pete, 23 Oct: the video and the slides are scored independently). So each
slide **lists the most important facts**, enough for someone reading the file to follow the argument without the
voice. The title's claim and the focal number are always spoken; supporting facts may stay unspoken on screen, as long
as they don't compete with the focal point. (Replaces "every on-screen phrase is spoken; cut a number the script
doesn't say", which stripped facts the separately scored slides need.)
**Density:** about 120 to 180 words on a call slide, about 150 on the summary: **warnings, not limits.** Never make a
phrase vaguer to meet a count (slide 4 lost "forced" that way, 23 Oct). The script: about 1,200 spoken words in all,
until the team's timed read-through sets the real cap (if they average 135 words a minute or faster, about 1,240, and
the extra goes to the personal statements).

**Charts:** one style. Grey series, the accent only on the value the title claims, labels on the data (no legends
where a label fits), axis text at 14 px. The ten futures (3, 7) and the premium line (7) come back from v7 (they
worked); everything else is redrawn in the system.

**Numbers:** tagged as a quiet "(measured)", "(case)" or "(sourced)" after the claim. MEASURED = the team model
(`numbers.json`); CASE = the case; SOURCED = a named public source.

**Builds:** each slide reveals in speaking order (`data-b`). **Later steps stay on the page in grey** (Pete, 23 Oct:
don't remove what's coming, grey it), so the layout never moves and the eye goes to what is in colour. `make.py
--builds` writes one frame per step (`Axis_builds.html`, `build/frames/`) for the video. Red reads as alarm: crimson
marks the title's claim as a point or a number, never a wall of lines (slide 7: ink lines, crimson ticks).
**Keep it simple** (Pete, 23 Oct): each slide as simple as it can be while its point stays clear.

## 5. Slide by slide
Each spec: the point; the panels in order (headings reading as one sentence); the evidence and its keys; the bar.
The scripts are in each slide's speaker notes (`round2/src/*.html`); `make.py` writes them to `Axis_Script.html`.

### 1 · Cover (Pete, all; 0:20)
"Built to Last", the promise line, the team; an illustration of the family (image set, §7). No numbers.

### 2 · On paper, secure (Pete; 0:30)
**v10 (23 Oct): forty years on one line** (Pete chose it over "what HK$24.4M is made of"). Title: "On paper, the Wongs
are secure, for a plan that must last forty years". One row per person on a shared 2026-2066 axis: working years an ink
line, retirement a rose band, Chloe's university a tint band, milestones labelled (Adrian retires at 65 in 2037, Carmen
at 62 in 2039, Chloe's university 2028-32); the plan's horizon, Carmen's 89, a crimson line. The strength as a band
below (HK$24.4M in the accent, 41% saved, 10% debt, 30 months of spending in cash). Bar: "But will it last to Carmen's
89? We tested it in 10,000 futures." The earlier specs below are superseded.
**Built 23 Oct** (`src/01_s01-02.html`; 96 words). Stacked: "Four people, four wants…" (upright cards, portraits
150 px) over "…and on paper, secure" (one band; HK$24.4M at 72 px in the accent).
- Four portraits with age, risk profile and want (case): Adrian 54, low to medium, capital, retirement and health
  protected; Carmen 49, medium to high, money that reflects her values; Ryan 24, high, crypto; Chloe 16, university in
  2028.
- The strength in three numbers (case): HK$24.4M net worth, 41% of after-tax income saved, debt 10% of assets.
- Bar: "On paper, secure. But will it last?" (hands to 3).

### 3 · Their own way (Pete; 0:45)
**Rebuilt 23 Oct: one typical future, told with the money** (Pete: the ten lines didn't say what the house meant or what
the other lines were, and gave little context; the flat placeholder took a quarter of the slide for one word).
**23 Oct, second pass: the prototype of the presentation system** (§4; Pete: the right side had "so many things to focus
on"; make the chart smaller and say under it what it means, as in his Banyan deck). Panels 7 + 5: "One typical future,
managed their own way…" / "…and across 10,000 futures".
- **Lede:** one line, the bridge from the written case: "Our written case measured investments alone: {{ladder_1_89}}.
  **The fairer test is their own way.**" What their own way means goes to the footer and the notes.
- **The picture:** one future from the model (`story_*`; the rule: of the futures where the flat is sold and the money
  still runs out, the median sale year, then the inheritance nearest the median), as stacked areas in today's money,
  2026 to 89: the home (dark, labelled "since 2015, where Ryan and Chloe grew up") under savings, investments and MPF
  (light). A dashed ring on the sale; numbered callouts ① "Savings run out: the flat is sold, Carmen
  {{story_sale_age}}" and ② "Out again at {{story_out_age}}". Same scale as slide 7 (`series.py`).
- **Under it, the reading** (dashed box, on the panel's floor): "Their savings run out first. **Selling the flat they
  raised Ryan and Chloe in carries Carmen only from {{story_sale_age}} to {{story_out_age}}.**" (Not the title again.)
- **Right:** three icon rows from the 10,000 futures: {{own_sold_pct}} sell the flat (Carmen about {{own_sale_age}},
  usually alone); {{own_89}} see the money last to 89, even after the sale; then the focal row, stacked, the only
  crimson: {{own_legacy_sold}} (46 px) left to Ryan and Chloe where the flat is sold, of HK$24.4M today. On the panel's
  floor, level with the reading, **"Why it runs out"** on mist: 61% of their wealth is a home and a business that pay
  nothing until sold; HK$375K a year of medical premiums sit outside their budget (both typed in the written case).
  The two causes Calls 2 and 3 fix.
- Builds (reveal): the future → the sale and 51% → the run-out and 62% → what's left, the reading, the why and the bar.
- Bar: "Their wealth will pay for their retirement either way. The question is when, and on whose terms."

### 4 · Our answer (Pete; 0:45)
**v10 (23 Oct): one house, drawn and labelled** (Pete chose it over a five-step sequence, after the first house, a wine
block with a legend beside it, said everything twice). An architect's elevation (`house.elevation`): fine crimson lines,
rose fills, the foundation hatched, one ground line, each part numbered; each part labelled directly by a callout on a
leader line (1, 2, 4 left; 3, 5 and the roof right), so there is no legend. Builds: the house starts as a grey draft,
each part takes colour as Pete names its call, the part being named solid crimson. The result is a plaque under the
house: {{own_89}} their own way → {{switch_89}} with the five calls. Bar: "Five calls, and the home is their choice, not
their last resort. The rest of this talk defends each one."
**Built 23 Oct** (`src/03_s04-05.html`; about 150 words). The brief as a quote, the five calls as five columns (ink
number squares matching the tracker, an icon each), the impact band under a rule: {{own_89}} grey → {{switch_89}} in
the accent, the only accent on the slide.
- **Question band:** the family's brief in its own words: "innovative yet prudent, forward-looking yet practical, and
  aligned with both financial goals and family values" (case p.5).
- **Five calls in a row**, each a number, a three-to-five-word name and one result:
  1 Insure the income, not the life · ≈HK$100K a year closes every gap (sourced)
  2 Put the home and the business to work · {{own_89}} → {{ladder_5_89}}, decided at 65 (measured)
  3 Fix the cost the budget ignores · {{switch_89}} with a medical review at 75 (measured)
  4 One family policy, a plan for each person · Chloe funded today; ≈HK$45K a year less in fees
  5 Values and innovation with guardrails · ESG 25%; crypto sized per person
- **Impact band:** the chance their money lasts to Carmen's 89: {{own_89}} their own way → {{switch_89}} with the plan;
  the home their choice, not their last resort.
- Bar: "Five calls, one family: the rest of this talk defends each one."

### 5 · Call 1: insure the income, not the life (Lookbua; 0:40)
**Built 23 Oct** (`src/03_s04-05.html`; 169 words). Panels 5 + 4 + 3: "If a parent can't work, nothing replaces their
pay…" (Adrian and Carmen, today a dashed empty bar, with cover an ink bar) / "…so we insure the income first…"
(HK$100K in the accent, the year-1 cost as one stacked bar) / "…and sign the papers now" (within three months: wills,
a guardian for Chloe, powers of attorney, **a buy-sell agreement**: added 23 Oct because the case asks for business
continuity and key-person risk, case p.6, and Call 1 had neither; the script says it). **Bar changed** to "Protected
first: now the plan can turn what they own into income": the old bar repeated the panels and led nowhere.
- **"Their biggest risk is an income stopping…"**: pay that continues if a parent can't work: today nothing (no
  disability cover) vs with the plan HK$65K a month to 65 (Adrian) and HK$39K to 62 (Carmen). Disability ranks first
  for both on severity, likelihood and warning time (proposal §8).
- **"…so we insure the income first…"**: ≈HK$100K in year 1 as one bar: disability HK$37K, critical illness HK$1.5M
  each HK$41K, individual VHIS now HK$15K, term-life top-up HK$7K; key-person cover paid by the company; Ryan
  ≈HK$900 a year. 14% of their surplus; ≈{{premiums_avg}} a year on average to retirement (sourced: 2026 rate cards,
  quotes to follow). The papers in month 1, under HK$25K: mirror wills (staged trusts at 25, 30, 35; a guardian for
  Chloe), enduring powers of attorney, advance directives.
- **"…and not with more whole-life" (defend):** the alternative: more whole-life or a savings plan. Why not: the same
  cover costs many times more, because most of the premium buys savings they already hold. The trade-off: the new
  cover ends at 65 and 62, when the need ends. If a claim is disputed, the 12-month reserve carries them.
- Bar: "Every income insured for about 14% of their surplus, and the papers signed in month one."

### 6 · Call 2: decide now, not at {{own_sale_age}} (Fahtai; 0:45)
**v10 (23 Oct): a flow, assets into income** (Pete chose it over the rows). The flat ({{rmp_income}} a year for life
from {{rmp_year}}) and the MPF ({{floor_2039_ann}} a year, two HKMC annuities) flow into one wine box, "Guaranteed income,
for life": {{floor_2039_pct}} of essential bills in 2039; the business flows into savings (HK$3.0M, counted low; their own
way sells it too). Under the flow, the fourth decision as what it is, a spending one: a survivor plans on 70%. The band:
{{own_89}} their own way → {{ladder_5_89}} four decisions, decided at 65, not forced at {{own_sale_age}}.
**Built 22 Oct** (prototype `looks/src/08_call2_v9.html`, render `looks/build/slide-14.png`; 172 words). Title (23 Oct, Fahtai's review): "Decide
now, not at {{own_sale_age}}: four decisions on what they own and spend lift the odds from {{own_89}} to
{{ladder_5_89}}": about half of the rise is the survivor budget, a spending decision, so "the same assets" and a title
crediting only the home and the business overclaimed. Option B, "Put to work" (Pete, 20 Oct), set against their own way; v1 to v6 in `round2/looks/`.
Rows run across the first two columns (each asset beside its decision), ranked by what moves the odds: the flat (the
tallest row, {{rmp_income}} the one large number), the business, the budget, the MPF. **The business row says "their
own way sells it too"**: the model sells it for the same HK$3.0M in both ways, so the rise from {{own_89}} comes from
the home paying from 65 instead of being sold at {{own_sale_age}}, the survivor budget and the annuities. The third
column is two bars on one scale: their own way (grey) and decided now (the accent, 72 px).
- **"What they own…"**: the four things the plan puts to work, grey bars to scale (case): the flat HK$11.5M, the
  business HK$5.0M, the MPF HK$1.7M, and the budget HK$780K a year.
- **"…what each becomes…"**, attached row by row: the flat: {{rmp_income}} a year for life by reverse mortgage from
  {{rmp_year}}, or downsize: they choose at 65; the business: sold in stages 2035 to 39 to her co-founder and managers,
  HK$3.0M counted of HK$5.0M; the MPF: two annuities, {{floor_2039_ann}} a year; the budget: a survivor plans on 70%.
- **"…and what it achieves"**: {{ladder_5_89}} (the accent, 72 px), against their own way {{own_89}}, with the flat
  sold at about {{own_sale_age}}.
- Speaker notes: more shares instead (80% in shares: {{alone_eq80_89}}, worst year {{alone_eq80_worst}}, and it breaks
  Adrian's profile); the 2039 floor ({{floor_2039_pct}} of essential bills; {{floor_2057_pct}} after Adrian's death, so
  never "for life"); even if the business never sells, {{biz_not_sold_89}}; the annuity is last on purpose, insurance
  for the worst markets ({{ann_w1_with_real}} vs {{ann_w1_without_real}}).
- Bar: "Decided now, four decisions close most of the gap; what's left is a cost the budget ignores."
- Answers questions 1, 7 and 8.
- **Icons** (23 Oct): the three things they own carry a neutral icon each (house, piggy bank, briefcase); the bars
  stay to scale (14 px per HK$1M).

### 7 · Call 3: fix the cost the budget ignores (Fahtai; 0:40)
**Rebuilt 23 Oct with slide 3.** Title: "Fix the cost the budget ignores: in that same future, the money now lasts to 89
and the home stays theirs". Left: the same future in the same markets under the plan (four decisions, the review at 75,
the spending rules): the home pays {{rmp_income}} a year from {{rmp_year}} and stays theirs; savings never run out;
their own way as a dashed line. Builds (reveal): the premiums → the review and {{switch_89}} → the rules → the future.
Notes answer "why does the plan look poorer until about 2056?" (the annuities and the home's income: a floor, not a peak).
- **Inset: the premium line** (series.py): Flexi for life climbs to HK$375K a year (today's money, by 2056) vs the
  Standard plan from Adrian's 75, about a third the cost; the saving shaded. {{switch_89}} with the review.
- The spending rules in one line: from 2039, no raise after a bad year, a trim only if withdrawals run well ahead,
  essentials never cut.
- Speaker notes: the defence (cut the budget now instead? The problem arrives after 2047, so the decision waits);
  the guardrail details; the worst one in twenty ({{guardswitch_worst5_real}} vs {{fixswitch_worst5_real}}); the rules
  cost about {{guard_cost}} a year of typical spending; the switch is guaranteed under the VHIS rules (Code of Practice
  s.2.11, FAQ Q30; Fahtai, 23 Oct), so "subject to underwriting" appears nowhere.
- **Results** under the premium line, in slide 3's row form: {{switch_89}} see the money last to 89, with the review
  (the hourglass, as on slide 3); from 2039, spending rules protect the bad years, essentials never cut (a shield).
- Bar: "Will it last? In almost every future: they retire on time, keep the way they live, and keep the home." (23 Oct:
  answers slide 2's question and slide 3's kicker; "Question 1" pointed to a list no slide shows.)

### 8 · Call 4: one family policy, a plan for each person (Win; 0:50)
**v10 (23 Oct): blocks with jobs and faces** (Pete chose it over two bars). The parents' HK$7.7M drawn twice on one
scale: today, grey blocks with no job (cash HK$2.5M, 30 months, idle; bond funds HK$1.35M; equity funds HK$3.85M at
about 1.5% a year); with the plan, crimson-family blocks, each a job and an owner's face (reserve HK$1.0M; Chloe's degree
HK$2.57M; Adrian HK$2.07M, 40% shares; Carmen HK$2.07M, 60% shares, led by ESG). Strip: Ryan's own plan (30% of his
pay); HK$45K a year less in fees.
- **"Today, one pot that fits nobody…"**: the parents' HK$7.7M outside the MPF and the home: cash HK$2.5M (30 months
  of spending), bonds HK$1.35M, shares HK$3.85M in funds at about 1.5% a year: more risk than Adrian's profile allows
  (case; proposal §5).
- **"…every dollar a job, by person…"**: a 12-month reserve HK$1.0M; Chloe HK$2.57M ring-fenced in HK dollars until
  she accepts an offer (covers the UK, Canada, Singapore and Hong Kong even after a currency shock); Adrian HK$2.07M,
  shares 40 · bonds 55 · cash 5, with US Treasuries maturing 2037 to 41; Carmen HK$2.07M, 60 · 35 · 5 (written case
  Figure 14; Fahtai, 23 Oct), led by ESG
  funds; Ryan saves 30% of his pay in his own three pots, his parents match half up to HK$24K a year until 2037.
- **"…with rules agreed in advance" (defend):** the alternative: one household portfolio. Why not: it would break
  Adrian's profile or under-serve Carmen's. All Treasuries for Adrian? After inflation they fail almost every time.
  Broad index funds cut fees by ≈HK$45K a year; rebalancing rules are set now (equities fall 20%: buy; drift 5
  points: rebalance); a quarterly review and an annual family meeting.
- Bar: "Chloe's degree is funded today, and each parent's money fits their own risk."
- Answers questions 2 and 6.

### 9 · Call 5: values and innovation, with guardrails (Win; 0:45)
- **"ESG from 11% to 25%…"**: a progress bar into the family's 20 to 25% goal band, of HK$10.47M; the three holdings
  (BOC-Prudential MSCI World ESG Index Fund; Allianz Green Bond; Sun Life MPF Global Low Carbon Index Fund).
- **"…tested, not trusted…"**: ESG ratings from different agencies agree far less than credit ratings (correlation
  about 0.54 vs 0.99; Berg, Kölbel and Rigobon, 2022), so each equity fund must pass two ratings (MSCI A or better,
  Sustainalytics risk below 20) and each green bond fund the ICMA principles; a downgrade means replacement within
  three months; no return premium assumed.
- **"…and crypto sized for each person" (defend):** not yes or no but form, size and custody: Adrian 0% (a tokenised
  money-market fund counts as cash); Carmen up to 2% through an HKEX spot ETF; Ryan keeps his HK$500K but adds no new
  money, so its share glides from about 74% of his wealth to 20% by 35; Chloe none while studying. Regulated channels
  only (HKEX ETFs, SFC-licensed platforms). The alternative: a forced sale, which overrides his conviction and could
  push him to unregulated channels.
- Bar: "Their values and Ryan's conviction both fit, without risk the family can't carry."
- Answers questions 3 and 4.

### 10 · Will it hold? (Lookbua; 0:30)
- **"Tested against the worst…"**: paired bars per test, the four decisions alone vs the full plan: Adrian's job ends
  at 60 ({{adrian60_89}} → {{rec_adrian60_89}}), low returns every year ({{stressA_89}} → {{rec_lowret_89}}), inflation
  and medical costs ({{stressB_89}} → {{rec_stressB_89}}); Carmen lives to 95: {{guardswitch_95}} (measured).
- **"…every risk has a named defence…"**: the risk register in brief (proposal Figure 26): suitability (one risk
  profile per person), crypto rules (licensed channels), greenwashing (two ratings), model risk (compare decisions,
  not forecasts), the business unsold (buy-sell agreement now).
- Footer: we compare decisions in the same 10,000 markets, we don't forecast them; premiums are from rate cards until
  quotes arrive; the tier switch is guaranteed under the VHIS rules.
- Bar: "It holds when the hardest things happen, and it starts this month."

### 11 · What happens when (Lookbua; 0:30)
- One dated sequence (a true sequence, so a line): month 1 the papers, the joint account, idle cash moved; months 1 to
  3 the cover; months 1 to 6 a portfolio each, the investment policy signed, voluntary MPF; month 12 the first family
  meeting (charter, Ryan's plan, the one-person budget); 2028 Chloe's offer, fees converted; 2032 managers built up;
  2037 mortgage cleared, Adrian's annuity, the home released; 2039 Carmen's annuity, the business sold, rules begin;
  2047 the medical review.
- Under it, the reviews: quarterly portfolio, annual family meeting, a full review after a death, a disability, a
  business sale, a 20% market fall or a 1.5-point rate move (proposal Figure 23).
- Bar: "For the Wongs, it starts this month; for Ryan and Chloe, it lasts beyond it."

### 12 · What passes on (Pete; 0:25)
- **The payoff of slide 3:** in the {{own_sold_pct}} of futures where their own way sells the flat, what Ryan and
  Chloe inherit in the same markets: their own way {{own_legacy_sold}} vs the plan {{plan_legacy_sold}} (two bars, the
  plan in the accent; the plan leaves more in {{plan_legacy_more_pct}} of them; today's money, measured).
- **"…passed on in stages, with a purpose"**: mirror wills, staged trusts at 25, 30 and 35, a guardian for Chloe; a
  named scholarship in sustainable design, about HK$30K a year, joining Carmen's mission and Chloe's interest.
- Speaker notes: across all futures, the home choice at 65 (keep {{legacy_keep}}, reverse mortgage {{legacy_rmp}},
  downsize {{legacy_down}}); MPF to the estate (no nomination); estate duty abolished in 2006, so succession is about
  control, not tax.
- Bar: "Built to last: for their lifetimes, and after."

### 13 · Wealth Management Connect (Pete; 0:40)
- The two flows between Hong Kong and Macao and the nine mainland Greater Bay Area cities; the advice rule on
  Southbound (without the investor's request or agreement, Hong Kong banks don't solicit or recommend across the
  boundary; HKMA Southbound page, checked 22 Oct); facts: since 2021; up to RMB 3M per investor since 2024 (RMB 1.5M
  each if both a bank and a securities firm); securities firms admitted in 2024; eligible products low to medium-high
  risk, non-complex (HKMA, checked 18 Oct).
- For the Wongs: Northbound kept out today (home, income and business already in Hong Kong); it comes in at the
  annual review if Adrian's work moves across the boundary. For us: a clear, suitable answer when the client asks.
- Bar: "Under the Connect, an adviser's value is a clear, suitable answer when the client asks."

### 14 · Who we want to become (all; 1:10)
Four cards: the goal in five years, what this plan taught each of us, the link to the Connect (personal statement,
proposal p.14). **Win's line is a draft for Win to confirm; Lookbua's edited line needs his OK.**

### 15 · Close (Pete, all; 0:15)
"Built to Last"; the five calls in one line each; the home their choice; the inheritance kept; the team; "Thank you."

## 6. The look
**23 Oct: the deck's identity** (Pete: "all default fonts with no clear design work"; e-Sentry has a clear style; slide
2 a weak first impression). Look B's structure stays; its "no motif" plainness goes.
- **Type:** EB Garamond, the written case's own display face, for titles (35 px), panel headings (22 px) and big numbers
  (lining figures), so the deck and the PDF are one brand; Inter for all text (Pete liked it for small text).
- **Colour:** the written case's crimson #A81E2D as the accent (#6F1320 deeper); its family for fills: wine #7D1D2A
  (the conclusion bar, the home layer, the family panels, cost bars), rose #E6CBCF and #D3A1A8 (savings, lighter
  series), tint #F7ECED; warm neutrals tuned to the crimson (mist #F5F1F0, rule #DDD6D4, grey #A69E9C, slate #5A5250,
  ink #1B1716). No blue. Events on wine-and-rose charts in ink.
- **One decorative idea: the house we build** (Pete chose it, 23 Oct, over the lifeline and over no thread). "Built to
  Last" drawn as a house from the written case's pillars (`round2/house.py`): the foundation is Call 1 (protected
  first), the walls Calls 2 and 3 (income that lasts), the rooms Calls 4 and 5 (a place for every voice), the roof what
  passes on. Slide 4 draws the whole house as the answer, built part by part as the calls are named; each call slide
  carries a small house beside its title (built parts wine, this call crimson, the rest dashed); the close shows it
  complete. The lifeline ruler is gone; time stays where it is data (the axes of slides 2, 3, 7, 11).
- **Signature:** a short crimson mark before every kicker (the call's numbered square on call slides); the cover's
  crimson bar; the family on a wine panel (cover, slide 2).
- **Not used:** gridlines across chart areas; grey-only charts; blue. (The footer tracker is back on trial, §4.)
History: look B (Swiss, cobalt, Archivo Narrow + Inter) chosen 20 Oct; crimson 23 Oct; this identity 23 Oct.

## 7. Images (one illustrated set)
One consistent flat-illustration set (Pete, 20 Oct), in look B's palette, no text in any image, every person labelled
fictional. Prompts are written for Pete's image tool; the four existing portraits (`img/*.jpg`) are the style
reference. Needed:
- the family together (cover and close);
- the family's flat (slide 3: the home their own way sells; slide 6: the home put to work);
- Carmen at 89 (slide 7: the futures that now reach her 89);
- Carmen's sustainable-packaging business (slide 6: sold in stages);
- Chloe at university (slide 8);
- optionally, the four of them at the annual family meeting (slide 11 or 12).

## 8. Evidence the deck is waiting for

| Evidence | Slides | Owner | If it doesn't arrive |
|---|---|---|---|
| ~~Insurer allows Flexi → Standard at 75 without new underwriting~~ | 7 | Fahtai | **Done 23 Oct:** guaranteed under the VHIS rules (Code of Practice s.2.11; FAQ Q30) |
| ~~HKMC reverse-mortgage payout for a borrower in their 80s~~ | 3 (notes) | Fahtai | **Done 23 Oct:** it lets Carmen stay, but in Fahtai's test the money lasts less often than selling; slide 3 keeps "sells" (`reviews/round2-fact-checks-fahtai.md` §b) |
| ~~HKMC annuity terms if Adrian dies soon after buying~~ | 6 (notes) | Fahtai | **Done 23 Oct:** the premium comes back, as a lump sum (premium less payments) or paid on to 105%; in the notes |
| Win's careers line; Lookbua's OK on his | 14 | Win, Lookbua | Use the manuscript's wording; Win's card says "investment and ESG" only |
| The illustrated set (§7) | 1, 3, 6, 7, 8, 15 | Pete | The four existing portraits; no scenes |
| BOC-Prudential fund's own fee and a channel without the 5% initial charge | 8, 9 (notes) | Win | "≈HK$45K a year" stays as in the written case |

## 9. Facts to check before they go on a slide

| Slide | Fact | Status |
|---|---|---|
| 13 | Connect: RMB 3M per investor, securities firms admitted in 2024, advice only when asked | Checked against HKMA, 18 and 22 Oct |
| 13 | "RMB 150bn each way" (in the written case) | Southbound quota shared by Hong Kong and Macao; don't say "each way" unless Northbound is checked; not on screen |
| 9 | ESG ratings correlation 0.54 vs 0.99 (Berg, Kölbel and Rigobon, 2022) | In the written case; quote as "about" |
| 5 | Premiums from 2026 rate cards and the market range | Labelled "quotes to follow" |
| 3 | "The home where they raised Ryan and Chloe": bought 11 years ago (case p.2), when Ryan was 13 and Chloe 5 | Case |
| 3, 6, 7, 10, 12 | Every model number equals `numbers.json`; the ones also in the PDF equal the PDF | Filled from `numbers.json`; compare the filled deck with the PDF's text before recording |

## 10. Hard questions (no Q&A in Round Two; the Final has ten minutes)

| Who asks | Question | Answered on |
|---|---|---|
| A practitioner | "They'd just sell the flat if they had to." | 3: we tested it; the sale comes at about {{own_sale_age}}, buys two to three years, and the inheritance pays the bills |
| A practitioner | "Couldn't they take a reverse mortgage at 83 and stay?" | Yes, and she could stay; but the fixed payout doesn't cover her bills, so in Fahtai's test the money lasts less often than selling, and the loan still eats the inheritance (slide 3 notes) |
| A practitioner | "A widow spending the couple's full budget? Your own way is a straw man." | 6 (notes): about half of the rise is the survivor budget; even with it cut in their own way, deciding the home, business and MPF now adds about ten points |
| A practitioner | "Why not rent, or buy cheaper than HK$7M?" | Either releases more; we use the same flat as our own downsizing option, so the two ways compare on the same terms |
| A judge with the PDF | "The written case says 33%; why 62% now?" | 3 footer: 33% is investments alone; 62% is their own way, the fairer start |
| An insurance adviser | "Why term cover, not more whole-life?" | 5, defend panel |
| Carmen | "Why sell my business, not keep it for dividends?" | 6 (notes): the dividend stops when she stops; even unsold, {{biz_not_sold_89}} |
| Adrian | "Do we have to leave our home?" | 6: they choose at 65; the reverse mortgage keeps them in it |
| A sceptic | "The annuity barely moves the odds; why buy it?" | 6 (notes): insurance for the worst markets: {{ann_w1_with_real}} vs {{ann_w1_without_real}} |
| A risk head | "What if Adrian loses his job before 65?" | 10 |
| A regulator | "Are these products suitable and licensed?" | 8, 9, 10 |
| An ESG judge | "How do you know these funds aren't greenwashing?" | 9 |
| A fintech judge | "Why let a 24-year-old hold 74% in crypto?" | 9: his money, about 2% of family wealth, no new money, glide to 20% |
| Any judge | "10,000 simulations: false precision?" | 10: we compare decisions, not forecasts |

## 11. Compliance and logistics (a breach can disqualify)
No university name, logo, campus, clothing, lanyard or account in any frame or file; files named "Axis"; PowerPoint
and MP4 metadata scrubbed (Office stamps the signed-in account: never submit an Office-exported PDF; `Fin Plan.pdf` in
the repo root is one, and is git-ignored); deliver by hand on Monday morning with a download link emailed as a backup.

## 12. From v8 to v9 (22 Oct)
- **The problem before the answer:** v8's "where they stand" split into "on paper, secure" (2) and "their own way" (3);
  the answer moves to 4 and still arrives at 1:30. 15 slides, 9:30.
- **"Their own way" replaces "investments alone"** as the baseline (Pete: a strawman). Measured, with the home and the
  inheritance as the emotional thread (Pete: "the home they have lived in", "what could have passed to the next
  generation"): slide 3 sets it up, 6 answers it, 7 redraws it, 12 pays it off.
- Call 2 retitled "Decide now, not at {{own_sale_age}}"; "more shares" moved to its notes. The medical premiums move from
  the problem slide to Call 3. Lookbua reads 11.

From v7 to v8 (20 Oct): the argument (the family's eight questions → five defended calls); the look (§6); the system
(§4: six type sizes, one grid, one navigation device, panels and a bar on every content slide). The v7 deck stays in
git (commit ad76533) and its source in `archive/`.
