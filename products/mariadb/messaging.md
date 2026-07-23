# Percona for MariaDB: Messaging

## Percona for MariaDB {#percona-for-mariadb}

For organizations running MariaDB in production, Percona helps teams get more value from **MariaDB Community**. That means steadier day-to-day operations, clearer cost and support boundaries, stronger performance and reliability practices, and security that fits how the estate already runs. Percona does this with **Expert Support**, **Expert Consulting and Services** for complex environments, and **Percona ExpertOps** when teams want operational ownership. Where Percona publishes **Extended Lifecycle Support (ELS)** for qualifying MariaDB Community versions near or past End of Life (EOL), that coverage is available as a bridge on the team's timeline. Teams do not need to change platforms to start.

MariaDB Community is a strong fit when teams use what MariaDB already does well: Galera-style clustering they already know, **ColumnStore** for analytics next to everyday transaction work (OLTP), MariaDB backup and audit tools, and software versions that match apps already built on MariaDB. Many organizations run MariaDB **alongside** MySQL because different jobs needed different databases for real reasons.

MariaDB Community is a production path for important open source workloads. Teams need production Expert Support that is clear about Community limits, consulting when the setup is larger or more mixed, and operators who know MariaDB-specific parts and use cases. Percona fills that gap without claiming to build MariaDB software, and without treating MariaDB as a short stop on the way to MySQL.

