# Percona for MySQL: Messaging

## Percona for MySQL {#percona-for-mysql}

For organizations running MySQL applications requiring enterprise-grade performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, Percona's MySQL solutions, including Percona Server for MySQL, Percona XtraDB Cluster, XtraBackup, ProxySQL, Orchestrator, and Percona Toolkit, provides a fully open source, production- and performance-tested foundation for critical workloads. The Percona Distribution for MySQL offers a curated, lifecycle-managed assembly of these components, while the optional Kubernetes Operator and Percona Monitoring and Management (PMM) provide automated operations and unified observability.

Unlike Oracle MySQL Enterprise or proprietary DBaaS offerings, Percona delivers the same reliability, scalability, and lifecycle assurance, backed by 24×7 Expert Support, without vendor lock-in, feature gating, or unpredictable costs, and with full transparency and data ownership across environments.

### Customer Challenges and Value Alignment – MySQL

**Optimized TCO**
- Open source with enterprise-grade capabilities: Percona Server for MySQL is a fully open source, enhanced, and backward-compatible replacement for MySQL Community Edition. It serves as a functional alternative to Oracle MySQL Enterprise Edition, delivering many comparable or extended capabilities without proprietary licensing or feature gating.
- EOL pressure and rising costs: Organizations running MySQL 5.7 or 8.0 face Oracle EOL deadlines or costly RDS extended support. Percona offers post-EOL security and maintenance coverage, helping customers maintain stability or migrate safely without inflated licensing costs. Percona Server for MySQL 5.7.44-57 (Mar 2026) continues this commitment with backported bug fixes (GIS index stability, join parsing performance, memory leak fixes), available to paying customers via private repository and to community users as quarterly source releases. Time To Pet avoided expensive proprietary EOL extensions by migrating safely to Percona Server for MySQL, gaining years of headroom for future growth and full lifecycle assurance.

**Performance and Reliability at Scale**
- Performance degradation under load: High-concurrency applications often face throughput drops and latency spikes. Percona Server for MySQL includes thread pooling, user statistics, and other extended instrumentation for better resource management. Layer7 processes 200M calls, 3M SMS, and 680M+ transactions per month on Percona Server for MySQL, and achieved zero unplanned downtime with 24x7 ExpertOps Proactive Database Management (previously Managed Services).

**Security, Sovereignty, and Compliance**
- Security and compliance: Regulated industries need strong encryption, auditing, and data residency assurance. Percona Server for MySQL includes FIPS 140-2–validated builds, auditing via the Audit Log Plugin or the newer Audit Log Component (depending on version), open audit plugin, and integration with LDAP and Kerberos with the Percona Authentication Plugin (PAM) for secure access, supporting compliance with frameworks like HIPAA, GDPR, and PCI-DSS. Percona XtraDB Cluster 8.0.45-36 (Mar 2026) fixed audit log filter execution sync across PXC nodes (PXC-4753), ensuring consistent audit policy enforcement cluster-wide.

**Adaptability for Emerging Workloads**
- Multi-environment operations: Running MySQL on Kubernetes or across multi-cloud requires specialized expertise. Percona Kubernetes Operator for MySQL (built for Percona XtraDB Cluster, with a technical preview available for standalone MySQL Server), automates backups, scaling, and upgrades.
- Continuous reliability investment: PXC 8.0.45-36 (Mar 2026) includes fixes for IST failure handling that could leave clusters unresponsive (PXC-4845), trigger definer consistency (PXC-4765), and OPTIMIZE TABLE under Rolling Schema Update mode (PXC-4814), reflecting ongoing hardening of the HA stack.
