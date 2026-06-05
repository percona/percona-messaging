# Percona for MySQL: Messaging

## Percona for MySQL {#percona-for-mysql}

For organizations running MySQL applications requiring enterprise-grade performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, Percona's MySQL solutions, including Percona Server for MySQL, Percona XtraDB Cluster, Percona XtraBackup, ProxySQL, Orchestrator, Percona Toolkit, and common MySQL ecosystem components such as HAProxy, MySQL Router, and MySQL Shell, provide a fully open source, production- and performance-tested foundation for critical workloads. The Percona Distribution for MySQL offers curated, lifecycle-managed assemblies for single-instance (Percona Server-based) and high-availability cluster (PXC-based) deployments, while the optional Kubernetes Operator and Percona Monitoring and Management (PMM) provide automated operations and unified observability.

Unlike Oracle MySQL Enterprise or proprietary DBaaS offerings, Percona delivers an in-place, backward-compatible replacement for Enterprise-grade capabilities, backed by 24×7 Expert Support, without vendor lock-in, feature gating, or unpredictable costs, and with full transparency and data ownership across environments.

### Customer Challenges and Value Alignment – MySQL

**In-place replacement for MySQL Enterprise Edition**

Percona Server for MySQL is a drop-in, binary-compatible replacement for the matching MySQL version, so teams move from Oracle MySQL Community or Enterprise Edition in place without re-architecting applications or changing connection libraries, using standard MySQL upgrade and replication paths. Enterprise parity features ship in standard open source builds without proprietary licensing. For the full itemized comparison across engines, see [Percona feature comparison](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb).

**Enterprise parity at a glance**

- **Enterprise parity:** Audit logging (including Audit Log Filter), PAM / LDAP / FIDO authentication, Data masking, Thread pool, External key management (HashiCorp Vault, KMIP, AWS KMS keyring), FIPS mode (standard PS and PXC builds from 8.4.7 onward).
- **Beyond Enterprise:** MyRocks, binary log and temporary file encryption, enforce-encryption, backup locks, kill idle transactions, per-table / per-index / per-user / per-thread counters, user statistics, extended slow query logging, deeper INFORMATION_SCHEMA (95 tables vs 65 in Community), per-column compression, and more ([feature comparison](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)).

**Optimized TCO**

