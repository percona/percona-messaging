# Prose and Links Validation Workflow (#14)

This workflow defines a lightweight quality gate for prose and links. It is designed for fast review, clear ownership, and consistent release decisions.

## Purpose

- Keep customer-facing messaging accurate, clear, and aligned with approved naming and licensing language.
- Catch high-risk prose and link defects before publish or release.
- Create a repeatable manual sign-off process with low overhead.

## Ownership

- Current DRI: Messaging lead (current assignee)
- Current backup: Content lead backup (Cindy)
- Long-term ownership model: Solutions Marketing role

## Decision Authority

- Content wording and messaging decisions: DRI or backup
- Technical accuracy decisions: Product Managers or BU Leads
- Mixed-risk issues (technical + messaging): joint sign-off between content owner and PM or BU lead

## Review SLA

- Target turnaround: 48 business hours
- Maximum turnaround: 72 business hours

## Tier Definitions and Cadence

### Tier 1 (highest risk, full monthly review)

- Product pages
- External naming and positioning content
- Compliance claims
- open source licensing claims and license statements
- Competitor comparison claims

### Tier 2 (monthly sampled review)

- Other customer-facing messaging assets not covered by Tier 1
- Sampling rate: 25 percent each monthly cycle

### Tier 3 (quarterly sampled review)

- Lower-risk internal or reference messaging content

## Inclusion Rule for Changed Content

Any recently changed Tier 2 or Tier 3 page is auto-included in the next review cycle, in addition to standard sampling.

## Severity Model and Release Impact

### P0 (hard block release or publish)

- Non-compliant or legally risky claims
- Incorrect license statements (including open source or source available mislabeling)
- Incorrect competitor claims
- Naming violations against approved canonical naming
- Broken critical links on key customer-facing or product pages

### P1 (must fix quickly, not always hard block)

- Potentially misleading prose without legal or compliance risk
- Broken non-critical links
- Major clarity defects that may confuse customer understanding

### P2 (non-blocking)

- Tone and style polish
- Minor wording improvements
- Low-impact cleanup

## Emergency Waiver Path

Waivers are allowed for urgent release needs.

Required waiver fields:

- Reason for waiver
- Scoped risk statement
- Owner for follow-up fix
- Target fix due date

Approval authority:

- DRI or backup

## Reviewer Checklist

Use this checklist for each page in scope.

- Naming follows canonical naming rules in `reference/canonical-naming.md`
- Terminology follows repository constraints in `reference/banned-terms.md`
- License language is accurate (open source vs source available)
- No unsupported or unverifiable competitor claims
- Compliance-sensitive wording is accurate and current
- Links resolve correctly and point to intended destinations
- No staging, internal, or placeholder links remain
- Product value statements are clear and not misleading
- Tone is consistent with `reference/brand-voice.md`
- Findings are tagged as P0, P1, or P2

## Sign-Off Template (Monthly Cycle)

Copy and fill:

```text
Validation Cycle: YYYY-MM (Monthly)
Reviewer(s):
DRI:
Backup:
Review Window:

Scope
- Tier 1 pages reviewed: [count]
- Tier 2 sampled pages reviewed (25%): [count]
- Auto-included changed pages from Tier 2 or Tier 3: [count]

Findings
- P0: [count] | Notes:
- P1: [count] | Notes:
- P2: [count] | Notes:

Decision
- Go / No-Go:
- Blocking reasons (if No-Go):

Waivers (if any)
- Approved by:
- Reason:
- Risk statement:
- Fix owner:
- Fix due date:

Follow-up Actions
- [action, owner, due date]
```

## Sign-Off Template (Quarterly Cycle)

Copy and fill:

```text
Validation Cycle: YYYY-Q# (Quarterly)
Reviewer(s):
DRI:
Backup:
Review Window:

Scope
- Tier 1 pages reviewed across quarter: [count]
- Tier 2 monthly sampling completed: [yes/no]
- Tier 3 sampled pages reviewed: [count]
- Auto-included changed pages from Tier 2 or Tier 3: [count]

Findings Summary
- P0 total:
- P1 total:
- P2 total:
- Recurring issue patterns:

Decision
- Quarter sign-off status: Complete / Partial / Blocked
- Outstanding blockers:

Waivers (if any)
- Approved by:
- Reason:
- Risk statement:
- Fix owner:
- Fix due date:

Process Improvements for Next Quarter
- [improvement, owner, due date]
```

## Operating Notes

- Keep this workflow manual-first unless recurring defect patterns justify automation.
- If repeated link failures persist, propose targeted CI link checking.
- If repeated naming or terminology drift persists, propose lint or review guardrails.
