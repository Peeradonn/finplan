# Reviews

Three sessions work in parallel. Reviewers find; the builder changes the document.

| Session | Brief | Writes (only these) |
|---|---|---|
| Story and coherence | `brief-story.md` | `story-findings.md` (append only) |
| Number check | `brief-numbers.md` | `numbers-findings.md` (append only) |
| HTML builder | `brief-builder.md` | page sources, `document/manuscript.md`, model, `figures/`, `applied.md`, git |

**Hand-off.** Reviewers write findings in batches and end each with `## Batch N ready`. The builder takes ready batches,
applies them, rebuilds (15 pages, all fit), and logs each finding in `applied.md` as Applied, Rejected (reason) or
Deferred. No two sessions write to the same file.

**Starting a session:** open Claude Code in this folder and say, for example,
"You are the HTML builder. Follow `reviews/brief-builder.md`."
