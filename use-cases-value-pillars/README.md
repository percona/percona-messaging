# Customer Scenarios and Value Pillars

This directory combines two closely related messaging layers:

- **Value pillars** (customer outcomes): cross-portfolio outcome narratives in the four files below
- **Use cases**: specific buyer **situations** under that outcome, listed as bullets under `### Use cases` inside a pillar file

Percona's open source identity, engineering expertise, and multi-environment support converge in a model designed for practical outcomes. The company's value proposition is reflected in four operational pillars: optimized total cost of ownership, performance and reliability at scale, comprehensive security and compliance, and adaptability for emerging workloads.

**What belongs in a use case bullet:** a named situation (requirement, workload pattern, or cost driver) plus how Percona addresses it in one or two sentences. **What does not:** repeating Solution proof, listing every offering SKU scope (see `offerings/`), or industry-vertical campaigns (see vertical messaging when that layer exists).

Do not add a new top-level pillar file for a use case. Add a bullet under the parent pillar (or open an issue if the narrative truly spans multiple pillars).

**Not the same as solution bundles:** [Expert Support, ExpertOps, and sold bundles](../offerings/solution-bundles/) describe offerings and fixed-scope packages. Pillar **use cases** are canonical scenario messaging for how an outcome shows up for buyers.

## Current files (value pillars)

- [cost-optimization.md](cost-optimization.md) (use cases: legacy and proprietary migration to open source, proprietary licensing, EOL transition, vendor consolidation, reduce cloud spend, workload tuning and rightsizing)
- [performance-reliability.md](performance-reliability.md) (use cases: business continuity, peak traffic, multi-engine Kubernetes operations, regional expansion)
- [security-sovereignty-compliance.md](security-sovereignty-compliance.md) (use cases: audit-ready, data governance, regional data residency, US extraterritorial access risk, multi-tenant isolation; sovereignty evidence table)
- [future-readiness-ai.md](future-readiness-ai.md) (use cases: RAG on PostgreSQL, vector search on Valkey)

Add new use cases when a distinct situation is not already covered by that file's Solution section. Cross-link to `offerings/solution-bundles/` when a sold package is a strong fit.
