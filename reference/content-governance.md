# Content Governance and Decomposition

This file defines how messaging requests become maintainable repository updates.

## Core rule

Prefer decomposition and propagation over net-new standalone messaging pages.

- Decompose requests into reusable modules
- Update canonical source files
- Propagate changes to related modules through review and automation

## Core versus overlay model

### Canonical core (this repository)

- `framework/`
- `use-cases-value-pillars/`
- `products/`
- `offerings/`
- `offerings/solution-bundles/`
- `reference/`

### Overlays (context-specific)

Overlays are fast-moving adaptations that should reference canonical core messaging instead of duplicating claims.

Examples of overlays that often belong in private systems:

- Market intelligence, internal market analysis, and internal response talk tracks
- Customer-specific confidential details
- Restricted internal business or legal details

Examples of overlays that may be public when safe and reusable:

- Campaign angle
- Region angle
- Industry angle

## New-file decision gate

Before adding a new markdown file, the contributor must answer:

1. Which existing files were reviewed first?
2. What exact gap was found?
3. Why can this not be an update to existing canonical files?
4. Who owns long-term maintenance of the new file?
5. What decomposition and propagation plan will keep related files aligned?

If these are not answered, the change should not merge.

## Practical decomposition examples

### Example: "Crunchy + PostgreSQL + APAC concern"

Break into modules:

- PostgreSQL product framing -> `products/postgresql/`
- Shared risk/continuity or future-readiness framing -> `use-cases-value-pillars/`
- Region-specific adaptation -> private overlay
- Internal response talk track -> private overlay

Do not create one standalone page that bundles all contexts into a single one-off narrative.

## Operating practices that preserve momentum

- Capture every idea quickly through issue intake
- Triage weekly into:
  - update existing module
  - create private overlay
  - rare new canonical file request
- Measure success by reuse and reduced duplication, not by count of new files