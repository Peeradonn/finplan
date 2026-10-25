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
| 2 | Meet the Wongs | On paper, the Wongs are secure, for a plan that must last forty years | Pete | 0:40 |
| 3 | Will it last? | Their own way, Carmen is forced to sell the home at about {{own_sale_age}}, too late to save the money or the inheritance | Pete | 0:45 |
| 4 | Our answer | Five calls make their wealth last, on their terms | Pete | 0:45 |
| 5 | Call 1 · Protection | Insure the income, not the life: about HK$100K a year closes every gap | Lookbua | 0:40 |
| 6 | Call 2 · The home and the business | Decide now, not at {{own_sale_age}}: four decisions on what they own and spend lift the odds from {{own_89}} to {{ladder_5_89}} | Fahtai | 0:45 |
| 7 | Call 3 · Retirement | Fix the cost the budget ignores: in that same future, the money now lasts to 89 and the home stays theirs | Fahtai | 0:40 |
| 8 | Call 4 · Each person | One family policy, a plan for each person: every dollar gets a job | Win | 0:50 |
| 9 | Call 5 · Values and innovation | Values and innovation, with guardrails: ESG at 25%, crypto sized for each person | Win | 0:45 |
| 10 | Will it hold? | Tested against the worst: even if Adrian loses his job at 60, the plan holds | Lookbua | 0:30 |
| 11 | What happens when | It starts this month and closes every gap within a year; after that, dates trigger each step | Lookbua | 0:20 |
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

**Three minds to build with** (Pete, 24 Oct, after a table on slide 5: "think of the winning teams, the world-class
financial planner and an expert deck builder"). The winning team: each slide answers the judge's question of the
moment, with one picture of a change (before to after), and keeps the tension. The planner: one vivid what-if in the
family's own money, the biggest risk first, the price in their terms, never a product list. The deck builder: a
three-second glance, the voice carries the detail, builds pace the reveal, and tables go to an appendix, never into
the talk.

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
7. **An easy eye path, one focal point, nothing fighting** (Pete, 25 Oct): the reader can tell at once what to read
   first and in what order. Hierarchy comes from contrast, not from sameness: size steps by importance (the title's
   number largest; each block's claim a step up, 18-19 px; body 15 px with its key phrase in bold; annotations and
   asides small and italic, 14 px), and notes on the pictures where they need one. Crimson only on the number(s) the
   title names. Pete corrected a first reading of this (25 Oct): stripping bold made every line the same weight, the
   opposite of what he meant.

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
- Builds reveal in speaking order (`data-b`), so the layout never moves (Pete, 23 Oct). Since 25 Oct the dense slides
  (3, 5 to 13) **hide** what is still to come (class `reveal`; visibility keeps the space), so the video shows only what
  has been said: greyed text still pulled the eye while the speaker was on something else. Slides 2, 4 and 14 keep the
  grey, where seeing what is coming helps. `make.py --builds` writes one frame per step (`Axis_builds.html`,
  `build/frames/`) for the video; rebuild the frames after any slide change, before recording.
  **Recording in Zoom (25 Oct):** the team shares `round2/Axis_present.pptx` (`make_pptx.py`), where the same steps are
  PowerPoint clicks (a 300 ms fade each; hidden on the reveal slides, greyed on 2, 4 and 14), with Morph into Calls 1 to
  5 so slide 4's house glides into each call's corner, and no transition between any other slides (Pete, 25 Oct: the
  fade between slides went). The submitted `Axis.pptx` has the transitions but no builds, so
  a judge clicking through sees every slide complete. Checked in a video PowerPoint exported itself (slides 3 to 6, 13
  and 14): no blink on slide 4's last click, no stray shapes in the Morphs.
- Each call (5 to 9) shows on the slide what the family gives up for it (Pete, 23 Oct: a planner names the cost before
  the client asks, and the judges score "client suitability awareness"). Where and how it shows is open.

**Defaults** (break one when the slide is better for it, and say why in its §5 section):
- Shadows on objects only (Pete, 24 Oct): one soft wine-tinted lift (--lift) for portraits, slide 6's results,
  slide 8's planned pots and the conclusion bar; never on anything drawn to a scale (a shadow moves an edge, so a bar
  or area reads longer or thicker than its value).
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
| The conclusion bar (ink since 25 Oct, white text, centred) | the slide needs a handover its title doesn't give | it would restate the title or the panels |
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
- **The loudest thing on the slide wasn't the point** (deck review, 25 Oct; Pete: "so much text, no hierarchy, no
  clear eye path"). Measured on the renders: the crimson conclusion bar was 72-89% of all the crimson on slides 2, 6 and
  9-14, so the eye went to the conclusion before the evidence; crimson icon circles (five on 10, nine on 11) pulled it
  away again; slides carried 14-21 text styles and up to 13 font sizes; slides 10 and 12 each held a second message;
  the screen showed about twice the words the voice said (slide 10: 265 shown, 64 spoken). Fixed: the bar is ink;
  icon circles are quiet (mist, wine marks); the title's number is the largest type and the only crimson; one message
  a slide, the second one cut to a line and the notes. Check a slide at thumbnail size: the first thing you see should
  be the number the title names.
- **The voice said what we recommend, the screen said why and at what cost** (script review, 25 Oct). Every call
  slide showed "The price:", but no call said it aloud; "because" was spoken once in the whole talk; the family's goal
  (retire at 65 and 62 on HK$780K a year) was never said, so slide 3's odds came before anyone had said what they
  measure; and 9 of the 12 conclusion bars were never spoken, so on video the judges read one sentence while hearing
  another. A practitioner hears the reasons and the price, not the slide. Say the question before the first number,
  and say the reason and the price where they matter most; pay for them by cutting what the screen already shows.

## 5. Slide by slide
Each spec: the point, the evidence and its keys, and the form as built so far. The form is a draft, not an order
(§4): when a better one fits the point, change it and record here what changed and why.
The scripts are in each slide's speaker notes (`round2/src/*.html`); `make.py` writes them to `Axis_Script.html`.
**Script pass, 25 Oct** (review as a practitioner judge and a presenter; Pete approved all fixes). Spoken words 1,253
→ 1,257: the added reasons and prices were paid for by cutting what the screen carries. Slide 2 now asks the question
(the goal, then "will it last to Carmen's 89? We tested it in 10,000 futures", its bar), so slide 3's 33% and 51% have a
frame. Prices and reasons said aloud: slide 5's HK$22K a month if Adrian couldn't work; slide 6's annuities ("an income
each can't outlive"; "the price: the annuities can't be undone"); slide 7's premiums "close to half the budget" and
the Standard plan's lower limits; slide 9's two ratings "because raters often disagree", the regulated channels, and
Ryan's price (a 70% fall costs him HK$350K). Ear fixes: slide 6's "after the first death, the survivor plans on 70% of
the budget"; slide 10's 83% now follows "Here", so it isn't heard as slide 6's 83%; slide 5's "so Carmen's business
survives her" (the old "her" pointed at Chloe); slide 8's "one family investment policy" (it followed the insurance
slide); slide 9's "on the SFC's ESG list" (not "SFC-listed"). Cut from the voice, still on screen: slide 2's 41%,
slide 5's 14% of surplus and the wills list (wills are said on 11 and 12), slide 7's rule mechanics, slide 11's later
dates and first-year tail, slide 13's Adrian clause. Times: slide 2 0:30 → 0:40, slide 11 0:30 → 0:20 (total 9:30).
Left for their owners: Win's line, Lookbua's "systems risk" (if he means a shock crossing markets, the finance term is
"systemic risk").

