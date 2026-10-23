# Built to Last, Round Two: Deck Plan (v10, "Their own way, then five calls", the house we build)

**Status:** v10, 23 Oct 2026. The story is v9's (agreed 22 Oct: the problem before the answer, "their own way" as the
baseline, Lookbua reads slide 11); v10 is the design pass (Pete, 23 Oct: "the story is ok, the pages are not"): the
house as the deck's idea, and a picture that portrays each slide's point (§6, §5). §4 rewritten the same day from a list of
required parts into tests, a few fixed things and a toolbox (Pete: the rules were locking the results into one way). The talk, timed, with the full draft script: `round2/Talk_Outline.md`. Look B chosen (20 Oct, §6).
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

## 4. What every slide must do, and what's open
**Rewritten 23 Oct** (Pete: the instructions were locking the results into one way, below standard). This section used to list the
parts every content slide must have: kicker, panels whose headings read as one sentence, a lede, a hero number, icons,
a conclusion bar, a trade-off strip on call slides, a footer tracker. Every built slide got all of them, and even the
unbuilt placeholders got a bar. It now holds the tests a slide must pass, the few things that are fixed, the pieces we can use, and
the failures we've already seen. Each slide's form is chosen for its point.

**The tests** (each slide, then the whole deck on a contact sheet):
1. **Would a world-class financial planner, pitching to this family, put this on screen?** (Pete, 23 Oct.)
2. **One point in five seconds.** The title states it. The one thing that proves it is the largest type in the body and
   the only accent; everything else is quieter.
3. **Its claim is shown, not argued.** A measured comparison where one can be run (the obvious alternative in the
   model, drawn beside the call, as Call 2 does with their own way), a chart with the one thing marked, a ledger with
   one figure a row; not a paragraph.
4. **It reads alone.** The PowerPoint is scored on its own (Pete, 23 Oct), so a reader without the voice gets the claim
   and the facts behind it. The reasoning is spoken and lives in the speaker notes; the claim and the focal number are
   always spoken.
5. **It moves the story.** It answers what the last slide left open and leaves the next question; the problem comes
   before the answer (§2). Nothing on it repeats the title, another part of the slide, or an earlier slide.
6. **As simple as it can be while the point stays clear** (Pete, 23 Oct): fewer pieces, never a vaguer message.

