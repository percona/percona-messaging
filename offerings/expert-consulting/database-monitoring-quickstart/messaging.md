# Database Monitoring QuickStart

**SKU:** CONS-PMM  
**Starting from:** $4,500

Most monitoring rollouts stall the same way: the server goes up, the default dashboards go unread, and the alerts never get tuned, so nobody trusts them. This engagement deploys Percona Monitoring and Management (PMM) against your environment and, more to the point, teaches your team to use it: reading query analytics, setting alert thresholds your team has actually agreed to, and owning upgrades going forward. PMM is open source; this is how it becomes useful in days instead of quarters. The packaged QuickStart covers MySQL, MariaDB Server, PostgreSQL, and MongoDB.

This is one packaged fixed-fee scope under [Expert Consulting and Services](../messaging.md), not the full Consulting catalog. PMM Customization, multi-environment rollouts, and other monitoring work outside this QuickStart are scoped separately.

## FAQ

### Is this just an installation service?

No, and that is the point. Installation is the easy part; this engagement covers configuration, verification of monitoring accounts and permissions, knowledge transfer on the dashboards and Query Analytics your team will use week to week, and documentation of your configuration and alerting thresholds. Teams that already have PMM running but never got onboarding are just as good a fit as first-time deployments.

### What do we need in place before kickoff?

A dedicated server capable of running a container or Kubernetes environment for PMM Server, with outbound access to every database or node being monitored. That is it; we handle the rest during the engagement.

### Does it work with RDS and Aurora?

For MySQL and PostgreSQL, yes: self-managed, RDS, and Aurora are all covered. MariaDB Server and MongoDB engagements cover self-managed deployments.

### What will our team actually learn?

How to read the dashboards for your engine (including the Galera cluster metrics or sharded cluster views most self-installs never configure), how to use Query Analytics, how to set and tune alerts, how to troubleshoot with Advisors, and how to run PMM upgrades. You leave with a named owner for ongoing maintenance and a written record of what was configured and why.

### We need custom dashboards. Is that included?

Custom dashboards beyond the standard set are scoped separately under PMM Customization. This engagement gets the standard dashboards deployed, configured, and understood first, which is where most teams get the fastest return.

### What does PMM itself cost?

Nothing. PMM is open source, with no license fees and no per-node pricing. The fixed fee covers deployment, configuration, and getting your team genuinely up to speed.

## Engine variants

Source files are split by engine so tech owners can review only their variant. Engine files on this PR are stubs; full copy lands in follow-up tech PRs (issue #274). On the Docsify site, includes still render below once those PRs land.

| Engine | Source file |
| --- | --- |
| MySQL | [MySQL](mysql.md) |
| MariaDB Server | [MariaDB Server](mariadb.md) |
| PostgreSQL | [PostgreSQL](postgresql.md) |
| MongoDB | [MongoDB](mongodb.md) |

<!-- docsify assemble: full package page for readers -->

[MySQL](/offerings/expert-consulting/database-monitoring-quickstart/mysql.md ':include')

[MariaDB Server](/offerings/expert-consulting/database-monitoring-quickstart/mariadb.md ':include')

[PostgreSQL](/offerings/expert-consulting/database-monitoring-quickstart/postgresql.md ':include')

[MongoDB](/offerings/expert-consulting/database-monitoring-quickstart/mongodb.md ':include')
