# Percona for PostgreSQL: Messaging

## Percona for PostgreSQL {#percona-for-postgresql}

For organizations running PostgreSQL applications requiring performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, the Percona Distribution for PostgreSQL is a fully open source, production- and performance-tested database platform with packaged and validated extensions such as Patroni, pgAudit, and pg_stat_monitor for observability and compliance, plus pgBackRest for backup catalog management and PiTR-capable restores. Those PostgreSQL components ship together through Percona Distribution release testing so operational teams consume matched binaries instead of assembling tooling ad hoc.

The distribution also includes the pg_tde extension for transparent data-at-rest encryption and integrates with external key management systems like Hashicorp Vault, Thales CipherTrust, Fortanix SDKMS, Open Bao, and Akeyless. Together with Percona Monitoring and Management (PMM) and the Percona Operator for PostgreSQL, organizations gain consistent visibility and automation across hybrid and Kubernetes-based environments.

Unlike license-restricted PostgreSQL offerings and proprietary DBaaS services, Percona provides enterprise-grade resilience and tooling without license restrictions, vendor-specific APIs, or feature gating, backed by 24x7 global support.

### Customer Challenges and Value Alignment: PostgreSQL

**Optimized TCO**

- Open source without compromise: The Percona Distribution for PostgreSQL consolidates trusted community components into one enterprise-validated package, eliminating the cost and complexity of proprietary add-ons. Türk Telekom eliminated licensing costs, cut query times substantially, and boosted customer satisfaction by delivering high availability and resilience across critical services with Percona Distribution for PostgreSQL.
- Open source Kubernetes automation: Percona Operator for PostgreSQL is a hard fork of Crunchy PGO with Percona-owned development and community-driven evolution, extending the same inspectable PostgreSQL stack to Kubernetes without a vendor-tied operator control plane. On upgrade, upstream Crunchy resources migrate automatically to the `upstream.pgv2.percona.com` API group so Percona and Crunchy operators can coexist during adoption and teams can move without re-architecting clusters. [Migration from Crunchy PGO](https://docs.percona.com/percona-operator-for-postgresql/3.0.0/migrate-from-crunchy.html)
- Migration clarity when PostgreSQL licensing or managed-service roadmaps change: Vendor bundles and subscription models evolve on timelines teams do not control. Percona publishes positioning on portable PostgreSQL software versus proprietary distributions and managed PostgreSQL stacks ([Percona Software for PostgreSQL](https://www.percona.com/postgresql/software)), which helps organizations compare options on cleared public materials and plan moves without proprietary APIs that trap operational state.
- Legacy RDBMS exit to PostgreSQL for TCO: Teams exiting proprietary or legacy RDBMS footprints can reduce license and support spend by landing on Percona Distribution for PostgreSQL with assessment-led migration through [Percona Expert Consulting and Services](https://www.percona.com/services/consulting). Scope and source-to-target patterns are confirmed during assessment.

**Performance and Reliability at Scale**

- High-availability and disaster recovery made simple: The Percona Distribution for PostgreSQL bundles Patroni and pgBackRest together: Patroni automates failover for high availability and coordinates switchovers for maintenance tasks; pgBackRest provides backup catalog management and Point-in-Time Recovery (PiTR) for granular restores when data must be recovered from backup, on the same validated PostgreSQL stack organizations deploy for HA. Distribution releases keep Patroni HA automation release-tested through upgrade cadence, including coordination-layer maintenance summarized in the [Patroni 4.1.2 update for Percona Distribution for PostgreSQL](https://docs.percona.com/new/2026/04/24/patroni-412-update-for-percona-distribution-for-postgresql/). Automated failover minimises recovery time, avoiding the revenue impact of downtime.
- Built-in replication lag monitoring: PostgreSQL provides native, accurate replication lag tracking through `pg_stat_wal_receiver` and WAL LSN comparison, without requiring external heartbeat tooling. PMM surfaces this data via the `pg_custom_stat_wal_receiver_lag_bytes` metric (sourced from `postgres_exporter`). Teams migrating from MySQL (where external tools like pt-heartbeat are common for lag measurement) gain this capability out of the box with PostgreSQL.

**Security, Sovereignty, and Compliance**

- End-to-end encryption and governance: Percona integrates pg_tde for transparent data-at-rest encryption, and supports LDAP, Kerberos and TLS for centralized authentication. pgAudit and Percona's documented CVE process strengthen auditability for GDPR, HIPAA, and PCI-DSS frameworks.
- Validated open source integrity: Every build is open for audit and inspection, ensuring compliance without dependence on opaque vendor frameworks.

**Adaptability for Emerging Workloads**

- Cloud-native operations: Percona Operator for PostgreSQL automates deployment, scaling, and failover in Kubernetes with the same open source, Percona-owned operator model as the distribution stack, delivering consistent governance and portability across any cloud.
- AI and analytics readiness: Teams run embeddings and vector search on PostgreSQL using pgvector packaged with other tested distribution components ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)), avoiding a separate AI-only datastore for many workloads. Optional extensions beyond that validated set, including pgvectorscale when packaged for a given distribution release, appear in Percona distribution documentation and release notes ([release notes](https://docs.percona.com/postgresql/latest/release-notes/release-notes.html)), which ties sizing and performance conversations to binaries customers deploy rather than benchmark scenarios that omit packaging constraints.
