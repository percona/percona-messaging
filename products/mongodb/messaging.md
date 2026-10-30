# Percona for MongoDB: Messaging

## Percona for MongoDB {#percona-for-mongodb}

For organizations running MongoDB workloads requiring performance, reliability, security, sovereignty, and compliance across on-premises, cloud, and hybrid environments, Percona Server for MongoDB provides a production-tested, self-managed platform that extends MongoDB Community Edition with enterprise-grade capabilities.

MongoDB Community Edition is licensed under the Server Side Public License (SSPL) (source-available), and Percona Server for MongoDB inherits this license for the database server. However, Percona-developed technologies and management components around the database, including Percona Backup for MongoDB, Percona ClusterSync for MongoDB, and Percona Operator for MongoDB, are released under the Apache 2.0 open source license. This keeps the operations stack auditable and portable while maintaining compatibility with MongoDB APIs and database clients.

Compared with MongoDB Enterprise Advanced or Atlas, Percona focuses on self-managed deployments backed by Percona's operational tooling and 24×7 Expert Support. Monitoring, backup, and automation are handled by Percona components deployed in customer-controlled environments.

PMM provides observability for backup operations and backup health indicators, while backup execution and policy management remain in dedicated Percona backup tooling.

### Customer Challenges and Value Alignment: MongoDB

**Optimized TCO**

