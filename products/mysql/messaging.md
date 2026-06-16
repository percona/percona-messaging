# Percona for MySQL: Messaging

## Percona for MySQL {#percona-for-mysql}

For organizations running MySQL applications requiring enterprise-grade performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, Percona's MySQL solutions, including Percona Server for MySQL, Percona XtraDB Cluster, Percona XtraBackup, ProxySQL, Orchestrator, Percona Toolkit, and common MySQL ecosystem components such as HAProxy, MySQL Router, and MySQL Shell, provide a fully open source, production- and performance-tested foundation for critical workloads. The Percona Distribution for MySQL offers curated, lifecycle-managed assemblies for single-instance (Percona Server-based) and high-availability cluster (PXC-based) deployments, while the optional Kubernetes Operator and Percona Monitoring and Management (PMM) provide automated operations and unified observability.

Unlike Oracle MySQL Enterprise or proprietary DBaaS offerings, Percona delivers the same reliability, scalability, and lifecycle assurance, backed by 24×7 Expert Support, without vendor lock-in, feature gating, or unpredictable costs, and with full transparency and data ownership across environments.

### Customer Challenges and Value Alignment – MySQL

**Optimized TCO**

- Open source with enterprise-grade capabilities: Percona Server for MySQL is a fully open source, enhanced, and backward-compatible replacement for MySQL Community Edition. It serves as a functional alternative to Oracle MySQL Enterprise Edition, delivering many comparable or extended capabilities without proprietary licensing or feature gating.
- EOL pressure and rising costs: Organizations running MySQL 5.7 or 8.0 face Oracle EOL deadlines or costly RDS extended support. MySQL 8.0 reached End of Life in the community on 21 April 2026. [Percona Server for MySQL 8.0.46-37](https://docs.percona.com/new/2026/06/10/percona-server-for-mysql-8046-37-has-been-released/) is the final release in the 8.0 series. Teams planning beyond 8.0 should align on Percona Server for MySQL and Percona Distribution for MySQL on supported 8.4 lines rather than treating 8.0 as the default reference release. For organizations that need more time on MySQL 8.0, Percona offers Extended Lifecycle Support (ELS): security and stability updates, optional migration planning, and a clear path to a supported release. ELS subscribers access pre-built binaries through a private repository; community members can build from publicly available source on a quarterly cadence. Percona does not use extended support to lock customers on end-of-life versions. ELS is a bridge while you plan and execute your upgrade. Percona continues Extended Lifecycle Support (ELS) for MySQL 5.7 for customers who cannot move to 8.x immediately. Oracle community support for MySQL 5.7 ended in November 2023. Percona Server for MySQL documents ELS and lifecycle coverage options in Percona lifecycle policy and release notes.

**Performance and Reliability at Scale**

- Performance degradation under load: High-concurrency applications often face throughput drops and latency spikes. Percona Server for MySQL includes thread pooling, user statistics, and other extended instrumentation for better resource management. Layer7 processes 200M calls, 3M SMS, and 680M+ transactions per month on Percona Server for MySQL, and achieved zero unplanned downtime with 24x7 ExpertOps Proactive Database Management (previously Managed Services).
- High availability without vendor roadmap dependency: **Percona XtraDB Cluster** runs Percona's own open source Galera fork for synchronous multi-primary HA with split-brain prevention and WAN-friendly weighted quorum, a vendor-independent HA home that does not depend on another vendor's roadmap. **MySQL Group Replication** is supported through the [Percona Operator for MySQL (Percona Server)](https://docs.percona.com/percona-operator-for-mysql/ps/index.html) (GA since November 2025) or on Percona Distribution for MySQL deployments. Percona supports whichever topology fits your architecture; neither path depends on a vendor's roadmap.
- MySQL Galera Cluster end of life: MariaDB has announced 2026-09-30 as the end of life for maintenance and regular binary releases of **MySQL Galera Cluster**. For teams still on MySQL Galera Cluster, **Percona XtraDB Cluster** is the natural replacement: both use Galera synchronous multi-primary HA, so the migration path is far simpler than crossing to a different database engine. Percona continues to maintain, release, and support PXC on the same lifecycle terms as today, including our own open Galera fork; teams already on PXC need no migration. **MySQL Group Replication** remains a supported alternative when that topology fits better ([continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/)).
- Continuous reliability investment: Percona XtraDB Cluster releases continue to harden the HA stack, including improvements for state transfer behavior, trigger consistency, and maintenance operations in rolling update paths.
- Backup and restore across environments: [Percona XtraBackup](https://docs.percona.com/new/2026/06/04/percona-xtrabackup-8035-36-has-been-released/) provides hot backup and restore for MySQL-compatible servers on bare metal, VMs, and cloud object stores, including the release supplied with [Percona Distribution for MySQL 8.0.46](https://docs.percona.com/new/2026/06/10/percona-distribution-for-mysql-8046-using-percona-server-for-mysql-has-been-released/). Percona XtraBackup removes backups correctly from Azure Data Lake Storage Gen2 accounts with hierarchical namespace enabled, where deletion previously failed, and streamlines sparse file handling to reduce backup overhead on thin-provisioned storage, helping teams keep retention policies enforceable and recovery paths tested.

**Security, Sovereignty, and Compliance**

- Security and compliance: Regulated industries need strong encryption, auditing, and data residency assurance. Percona Server for MySQL includes auditing via the Audit Log Plugin or the newer Audit Log Component (depending on version), integration with LDAP and Kerberos through the Percona Authentication Plugin (PAM), and FIPS-capable binaries in standard builds (from Percona Server for MySQL 8.4.0-5 onward; FIPS mode depends on a FIPS-enabled host OpenSSL stack and documented configuration; see [FIPS compliance](https://docs.percona.com/percona-server/8.4/fips.html)). [Percona Server for MySQL 8.0.46-37](https://docs.percona.com/new/2026/06/10/percona-server-for-mysql-8046-37-has-been-released/) flushes the audit log buffer on graceful shutdown when asynchronous logging is enabled, helping teams avoid losing buffered audit events during planned maintenance. Recent Percona XtraDB Cluster releases include audit policy consistency improvements across cluster nodes, reinforcing reliable policy enforcement in distributed environments.

**Adaptability for Emerging Workloads**

- Kubernetes operator choice by topology: Percona maintains **three** MySQL operator deployment paths on Kubernetes. The [Percona Operator for MySQL (PXC)](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) line automates **Percona XtraDB Cluster** for synchronous multi-primary HA. The [Percona Operator for MySQL (Percona Server)](https://docs.percona.com/percona-operator-for-mysql/ps/index.html) line delivers production-grade automation for **standalone Percona Server for MySQL**, with point-in-time recovery and incremental backups in technical preview where documented. The same Percona Server for MySQL operator line ships **MySQL Group Replication** as its GA topology (distinct from the PXC operator), offering strongly consistent HA with asynchronous replication in technical preview where documented. Pick the path that matches your HA model.

### Sales enablement

**Elevator pitch**

Percona makes MySQL operations easier for developers and database practitioners. Our open source software and Expert Support help teams run demanding workloads with better performance, scalability, availability, and visibility, without proprietary licensing or feature gating.

**Purpose**

MySQL is powerful, but teams running diverse infrastructure often face release cadence gaps, subscription-only features, and rising costs as workloads grow. Percona helps organizations adopt and operate MySQL on their own terms: build, deploy, manage, customize, and scale with transparent software, expert support, and optional ExpertOps for proactive operations.

**Conversation starters**

- Is your current vendor flexible when scaling MySQL up and down? (Open source Percona software can adapt quickly without license escalation.)
- What is keeping you from moving off MySQL Community or Enterprise Edition? (Expert Support and migration services help reduce downtime and data-loss risk.)
- Are you satisfied with the cost and support you receive from Oracle for MySQL? (Many teams compare Percona for comparable operational capabilities without proprietary licensing.)
- What databases besides MySQL does your team support? (Percona provides multi-engine expertise across MySQL, PostgreSQL, MongoDB, and Valkey.)
- Now that MySQL 8.0 reached End of Life in the community on 21 April 2026, are you still running 8.0? Do you have a plan for support or continuity? (Migrate or upgrade with Percona, or use Extended Lifecycle Support (ELS) while you finish your plan.)
- Are you planning vector search or AI workloads on MySQL without adding another datastore? (Percona is developing native MySQL Vector indexing and a dedicated Binlog Server for reliable point-in-time recovery and replication at scale.)
- Do compliance requirements keep you on MySQL Enterprise Edition? (Percona Distribution for MySQL and Percona Server for MySQL provide open, inspectable components and documented FIPS mode without Enterprise licensing.)
- Are you enabling FIPS on the database layer today? (Confirm OS OpenSSL FIPS readiness and Percona Server for MySQL configuration against public FIPS documentation.)
- Which HA model fits your architecture: synchronous multi-primary (Percona XtraDB Cluster / Galera) or Group Replication? (Percona supports both through software, operators, and Expert Support; pick the topology that matches your requirements.)
- Are you on MySQL Galera Cluster and tracking its 2026-09-30 end of life? (PXC is the natural Galera-to-Galera replacement; Percona continues releases and long-term support as before.)

**Public resources**

- [Continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/)
- [Percona for MySQL software](https://www.percona.com/software/mysql-database)
- [Alternative to Enterprise MySQL](https://www.percona.com/alternative-to-enterprise-mysql)
- [Upgrade to MySQL 8.0 with Percona](https://www.percona.com/upgrading-to-mysql-8-0-with-percona)
- [MySQL 5.7 Extended Lifecycle Support (ELS)](https://www.percona.com/post-mysql-5-7-eol-support)
- [FIPS compliance for Percona Server for MySQL](https://docs.percona.com/percona-server/8.4/fips.html)
- [MySQL Vector and Binlog Server roadmap](https://www.percona.com/blog/building-the-future-of-mysql-announcing-plans-for-mysql-vector-support-and-a-mysql-binlog-server/)
