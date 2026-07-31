# Percona for PostgreSQL: Messaging

## Percona for PostgreSQL {#percona-for-postgresql}

Percona Distribution for PostgreSQL is a fully open source, production- and performance-tested database platform for organizations running PostgreSQL across on-prem, cloud, and hybrid environments. It's built for high performance, reliability, security, sovereignty, and compliance. 

It packages and validates trusted PostgreSQL components as matched, release-tested binaries, so teams don't have to assemble and validate tooling themselves:

- Patroni for high availability
- pgBackRest for backup catalog management and PITR-capable restores
- pgAudit and pg_stat_monitor for compliance and observability
- PostGIS for geospatial workloads
- pgvector for vector search and embeddings
- pg_tde for transparent data-at-rest and WAL encryption, with integration for external key management systems (HashiCorp Vault, Thales CipherTrust, Fortanix SDKMS, OpenBao, and Akeyless)
  
Paired with Percona Monitoring and Management (PMM) and the Percona Operator for PostgreSQL, organizations get consistent visibility and automation across hybrid and Kubernetes environments.
Unlike license-restricted PostgreSQL offerings and proprietary DBaaS services, Percona delivers enterprise-grade resilience and tooling with no license restrictions, vendor-specific APIs, or feature gating. It's backed by 24x7 Expert Support and optional ExpertOps.


### Customer Challenges and Value Alignment: PostgreSQL

**Optimized TCO**

- Open source without compromise: Reduce licensing costs without giving up enterprise capabilities. Percona Distribution for PostgreSQL brings trusted PostgreSQL components together in a single validated distribution, cutting operational complexity while avoiding proprietary licensing. Türk Telekom eliminated licensing costs, reduced query times, and improved customer satisfaction by deploying HA and resilience with Percona.
  
- Open source Kubernetes automation: Run PostgreSQL consistently across Kubernetes without introducing another proprietary control plane. Percona Operator for PostgreSQL is a hard fork of Crunchy PGO, with Percona-owned development and community-driven evolution. On upgrade, upstream Crunchy resources migrate automatically to the `upstream.pgv2.percona.com` API group so Percona and Crunchy operators can coexist during adoption and teams can move without re-architecting clusters.
  
- Migration clarity when PostgreSQL licensing or managed-service roadmaps change: Evaluate migration options with confidence as licensing models evolve. Percona helps organizations compare portable PostgreSQL software against proprietary distributions and managed services ([Percona Software for PostgreSQL](https://www.percona.com/postgresql/software)), using publicly available information, making it easier to choose a migration path while maintaining flexibility and avoiding vendor lock-in.

- Legacy RDBMS exit to PostgreSQL for TCO: Modernize legacy databases with a structured migration approach. [Percona Expert Consulting and Services](https://www.percona.com/services/consulting) support migrations from MySQL, MariaDB, Oracle, and SQL Server to [Percona Distribution for PostgreSQL](https://www.percona.com/postgresql/software), covering schema migration, code conversion, data migration, continuous replication, validation, and cutover, with scope and downtime tolerance confirmed during assessment. 

**Performance and Reliability at Scale**

- High-availability and disaster recovery made simple: Minimize downtime with automated failover. Patroni handles failover and coordinates maintenance switchovers; pgBackRest manages backups and enables Point-in-Time Recovery (PITR). Both are release-tested together across every supported PostgreSQL major version. See [High availability for PostgreSQL](https://www.percona.com/ha-for-postgresql) for implementation guidance.

- Logical replication for migration and distributed PostgreSQL:  Reduce cutover risk and speed up migrations. PostgreSQL 18 supports parallel logical replication for faster initial sync during replica builds and major-version migrations. For active-active replication, conflict handling, or zero-downtime upgrades, teams can add pgEdge Spock; pgEdge Snowflake Sequences generates globally unique, time-ordered 64-bit IDs on each node, avoiding collisions on standard sequences and primary keys without centralized coordination. Both are ([third-party components](https://docs.percona.com/postgresql/18/third-party.html)), not packaged in the distribution. Expert Support advises on both for Advanced and Premium tiers.

- Built-in replication lag monitoring:  Get accurate lag visibility with no extra tooling. PostgreSQL provides native, accurate replication lag tracking through `pg_stat_wal_receiver` and WAL LSN comparison, without requiring external heartbeat tooling. PMM surfaces this data via the `pg_custom_stat_wal_receiver_lag_bytes` metric (sourced from `postgres_exporter`). Teams migrating from MySQL (where external tools like pt-heartbeat are common for lag measurement) gain this capability out of the box with PostgreSQL.
  
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
