# Percona for MongoDB: Messaging

## Percona for MongoDB {#percona-for-mongodb}

For organizations running MongoDB workloads requiring performance, reliability, security, sovereignty, and compliance across on-premises, cloud, and hybrid environments, Percona Server for MongoDB provides a production-tested, self-managed platform that extends MongoDB Community Edition with enterprise-grade capabilities.

MongoDB Community Edition is licensed under the Server Side Public License (SSPL) (source-available), and Percona Server for MongoDB inherits this license for the database server. However, Percona-developed technologies and management components around the database, including Percona Backup for MongoDB, Percona ClusterSync for MongoDB, and Percona Operator for MongoDB, are released under the Apache 2.0 open source license. This keeps the operations stack auditable and portable while maintaining compatibility with MongoDB APIs and database clients.

Compared with MongoDB Enterprise Advanced or Atlas, Percona focuses on self-managed deployments backed by Percona's operational tooling and 24×7 Expert Support. Monitoring, backup, and automation are handled by Percona components deployed in customer-controlled environments.

PMM provides observability for backup operations and backup health indicators, while backup execution and policy management remain in dedicated Percona backup tooling.

### Customer Challenges and Value Alignment: MongoDB

**Optimized TCO**

- **High licensing costs and vendor lock-in:** MongoDB Enterprise Advanced and Atlas introduce restrictive licensing and escalating subscription fees. Percona Server for MongoDB removes license cost while retaining major enterprise features, cutting total database spend by up to 50%. [Sailthru by Zeta](https://www.percona.com/customer-story/sailthru/) cut more than $1 million annually in MongoDB licensing and backup renewal costs by migrating from MongoDB Enterprise to Percona Server for MongoDB as a drop-in replacement with no application changes, and moved backup to [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/). [BBVA](https://www.percona.com/customer-story/bbva-migrates-document-oriented-database-nosql-workloads-to-percona-avoiding-license-costs-and-lock-in/) migrated document-oriented workloads to Percona Server for MongoDB to avoid license costs and vendor lock-in.
- **Migration with expert-led cutover:** Teams moving from MongoDB Enterprise Advanced, Atlas, or Community need production to stay up while they set up Percona. Percona ClusterSync for MongoDB copies data to the new cluster and keeps it updated. When you are ready, you move the app to the new cluster. On Kubernetes, the Percona Operator for MongoDB can run ClusterSync for you. Experts help plan and execute the migration.

**Performance and Reliability at Scale**

- **Faster recovery and replica sync:** Manual HA/DR operations create business risk as well as labor cost: outages during scale-out or node replacement, prolonged recovery windows, and replication catch-up lag can interrupt revenue-critical workloads while consuming scarce DBA time. Percona Server for MongoDB includes file copy-based initial sync to shorten recovery and lighten day-two work so topology changes stay reliable.
- **Low-latency in-memory workloads:** Teams running cache-like, session, or real-time data that must stay hot in RAM need in-memory storage without MongoDB Enterprise Advanced licensing costs. Percona Server for MongoDB includes the [Percona Memory Engine](https://docs.percona.com/percona-server-for-mongodb/8.0/inmemory.html), a WiredTiger configuration that keeps the working set in memory for faster reads and writes on infrastructure you control.
- **Deployment, backup, and restore automation:** The Percona Operator for MongoDB and [Percona Backup for MongoDB](https://docs.percona.com/percona-backup-mongodb/) automate deployment and backup schedules on infrastructure you control; restore runs through the Operator and PBM when teams initiate it after an incident. ExpertOps supports predictable uptime and capacity planning. Percona Backup for MongoDB supports logical, physical, snapshot-based, and incremental backups with point-in-time recovery, selective backups that include users and roles, and storage profiles for multi-storage targets, so teams can align backup design with recovery time and recovery point objectives and strengthen restore confidence in regulated environments.
- **Major-version upgrades with controlled cutover:** Teams on end-of-life MongoDB releases need a supported path to current versions without relying on a single high-stakes maintenance window. [Percona ClusterSync for MongoDB](https://docs.percona.com/percona-clustersync-for-mongodb/) supports cross-major-version replication and controlled cutover from [Percona ClusterSync for MongoDB 0.9.0 (2026-06-01)](https://docs.percona.com/percona-clustersync-for-mongodb/release-notes/0.9.0.html) across [supported upgrade paths](https://docs.percona.com/percona-clustersync-for-mongodb/system-requirements.html), including 6.x to 7.x, 6.x to 8.x, and 7.x to 8.x. Percona experts help plan replication, performance validation, and cutover sequencing so teams reach an actively supported release (including from 6.0.17+ where supported) with predictable uptime.

**Security, Sovereignty, and Compliance**

- **Encrypted source-available database with enterprise controls:** Community builds lack enterprise controls for regulated industries. Percona Server for MongoDB includes transparent data-at-rest encryption with external key management (KMIP-compatible providers, HashiCorp Vault, OpenBao), advanced authentication and authorization integrations (LDAP/AD, Kerberos, OpenID Connect, AWS IAM), auditing, and log redaction, supporting GDPR, HIPAA, and PCI-DSS requirements on infrastructure customers operate.
- **Enterprise directory auth continuity:** [MongoDB deprecated LDAP authentication and authorization in MongoDB 8.0](https://www.mongodb.com/docs/manual/core/ldap-deprecation/) and plans removal in a future major release; MongoDB Enterprise Advanced and Atlas are dropping LDAP support. Percona Server for MongoDB maintains long-term LDAP/AD support on [supported releases](https://www.percona.com/services/policies/percona-software-support-lifecycle) so teams keep existing directory identity infrastructure without forced migration to vendor-specific identity platforms. OpenID Connect remains available where teams want modern federated auth alongside LDAP.
- **FIPS 140-3 compliance:** Federal, healthcare, and financial programs often require FIPS 140-3 validated cryptographic modules for database network TLS and authentication. Percona Server for MongoDB includes native support for running a FIPS 140-3-compliant OpenSSL module for data encryption in transit and at rest. It also means that TLS, SCRAM, and X.509 authentication can use validated OpenSSL cryptography on supported platforms. Teams can run on self-managed infrastructure they control while configuring FIPS mode to support program requirements; full compliance still depends on OS, certificates, auth choices, and any at-rest encryption controls your auditors require.

**Adaptability for Emerging Workloads**

- **Full-text and vector search (Technical Preview):** Percona Search for MongoDB is an optional add-on for Percona Server for MongoDB that adds full-text and vector search so you can find data by meaning and build AI features on data you already keep, without a second search system, while apps keep the same connection string. In this Technical Preview you provide embeddings yourself; it needs Percona Server for MongoDB 8.3 and is for staging, not production. More Search capability is planned in upcoming releases. On Kubernetes, the Percona Operator for MongoDB can install and run Search with the cluster.
- **Multi-environment operations:** The Percona Operator for MongoDB helps you create and grow MongoDB clusters on Kubernetes across clouds, while PMM shows health and performance across those clusters. The same Operator model works on Rancher (RKE2) and on ARM servers. It can also grow disk space when needed and make restores safer when you move between environments. Minsait moved major telecom workloads to Percona Server for MongoDB on Google Cloud with the Operator, cut cost, and kept more control across Kubernetes.

### Sales enablement

**Elevator pitch**

Percona for MongoDB is the self-managed way off MongoDB Enterprise Advanced and Atlas. You get security controls, backup, migration tools, Kubernetes automation, and Expert Support on infrastructure you control, without proprietary licensing.

**Best-fit customer profiles**

- Teams leaving MongoDB Enterprise Advanced or Atlas for lower cost, less lock-in, and self-managed security (LDAP, encryption, audit, FIPS)
- Platform and SRE teams who want MongoDB Day 2 work automated on Kubernetes
- Teams trying search or AI features on MongoDB data they already keep (Technical Preview)

**Discovery questions**

- What is driving cost or renewal pressure on MongoDB Enterprise Advanced or Atlas today?
- Do you still need LDAP/AD for database login, and what will you do as MongoDB removes it?
- How do you migrate or upgrade MongoDB without a long production outage?
- If you run MongoDB on Kubernetes, which Day 2 tasks are still manual? (backup, restore, scaling, upgrades, failover)
- Are you trying search or AI features on self-managed MongoDB without a second search system? (Percona Search for MongoDB is Technical Preview on Percona Server for MongoDB 8.3; staging only.)
- Where would Expert Support or ExpertOps help most: design, migration, or day-to-day operations?
- Do you have upcoming projects that need consulting, professional services, or training? (architecture review, migration, performance work, team enablement)

**Public resources**

- [Percona Software for MongoDB](https://www.percona.com/mongodb/software/)
- [Sailthru by Zeta customer story](https://www.percona.com/customer-story/sailthru/)
- [BBVA customer story](https://www.percona.com/customer-story/bbva-migrates-document-oriented-database-nosql-workloads-to-percona-avoiding-license-costs-and-lock-in/)
- [Compare MySQL, MongoDB, PostgreSQL, and MariaDB](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
- [Percona Operator for MongoDB](https://docs.percona.com/percona-operator-for-mongodb/index.html)
- [Percona ClusterSync for MongoDB](https://docs.percona.com/percona-clustersync-for-mongodb/)
