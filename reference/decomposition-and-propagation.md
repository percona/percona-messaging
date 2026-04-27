# Decomposition and Propagation Guide

Use this guide when requests arrive as one-off messaging and need to become maintainable canonical updates.

## Why this process exists

Creating net-new pages is fast in the short term and expensive in the long term. Decomposition and propagation reduce duplication and keep messaging maintainable.

## Core method

1. **Intake:** capture request in issue with source context and timing.
2. **Decompose:** split the request into reusable message modules.
3. **Map:** assign each module to existing canonical files.
4. **Update:** edit canonical files first.
5. **Propagate:** update related files impacted by claim, positioning, or naming changes.
6. **Exception path:** request new-file approval only if a real gap remains.

## AI-assisted decomposition (recommended)

If you use an AI assistant, keep prompts anchored to repository policy and naming rules:

- Start with this guide plus `reference/content-governance.md`.
- Use `.cursor/rules/impact-analysis.mdc` for impact and propagation checks.
- Use `.cursor/rules/terminology-and-naming.mdc`, `.cursor/rules/offering-naming.mdc`, and `.cursor/rules/brand-voice.mdc` for wording consistency.
- Ask for a decomposition output that includes: reusable modules, target canonical files, propagation targets, and whether any true new-file gap remains.

AI can accelerate routing and draft generation, but owners and reviewers still decide final claim quality and approval.

## Decomposition map

Use this quick map for routing:

- Company narrative: `framework/`
- Shared value and scenario narratives: `use-cases-value-pillars/`
- Product-specific framing and product language: `products/`
- Core service messaging: `offerings/`
- Sold package messaging: `offerings/solution-bundles/`
- Naming and policy guidance: `reference/`

## Example decomposition

Request:
"Need messaging for PostgreSQL risk after market change in APAC."

Decompose into:

- PostgreSQL product framing and positioning updates -> `products/postgresql/`
- Shared risk/continuity and future-readiness narrative -> `use-cases-value-pillars/`
- Region-specific campaign adaptation -> **execution-layer output** (owned by the requesting team)
- Internal market-response talk track -> **execution-layer output** (owned by the requesting team)

Do not create one standalone markdown page that combines all contexts.

## Execution-layer outputs vs canonical updates

**Canonical updates** live in this repository as durable modules (`framework/`, `products/`, `offerings/`, `use-cases-value-pillars/`, `reference/`).

**Execution-layer outputs** are the real-world deliverables teams assemble from canonical modules: talk tracks, campaign assets, regional variants, sales enablement packs, customer-specific decks, and similar artifacts. They live in whatever systems those teams already use for execution and distribution.

Rules:

- Teams own execution-layer assembly from canonical source.
- If a team cannot produce what they need from canonical modules, open an issue here describing the gap (what is missing, what was tried, and what output is blocked).
- If something is reusable and durable, bring it back into canonical modules through normal issue + PR flow.
- A future goal is a smoother interface between canonical modules and execution tools; that is not required to start.

**When to keep work in execution vs add canonical surface area**

- Keep in execution when it is audience-specific, time-bound, or combines existing modules for a one-off deliverable.
- Add or expand canonical modules only when the gap is reusable across teams and should be maintained long-term.

## Execution assembly (including AI)

Combine context at execution time instead of creating new top-level canonical pages.

1. Update canonical modules first.
2. Assemble the execution deliverable from those modules in the team's normal execution workspace.
3. If using AI, point it at canonical files and constraints so it synthesizes rather than inventing new canonical positioning.
4. Feed durable learnings back through issues/PRs.

## End-to-end propagation flow (step by step)

Use this sequence after canonical files are updated in a pull request.

Anchor prompts with repository policy, not generic model defaults:

- [reference/content-governance.md](content-governance.md)
- [reference/canonical-naming.md](canonical-naming.md), [reference/banned-terms.md](banned-terms.md), [reference/brand-voice.md](brand-voice.md)
- [.cursor/rules/impact-analysis.mdc](../.cursor/rules/impact-analysis.mdc), [.cursor/rules/terminology-and-naming.mdc](../.cursor/rules/terminology-and-naming.mdc), [.cursor/rules/offering-naming.mdc](../.cursor/rules/offering-naming.mdc), [.cursor/rules/brand-voice.mdc](../.cursor/rules/brand-voice.mdc)

### Step 1: Open/update the PR

- **Automation now:** none at this step.
- **Human now:** add context, rationale, and expected downstream impact in PR body.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to draft PR narrative from the linked issue, changed files, and constraints above.
- Do not let AI invent new canonical claims; it should summarize intent and list open questions for reviewers.

</details>

### Step 2: Run PR checks

- **Automation now:** workflows run automatically on PR updates (see [AUTOMATION.md](../AUTOMATION.md) for the full map).
- **Human now:** review check output in PR comments/summary.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to summarize workflow output into a reviewer checklist, but treat CI as authoritative.
- If a check fails, use AI to propose fixes only after you confirm the underlying rule (do not "argue past" required checks).

</details>

### Step 3: Decide propagation updates

- **Automation now:** proposes impact/suggestion candidates.
- **Human now:** decide which suggested files actually need updates; reject noise; add missing files if automation missed context.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to turn suggestion output into a prioritized propagation plan: must-update vs optional vs reject-with-reason.
- Require explicit human sign-off before treating any suggestion as mandatory work.

</details>

### Step 4: Apply propagation edits and re-check

- **Automation now:** no auto-write to canonical docs in this workflow.
- **Human now:** edit related canonical files, keep claims aligned, and re-run checks by pushing updates.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to draft edits file-by-file, grounded in linked canonical sources and naming rules.
- Keep humans as authors/reviewers of the final diff; merge only after checks pass.

</details>

### Step 5: Review, merge, and ship execution outputs

- **Automation now:** blocks merge on failed required checks.
- **Human now:** reviewers approve canonical changes; requesting teams produce execution-layer outputs from updated modules.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to assemble execution-layer deliverables from updated canonical modules (talk tracks, campaign copy, regional variants), with explicit constraints and no new positioning claims.
- If execution is blocked, open an issue describing what canonical material is missing.

</details>

### Step 6: Post-merge maintenance

- **Automation now:** scheduled jobs can open maintenance artifacts (for example staleness/case-study workflows).
- **Human now:** triage maintenance items and feed durable learnings back through issues/PRs.

<details>
<summary><strong>When to use AI here (optional)</strong></summary>

- Use AI to draft maintenance issue updates or a short retro note, then convert durable changes into follow-up PRs.

</details>

Future optional split: if these toggles grow, extract each step into a dedicated how-to under `reference/` and link here.

## What is not automated today (and could be later)

- Automatic PR creation for propagation edits (currently human-owned)
- Automatic acceptance/rejection of suggestion candidates (currently human-owned)
- Automatic AI rewrite of canonical messaging (currently human-owned, with reviewer approval required)

Future automation can assist these steps, but canonical content changes should remain reviewer-controlled.
