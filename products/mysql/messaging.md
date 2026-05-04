# Percona for MySQL: Messaging

## Percona for MySQL {#percona-for-mysql}

For organizations running MySQL applications requiring enterprise-grade performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, Percona's MySQL solutions, including Percona Server for MySQL, Percona XtraDB Cluster, XtraBackup, ProxySQL, Orchestrator, and Percona Toolkit, provide a fully open source, production- and performance-tested foundation for critical workloads. The Percona Distribution for MySQL offers a curated, lifecycle-managed assembly of these components, while the optional Kubernetes Operator and Percona Monitoring and Management (PMM) provide automated operations and unified observability.

Unlike Oracle MySQL Enterprise or proprietary DBaaS offerings, Percona delivers the same reliability, scalability, and lifecycle assurance, backed by 24×7 Expert Support, without vendor lock-in, feature gating, or unpredictable costs, and with full transparency and data ownership across environments.

### Customer Challenges and Value Alignment – MySQL

**Optimized TCO**

- Open source with enterprise-grade capabilities: Percona Server for MySQL is a fully open source, enhanced, and backward-compatible replacement for MySQL Community Edition. It serves as a functional alternative to Oracle MySQL Enterprise Edition, delivering many comparable or extended capabilities without proprietary licensing or feature gating.
- EOL pressure and rising costs: Organizations running MySQL 5.7 or 8.0 face Oracle EOL deadlines or costly RDS extended support. The date-certain external deadline in this cycle is Oracle MySQL 8.0 EOL on 2026-04-30. Percona offers post-EOL security and maintenance coverage, helping customers maintain stability or migrate safely without inflated licensing costs. Percona Server for MySQL continues this commitment with backported fixes and lifecycle coverage options documented in Percona lifecycle policy and release notes. Time To Pet avoided expensive proprietary EOL extensions by migrating safely to Percona Server for MySQL, gaining years of headroom for future growth and full lifecycle assurance.

**Performance and Reliability at Scale**

- Performance degradation under load: High-concurrency applications often face throughput drops and latency spikes. Percona Server for MySQL includes thread pooling, user statistics, and other extended instrumentation for better resource management. Layer7 processes 200M calls, 3M SMS, and 680M+ transactions per month on Percona Server for MySQL, and achieved zero unplanned downtime with 24x7 ExpertOps Proactive Database Management (previously Managed Services).

**Security, Sovereignty, and Compliance**

- Security and compliance: Regulated industries need strong encryption, auditing, and data residency assurance. Percona Server for MySQL includes FIPS 140-2–validated builds, auditing via the Audit Log Plugin or the newer Audit Log Component (depending on version), open audit plugin, and integration with LDAP and Kerberos with the Percona Authentication Plugin (PAM) for secure access, supporting compliance with frameworks like HIPAA, GDPR, and PCI-DSS. Percona Toolkit 3.7.1-3 messaging in this cycle is security-focused, centered on remediation updates, not new feature positioning. Recent Percona XtraDB Cluster releases also include audit policy consistency improvements across cluster nodes, reinforcing reliable policy enforcement in distributed environments.

**Adaptability for Emerging Workloads**

- Multi-environment operations: Running MySQL on Kubernetes or across multi-cloud requires specialized expertise. Percona Kubernetes Operator for MySQL has separate lines for Percona XtraDB Cluster and Percona Server for MySQL. The Percona Server for MySQL operator line is production-grade automation for MySQL on Kubernetes, with point-in-time recovery (PITR) and incremental backups in technical preview, while the Percona XtraDB Cluster line is mature production. Together, they automate backups, scaling, and upgrades based on deployment requirements.
- Current shipped operator signals: Percona Operator for MySQL 1.1.0 (Percona Server for MySQL line) delivers production-grade Kubernetes automation with PITR and incremental backups in technical preview, plus compression updates, while Percona Operator for MySQL 1.19.1 (Percona XtraDB Cluster line) shipped with fixes such as the ProxySQL crash-loop scenario in cross-site replication setups. Detailed release-specific operator narrative is maintained in the Operators lane.
- Continuous reliability investment: Percona XtraDB Cluster releases continue to harden the HA stack, including improvements for state transfer behavior, trigger consistency, and maintenance operations in rolling update paths.
