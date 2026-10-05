# Percona Coroot Edition: Partner messaging

## Percona Coroot Edition {#percona-coroot-edition}

Coroot is a technology partner. [Percona Coroot Edition](https://www.percona.com/coroot/) is in early access. Percona does not maintain the Coroot project.

Better together with Percona Monitoring and Management (PMM): Coroot follows the application, network, and infrastructure and recommends how to fix the incident. PMM remains the pane for database health, queries, replication, and engine internals. The customer gets both in one motion, and can tell whether the cause is the application, the network, or the database.

One agent, with no manual instrumentation, collects metrics, logs, traces, and profiles continuously. Install is measured in minutes, with no per-service setup. On Kubernetes it keeps that view through rescaling, node changes, and reconfiguration, past 1,000 nodes.

### Better together

**Optimized TCO**

Coroot community software is free, self-hosted, and open source under Apache 2.0. PMM is free and open source for the database pane. Together, the customer covers the database and the surrounding stack without a separate commercial monitoring contract for each layer. Percona Coroot Edition is the paid edition when the team needs unlimited AI root cause analysis, SSO and RBAC, and dedicated support.

**Performance and Reliability at Scale**

PMM keeps query, replication, and engine diagnosis on the database. Coroot traces the incident from the affected service through the network and infrastructure to a cause and recommends a fix, for PostgreSQL, MongoDB-compatible workloads, and MySQL. The customer spends less time deciding which layer failed.

**Security, Sovereignty, and Compliance**

Both stay in the customer's environment, including on-premises, in a VPC, and in air-gapped deployments, so observability data does not have to leave infrastructure the customer controls. Percona Coroot Edition adds SSO and RBAC on top of that.

**Adaptability for Emerging Workloads**

The same agent holds visibility through Kubernetes rescaling and node changes past 1,000 nodes. That is the environment small platform teams meet when they run databases on Percona Operators without a dedicated DBA. When new application traffic looks like a database failure, PMM shows the queries and Coroot shows the path outside the database.

### Engines

- **PostgreSQL:** Coroot explains autovacuum, checkpointer, transaction ID wraparound, and backup or replication problems, so teams get the cause and a recommended fix rather than another chart.
- **MongoDB-compatible workloads:** Outside-in query and latency signals sit alongside WiredTiger cache, replication lag, the oplog window, and index-change tracking.
- **MySQL:** Schema and configuration change tracking is still in development. Early access still covers MySQL environments for the surrounding-stack trace.
- **Valkey, Redis, and MariaDB Server:** Coroot coverage for Valkey and Redis is on the roadmap. Until then, that visibility stays on PMM, along with MariaDB Server.

### Editions

Coroot community software includes core automatic telemetry and a limited amount of AI root cause analysis per month.

Percona Coroot Edition adds unlimited AI root cause analysis, SSO and RBAC, and dedicated support. That dedicated support is part of the edition. It is not an Expert Support response-time commitment.

Still in development for the full edition: filing a Percona Support case from Coroot with diagnostics attached, deep database root cause analysis, and AI analysis powered by the Percona Knowledge Base.

### Sales enablement

- **Qualification framework:** Use this module when the incident is not explained by the database pane alone. Pair Coroot with PMM. PMM stays the database pane.
- **Discovery questions:**
  - When the database checks out, where does the incident investigation stop: the application, the network, or the infrastructure?
  - Who has to decide whether the cause is the code, the network, or the database, and do they have a DBA to call?
  - Does observability have to stay on-premises or air-gapped?
- **Fit indicators:** Strongest for platform and SRE teams on Kubernetes, and for teams that need a recommended fix across the surrounding stack for PostgreSQL, MongoDB-compatible workloads, or MySQL.
- **Supported technologies:** Early access covers PostgreSQL, MongoDB-compatible workloads, and MySQL, on Kubernetes, virtual machines, and bare metal. MySQL schema and configuration change tracking is still in development. Valkey, Redis, and MariaDB Server visibility stays on PMM.
