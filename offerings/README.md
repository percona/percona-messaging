# Offerings

This directory contains canonical messaging for commercial offerings. Each offering has its own subdirectory; use **`messaging.md`** for positioning and buyer-facing language.

## How offerings work together

Because Percona has no proprietary licensing business, our Expert Support, ExpertOps, and Expert Consulting and Services teams are accountable only to the customer's outcome. We advise customers on the best path for their environment, and our advice is not tied to product quotas or platform lock-in. Customers rely on Percona to support combinations of upstream technologies, Percona distributions, and supported database engines on customer-chosen infrastructure (including cloud-managed and private-cloud platforms), knowing our guidance is based on technical merit and engine-level expertise, not proprietary platform operations. This neutrality makes our guidance unusually honest.

Percona offers complementary ways to meet customer needs across the full lifecycle of database operations.

- **[Expert Support](expert-support/messaging.md)** is *reactive and advisory*: customers own execution, and Percona engineers respond when issues or questions arise.
- **[ExpertOps](expertops/messaging.md)** is *proactive and operational*: a flexible partnership where Percona engineers handle the parts of day-to-day database operations customers want support with, ranging from full operational ownership to shared workflows or targeted help with high-risk tasks.
- **[Expert Consulting and Services](expert-consulting/messaging.md)** are *proactive and project-based*: Percona experts help teams plan and execute complex, high-impact work such as architecture decisions, deep performance tuning, and scoped project delivery at the level of involvement the customer needs. The fixed-fee SKUs listed there (Health Audit, Architecture and Design, Performance Tuning, PMM QuickStart, Security Assessment) are a **subset** of Consulting, not the full catalog; work outside those gates is custom-scoped.
- **[Migration and Modernization](migration-program/messaging.md)** is the capability home for legacy exit and modernization programs. For proprietary exits such as Oracle to PostgreSQL, Percona partners with HexaCluster in one offer. Customers contract with Percona for the full engagement; a migration software license is part of that engagement when the path uses migration tooling. The packaged migration engagements nested there are likewise a **subset** of what the program can cover.

## Which offering?

The main fork is **who runs day-to-day database operations**:

- **Your team executes**: [Expert Support](expert-support/messaging.md): Percona guides; you operate production.
- **Percona executes in your environment**: [ExpertOps](expertops/messaging.md): hands-on operational partnership.

Add **[Expert Consulting and Services](expert-consulting/messaging.md)** for bounded projects (architecture, deep tuning, scoped delivery) alongside either steady-state offering. When the buyer need is **legacy exit or modernization to open source**, use **[Migration and Modernization](migration-program/messaging.md)**. **[Solution bundles](solution-bundles/messaging.md)** package Consulting + Support for known buyer moments when fixed scope fits; they are not ExpertOps subscriptions.

Percona also offers **database training** as a complementary service. Training builds in-house skill; it is not a substitute for ExpertOps operational coverage or Expert Support for production incidents.

## Offering scope

Expert Support, ExpertOps, and Expert Consulting and Services are **engine-level**. Percona engineers cover supported database engines that customers run on infrastructure they choose, including on-premises datacenters, public cloud, private cloud, and Kubernetes.

Percona does not support third-party **database platform or DBaaS control planes** (for example Nutanix NDB provisioning, patching, or platform operations). When a supported engine runs on such a platform, these offerings apply to the engine workload so teams can resolve replication, performance, backup, upgrade, migration, and operational issues with upstream-level database expertise.

- **In scope:** PostgreSQL or MySQL running on Nutanix NDB, with the customer operating the engine tier.
- **Out of scope:** Nutanix NDB as a managed database platform; Percona does not replace Nutanix platform support.

When the need is a defined outcome on fixed scope with Consulting and Support packaged together, see [solution bundles](solution-bundles/messaging.md).

## Directory layout

| Path | Purpose |
| --- | --- |
| [expert-support/messaging.md](expert-support/messaging.md) | Expert Support positioning |
| [expertops/messaging.md](expertops/messaging.md) | ExpertOps positioning |
| [expert-consulting/messaging.md](expert-consulting/messaging.md) | Expert Consulting and Services positioning |
| [expert-consulting/health-audit.md](expert-consulting/health-audit.md) | Fixed-fee Health Audit (CONS-HAFF) |
| [expert-consulting/architecture-and-design.md](expert-consulting/architecture-and-design.md) | Fixed-fee Architecture and Design (CONS-AD) |
| [expert-consulting/performance-tuning.md](expert-consulting/performance-tuning.md) | Fixed-fee Performance Tuning (CONS-PTFF) |
| [expert-consulting/database-monitoring-quickstart.md](expert-consulting/database-monitoring-quickstart.md) | Fixed-fee Database Monitoring QuickStart (CONS-PMM) |
| [expert-consulting/security-assessment.md](expert-consulting/security-assessment.md) | Fixed-fee Security Assessment (CONS-SECFF) |
| [migration-program/messaging.md](migration-program/messaging.md) | Migration and Modernization; Percona + HexaCluster for proprietary exits; Percona-wrapped contracting |
| [migration-program/database-migrations.md](migration-program/database-migrations.md) | Homogeneous / platform Database Migrations (CONS-MIG) |
| [migration-program/proprietary-to-postgresql.md](migration-program/proprietary-to-postgresql.md) | Proprietary → PostgreSQL assessment (DMAT) |
| [migration-program/mysql-galera-cluster-migration.md](migration-program/mysql-galera-cluster-migration.md) | MySQL Galera Cluster → Percona XtraDB Cluster migration |
| [solution-bundles/messaging.md](solution-bundles/messaging.md) | Packaged Consulting + Support bundles |

Fixed-fee Consulting scopes live under `expert-consulting/`. Migration cutover and proprietary-exit assessment scopes nest under `migration-program/`, not as peer Consulting SKUs.

Engine-specific Support or Consulting scope (extensions, compatibility boundaries, advisory add-ons) belongs under `products/{engine}/`, not in offering files here. Offering files describe how Support, ExpertOps, and Consulting work across all supported engines.


