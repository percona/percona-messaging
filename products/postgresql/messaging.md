# Percona for PostgreSQL: Messaging

## Percona for PostgreSQL {#percona-for-postgresql}

For organizations running PostgreSQL applications requiring performance, reliability, security, sovereignty, and compliance across on-prem, cloud, and hybrid environments, the Percona Distribution for PostgreSQL is a fully open source, production- and performance-tested database platform that includes tested, enterprise-grade extensions such as pgBackRest, Patroni, pgAudit, and pg_stat_monitor for observability and compliance.

The distribution also includes the pg_tde extension for transparent data-at-rest encryption and integrates with external key management systems like Hashicorp Vault, Thales CipherTrust, Fortanix SDKMS, Open Bao, and Akeyless. pg_tde 2.1.2 (Mar 2026) improved Vault/OpenBao KV v2 mount point validation, so the extension now works correctly with tokens that have only the required KV v2 read/write permissions (no metadata endpoint access needed). Together with Percona Monitoring and Management (PMM) and the Percona Operator for PostgreSQL, organizations gain consistent visibility and automation across hybrid and Kubernetes-based environments.

Unlike commercialized PostgreSQL derivatives such as EDB or proprietary DBaaS services, Percona provides the same enterprise-grade resilience and tooling without license restrictions, vendor-specific APIs, or feature gating, backed by 24×7 global support.

### Customer Challenges and Value Alignment – PostgreSQL

**Optimized TCO**
- Open source without compromise: The Percona Distribution for PostgreSQL consolidates trusted community components into one enterprise-validated package, eliminating the cost and complexity of proprietary add-ons. Türk Telekom eliminated licensing costs, cut query times substantially, and boosted customer satisfaction by delivering high availability and resilience across critical services with Percona Distribution for PostgreSQL.

**Performance and Reliability at Scale**
- High-availability and disaster recovery made simple: The Percona Distribution for PostgreSQL includes Patroni to automate the management of failover for high availability and coordinate switchovers for maintenance tasks. Automated failover minimises recovery time, avoiding the revenue impact of downtime. For higher impact events, when data needs to be recovered from backup, pgBackRest provides backup catalog management and Point-in-Time Recovery (PiTR) for reliable, specific disaster recovery.
- Built-in replication lag monitoring: PostgreSQL provides native, accurate replication lag tracking through `pg_stat_wal_receiver` and WAL LSN comparison, without requiring external heartbeat tooling. PMM surfaces this data via the `pg_custom_stat_wal_receiver_lag_bytes` metric (sourced from `postgres_exporter`). Teams migrating from MySQL (where external tools like pt-heartbeat are common for lag measurement) gain this capability out of the box with PostgreSQL. *(Internal validation: PG experts thread, Jan 2026, PT-2030. Confirmed via Sysbench TPCC R/W workload + PMM analysis.)*

**Security, Sovereignty, and Compliance**
- End-to-end encryption and governance: Percona integrates pg_tde for transparent data-at-rest encryption, and supports LDAP, Kerberos and TLS for centralized authentication. pgAudit and Percona's documented CVE process strengthen auditability for GDPR, HIPAA, and PCI-DSS frameworks.
- Validated open source integrity: Every build is open for audit and inspection, ensuring compliance without dependence on opaque vendor frameworks.

**Adaptability for Emerging Workloads**
- Cloud-native operations: The Percona Operator for PostgreSQL automates deployment, scaling, and failover in Kubernetes environments, delivering consistent governance and portability across any cloud.
- AI and analytics readiness: The 2024 "State of PostgreSQL" survey reports that 55.3% of respondents now use PostgreSQL with AI-enabled tools (e.g., vector search). Percona Distribution for PostgreSQL supports modern workloads through extensions like pgvector (for embeddings and vector search). Distribution 18.3.1 (Mar 2026) ships pgvector 0.8.2, pg_stat_monitor 2.3.2, pg_tde 2.1.2, and addresses five CVEs (CVE-2026-2003 through CVE-2026-2007).
