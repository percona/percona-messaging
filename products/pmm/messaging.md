# Percona Monitoring and Management (PMM): Messaging

## Percona Monitoring and Management (PMM) {#percona-monitoring-and-management-pmm}

The data observability market is projected to grow from USD 3.15B in 2025 to USD 5.45B by 2030, per Mordor Intelligence. For database engineering and DevOps teams that need unified, database-level visibility into performance, health, and efficiency across multiple cloud and database environments, Percona Monitoring and Management (PMM) provides real-time, database-native observability built entirely on open standards and open source technologies. PMM integrates Grafana and VictoriaMetrics (Prometheus-compatible) with database-specific exporters. Query Analytics (QAN) provides query-level insight for MySQL, PostgreSQL, and MongoDB. Metrics-based visibility covers Valkey and Redis through dedicated dashboards for commands, memory, clients, latency, replication, and slowlog, as well as Kubernetes environments, including resource usage, availability, and operational health.

76% of companies in the 2025 Grafana 'State of Observability' survey report using open source observability tools; only 8% rely exclusively on commercial observability stacks. Unlike SaaS monitoring tools that abstract or restrict access to raw metrics, PMM is fully open source and deployable anywhere: on-prem, in the cloud, or integrated with Percona Operators for metric discovery. This provides consistent performance insight across environments, while keeping telemetry fully self-hosted and free of proprietary licensing.

### Customer Challenges and Value Alignment – PMM

**Optimized TCO**
- Unified observability without licensing costs: PMM uses fully open source components and is free to deploy for MySQL, PostgreSQL, MongoDB, Valkey, and Redis environments, eliminating recurring licensing fees. PMM's REST API (nodes, services, agents) allows programmatic access to cluster inventory. The Query Analytics (QAN) component exposes execution-plan, latency, and resource-usage data for MySQL, PostgreSQL and MongoDB. Organizations consolidate tooling and reduce spend while maintaining deep insight at the database layer.

**Performance and Reliability at Scale**
- Query-level and engine analytics: Teams can diagnose root causes faster by using the correct PMM surface for each engine. PMM's QAN component exposes query execution plans and latency for MySQL, PostgreSQL, and MongoDB, while Valkey and Redis observability is delivered through dedicated PMM dashboards and exporter metrics.
- Engine-native replication metrics: PMM leverages each engine's native capabilities for replication monitoring. For PostgreSQL, PMM reads `pg_stat_wal_receiver` data via custom queries in `postgres_exporter` (namespace: `pg_custom_stat_wal_receiver`, columns include `lag_bytes`), providing accurate replication lag measurement without requiring external heartbeat tools. This is a concrete advantage for MySQL-to-PostgreSQL migration stories: PostgreSQL's built-in replication instrumentation replaces the need for tools like pt-heartbeat. *(Source: `postgres_exporter/queries-hr.yml#L32`; validated Feb 2026.)*
- Advisors for proactive tuning: PMM includes Percona Advisors, a rules-based framework that runs best-practice checks for common performance and configuration issues, so organizations catch misconfigurations early, enforce best practices automatically, and reduce the operational burden on DBAs.

**Security, Sovereignty, and Compliance**
- Granular access and auditability: Role-based access control (RBAC) and integration with standard authentication systems ensure that visibility is properly segmented and traceable, supporting secure deployment at scale and simplifying audit preparation.
- Data sovereignty and transparency: PMM is fully open source and self-hostable in air-gapped or private environments. All components are open for inspection, ensuring alignment with sovereignty requirements and eliminating dependency on opaque SaaS monitoring platforms.

**Adaptability for Emerging Workloads**
- Kubernetes-native observability: PMM integrates directly with Percona Operators to automatically capture metrics from MySQL, PostgreSQL, and MongoDB clusters running in Kubernetes. Teams gain consistent visibility across hybrid and multi-cloud environments, improving reliability and cutting monitoring costs. Custom exporters are built-in to monitor additional systems such as Valkey/Redis or ProxySQL, providing a consistent observability model across hybrid and multi-cloud architectures.
