# Percona Coroot Edition: Partner messaging

## Percona Coroot Edition {#percona-coroot-edition}

Coroot is a technology partner. [Percona Coroot Edition](https://www.percona.com/coroot/) is in early access. Percona does not maintain the Coroot project.

Coroot follows the application, network, and infrastructure and recommends how to fix the incident. Percona Monitoring and Management (PMM) remains the pane for database health, queries, replication, and engine internals. The customer gets both in one motion, and can tell whether the cause is the application, the network, or the database.

Coroot runs on-premises, in your VPC, or fully air-gapped. Telemetry stays where you install it.

One agent, with no manual instrumentation, collects metrics, logs, traces, and profiles continuously. Install is measured in minutes, with no per-service setup. For a database incident, install it on the database hosts and on the applications that call the database. On Kubernetes it keeps that view through rescaling, node changes, and reconfiguration, past 1,000 nodes.

### Better together

**Optimized TCO**

Coroot Community is free, self-hosted, and open source under Apache 2.0. Its limited monthly AI root cause analysis runs through Coroot Cloud. PMM is free and open source for the database pane. PMM and Coroot together cover the database and the application, network, and infrastructure around it. Percona Coroot Edition adds unlimited AI root cause analysis and SSO and RBAC. Contact Percona either way. Percona routes database issues on the Expert Support agreement and Coroot product issues to Coroot.

**Performance and Reliability at Scale**

PMM keeps query, replication, and engine diagnosis on the database. Coroot traces the incident from the affected service through the network and infrastructure to a cause and recommends a fix, for PostgreSQL, MongoDB-compatible workloads, and MySQL. Coroot follows an application failure to the database, and follows a database symptom out to the network path in front of it. What Coroot inspects inside each database is in the Coroot docs for [PostgreSQL](https://docs.coroot.com/databases/postgres/), [MongoDB](https://docs.coroot.com/databases/mongodb/), and [MySQL](https://docs.coroot.com/databases/mysql/). PMM is recommended for Valkey, Redis, and MariaDB Server visibility.

**Security, Sovereignty, and Compliance**

Percona Coroot Edition adds SSO and RBAC, so access to that telemetry can be limited to the people who should see it. The customer points AI root cause analysis at a model provider, or at an OpenAI-compatible endpoint inside their own network.

**Adaptability for Emerging Workloads**

You do not reconfigure monitoring every time Kubernetes rescales. One agent keeps working past 1,000 nodes. That is the environment small platform teams meet when they run databases on Percona Operators without a dedicated DBA. When new application traffic looks like a database failure, PMM shows the queries and Coroot shows the path outside the database.

### Sales enablement

- **Qualification framework:** Use Coroot when developers, platform engineers, or SREs need the path across the application, network, and database. Use PMM when DBAs need engine internals. Pair them when the customer needs both. PMM stays the database pane.
- **Discovery questions:**
  - When the database looks healthy, where does the investigation stop: the application, the network, or the infrastructure?
  - Who has to decide whether the cause is the code, the network, or the database, and do they have a DBA to call?
  - Does observability have to stay on-premises or air-gapped?
- **Fit indicators:** Strongest for platform and SRE teams on Kubernetes, and for developers who need to know whether the cause is their code, the network, or the database. Strong fit when telemetry has to stay on-premises or air-gapped, including in finance, healthcare, and government. It also runs on virtual machines and bare metal. A single database with no surrounding services is a weaker fit.
- **Supported technologies:** Early access covers PostgreSQL, MongoDB-compatible workloads, and MySQL, on Kubernetes, virtual machines, and bare metal. The Coroot server runs on Linux. A Windows agent can send metrics, logs, and DNS and network telemetry. Protocol tracing and continuous profiling stay on Linux. PMM is recommended for Valkey, Redis, and MariaDB Server visibility.
