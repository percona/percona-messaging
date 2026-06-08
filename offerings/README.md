# Offerings

This directory contains canonical messaging for commercial offerings.

## How the three offerings work together

Because Percona has no proprietary licensing business, our Expert Support, ExpertOps, and Expert Consulting and Services teams are accountable only to the customer's outcome. We advise customers on the best path for their environment, and our advice is not tied to product quotas or platform lock-in. Customers rely on Percona to support combinations of upstream technologies, Percona distributions, and supported database engines on customer-chosen infrastructure (including cloud-managed and private-cloud platforms), knowing our guidance is based on technical merit and engine-level expertise, not proprietary platform operations. This neutrality makes our guidance unusually honest.

Percona offers three complementary ways to meet customer needs across the full lifecycle of database operations.

- **Expert Support** is *reactive and advisory*: customers own execution, and Percona engineers respond when issues or questions arise.
- **ExpertOps** is *proactive and operational*: a flexible partnership where Percona engineers handle the parts of day-to-day database operations customers want support with, ranging from full operational ownership to shared workflows or targeted help with high-risk tasks.
- **Expert Consulting and Services** are *proactive and project-based*: Percona experts help teams plan and execute complex, high-impact work such as migrations, deep performance tuning, and architectural changes at the level of involvement the customer needs.

## Offering scope

Expert Support, ExpertOps, and Expert Consulting and Services are **engine-level**. Percona engineers cover supported database engines that customers run on infrastructure they choose, including on-premises datacenters, public cloud, private cloud, and Kubernetes.

Percona does not support third-party **database platform or DBaaS control planes** (for example Nutanix NDB provisioning, patching, or platform operations). When a supported engine runs on such a platform, these offerings apply to the engine workload so teams can resolve replication, performance, backup, upgrade, migration, and operational issues with upstream-level database expertise.

- **In scope:** PostgreSQL or MySQL running on Nutanix NDB, with the customer operating the engine tier.
- **Out of scope:** Nutanix NDB as a managed database platform; Percona does not replace Nutanix platform support.

When the need is a defined outcome on fixed scope with Consulting and Support packaged together, see [solution bundles](solution-bundles/messaging.md).

Per-file messaging: [expert-support.md](expert-support.md), [expertops.md](expertops.md), [expert-consulting.md](expert-consulting.md). For packaged sold bundles, use `offerings/solution-bundles/`.
