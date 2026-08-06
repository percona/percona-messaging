# MySQL Galera Cluster Migration

**Starting from:** $26,000 for the least complex migrations

MariaDB acquired Codership, the original creators of Galera Cluster, in May 2025. That led to two important changes for MySQL Galera Cluster users. In February 2026, MariaDB moved to strip Galera clustering libraries from the community server entirely, then reversed course after public pushback, including from its own foundation, and confirmed that Community Server 12.3 will keep Galera. Regardless of that development, at the end of September 2026 MySQL Galera Cluster goes EOL and will not be further developed, which means its users are forced to implement changes.

If your production HA strategy depends on a library MariaDB has already tried to pull once, or you run the original MySQL version of it, that is not a hypothetical risk; it is a live one. This engagement migrates your cluster to a Galera-based architecture (Percona XtraDB Cluster) that Percona builds, tests, and supports directly, so your HA strategy is not tied to MariaDB's next roadmap decision.

This engagement is one packaged path under [Migration and Modernization](messaging.md), not the full migration and modernization catalog. Homogeneous platform or version moves that are not Galera-specific use [Database Migrations](database-migrations.md). Broader HA redesigns outside this Galera-to-Percona XtraDB Cluster path are scoped as a custom migration or architecture engagement.

## FAQ

### MariaDB kept Galera in Community Server 12.3. Why would we still migrate?

Because the direction is on the record. In February 2026 MariaDB moved to strip Galera from the community server, reversed course after public pushback, and made no commitment beyond 12.3; its commercial HA options are paid-only. MySQL Galera Cluster also reaches EOL in September 2026. If your production HA depends on a library the vendor has already tried to pull once, or on a MySQL Galera line that is ending, that is a live risk. This engagement moves you to a Galera-based architecture Percona builds, tests, and supports directly, so you keep the multi-master setup your application was built around without that roadmap exposure.

## Deliverables

- Joint planning session assessing your current Galera cluster's configuration, write conflict handling, and application dependencies, and mapping it to Percona XtraDB Cluster or another HA architecture if feasible
- Percona Monitoring and Management setup and configuration for the migration environment, with knowledge transfer available throughout
- Test environment built on the target Percona-supported cluster, with data migration, back-end validation, and wsrep/Galera behavior comparison against your current cluster
- Production target setup and configuration, tested migration process, and documented rollback plan
- Scheduled cutover with off-hours support and emergency rollback assistance
- Post-migration review: 2 days of monitoring, a follow-up health audit 2–4 weeks out, and a PDF findings report

## Who it is for

Built for teams running MySQL or MariaDB Community Galera Cluster in production who want a reliable, future-proof HA strategy. Actual scope is refined during planning based on cluster size, used features, and application dependencies.

## Outcome

A Galera-based cluster running on an architecture Percona builds, tests, and supports directly, so future MariaDB decisions do not become your outage. You keep the multi-master architecture your application was built around; you stop depending on another vendor's willingness to keep shipping it for free.

**CTA:** Get your MySQL Galera cluster off MariaDB's roadmap risk.