### 1 · Cover (Pete, all; 0:20)
**The written case's photograph, 25 Oct** (Pete asked whether the cover was ideal; four covers were rendered side by
side: the illustrated family on wine, the written case's photo in colour and in a wine duotone, and a stock beach
photo). Now the right panel is Peter Steinhauer's *Cocoons* (Hong Kong towers under construction, in green netting),
credited on the photo. Why: the judges hold the written case with this cover (half the score), so the deck and the
document share one picture; it is Hong Kong; buildings under construction open the deck and the finished house closes
it (slide 15); and the cover no longer repeats slide 2's four portraits. The beach photo was 547 px wide (soft at
video size), showed two small boys (the Wongs' children are 24 and 16), clashed with the crimson and had no known
licence; the duotone read gloomy. **Open: the photograph is credited but no licence is on file; ask the photographer
for permission, or go back to the illustrated family (git history) if the risk isn't wanted.** No numbers.
Before 25 Oct: "Built to Last", the promise line, the team; an illustration of the family (image set, §7).

### 2 · On paper, secure (Pete; 0:40)
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
**Fourth pass, 24 Oct** (Pete: do we need the big house chart, or can the space be used for something else? Look at
the annotation). The 100 houses are gone: they said {{own_sold_pct}} a second time, under the number that already said
it, and were the slide's largest block of crimson, pulling the eye from the chart and from {{own_legacy_sold}}. One
split bar (sold in wine, kept in rose, its width straight from {{own_sold_pct}}) shows the same half in one line. The
freed height went to the two blocks that remain (51% at 48 px, bars 38 px, {{own_legacy_sold}} at 60 px), not to new
content: "Why it runs out" stays in the notes (third pass, below). The chart's events are now a dot on the data with a
leader up to a label in the white space (no ring, no line to the axis). Both labels read the same way, event and age
in bold and the consequence quiet: "The flat is sold, Carmen {{story_sale_age}}: when her savings are gone"; "Runs out
again, Carmen {{story_out_age}}: then unpaid bills eat into the smaller flat". The second label now explains why the
home layer shrinks after 86 (the model nets unpaid bills against the smaller flat); "short of 89" said nothing a judge
could check. Trade-off: the run-out label sits above the sale label, so reading top-down meets the later event first.
That is the only order in which neither leader crosses a label; the dots and the builds keep the sequence.
**Retitled 24 Oct** (Pete: if the problem is "51% sell the home" and the plan releases it with a reverse mortgage,
isn't that conflicting?). The model says the home pays either way: kept untouched, even the plan lasts in only
{{prop_keep_89}}; the written case calls downsizing the stronger option. So the harm is now worded as what the model
shows, forced, late and not enough: "Their own way, Carmen is forced to sell the home at about {{own_sale_age}}, too late
to save the money or the inheritance", and "{{own_sold_pct}} of futures are forced to sell the home". Slide 6's flat row
says "they stay, with a reverse mortgage, or downsize: their choice". The objection and its answer are in §10.
**Right side, third pass, 24 Oct** (Pete: still conflicting; the point is clear but it takes time to understand).
Cause: six numbers on screen (51%, 62%, HK$24.4M, HK$2.3M, 61%, HK$375K), three of them percentages of different
things, two never spoken, so the eye read one thing while the voice said another. Now only what is said, in its
order: "{{own_sold_pct}} of futures sell the home" as 100 small houses with the sold ones filled ([[own_sold_icons]],
series.py, from the model), then what Ryan and Chloe inherit (HK$24.4M today, {{own_legacy_sold}} left, the focal
point). {{own_89}} moves to the notes (it is slide 4's baseline); "Why it runs out" moves to the notes too, reversing
23 Oct's choice, since slides 6 and 7 show and fix each cause (the home and business put to work; the HK$375K
premium line).
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
**Rebuilt 24 Oct: the house as an exploded 3D model** (Pete: the elevation was too simple; he asked for both a coded
exploded 3D house and a realistic AI render). `house.exploded()` draws a flat dimetric model: the foundation, two floors
of two blocks and an overhanging roof pulled apart, each floating layer casting a soft shadow on the one below; windows
and a door make it a house; colours step from a dark wine foundation to a pale roof, each face shaded. The number badges
sit at each face's outer edge so the leader lines leave the model at once; callouts align on their titles. Builds: a
grey draft, each block crimson (shading kept) as its call is named. The realistic render's prompt is Image_Prompts.md §7;
when it comes back it can replace the model under the same labels, but its parts cannot light up one by one.
**Same day, the reveal** (Pete: keep it 3D in code, no AI; make it unmistakably the answer reveal; look at density).
Treatment A, "the stage", chosen over B, "the spotlight" (the white page with a rose glow), after both were rendered
side by side: a dark wine stage lit from behind the house, the only dark slide after the cover (it echoes the cover's
wine panel); the house in light tones (`house.exploded(palette="light")`); white text; 97% in white, the brightest
thing on the slide; the bar stays crimson on the stage's darker foot. Each call's callout carries an icon that names its
subject (shield, home, pulse, people, leaf, gift) and its number, which fills the empty third the density check found.
Builds: the house a faint ghost, each block glowing white as its call is named. Second pass the same day (Pete: two
long horizontal bars at the bottom, keep one, the result box; the heading too long): no conclusion bar on this slide
(its handover is spoken; the one exception to the bar), the result box the only ending; the title shortened and set
larger on one line, "Five calls make their wealth last, on their terms", answering slide 3's bar ("when, and on whose
terms"); "innovative yet prudent" stays in the spoken opening; the house larger in the freed space. The elevation
notes below are superseded.
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
**Hierarchy pass, 25 Oct evening** (deck review, Pete: no eye path). The curved arrow "his cover closes the gap" is
gone: the deck's lessons rule out hand-drawn curves, the two columns are too close for a straight arrow with a label,
and the bills line, the dashed gap and the bracket already show the gap closing. Builds now hide what is still to come.
**Presentation pass, 25 Oct** (Pete: slides 5, 7, 9, 10 present their points poorly). The trade-off strip is gone: its
price now ends the covers ("The price: term cover lapses at 65 and 62 …", on mist). The papers checklist (five ticked
boxes) is one line at the panel's floor, since Lookbua speaks them and slides 11 and 12 show them. Content text in ink;
the bar list breathes.
**Rebuilt again the same day around one scenario** (Pete: a big table is not a presentation). Left: "If Adrian
couldn't work tomorrow…", the household's money each month against its HK$82K of bills: today Carmen's HK$60K leaves
HK$22K short every month (a dashed gap); with the plan his cover, HK$65K a month to 65, lifts them over the line
(Carmen's own: HK$39K to 62, in a note). Right: "…so we insure the income first", HK$100K a year, 14% of their
surplus, the four covers as chips with their prices, Ryan in one line, then the five papers within three months.
Builds follow the script: the gap, the cover, the four covers, the papers. The scorecard below is superseded.
**Built 24 Oct as a gap scorecard** (Pete: not good yet, covering so many things; invent a layout if three
panels don't fit). The three panels (the income gap as bars, the HK$100K split as a stacked bar with a legend, the
papers as a checklist) spoke three visual languages for one claim. Now one form: a row per risk, in the case's own
list of what they have (p.4): can't work, seriously ill, in hospital, dies, can't decide or no will, the business
loses Carmen; Today (a cross, or a dash where cover is partial) against With the plan (a tick), what each costs a
year as a bar to scale, and the total, about HK$100K a year, 14% of their surplus, the one crimson number. Ryan and
the average premium sit in one quiet line. Builds: the gaps first, then each row closes in the order Lookbua says it.
The earlier specs below are superseded.
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
**Hierarchy pass, 25 Oct evening** (deck review). 116% was larger and higher than the title's 83%, so it was read
first: the three destinations now share one quiet size (26 px) and 83% is 60 px, the slide's only crimson. The
trade-off strip is a price line under the result ("The price: staying in the home leaves …"), as on Calls 1, 3 and 5:
the strip, the result bar and the conclusion bar had stacked three bands at the foot. Builds now hide.
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
**Left redrawn, 25 Oct late** (Pete: the content is fine, the look isn't; chose "clean chart + tiles" of three options,
over two big-number rows and before/after bars). The premium chart had no names on its lines and "HK$375K kept for life"
read as money saved. Now the caption is the chart's title ("Medical premiums a year, above the HK$65K the budget holds"),
the chart runs the panel's width without a y-axis, each line is named at its end in its own colour ("Flexi for life";
"Standard, after review", the end heights from series.py's `prem_flexi_end_t` and `prem_rec_end_t`), the peak carries
HK$375K, and the review is a thin marker labelled "Review at 75". Fix 2's rules are three icon tiles (40 px mist
circles, the label under each), so the two fixes weigh the same. Everything under a heading starts under its text.
**Hierarchy pass, 25 Oct evening** (deck review: the left panel was a slide of its own, 20 text styles). The left is
now the two fixes, each with its picture and its price; the numbered discs and rule icons are quiet (mist, wine). The
odds moved under the redrawn future, as its result across all futures: "In 10,000 futures: {{ladder_5_89}} →
{{switch_89}} last to 89 with the review; almost all with the rules". {{story_plan_left}} left at 89 is the one crimson
figure, 34 px (40 px narrowed the chart until its axis labels collided). The home's caption is 14 px (was 12).
**Presentation pass, 25 Oct.** Fix 2's three rules are a row of icons with short labels (pause, a 10% trim, a shield
for essentials) rather than a line of text, so both fixes have a picture.
**Third pass, 24 Oct evening** (Pete: heading 1 clashed with the chart's lines; grey text hard to read; is the
trade-off strip needed on every slide?). The review's label now sits inside the chart beside its line, so the line no
longer rises into the heading. Every content line is ink; grey (slate) is kept for the caption and the axis labels.
The trade-off strip is off this slide: each fix carries its own price as its last line ("The price: lower limits and
fewer private-hospital choices"; "The price: typical spending about {{guard_cost}} a year lower"). The trade-off is
still on the slide, where it belongs, which §4 requires ("where and how it shows is open"); the strip was the same
device on five slides.
**Second pass, 24 Oct evening** (Pete: not the deck's palette; "The cost:" and "The risk:" fought the title; text too
small, no hierarchy; does it need this much depth; would the planner, the winning team and the deck builder push it
out?). Not as it was. The left now leads with the two fixes, as the title does ("Fix…"): numbered 18 px ink headings
(the number in a wine disc, no crimson), each ending on its result. (1) "Review the medical plan at Adrian's 75":
the premium chart, a quiet caption, then {{ladder_5_89}} → {{switch_89}} of futures last to 89. (2) "From 2039,
spending rules for the bad years": the rules on two quiet lines, then "with the rules, almost every future lasts to 89".
The leanest-year figures ({{guardswitch_worst5_real}}, {{fixswitch_worst5_real}}) are unspoken, so they're in the
notes only, which already explain them. The right chart takes slide 3's fills (the home in the wine gradient, the four
decisions' savings in the rose gradient, what Call 3 adds a paler tint), so the payoff looks like the problem it
answers, and it is taller so both columns end level.
**Refined, 24 Oct evening** (Pete: cluttered; keep the depth that's needed, make it nicer, take out what isn't).
Fahtai's structure is kept (two things still break the plan, then the same future, fixed), with every number his
script speaks. Out: the "THE COST" / "THE RISK" chips and the italic highlights (now "The cost:" and "The risk:" in
crimson); both legends (the premium lines and the savings band are labelled on the chart); the three rule boxes (one
quiet line); the dotted leaders, their label stack and the ghost dots (the right heading now carries the thread: "…so
the future that ran out at {{story_out_age}} now reaches 89"); and the four-block bar (the deck's one-sentence bar:
"Will it last? In almost every future: they retire on time, keep the way they live, and keep the home"). Each left
block ends on its measured result: {{ladder_5_89}} → {{switch_89}} with the review, and her leanest year at
{{guardswitch_worst5_real}} or more in 19 futures of 20 ({{fixswitch_worst5_real}} without the rules). On the right,
the light band carries one label, "Added by Call 3", with a leader from white space. The one crimson number is
{{story_plan_left}} left at 89.
**Reworked 24 Oct (Fahtai): why, then the fix, then the result.** What the slide must say: after slide 6, two things
still break the plan, a cost (medical premiums outside the budget) and a risk (bad markets late in life); the review at
75 fixes the first, spending rules from 2039 the second; in slide 3's future the money now lasts to 89 and the home
stays theirs. Read left to right: the two threats, each with its why and its fix, then the payoff.
- **Left, "Two things still break the plan…":** *The cost*: premiums above the budget's HK$65K; the fix highlighted
  and in italics, *review the plan at Adrian's 75*; a key in the lines' own colours, same format for both ("Flexi, kept
  for life: up to HK$375K a year"; "Standard, from Adrian's 75: about a third of the cost"); in the chart "the saving"
  (in the saving's pink) and "Adrian dies" at the drop (the footer says why the drop). *The risk*, in two balanced lines
  mirroring the cost's: in the worst 1 future in 20 her leanest year falls to {{fixswitch_worst5_real}}; the fix,
  *spending rules from 2039* (highlighted), keeps it at {{guardswitch_worst5_real}} or more; the three rules as three short blocks (no raise after markets fall; trim 10% if drawing too
  fast; essentials never cut).
- **Right, "…so in slide 3's future, the money lasts and the home stays theirs":** the savings split in two, the four
  decisions alone (darker pink) and what call 3 adds (lighter): in this future the four decisions alone leave
  {{story_plan6_left}} of savings at 89, under a year of spending. "The home: still theirs", with the reverse
  mortgage's {{rmp_income}} a year from {{rmp_year}} (it shrinks because the loan grows against it: notes). Their own
  way dashed, slide 3's two events as dots, each label set on its dot's x with a dotted leader straight down; what
  is left at 89 in a gutter: {{story_plan_left}} with the plan (the accent). Their own way's
  {{story_own_left}} is left to slide 12 (Pete's call, agreed by Fahtai 24 Oct: one comparison, one set of numbers).
- **The bar as four blocks:** they retire on time | they keep their spending | they keep the home | {{ladder_5_89}} →
  **{{switch_89}}** of futures last to Carmen's 89 (the largest type on the slide). "Almost every future with the
  rules" is spoken and in the notes. Version B of two compared on 24 Oct (A: one line).
- Flat colours on this slide, no gradients (Fahtai, 24 Oct). Script: premiums, the review, the rules, the future, the
  odds (about 95 spoken words, was 80).
- Earlier drafts below.
**Endings marked, 24 Oct (Pete; carried into the rework above as the dots, leaders and the gutter; their own way's figure left to slide 12, as Pete wrote)** (with slides 10 to 15): the chart now says how this future ends, as slide 3 does. A
crimson dot at the plan's end with a leader up to "{{story_plan_left}} left at 89 · and still their home". Slide 3's sale
and run-out sit as hollow ghosts on their own way's dashed line ("sold, {{story_sale_age}}", "ran out,
{{story_out_age}}"). The comparison with {{story_own_left}} is left to slide 12, the payoff.
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
**25 Oct evening:** the trade-off strip is a price line ("The price: Chloe's HK$2.57M stays in deposits …"), as on
every other call since slide 6 lost its strip. Builds now hide. The layout is otherwise unchanged.
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
**Hierarchy pass, 25 Oct evening** (deck review: 13 font sizes, 21 styles). One scale: 14 for asides and labels, 16
body, 18 Ryan's claim, 17 the panel headings, 20 the supporting figures (74%, 32%), 40 the two the title names (25%,
20%, the only crimson). Bold leads and italic asides kept (Pete, 25 Oct). "Like for like, not a new bet" is one line
with its lead in bold, not a heading and a sentence. The curved "+14 points" arrow is a straight arrow from the end of
today's bar to where the plan's ends. Builds now hide.
**Four levels, 25 Oct** (Pete: keep bold and italic; vary the size by importance; annotate). 25% and 20% largest;
"Like for like, not a new bet" at 19 px and Ryan's line at 18 px; body 15 px with its key phrase bold; the fund
roles, the price lines and "(case)" in italic as asides; a note on Ryan's chart ("The dark block: his HK$500K, the
same at every age") in the space above his first column.
**White space and eye path, 25 Oct.** The gaps left by the text cut went to the charts (taller ESG bars, a roomier key,
wider and taller columns for Ryan, his text centred against them). Then the accents were cut to one per block: no
inline bold under "Like for like" or in Ryan's text, the fund amounts plain, the price labels in ink. Crimson is on
25% and 20% only, the two numbers the title names.
**Text cut, 25 Oct** (Pete: still too text-heavy). 253 words to 190. Kept: what Win says and what a judge needs to
trust it, one short line each ("the same risk, the same expected return"; "two ESG ratings per equity fund, or it is
replaced"; Adrian none, Carmen up to 2% (ETF), Chloe none; Ryan's savings go to a world index fund, so the crypto's
share falls; a 70% fall would cost him HK$350K; HKEX-listed ETFs or SFC-licensed platforms only). To the notes: the
rating thresholds and the three-month rule, tokenised cash, "while she studies", the rally trim, no lending or
leverage. The ESG bars and Ryan's columns are larger in the space freed.
**Presentation pass, 25 Oct.** The trade-off strip is gone: each half ends on its own price ("The price: ESG funds
cost a little more …"; "The price: Ryan keeps the risk; a 70% fall would cost him HK$350K today"). Ryan's columns are
wider and centred, the crypto block labelled HK$500K inside the first column instead of a legend at the side. All
content text in ink.
**Left column, second pass, 24 Oct evening** (Pete: still too full, no hierarchy, and the arrow pointed nowhere). Now
three levels, one job each. The picture: the arrow joins the end of today's bar to the end of the plan's, "+14 points"
under its curve, and "11%" sits inside today's bar so the arrow has a start. The key: one line a fund, in its segment's
colour (name, amount, what it replaces). The claim: a 16 px heading, "Like for like, not a new bet", and one quiet
sentence (sized by what it replaces; risk and return as Call 4 set them; every sector still held; no ESG premium). The
test sits on the floor, level with the right column's custody rule. Gone: HK$1.15M today (it's in the written case)
and each fund's longer description (in the notes and the written case §6).
**Reworked 24 Oct, evening** (Pete: the right side missed the main point, that Ryan isn't selling his crypto, we let it
size down over time; on the left, annotate the growth, and ask whether to explain why the world ESG index, why MPF
low-carbon, why these sizes, and the financial side of risk and diversification). Verdict: yes, one line each, because
"what does ESG cost in risk and return?" is a practitioner's first question, and the written case already answers it
(§6). Left: a crimson arrow from 11% to 25%, "+14 points". "Like for like, not a new bet: each fund is sized by what it
replaces, so risk and expected return stay where Call 4 set them; no ESG premium assumed." Then each fund keyed to its
segment by colour, with its role: the world ESG index is the global shares core (the highest-rated firms in each
sector, so still diversified); MPF low-carbon is the half of each MPF from their own contributions (Employee Choice);
green bonds are part of the bonds, each checked against ICMA. The two-rating test now says "per equity fund", as the
written case does (green bonds are checked against ICMA instead). Right: Adrian, Carmen and Chloe in one row; then
"Ryan keeps his HK$500K: nothing sold, nothing added", with his wealth at 24, 30 and 35 as three columns on one scale.
The crypto block is the same size in each, with a dashed line along its top; the shares 74% → 32% → 20% (the cap at 35 in
crimson) come from Figure 18 (30% of his pay saved, prices held flat), and each column's total is HK$500K over its
share. The trim rule (a rally more than 10 points above the path) makes the 20% a cap, not a hope. The axis under the
ESG bars went to make room.
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
**One message, 25 Oct evening** (deck review: 265 words shown for 64 spoken, two messages, five crimson icon circles
competing with the result). The four tests take the whole width, larger; the lost job's 83% is 40 px, the only crimson,
and its row leads. The risk register is one quiet line at the foot: Pete's five icons (mist circles, wine marks) and
each risk's name; the defences are in the notes, said if asked. 209 words. Builds now hide.
**Presentation pass, 25 Oct.** The price-of-holding strip now sits under the chart it belongs to, inside the left
panel; the risk register's detail and the rows' descriptions in ink.
**Third pass, 24 Oct evening** (Pete: the arrows weren't premium; "what holds it" needed to look better). Each test is
now one rounded bar from 0% on a soft track. The rose part is the four decisions alone, and the wine part, after a white
seam, is what the review at 75 and the spending rules add (crimson on the lost job); each value sits above its end. It
reads as a level against 100%, as slide 5's bar list does, and a bar from zero can't read as a fall. Rendered against a
refined dot plot, the bars read faster. The sentence above the chart names both parts with colour swatches, which
replaces the labels under the first bar (they ran into each other where the rose part is short). "What holds it" is
one line a defence, its name in bold and what it does in a few quiet words ("**Spending rules** trim lean years",
"**Treasuries** mature on schedule", "**Annuities** pay for life"). Tried the same evening: pills with icons (Pete: back
to text), names alone (they didn't say how) and full sentences (too busy for a 30-second slide).
**Icons, 24 Oct evening** (Pete sent five icons for the risk list: a briefcase, people, bitcoin, a leaf, a rising chart).
Kept his choice of pictures, drawn from Phosphor's filled set (MIT; `src/lucide/ph-*.svg`, scaled to the 24-unit box),
white on a wine circle. His files themselves stay out of the deck: the leaf is a VectorStock preview with its watermark,
the others look like stock downloads with no licence on file, and they bring four new colours on white squares.
**Second pass, 24 Oct evening** (Pete: does red suit this chart? more bold or italic? at first glance the big red number
didn't say it was the full plan). Red kept: crimson means "with our plan" across the deck (97%, 25%, HK$7.7M), and A
against B (numbers in ink, red on all four arrows) showed B with four red marks and no focal point. Each gain bar now
ends in an arrowhead, so the move reads as up the scale, not as a red fall (Hong Kong screens show falls in red). The
first row names its dots ("the four decisions alone", "the full plan", the second in crimson), and the legend is
replaced by one plain sentence. No italics (one font, Zoom), no extra bold: the one bold added is "about
{{rec_lowret_typical_pct}} of the budget" in the price strip.
**Drafted 24 Oct** (Pete: draft our own version, not the teammate's of the same afternoon, which is in git, commits
1ef9433 and e8d5f30). Left: each hard test as one row, a dumbbell on one 0–100% scale from the four decisions alone
(hollow grey) to the full plan (filled), then "what holds it" (the written case's defence for that row). Only the
title's test is crimson ({{adrian60_89}} → {{rec_adrian60_89}}, 36 px); the others are ink. Rows in speaking order: the
lost job; low returns every year ({{stressA_89}} → {{rec_lowret_89}}); inflation and medical costs together
({{stressB_89}} → {{rec_stressB_89}}); Carmen to 95 ({{ladder_5_95}} → {{guardswitch_95}}). Stress inputs typed from the
written case's A1 (shares 4%, bonds 2.5%, inflation 3.5%, medical 8.5%). Right: "…and every other risk has a named
defence", five rows from Figure 26 (the business unsold, three risk appetites, crypto rules, greenwashing, model risk).
A strip under both names the price, so "holds" isn't read as "nothing changes": in years of low returns the rules trim
typical spending to about {{rec_lowret_typical_pct}} of the budget. Builds: the lost job, the two market tests, 95, then the
register, the price and the bar.
- **"Tested against the worst…"**: paired bars per test, the four decisions alone vs the full plan: Adrian's job ends
  at 60 ({{adrian60_89}} → {{rec_adrian60_89}}), low returns every year ({{stressA_89}} → {{rec_lowret_89}}), inflation
  and medical costs ({{stressB_89}} → {{rec_stressB_89}}); Carmen lives to 95: {{guardswitch_95}} (measured).
- **"…every risk has a named defence…"**: the risk register in brief (proposal Figure 26): suitability (one risk
  profile per person), crypto rules (licensed channels), greenwashing (two ratings), model risk (compare decisions,
  not forecasts), the business unsold (buy-sell agreement now).
- Footer: we compare decisions in the same 10,000 markets, we don't forecast them; premiums are from rate cards until
  quotes arrive; the tier switch is guaranteed under the VHIS rules.
- Bar: "It holds when the hardest things happen, and it starts this month."

### 11 · What happens when (Lookbua; 0:20)
**First year as the hero, 25 Oct evening** (deck review: nine equal columns, no focal point). The title says "it starts
this month", so the first year is the left seven columns: four steps on one line, large, Month 1 the only crimson
(its date and its circle). The dated steps after it are a quieter list on the right, a thin line down their dates
(a sequence), each with its owners' faces. The reviews are one line at the foot; the yearly review's detail
(rebalance; the mortgage, cover and ESG list) is in the notes. Builds now hide.
**Layout review, 24 Oct evening** (Pete: is the layout ideal yet?). No; three changes, then one addition.
(1) Ryan and Chloe's strip is gone, its facts kept: it repeated the line (Ryan's plan is in the month-12 meeting,
Chloe's offer is 2028) and said slide 12's point early (trusts at 25, 30, 35); its new fact, Chloe starting work in 2032,
is now a step on the line, so the children stay in the story the bar promises (the lane came from the 24 Oct plan edit
above; this is how it's carried now). (2) 2037 and 2039 merged into "They retire, 2037–39: the home released; an
annuity each", as the script says it ("the home and the annuities from 2037"). (3) Each step is a date, a bold action
and one short detail, about half the words, on larger dates and circles. Added: who acts on each step, as small
overlapping portraits on one row, from the written case's Figure 23 owners (the parents; the family; all four; Chloe;
Carmen). It fills the space the strip left with something a practitioner looks for, and the footer had promised the
owners without showing them.
**One timeline, 24 Oct evening** (Pete: the left half read as a chart of progress, not a timeline, and after slide
10's bars it looked like more chances of success). Now nine steps on one line across the slide, each a date over a
circle over what happens. The first year (month 1, by month 3, by month 6, month 12) sits on a soft band, its dates,
circles and stretch of line in crimson: the zoom into this year, which the title starts with. The later steps (2028 to
2047) are on the rose line in wine. Equal spacing: it's a sequence of triggers, not a time scale. Ryan and Chloe's
strip and the reviews run underneath as before. Pete's idea of deep dives per step, raised the same evening, was not
built: the speech gives each later step about 3 seconds, and the scored PowerPoint must read in its final state. A
crimson highlight that moves along the line as Lookbua names each step is offered, not built.
**Drafted 24 Oct.** Title: "It starts this month and closes every gap within a year; after that, dates trigger each step". It joins the storyline's title (and the script's "after that, dates trigger
each step") to the written case's §10 heading, which the 24 Oct plan edit below had brought in. Left, "This year: close
every gap…": the first year as a staircase of deadlines, each bar ending on its month on a 12-month track (month 1 the
papers and the joint account; by month 3 the cover and the buy-sell agreement; by month 6 a portfolio each; month 12
the first family meeting). Right, "…then dates trigger each step": five dated steps on one line, an icon each (2028
Chloe's offer, 2035–39 the business, 2037 Adrian retires, 2039 Carmen retires, 2047 the medical review), equally
spaced (a sequence of triggers, not a time scale). Under them, "Alongside, Ryan and Chloe": Ryan's own plan now, Chloe's
own plan from 2032, their inheritance in stages at 25, 30 and 35, the support for the bar's "it lasts beyond it". The
reviews strip (quarterly, yearly, and at once after the written case's five events) runs under both.
- title: **"It starts this month; Close all gap within the first year"**
- three phase panels: "This year: close every gap..." - month 1-12, "...hand over to the next generation..." - 2028-2036, "...then turn assets into income" - 2037-
- One dated sequence (a true sequence, so a line): month 1 the papers, the joint account, idle cash moved; months 1 to
  3 the cover; months 1 to 6 a portfolio each, the investment policy signed, voluntary MPF; month 12 the first family
  meeting (charter, Ryan's plan, the one-person budget); 2028 Chloe's offer, fees converted (no currency risk); 2032 managers built up;
  2037 mortgage cleared, Adrian's annuity, the home released; 2039 Carmen's annuity, the business sold, rules begin;
  2047 the medical review.
- under the line: 2 thin lanes - first is Ryan and Chloe's (to support the argument 'it lasts beyond it'): Chloe's first job in 2032, Ryan turns 35 in 2037, trusts at 25, 30, 35
- Under it, the second lane the reviews: quarterly portfolio, annual family meeting, a full review after a death, a disability, a
  business sale, a 20% market fall or a 1.5-point rate move (proposal Figure 23). every year: rebalance; review mortgage, cover, ESG list
- Bar: "For the Wongs, it starts this month; for Ryan and Chloe, it lasts beyond it."

### 12 · What passes on (Pete; 0:25)
**Hierarchy pass, 25 Oct evening** (deck review: HK$24.4M out-shouted the title's HK$7.7M; three messages). The
inheritance is the hero: the left takes seven columns and HK$7.7M is 72 px, the only crimson ("more than three times
as much" in ink). Pete's 24 Oct order is kept (what they have, what it pays for first, what is left), with HK$24.4M
now a quiet 20 px start to the sentence. The tree and the scholarship are smaller, on the right five columns, with
quiet marks. This reverses Fahtai's 25 Oct split (left 5, right 7) in size only; his two groups by moment stay.
**The scholarship's reason, 25 Oct** (Pete: why a legacy with purpose; did Chloe say sustainable design?). She didn't:
the case says she "has expressed interest in pursuing undergraduate studies in business, psychology or design". The
reason is the family's goal 8: "a possible philanthropic plan related to education or environmental causes". The slide
now says so ("the education and environmental causes the family asked to support") instead of "Carmen's mission to
Chloe's interest". The spoken line still says "joins Carmen's mission to Chloe's interest": Pete to approve a change.
**Right side as a family tree, 24 Oct evening** (Pete: too text-heavy, bland?). Yes on both: 240 words, the second
densest slide, for 25 seconds; no picture at the emotional payoff; and the "IF THEY DIE EARLY" chips were the device
removed from slide 7. Now "…and if a parent dies early, it still passes on safely": Adrian and Carmen's portraits
("each to the other first, then to Ryan and Chloe", the mirror wills), a line down that branches to Ryan, 24 (his share
in trust, paid at 25, 30, 35: 2027, 2032, 2037) and Chloe, 16 (a guardian until 18; 2035, 2040, 2045). The years come
from the case ages. The scholarship is one line on mist. The MPF detail and "control, not tax" moved to the notes.
200 words.
**Left side reframed, 24 Oct evening** (Pete: with HK$24.4M today drawn beside HK$7.7M, the plan read as if it loses
the family's money; we never said why HK$7.7M is good). Their wealth's first job is their own forty years, so the left
now tells it in that order. HK$24.4M today stands as a figure, not a bar to compare lengths with. "First, it pays for
40 years of the life they chose: their HK$780K a year, Chloe's degree, the medical cover" (case facts). Then what is
left at Carmen's 89, in the futures where their own way sells the home: {{own_legacy_sold}} against
{{plan_legacy_sold}}, drawn on each other's scale, with "[[legacy_times_word]] as much, and more in
{{plan_legacy_more_pct}} of those futures". The multiple comes from the two model figures (series.py), not typed.
**Rebalanced 25 Oct (Fahtai, for Pete's OK).** The two halves were about different moments, and the script mixed
them: the {{plan_legacy_sold}} arrives at Carmen's 89, when Ryan is 64 and Chloe 56, so it cannot be "passed on in
stages at 25, 30 and 35"; the staged trusts matter only if a parent dies early. Now the left (5 columns) is the
inheritance at 89, compact; the right (7 columns), "…passed on safely, and with a purpose", in two groups by when they
apply: **If they die early** (signed in month 1, under HK$25K): mirror wills (the MPF, with no nominee, passes through
them), a guardian for Chloe while she is under 18, each child's share held in trust and paid at 25 · 30 · 35; **A
legacy with purpose** (every year, while they are alive): the scholarship in sustainable design, about HK$30K a year
through a registered charity, tax-deductible, the case's "education or environmental causes" (case §8). Script: "And if
either parent dies early, the wills name a guardian for Chloe and hold each child's share in trust until 25, 30 and 35.
Meanwhile, a scholarship…" (about 10 words more).
**Drafted 24 Oct.** The payoff of slide 3, in slide 3's own form: the inheritance bars on the same scale
(HK$24.4M today), their own way {{own_legacy_sold}} in rose, the plan {{plan_legacy_sold}} in crimson at 72 px, the only
accent; under them, the plan leaves more in {{plan_legacy_more_pct}} of those futures and releases the home at 65, not
by force at about {{own_sale_age}}. Right: mirror wills with staged trusts (a 25 · 30 · 35 track), a guardian for Chloe,
the scholarship; lede "Signed in the first three months, for under HK$25K"; on the floor, level with the left, "Control,
not tax" (estate duty abolished 2006). The title house is complete with its roof crimson (`house.progress3d(6)`).
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
**Northbound first, 25 Oct** (script review). The voice spoke Southbound first while the slide reads left to right
and the title puts the Wongs first. Now the voice and the builds follow the title: the three facts (step 1), Northbound
and the Wongs (step 2, "a tool for later", which closes their story), then Southbound and us with the bar (step 3),
which leads into slide 14.
**Flows fixed, 25 Oct evening** (Pete: the arrows didn't point correctly; Northbound didn't start from Hong Kong and
Southbound pointed back into the mainland). Both ended about 14 map units north of Hong Kong's centre, in Shenzhen.
Now each flow joins Hong Kong and the nine cities, with a ring at its start and an arrowhead at its end: Northbound
(dashed wine) from Hong Kong's New Territories to the Guangzhou-Foshan core; Southbound (solid crimson) from the
Dongguan-Huizhou side to an arrowhead on Hong Kong. A white casing keeps both readable over Hong Kong's crimson. The
headings' leaders are straight elbows (across, then down onto the middle of each flow), so they read as callouts, not
as a third and fourth flow. `gba_map.py --flows round2/img/gba_map.svg` redraws only the flows (the boundary file
isn't needed) and prints where the leaders land.
**Emphasis, 24 Oct evening** (Pete: bold or italicise the parts we want to highlight, not only the headings). Bold
on the phrase each paragraph turns on: "mainland wealth products", "Kept out today", "if Adrian's work moves across the
boundary"; "Hong Kong funds, bonds and deposits", "won't solicit or recommend", "unless the investor asks or agrees".
No italics: the deck builds emphasis from weight and colour in one face, and slanted text blurs in video.
**Second pass, 24 Oct evening** (Pete: point the headings at the arrows, not a legend; the map's text is hard to
read; why an oval under the raised area?). "Northbound" and "Southbound" lost their line swatches. Each now has a thin
leader in its flow's colour, ending on a dot at the middle of its flow on the map (the arrow helper in `99_tail.html`
gained `data-end="dot"` for leaders that point at something). Northbound's leader runs along its heading to the column
edge before it curves, so it never crosses the text. The on-map flow labels went (the headings now point). Map labels
sit on a white backing; the drop shadow under the map is gone.
**The map, 24 Oct evening** (Pete: the flows diagram was bland and didn't say it clearly; a 3D map of the Greater Bay
Area). The middle of the slide is now the real region, drawn from boundary data by `round2/gba_map.py` into
`img/gba_map.svg`. The nine mainland cities are one raised rose slab, Hong Kong and Macao a higher wine block, and the
land around fades out. It is tilted toward the viewer with a little perspective, in the spirit of slide 4's house. Both
flows are drawn over the water: Northbound west (dashed wine, from Hong Kong into the mainland), Southbound east (solid
crimson, into Hong Kong). The text sits either side, each heading carrying its line style (Northbound and the Wongs
left, Southbound and us right), and the labels lie over the map as text at true size. The three growth facts stay on
top. Data: geoBoundaries gbHumanitarian CHN ADM2 (prefecture-level, with the SARs), CC BY 3.0 IGO, credited in the
footer. The gbOpen file was tried first and is county-level, so each city came out as its urban core only.
**Drafted 24 Oct.** The growth in three facts across the top (2021; RMB 3M per investor since 2024, from RMB
1M; securities firms admitted in 2024), then the two flows on one boundary, drawn north up: the nine cities in a rose
band, Hong Kong and Macao in a light band (not wine: it sat on the conclusion bar as a second wine strip). Each arrow
carries one half of the title. Northbound is dashed wine, kept out today: "For the Wongs: a tool for later". Southbound
is solid crimson: "For us: the market we want to serve", with the advice rule. Above the boundary, what each flow is
(the investors or products on the mainland side); below it, what it means on the Hong Kong side. Facts checked on 24
Oct against the HKMA's Southbound page (revised 11 May 2026): "Without the request or agreement from the investors,
Hong Kong banks will not proactively conduct" cross-boundary solicitation or recommendation; the individual quota is
RMB 3M (RMB 1.5M each if a bank and a securities firm are both used); eligible funds are rated low to medium-high risk
and non-complex. Not on screen: the in-person exception on that page, and "RMB 150bn each way" (§9).
- The two flows between Hong Kong and Macao and the nine mainland Greater Bay Area cities; the advice rule on
  Southbound (without the investor's request or agreement, Hong Kong banks don't solicit or recommend across the
  boundary; HKMA Southbound page, checked 22 Oct); facts: since 2021; up to RMB 3M per investor since 2024 (RMB 1.5M
  each if both a bank and a securities firm); securities firms admitted in 2024; eligible products low to medium-high
  risk, non-complex (HKMA, checked 18 Oct).
- For the Wongs: Northbound kept out today (home, income and business already in Hong Kong); it comes in at the
  annual review if Adrian's work moves across the boundary. For us: a clear, suitable answer when the client asks.
- Bar: "Under the Connect, an adviser's value is a clear, suitable answer when the client asks."

### 14 · Who we want to become (all; 1:10)
**Two sections a person, 25 Oct** (Pete: what are the location tags, and are they true; "In this plan, I led" in
grey; are three sections ideal?). The location tags were my inference from each script, not anyone's words (Lookbua's
not even that), and a pin under a name reads as where someone is from: removed. "In this plan, I led" was unspoken and
disputed (the written case's notes and Fahtai's statement disagree on who led the model): moved to the notes for the
team to settle. Each column is now the person (photo, name, role), the goal in five years with its Connect link (the
link in bold, since the criterion scores the Connect), and the lesson as a quote at 18 px on mist. All content in ink;
the two labels in wine.
**The team's photos, 25 Oct** (Pete: use photos of ourselves; can we, without being disqualified?). Yes: the rules
ban naming the university ("do NOT mention your university names and related words"), not faces; the video shows us
anyway, and the Final asks for names and name tags. Pete, Fahtai and Win now appear as their own photos, cropped
to matching head-and-shoulders circles and re-saved without metadata (`img/team/`; the built deck carries no
original file name and no EXIF). Lookbua keeps his role icon: his photo showed a badge on his blazer and a campus
window, either of which could identify the university. **A plain head-and-shoulders photo from Lookbua (plain
background, no badge or logo) replaces the icon.** The raw folders (`Photos/`, `Icons/`) are git-ignored.
**Drafted 24 Oct.** One column a speaker, in speaking order, each with an icon for the work: where (Hong Kong;
East and Southeast Asia; Asia-Pacific; across the boundary), the goal in five years and its link to the Connect (the
script's words), "In this plan, I led" (from the written case p.14, its owner notes and each statement; **each member
to confirm his line**), then "What this plan taught me" on mist, level across the four. Win's lesson is a dashed
placeholder until he gives it. Bar: "What the Wongs taught all four of us: a plan is a set of choices between people,
each made clear" (it draws the three lessons together; the title already says the aim).
Four cards: the goal in five years, what this plan taught each of us, the link to the Connect (personal statement,
proposal p.14). **Win's line is a draft for Win to confirm; Lookbua's edited line needs his OK.**

### 15 · Close (Pete, all; 0:15)
**Drafted 24 Oct.** The cover mirrored: "Built to Last", the three results the talk promised ({{switch_89}}
from {{own_89}}; {{plan_legacy_sold}} where their own way leaves {{own_legacy_sold}}; the home their choice at 65, not
forced at about {{own_sale_age}}), "Thank you" and the team at the foot. On the wine panel, where the cover had the
family, the house built for them, complete (slide 4's model in light tones, assembled closer), labelled with the
written case's four pillars from the roof down: what passes on; a place for every voice (Calls 4, 5); income for life
(2, 3); protected first (1).
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
- **Colour, 25 Oct: a brighter crimson (red B)** (Pete: more colour, more red than the low-saturation crimson). Three
  strengths were rendered on slides 4, 6 and 10: today's, a brighter crimson, a vivid red. The vivid red read as an
  alert or a sale, blurs most in video compression, and strengthens "red means down" on Hong Kong screens; Pete chose
  B. Every strong red is pushed half way toward 356 degrees, saturated by 1.25 and lightened by 0.03: the accent
  #A81E2D becomes #C80E1E, wine #7D1D2A becomes #971320, the gradients #A62535/#5A1520 become #C41627/#700E19. Pale
  tints, ink and greys are unchanged. Applied to the sources (`src/*.html`, `house.py`, `gba_map.py`, `img/gba_map.svg`),
  so every build keeps it. The written case keeps its own #A81E2D: the same family, a step brighter on screen.
- **Colour, since 24 Oct: slide 4's tones on every slide, on white** (Pete liked slide 4's colours; tried on slide 3,
  then rolled out): secondary text a rose-tinted grey (slate #80606A, grey #B5979D), rules #ECDADD, panels #F8EFF0;
  soft rose fills (#EFD9DC, #E6CDD1, #D3A6AD) in place of the greyed rose and warm greys; wine and crimson with depth,
  as gradients (--wine-g #A62535 to #5A1520, --accent-g #B3202F to #7D1D2A, and #p4wine / #p4rose for SVG areas, in
  99_tail); the conclusion bar a small stage (a radial gradient, crimson at the centre, wine at the ends). The text
  above this line in earlier versions, kept below for the record:
- **The conclusion bar, since 25 Oct: ink** (#1B1716, flat, white text; Pete, after the deck review). The crimson bar
  was 72-89% of all the crimson on slides 2, 6 and 9-14, so the eye reached the conclusion before the evidence and the
  focal number was never the only red. Ink keeps the bar (it still reads as the conclusion, as e-Sentry's black bar
  did) and leaves crimson to the number the title names. Measured after: crimson is 0.5-2.3% of slides 2, 6, 9-14, all of
  it on the focal figures. Still to watch: the ink bar is the darkest block on the page; it no longer competes in colour.
- **Colour (23 Oct):** the written case's crimson #A81E2D as the accent (#6F1320 deeper); its family for fills: wine #7D1D2A
  (the home layer, the family panels, the guaranteed income, cost bars), a greyed rose #DDD0CD and #B99A9C (savings,
  lighter series), tint = mist; warm neutrals tuned to the crimson (mist #F5F1F0, rule #DDD6D4, grey #A69E9C, slate
  #5A5250, ink #1B1716). No blue. Events on wine-and-rose charts in ink. The conclusion is a crimson bar, white text
  centred (Pete, 24 Oct: without a bar the last line didn't read as a conclusion; it had been a line on a crimson rule
  since the evening before, after a wine block outweighed the focal numbers).
- **One decorative idea: the house we build** (Pete chose it, 23 Oct, over the lifeline and over no thread). "Built to
  Last" drawn as a house from the written case's pillars (`round2/house.py`): the foundation is Call 1 (protected
  first), the walls Calls 2 and 3 (income that lasts), the rooms Calls 4 and 5 (a place for every voice), the roof what
  passes on. Slide 4 draws the whole house as the answer, an exploded 3D model since 24 Oct (`house.exploded()`), built part by
  part as the calls are named; each call slide
  carries a small house beside its title, since 24 Oct slide 4's 3D model in miniature (`house.progress3d(call)`):
  earlier calls built in the house's colours, this call crimson, the rest and the roof dashed ghosts; the close shows it
  complete. The lifeline ruler is gone; time stays where it is data (the axes of slides 2, 3, 7, 11).
- **Slide 4 is the one dark slide after the cover** (24 Oct): the answer reveal, on a wine stage; every other content
  slide stays on white.
- **Signature:** a 5 px crimson rule on the title block, kicker and title 14 px in from it, as in e-Sentry (Pete, 24
  Oct: the header was too big and its title competed with the panel headings); the cover's crimson bar (no dash before the kicker: Pete, 24 Oct,
  "not needed"); the family on a wine panel (slide 2; the cover until 25 Oct, now the written case's photograph, §5).
- **Icons:** Lucide line icons (ISC, `src/lucide/`) for the deck; Phosphor's filled set (MIT, `src/lucide/ph-*.svg`)
  where a list needs pictograms that read at a glance (slide 10's risks). Downloaded stock images only with a licence
  on file.
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
| A practitioner | "You attack selling the home, then release it with a reverse mortgage. Isn't that the same?" | 3, 6: the home pays for retirement either way (kept untouched, even the plan lasts to 89 in only {{prop_keep_89}}); the difference is when (at 65, not forced at about {{own_sale_age}}), who decides (both of them, not Carmen alone in {{own_alone_pct}} of forced sales), whether they stay (the reverse mortgage keeps them home; downsizing is the stronger financial option, written case §9), and what is left ({{plan_legacy_sold}}, not {{own_legacy_sold}}, in the same futures) |
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
