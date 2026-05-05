# Agent guidelines (portable baseline)

This file is the **shared baseline** for humans and coding agents (Cursor, Claude Code, headless runners, and similar tools). **Cursor-specific packaging** lives under `.cursor/rules/` and must **not** contradict this document on git boundaries or on where canonical messaging rules apply.

## Git and automation boundaries

Unless the user **explicitly** asks for that action in the conversation:

- Do **not** create a git commit.
- Do **not** push to a remote.
- Do **not** merge branches.
- Do **not** open or submit a pull request.

Casual wrap-up such as "finish it," "wrap up," or "you are done" **does not** count as permission to commit, push, merge, or open a PR **unless** the user clearly names that action (for example "commit this," "open the PR," "push the branch").

Preparing diffs, suggested commit messages, and suggested PR descriptions **without** committing or pushing is fine unless the user forbids it.

## Rule layering

| Layer | Role |
| --- | --- |
| **This document** | Portable baseline: git boundaries, how guidance scopes apply, pointers into human docs. |
| **[CONTRIBUTING.md](../CONTRIBUTING.md)** | Contribution workflow, definition of done, markdown hygiene expectations. |
| **[reference/](../reference/)** | Naming, voice, decomposition, and governance references contributors reuse across edits. |
| **`.cursor/rules/`** | Short reminders and Cursor-facing packaging; align with this baseline (no conflicting git policy or scope). |

If `.cursor/rules/` and this baseline ever disagree on git boundaries or scope, **this baseline wins**.

## Applies to all edits

When editing **any** tracked content:

- Follow **[CONTRIBUTING.md](../CONTRIBUTING.md)** for workflow and what belongs in the repository.
- Treat **[terminology and naming](../.cursor/rules/terminology-and-naming.mdc)** guardrails as repo-wide for terminology, banned terms, formatting conventions described there, and licensing accuracy called out in that rule, unless you are only touching purely mechanical automation config unrelated to prose.

Keep internal planning, sequencing-only notes, and reviewer-only instructions **out** of canonical messaging files (see CONTRIBUTING **What not to put in tracked content**).

## Applies only to canonical messaging paths

The stronger messaging-quality bars (**value linkage, canonical audience, present-state framing**, placement rules, and related Cursor snippets) apply when editing reusable positioning under:

- `products/`
- `framework/`
- `use-cases-value-pillars/`
- `offerings/`
- `reference/` **when** the file is **canonical positioning** (not contributor-only docs such as navigation READMEs inside `reference/` that only explain the repo).

For those paths, combine this baseline with **[reference/canonical-naming.md](../reference/canonical-naming.md)**, **[reference/banned-terms.md](../reference/banned-terms.md)**, **[reference/brand-voice.md](../reference/brand-voice.md)**, and **[reference/decomposition-and-propagation.md](../reference/decomposition-and-propagation.md)** as appropriate.

## Human docs for governance and automation

- **[GOVERNANCE.md](../GOVERNANCE.md)** for ownership, approvals, and canonical status when changes warrant it.
- **[AUTOMATION.md](../AUTOMATION.md)** for how CI relates to this repository (agents still follow the git boundaries above).

## Out of scope for this baseline

Automated enforcement (pre-commit hooks, new CI gates) is a **separate** decision and issue. This document describes expectations for agents and contributors, not new automation.
