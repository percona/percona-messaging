# Open Source Messaging Playbook

## Purpose

This playbook is the single narrative for how Percona runs messaging as an adoption program with open source practices: operating rhythm, **automation** (deterministic checks plus AI-assisted or hybrid steps), program delivery (workstreams and what we shipped), stakeholder communication, and **measurement suggestions woven through**—with pointers to day-to-day contributor material below.

Contributor workflow, ownership rules, and automation behavior also live in:

- [CONTRIBUTING.md](CONTRIBUTING.md) (day-to-day contributor workflow)
- [GOVERNANCE.md](GOVERNANCE.md) (ownership, approval model, canonical status)
- [automation/README.md](automation/README.md) and [scripts/README.md](scripts/README.md) (automation behavior)

## Executive framing

Percona treats messaging as shared infrastructure:

- Versioned source of truth in markdown
- Visible review and ownership
- Repeatable automation for quality and release safety

The result is faster updates, stronger consistency, and clearer accountability for teams and customers.

### Why automation is central here

This program pays off disproportionately when **automation carries recurring judgment**—naming and governance gates, impact and propagation hints, staleness signals—so humans spend review time on substance, not re-deriving the same checks each PR. The stack mixes **deterministic rules** (predictable, easy to own) with **AI-assisted or hybrid steps** where fuzzy matching or suggestions help without replacing approval.

That combination is also **portable learning for other teams**: the workflows, maps in `automation/`, and how we scope “rule vs model vs hybrid” are a concrete reference for standing up **good automation with AI** elsewhere—same pattern of start from failure mode, keep scope honest, measure signal versus noise. Details live in [automation/README.md](automation/README.md), [scripts/README.md](scripts/README.md), and [.github/workflows/](.github/workflows/).

**Worth measuring early:** how often automation fires on real problems versus noise; time from open PR to first meaningful signal from checks; and whether reviewers still feel they have to re-do work the bots already covered.

## Working order and operating cadence

### Operating loop (high level)

A typical pass through the work looks like this (order flexes by change size):

1. Intake requests and define canonical file targets
2. Draft or revise canonical source messaging
3. Run automation checks and complete human review
4. Merge to canonical source (`main`) at the right launch timing
5. Adapt to downstream channels and capture lessons for rule/process updates

That loop sits alongside the program delivery workstreams below (structure, governance, automation, training, rollout). Rollout phasing is described there so intent and delivery stay one story.

**Worth measuring as you go:** PR cycle time end to end; how much of that time sits in review versus drafting; template or issue usage when changes start; and whether merges cluster right before launches (a sign staging or comms timing may need tuning).

### Cadence across a month (still defining)

We have **not** locked a calendar template—this sketch is only a placeholder while the team figures out what rhythm fits load and review capacity:

- Intake and priority setting clustered early in a cycle
- Drafting and technical review in the middle
- Cross-functional review and approvals before merge pressure
- Publish, distribution, and retrospective when it matches launch reality

Revisit once you have a few months of throughput data (volume of PRs, reviewer load, how often automation catches issues pre-merge).

### Automation touchpoints in the loop

- **During drafting/review:** terminology and governance checks run via pull request workflows (see `[.github/workflows/](.github/workflows/)`).
- **During impact assessment:** impact map and suggestion logic surface **rule-backed** propagation hints (see [automation/messaging-impact-map.yml](automation/messaging-impact-map.yml) and [automation/claim-types.yml](automation/claim-types.yml)). They complement, but do not replace, structured decomposition in [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md).
- **During quality control:** new-file and doc coverage checks guard against one-off sprawl and undiscoverable docs.
- **During maintenance:** staleness and case study maintenance reminders support periodic housekeeping issues.

**Worth measuring as you go:** per-check or per-category **true positive rate** (did it catch a real miss?); **false positive burden** (how often contributors dismiss or work around a check); and **coverage** (what share of merged messaging PRs touched paths the impact map cares about). Those three tell you whether to tighten rules, widen training, or adjust AI scope for other teams copying the model.

## Program delivery and workstreams

