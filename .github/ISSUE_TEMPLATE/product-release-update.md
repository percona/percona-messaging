---
name: Product release update
about: Sync canonical messaging to a specific shipped product version using public release artifacts (notes, changelog, docs)
title: "[Release] "
labels: product-update
assignees: ''
---

## Use this template when

- There is a **concrete version** (or build) that **shipped or is about to ship**, and messaging should reflect **what that release contains**.
- The **primary source of truth** is **public** release notes, changelog, or versioned docs—not a positioning pivot, SKU rename, or campaign-only narrative.

## Use a different template when

- The driver is **positioning, GTM, competitive story, packaging tiers, or cross-release narrative** → open **[Messaging change or update](https://github.com/percona/percona-messaging/issues/new?template=messaging-change-update.md)** instead (you can link this release issue from there if both apply).
- You mostly need **intake / decomposition** across many modules or a **new canonical file** → use **Messaging intake and decomposition** or the relevant specialized template.

## Product and version

<!-- e.g., Percona Server for PostgreSQL 17.4, PXC 8.0.45-36 — include the exact version string consumers see. -->

## Release artifact (link)

<!-- Required: URL to release notes, changelog, or versioned docs page for this ship. -->

## What's new in this release (messaging-relevant)

<!-- Features, fixes, deprecations, or support changes that change claims, comparisons, or “what we ship” language. Omit internal-only churn. -->

## What messaging needs updating

<!-- Paths under products/, use-cases-value-pillars/, offerings/, framework/ if known; otherwise “unknown — triage”. -->

## Release date

<!-- Ship date or expected GA. -->

## Source

<!-- If anything is not in the linked artifact, summarize briefly. Do not paste private repo paths, CRM links, or customer-specific notes into GitHub; point reviewers to approved channels. -->