**Fixed** (constraints, on every slide):
- 1280 × 720. Nothing meant to be read under 14 px: the judges may watch on Zoom.
- The identity (§6) and the tokens in `src/00_head.html`. One type scale in Plus Jakarta Sans, so the deck looks like one deck: kicker 14
  semibold crimson · title 29 bold · panel heading 17 semibold · body and bold label 16 · small 14 · tag and source 12 · numbers 40 and 72 (76 for
  slide 2's net worth). Use these sizes rather than new ones.
- A 12-column grid with 48 px side margins and 24 px gutters. How a slide divides it is open.
- One gap of 26 px between the title and whatever comes under it, on every content slide (Pete, 24 Oct: each slide
  had its own, 14 to 22 px, and the tight ones pressed the content against the title).
- Every model number is a `{{key}}` (CLAUDE.md), tagged as a quiet "(measured)", "(case)" or "(sourced)": MEASURED is
  the team model (`numbers.json`), CASE the case, SOURCED a named public source.
- Builds reveal in speaking order (`data-b`) and grey what is still to come, so the layout never moves (Pete, 23 Oct),
  except where the grey would give the payoff away (the ten futures reveal). `make.py --builds` writes one frame per
  step (`Axis_builds.html`, `build/frames/`) for the video.
- Each call (5 to 9) shows on the slide what the family gives up for it (Pete, 23 Oct: a planner names the cost before
  the client asks, and the judges score "client suitability awareness"). Where and how it shows is open.

**Defaults** (break one when the slide is better for it, and say why in its §5 section):
- Charts: grey or rose series, the accent only on the value the title claims, labels on the data rather than legends,
  axis text 14 px, no gridlines, events anchored to the axis. Crimson marks a point or a number, never a wall of lines.
- The kicker names the section; the footer carries the source (two lines at most; the detail goes to the notes), the
  page number and, on trial pending Pete, a quiet section tracker (The problem · The answer · The five calls · Will it
  hold · What next · Us).
- Density: a dense slide reads well at about 120 to 180 words. **A warning, not a limit:** never make a phrase vaguer
  to meet a count.
- The script: about 1,200 spoken words in all, until the team's timed read-through sets the real cap
  (`Talk_Outline.md`).

**Pieces we can use** (none is required; each earns its place on a slide or stays off it):

| Piece | Earns its place when | Leave it off when |
|---|---|---|
| Two or three panels whose headings read as one sentence | the point is a chain of steps | the point is one picture, one number or one comparison |
| The conclusion bar (crimson, white text, centred) | the slide needs a handover its title doesn't give | it would restate the title or the panels |
| A one-line lede under a heading | the content needs a bridge to make sense | the heading already says it |
| A reading under a chart (dashed box) | the chart doesn't speak alone | it would repeat the chart's labels or the title |
| One dashed ring | one moment on a chart matters most | nothing stands out more than the rest |
| Icons | they name a real thing (the home, the pension, the business) | they decorate, or every row gets one by habit |
| The small house by a call's title | it shows where the call sits in the plan | the slide already draws the house |
| A picture from the image set (§7) | a real person or place carries the stakes | it pushes out evidence the slide needs |

**Failures we've seen** (add here, with the reason, instead of adding a rule):
- **v7: 40 font sizes, about ten navigation items a slide, a different grid on every slide** (before 20 Oct), plus
  question pills, "slide 5's…" references and tags inside sentences. This is why the scale and the grid are fixed.
- **A third of Call 2 restating the written case's headline** (Pete, 20 Oct). The repeat took the space the new fact
  needed.
- **"Many disconnected text, we're just pushing out text everywhere"** (Pete, 20 Oct): labels floating away from what
  they explain, captions repeating the title. Attach every label to its thing; say each thing once. But the fix for
  clutter is fewer, connected pieces, not fewer facts (Pete, 20 Oct, on Call 2 v6).
- **"A document put into a powerpoint slide format"; "boxes of information with no clear visual guideline"** (Pete,
  19 and 23 Oct): rows of text hiding a shape, no entry point for the eye, no mark on the one thing to see.
- **The result shown before the problem** (19 Oct: slide 3 drew the plan's result and killed the tension).
- **Too many accents** (19 Oct: crimson nine times on one slide; four 32 px numbers out-shouting the point).
- **A phrase made vaguer to meet a word count** (23 Oct: slide 4 lost "forced").
- **Unlike things listed as equal rows** (a cost, a safety margin and a legacy side by side). Rank by what the evidence
  says matters; small items go to a note.
- **A section with a topic label and a flat list** (Pete, 23 Oct, slide 9's "How a fund gets in": "except from the
  bold I don't really know what to focus on, what the chart is telling"). It had no claim to enter on, a chart with no
  annotation saying what it shows, no ending, and an ink rule that made it compete with the panel headings. Every
  block needs a way in (an icon and a bold claim), the finding written on its picture, and a way out (what happens
  next, or when it fails); a sub-section looks subordinate (no rule as heavy as a panel heading's).
- **Two typefaces splitting the hierarchy** (Pete, 23 Oct evening): one family; size, weight and colour do the work.
- **One device on every slide** (23 Oct, from the reference decks: a takeaway box, a chevron, a crimson punch-line in
  every panel) reads as a template, and so did this section's old list of required parts (23 Oct).

## 5. Slide by slide
Each spec: the point, the evidence and its keys, and the form as built so far. The form is a draft, not an order
(§4): when a better one fits the point, change it and record here what changed and why.
The scripts are in each slide's speaker notes (`round2/src/*.html`); `make.py` writes them to `Axis_Script.html`.

### 1 · Cover (Pete, all; 0:20)
"Built to Last", the promise line, the team; an illustration of the family (image set, §7). No numbers.

### 2 · On paper, secure (Pete; 0:30)
**Rebuilt 24 Oct, layout A** (Pete chose it over "the family as the hero" and over keeping the rows). The 23 Oct build
repeated the cover (the four faces, names and wants) and slide 3 (its timeline's milestones are on slide 3's axis),
and Ryan's row carried no event. Now two pieces for the title's two halves: "What they have today…", redrawn the same day as one picture (Pete:
four separate numbers were not the way, and the slide felt empty): what they own, HK$27.2M, as a bar to scale (the
home in wine as on slide 3, the business, investments, MPF, cash marked "30 months of spending"), what they owe,
HK$2.8M, on the same scale ("10% of what they own"), and HK$24.4M net worth beside them, the only accent, with "41% of
after-tax income saved each year" under it and "…and the forty years it has to last": one line from
2026 to 2066, the four faces as markers (Ryan, his own plan from now; Chloe, university 2028 to 2032; Adrian retires at
65 in 2037; Carmen at 62 in 2039), the retirement years shaded, "Both retired from 2039: 27 years paid from what they
own", and the end marked "2066: Carmen is 89, the money must last to here". Builds: the line as the people are named,
then the strength. The portraits will be regenerated with one detail from the case each (Image_Prompts.md §6). The
earlier specs below are superseded.
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
**Revised 24 Oct** (Pete: the right side conflicted for attention; too many annotations on the chart; not every text
deserves bold; the descriptions under the years were not emphasised enough). Right: one focal point, "What Ryan and Chloe
inherit, where the flat is sold": HK$24.4M today as a grey bar, {{own_legacy_sold}} left as a crimson bar on the same scale
(width [[own_legacy_sold_w]] from series.py) and the only big number; {{own_sold_pct}} and {{own_89}} as small supporting rows (a
small icon, a 28 px number, no bold); "Why it runs out" a quiet note, its two causes side by side (second pass the same day: Pete found it crammed and the
spacing odd; the right side is now three groups, the odds, the inheritance, the causes, each opening on a thin rule, with
equal gaps). Left: area labels regular, only
the event bold in each event label ("The flat is sold", "Runs out again", with "Carmen 86, short of 89"); the reading
box under the chart removed (the run-out label carries it); the axis bold on Carmen's age and Adrian's events, the
years grey (shared with slide 7). Supersedes the notes below where they differ.
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
- **Under it, the reading** (dashed box, under the axis): "In this future, **even selling the home does not carry Carmen
  to 89.**" (23 Oct: the earlier wording repeated the chart's own labels; the reading says what they mean.) The second
  label reads "Runs out again at {{story_out_age}}".
- **Right:** three icon rows from the 10,000 futures: {{own_sold_pct}} sell the flat (Carmen about {{own_sale_age}},
  usually alone); {{own_89}} see the money last to 89, even after the sale; then the focal row, stacked, the only
  crimson: {{own_legacy_sold}} (46 px) left to Ryan and Chloe where the flat is sold, of HK$24.4M today. On the panel's
  floor, level with the reading, **"Why it runs out"** on mist: 61% of their wealth pays nothing until sold (home and
  business); HK$375K a year of medical premiums, outside their budget (both typed in the written case). The two causes
  Calls 2 and 3 fix. **It stays on slide 3** (23 Oct, density check at 205 words): the diagnosis belongs before the
  answer on slide 4, so the cuts went to repeats instead (about 190 words now, with the chart's labels).
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
- **Trade-off** (23 Oct, written case §8): "Term cover costs a fraction of whole life, but it lapses at 65 and 62;
  after that, their existing policies and savings carry the risk." It replaces the line "Term, not whole life: the need
  ends at retirement" (the reason, not the cost).

### 6 · Call 2: decide now, not at {{own_sale_age}} (Fahtai; 0:45)
**Rebuilt 24 Oct** (Pete: the same hierarchy problem as slide 9). Before: the wine income box (116%) was the darkest thing
on the slide and outweighed the result; the flow had no way in; the budget floated in a dashed box; the band only
restated the title. Now: three column labels ("What they own and spend" / "What each becomes, decided now" / "What it
gives them"); four rows, one per decision, so the four can be counted (the flat, the MPF, the business, their budget
HK$780K a year → a survivor plans on 70%); quiet destinations (mist, a wine rule, ink numbers); and the result as a bar
on one scale: grey to {{own_89}} (their own way), crimson to {{ladder_5_89}} (the only accent), dashed to {{switch_89}}
"with Call 3, next", so the slide shows what is left for slide 7. Builds follow the script: the home, the business, the
budget, the MPF and the income box, then the result. Same day, second pass (Pete: too many icons; left and middle
not aligned): no icons; each row is one band, the asset's grey bar (to scale) starting its own ribbon, the left and
middle labels above the line in the same metrics so they align. The earlier specs below are superseded.
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
- **Trade-off** (23 Oct, written case §9 and §3): "Staying in the home leaves {{legacy_down_vs_rmp}} less to Ryan and
  Chloe than downsizing would, and the annuities can't be undone." The band's "decided at 65, not forced at
  {{own_sale_age}}" is cut: it restated the title.

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
- **Trade-off** (23 Oct, written case §3): "The Standard plan has lower limits and fewer private-hospital choices;
  the spending rules trim typical spending by about {{guard_cost}} a year."

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
- **Trade-off** (23 Oct, written case §4): "Chloe's HK$2.57M stays in deposits and short bonds: safe for 2028, but it
  earns less than shares would." The connector now reads "The same HK$7.7M, with a job for each part" (it restated the
  title).

### 9 · Call 5: values and innovation, with guardrails (Win; 0:45)
**Built 23 Oct** (`src/05_s08-15.html`; about 225 words, the densest slide: it carries two of the case title's four
topics). Two columns, so it doesn't repeat slide 8's rows, in one language: grey today, the wine family the plan, crimson
only on 25% (the one number the title names). Left: "Carmen's values: ESG from 11% to 25%…": two bars on one scale over
the family's 20–25% goal band, the plan bar split into its three funds and labelled on the data; "like for like" (same
risk, no extra return) under the axis, because a practitioner asks that first. Right: "…and Ryan's conviction: crypto
sized for each person": one row a person on one scale, in rising size (Adrian none, Chloe none, Carmen up to 2%, Ryan
up to 74% today and 20% by 35, no new money). The guardrails, rebuilt twice the same evening (Pete: no hierarchy, so many things to focus on, left and right
repeated): each column now ends on one sentence under its own chart, on a wine rule, its lead in bold ("Tested, not
trusted: each fund needs two ratings ..."; "Held where a regulator watches: bought only through HKEX-listed ETFs or
SFC-licensed platforms ..."). The detail (ICMA, the three-month and 30-day rules, key recovery, the 0.54 against
0.99 correlation, like for like) is in the notes. Ryan's bar says its finding, "20% by 35, without selling". Builds in speaking order:
ESG → its test → Adrian, Chloe, Carmen → Ryan, the custody rules, the trade-off and the bar. Product names and the
downgrade rule are in the notes.
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
- **Trade-off** (23 Oct, written case §6 and §7): ESG funds cost a little more in fees and the choice is narrower;
  Ryan keeps his crypto, so a 70% fall would cost him HK$350K today (his cap brings it to 14% of his wealth by 35).

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
- **Type: one family, Plus Jakarta Sans, for every part.** Pete, 23 Oct evening: "keep one clear font for all of the
  parts", as in e-Sentry, which uses Barlow throughout; Inter first, then "I want a font that makes us stand out"; he
  chose Plus Jakarta Sans on 24 Oct from four candidates set side by side on one page (with Bricolage Grotesque,
  Schibsted Grotesk and Manrope). Weights 400 to 800, in `round2/fonts/`, SIL OFL, embeddable. The hierarchy comes from size, weight and colour, never from switching
  faces: with Garamond for numbers and Inter for labels, the same kind of thing (a share, an amount) looked like two
  kinds. EB Garamond stays the written case's face only.
- **Colour:** the written case's crimson #A81E2D as the accent (#6F1320 deeper); its family for fills: wine #7D1D2A
  (the home layer, the family panels, the guaranteed income, cost bars), a greyed rose #DDD0CD and #B99A9C (savings,
  lighter series), tint = mist; warm neutrals tuned to the crimson (mist #F5F1F0, rule #DDD6D4, grey #A69E9C, slate
  #5A5250, ink #1B1716). No blue. Events on wine-and-rose charts in ink. The conclusion is a crimson bar, white text
  centred (Pete, 24 Oct: without a bar the last line didn't read as a conclusion; it had been a line on a crimson rule
  since the evening before, after a wine block outweighed the focal numbers).
- **One decorative idea: the house we build** (Pete chose it, 23 Oct, over the lifeline and over no thread). "Built to
  Last" drawn as a house from the written case's pillars (`round2/house.py`): the foundation is Call 1 (protected
  first), the walls Calls 2 and 3 (income that lasts), the rooms Calls 4 and 5 (a place for every voice), the roof what
  passes on. Slide 4 draws the whole house as the answer, built part by part as the calls are named; each call slide
  carries a small house beside its title (built parts wine, this call crimson, the rest dashed); the close shows it
  complete. The lifeline ruler is gone; time stays where it is data (the axes of slides 2, 3, 7, 11).
- **Signature:** a 5 px crimson rule on the title block, kicker and title 14 px in from it, as in e-Sentry (Pete, 24
  Oct: the header was too big and its title competed with the panel headings); the cover's crimson bar (no dash before the kicker: Pete, 24 Oct,
  "not needed"); the family on a wine panel (cover, slide 2).
