# Business R/I candidate

Fahtai's standalone candidate, 13 November 2026. It inherits the existing Final deck's fonts, tokens, title style
and conclusion bar. It does not replace Lookbua's whole-household slide 5 or add a slide to the timed main deck.

**Job:** show how Risk and Impact are assessed before Select. The reusable scan and activity trace appear first;
Carmen's packaging is the example; the bottom of each column states the evidence Select needs. Customer loss is a
conditional exposure, not an established outcome. The approximately 98% share is the existing illustrative business
estimate, not measured company data or an achieved reduction. Full sources and boundaries are in the speaker notes.

Edit `slide.html` and `slide.css`, then run `python Final/deck/business-ri/build.py` from the repo root (or the
equivalent relative path from Final). The build reuses `Final/deck/src/00_head.html` and embeds its fonts, producing
`Axis.html`. Run `python Final/deck/business-ri/render.py` to render with installed Chrome and check font loading
and element bounds; `Axis.png` is the visually checked preview. Temporary browser profiles and DOM output stay in
the ignored `build/` directory. No PowerPoint export has been performed for this candidate.

The candidate is allotted 55 seconds. Main-deck placement and the effect on the ten-minute running time need to be
settled alongside the remaining business Select slides; the candidate is not silently inserted into that schedule.

Existing shared model figures and main-deck source files are unchanged.
