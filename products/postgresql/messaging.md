# Percona for PostgreSQL: Messaging

## Percona for PostgreSQL {#percona-for-postgresql}

For organizations running PostgreSQL applications requiring performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, the Percona Distribution for PostgreSQL is a fully open source, production- and performance-tested database platform with packaged and validated extensions such as pgBackRest, Patroni, pgAudit, pg_stat_monitor, PostGIS, and pgvector for observability, geospatial, and embedding workloads.

The distribution also includes the pg_tde extension for transparent data-at-rest encryption and integrates with external key management systems like Hashicorp Vault, Thales CipherTrust, Fortanix SDKMS, Open Bao, and Akeyless. Together with Percona Monitoring and Management (PMM) and the Percona Operator for PostgreSQL, organizations gain consistent visibility and automation across hybrid and Kubernetes-based environments.

Unlike license-restricted PostgreSQL offerings and proprietary DBaaS services, Percona provides enterprise-grade resilience and tooling without license restrictions, vendor-specific APIs, or feature gating, backed by 24×7 Expert Support and optional ExpertOps.

### Customer Challenges and Value Alignment: PostgreSQL

**Optimized TCO**

- Open source without compromise: The Percona Distribution for PostgreSQL consolidates trusted community components into one enterprise-validated package, eliminating the cost and complexity of proprietary add-ons. Türk Telekom eliminated licensing costs, cut query times substantially, and boosted customer satisfaction by delivering high availability and resilience across critical services with Percona Distribution for PostgreSQL.
- Migration clarity when PostgreSQL licensing or managed-service roadmaps change: Vendor bundles and subscription models evolve on timelines teams do not control. Percona publishes positioning on portable PostgreSQL software versus proprietary distributions and managed PostgreSQL stacks ([Percona Software for PostgreSQL](https://www.percona.com/postgresql/software)), which helps organizations compare options on cleared public materials and plan moves without proprietary APIs that trap operational state.

**Performance and Reliability at Scale**

- High-availability and disaster recovery made simple: The Percona Distribution for PostgreSQL includes Patroni to automate the management of failover for high availability and coordinate switchovers for maintenance tasks. Reference patterns and implementation guidance are in [High availability for PostgreSQL](https://www.percona.com/ha-for-postgresql). Distribution releases keep Patroni HA automation release-tested through upgrade cadence, including coordination-layer maintenance summarized in the [Patroni 4.1.2 update for Percona Distribution for PostgreSQL](https://docs.percona.com/new/2026/04/24/patroni-412-update-for-percona-distribution-for-postgresql/). Automated failover minimises recovery time, avoiding the revenue impact of downtime. For higher impact events, when data needs to be recovered from backup, pgBackRest provides backup catalog management and Point-in-Time Recovery (PiTR) for reliable, specific disaster recovery.
- Built-in replication lag monitoring: PostgreSQL provides native, accurate replication lag tracking through `pg_stat_wal_receiver` and WAL LSN comparison, without requiring external heartbeat tooling. PMM surfaces this data via the `pg_custom_stat_wal_receiver_lag_bytes` metric (sourced from `postgres_exporter`). Teams migrating from MySQL (where external tools like pt-heartbeat are common for lag measurement) gain this capability out of the box with PostgreSQL.
- Horizontal scale and legacy tooling: Expert Support and consulting cover Citus sharding and coordination with Patroni HA on customer deployments; confirm whether Citus is in the distribution build for a given release against [third-party components](https://docs.percona.com/postgresql/18/third-party.html) before stating it is packaged. Advisory Expert Support is also available for estates that still run barman or repmgr alongside PostgreSQL where migration to pgBackRest and Patroni is phased.

**Security, Sovereignty, and Compliance**

- End-to-end encryption and governance: Percona integrates pg_tde for transparent data-at-rest encryption with database-level TDE (not storage-only encryption alone), and supports LDAP, Kerberos and TLS for centralized authentication. pgAudit and Percona's documented CVE process strengthen auditability for GDPR, HIPAA, and PCI-DSS frameworks. Current constraints and KMS options are documented in [pg_tde release notes](https://docs.percona.com/postgresql/latest/).
- Validated open source integrity: Every build is open for audit and inspection, ensuring compliance without dependence on opaque vendor frameworks.

**Adaptability for Emerging Workloads**

- Cloud-native operations: The Percona Operator for PostgreSQL automates deployment, scaling, and failover in Kubernetes environments, delivering consistent governance and portability across any cloud.
- AI and analytics readiness: Teams run embeddings and vector search on PostgreSQL using pgvector packaged with other tested distribution components ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)), avoiding a separate AI-only datastore for many workloads. Optional extensions beyond that validated set, including pgvectorscale when packaged for a given distribution release, appear in Percona distribution documentation and release notes ([release notes](https://docs.percona.com/postgresql/latest/release-notes/release-notes.html)), which ties sizing and performance conversations to binaries customers deploy rather than benchmark scenarios that omit packaging constraints.
- Geospatial workloads: PostGIS ships as a validated third-party component; Expert Support and consulting cover coordinated PostgreSQL and PostGIS upgrades, dependency checks, and spatial workload regression planning ([PostGIS deployment](https://docs.percona.com/postgresql/17/solutions/postgis-deploy.html)).
- Time-series on PostgreSQL: Expert Support and consulting cover timescale (Apache 2.0, installed separately; not packaged in Percona Distribution for PostgreSQL) alongside core PostgreSQL for hybrid estates that combine relational and time-series workloads.
