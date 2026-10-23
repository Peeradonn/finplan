# Round Two deck fixes (Fahtai)

From Fahtai (model and numbers) · 23 Oct 2026 · for Pete

These are my review findings on the v9 deck (`round2/src/`, main at `0586b8b`, 22 Oct). I rendered the slides and checked
every model number on my slides against `figures/numbers.json`. I also reran the model for the "their own way"
baseline. Following CLAUDE.md, I haven't edited any slide; these are suggestions for the builder.

**Already correct:**
- 62% own way, 51% sell, sale at about 83 (79–87).
- The ladder 33 → 43 → 60 → 82 → 83%, and 97%.
- All ten futures last with the plan.
- HK$230K reverse mortgage, HK$375K premium peak, HK$2.3M vs HK$7.7M.
- I reproduced these by running `model/run_model.py` myself.
- No `{{` placeholders left. Your earlier fixes are in: "worst one in twenty" in the notes, "subject to underwriting",
  no `fut_*` keys missing.

## Fixes, most important first

| # | Slide | Change | Why | Source of the finding |
|---|---|---|---|---|
| 1 | 6 | Bar label "the same assets" → **"decided now"**; don't say "same assets" in the script | About half of 62% → 83% comes from spending less after a death, not from the assets (model test below) | My review of v9, 22 Oct (model rerun) |
| 2 | 3 (notes) | Add the answer to "why not a reverse mortgage at 83?" | A late reverse mortgage pays a lot, and a judge may ask. Our model says it's worse than selling, so slide 3 stands | Fact check (b), 23 Oct, and a model test |
| 3 | 7 (title) | "none sells the home" → **"none is forced to sell the home"** | Slide 6 lets them choose to downsize at 65, which is selling | My review of v9, 22 Oct |
| 4 | 7 (notes) | Remove "The switch is subject to underwriting until the insurer confirms"; say it's guaranteed under the VHIS rules | Confirmed: VHIS Code of Practice s.2.11; VHIS FAQ Q30 (25 Sep 2025) | Fact check (a), 23 Oct |
| 5 | 6 (notes) | Add one line on the annuity's death benefit | Answers "what if Adrian dies early?" | Fact check (c), 23 Oct |
| 6 | 8 (when built) | Carmen's mix **shares 60 / bonds 35 / cash 5** | The v7 deck had 33/7 typed in. Figure 14 of the written case gives 35 bonds (3450 5 + AGGU 20 + green 10) and 5 cash (3053) | My review of v7, 20 Oct |
| 7 | 14 | My career line (wording below) | The deck has a shortened version that drops "data", "East and Southeast Asia" and what I built | My review of v7, 20 Oct |
| 8 | 6 (notes, optional) | Don't call HK$230K "conservative" | It's about right for a joint loan with Carmen at 60; only a single borrower at 65 gets more | Fact check (b), 23 Oct |

---

### 1 · Slide 6: "the same assets"

**Now.** The bars read "Their own way 62%" vs "Decided now 83%, the same assets". The script says "The same assets,
decided now: 83%, not 62%."

**The problem.** The 62% baseline keeps the **couple's full budget after Adrian's death** (footnote: "the budget kept
after a death"). The 83% includes decision 1, the survivor planning on 70%. That's a spending change, not an asset. I
reran the model with "their own way" also cutting the survivor's budget to 70%:

| Their own way, 10,000 markets | Lasts to Carmen's 89 | Flat sold |
|---|---|---|
| As in the deck (full budget after a death) | 62% | 51% |
| Survivor budget 70%, otherwise the same | **73%** | 40% |
| The plan (four decisions) | 83% | none sold by force |

So of the 21 points, about **11 come from the survivor budget** and about **10 from deciding the home, business and
MPF now**. A practitioner judge might call a widow spending the couple's full budget a straw man.

**The fix (small).** The slide already shows the "Their budget → A survivor plans on 70%" row, so the decision is on
screen. Only the label overclaims.
- Bar caption: "Decided now, the same assets" → **"Decided now"**.
- Script: "The same assets, decided now: 83%, not 62%." → **"Decided now, not at 83: 83%, not 62%."**
- Optional note for Q&A: "Even if their own way also cut the survivor budget to 70%, it would reach 73%: deciding the
  home and business now is worth about ten points on its own."

File: `round2/src/04_s06-07.html` (the bar caption at line ~45, the notes at line ~52).

### 2 · Slide 3: the late reverse mortgage

**The question a judge may ask.** "Why would Carmen sell? She could take a reverse mortgage at 83 and stay."

**What I found** (details in `reviews/round2-fact-checks-fahtai.md`, §b):
- HKMC's March 2026 table pays a single 83-year-old HK$5,640 a month per HK$1M counted, for life.
- On the model's flat value in 2060 (HK$19.1M as paid), that's about **HK$916K a year as paid, ≈HK$396K in today's money**.

**What the model says.** I ran "their own way" with a reverse mortgage at the moment the money runs out, instead of
the sale:

| Their own way | Lasts to Carmen's 89 |
|---|---|
| Sell the flat when the money runs out (deck) | **62%** |
| Reverse mortgage instead | **51%** |

The payout is fixed and doesn't cover her bills, which are the full budget plus Flexi premiums up to HK$375K a year.
Selling releases a lump sum that lasts longer. So **slide 3 stands**: selling is the better of the two options for
their own way.

**The fix.** Add to slide 3's notes:
> *"Why not a reverse mortgage at 83? It would let Carmen stay: about HK$400K a year in today's money, for life (HKMC,
> March 2026 table). But it's fixed and doesn't cover her bills: the money then lasts to 89 in only 51%, worse than
> selling (62%), and the loan eats into what Ryan and Chloe inherit."*

