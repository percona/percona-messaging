# MySQL Galera Cluster EOL Offering: Messaging

## MySQL Galera Cluster EOL offering {#mysql-galera-cluster-eol}

**Value proposition**

Opt for continued support of your MySQL Galera Cluster after its end of life, or migrate to a head-to-head replacement in Percona XtraDB Cluster. Either way, your clustering layer stays open source, stays on MySQL, and stays supported. We've got you covered.

### Messaging

MySQL Galera Cluster reaches end of support on 30 September 2026. After that date there is no maintenance, no bug fixes, and no binary releases for the MySQL build. The vendor's recommended path is to migrate to MariaDB, a different database with a different system table structure, a different data dictionary, and user privileges you have to recreate by hand.

You built a high-availability layer on open source MySQL because you wanted control. Changing database vendor to keep a support contract is the opposite of control.

Percona offers two paths, and you choose:

1. **Keep the cluster you have, and get a support contract that outlives the EOL date.** The hardest part of running Galera has always been diagnosis under pressure. And that's exactly what degrades when maintenance ends. Percona MySQL Support covers your existing MySQL Galera Cluster environment as it is. No migration, no re-platforming, no privilege rebuild. Under your agreement you get an escalation point to senior MySQL engineers 24x7x365 on a follow-the-sun model. Use that time to plan your next architecture on your schedule instead of MariaDB's.
2. **Migrate to Percona XtraDB Cluster and stay on MySQL, fully open source.** PXC is Percona Server for MySQL plus the Galera write-set replication library. It is our own Galera fork, maintained in a public repository, and it is fully compatible with MySQL Server Community Edition. What makes this migration different from the MariaDB path? Your schema, system tables, and user accounts carry over as they are. Same wsrep behavior, same MySQL ecosystem, same tools, same connectors.

Running unsupported is not the alternative. An unmaintained clustering layer under a revenue-generating application is a compliance and availability exposure.

### Benefits

**Percona MySQL Support for MySQL Galera Cluster will provide you:**

- An escalation point to highly technical MySQL engineers, 24x7x365, follow-the-sun.
- Consultative and operational support: detailed responses and direction on advisory questions, not just incident triage.
- Access to Percona's internal knowledge base.
- Industry-leading SLAs, up to 15-minute response times, ensure issues are addressed before they escalate.
- [Support datasheet with full details](https://learn.percona.com/hubfs/Datasheet/New-Services-Offerings/Percona-Support-for-MySQL-datasheet.pdf)

**Percona Migration Services to PXC guarantee:**

- Continued PXC engineering on the cluster layer. The hard part was never the replication library, it's the cluster around it. IST/SST behaviour, node eviction, flow control, and DDL under concurrent writes, fixed in public across every release.
- Joint planning session assessing your current Galera cluster's configuration, write conflict handling, and application dependencies, and mapping it to Percona XtraDB Cluster
- Test environment built on the target Percona-supported cluster, with data migration, back-end validation, and wsrep/Galera behavior comparison against your current cluster
- Production target setup and configuration, tested migration process, and documented rollback plan
- Scheduled cutover with off-hours support and emergency rollback assistance
- Post-migration review: 2 days of monitoring, a follow-up health audit 2–4 weeks out, and a PDF findings report
