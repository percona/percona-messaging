# Percona Search for MongoDB: Messaging

## Product overview

Percona Search for MongoDB is Percona's supported, integrated version of `mongot`, MongoDB®'s vector, full-text, and hybrid search engine, built on Percona Server for MongoDB (PSMDB). It is free to use. Support is an optional add-on to a Percona Support contract.

Percona Search adds local-first automatic embeddings, Operator-managed deployment, index backup, and PMM observability. It is for teams running MongoDB themselves that need production search but cannot send document text to a third-party embedding service. With local inference, document text stays in the cluster, the embedding path has no per-token meter, and the stack runs without deployment limits or paid software tiers.

## Value proposition

Run vector, full-text, and hybrid search with MongoDB data on infrastructure you control. Keep embedding inference in the cluster, manage the search tier with the database control plane, and restore indexes without a full re-index. Use the software at no cost, with one optional support add-on for the full stack.

## Messaging

**Keep document text in the cluster.** MongoDB's automatic embedding pipeline requires a Voyage AI key in both Enterprise Advanced and Community Edition, and every embedding call sends document text to Voyage's cloud. MongoDB has no first-class local inference path. Percona Search runs inference inside the cluster by default.

**Local inference without another embedding service.** Voyage AI offers on-premises deployment, which avoids cloud egress but retains a separate enterprise contract and leaves GPU capacity and model upkeep to the customer. Percona supports open-weight providers for local inference, with no separate embedding service to buy.

**Operate the search tier with the database.** Enterprise Advanced and MongoDB Controllers for Kubernetes cover deployment and lifecycle, but index lifecycle, backup, recovery, autoscaling, and observability remain customer responsibilities. Percona Search integrates with the Percona Operator for MongoDB, Percona Backup for MongoDB (PBM), and Percona Monitoring and Management (PMM), extending the database control plane to the search tier.

**Use infrastructure you already run.** Voyage billing grows with corpus size and query volume. Local open-weight models run on fixed, amortized hardware. Percona Search is free to use; support is an optional add-on to a Percona Support contract, not a condition of running the software.

## Unique benefits

| Benefit | Why it matters |
| --- | --- |
| **No embedding paywall, no data egress** | Local-first automatic embeddings keep document text in the cluster when a local provider is configured. The local embedding path has no per-token charge. |
| **Air-gapped capable end to end** | With local providers configured, the stack can run without outbound traffic, including in environments where third-party API signup is blocked by sanctions, residency, or procurement policy. |
| **Full stack, one support add-on** | The Percona Operator for MongoDB, PBM, PMM, and PSMDB cover deployment, sharded clusters, backup, encryption, and audit. Search adds Atlas-equivalent management CRDs for the search tier. The software is free to use; an optional support add-on covers the stack together. |
| **Backup and restore without re-indexing** | Percona orchestrates native `mongot` blobstore snapshots. Restore does not require a full re-index. Index definitions are covered, manual setup is available, and the capability works with PSMDB, MongoDB Community Edition, and Enterprise Advanced. |
| **Enterprise security included** | LDAP, OIDC, Kerberos, FCBIS, audit logging, and encryption at rest are standard in PSMDB, with no separate license cost. |
| **Predictable TCO** | Voyage billing scales with corpus size and query volume. Local open-weight models run on fixed, amortized hardware. |

## Features that prove the benefits

| Capability | What it does | Benefit it proves | How to say it |
| --- | --- | --- | --- |
| **Local-first auto-embeddings** | Provides an OpenAI-compatible interface for Ollama, vLLM, LocalAI, in-cluster Hugging Face, OpenAI, and Azure OpenAI. It also provides a Hugging Face Inference API interface, hosted in the same shape as Voyage, with roughly 2,000 models instead of four at lower cost. | No embedding paywall, no data egress, and predictable TCO | Lead with the in-cluster path. The hosted interface is an option for teams not ready to run inference themselves. |
| **End-to-end data sovereignty** | With local providers configured, document text stays in the cluster by default and no outbound traffic is required. | Air-gapped capable | Use the GA data-flow audit as evidence for compliance audiences. |
| **Percona Operator integration** | Deploys the search tier alongside the MongoDB replica set and scales it separately from the database. | Full stack, one support add-on | Lead with management through the existing control plane. Separate search-tier scaling is the detail for architects. |
| **Backup and restore for vector indexes** | Orchestrates native `mongot` blobstore snapshots and covers index definitions. Manual setup is available. Compatible with MongoDB Community Edition, Enterprise Advanced, and PSMDB. | Backup and restore without re-indexing | Lead with no re-indexing on restore. Say index definitions are covered and manual setup is available. Do not state unmeasured time savings. |
| **PMM dashboards and alerts** | Monitors recall regression, JVM heap, Lucene cache, sync lag, and embedding provider health. | Full stack, one support add-on | Lead with recall regression, followed by JVM heap, Lucene cache, sync lag, and embedding provider health. |
| **Enterprise security baseline** | PSMDB includes LDAP, OIDC, Kerberos, FCBIS, audit logging, and encryption at rest with no separate license. | Security included, not unlocked | Always say included, never available. Contrast with capabilities sold behind a separate tier. |
