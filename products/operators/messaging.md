# Percona Kubernetes Operators: Messaging

## Operate and Observe {#operate-and-observe}

As organizations move stateful databases into Kubernetes and hybrid-cloud environments, the challenge shifts from simply running systems to observing and operating them efficiently and in real time. In this context, cloud native database operations means running databases with Kubernetes-native control planes, declarative lifecycle automation, and integrated observability that can scale across environments. Percona's open source operations stack unifies automation and observability across MySQL, PostgreSQL, and MongoDB clusters, reducing hands-on overhead and eliminating vendor lock-in.

Percona Operators define database clusters as Kubernetes Custom Resources (CRDs), automating common Day-1 and Day-2 operations (like deployment, scaling, backups, and failover) with declarative precision. After establishing a production foundation, the next challenge is operational scale and visibility. Percona Monitoring and Management (PMM) extends that automation with database-native observability, surfacing query analytics, system metrics, and performance trends through integrated Prometheus and Grafana dashboards.

Together, these components deliver a transparent, cloud-neutral operations layer that complements Percona's production-hardened databases, completing the lifecycle from run to optimize.

---

## Percona Kubernetes Operators (MySQL, PostgreSQL, MongoDB) {#percona-kubernetes-operators}

For engineering organizations managing stateful workloads across Kubernetes and hybrid infrastructures, Percona Kubernetes Operators provide a production-grade automation framework built for consistency and control. According to the Data on Kubernetes 2024 survey, databases remain the most common workload running on Kubernetes for the third year in a row. In Data on Kubernetes 2021 survey, operators were cited as the key automation mechanism for hybrid and multi-cloud deployments. Each Operator defines MySQL, PostgreSQL, and MongoDB clusters as Kubernetes Custom Resources (CRDs), integrating lifecycle management (provisioning, scaling, upgrades, backups, and failover) into the same declarative model developers already use for application workloads. This cloud native operating model helps teams standardize Day 1 and Day 2 work across engines while preserving infrastructure choice and governance control.

Modern teams need database operations that move at product speed without giving up control, visibility, or flexibility. Percona Operators let platform teams standardize deployment, scaling, backup, and recovery with Kubernetes-native automation that is fully declarative. Unlike public DBaaS offerings that can limit infrastructure and operating model choices, Percona Operators enable an in-house DBaaS approach that preserves transparency, portability, and governance across environments. Civo, a cloud-native provider, launched its DBaaS using the Percona Operator for MySQL rather than developing its own, accelerating time-to-market and cutting engineering overhead while maintaining open source flexibility. The result is deterministic operations, predictable performance, and full sovereignty over database environments across any cloud or on-prem infrastructure.

**Optimized TCO**

