# Brief: story and coherence review

**Your job:** read the proposal as a judge would and find every place where the argument does not hold together.
You do **not** check whether numbers are correct (another session does); you check whether they are *used consistently
and make sense where they appear*. You do not edit the page sources or the manuscript: write findings to
`reviews/story-findings.md` in the format below.

## Read

1. `CLAUDE.md` (rules, decisions already made and why).
2. `document/build/proposal.pdf`, page by page. Rebuild first so it is current:
   `cd document && ../.venv/Scripts/python.exe assemble.py && ../.venv/Scripts/python.exe render.py proposal.html`.
   Page images are in `document/build/page-N.png`; the PDF text can be read with PyMuPDF.
3. The case (`Primary Info/Award2026Case20260919.pdf`): the family's goals, concerns and questions. The manuscript
   (`document/manuscript.md`) lists, for each page, what the case asks for ("Case asks for:").

## Check, in this order

1. **The spine.** Can you state the plan in three sentences after reading only the cover and page 2? Does every section
   serve the theme "Built to Last" and its three pillars (Protect · Turn assets into lifelong income · Give every voice a
   place)? Is there anything that belongs to no pillar?
2. **Promises kept.** Every claim on the cover and page 2 must be shown in the body. Every recommendation in the body that
   matters should be visible from page 2 or the roadmap (page 12).
3. **The case is answered.** For each section, tick off what the case asks for. List anything missing or answered only
   in passing. Check that each family member's goals and concerns (Adrian, Carmen, Ryan, Chloe) are addressed.
4. **Consistency.** The same thing is described the same way everywhere: the four decisions (and their order), the
   annuity (single life, insurance for the worst case), the medical tier review, guardrails, the ESG target, portfolio
   splits, the home decision in 2037. Section and figure cross-references (§ numbers, "Figure N") point to the right place.
5. **Each section's defence.** Every section should name the alternative it rejected, why the choice suits this family,
   the trade-off, and what happens if it fails. Flag sections where this is missing or weak.
6. **Flow.** Does each page lead to the next? Repetition that wastes space? A judge's likely first question on each page
   that the page does not answer?
7. **Voice.** Plain English, client-first. Flag jargon, model-speak, shorthand, or anything a family could misread.

## Findings format (`reviews/story-findings.md`)

Rank by how much the fix would move the score. One entry per issue:

```
### S1 · Page 4 · severity: high | medium | low
Quote: "exact words from the page"
Issue: what is wrong or missing, and why a judge would care.
Fix: the change you propose (new wording if it is a wording fix). Say which page has room: render.py reports free mm.
```

End with a short list of **what works well** (so the fixes do not break it) and **anything you are unsure about**.
Pages have little spare room (see `render.py`'s report): a fix that adds text should say what it replaces.