This repository is operationalized as an adoption program, not a one-time document drop. The work runs in parallel tracks: content architecture, governance, automation, training and change management, and rollout.

### How the program runs in practice

The program has tended to run with these defaults (they can flex):

- Workstreams in parallel rather than strict linear phases.
- `main` stays canonical; pre-go-live content is staged in draft PRs where that helps.
- Change management (training, adoption, reinforcement) treated as its own track, not an afterthought.
- Issues used for program tasks and decisions as well as content updates.

**Worth measuring as you go:** ratio of program or intake issues to drive-by DMs or email-only asks (a rough proxy for whether routing is landing in the repo); and whether workstream-level issues stay current or go stale (signal for check-in frequency).

### Workstream 1: Canonical content and structure

- **1.1 Directory architecture:** clear ownership and purpose per top-level area (`framework/`, `products/`, `offerings/`, `use-cases-value-pillars/`, `reference/`).
- **1.2 Decomposition routing:** default is updating existing modules before adding files; detail in [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md).
- **1.3 Privacy boundary:** private-sensitive overlays do not belong in public canonical content.

#### Workstream 1 story

- Reorganized shared value content under `use-cases-value-pillars/`.
- Tightened `README.md` repository map with explicit examples (including managed services / `ExpertOps`).
- Added decomposition routing guidance in [reference/decomposition-and-propagation.md](reference/decomposition-and-propagation.md) and linked it from [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and [README.md](README.md).

**Worth measuring as you go:** new-file versus update-existing ratio (sprawl signal); and how often decomposition guidance gets cited in PR discussion (adoption of the default path).

### Workstream 2: Governance and ownership

- **2.1 Role clarity:** maintainer, domain-owner, and reviewer responsibilities are explicit enough to route real changes.
- **2.2 Routing authority:** in this repo, [CODEOWNERS](CODEOWNERS) is the reviewer routing source of truth.
- **2.3 Risk policy:** broader claims and governance changes skew toward explicit review; exact bar lives in [GOVERNANCE.md](GOVERNANCE.md).

#### Workstream 2 story

- Simplified governance principles and clarified canonical status.
- Clarified shared reviewer responsibilities across maintainers and domain owners.
- Added conduct policy linkage and enforcement and reporting expectations.
- Rebased `CODEOWNERS` to concrete path-level owners and compliance-sensitive overrides.

**Worth measuring as you go:** median time to first review and to approval; how often the right owners from `CODEOWNERS` actually engage versus escalation; and informal routing (chat or email) as a share of total change volume—behavior change shows up there.

### Workstream 3: Automation program

- **3.1 Tool-fit design:** start from the use case, then pick a mechanism (deterministic rule, AI-assisted check, or hybrid).
- **3.2 Failure-mode mapping:** each automation maps to a failure mode the team cares about (for example naming drift, missed propagation, stale docs), with scope sized to match maturity.
- **3.3 Scope reassessment:** as coverage grows, it is reasonable to revisit whether a rule, hybrid, or other approach still fits.
- **3.4 Rollout tracking:** milestones and owners for automation land wherever the program tracks execution (often issues).

#### Workstream 3 story

- Established checks and scaffolding for terminology, impact, smart suggestions, content governance gates, staleness reporting, and case study maintenance reminders.
- Added support scripts and maps in [scripts/README.md](scripts/README.md), [automation/README.md](automation/README.md), and [data/README.md](data/README.md).
- Updated contribution and governance docs so automation behavior is documented where contributors look first.

**Worth measuring as you go:** incidents caught in CI that would have shipped without it; contributor sentiment on noisy checks; and **reuse**—whether other repos or teams lifted patterns (workflow shape, claim maps, hybrid design) with fewer support threads. That last one is the outward signal that “good automation with AI” is enabling others, not only this codebase.

### Workstream 4: Training and change management

- **4.1 Role-based training:** different roles (maintainers, domain owners, frequent vs occasional contributors) often need different depth; same deck rarely fits all.
- **4.2 Onboarding support:** role-based contribution examples and optional office hours reduce friction early.
- **4.3 Reinforcement loop:** templates, checklists, and review habits carry more load over time than a single training deck.

#### Workstream 4 story

- Contribution flow was simplified to one common workflow in [CONTRIBUTING.md](CONTRIBUTING.md) to reduce cognitive load.
- Issue and PR template guidance was moved earlier so contributors follow it by default (see `[.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)` and `[.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)`).
- AI decomposition guidance was added so assisted contributors produce reusable outputs consistently.
- Next gap to close: formal training cadence and quickstart sessions by role.

**Worth measuring as you go:** template completion rate or equivalent; repeat questions in office hours or Slack (training gap signal); and post-training PR quality (fewer round-trips for the same class of mistake).

### Workstream 5: Rollout strategy (private → trained → public)

- **5.1 Private setup:** structure, governance, and initial automation with a smaller contributor set first.
- **5.2 Training window:** pilots with maintainers and domain owners; docs, templates, and checks tuned from real changes.
- **5.3 Public launch:** broader usage when contribution and review paths feel stable enough for the risk you accept.
- **5.4 Stabilization:** adoption and quality inform what to simplify or harden next.

#### Workstream 5 story

- Repository and governance docs were built and refined first.
- Launch-staging policy was defined for pre-go-live content via draft PRs.
- Team is currently in transition between training readiness and broader operating use.

**Worth measuring as you go:** active contributors by cohort (maintainer vs domain vs other); PRs opened from outside the original pilot group; and stabilization metrics after broaden—revert rate, hotfix PRs, or “urgent” merges (stress on the model).

## Stakeholder communication (comms)

A useful principle: communicate as early as is responsible, rather than waiting until everything feels polished. Much of the program is behavior change over time (pull requests, [CODEOWNERS](CODEOWNERS), fewer ad hoc approval threads). People who will need to work differently are often the same people whose early reactions improve the rollout.

### Concrete anchors alongside the story

When explaining what "open sourcing product messaging" means, it helps if people can open something specific—not only a headline. Examples others can copy or adapt:

- This repository (canonical source and review surface)
- A go-live program board (where the program is sequenced and visible), where you use one
- A roll-up issue (ownership, routing, child work)

That kind of pairing tends to surface better feedback before habits harden.

### Outreach shape

Patterns that have worked alongside the repo:

- A broad FYI so the default is not a surprise.
- Unit calendar conversations where existing meetings already pull the right owners together.
- Targeted Slack where that reaches people who are not on a unit thread or where async fits better.

### In-repo and review channels

- Pull requests for change review and an approval trail
- Repository issues for intake and decomposition planning
- Optional private systems for competitive or internal talk tracks

### Core communication artifacts

- Pull requests with review history and rationale
- Canonical source files in `framework/`, `offerings/`, `products/`, and `reference/`
- Workflow-generated quality feedback (terminology, impact checks, suggestions)
- Governance and routing artifacts ([GOVERNANCE.md](GOVERNANCE.md), [CODEOWNERS](CODEOWNERS))

**Worth measuring as you go:** after a comms beat, did traffic to the repo and roll-up issue spike usefully? Did review threads move in-repo versus staying in chat? Qualitative pulse from the stakeholders who most need to change behavior is as important as counts.

## Cross-workstream execution and control loop

Ideas that span workstreams: how the program gets managed, measured, and revisited over time. The **“Worth measuring as you go”** notes earlier are the running list of signals; the subsection below pulls some of those into placeholder targets when you are ready to commit numbers.

### Milestones and measurable goals

Explicit targets and dates make tradeoffs visible; adjust placeholders as commitments firm up. They should line up with the signals you already started tracking above (automation quality, review latency, adoption breadth, comms follow-through).

- **Contributor adoption:** `<X>` active contributors by `<date>`, with at least `<Y>` non-maintainer contributors.
- **Workflow adoption:** `<X>%` of messaging changes opened via issue and PR templates by `<date>`.
- **Review SLAs:** median time-to-first-review `<X>` business days; merge cycle time `<Y>` days by `<date>`.
- **Automation coverage:** deploy `<N>` named checks by `<date>` (terminology, impact, governance, suggestions, staleness).
- **Quality outcomes:** reduce repeat naming and propagation misses by `<X>%` by `<date>`.

Dated targets and current numbers usually live in a parent program tracking issue (and optionally the action tracker table at the end of this playbook) so prose here does not silently go stale.

#### Milestones story

- Directional goals often become dated targets in one tracking issue.
- Contributor count, PR throughput, review latency, and check outcomes are worth revisiting on a rhythm the team agrees on.
- Clear "done" criteria per automation make rollout easier to discuss than when completion is implied.

### Issue-driven program plan

A structure many programs use (adapt labels and cadence to your org):

- A parent epic (or equivalent) for the program, with child issues for workstreams or milestones.
- Labels for visibility (`implementation`, `training`, `automation`, `governance`, `rollout`) or whatever set you standardize on.
- A recurring check-in whose frequency matches intensity—for example, weekly while rollout is hot, then monthly.

### Suggested issue backlog (starter set)

- Training plan and calendar by role (maintainers, domain owners, contributors)
- Office-hours plan and onboarding materials
- Automation rollout plan with owners and target dates
- Metrics dashboard definition (what to measure and where to report)
- First launch-cycle retrospective issue
- Deferred scope candidate: datasheet source-of-truth structure after core model stabilizes

### Human change-management risks (worth naming)

- Documentation exists but behavior does not change
- Ownership ambiguity during cross-domain changes
- Contributor drop-off from template or check friction
- Over-automation before process maturity
- No reinforcement loop after initial training

### Review cadence questions

- Are domain owners actually opening issues and PRs, or routing informally?
- Which checks catch real problems versus create noise?
- Where do contributors still need live translation from maintainers?
- What recurring training gaps show up in review comments?
- What should be simplified next release cycle?

## Goals and success measures (consolidated)

Earlier sections already suggest **what to watch as you go** (automation signal versus noise, review and routing behavior, structure and sprawl, training gaps, rollout breadth, comms effectiveness). This block gathers **directional goals** and **example KPIs** in one place for quarterly or program-level planning—not as a fixed scorecard.

### Near-term goals

- One canonical source per messaging topic where it matters most
- Less cross-file drift on product and offering claims
- Less one-off page creation when decomposition and propagation rules are followed

### Example KPIs (pick what matches your signals)

- PR cycle time for messaging changes
- Impact-check or propagation misses caught before merge (and misses that still shipped—learn from both)
- Terminology or governance violations caught in CI versus in human review only
- Time from approved draft to published public update
- Reuse of canonical language in downstream deliverables (sampling is fine early on)
- **Automation-specific:** true positive / false positive trends per check; optional “hours saved” proxy if you lightweight a short contributor survey after a quarter

## Automation opportunities and backlog

### Candidates to evaluate when rollout data supports them

- Launch-readiness state checks (`ready-for-launch`, `go-live:`*) for draft PR coordination
- CODEOWNERS coverage drift detection for newly added path scopes
- Reviewer-SLA reminder automations for long-pending approvals
- Decomposition completeness assistant for propagation-target coverage

### Next wave (build backlog)

- Add a PR label and status consistency check (for example `ready-for-launch` plus `go-live:`*) so staging state is machine-readable.
- Add reviewer-SLA reminders (issue or PR comment nudges) when pending approvals exceed target windows.
- Add a decomposition-completeness assistant that checks whether likely propagation targets were considered before merge.

These items are usually tracked as issues (for example under the `automation` label) when you decide to fund them.

## Action tracker template

Optional: use this table as a lightweight monthly tracker if it helps your team.

| Month   | Priority                          | Owner | Status                   | Key output          | Notes                          |
| ------- | --------------------------------- | ----- | ------------------------ | ------------------- | ------------------------------ |
| YYYY-MM | Example: PostgreSQL claim refresh | Name  | Planned/In progress/Done | PR link or artifact | Risks, dependencies, follow-up |
