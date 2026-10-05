# Percona Coroot Edition: Partner messaging

## Percona Coroot Edition {#percona-coroot-edition}

Coroot is a technology partner. [Percona Coroot Edition](https://www.percona.com/coroot/) is in early access. Percona does not maintain the Coroot project.

Coroot follows the application, network, and infrastructure and recommends how to fix the incident. Percona Monitoring and Management (PMM) remains the pane for database health, queries, replication, and engine internals. The customer gets both in one motion, and can tell whether the cause is the application, the network, or the database.

Coroot runs on-premises, in your VPC, or fully air-gapped. Telemetry stays where you install it.

One agent, with no manual instrumentation, collects metrics, logs, traces, and profiles continuously. Install is measured in minutes, with no per-service setup. On Kubernetes it keeps that view through rescaling, node changes, and reconfiguration, past 1,000 nodes.

### Better together

**Optimized TCO**

Coroot community software is free, self-hosted, and open source under Apache 2.0, with a limited amount of AI root cause analysis per month. PMM is free and open source for the database pane. PMM and Coroot together cover the database and the application, network, and infrastructure around it, without a second monitoring contract. Percona Coroot Edition adds unlimited AI root cause analysis and SSO and RBAC. Buying Percona Coroot Edition includes support for Coroot. Expert Support response times are a separate agreement.

**Performance and Reliability at Scale**

PMM keeps query, replication, and engine diagnosis on the database. Coroot traces the incident from the affected service through the network and infrastructure to a cause and recommends a fix, for PostgreSQL, MongoDB-compatible workloads, and MySQL. What Coroot inspects inside each database is in the Coroot docs for [PostgreSQL](https://docs.coroot.com/databases/postgres/), [MongoDB](https://docs.coroot.com/databases/mongodb/), and [MySQL](https://docs.coroot.com/databases/mysql/). PMM is recommended for Valkey, Redis, and MariaDB Server visibility.

**Security, Sovereignty, and Compliance**

Percona Coroot Edition adds SSO and RBAC, so access to that telemetry can be limited to the people who should see it.

**Adaptability for Emerging Workloads**

You do not reconfigure monitoring every time Kubernetes rescales. One agent keeps working past 1,000 nodes. That is the environment small platform teams meet when they run databases on Percona Operators without a dedicated DBA. When new application traffic looks like a database failure, PMM shows the queries and Coroot shows the path outside the database.

### Sales enablement

- **Qualification framework:** Use this module when the incident is not explained by the database pane alone. Pair Coroot with PMM. PMM stays the database pane.
- **Discovery questions:**
  - When the database checks out, where does the incident investigation stop: the application, the network, or the infrastructure?
  - Who has to decide whether the cause is the code, the network, or the database, and do they have a DBA to call?
  - Does observability have to stay on-premises or air-gapped?
- **Fit indicators:** Strongest for platform and SRE teams on Kubernetes, and for teams that need a recommended fix across the surrounding stack for PostgreSQL, MongoDB-compatible workloads, or MySQL.
- **Supported technologies:** Early access covers PostgreSQL, MongoDB-compatible workloads, and MySQL, on Kubernetes, virtual machines, and bare metal. PMM is recommended for Valkey, Redis, and MariaDB Server visibility.