If this goes on screen, add it to the model first (e.g. `own_rm_89` in `export_numbers()`), so it's a `{{key}}`. I ran
it as a separate test script with today's HKMC table (age rates interpolated, HK$8M threshold fixed); `run_model.py` is unchanged.

### 3 · Slide 7: "none sells the home"

Title now: "…now all ten futures reach Carmen's 89, and none sells the home". On slide 6, "they choose at 65: stay, with
a reverse mortgage, or downsize". Downsizing is selling, by choice.
**Fix:** "…and **none is forced to sell** the home". The script line "and not one sells the home" becomes "and not one
has to sell the home".

### 4 · Slide 7 notes: underwriting

**Now:** "The switch is subject to underwriting until the insurer confirms."
**Fix:** "The switch is guaranteed: under the VHIS rules, every Flexi policyholder can move to the insurer's Standard
Plan at renewal without new medical checks, at any age (VHIS Code of Practice s.2.11; VHIS FAQ Q30, 25 Sep 2025).
Exclusions from the original policy stay; no new ones can be added."
The deck plan §8 fallback ("Say 'subject to underwriting' on 7 and 10") is no longer needed. Today the phrase appears only
in slide 7's notes (line ~116); don't add it to slides 10 or 15 when you build them.

### 5 · Slide 6 notes: the annuity if Adrian dies early

**Add:** "If Adrian died soon after buying, the family wouldn't lose the money: HKMC pays the premium less what's been
received as a lump sum, or keeps paying until 105% is returned (HKMC Annuity brochure, April 2024). Single life only,
so one policy each."

### 6 · Slide 8 (when built): Carmen's mix

The v7 slide 8 typed Carmen's bar as shares 60 / bonds 33 / cash 7. The written case (Figure 14, `document/pages-03-09.html`)
has Carmen at 3450 5% + AGGU 20% + Allianz Green Bond 10% = **35% bonds**, and 3053 **5% cash**. Adrian's 40/55/5 is
correct.

### 7 · Slide 14: my career line

**Now** (card and script): "I want to build the risk models that wealth managers across Asia use for families. This plan
taught me that a model's job is to price the trade-offs between people. Next is the FRM, with Connect funds as my first case."

**Please use** (my approved wording, trimmed to fit about 15 s):
> "In five years I want to build the data and risk models that wealth managers across East and Southeast Asia use to
> advise families. Building this proposal's model, from the salaries-tax engine to 10,000 simulated markets, taught me
> that a model's job is to price the trade-offs between people. Next is the FRM, with Connect funds as my first case."

That's about 55 words, about 15 seconds more than now. If the time is short, keep the current line and change only "across Asia" →
"across East and Southeast Asia", and "risk models" → "data and risk models".
Card: "Building data and risk models for East and Southeast Asia's wealth managers".

### 8 · Slide 6 (optional): HK$230K

HK$230K a year from 2037 matches a **joint** loan with Carmen as the younger borrower (about 60). Carmen must be on the
loan to stay after Adrian's death. A single borrower at 65 would get about HK$323K on the 2037 value, so don't describe
HK$230K as conservative. Nothing on the slide needs to change.

---

## Checklist for Pete

- [ ] 1 Slide 6: "decided now" label and script
- [ ] 2 Slide 3: reverse-mortgage note
- [ ] 3 Slide 7: "forced to sell"
- [ ] 4 Slide 7 notes: drop "subject to underwriting" (and keep it off 10 and 15)
- [ ] 5 Slide 6: annuity death-benefit note
- [ ] 6 Slide 8: Carmen 60/35/5
- [ ] 7 Slide 14: Fahtai's line
- [ ] After the remaining slides are built: I'll run a final numbers check of the whole deck against `numbers.json`
  and the Round One PDF.
