# Built to Last, Round Two: Deck Plan (v10, "Their own way, then five calls", told on the page)

**Status:** **v10 proposed 23 Oct, to agree with Pete**: the same story and points, designed as a story on the page:
one picture the audience watches change (§3, the spine), setups and payoffs (§3), a headline annotation on every
picture and the family's own words on every call slide (§4a), slide 4 as the map, and every spec in §5 rewritten to
one template that starts from the picture and its point. Changes listed in §12. v9 agreed with Pete, 22 Oct 2026: the problem before the answer, "their own way" as the baseline, Lookbua
reads slide 11. The talk, timed, with the full draft script: `round2/Talk_Outline.md`. Look B chosen (20 Oct, §6).
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

**How to use it:** build each slide from its section in §5, to the rules in §4 and §4a. The deck is `round2/src/` (v9, set up 22 Oct: slides 1,
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
| Powerpoint (15): "Quality of ppt" | A designed, consistent deck; one claim a slide; charts that read, each with its point written on it (§4a); works without the voice | All |
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
| 2 | Where they stand | On paper, the Wongs are secure | Pete | 0:30 |
| 3 | Will it last? | Their own way, Carmen sells the family home at about {{own_sale_age}}, and the children's inheritance pays the bills | Pete | 0:45 |
| 4 | Our answer | The family asked for innovative yet prudent: five calls make the home their choice and their wealth last | Pete | 0:45 |
| 5 | Call 1 · Protection | Insure the income, not the life: about HK$100K a year closes every gap | Lookbua | 0:40 |
| 6 | Call 2 · The home and the business | Decide now, not at {{own_sale_age}}: four decisions on what they own and spend lift the odds from {{own_89}} to {{ladder_5_89}} | Fahtai | 0:45 |
| 7 | Call 3 · Retirement | Fix the cost the budget ignores: now all {{plan_fut_lasts_n_word}} futures reach Carmen's 89, and none is forced to sell the home | Fahtai | 0:40 |
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

**The spine: one picture the audience watches change** (v10, 23 Oct; replaces v9's "threads", which still described
the ten futures that slides 3 and 7 dropped on 23 Oct). The flow has to be on the page, not only in the script. The
deck has one recurring picture, **the family's money over their lives** (2026 to Carmen's 89, today's money, one scale),
and one recurring axis, **the family's lifeline** (the same years):
- **3** draws the picture their own way, with each problem marked where it happens: the home that pays nothing, the
  premiums on the slope, the sale at {{own_sale_age}}, the inheritance spent.
- **4** lays the five calls on the same years: **the map**. Each call slide's lifeline (top right) is its row of the
  map, so a reader always knows where they are and when this call acts.
- **7** redraws 3's picture with the plan, in the same place and scale: the sale mark is empty, the money reaches 89.
- **11** is the map again, dated; **12** is the end of the picture, what's left; **15** is the map, complete.

**Setups and payoffs.** Each is planted on the page and paid off on the page; the voice only points at it.

| Planted | On | Paid off |
|---|---|---|
| "On paper": 61% of their assets are a home and a business (a bracket on the bar of what they own) | 2 | 3: they pay nothing until sold; 6: put to work from 65 |
| Medical premiums climbing to HK$375K a year, written on the slope where the money drains | 3 | 7: the review at 75 cuts them to about a third |
| Carmen, {{own_sale_age}} and on her own, sells the home (a mark on the chart) | 3 | 4: a grey line every call acts before; 6: chosen at 65; 7: the same mark, empty |
| {{own_legacy_sold}} left to Ryan and Chloe (the chart's end label) | 3 | 12: {{plan_legacy_sold}} in the same futures, next to the same grey figure |
| The chance the money lasts: {{own_89}} their own way | 3, 4 | 6: {{ladder_5_89}} → 7: {{switch_89}} → 10: still {{rec_adrian60_89}} if Adrian loses his job. **One measure, one look:** grey for their own way, the accent for the plan, the same 0–100% bars wherever two are compared (4, 6, 10) |
| HK$2.5M in cash, "30 months of spending" | 2 | 8: safe, but earning little; every dollar given a job |
| Four faces, four wants | 2 | 5 to 9: each call slide shows whose want it answers, in the case's words |
| Ryan "holds crypto"; Carmen wants "money that reflects her values" | 2 | 9: the family's three views on crypto, and the size each gets |

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
- **panels whose headings read as one sentence across the slide** where the slide is a sequence ("What they own…" /
  "…what each becomes…" / "…and what it achieves"; v10: a story chart or a map has one heading, §4a); **each panel is one step of the argument and adds a new fact**: no panel restates another
  panel or an earlier slide (Pete, 20 Oct: v8's first Call 2 spent a third of the slide repeating 33%);
- **every claim gets a shape, not a paragraph.** The defence of a call is **measured** where it can be: run the
  obvious alternative in the model and draw it beside the call (Call 2: their own way, `own_*`); where it can't, a
  ledger with one figure a row. Each panel opens with its hero number or object;
- one **conclusion bar**: the slide's point in one sentence, worded to lead into the next slide;
- **one navigation device: the kicker** (the section, with the call's number); the tracker was dropped (Pete, 23 Oct:
  three signals for one fact). Footer: the source and the page number. Nothing else.
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

**Type (23 Oct):** EB Garamond for the title, panel headings and big numbers; **Inter** for everything else, bold
labels included. **Scale:** title 35 · panel heading 22 · bold label and body 16 (Inter) · small 14 (Inter) · tag and
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
where a label fits), axis text at 14 px, **and a headline annotation on every picture** (v10, §4a). Slides 3 and 7
share one picture and one scale (`story_*`); the premium line (7) comes back from v7; everything else is redrawn in
the system.

**Numbers:** tagged as a quiet "(measured)", "(case)" or "(sourced)" after the claim. MEASURED = the team model
(`numbers.json`); CASE = the case; SOURCED = a named public source.

**Builds:** each slide reveals in speaking order (`data-b`). **Later steps stay on the page in grey** (Pete, 23 Oct:
don't remove what's coming, grey it), so the layout never moves and the eye goes to what is in colour. `make.py
--builds` writes one frame per step (`Axis_builds.html`, `build/frames/`) for the video. Red reads as alarm: crimson
marks the title's claim as a point or a number, never a wall of lines (slide 7: ink lines, crimson ticks).
**Keep it simple** (Pete, 23 Oct): each slide as simple as it can be while its point stays clear.

## 4a. Story and annotation (v10, proposed 23 Oct, to agree with Pete)
**Why** (Pete, 23 Oct): the story and the points are "ok already", but how each page is designed is "still lacking
personality"; "right now we're just listing out facts and not connecting them together as one big picture"; and
"without annotation people reading the powerpoint slide will have a hard time trying to grasp what exactly in each
chart we're trying to communicate". He asked for the same on 18 Oct
("boxes of information with no clear visual guideline, and most don't have annotation"); v6 answered it with an
annotation table and vocabulary (`archive/Round2_Deck_Plan_v1-v7.md`, "Focus, annotation and builds"), and the v8
rewrite dropped both. This section restores them, updated for v9's story.

**What went wrong in v9** (slides 2 to 7 as built, rendered and read 23 Oct):
1. **The plan specified lists, so the slides came out as lists.** §5 described each panel as a list of facts. It never
   said what the eye reads first, what the picture proves, or what the slide picks up from the one before.
2. **Charts label their series, not their point.** Slide 3's chart never shows the title's claim: the end of the line,
   where the children's inheritance is spent, is unlabelled, and the two causes sit in a box beside the chart instead
   of on it. Slide 7's one annotation explains why their own way is ahead on paper until the 2050s, instead of showing
   the payoff, and its premium inset halves in 2057 with no reason given (Adrian's death: one
   policy). Slide 5's cost bar uses a legend.
3. **The big-picture slide is a list.** Slide 4 shows five equal columns. Later slides don't expand it, and the written
   case's three pillars (Protect · Turn assets into income · Give every voice a place) appear on no slide.
4. **The one decorative idea doesn't carry meaning yet.** The lifeline is a 200-px ruler with 12-px years, never
   introduced at a size anyone can read, so it reads as ornament.
5. **The family leave the slides after slide 5.** Faces appear on 1, 2 and 5; from Call 2 on, the slides are about
   money, not people. The case's own words (the family's eight concerns, p.5) appear nowhere.

**What the reference decks do that v9 doesn't** (from the team's notes on e-Sentry and the Nordea winners, 18 to 20 Oct,
in `archive/Round2_Deck_Plan_v1-v7.md`; Pete to check against `reference/Slides/`, which is not in git):