- **High licensing costs and vendor lock-in:** MongoDB Enterprise Advanced and Atlas introduce restrictive licensing and escalating subscription fees. Percona Server for MongoDB removes license cost while retaining major enterprise features, cutting total database spend by up to 50%. [Sailthru by Zeta](https://www.percona.com/customer-story/sailthru/) cut more than $1 million annually in MongoDB licensing and backup renewal costs by migrating from MongoDB Enterprise to Percona Server for MongoDB as a drop-in replacement with no application changes, and moved backup to [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/). [BBVA](https://www.percona.com/customer-story/bbva-migrates-document-oriented-database-nosql-workloads-to-percona-avoiding-license-costs-and-lock-in/) migrated document-oriented workloads to Percona Server for MongoDB to avoid license costs and vendor lock-in.
- **Migration with expert-led cutover:** Teams moving from MongoDB Enterprise Advanced or Atlas need production to stay up while they set up Percona. [Percona ClusterSync for MongoDB](https://docs.percona.com/percona-clustersync-for-mongodb/) copies data to the new cluster and keeps it updated. You can run multiple ClusterSync instances with automatic active-standby failover during continuous change-stream replication so a host or pod failure does not stop the sync; a single instance behaves as before, and starting a second instance enables failover. High availability covers the replication phase, not the initial clone. When you are ready, you move the app to the new cluster. On Kubernetes, the Percona Operator for MongoDB can run ClusterSync for you. Experts help plan and execute the migration.

**Performance and Reliability at Scale**

- **Faster recovery and replica sync:** Manual HA/DR operations create business risk as well as labor cost: outages during scale-out or node replacement, prolonged recovery windows, and replication catch-up lag can interrupt revenue-critical workloads while consuming scarce DBA time. Percona Server for MongoDB includes file copy-based initial sync to shorten recovery and lighten day-two work so topology changes stay reliable.
- **Low-latency in-memory workloads:** Teams running cache-like, session, or real-time data that must stay hot in RAM need in-memory storage without MongoDB Enterprise Advanced licensing costs. Percona Server for MongoDB includes the [Percona Memory Engine](https://docs.percona.com/percona-server-for-mongodb/8.0/inmemory.html), a WiredTiger configuration that keeps the working set in memory for faster reads and writes on infrastructure you control.
- **Deployment, backup, and restore automation:** The Percona Operator for MongoDB and [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/) automate deployment and backup schedules on infrastructure you control; restore runs through the Operator and PBM when teams initiate it after an incident. ExpertOps supports predictable uptime and capacity planning. Percona Backup for MongoDB supports logical, physical, snapshot-based, and incremental backups with point-in-time recovery, selective backups that include users and roles, and storage profiles for multi-storage targets, so teams can align backup design with recovery time and recovery point objectives and strengthen restore confidence in regulated environments.
- **Major-version upgrades with controlled cutover:** Teams on end-of-life MongoDB releases need a supported path to current versions without relying on a single high-stakes maintenance window. [Percona ClusterSync for MongoDB](https://docs.percona.com/percona-clustersync-for-mongodb/) supports cross-major-version replication and controlled cutover across [supported upgrade paths](https://docs.percona.com/percona-clustersync-for-mongodb/system-requirements.html), including 6.x to 7.x, 6.x to 8.x, and 7.x to 8.x. Percona experts help plan replication, performance validation, and cutover sequencing so teams reach an actively supported release (including from 6.0.17+ where supported) with predictable uptime.

**Security, Sovereignty, and Compliance**

- **Encrypted source-available database with enterprise controls:** Community builds lack enterprise controls for regulated industries. Percona Server for MongoDB includes transparent data-at-rest encryption with external key management (KMIP-compatible providers, HashiCorp Vault, OpenBao), advanced authentication and authorization integrations (LDAP/AD, Kerberos, OpenID Connect, AWS IAM), auditing, and log redaction, supporting GDPR, HIPAA, and PCI-DSS requirements on infrastructure customers operate.
- **Enterprise directory auth continuity:** [MongoDB deprecated LDAP authentication and authorization in MongoDB 8.0](https://www.mongodb.com/docs/manual/core/ldap-deprecation/) and plans removal in a future major release; MongoDB Enterprise Advanced and Atlas are dropping LDAP support. Percona Server for MongoDB maintains long-term LDAP/AD support on [supported releases](https://www.percona.com/services/policies/percona-software-support-lifecycle) so teams keep existing directory identity infrastructure without forced migration to vendor-specific identity platforms. OpenID Connect remains available where teams want modern federated auth alongside LDAP.
- **FIPS 140-3 compliance:** Federal, healthcare, and financial programs often require FIPS 140-3 validated cryptographic modules for database network TLS and authentication. Percona Server for MongoDB includes native support for running a FIPS 140-3-compliant OpenSSL module for data encryption in transit and at rest. It also means that TLS, SCRAM, and X.509 authentication can use validated OpenSSL cryptography on supported platforms. Teams can run on self-managed infrastructure they control while configuring FIPS mode to support program requirements; full compliance still depends on OS, certificates, auth choices, and any at-rest encryption controls your auditors require.
- **Supply-chain transparency with SBOM and VEX:** Security and compliance teams need an inventory of what ships in each database build and clearer exploitability signal than raw CVE lists alone. Percona Server for MongoDB includes a CycloneDX Software Bill of Materials with each release and publishes OpenVEX statements so teams can document dependencies and filter noise during reviews ([SBOM documentation](https://docs.percona.com/percona-server-for-mongodb/8.0/sbom.html)).

**Adaptability for Emerging Workloads**

- **Full-text, vector, and hybrid search:** [Percona Search for MongoDB](#percona-search-for-mongodb) adds a supported, integrated search tier to self-managed MongoDB. Local-first automatic embeddings keep document text in the cluster when a local provider is configured. The Percona Operator for MongoDB manages deployment and separate search-tier scaling, while Percona Backup for MongoDB and PMM cover index backup and observability. The software is free to use, with support available as an optional add-on to a Percona Support contract.
- **Platform portability for infrastructure refresh:** Teams standardizing on current enterprise Linux images, including ARM, need database packages that match those platforms. Percona Server for MongoDB ships packages for RHEL 10 and its derivatives and for Debian 13 on x86_64 and ARM64 ([supported platforms](https://www.percona.com/services/policies/percona-software-support-lifecycle)). Percona builds and tests Debian 13 packages independently, while upstream MongoDB Community lists only Debian 13 on the x64 architecture, with MongoDB 9.0 as the first supported platform.
- **Multi-environment operations:** The Percona Operator for MongoDB helps you create and grow MongoDB clusters on Kubernetes across clouds, while PMM shows health and performance across those clusters. The same Operator model works on Rancher (RKE2) and on ARM servers. It can also grow disk space when needed and make restores safer when you move between environments. Minsait moved major telecom workloads to Percona Server for MongoDB on Google Cloud with the Operator, cut cost, and kept more control across Kubernetes.

### Percona Search for MongoDB {#percona-search-for-mongodb}

Percona Search for MongoDB is Percona's supported, integrated version of `mongot`, MongoDB®'s vector, full-text, and hybrid search engine, built on Percona Server for MongoDB (PSMDB). It is free to use. Support is an optional add-on to a Percona Support contract.

Percona Search adds local-first automatic embeddings, Operator-managed deployment, index backup, and PMM observability. It is for teams running MongoDB themselves that need production search but cannot send document text to a third-party embedding service. When a local provider is configured, document text stays in the cluster, the embedding path has no per-token charge, and the stack can run without outbound traffic.

#### Value proposition

Run vector, full-text, and hybrid search with MongoDB data on infrastructure you control. Keep embedding inference in the cluster, manage the search tier with the database control plane, and restore indexes without a full re-index. Use the software at no cost, with one optional support add-on for the full stack.

#### Messaging

- **Keep document text in the cluster.** MongoDB's automatic embedding pipeline requires a Voyage AI key in both Enterprise Advanced and Community Edition, and every embedding call sends document text to Voyage's cloud. MongoDB has no first-class local inference path. Percona Search runs inference inside the cluster by default.
- **Local inference without another embedding service.** Voyage AI offers on-premises deployment, which avoids cloud egress but retains a separate enterprise contract and leaves GPU capacity and model upkeep to the customer. Percona supports open-weight providers for local inference, with no separate embedding service to buy.
- **Operate the search tier with the database.** Enterprise Advanced and MongoDB Controllers for Kubernetes cover deployment and lifecycle, but index lifecycle, backup, recovery, autoscaling, and observability remain customer responsibilities. Percona Search integrates with the Percona Operator for MongoDB, Percona Backup for MongoDB (PBM), and Percona Monitoring and Management (PMM), extending the database control plane to the search tier.
- **Use infrastructure you already run.** Voyage billing grows with corpus size and query volume. Local open-weight models run on fixed, amortized hardware. Percona Search is free to use; support is an optional add-on to a Percona Support contract, not a condition of running the software.

#### Unique benefits

| Benefit | Why it matters |
| --- | --- |
| **No embedding paywall, no data egress** | Local-first automatic embeddings keep document text in the cluster when a local provider is configured. The local embedding path has no per-token charge. |
| **Air-gapped capable end to end** | With local providers configured, the stack can run without outbound traffic, including in environments where third-party API signup is blocked by sanctions, residency, or procurement policy. |
| **Full stack, one support add-on** | The Percona Operator for MongoDB, PBM, PMM, and PSMDB cover deployment, sharded clusters, backup, encryption, and audit. Search adds Atlas-equivalent management CRDs for the search tier. The software is free to use; an optional support add-on covers the stack together. |
| **Backup and restore without re-indexing** | Percona orchestrates native `mongot` blobstore snapshots. Restore does not require a full re-index. Index definitions are covered, manual setup is available, and the capability works with PSMDB, MongoDB Community Edition, and Enterprise Advanced. |
| **Enterprise security included** | LDAP, OIDC, Kerberos, FCBIS, audit logging, and encryption at rest are standard in PSMDB, with no extra charge. |
| **Predictable TCO** | Voyage billing scales with corpus size and query volume. Local open-weight models run on fixed, amortized hardware. |

#### Features that prove the benefits

| Capability | What it does | Benefit it proves | How to say it |
| --- | --- | --- | --- |
| **Local-first auto-embeddings** | Provides an OpenAI-compatible interface for Ollama, vLLM, LocalAI, in-cluster Hugging Face, OpenAI, and Azure OpenAI. It also provides a Hugging Face Inference API interface, hosted in the same shape as Voyage, with roughly 2,000 models instead of four at lower cost. | No embedding paywall, no data egress, and predictable TCO | Lead with the in-cluster path. The hosted interface is an option for teams not ready to run inference themselves. |
| **End-to-end data sovereignty** | With local providers configured, document text stays in the cluster by default and no outbound traffic is required. | Air-gapped capable | Use the GA data-flow audit as evidence for compliance audiences. |
| **Percona Operator integration** | Deploys the search tier alongside the MongoDB replica set and scales it separately from the database. | Full stack, one support add-on | Lead with management through the existing control plane. Separate search-tier scaling is the detail for architects. |
| **Backup and restore for vector indexes** | Orchestrates native `mongot` blobstore snapshots and covers index definitions. Manual setup is available. Compatible with MongoDB Community Edition, Enterprise Advanced, and PSMDB. | Backup and restore without re-indexing | Lead with no re-indexing on restore. Say index definitions are covered and manual setup is available. Do not state unmeasured time savings. |
| **PMM dashboards and alerts** | Monitors recall regression, JVM heap, Lucene cache, sync lag, and embedding provider health. | Full stack, one support add-on | Lead with recall regression, followed by JVM heap, Lucene cache, sync lag, and embedding provider health. |
| **Enterprise security baseline** | PSMDB includes LDAP, OIDC, Kerberos, FCBIS, audit logging, and encryption at rest with no extra charge. | Security included, not unlocked | Always say included, never available. Contrast with capabilities sold behind a separate tier. |

### Sales enablement

**Elevator pitch**

Percona for MongoDB is the self-managed way off MongoDB Enterprise Advanced and Atlas. You get security controls, backup, migration tools, Kubernetes automation, and Expert Support on infrastructure you control, without proprietary licensing.

**Best-fit customer profiles**

- Teams leaving MongoDB Enterprise Advanced or Atlas for lower cost, less lock-in, and self-managed security (LDAP, encryption, audit, FIPS)
- Platform and SRE teams who want MongoDB Day 2 work automated on Kubernetes
- Teams that need production full-text, vector, or hybrid search on MongoDB data they already keep, especially when document text must stay in the cluster

**Discovery questions**

- What is driving cost or renewal pressure on MongoDB Enterprise Advanced or Atlas today?
- Do you still need LDAP/AD for database login, and what will you do as MongoDB removes it?
- How do you migrate or upgrade MongoDB without a long production outage?
- Do long-running ClusterSync migrations need automatic failover if the sync host or pod fails during continuous replication?
- Are you refreshing onto RHEL 10, Debian 13, or ARM while keeping MongoDB self-managed?
- If you run MongoDB on Kubernetes, which Day 2 tasks are still manual? (backup, restore, scaling, upgrades, failover)
- Does document text need to stay inside your MongoDB cluster during embedding, and do you need production vector, full-text, or hybrid search?
- Where would Expert Support or ExpertOps help most: design, migration, or day-to-day operations?
- Do you have upcoming projects that need consulting, professional services, or training? (architecture review, migration, performance work, team enablement)

**Public resources**

- [Percona Software for MongoDB](https://www.percona.com/mongodb/software/)
- [Sailthru by Zeta customer story](https://www.percona.com/customer-story/sailthru/)
- [BBVA customer story](https://www.percona.com/customer-story/bbva-migrates-document-oriented-database-nosql-workloads-to-percona-avoiding-license-costs-and-lock-in/)
- [Compare MySQL, MongoDB, PostgreSQL, and MariaDB](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
- [Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/index.html)
- [Percona ClusterSync for MongoDB](https://docs.percona.com/percona-clustersync-for-mongodb/)
