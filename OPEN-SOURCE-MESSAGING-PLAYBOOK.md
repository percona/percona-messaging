# Open Source Messaging Playbook

## Purpose

This playbook defines operating rhythm, communication patterns, and presentation framing for how Percona manages messaging with open source practices.

Execution design and implementation details live in:

- [IMPLEMENTATION.md](IMPLEMENTATION.md) (workstreams, rollout, milestones, issue plan)
- [CONTRIBUTING.md](CONTRIBUTING.md) (day-to-day contributor workflow)
- [GOVERNANCE.md](GOVERNANCE.md) (ownership, approval model, canonical status)
- [automation/README.md](automation/README.md) and [scripts/README.md](scripts/README.md) (automation behavior)

## Executive framing

Percona treats messaging as shared infrastructure:

- Versioned source of truth in markdown
- Visible review and ownership
- Repeatable automation for quality and release safety

The result is faster updates, stronger consistency, and clearer accountability for teams and customers.

## Working order and operating cadence

### Operating loop (high level)

1. Intake requests and define canonical file targets
2. Draft or revise canonical source messaging
3. Run automation checks and complete human review
4. Merge to canonical source (`main`) at the right launch timing
5. Adapt to downstream channels and capture lessons for rule/process updates

For execution specifics (workstream sequencing, private -> trained -> public rollout), see [IMPLEMENTATION.md](IMPLEMENTATION.md).

### Recommended monthly rhythm

- Week 1: intake and priority setting
- Week 2: drafting and technical review
- Week 3: cross-functional review and approvals
- Week 4: publish, distribution, and retrospective

### Automation touchpoints in the loop

- **During drafting/review:** terminology and governance checks run via pull request workflows (see `[.github/workflows/](.github/workflows/)`).
- **During impact assessment:** impact map and suggestion logic identify likely propagation targets (see [automation/messaging-impact-map.yml](automation/messaging-impact-map.yml) and [automation/claim-types.yml](automation/claim-types.yml)).
- **During quality control:** duplicate and coverage/new-file checks guard against one-off sprawl and undiscoverable docs.
- **During maintenance:** staleness/case-study monitoring supports periodic housekeeping issues.

## Communication plan (comms)

### Internal channels

- Pull requests for change review and approval trail
- Repository issues for intake and decomposition planning
- Optional private systems for competitive/internal talk tracks

### Core communication artifacts

- Pull requests with review history and rationale
- Canonical source files in `framework/`, `offerings/`, `products/`, and `reference/`
- Workflow-generated quality feedback (terminology, impact checks, suggestions)
- Implementation and governance artifacts (`IMPLEMENTATION.md`, `GOVERNANCE.md`, `CODEOWNERS`)

## Goals and success measures

### Near-term goals

- Maintain one canonical source per messaging topic
- Reduce cross-file drift for product and offering claims
- Reduce one-off page creation through decomposition and propagation rules

### Suggested KPIs

- PR cycle time for messaging changes
- Number of impact-check misses caught before merge
- Terminology violations caught in CI
- Time from approved draft to published public update
- Reuse rate of canonical language in downstream deliverables

Target values and dated milestones should be maintained in [IMPLEMENTATION.md](IMPLEMENTATION.md) under cross-workstream goals.

## Automation opportunities to evaluate

Use these as candidates for future issues when rollout data shows clear value:

- Launch-readiness state checks (`ready-for-launch`, `go-live:`*) for draft PR coordination
- CODEOWNERS coverage drift detection for newly added path scopes
- Reviewer-SLA reminder automations for long-pending approvals
- Decomposition completeness assistant for propagation-target coverage

Track these in implementation issues under the `automation` label.

## Presentation scaffold (future talk)

Use this outline for a future presentation on why and how Percona open sourced messaging operations.

1. **Why change was needed**
  - Scattered source material, uneven quality, unclear ownership
2. **Core thesis**
  - Open source company, open source messaging operations
3. **Operating model**
  - Canonical markdown + governance + CI guardrails
4. **Repository architecture**
  - Framework, offerings, products, reference, automation, workflows
5. **Quality controls**
  - Terminology checks, impact map, new-file gate, duplicate detector, staleness report
6. **Decomposition workflow**
  - Intake, module decomposition, propagation updates, limited new-file exceptions
7. **Business value**
  - Higher trust, faster execution, clearer customer-safe communication
8. **What this means for customers**
  - More consistent messaging, fewer contradictory claims, better transparency
9. **What this means internally**
  - Better collaboration, less duplicated effort, explicit accountability
10. **Next evolution**
  - Improve suggestion precision, strengthen approver identity checks, expand external signal sync

## Action tracker template

Use this section as a running tracker each month.


| Month   | Priority                          | Owner | Status                   | Key output          | Notes                          |
| ------- | --------------------------------- | ----- | ------------------------ | ------------------- | ------------------------------ |
| YYYY-MM | Example: PostgreSQL claim refresh | Name  | Planned/In progress/Done | PR link or artifact | Risks, dependencies, follow-up |