| Pattern | v9 | v10 |
|---|---|---|
| A map early that later slides expand (e-Sentry) | 4 is a list; nothing expands it | 4 is the map; each call slide's lifeline is its row (§3, the spine) |
| A persona's road with pain points that returns solved (Nordea p.9 → p.33) | 3's chart is the road, but its pain points are in a side box | the pain points are marked on the road (3), shown solved on the same road (7), and its end paid off (12) |
| Annotation drawn on the evidence: an arrow over a chart, a bracket, a callout (e-Sentry p.3) | labels on series only | a headline annotation on every picture (rules below) |
| The same cases return, changed | 3 → 7 only | 2 → 3 → 4 → 6 → 7 → 12 (§3, setups and payoffs) |
| A pillar hub that reappears (Nordea p.13, 14, 21) | absent | the three pillars group the calls on 4 and close the talk on 15 |
| Big numbers with the compared value highlighted; dim the rest | yes | kept |

**Rules (each slide, before it is called done):**
1. **A headline annotation on every picture.** Every chart, bar pair, ledger and timeline carries the takeaway in
   words, written on the picture at the point that proves the title: a callout (a leader and a dot), a bracket, a
   marked band, or an end label. The title states the claim; the annotation shows where to look. It never repeats the
   title as a caption.
2. **At most two supporting annotations:** explain a kink where it happens, name an event, label an end value. Three
   in all; a picture that needs more is two pictures, or one too many. Series and layer names don't count.
3. **Label the end.** The result of a line is read at its end: end labels sit in a gutter to the right of the chart;
   no legend where a label fits.
4. **Annotations replace side text, not facts.** A fact that belongs to a point on the picture moves onto it (slide 3's
   "why it runs out" box goes onto the chart and to slide 2). Words on the slide stay about the same, and the facts a
   reader needs stay on the slide (they are scored on their own, §4).