- In-place Enterprise replacement without license escalation: Teams retire Oracle MySQL Enterprise subscriptions while keeping applications on a backward-compatible MySQL code line. Enterprise parity and beyond-Enterprise capabilities ship in open source builds, so operational teams stop paying for feature gating without a rip-and-replace migration ([upgrade documentation](https://docs.percona.com/percona-server/8.4/upgrade.html)).
- EOL pressure and rising costs: Organizations running MySQL 5.7 or 8.0 face Oracle EOL deadlines or costly RDS extended support. The date-certain external deadline in this cycle is Oracle MySQL 8.0 EOL on 2026-04-30. Percona offers post-EOL security and maintenance coverage, helping customers maintain stability or migrate safely without inflated licensing costs. Teams planning beyond 8.0 should align on Percona Server for MySQL and Percona Distribution for MySQL on supported 8.4 lines rather than treating 8.0 as the default reference release. Percona Server for MySQL continues this commitment with backported fixes and lifecycle coverage options documented in Percona lifecycle policy and release notes. Time To Pet avoided expensive proprietary EOL extensions by migrating safely to Percona Server for MySQL, gaining years of headroom for future growth and full lifecycle assurance.

**Performance and Reliability at Scale**

- Throughput under high concurrency: Percona Server for MySQL includes a connection Thread pool so high-concurrency applications sustain throughput with less latency spike than default threading alone.
- Operational visibility: Per-table, per-index, per-user, and per-thread counters, user statistics, extended slow query logging, and a deeper INFORMATION_SCHEMA (95 tables vs 65 in Community) help teams pinpoint hot objects and abusive sessions faster than Community instrumentation alone.
- Storage and maintenance efficiency: MyRocks reduces storage footprint and write amplification for write-heavy workloads. Backup locks and kill idle transactions improve backup consistency and reduce lock contention during maintenance windows.
- Proven scale: Layer7 processes 200M calls, 3M SMS, and 680M+ transactions per month on Percona Server for MySQL, and achieved zero unplanned downtime with 24x7 ExpertOps Proactive Database Management (previously Managed Services).
- High availability without vendor roadmap dependency: After MariaDB nearly removed Galera from Community Server in 2026 (and walked back only after community outcry), **Percona XtraDB Cluster** runs Percona's own open Galera fork for synchronous multi-primary HA with split-brain prevention and WAN-friendly weighted quorum, giving mission-critical workloads a stable, vendor-controlled HA home. **MySQL Group Replication** is supported through the [Percona Operator for MySQL (Percona Server)](https://docs.percona.com/percona-operator-for-mysql/ps/index.html) (GA since November 2025) or on Percona Distribution for MySQL deployments. Percona supports whichever topology fits your architecture; neither path depends on a competitor's roadmap.
- Continuous reliability investment: Percona XtraDB Cluster releases continue to harden the HA stack, including improvements for state transfer behavior, trigger consistency, and maintenance operations in rolling update paths.

**Security, Sovereignty, and Compliance**

- Audit and access controls: Audit logging, including Audit Log Filter, meets regulatory and internal audit requirements with configurable policy enforcement. PAM, LDAP, and FIDO authentication (PAM supports Kerberos and other enterprise methods) integrate MySQL with existing identity systems. Recent Percona XtraDB Cluster releases include audit policy consistency improvements across cluster nodes.
- Data protection: Data masking protects sensitive fields in non-production and analytics environments. External key management through HashiCorp Vault, KMIP, and AWS KMS keyring aligns encryption key custody with enterprise KMS programs. Binary log and temporary file encryption plus enforce-encryption strengthen data-in-motion and at-rest posture beyond baseline Community options.
- FIPS for regulated environments: As of Percona Server for MySQL 8.4.7, FIPS-capable binaries ship in all supported PS builds; Percona XtraDB Cluster supports FIPS as well. Regulated and government buyers can enable documented FIPS mode on those standard builds. FIPS mode depends on a FIPS-enabled host OpenSSL stack and documented configuration; see [FIPS compliance](https://docs.percona.com/percona-server/8.4/fips.html).
- Tooling posture: Percona Toolkit 3.7.1-3 messaging in this cycle is security-focused, centered on remediation updates, not new feature positioning.

**Adaptability for Emerging Workloads**

- Kubernetes operator choice by topology: Percona maintains **three** MySQL operator deployment paths on Kubernetes. The [Percona Operator for MySQL (PXC)](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) line automates **Percona XtraDB Cluster** for synchronous multi-primary HA. The [Percona Operator for MySQL (Percona Server)](https://docs.percona.com/percona-operator-for-mysql/ps/index.html) line delivers production-grade automation for **standalone Percona Server for MySQL**, with point-in-time recovery and incremental backups in technical preview where documented. The same Percona Server for MySQL operator line ships **MySQL Group Replication** as its GA topology (distinct from the PXC operator), offering strongly consistent HA with asynchronous replication in technical preview where documented. Pick the path that matches your HA model.
- Driving MySQL evolution in the open: Percona invests in vector and AI inside the database, backup and replication reliability, performance leadership, cloud-native operations by default, modern security and compliance, and a healthy MySQL community, so teams adopt innovation on open, inspectable software rather than waiting on proprietary release gates.

### Sales enablement

**Elevator pitch**

Percona delivers a drop-in, in-place, backward-compatible replacement for Oracle MySQL Enterprise Edition: open source software with Enterprise parity features shipped free, plus Expert Support so teams run demanding workloads with better performance, scalability, availability, and visibility, without proprietary licensing or feature gating.

**Purpose**

MySQL is powerful, but teams running diverse infrastructure often face subscription-only features, rising Enterprise licensing costs, and release cadence gaps as workloads grow. Percona helps organizations adopt and operate MySQL on their own terms: migrate in place, retain Enterprise-grade capabilities in open source builds, and scale with transparent software, expert support, and optional ExpertOps for proactive operations.

**Conversation starters**

- Do compliance requirements keep you on MySQL Enterprise Edition? (Percona Server for MySQL and Percona Distribution for MySQL provide Enterprise-parity audit, authentication, masking, and FIPS capabilities in standard open source builds without Enterprise licensing.)
- Are you enabling FIPS on the database layer today? (FIPS-capable binaries ship in all supported Percona Server for MySQL builds from 8.4.7 onward, and Percona XtraDB Cluster supports FIPS. Confirm OS OpenSSL FIPS readiness and documented configuration.)
- What is keeping you from moving off MySQL Enterprise Edition? (Migration is a drop-in, in-place move on a backward-compatible code line; Expert Support and migration services help reduce downtime and data-loss risk.)
- Which HA model fits your architecture: synchronous multi-primary (Percona XtraDB Cluster / Galera) or Group Replication? (Percona supports both through software, operators, and Expert Support; pick the topology that matches your requirements.)
- Is your current vendor flexible when scaling MySQL up and down? (Open source Percona software can adapt quickly without license escalation.)
- Are you satisfied with the cost and support you receive from Oracle for MySQL? (Many teams compare Percona for comparable operational capabilities without proprietary licensing.)
- What databases besides MySQL does your team support? (Percona provides multi-engine expertise across MySQL, PostgreSQL, MongoDB, and Valkey.)
- Are you planning vector search or AI workloads on MySQL without adding another datastore? (Percona is developing native MySQL Vector indexing and a dedicated Binlog Server for reliable point-in-time recovery and replication at scale.)
- Now that Oracle MySQL 8.0 reached end of life on 2026-04-30, are you still running 8.0? Do you have a plan for support or continuity? (Migrate or upgrade with Percona, or use post-EOL coverage while you finish your plan.)

**Public resources**

- [Percona for MySQL software](https://www.percona.com/software/mysql-database)
- [Alternative to Enterprise MySQL](https://www.percona.com/alternative-to-enterprise-mysql)
- [Percona feature comparison](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
- [Upgrade to MySQL 8.0 with Percona](https://www.percona.com/upgrading-to-mysql-8-0-with-percona)
- [Post-MySQL 5.7 EOL support](https://www.percona.com/post-mysql-5-7-eol-support)
- [FIPS compliance for Percona Server for MySQL](https://docs.percona.com/percona-server/8.4/fips.html)
- [MySQL Vector and Binlog Server roadmap](https://www.percona.com/blog/building-the-future-of-mysql-announcing-plans-for-mysql-vector-support-and-a-mysql-binlog-server/)
