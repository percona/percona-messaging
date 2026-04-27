# Contributing to Percona Messaging

Percona Messaging improves through small, reviewable changes. You do not need to be a Git expert to contribute, but you do need to make it easy for reviewers to understand what changed, why it changed, and what else may be affected.

## Product managers and owners

*Not a PM or product owner? Skip to **[Who can contribute](#who-can-contribute)**—everything from there down is shared guidance.*

- **Open an issue** as soon as you know something is changing and will need to be **described** in canonical messaging. **Before go-live is normal and encouraged**—early issues are part of working transparently here, not something to avoid until launch week.
- **Open a pull request** (draft is fine) as soon as you know **which product or feature** is changing. You do not need final copy first: a PR starts review and **runs automation** (terminology, impact hints, governance checks), which helps catch drift early.
- If Marketing or GTM will package the change (web, social, decks, campaigns, launches), say so and leave **time after merge** for them to adapt—still open the issue or draft PR early.

For structured intake, use *New issue* → **Messaging intake and decomposition** — [template](.github/ISSUE_TEMPLATE/messaging-intake-and-decomposition.md).

## What this repository does not do yet

*This applies to everyone, including PMs.*

There is still **no single automated path** from merged markdown to social, the website, or every downstream asset. Percona’s portfolio is not one product line, and teams do not all watch this repo the same way. Canonical messaging **lives here after merge**; getting it into campaigns, social, and sales materials still takes explicit handoff for now. We want clearer propagation and visibility over time; until then, early issues and PRs plus clear notes in the description are how people find out.

## Who can contribute

Anyone with useful context can contribute. That includes product owners, Solutions Marketing, developer advocates, designers, reviewers, and collaborators working from downstream assets back to the canonical source.

## Before you edit

1. Find the canonical file that should hold the change.
2. Check the relevant reference guidance in `reference/` and `.cursor/rules/`.
3. Ask whether the change affects other files, names, or claims across the repository.

## Ways to contribute

- GitHub web UI: best for small wording, factual, or formatting changes
- `github.dev`: best for multi-file edits in a browser-based editor
- Local clone: best for contributors comfortable with Git or using AI-assisted editors

## Markdown whitespace formatting

For markdown structure checks, this repository enforces whitespace consistency only:

- no trailing spaces (`MD009`, with normal 2-space hard-break behavior)
- no multiple consecutive blank lines (`MD012`)
- one trailing newline at end of file (`MD047`)

Use the same CLI locally as CI:

- Check: `npx -y markdownlint-cli2@0.22.1 "**/*.md"`
- Autofix: `npx -y markdownlint-cli2@0.22.1 --fix "**/*.md"`

## Contribution workflow

1. Make the smallest change that solves the problem.
2. Update the canonical source, not only the downstream derivative.
3. Open a pull request that explains what changed, why, and what other files may need attention.
4. Respond to review, revise as needed, and merge once approved.

## What reviewers look for

- Factual accuracy and claim defensibility
- Correct naming, terminology, and license language
- Reusable language rather than one-off copy tied to a single asset
- Alignment with the existing framework and surrounding pages
- Clear notes about downstream impact when a core term or position changes

## Definition of done

- The right canonical file has been updated
- Naming and terminology rules are followed
- Related files have been checked when the change affects shared language
- The pull request explains rationale and likely downstream impact
- Required reviewers have approved the change

## Examples of strong contributions

- Correcting a product or offering name in the canonical source and updating related references
- Improving a reusable value statement so downstream teams can adapt it consistently
- Clarifying a messaging section and noting which other files should be reviewed for alignment

## What not to put in tracked content

Do not move internal planning notes, private review prep, sequencing notes, or other working material into canonical repository docs. Keep that material in gitignored `*.draft.md` files or outside the repository.

## Reference files

- [reference/canonical-naming.md](reference/canonical-naming.md)
- [reference/banned-terms.md](reference/banned-terms.md)
- [reference/brand-voice.md](reference/brand-voice.md)
- [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md) (after intake, how changes spread across files)
- [GOVERNANCE.md](GOVERNANCE.md)

## Getting help

- If you are not sure where a change belongs, open an issue or draft pull request and ask for direction.
- If a change feels high-risk or cross-cutting, ask for review early rather than waiting for a polished draft.