5. **Write annotations as a planner talks:** people and ages, not model terms ("Carmen, {{own_sale_age}} and on her
   own, sells the home", not "forced sale, median year"); 12 words at most; Inter 14 or 16 px, ink. The accent only when the
   annotation is the title's claim; then it is the slide's one accent.
6. **Reading order = build order = speaking order.** Each spec in §5 lists what the eye reads first, second and third;
   each is one build step and one spoken sentence. Later steps stay grey (§4, builds).
7. **Form:** straight leaders with a dot on the point (no curved arrows: Pete, 18 Oct); hatching, not pale fills, to
   mark a period (pale crimson reads pink); dashed lines for a baseline to beat. The tail's `svg.conn` arrows are used
   with `data-bend="0"` only.

**Vocabulary** (choose by the content's shape; never the same device on every slide):

| Device | Use it for | In v10 |
|---|---|---|
| Callout: leader and dot | a cause acting at one point | 3 (the money draining), 7 (the sale that doesn't happen) |
| End label, in a gutter | the result of a line | 3 ({{story_own_left}} left), 7 (lasts to 89) |
| Bracket | a group; a share of a whole | 2 (61% of assets), 5 (14% of surplus), 11 (year one) |
| Hatched band | a period | 3 ({{story_out_age}} to 89: the home pays the bills) |
| Dashed reference line | a baseline to beat | 4 (their own way's sale at {{own_sale_age}}), 10 (their own way, {{own_89}}, with no shock) |
| Change label between bars | before and after | 6, 8, 10, 12; written as a pair from existing keys ("{{own_89}} → {{ladder_5_89}}"), so no new numbers |
| Event marker on the axis | a date that matters | 3, 7, 11 |

**Two tests** (run on the contact sheet with Win or Lookbua before recording; 5 minutes):
- **The finger test:** someone who hasn't seen the slide puts a finger on the spot that proves its title within five
  seconds, without the voice. If they can't, the headline annotation is missing or in the wrong place.
- **The flick test:** read only the titles and headline annotations, in order, across the contact sheet: they tell
  the story on their own. (v8's test was titles and bars; the annotations now carry part of it.)

**Slide types.** The system fixes type, grid and colour (§4, §6); the layout follows the content, so the deck has a
rhythm instead of fifteen copies of one template.

| Type | Slides | Shape |
|---|---|---|
| People | 1, 2, 14 | faces with their own words |
| Story chart | 3, 7, 10, 12 | one picture, 8 columns or more, annotated; a narrow column of facts |
| Map | 4, 11, 13 | things placed on the family's timeline, or on the region |
| Call ledger | 5, 6, 8, 9 | today or their own way (grey) beside the call (the accent); the person served on the page |
| Close | 15 | the map, complete; the family |

Panel headings that read as one sentence ("What they own…" / "…what each becomes…") stay where a slide is a real
sequence (5, 6, 8, 9). A story chart or a map has one heading. Opinion: as a rule on every slide, the device reads as
a tic, and it forces three panels onto content that is one picture.

**Personality comes from people and voice, not more ornament:**
- **The family on every call slide.** Each call slide shows whose want it answers (their portrait from `img/`, 48 to
  64 px) and the concern it answers **in the case's own words** (p.5, or p.2 for a person), in the lede's place. One
  line, no pill, no number, no tracker: v7's "question pills" were navigation; this is the client's voice, which the
  case scores as "client suitability awareness" (p.9).
- **Their disagreements are the drama.** Adrian is "skeptical of digital assets", Carmen "open to new opportunities but
  concerned", Ryan "optimistic" (case p.2). Slide 9 shows the three views side by side, then the size each gets.
- **The annotations are where the planner's voice shows:** short, human, about Carmen and Adrian, not about models.
- **Rhythm:** the slide types alternate, so neighbours rarely look alike; where two ledgers follow each other (5 and 6;
  8 and 9), their pictures differ. 12 and 15, the two endings, are the lightest slides.

**Order of work** (recording is Saturday; 8 to 15 are not built yet): (1) build 8 to 15 to the v10 specs from the start,
which costs nothing extra; (2) annotate 3 and 7 (the spine; about an hour); (3) slide 4 as the map (about two hours;
the fallback is the five columns with the three pillar headings and a "when" line each); (4) the family's words on 5
to 9; (5) the tests. Leave the conclusion bar's style and the illustrated image set until the rest is done.

## 5. Slide by slide
**v10 (23 Oct): every spec answers the same questions, in this order,** so the build starts from the picture and its
point, not from a list of facts (§4a):
- **In → out:** what the slide picks up from the one before, and what its bar hands to the next;
- **Picture:** its type (§4a) and the one form;
- **Read:** what the eye reads first, second, third: the build steps, each one spoken sentence;
- **Annotate:** the headline annotation (its words, where it attaches), then at most two supporting ones;
- **Voice:** whose slide it is (their face) and their words from the case;
- **Facts:** what a reader without the voice needs (the slides are scored on their own), placed on the picture where
  they belong;
- **Notes:** reasons and secondary figures, spoken or in the speaker notes.
The scripts are in each slide's speaker notes (`round2/src/*.html`); `make.py` writes them to `Axis_Script.html`.
Built slides list their **v10 changes** first.

### 1 · Cover (Pete, all; 0:20)
- **Picture (people):** "Built to Last", the promise line, the team; the family (illustration, §7, or the four
  portraits as built). No numbers.
- **Out:** four faces, four wants: the people the talk is about.

### 2 · On paper, secure (Pete; 0:30)
**Built 23 Oct** (`src/01_s01-02.html`). **v10 changes:** the three-number stack becomes one bar of what they own, with
the bracket that explains "on paper"; it takes over the 61% from slide 3.
- **In → out:** the cover's faces become four people with four wants → "But will it last to Carmen's 89?"
- **Picture (people):** the four portraits as built (age, risk profile, want), and beside them **HK$24.4M** (72 px,
  the accent) over **one bar of what they own** (case, HK$27.2M of assets): the home HK$11.5M · the business HK$5.0M
  · investments, MPF and policies HK$8.0M · cash HK$2.5M · the car; the debt HK$2.8M as a short grey bar beneath.
- **Read:** the four faces → HK$24.4M → the bracket.
- **Annotate:** headline: a bracket over the home and the business, **"61% is a home and a business, which pay nothing
  until sold"**, in ink: it is what "on paper" means, and it plants slide 3. Supporting: on the cash, "30 months of
  spending" (planted for 8); beside the bar, "41% of after-tax income saved" and the debt "10% of assets".
- **Voice:** each person's want in the case's terms (as built).
- **Facts (case):** net worth, assets by kind, saving rate, debt; Chloe's university in 2028; Ryan holds crypto.
- **Bar:** "On paper, secure. But will it last to Carmen's 89? We tested it in 10,000 futures."

### 3 · Their own way (Pete; 0:45)
**Rebuilt 23 Oct: one typical future, told with the money** (`src/02_s03.html`). **v10 changes:** the title's claim is
written on the chart (the end label and the band); the causes move onto the slope; the "Why it runs out" box goes; the
right column says how typical this future is, in ink.
- **In → out:** slide 2's "will it last?" and its 61% → "the question is when, and on whose terms" (4 answers it).
- **Picture (story chart, panels 8 + 4):** one future from the model (`story_*`: of the futures where the flat is sold
  and the money still runs out, the median sale year, then the inheritance nearest the median), stacked areas in
  today's money, 2026 to 89: the home (wine) under savings, investments and MPF (rose). Same scale as slide 7
  (`series.py`), with a 150-px gutter on the right for end labels on both.
- **Lede:** the bridge from the written case, as built: "Our written case measured investments alone:
  {{ladder_1_89}}. The fairer test is their own way: the business sold when Carmen retires; the flat kept, and sold
  only when the money runs out".
- **Read:** the money rises, then drains → the sale at {{story_sale_age}} → what's left.
- **Annotate:**
  - headline, the accent: a hatched band from {{story_out_age}} to 89 over the home, starting "{{story_out_age}}: out
    again", and the end label in the gutter, **"{{story_own_left}} left to Ryan and Chloe: from {{story_out_age}}, the
    home pays the bills"** (40 px number);
  - a callout with a dot on the falling slope (about 2052): "Retired, they spend, and medical premiums climb to
    HK$375K a year";
  - the sale marker: "{{story_sale_age}}: savings run out, and Carmen, on her own, sells the home".
  - Layer labels: "The home, where Ryan and Chloe grew up: it pays nothing until it is sold"; "Savings, investments
    and MPF".
- **Right column, "…and across 10,000 futures: this one is typical"** (measured, ink, 40-px numbers):
  {{own_sold_pct}} must sell the flat, Carmen at about {{own_sale_age}}; {{own_alone_pct}} of those sales, Carmen on her
  own; {{own_fut_buys_min}} to {{own_fut_buys_max}} years is all the late sale buys where the money runs out again (ten
  typical futures); {{own_89}} the money lasts to 89, even counting the sale. The 72-px {{own_legacy_sold}} moves to the
  chart's end label: the same figure, because the model picks this future as the one whose inheritance is closest to
  the median (`run_model.py`, "One future, told with the money"), and the eye finishes the line there. If a model change
  ever makes the two print differently, the end label shows {{story_own_left}} and the column adds {{own_legacy_sold}}
  as the median. (The model subtracts the bills the money couldn't pay from the home's value, so "the home pays the
  bills" is literal.)
- **Builds:** the future → the drain → the sale with {{own_sold_pct}} and {{own_alone_pct}} → the band, what's left,
  the rest of the column and the bar.
- **Bar:** "Their wealth will pay for their retirement either way. The question is when, and on whose terms."

### 4 · Our answer (Pete; 0:45)
**Built 23 Oct as five columns** (`src/03_s04-05.html`). **v10 changes:** it becomes **the map**, the deck's big
picture: the same five calls, the same results and the same impact band, placed on the family's years and grouped by
the written case's three pillars.
- **In → out:** 3's "when, and on whose terms" → five calls, each placed where it acts in their lives, each starting
  years before the sale at {{own_sale_age}} → "the rest of this talk defends each one".
- **Picture (map):** five rows on the family's timeline (2026 to Carmen's 89, the axis of 3 and 7, ticks at Adrian's 65
  and 75), grouped in a left column by pillar: **Protect** (1) · **Turn assets into income** (2, 3) · **Give every
  voice a place** (4, 5). Each row: the call's number (ink square), its name, its one result, and an ink bar for when it
  acts:
  1 Insure the income, not the life · ≈HK$100K a year closes every gap (sourced) · now, until each retires;
  2 Put the home and the business to work · {{own_89}} → {{ladder_5_89}}, chosen at 65, not forced at
  {{own_sale_age}} (measured) · 2035 the business, 2037 the home and the annuities;
  3 Fix the cost the budget ignores · → {{switch_89}} with a medical review at 75 (measured) · 2039 the spending
  rules, 2047 the review;
  4 One family policy, a plan for each person · Chloe funded today; ≈HK$45K a year less in fees · now; Chloe's degree
  2028 to 32 marked;
  5 Values and innovation, with guardrails · ESG at 25%; crypto sized per person · now, reviewed every year.
  This full-size axis introduces the lifeline: each call slide's ruler is its row of this map.
- **Read:** the calls, row by row (one build each) → the grey line → the impact band.
- **Annotate:** headline, the impact band: "Chance the money lasts to Carmen's 89": {{own_89}} their own way (grey) →
  {{switch_89}} with the five calls (the accent, 72 px), "and the home their choice, not their last resort".
  Supporting: a grey dashed line at about 2060 down through the rows, **"Their own way: the home sold at
  {{own_sale_age}}"**: every call starts years before it.
- **Voice:** the family's brief is in the title; v9's separate quote band repeated it and goes (footer: "The family's
  brief, case p.5").
- **Fallback** if time runs short: keep the five columns, add the three pillar headings across them (1 | 2, 3 | 4, 5)
  and a "when" line under each result.
- **Bar:** "Five calls, one family: the rest of this talk defends each one."

### 5 · Call 1: insure the income, not the life (Lookbua; 0:40)
**Built 23 Oct** (`src/03_s04-05.html`; 169 words). **v10 changes:** the headline annotation on the gap; labels on the
cost bar's segments instead of a legend; a bracket for the share of surplus; the family's words.
- **In → out:** 4's first row → "Protected first: now the plan can turn what they own into income" (6).
- **Picture (call ledger, panels 5 + 4 + 3):** "If a parent can't work, nothing replaces their pay…" (Adrian and
  Carmen: today a dashed empty bar, with cover an ink bar) / "…so we insure the income first…" (HK$100K in the
  accent; the year-1 cost as one bar) / "…and sign the papers now" (four documents, ticked).
- **Read:** today, nothing → with cover → HK$100K → the papers.
- **Annotate:** headline, beside the two dashed bars: **"No disability cover today: their largest risk, uncovered"**
  (ranked first for both on severity, likelihood and warning time, proposal §8). Supporting: each segment of the cost
  bar named on the bar (disability HK$37K, critical illness HK$41K, medical HK$15K, term top-up HK$7K); a bracket over
  the whole bar, "14% of their surplus".
- **Voice:** Adrian's and Carmen's faces (built); in the lede's place, the concern in the case's words: "sufficient in
  the event of death, critical illness, disability, hospitalization or business disruption" (case p.5, concern 5).
- **Facts:** pay that continues if a parent can't work: HK$65K a month to 65 (Adrian), HK$39K to 62 (Carmen); the
  year-1 cost ≈HK$100K, ≈{{premiums_avg}} a year on average to retirement (sourced: 2026 rate cards, quotes to follow);
  key-person cover paid by the company; Ryan ≈HK$900 a year. The papers, in month one and under HK$25K: mirror wills
  (staged trusts at 25, 30, 35; a guardian for Chloe), enduring powers of attorney, advance directives; and a buy-sell
  agreement (case p.6 asks for business continuity and key-person risk). "Term, not whole life: the need ends at
  retirement."
- **Notes (defend):** more whole-life or a savings plan costs many times more for the same cover, because most of the
  premium buys savings they already hold; the new cover ends at 65 and 62, when the need ends; a disputed claim is
  carried by the 12-month reserve.
- **Bar:** "Protected first: now the plan can turn what they own into income."

### 6 · Call 2: decide now, not at {{own_sale_age}} (Fahtai; 0:45)
**Built 22 Oct** (prototype `looks/src/08_call2_v9.html`). Title (23 Oct, Fahtai's review): "Decide now, not at
{{own_sale_age}}: four decisions on what they own and spend lift the odds from {{own_89}} to {{ladder_5_89}}". **v10
changes:** the headline annotation links the flat row to slide 3's sale; the faces and the case's words; **the row
order is measured, or no ranking is claimed** (below).
- **In → out:** 3's sale at {{own_sale_age}} and 4's second row → "what's left is a cost the budget ignores" (7).
- **Picture (call ledger):** rows across the first two columns, each asset beside its decision: "What they own…" (grey
  bars to scale, case: the flat HK$11.5M, the business HK$5.0M, the MPF HK$1.7M, the budget HK$780K a year) / "…what
  each becomes…" (the flat: {{rmp_income}} a year for life by reverse mortgage from {{rmp_year}}, or downsize: they
  choose at 65; the business: sold in stages 2035 to 39 to her co-founder and managers, HK$3.0M counted of HK$5.0M,
  "their own way sells it too"; the MPF: two annuities, {{floor_2039_ann}} a year; the budget: a survivor plans on
  70%) / "…and what it achieves" (two bars on the 0–100% scale: their own way {{own_89}} grey, decided now
  {{ladder_5_89}} the accent, 72 px).
- **Read:** the flat row → the other rows → the two bars.
- **Annotate:** headline, on the flat row, the link back to slide 3: **"Paying from 65, not sold at {{own_sale_age}}"**.
  Supporting: under the grey bar, "the flat sold at about {{own_sale_age}}" (as built); **each row's share of the rise**
  once it is measured.
- **The row order (an open problem, found 23 Oct):** v9 ranks the rows "by what moves the odds" (flat, business,
  budget, MPF), but that order comes from the written case's ladder, which starts from investments alone. From their
  own way, the business should add almost nothing (inference: the model sells it for the same HK$3.0M both ways), and
  about half the rise is the survivor budget (Fahtai's model check, 23 Oct). So the slide implies a ranking its own baseline contradicts. **Measure the
  decomposition from their own way** (§8); until it is in `numbers.json`, order the rows by the size of the asset, and
  don't call the order a ranking.
- **Voice:** Carmen's face on the business row, both on the flat; in the lede's place, the concern in the case's words:
  "retain their current residence in retirement, downsize to a smaller property, or relocate" (concern 8); on the
  business row, "restructure, reduce, or monetize part of her business interest over time" (concern 7).
- **Notes:** more shares instead (80% in shares: {{alone_eq80_89}}, worst year {{alone_eq80_worst}}, and it breaks
  Adrian's profile); the 2039 floor ({{floor_2039_pct}} of essential bills; {{floor_2057_pct}} after Adrian's death, so
  never "for life"); even if the business never sells, {{biz_not_sold_89}}; the annuity is last on purpose, insurance
  for the worst markets ({{ann_w1_with_real}} vs {{ann_w1_without_real}}).
- **Bar:** "Decided now, four decisions close most of the gap; what's left is a cost the budget ignores."
- Answers questions 1, 7 and 8.

### 7 · Call 3: fix the cost the budget ignores (Fahtai; 0:40)
**Rebuilt 23 Oct with slide 3** (`src/04_s06-07.html`). Title: "Fix the cost the budget ignores: in that same future,
the money now lasts to 89 and the home stays theirs". **v10 changes:** the payoff written on the chart at slide 3's
sale and at the end; the defensive label goes to the notes; the premium inset explains its own drop.
- **In → out:** slide 3's picture, the same future, place and scale; 6's "a cost the budget ignores" → "Question 1,
  answered" (8 turns from the parents to each person).
- **Picture (story chart, panels 8 + 4):** left, the same future under the plan (the four decisions, the review at 75,
  the rules): the home pays {{rmp_income}} a year from {{rmp_year}} and stays theirs; savings never run out; their own
  way as a dashed line. Right, the premium inset (`series.py`): Flexi for life climbs to HK$375K a year (today's money,
  by 2056) vs the Standard plan from Adrian's 75, about a third the cost, the saving shaded; under it {{switch_89}} and
  the spending rules in one line.
- **Read:** the premiums and the review → {{switch_89}} → the rules → the future, redrawn.
- **Annotate:**
  - headline: at Carmen's {{story_sale_age}}, a hollow mark on the dashed line and a dashed leader to the top, **"Carmen
    {{story_sale_age}}: their own way sells the home here. With the plan, no sale"**; at the end, in the gutter and the
    accent, **"Savings last to 89; the home is still theirs"**, with "their own way" in grey beside the dashed line's
    end;
  - in the inset: "one policy after Adrian dies" at the drop, and "the saving" on the shaded gap.
  - The dashed line's own label shortens to "their own way"; the "ahead on paper until the 2050s" note moves to the
    speaker notes (it answers a question the slide doesn't ask). No inheritance figure on 7: it would compete with 12's.
- **Voice:** in the lede's place, concern 1 in the case's words: "on track to retire at their desired ages while
  maintaining their preferred standard of living".
- **Notes:** the defence (cut the budget now instead? the problem arrives after 2047, so the decision waits); why the
  plan looks poorer until the 2050s (part of the savings buys the annuities, and the home is drawn as income: a floor,
  not a peak); the guardrail details; the worst one in twenty ({{guardswitch_worst5_real}} vs
  {{fixswitch_worst5_real}}); the rules cost about {{guard_cost}} a year of typical spending; the switch is guaranteed
  under the VHIS rules (Code of Practice s.2.11, FAQ Q30; Fahtai, 23 Oct), so "subject to underwriting" appears nowhere.
- **Bar:** "Question 1, answered: they retire on time, keep the way they live, and keep the home."

### 8 · Call 4: one family policy, a plan for each person (Win; 0:50)
- **In → out:** 2's "30 months of spending" in cash and Chloe's "university in 2028" → "each parent's money fits their
  own risk" (9: and their values).
- **Picture (call ledger):** two horizontal bars of the same HK$7.7M (the parents' money outside the MPF and the home):
  **today** (cash HK$2.5M · bonds HK$1.35M · shares HK$3.85M in funds at about 1.5% a year) over **the plan**, each block
  with its owner's face: a 12-month reserve HK$1.0M · Chloe HK$2.57M · Adrian HK$2.07M · Carmen HK$2.07M. Under each
  parent's block, their mix as a thin bar: Adrian shares 40 · bonds 55 · cash 5 ("fits low to medium"); Carmen 60 · 35
  · 5 ("fits medium to high"), led by ESG funds (written case Figure 14; Fahtai, 23 Oct). Ryan in one line beneath.
- **Read:** today's bar → the plan's bar, block by block → the fee saving.
- **Annotate:** headline, the accent, on Chloe's block: **"HK$2.57M: her degree funded today, here or overseas"** (it
  covers the UK, Canada, Singapore and Hong Kong even after a currency shock; ring-fenced in HK dollars until she
  accepts an offer). Supporting: on today's cash, "HK$2.5M in cash: safe, but earning little"; between the bars, the
  change label "≈HK$45K a year less in fees".
- **Voice:** Chloe's words (case p.2): "attend a suitable university without excessive reliance on debt"; Ryan's (case
  p.5): "build his own financial independence": 30% of his pay into three pots of his own; his parents match half, up
  to HK$24K a year until 2037.
- **Facts:** Adrian's US Treasuries maturing 2037 to 41; rules agreed in advance (equities fall 20%: buy; drift 5
  points: rebalance); a quarterly review and an annual family meeting.
- **Notes (defend):** the alternative, one household portfolio, would break Adrian's profile or under-serve Carmen's;
  all Treasuries for Adrian fail almost every time after inflation.
- **Bar:** "Chloe's degree is funded today, and each parent's money fits their own risk."
- Answers questions 2 and 6.

### 9 · Call 5: values and innovation, with guardrails (Win; 0:45)
- **In → out:** 2's Carmen ("money that reflects her values") and Ryan ("holds crypto") → "without risk the family can't
  carry" (10 tests it).
- **Picture (call ledger, two halves):** left, ESG as a progress bar of the HK$10.47M investable: 11% today → 25%, the
  family's 20 to 25% goal band shaded, the three holdings named on the bar (BOC-Prudential MSCI World ESG Index Fund;
  Allianz Green Bond; Sun Life MPF Global Low Carbon Index Fund). Right, **four people, four views, four sizes**: each
  face with their view in the case's words and their crypto: Adrian 0% (a tokenised money-market fund counts as cash);
  Carmen up to 2% through an HKEX spot ETF; Ryan keeps his HK$500K, adds no new money, and his share glides from about
  74% of his wealth to 20% by 35 (a small line, the 20% dashed); Chloe none while studying.
- **Read:** the ESG bar to 25% → the test the funds pass → the four people, Ryan's glide last.
- **Annotate:** headline, the accent, on the ESG bar: **"25%: the top of the family's goal, in funds that pass two
  ratings"**. Supporting: on Ryan's line, "no new money: the share falls as his savings grow"; at the bar's start,
  "11% today".
- **Voice (the slide's drama):** the family disagree, in their own words (case p.2): Adrian "remains skeptical of
  digital assets"; Carmen is "open to new opportunities but concerned about volatility, fraud, custody"; Ryan is
  "optimistic about the long-term role of blockchain". The sizes resolve the disagreement without overriding anyone.
- **Facts:** ESG ratings agree far less than credit ratings (correlation about 0.54 vs 0.99; Berg, Kölbel and Rigobon,
  2022), so each equity fund must pass two (MSCI A or better; Sustainalytics risk below 20) and each green bond fund the
  ICMA principles; a downgrade means replacement within three months; no return premium assumed. Regulated channels
  only (HKEX ETFs, SFC-licensed platforms).
- **Notes (defend):** a forced sale of Ryan's crypto overrides his conviction and could push him to unregulated
  channels.
- **Bar:** "Their values and Ryan's conviction both fit, without risk the family can't carry."
- Answers questions 3 and 4.

### 10 · Will it hold? (Lookbua; 0:30)
- **In → out:** 7's "question 1, answered" → "then we tried to break it" → "it holds, and it starts this month" (11).
- **Picture (story chart):** paired bars per test on the 0–100% scale of 4 and 6, the four decisions alone (grey) vs
  the full plan (the accent): Adrian's job ends at 60 ({{adrian60_89}} → {{rec_adrian60_89}}); low returns every year
  ({{stressA_89}} → {{rec_lowret_89}}); inflation and medical costs ({{stressB_89}} → {{rec_stressB_89}}); and Carmen
  living to 95 ({{guardswitch_95}}), measured.
- **Read:** the lost job → the other tests → the reference line.
- **Annotate:** headline, the accent, on the lost-job pair: **"Even if Adrian's pay stops at 60, the money lasts in
  {{rec_adrian60_89}} of futures"**, with his face. Supporting: a dashed reference line at {{own_89}}, **"their own way, with no
  shock"**: all three tested plan bars clear it (measured, 23 Oct: {{rec_adrian60_89}}, {{rec_lowret_89}} and
  {{rec_stressB_89}} against {{own_89}}); Carmen to 95 stays a separate figure (a different horizon).
- **Facts:** the risk register in one strip (proposal Figure 26): suitability (one profile per person), crypto rules
  (licensed channels), greenwashing (two ratings), model risk (compare decisions, not forecasts), the business unsold
  (a buy-sell agreement now). Footer: we compare decisions in the same 10,000 markets, we don't forecast them;
  premiums are from rate cards until quotes arrive; the tier switch is guaranteed under the VHIS rules.
- **Bar:** "It holds when the hardest things happen, and it starts this month."

### 11 · What happens when (Lookbua; 0:30)
- **In → out:** 10's "it starts this month" → "for Ryan and Chloe, it lasts beyond it" (12).
- **Picture (map):** slide 4's axis again, now dated. On the left, year one magnified: month 1 the papers, the joint
  account, idle cash moved; months 1 to 3 the cover; months 1 to 6 a portfolio each, the investment policy signed,
  voluntary MPF; month 12 the first family meeting (charter, Ryan's plan, the one-person budget). Then event markers on
  the same years as slide 4: 2028 Chloe's offer, fees converted; 2032 managers built up; 2037 mortgage cleared, Adrian's
  annuity, the home released; 2039 Carmen's annuity, the business sold, the rules begin; 2047 the medical review.
- **Read:** year one → the dates → the reviews.
- **Annotate:** headline: a bracket over year one, **"Everything that can't wait is done in the first year"**.
  Supporting: over the dated part, "after that, dates trigger each step, not decisions"; the four faces at month 12.
- **Facts:** under the line, the reviews: quarterly portfolio, annual family meeting, a full review after a death, a
  disability, a business sale, a 20% market fall or a 1.5-point rate move (proposal Figure 23).
- **Bar:** "For the Wongs, it starts this month; for Ryan and Chloe, it lasts beyond it."

### 12 · What passes on (Pete; 0:25)
- **In → out:** the end of slide 3's picture returns (the same grey figure) → "Built to last: for their lifetimes, and
  after" (13 turns to us).
- **Picture (story chart, few words):** two bars, in the {{own_sold_pct}} of futures where their own way sells the flat,
  the same markets, today's money: their own way {{own_legacy_sold}} (grey) vs the plan {{plan_legacy_sold}} (the
  accent). Beside them, how it passes on: a short timeline for each child, staged trusts at 25, 30 and 35; a named
  scholarship in sustainable design, about HK$30K a year, joining Carmen's mission and Chloe's interest.
- **Read:** the grey bar (recognised from 3) → the accent bar → the stages.
- **Annotate:** headline: on the plan's bar, **"More than their own way in {{plan_legacy_more_pct}} of these
  futures"**. Supporting: under the grey bar, "their own way: the home sold, then spent" (3's words, back).
- **Voice:** Ryan's and Chloe's faces at the stages; concern 6 in the case's words: "intergenerational wealth transfer
  and financial responsibility between parents and children".
- **Notes:** across all futures, the home choice at 65 (keep {{legacy_keep}}, reverse mortgage {{legacy_rmp}}, downsize
  {{legacy_down}}); MPF to the estate (no nomination); estate duty abolished in 2006, so succession is about control,
  not tax.
- **Bar:** "Built to last: for their lifetimes, and after."

### 13 · Wealth Management Connect (Pete; 0:40)
- **In → out:** 12's "and after" → from the Wongs to families like them → 14.
- **Picture (map):** a schematic of Hong Kong, Macao and the nine mainland Greater Bay Area cities, the Southbound and
  Northbound flows as two straight arrows; the Wongs as a pin in Hong Kong.
- **Read:** the region and the flows → the advice rule → the Wongs' pin.
- **Annotate:** headline, on the Southbound arrow, a barrier mark: **"No solicitation or recommendation across the
  boundary unless the investor asks"** (HKMA Southbound page, checked 22 Oct). Supporting: on the Wongs' pin, "Not today:
  home, income and business all in Hong Kong; reviewed if Adrian's work moves across".
- **Facts (sourced, HKMA, checked 18 Oct):** since 2021; up to RMB 3M per investor since 2024 (RMB 1.5M each if both a
  bank and a securities firm); securities firms admitted in 2024; eligible products low to medium-high risk,
  non-complex.
- **Bar:** "Under the Connect, an adviser's value is a clear, suitable answer when the client asks."

### 14 · Who we want to become (all; 1:10)
- **Picture (people):** four cards, each in its owner's own first-person words: the goal in five years, what this plan
  taught them, the link to the Connect (personal statement, proposal p.14). The video carries their faces; the cards
  carry their words. **Win's line is a draft for Win to confirm; Lookbua's edited line needs his OK.**
- **Annotate:** none; one shared line across the four cards: the Connect.

### 15 · Close (Pete, all; 0:15)
- **In:** slide 4's map, complete: each row ticked, the grey sale line gone.
- **Picture (close):** "Built to Last"; the three pillars in one line ("Protected first, income for life, and a place
  for every voice"); the home their choice; the inheritance kept; the family; the team; "Thank you."

## 6. The look
**23 Oct: the deck's identity** (Pete: "all default fonts with no clear design work"; e-Sentry has a clear style; slide
2 a weak first impression). Look B's structure stays; its "no motif" plainness goes.
- **Type:** EB Garamond, the written case's own display face, for titles (35 px), panel headings (22 px) and big numbers
  (lining figures), so the deck and the PDF are one brand; Inter for all text (Pete liked it for small text).
- **Colour:** the written case's crimson #A81E2D as the accent (#6F1320 deeper); its family for fills: wine #7D1D2A
  (the conclusion bar, the home layer, the family panels, cost bars), rose #E6CBCF and #D3A1A8 (savings, lighter
  series), tint #F7ECED; warm neutrals tuned to the crimson (mist #F5F1F0, rule #DDD6D4, grey #A69E9C, slate #5A5250,
  ink #1B1716). No blue. Events on wine-and-rose charts in ink.
- **One decorative idea: the family's lifeline.** A ruler from 2026 to Carmen's 89 on the kicker row of each content
  slide; the crimson span is when that slide's decisions act ("When: now, until they retire"; "from 2035, for life";
  "from 2039; the review in 2047"). The same years are the time axis of slides 3, 7 and 11. Not used on 1, 13 to 15.
  **v10:** introduced at full size on slide 4, where it is the map; on each call slide the ruler is that call's row of
  the map, so it reads as "you are here", not ornament. If it isn't introduced on 4, drop it: at 200 px with 12-px
  years it can't be read on Zoom (§4: nothing meant to be read under 14 px).
- **Personality** (v10) comes from the family and the planners' voice, not more decoration: faces and the case's
  words on every call slide, annotations written as a planner talks, the family's disagreement on slide 9, and a
  rhythm of dense and light slides (§4a).
- **Annotations:** ink, Inter 14 or 16 px, straight leaders with a dot; the accent only for the headline annotation
  when it is the title's claim; periods hatched in the accent, never filled pale (§4a).
- **Signature:** a short crimson mark before every kicker (the call's numbered square on call slides); the cover's
  crimson bar; the family on a wine panel (cover, slide 2).
- **Not used:** gridlines across chart areas; a section tracker (the kicker navigates); grey-only charts; blue.
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
| **v10:** the rise from {{own_89}} to {{ladder_5_89}} split by decision, starting from their own way (the home chosen at 65 instead of sold, the survivor budget, the annuities; the business is sold both ways), as new keys in `export_numbers()`, with `numbers.json` diffed and the change logged in `reviews/applied.md` | 6 | Fahtai (model), builder | Slide 6 orders its rows by the size of the asset and claims no ranking (§5, slide 6) |

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
| A practitioner | "If their own way sells the business too, why is it your second row?" | 6: v10 orders the rows by measured share of the rise, or by asset size with no ranking claimed, until the split is measured (§8) |
| A risk head | "What if Adrian loses his job before 65?" | 10 |
| A regulator | "Are these products suitable and licensed?" | 8, 9, 10 |
| An ESG judge | "How do you know these funds aren't greenwashing?" | 9 |
| A fintech judge | "Why let a 24-year-old hold 74% in crypto?" | 9: his money, about 2% of family wealth, no new money, glide to 20% |
| Any judge | "10,000 simulations: false precision?" | 10: we compare decisions, not forecasts |

## 11. Compliance and logistics (a breach can disqualify)
No university name, logo, campus, clothing, lanyard or account in any frame or file; files named "Axis"; PowerPoint
and MP4 metadata scrubbed (Office stamps the signed-in account: never submit an Office-exported PDF; `Fin Plan.pdf` in
the repo root is one, and is git-ignored); deliver by hand on Monday morning with a download link emailed as a backup.

## 12. From v9 to v10 (23 Oct, proposed)
Pete: the story and the points are right; the pages list facts without connecting them, lack personality, and their
charts have no annotation. The content, the titles, the numbers and the script stay; how each page tells it changes.
- **The spine (§3):** slide 3's picture of their money is the deck's road: problems marked on it (3), the calls laid on
  its years (4), the same picture redrawn with the plan (7), its end paid off (12). Replaces v9's "threads", which
  still described the ten futures dropped on 23 Oct.
- **Setups and payoffs (§3):** eight, each planted and paid off on the page; one look for the chance the money lasts.
- **Story and annotation (§4a, new):** what went wrong in v9; what the reference decks do that v9 doesn't; seven
  rules, a vocabulary and two tests (finger, flick); five slide types; the family's own words on every call slide;
  where personality comes from; the order of work before Saturday's recording.
- **§5 rewritten to one template** (in → out, picture, read, annotate, voice, facts, notes); built slides list their
  v10 changes. The biggest: 3 writes its claim on the chart and drops the side box (the 61% moves to 2); 4 becomes the
  map, grouped by the three pillars; 7 writes its payoff where their own way sold the home; 9 shows the family's three
  views on crypto.
- **Found while rewriting:** slide 6's row order implies a ranking its own baseline contradicts (about half the rise
  from their own way is the survivor budget, and the business is sold both ways): measure it (§8) or claim no ranking.
- **§6:** the lifeline is introduced at full size on 4, or dropped; personality and annotation added to the look.

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