Percona does not ship MariaDB database software. Percona supports **MariaDB Community** in production with the same upstream-level engineering depth applied across MySQL, PostgreSQL, MongoDB, and Valkey. **Expert Support** covers **MariaDB Community versions only**, not MariaDB Enterprise editions under standard Support entitlements. **Expert Consulting and Services** may apply to other MariaDB versions and complex environments. See [MariaDB support](https://www.percona.com/services/support/mariadb-support).

### Customer Challenges and Value Alignment – MariaDB

**Optimized TCO**

- **Extended Lifecycle Support (ELS) for MariaDB Community:** When MariaDB Community versions near or pass End of Life (EOL), teams face higher security, compliance, and support risk if they stay with no continuity plan, or costly rush upgrades if they move under deadline pressure. Where Percona publishes MariaDB Community ELS coverage, treat it as a bridge to a supported Community release on the team's timeline, not a permanent stay on EOL. ELS is not a replacement for moving to a supported version, and it does not mean Percona ships MariaDB database software.
- **MySQL Galera Cluster end of life (adjacent estates):** MariaDB has announced 2026-09-30 as the end of life for maintenance and regular binary releases of **MySQL Galera Cluster**. For teams on MySQL Galera Cluster (not MariaDB Galera) who want a Galera-to-Galera path forward, **Percona XtraDB Cluster** is available ([continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/)). Teams already on MariaDB Community stay in the MariaDB Support, consulting, and published-ELS motion above.
- **Multi-database vendor consolidation:** Teams already working with Percona for MySQL, PostgreSQL, MongoDB-compatible environments, Valkey, or Redis can add **MariaDB Community** Expert Support without a separate database vendor relationship, duplicate SLAs, or slower handoffs when incidents cross engines.

**Performance and Reliability at Scale**

- **Faster recovery when production breaks:** Percona Expert Support and ExpertOps give MariaDB Community environments 24×7 upstream-level help for incidents, upgrades, replication, and performance problems on the stack teams run today. That helps restore service and reduce repeat risk without waiting on a platform change.
- **Reliability without forced re-architecture:** Teams keep existing HA, backup, and ops patterns while Percona helps diagnose root causes, reduce repeat incidents, and harden recovery practices.
- **Workload-shaped tuning:** OLTP, analytics (including ColumnStore where in use), and clustering patterns get guidance matched to how the application actually behaves. Prefer "evaluate for the workload" over unverified head-to-head claims.
- **Keep MariaDB when components are load-bearing:** Keep MariaDB Community when Galera-style clustering, ColumnStore, MariaDB backup and audit tooling, or app assumptions built on MariaDB are load-bearing. Keep MySQL or Percona Server for MySQL when that stack is already the estate standard. Both can be valid; match the engine to the workload and ops constraints without ranking the engines.

**Security, Sovereignty, and Compliance**

- **Hardening on the estate in operation:** Expert Support and consulting help teams strengthen configuration, access controls, audit posture, backup encryption practices, and upgrade discipline on MariaDB Community running on customer-controlled infrastructure.
- **Clear entitlement boundaries:** Community Support coverage is spelled out. Non-Community or Enterprise-adjacent environments need a consulting scope so security and compliance work is not assumed under the wrong entitlement.
- **Controls matched to how MariaDB is run:** Focus on what the team can enforce on Community today (process, config, patch cadence, audit retention) rather than pitching a different engine as the default compliance answer.

**Adaptability for Emerging Workloads**

- **Evolve on MariaDB:** Consulting and Support help teams plan upgrades, topology changes, and stronger day-to-day ops while applications remain on MariaDB Community.
- **Analytics and AI-adjacent use cases:** Some environments already use ColumnStore or are evaluating newer MariaDB capabilities next to OLTP. Treat fit as workload-specific; prefer "evaluate for the workload" over unverified vector or performance claims.
- **Multi-engine future without a conversion narrative:** Teams often keep MariaDB where it fits and run other databases elsewhere. Percona helps MariaDB stay healthy in that mix rather than framing every roadmap talk as a move off MariaDB.

### Sales enablement

**Elevator pitch**

Percona helps MariaDB Community environments run in production with Expert Support and optional ExpertOps. Consulting covers complex or non-Community environments. Where Percona publishes ELS for qualifying Community versions near or past EOL, that coverage bridges to a supported release on the team's timeline. Teams get more reliability, clarity, and operational depth on MariaDB, without Percona claiming to ship MariaDB software.

**Purpose**

MariaDB Community is a lasting production path, not a short stop on the way to MySQL. Teams need honest Community Support scope, consulting when the environment is broader or outside Community entitlements, ExpertOps when teams want operational ownership, and published ELS coverage where Community versions near or pass EOL. Percona meets those needs on MariaDB with clear boundaries: Community-only Expert Support, no Percona MariaDB database software, and engine-change work only when the customer asks for a different home.

**Conversation starters**

- Are you running MariaDB Community or Enterprise in production today, and which versions matter for Support scope? (Expert Support covers MariaDB Community only; non-Community surfaces need consulting scope so entitlements stay honest.)
- Which Community versions are approaching or past End of Life (EOL), and do you need runway before an upgrade finishes? (Where Percona publishes MariaDB Community ELS, treat it as a bridge to a supported Community release on the team's timeline, not a permanent stay on EOL.)
- Which MariaDB-specific components are load-bearing today: Galera patterns, ColumnStore, backup, audit, or app assumptions built on MariaDB? (Stay-and-stabilize is the default when those pieces are central; engine-change only if the customer asks.)
- Do you already buy Percona Support for other engines while MariaDB sits on a separate vendor relationship? (Same Support relationship and SLAs across engines without forcing one database.)
- What are the top recurring MariaDB incidents (replication, failover, upgrades, query regressions), and how are they handled today? (Expert Support and optional ExpertOps reduce repeat fire drills on the stack you run now.)
- If you run Galera or similar clustering, what do failover and recovery look like under real failure drills? (Harden HA and recovery practices in place; match guidance to the clustering model you already operate.)
- Are you on MySQL Galera Cluster (not MariaDB Galera) with a 2026 maintenance cliff in view? (Adjacent estate only: for teams who want a Galera-to-Galera path, PXC is available. MariaDB Community stays on the MariaDB Support / consulting / published-ELS motion.)
- Which audit, identity, encryption, or evidence requirements must the MariaDB layer meet, and who owns keys, audit retention, and patch cadence? (Harden Community in place with clear ownership; separate Support vs consulting if non-Community versions are in the estate.)
- Which workloads on MariaDB are latency-sensitive, write-heavy, or analytics-heavy (including ColumnStore where used)? (Tune and capacity-plan for how the app behaves; evaluate fit per workload rather than engine rankings.)
- What emerging work (analytics, AI-assisted features, Kubernetes ops) are you placing near MariaDB in the next 12 months, and what must stay true for MariaDB to remain the right home? (Grow on Community with Support and consulting when MariaDB-specific pieces stay central; multi-engine estates are normal.)
- Would you rather keep day-to-day MariaDB operations on your team with Expert Support, or hand defined operational ownership to Percona? (ExpertOps is optional; Support alone is a complete starting point.)

**Situation talk tracks**

- **ELS bridge on MariaDB Community:** Version is near or past EOL, MariaDB-specific components still matter, and the team needs continuity plus an upgrade plan. Use published MariaDB Community ELS where available; do not invent coverage.
- **Unify Support across engines:** Multi-engine estate, MariaDB is staying, buyer wants one Support relationship and clear Community entitlements.
- **Stabilize on MariaDB:** Recurring incidents or HA drill gaps are the pain; Expert Support and optional ExpertOps deepen operations without a platform change.
- **Harden Community in place:** Audit, identity, encryption, or evidence requirements can be met on the current MariaDB Community estate with Support and consulting.
- **Multi-engine stay:** MariaDB keeps workloads where its components are load-bearing; MySQL or Percona Server for MySQL stays where that stack is the estate standard. No conversion narrative.

**Public resources**

- [MariaDB support](https://www.percona.com/services/support/mariadb-support)
- [Compare MySQL, MongoDB, PostgreSQL, and MariaDB](https://www.percona.com/compare-mysql-mongodb-postgresql-mariadb)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [Continued commitment to Percona XtraDB Cluster](https://www.percona.com/blog/continued-commitment-to-percona-xtradb-cluster/) (for MySQL Galera Cluster EOL estates who want a Galera-to-Galera path)
- [How to migrate from MariaDB to Percona Server for MySQL](https://www.percona.com/resources/how-to-migrate-from-mariadb-to-percona-server-for-mysql) (customer-requested engine change only)
- [Open source migration](https://www.percona.com/services/open-source-migration) (customer-requested engine change only)