- **Not used:** gridlines across chart areas; grey-only charts; blue. (The footer tracker is back on trial, §4.)
**Reviewed 23 Oct, evening** (Pete handed the identity to Claude to judge). Kept: EB Garamond and the crimson. They read
as heritage and trust, they fit "Built to Last" and a family legacy, and they make the deck and the written case
(half the score, already in the judges' hands) one brand. Changed, rendered side by side first: (1) the wine
conclusion bar became a line, because it was the darkest thing on every slide, outweighed each slide's focal number and
repeated down the deck as a template; (2) the pale pinks became a greyed rose (Pete dislikes pale pink tints of the
accent; the old rose read as pink, not as the crimson's family). Known and accepted: Hong Kong screens show a fall in
red (綠升紅跌), so a crimson result could read as a loss for a moment; the arrow and the grey baseline beside each
result make the direction plain, so it stays.
History: look B (Swiss, cobalt, Archivo Narrow + Inter) chosen 20 Oct; crimson 23 Oct; this identity 23 Oct.

## 7. Images (one illustrated set)
One consistent flat-illustration set (Pete, 20 Oct), in look B's palette, no text in any image, every person labelled
fictional. Prompts are written for Pete's image tool; the four existing portraits (`img/*.jpg`) are the style
reference. Needed:
- the four portraits again, each with one detail from the case (Pete, 24 Oct: the current ones read as generic);
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
