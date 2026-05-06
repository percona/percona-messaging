# Percona for MongoDB: Messaging

## Percona for MongoDB {#percona-for-mongodb}

For organizations running MongoDB workloads requiring performance, reliability, security, sovereignty, and compliance across on-premises, cloud, and hybrid environments, Percona Server for MongoDB provides a production-tested, self-managed platform that extends MongoDB Community Edition with enterprise-grade capabilities.

MongoDB Community Edition is licensed under the Server Side Public License (SSPL) (source-available), and Percona Server for MongoDB inherits this license for the database server. However, Percona-developed technologies and management components around the database, including Percona Backup for MongoDB, Percona ClusterSync for MongoDB, and Percona Operator for MongoDB, are released under the Apache 2.0 open source license. This keeps the operations stack auditable and portable while maintaining compatibility with MongoDB APIs and database clients.

Compared with MongoDB Enterprise Advanced or Atlas, Percona focuses on self-managed deployments backed by Percona's operational tooling and 24×7 support. Monitoring, backup, and automation run through Percona components deployed in customer-controlled environments, not Atlas-only integrations.

PMM provides observability for backup operations and backup health indicators, while backup execution and policy management remain in dedicated Percona backup tooling.

MongoDB Vector Search and Full-Text Search are powered by `mongot`, a separate JVM-based search engine integrated into MongoDB's indexing and query workflows. With upstream Vector Search now source-available under SSPL and in public preview for community usage, Percona's plan is to validate and publish early builds (8.3 as a technical preview), then ship a fully integrated, observable experience (Operator + PMM dashboards/metrics, plus operational guidance) aligned to MongoDB 9.0 GA timing (estimated Sep/Oct 2026).

### Customer Challenges and Value Alignment: MongoDB

**Optimized TCO**

- High licensing costs and vendor lock-in: MongoDB Enterprise Advanced and Atlas introduce restrictive licensing and escalating subscription fees. Percona Server for MongoDB removes license cost while retaining major enterprise features, cutting total database spend by up to 50%. BBVA (global bank) chose Percona for its MongoDB workload migration to avoid license costs.

**Performance and Reliability at Scale**

- Operational complexity: Scaling and maintaining HA/DR clusters consumes significant DBA effort. Percona Server for MongoDB includes in-memory storage engine support and file copy-based initial sync, reducing recovery times and operational overhead. The Percona Kubernetes Operator for MongoDB and Percona Backup for MongoDB automate deployment, backups, and failover, while ExpertOps ensures predictable uptime and capacity planning. [Percona Backup for MongoDB 2.13.0 (2026-03-03)](https://docs.percona.com/percona-backup-mongodb/release-notes/2.13.0.html) strengthens backup operations with Workload Identity Federation for GCS (no long-lived service account keys), selective backups that include users and roles, and uninterrupted PITR during logical backups on external storage profiles. Together, these changes reduce security exposure and improve restore reliability for regulated and multi-storage environments.
- Lower migration effort and risk: Percona ClusterSync for MongoDB helps teams migrate to Percona Server for MongoDB by automating data sync and coordinating a controlled cutover. [Percona ClusterSync for MongoDB 0.8.0 (2026-04-06)](https://docs.percona.com/percona-clustersync-for-mongodb/release-notes/0.8.0.html) introduces document-level parallel replication and an async bulk write pipeline, delivering 3× to 8× faster processing than prior versions under tested conditions. This helps teams reduce migration windows and replication lag during cutover.

**Security, Sovereignty, and Compliance**

- Encrypted open source: Community builds lack enterprise controls for regulated industries. Percona Server for MongoDB includes transparent data-at-rest encryption with external key management (KMIP-compatible providers, HashiCorp Vault, OpenBao), advanced authentication and authorization integrations (LDAP/AD, Kerberos, OpenID Connect, AWS IAM), FIPS 140-2–validated cryptographic mode, auditing, and log redaction to support GDPR, HIPAA, and PCI-DSS requirements.

**Adaptability for Emerging Workloads**

- Multi-environment operations: The Percona Operator for MongoDB automates provisioning and scaling across Kubernetes and multi-cloud environments, while PMM provides cross-cluster observability and performance analytics. Minsait migrated tier-one telecom workloads to Percona Server for MongoDB on Google Cloud using the Percona Operator, achieving significant cost savings and operational freedom across Kubernetes environments. [Percona Operator for MongoDB 1.22.0 (2026-02-25)](https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.22.0.html) adds automatic PVC resizing and restore remapping for clusters with different replica set names, plus native MinIO backup support for S3-compatible storage. These features reduce disk-capacity incidents, improve restore reliability across environment changes, and stabilize backup connectivity for common object stores. See the [Operator release index](https://docs.percona.com/percona-operator-for-mongodb/RN/index.html).
- Vector and full-text search readiness: Percona is preparing a MongoDB Vector Search stack based on upstream `mongot`, focused on packaging, orchestration, and observability for self-managed deployments (aligned to MongoDB 9.0 GA timing).
