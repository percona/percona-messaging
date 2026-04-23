# Implementation

This guide describes how to implement and operationalize this repository as an adoption program, not a one-time document drop. The work runs in parallel tracks: content architecture, governance, automation, training/change management, and rollout.

## How implementation works in practice

- Run in workstreams, not strict linear phases.
- Keep `main` canonical; use draft PRs for pre-launch staging.
- Treat change management (training, adoption, reinforcement) as a first-class track.
- Use issues to track implementation tasks and decisions, not just content updates.

## Workstream 1: Canonical content and structure

- **1.1 Directory architecture:** maintain clear directory ownership and purpose (`framework/`, `products/`, `offerings/`, `use-cases-value-pillars/`, `reference/`).
- **1.2 Decomposition routing:** keep decomposition as default behavior by updating existing modules before creating new files (see [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md)).
- **1.3 Privacy boundary:** keep private-sensitive overlays out of public canonical content.

### Workstream 1 story

- Reorganized shared value content under `use-cases-value-pillars/`.
- Tightened `README.md` repository map with explicit examples (including managed services / `ExpertOps`).
- Added decomposition routing guidance in [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md) and linked it from [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and [README.md](README.md).

## Workstream 2: Governance and ownership

- **2.1 Role clarity:** define maintainer/domain-owner/reviewer responsibilities clearly.
- **2.2 Routing authority:** keep [CODEOWNERS](CODEOWNERS) as the source of truth for reviewer routing.
- **2.3 Risk policy:** use a risk-based review model where broad claims and governance changes require explicit approval.

### Workstream 2 story

- Simplified governance principles and clarified canonical status.
- Clarified shared reviewer responsibilities across maintainers and domain owners.
- Added conduct policy linkage and enforcement/reporting expectations.
- Rebased `CODEOWNERS` to concrete path-level owners and compliance-sensitive overrides.

## Workstream 3: Automation program

- **3.1 Tool-fit design:** evaluate each automation use case first, then choose the best-fit mechanism (deterministic rule, AI-assisted check, or hybrid).
- **3.2 Failure-mode mapping:** tie each automation to a specific failure mode (naming drift, missed propagation, duplicate content, stale docs) and confirm scope is right-sized.
- **3.3 Scope reassessment:** reassess tool choice as coverage grows so each use case stays in the optimal implementation path.
- **3.4 Rollout tracking:** track automation rollout with explicit milestones and owners.

### Workstream 3 story

- Established checks and scaffolding for terminology, impact, smart suggestions, content governance gates, and staleness/case-study monitoring.
- Added support scripts and maps in [scripts/README.md](scripts/README.md), [automation/README.md](automation/README.md), and [data/README.md](data/README.md).
- Updated contribution and governance docs so automation behavior is documented where contributors look first.

### 3.5 Automation opportunity backlog (next wave)

- Add a PR label/status consistency check (for example `ready-for-launch` + `go-live:`*) so staging state is machine-readable.
- Add a CODEOWNERS coverage drift check that flags new top-level content paths without explicit ownership rules.
- Add reviewer-SLA reminders (issue or PR comment nudges) when pending approvals exceed target windows.
- Add a decomposition-completeness assistant that checks whether likely propagation targets were considered before merge.

## Workstream 4: Training and change management

- **4.1 Role-based training:** train maintainers, domain owners, frequent contributors, and occasional contributors separately.
- **4.2 Onboarding support:** provide role-based "how to contribute" examples and office-hours support during onboarding.
- **4.3 Reinforcement loop:** reinforce behavior through templates, checklists, and review comments, not one-time docs alone.

### Workstream 4 story

- Contribution flow was simplified to one common workflow in [CONTRIBUTING.md](CONTRIBUTING.md) to reduce cognitive load.
- Issue and PR template guidance was moved earlier so contributors follow it by default (see `[.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)` and `[.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)`).
- AI decomposition guidance was added so assisted contributors produce reusable outputs consistently.
- Next gap to close: formal training cadence and quickstart sessions by role.

## Workstream 5: Rollout strategy (private -> trained -> public)

- **5.1 Private setup:** stand up structure, governance, and initial automation in a controlled contributor set.
- **5.2 Training window:** train maintainers/domain owners, run pilot updates, and tune docs/templates/checks.
- **5.3 Public launch:** open repository usage broadly once contribution and review paths are stable.
- **5.4 Stabilization:** measure adoption and quality, then iterate on friction points.

### Workstream 5 story

- Repository and governance docs were built/refined first.
- Launch-staging policy was defined for pre-go-live content via draft PRs.
- Team is currently in transition between training readiness and broader operating use.

## Cross-workstream execution and control loop

These sections apply across all five workstreams and define how implementation is managed, measured, and improved over time.

### 6.1 Milestones and measurable goals

Use explicit targets and dates. Adjust values as the team finalizes commitments.

- **Contributor adoption:** `<X>` active contributors by `<date>`, with at least `<Y>` non-maintainer contributors.
- **Workflow adoption:** `<X>%` of messaging changes opened via issue + PR templates by `<date>`.
- **Review SLAs:** median time-to-first-review `<X>` business days; merge cycle time `<Y>` days by `<date>`.
- **Automation coverage:** deploy `<N>` named checks by `<date>` (terminology, impact, governance, suggestions, staleness).
- **Quality outcomes:** reduce repeat naming/propagation misses by `<X>%` by `<date>`.

#### 6.1 story

- Convert current directional goals into dated targets in a single tracking issue.
- Track contributor count, PR throughput, review latency, and check outcomes monthly.
- Define "done" for each automation so rollout is measured, not implied.

### 6.2 Issue-driven implementation plan

- Create a parent implementation epic issue.
- Create child issues for each workstream and milestone.
- Use labels for visibility (`implementation`, `training`, `automation`, `governance`, `rollout`).
- Review progress on a fixed cadence (weekly during rollout, then monthly).

### 6.3 Suggested issue backlog (starter set)

- Training plan and calendar by role (maintainers, domain owners, contributors)
- Office-hours plan and onboarding materials
- Automation rollout plan with owners and target dates
- Metrics dashboard definition (what to measure and where to report)
- First launch-cycle retrospective issue
- Deferred scope candidate: datasheet source-of-truth structure after core model stabilizes

### 6.4 Human change-management risks to plan for

- Documentation exists but behavior does not change
- Ownership ambiguity during cross-domain changes
- Contributor drop-off from template/check friction
- Over-automation before process maturity
- No reinforcement loop after initial training

### 6.5 Review cadence questions

- Are domain owners actually opening issues/PRs, or routing informally?
- Which checks catch real problems vs create noise?
- Where do contributors still need live translation from maintainers?
- What recurring training gaps show up in review comments?
- What should be simplified next release cycle?