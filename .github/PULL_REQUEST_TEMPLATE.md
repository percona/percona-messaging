## What changed

## Why

## Sources and evidence

- Link **public** release notes, docs, or roadmap pages here when claims depend on them (helps reviewers and future readers).
- Do **not** paste private repo paths, CRM links, customer identifiers, or restricted competitive material in the PR body or thread. If evidence is internal-only, say you aligned with the listed reviewers and keep detail in approved channels.

## Related issues

<!-- Link any GitHub issues this PR closes or coordinates with (e.g. hub issues). If another PR must land first for the same files, say so here. -->

## What else might be affected

For a structured pass (customer impact level, value pillars, when to update `framework/why-percona.md`), use **`.cursor/rules/impact-analysis.mdc`** in Cursor, or the full human flow in **`reference/decomposition-and-propagation.md`**. The **Impact Check** and **Smart Suggestions** bot comments on this PR are text-map **candidates**; triage them with that rule when decisions matter (they do not include the L/M/H rubric by themselves). Even when the bots are quiet, sanity-check whether **`framework/`**, **`products/`**, **`use-cases-value-pillars/`**, or **`offerings/`** need aligned edits when claims, naming, or pillars shift.

## New markdown file gate (required only when adding new `.md` files)

### Existing files reviewed first

### Exact gap not covered by existing files

### Why this must be a new canonical file

### Owner and maintenance plan

### Decomposition and propagation plan

## Checklist

- Product/offering names match `reference/canonical-naming.md`
- No banned terms (see `reference/banned-terms.md`)
- "Open source" is not hyphenated anywhere in the change
- Licensing claims are accurate (SSPL = "source available," not "open source")
- Relevant PM has reviewed for technical accuracy (required for product section changes)
- I have checked other files that might reference updated terminology
- This PR description does not rely on paths or links that only exist outside the public repository (no `instructions/` or other private-tree references)
