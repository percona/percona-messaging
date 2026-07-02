# Percona for PostgreSQL: Messaging

## Percona for PostgreSQL {#percona-for-postgresql}

For organizations running PostgreSQL applications requiring performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, the Percona Distribution for PostgreSQL is a fully open source, production- and performance-tested database platform with packaged and validated extensions such as Patroni for HA, pgBackRest for backup catalog management and PiTR-capable restores, pgAudit and pg_stat_monitor for compliance and observability, PostGIS for geospatial workloads, and pgvector for vector search and embedding workloads. Those PostgreSQL components ship together through Percona Distribution release testing so operational teams consume matched binaries instead of assembling tooling ad hoc.

The distribution also includes the pg_tde extension for transparent data-at-rest and WAL encryption and integrates with external key management systems like HashiCorp Vault, Thales CipherTrust, Fortanix SDKMS, Open Bao, and Akeyless. Together with Percona Monitoring and Management (PMM) and the Percona Operator for PostgreSQL, organizations gain consistent visibility and automation across hybrid and Kubernetes-based environments.

Unlike license-restricted PostgreSQL offerings and proprietary DBaaS services, Percona provides enterprise-grade resilience and tooling without license restrictions, vendor-specific APIs, or feature gating, backed by 24×7 Expert Support and optional ExpertOps.

### Customer Challenges and Value Alignment: PostgreSQL

**Optimized TCO**