- Operational efficiency through automation: Managing database clusters manually in Kubernetes often consumes excessive engineering hours for deployment, scaling, and failover management. Percona Operators automate operations like backups, upgrades, and recovery through declarative Kubernetes Custom Resources (CRDs). This ensures every operation follows a consistent, version-controlled process, reducing manual error and stabilizing lifecycle costs. A 2024 DoK survey found that organizations running 75%+ of their data workloads in production on Kubernetes reported significant productivity gains when using operators. Percona Operator for MySQL based on Percona XtraDB Cluster provides configurable leader election for high-latency or resource-constrained clusters and carries forward backup queuing and automatic backup suspension during unhealthy cluster states. The Percona Operator for MySQL includes zstd backup compression, together reducing operational overload and backup storage waste.
- Freedom from DBaaS markup: Proprietary managed services like RDS or Atlas add convenience but impose per-instance fees and license gating. With Percona Operators, organizations can deploy production-grade databases on any Kubernetes environment, maintaining automation benefits without recurring license or subscription costs. [MySQL Operator backup workflows](https://docs.percona.com/percona-operator-for-mysql/pxc/backups.html) support object storage and persistent volumes, letting teams keep self-managed cost control while retaining production backup automation.

**Performance and Reliability at Scale**

- Predictable high availability: Operators embed replication and failover tuned per engine: synchronous multi-primary clustering via Percona XtraDB Cluster for MySQL, Patroni for PostgreSQL, and replica automation for MongoDB. For PostgreSQL on Kubernetes, Percona Operator for PostgreSQL ships Patroni 4.1.3 as the HA automation layer, coordinated through Kubernetes APIs, with validation tracked alongside distribution release cadence. For MySQL on Percona XtraDB Cluster, configurable HAProxy file-descriptor limits keep external health checks fast and stable when system limits are very high, reducing timeout-driven failover noise. Rolling upgrades and automated node recovery keep workloads online through failures, maintenance, and traffic spikes.
- Elastic scaling without disruption: Operators dynamically scale clusters using Kubernetes StatefulSets and engine-specific replication, scaling up during demand spikes and scaling down during low-utilization windows. This protects performance SLOs while reducing idle infrastructure spend, without risking downtime, data loss, or emergency reconfiguration. The Percona Operator for MongoDB and Percona Operator for MySQL based on Percona XtraDB Cluster automatically resize PVCs based on usage thresholds, preventing disk-full outages without manual intervention.
- Service mesh compatibility: Operators support the Kubernetes `appProtocol` field (e.g., `appProtocol: mongo`), enabling correct traffic recognition in service meshes like Istio. This ensures reliable cluster formation and secure mTLS connections in enterprise Kubernetes environments without manual configuration.

**Security, Sovereignty, and Compliance**

- Declarative policy controls: Operators define security and operations policies in Kubernetes Custom Resources (CRDs), including backup, upgrade, and failover behavior, so controls are versioned, repeatable, and auditable through GitOps workflows. [MySQL Operator Custom Resource options](https://docs.percona.com/percona-operator-for-mysql/pxc/operator.html) show how operational policy is expressed declaratively in cluster specs.
- Automated TLS certificate rotation: Percona Operator for MySQL based on Percona XtraDB Cluster applies updated CA, server, and key material from Secrets on the next reconciliation loop with minimal downtime, reducing manual certificate rollover steps and human-error risk during TLS updates. [Percona Operator for MySQL based on Percona XtraDB Cluster 1.20.0 release notes](https://docs.percona.com/percona-operator-for-mysql/pxc/ReleaseNotes/Kubernetes-Operator-for-PXC-RN1.20.0.html)
- Secrets and credential governance: [MongoDB Operator Vault integration](https://docs.percona.com/percona-operator-for-mongodb/system-users-vault.html) supports system user credential management, including authentication to Vault and periodic password sync, so teams can centralize credential rotation and separate security duties from day-to-day operations.
- Access governance with Kubernetes-native enforcement: Operators use Kubernetes APIs and RBAC integration to apply consistent access controls across clusters, helping organizations enforce internal governance requirements in cloud and on-prem environments. [PostgreSQL Operator Custom Resource options](https://docs.percona.com/percona-operator-for-postgresql/latest/operator.html) provide a concrete example of policy expressed and enforced through Kubernetes-native resources and service configuration.
- Predictable OpenShift operator scope: Percona Operator for PostgreSQL Community-catalog OLM installs honor OperatorGroup namespace scope (`olm.targetNamespaces`), so reconciliation matches how the subscription is installed. Confirm install mode before upgrade when multiple operators share a cluster, and set explicit `targetNamespaces` where you need to limit overlap.
- Compliance consistency across environments: Operators support multi-cluster and multi-region deployment patterns that help teams meet data residency and regulated deployment requirements across jurisdictions, while keeping one operational model across cloud and on-prem environments. [MongoDB multi-cluster and multi-region deployments](https://docs.percona.com/percona-operator-for-mongodb/replication.html) are documented as a first-class pattern for geo-distributed and compliance-isolated operations.

**Adaptability for Emerging Workloads**

- Multi-cloud and hybrid portability: Percona Operators run on any CNCF-conformant Kubernetes, including OpenShift, Amazon EKS, Google GKE, Azure AKS, and on-prem clusters. Teams can move workloads freely without rewriting automation or getting trapped by a single cloud vendor. The [Percona Operator for MySQL cross-site replication](https://docs.percona.com/percona-operator-for-mysql/pxc/dr-replication.html) enables multi-environment continuity with replication between Kubernetes sites.
- Integration with cloud-native toolchains: Operators expose APIs for CI/CD pipelines and policy engines, with support for Prometheus, Grafana, and PMM (Percona Monitoring and Management), so database operations fit naturally into platform engineering workflows and support rapid, reliable delivery. [PostgreSQL Operator architecture](https://docs.percona.com/percona-operator-for-postgresql/latest/architecture.html) also highlights integration components such as Patroni, pgBackRest for PostgreSQL backup catalog management and PiTR-oriented workflows, and pgBouncer that align with platform engineering operating models. A dedicated CRD Helm chart (Operator for MongoDB 1.22.0+) improves compatibility with GitOps tools like ArgoCD and FluxCD by letting Helm manage all resources, including CRDs.
- Modernization path for legacy operations: Operators replace ticket-driven, manual database lifecycle tasks with declarative workflows for provisioning, upgrades, backups, and recovery. For PostgreSQL on Kubernetes, upstream Crunchy resources migrate automatically to the `upstream.pgv2.percona.com` API group on upgrade so Percona and Crunchy operators can coexist during adoption and teams can move without re-architecting clusters. Major-version upgrades use `PerconaPGUpgrade` and the official Percona distribution upgrade image for controlled execution in Kubernetes. [Migration from Crunchy PGO](https://docs.percona.com/percona-operator-for-postgresql/3.0.0/migrate-from-crunchy.html), [PostgreSQL major version upgrade workflow](https://docs.percona.com/percona-operator-for-postgresql/latest/update-db-major.html)

### Sales enablement: cloud native database operations

Percona supports teams that need to run MySQL, PostgreSQL, and MongoDB on Kubernetes with predictable operations, visibility, and control, without being locked into a single cloud provider's DBaaS model.

**Best-fit customer profiles**

- Platform engineering teams building internal database services on Kubernetes
- SRE and DevOps teams standardizing Day 2 operations across multiple database engines
- Organizations with compliance, residency, or sovereignty requirements across cloud and on-prem environments
- Teams modernizing from VM-based database operations to Kubernetes-native workflows

**Technical signals to qualify**

- Current or planned Kubernetes footprint for stateful workloads
- Operational pain around backup, recovery, scaling, or failover consistency
- Need for GitOps-compatible control and auditability via declarative resources
- Requirement for integrated observability across database fleets
- Preference for open source tooling and cloud portability

**Discovery questions**

- Which database operations are still manual in your Kubernetes environments today?
- Where do incidents most often start: failover, backup and recovery, scaling events, or visibility gaps?
- How are you balancing standardization across engines with team-level autonomy?
- What compliance or governance requirements influence where and how you run databases?
- Where would expert help accelerate outcomes, architecture planning, reliability tuning, or ongoing operations?

**Public resources**

- [Percona Operators documentation](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html)
- [Percona Operator for PostgreSQL documentation](https://docs.percona.com/percona-operator-for-postgresql/latest/index.html)
- [Percona Operator for MongoDB documentation](https://docs.percona.com/percona-operator-for-mongodb/index.html)
- [Percona Monitoring and Management (PMM)](https://docs.percona.com/percona-monitoring-and-management/index.html)

