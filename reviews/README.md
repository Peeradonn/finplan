# Reviews

Parallel review sessions write findings here; one integrating session applies them.

| Session | Brief | Writes |
|---|---|---|
| Story and coherence | `brief-story.md` | `story-findings.md` |
| Number check | `brief-numbers.md` | `numbers-findings.md` |
| Integrator (applies fixes) | `CLAUDE.md` | page sources, `document/manuscript.md`, model; then rebuilds and checks fit |

**Integrator order:** wrong numbers first, then story fixes, then wording. After each batch: `assemble.py`,
`render.py proposal.html` (15 pages, all fit), look at the changed page PNGs, and mark each finding in its file as
`Applied`, `Rejected (reason)` or `Deferred`.