- Open source without compromise: The Percona Distribution for PostgreSQL consolidates trusted community components into one enterprise-validated package, eliminating the cost and complexity of proprietary add-ons. Türk Telekom eliminated licensing costs, cut query times substantially, and boosted customer satisfaction by delivering high availability and resilience across critical services with Percona Distribution for PostgreSQL.
- Open source Kubernetes automation: Percona Operator for PostgreSQL is a hard fork of Crunchy PGO with Percona-owned development and community-driven evolution, extending the same inspectable PostgreSQL stack to Kubernetes without a vendor-tied operator control plane. On upgrade, upstream Crunchy resources migrate automatically to the `upstream.pgv2.percona.com` API group so Percona and Crunchy operators can coexist during adoption and teams can move without re-architecting clusters.
- Migration clarity when PostgreSQL licensing or managed-service roadmaps change: Vendor bundles and subscription models evolve on timelines teams do not control. Percona publishes positioning on portable PostgreSQL software versus proprietary distributions and managed PostgreSQL stacks ([Percona Software for PostgreSQL](https://www.percona.com/postgresql/software)), which helps organizations compare options on cleared public materials and plan moves without proprietary APIs that trap operational state.
- Legacy RDBMS exit to PostgreSQL for TCO: Teams exiting proprietary or legacy RDBMS footprints can reduce license and support spend by landing on Percona Distribution for PostgreSQL with assessment-led migration through [Percona Expert Consulting and Services](https://www.percona.com/services/consulting). Scope and source-to-target patterns are confirmed during assessment.

**Performance and Reliability at Scale**

- High-availability and disaster recovery made simple: The Percona Distribution for PostgreSQL includes Patroni to automate failover for high availability and coordinate switchovers for maintenance tasks, and pgBackRest for backup catalog management and Point-in-Time Recovery (PiTR) when data must be restored after higher-impact incidents. Reference patterns and implementation guidance are in [High availability for PostgreSQL](https://www.percona.com/ha-for-postgresql). Distribution releases keep Patroni HA automation and its coordination stack release-tested through upgrade cadence across supported PostgreSQL majors. Automated failover minimises recovery time and outage impact.
- Logical replication for migration and distributed PostgreSQL: Percona Distribution for PostgreSQL on PostgreSQL 18 supports parallel logical replication for faster initial data synchronization during replica build and major-version migration, reducing cutover risk and replication catch-up time. When teams need active-active replication, conflict handling, selective replication, or zero-downtime major-version upgrades beyond that native capability, they often add pgEdge Spock on customer-managed PostgreSQL. In those distributed topologies, multiple nodes accepting writes can collide on standard PostgreSQL sequences and primary keys; pgEdge Snowflake Sequences generates globally unique, time-ordered 64-bit identifiers on each node without centralized sequence coordination and is often used alongside Spock. Spock and Snowflake Sequences are not packaged in Percona Distribution for PostgreSQL ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)). Percona Expert Support includes advisory guidance for installation, configuration, and production use of both on Advanced Support and Premium Support tiers.
- Built-in replication lag monitoring: PostgreSQL provides native, accurate replication lag tracking through `pg_stat_wal_receiver` and WAL LSN comparison, without requiring external heartbeat tooling. PMM surfaces this data via the `pg_custom_stat_wal_receiver_lag_bytes` metric (sourced from `postgres_exporter`). Teams migrating from MySQL (where external tools like pt-heartbeat are common for lag measurement) gain this capability out of the box with PostgreSQL.
- Horizontal scale and legacy tooling: Expert Support and consulting cover Citus sharding and timescale time-series workloads on customer-managed PostgreSQL coordinated with Patroni HA where those extensions run alongside the distribution stack (neither Citus nor timescale is packaged in the standard distribution build; see [third-party components](https://docs.percona.com/postgresql/18/third-party.html)). Percona Expert Support includes advisory guidance for estates that still run barman or repmgr alongside PostgreSQL where migration to pgBackRest and Patroni is phased.
- Deep PostgreSQL observability extensions: Percona Expert Support includes advisory guidance for pg_stat_kcache and pg_wait_sampling for kernel-level query resource visibility and sampled wait-event analysis; pg_wait_sampling integrates with PMM for unified wait analysis where teams deploy both.

**Security, Sovereignty, and Compliance**

- End-to-end encryption: Percona integrates pg_tde for database-level transparent data-at-rest and WAL encryption (not storage-only encryption alone), including 256-bit AES, optimized encrypted I/O, and external key management through HashiCorp Vault, Thales CipherTrust, Fortanix SDKMS, Open Bao, and Akeyless. Encrypted-cluster upgrades are supported through pg_tde_upgrade and validated major-version upgrade paths on the distribution stack. Current constraints and KMS options are documented in [Percona Transparent Data Encryption for PostgreSQL](https://docs.percona.com/pg-tde/).
- Authentication, audit, and vulnerability management: Percona supports LDAP, Kerberos, and TLS for centralized authentication. pgAudit and Percona's documented CVE process strengthen auditability for GDPR, HIPAA, and PCI-DSS frameworks and keep supported PostgreSQL versions on current security fixes.
- Validated open source integrity: Every build is open for audit and inspection, ensuring compliance without dependence on opaque vendor frameworks.

**Adaptability for Emerging Workloads**

- Cloud-native operations: The Percona Operator for PostgreSQL automates deployment, scaling, and failover in Kubernetes environments, delivering consistent governance and portability across any cloud.
- Platform portability: Percona Distribution for PostgreSQL ships packages for current Ubuntu LTS releases, including Ubuntu 26.04 on AMD64 and ARM64, so teams can standardize database deployments on their long-term support platform images without retooling the stack.
- AI and analytics readiness: Teams run embeddings and vector search on PostgreSQL using pgvector packaged with other tested distribution components ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)), avoiding a separate AI-only datastore for many workloads. Percona Expert Support includes advisory guidance for pgvector and pgvectorscale production tuning; pgvectorscale is not packaged in Percona Distribution for PostgreSQL.
- Geospatial workloads: PostGIS ships as a validated third-party component; Expert Support and consulting cover coordinated PostgreSQL and PostGIS upgrades, dependency checks, and spatial workload regression planning ([PostGIS deployment](https://docs.percona.com/postgresql/17/solutions/postgis-deploy.html)).

### Conversation starters

- How long does it take your team to configure vanilla PostgreSQL for a new production environment? (The distribution ships HA, backup, and security components release-tested together.)
- What do you do when PostgreSQL is down? (Percona Expert Support provides SLA-backed escalation.)
- How do you ensure PostgreSQL infrastructure performs well under load? (Support, ExpertOps, and consulting cover tuning and architecture.)
- How do you meet uptime and incident-response requirements from regulators or customers?
- How much internal PostgreSQL expertise does your team have today?
- If you already have a support contract: How has your experience been with your current vendor?
- If migrating from Oracle or another proprietary database: How will you handle schema and data migration, HA architecture, and zero-downtime cutover if the target needs active-active replication or distributed writes?

### Public resources

- [Percona Software for PostgreSQL](https://www.percona.com/postgresql/software)
- [High availability for PostgreSQL](https://www.percona.com/ha-for-postgresql)
- [pg_tde documentation](https://docs.percona.com/pg-tde/)
- [Percona Distribution for PostgreSQL release notes](https://docs.percona.com/postgresql/latest/release-notes/release-notes.html)
- [Support for PostgreSQL](https://www.percona.com/services/support/postgresql-support)
- [Database comparison (MySQL, MongoDB, PostgreSQL, MariaDB)](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
