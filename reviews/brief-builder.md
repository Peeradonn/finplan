# Brief: HTML builder

**Your job:** turn the reviewers' findings into the document. You are the **only** session that edits the page sources,
`document/manuscript.md`, the model and `figures/`, and the only one that commits. Read `CLAUDE.md` first.

## Inputs, and who writes what

| File | Written by | You |
|---|---|---|
| `reviews/numbers-findings.md` | number checker (appends only) | read; never edit |
| `reviews/story-findings.md` | story reviewer (appends only) | read; never edit |
| `reviews/applied.md` | **you** | log every finding you act on |

Reviewers end each batch with a line `## Batch N ready`. Work only on batches marked ready; findings below the last
"ready" line are still being written. Keep a note in `reviews/applied.md` of the last batch you took from each file.

## For each batch

1. **Order:** wrong numbers → inconsistent numbers → missing case requirements → story and flow → wording.
2. **Judge each finding** against `CLAUDE.md` (decisions already made, hard rules). Apply it, reject it with a reason, or
   defer it (needs Pete or an outside fact). If two findings conflict, the number checker wins on facts, the story
   reviewer on wording; if unsure, ask Pete.
3. **Apply it in the right place:**
   - Wording: the page source (see the table in `CLAUDE.md`) **and** the same text in `document/manuscript.md`.
   - A model number: never type it. Add or fix the key in `export_numbers()` (`model/run_model.py`), rerun
     `make_charts.py`, and use `{{key}}` in both files. If a model input changes, rebuild the workbook
     (`build_xlsx.py` → `tools/recalc.ps1`) and diff `numbers.json` before and after: every changed number must be
     expected, and hard-typed text that depends on it must be updated too.
   - A chart: change `model/make_charts.py`, never the PNG.
4. **Rebuild and check fit:** `cd document && ../.venv/Scripts/python.exe assemble.py && ../.venv/Scripts/python.exe
   render.py proposal.html`. It must report 15 pages and every page "fits". If a fix overflows a page, cut words on
   that page (say what you cut in the log); never shrink fonts below 12pt, change margins or drop a required element.
5. **Look** at the PNG of every page you changed (`document/build/page-N.png`): wrapping, orphans, tables.
6. **Log** each finding in `reviews/applied.md`:
   ```
   N3 · Applied · page 10 · "old words" → "new words" (manuscript synced)
   S5 · Rejected · contradicts the decision to keep the annuity last in the ladder (CLAUDE.md)
   N7 · Deferred · needs the HKMC death-benefit terms (Pete)
   ```
7. **Commit** the batch if Pete has agreed to per-batch commits (ask once at the start), with a message listing the
   finding IDs.

## Before you start: pending direct edits

`document/proposal-v2.html` holds edits made directly to a built copy (new headings on pages 2 and 3, among others).
Built HTML is overwritten by `assemble.py`, so those edits are lost unless carried into the sources. Diff it against
`document/proposal.html`, list the changes for Pete, apply the ones he approves to the page sources and manuscript,
then delete `proposal-v2.html`.

## When a batch is done

Tell Pete: how many findings were applied, rejected and deferred; the pages changed; free space left on each changed
page; and anything he must decide. Do not export PowerPoint unless he asks.
