# Percona for MySQL: Messaging

## Percona for MySQL {#percona-for-mysql}

For organizations running MySQL applications requiring enterprise-grade performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, Percona's MySQL solutions, including Percona Server for MySQL, Percona XtraDB Cluster, Percona XtraBackup, ProxySQL, Orchestrator, Percona Toolkit, and common MySQL ecosystem components such as HAProxy, MySQL Router, and MySQL Shell, provide a fully open source, production- and performance-tested foundation for critical workloads. The Percona Distribution for MySQL offers curated, lifecycle-managed assemblies for single-instance (Percona Server-based) and high-availability cluster (PXC-based) deployments, while the optional Kubernetes Operator and Percona Monitoring and Management (PMM) provide automated operations and unified observability.

Unlike Oracle MySQL Enterprise or proprietary DBaaS offerings, Percona delivers the same reliability, scalability, and lifecycle assurance, backed by 24×7 Expert Support, without vendor lock-in, feature gating, or unpredictable costs, and with full transparency and data ownership across environments.

### Customer Challenges and Value Alignment – MySQL

**Optimized TCO**

- Open source with enterprise-grade capabilities: Percona Server for MySQL is a fully open source, enhanced, and backward-compatible replacement for MySQL Community Edition. It serves as a functional alternative to Oracle MySQL Enterprise Edition, delivering many comparable or extended capabilities without proprietary licensing or feature gating.
- EOL pressure and rising costs: Organizations running MySQL 5.7 or 8.0 face Oracle EOL deadlines or costly RDS extended support. The date-certain external deadline in this cycle is Oracle MySQL 8.0 EOL on 2026-04-30. Percona offers post-EOL security and maintenance coverage, helping customers maintain stability or migrate safely without inflated licensing costs. Teams planning beyond 8.0 should align on Percona Server for MySQL and Percona Distribution for MySQL on supported 8.4 lines rather than treating 8.0 as the default reference release. Percona Server for MySQL continues this commitment with backported fixes and lifecycle coverage options documented in Percona lifecycle policy and release notes. Time To Pet avoided expensive proprietary EOL extensions by migrating safely to Percona Server for MySQL, gaining years of headroom for future growth and full lifecycle assurance.

**Performance and Reliability at Scale**

- Performance degradation under load: High-concurrency applications often face throughput drops and latency spikes. Percona Server for MySQL includes thread pooling, user statistics, and other extended instrumentation for better resource management. Layer7 processes 200M calls, 3M SMS, and 680M+ transactions per month on Percona Server for MySQL, and achieved zero unplanned downtime with 24x7 ExpertOps Proactive Database Management (previously Managed Services).

**Security, Sovereignty, and Compliance**

- Security and compliance: Regulated industries need strong encryption, auditing, and data residency assurance. Percona Server for MySQL includes auditing via the Audit Log Plugin or the newer Audit Log Component (depending on version), integration with LDAP and Kerberos through the Percona Authentication Plugin (PAM), and FIPS-capable binaries in standard builds (from Percona Server for MySQL 8.4.0-5 onward; FIPS mode depends on a FIPS-enabled host OpenSSL stack and documented configuration; see [FIPS compliance](https://docs.percona.com/percona-server/8.4/fips.html)). Percona Toolkit 3.7.1-3 messaging in this cycle is security-focused, centered on remediation updates, not new feature positioning. Recent Percona XtraDB Cluster releases include audit policy consistency improvements across cluster nodes, reinforcing reliable policy enforcement in distributed environments.

**Adaptability for Emerging Workloads**

- Kubernetes operator choice by topology: Percona maintains **three** MySQL operator deployment paths on Kubernetes. The [Percona Operator for MySQL (PXC)](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) line automates **Percona XtraDB Cluster** for synchronous multi-primary HA. The [Percona Operator for MySQL (Percona Server)](https://docs.percona.com/percona-operator-for-mysql/ps/index.html) line delivers production-grade automation for **standalone Percona Server for MySQL**, with point-in-time recovery and incremental backups in technical preview where documented. The same Percona Server for MySQL operator line ships **MySQL Group Replication** as its GA topology (distinct from the PXC operator), offering strongly consistent HA with asynchronous replication in technical preview where documented. Pick the path that matches your HA model.
- Continuous reliability investment: Percona XtraDB Cluster releases continue to harden the HA stack, including improvements for state transfer behavior, trigger consistency, and maintenance operations in rolling update paths.

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
- Now that Oracle MySQL 8.0 reached end of life on 2026-04-30, are you still running 8.0? Do you have a plan for support or continuity? (Migrate or upgrade with Percona, or use post-EOL coverage while you finish your plan.)
- Are you planning vector search or AI workloads on MySQL without adding another datastore? (Percona is developing native MySQL Vector indexing and a dedicated Binlog Server for reliable point-in-time recovery and replication at scale.)
- Do compliance requirements keep you on MySQL Enterprise Edition? (Percona Distribution for MySQL and Percona Server for MySQL provide open, inspectable components and documented FIPS mode without Enterprise licensing.)
- Are you enabling FIPS on the database layer today? (Confirm OS OpenSSL FIPS readiness and Percona Server for MySQL configuration against public FIPS documentation.)

**Public resources**

- [Percona for MySQL software](https://www.percona.com/software/mysql-database)
- [Alternative to Enterprise MySQL](https://www.percona.com/alternative-to-enterprise-mysql)
- [Upgrade to MySQL 8.0 with Percona](https://www.percona.com/upgrading-to-mysql-8-0-with-percona)
- [Post-MySQL 5.7 EOL support](https://www.percona.com/post-mysql-5-7-eol-support)
- [FIPS compliance for Percona Server for MySQL](https://docs.percona.com/percona-server/8.4/fips.html)
- [MySQL Vector and Binlog Server roadmap](https://www.percona.com/blog/building-the-future-of-mysql-announcing-plans-for-mysql-vector-support-and-a-mysql-binlog-server/)
