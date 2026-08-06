# Database Monitoring QuickStart

**SKU:** CONS-PMM  
**Starting from:** $4,500

Most monitoring rollouts stall the same way: the server goes up, the default dashboards go unread, and the alerts never get tuned, so nobody trusts them. Percona Monitoring and Management (PMM) helps teams fine-tune configuration to fit the workload, analyze root causes, and set proactive alerts when something is off. This engagement deploys PMM against your environment and, more to the point, teaches your team how to use it: reading query analytics, setting alert thresholds your team has actually agreed to, and owning upgrades going forward. PMM is open source and can monitor MySQL, PostgreSQL, MariaDB Community, MongoDB, and Valkey instances; this is how it becomes useful in days instead of quarters.

This is one packaged fixed-fee scope under [Expert Consulting and Services](messaging.md), not the full Consulting catalog. PMM Customization, multi-environment rollouts, and other monitoring work outside this QuickStart are scoped separately.

## FAQ

### Is this just an installation service?

No, and that is the point. Installation is the easy part; this engagement covers configuration, verification of monitoring accounts and permissions, knowledge transfer on the dashboards and Query Analytics your team will use week to week, and documentation of your configuration and alerting thresholds. Teams that already have PMM running but never got onboarding are just as good a fit as first-time deployments.

### What do we need in place before kickoff?

A dedicated server capable of running a container or Kubernetes environment for PMM Server, with outbound access to every database or node being monitored. That is it; we handle the rest during the engagement.

### Does it work with RDS and Aurora?

For MySQL and PostgreSQL, yes: self-managed, RDS, and Aurora are all covered. MariaDB Community and MongoDB engagements cover self-managed deployments (MariaDB Community on AWS RDS where monitoring access allows).

### What will our team actually learn?

How to read the dashboards for your engine (including the Galera cluster metrics or sharded cluster views most self-installs never configure), how to use Query Analytics, how to set and tune alerts, how to troubleshoot with Advisors, and how to run PMM upgrades. You leave with a named owner for ongoing maintenance and a written record of what was configured and why.

### We need custom dashboards. Is that included?

Custom dashboards beyond the standard set are scoped separately under PMM Customization. This engagement gets the standard dashboards deployed, configured, and understood first, which is where most teams get the fastest return.

### What does PMM itself cost?

Nothing. PMM is open source, with no license fees and no per-node pricing. The fixed fee covers deployment, configuration, and getting your team genuinely up to speed.

## Database Monitoring QuickStart for MySQL

Get Percona Monitoring and Management (PMM) deployed and actually used, not just installed. Most teams stand up PMM, look at the Overview dashboard once, and never touch Query Analytics again because nobody walked them through it.

We set up PMM against your MySQL environment and run your team through the dashboards, query analytics, and alerting you will actually use week to week. This is not a generic monitoring rollout; it is built specifically around how MySQL exposes performance data, from the slow query log to performance_schema, so your team learns to read the signals your database is already giving you.

### Deliverables

- PMM server installation and configuration for your environment
- Client setup for MySQL monitoring and Query Analytics, including RDS, Aurora, or self-managed deployments
- Verification that monitoring user accounts and permissions are correctly provisioned for every server in scope
- Knowledge transfer covering MySQL dashboards, Query Analytics, alerting, troubleshooting, and Advisors
- Review of the PMM upgrade process and administrative tasks your team will own going forward
- Documentation summarizing your PMM configuration, recommended alerting thresholds, and operational practices covered

### Who it is for

Built for teams standing up PMM for the first time, or who have had it running without ever getting proper onboarding. Custom dashboards beyond the standard MySQL set are scoped separately under PMM Customization. Works across self-managed MySQL, RDS, and Aurora; the prerequisite is a dedicated server and outbound access to the databases being monitored.

### Outcome

Your team walks away knowing how to read your own query analytics and set alerts that matter, not just where the Overview dashboard is. You will leave with documented alerting thresholds your team actually agreed to, not defaults nobody reviewed, and a clear owner for PMM upgrades going forward.

**CTA:** Deploy PMM in days, not backlog quarters.

## Database Monitoring QuickStart for MariaDB Community

Get Percona Monitoring and Management (PMM) deployed and actually used, not just installed. Most teams stand up PMM, look at the Overview dashboard once, and never touch Query Analytics again because nobody walked them through it.

We set up PMM against your MariaDB Community environment and run your team through the dashboards, query analytics, and alerting you will actually use week to week. This is not a generic monitoring rollout; it is built specifically around how MariaDB Community exposes performance data, from the slow query log to performance_schema, so your team learns to read the signals your database is already giving you. Percona supports MariaDB Community versions; Enterprise editions are out of scope.

### Deliverables

- PMM server installation and configuration for your environment
- Client setup for MariaDB Community monitoring and Query Analytics, including RDS or self-managed deployments
- Verification that monitoring user accounts and permissions are correctly provisioned for every server in scope
- Knowledge transfer covering MariaDB dashboards, Query Analytics, alerting, troubleshooting, and Advisors
- Review of the PMM upgrade process and administrative tasks your team will own going forward
- Documentation summarizing your PMM configuration, recommended alerting thresholds, and operational practices covered

### Who it is for

Built for teams standing up PMM for the first time, or who have had it running without ever getting proper onboarding. Custom dashboards beyond the standard set are scoped separately under PMM Customization. Works across self-managed MariaDB Community and AWS RDS; the prerequisite is a dedicated server and outbound access to the databases being monitored.

### Outcome

Your team walks away knowing how to read your own query analytics and set alerts that matter, not just where the Overview dashboard is. You will leave with documented alerting thresholds your team actually agreed to, not defaults nobody reviewed, and a clear owner for PMM upgrades going forward.

**CTA:** Deploy PMM in days, not backlog quarters.

## Database Monitoring QuickStart for PostgreSQL

Deploy Percona Monitoring and Management (PMM) against your PostgreSQL environment, configured with the query analytics and replication dashboards you need to catch problems before they page you.

We handle installation and configuration, then walk your team through reading replication lag, autovacuum activity, and query performance in PMM. Most teams that self-install PMM against PostgreSQL never get past the default dashboards; this engagement makes sure someone actually explains what pg_stat_statements is telling you and which alerts are worth acting on.

### Deliverables

- PMM server installation and configuration for your environment
- Client setup for PostgreSQL monitoring and Query Analytics, including RDS, Aurora, or self-managed deployments
- Verification that monitoring user accounts and required extensions (pg_stat_statements) are correctly provisioned
- Knowledge transfer covering PostgreSQL dashboards, Query Analytics, alerting, troubleshooting, and Advisors
- Review of the PMM upgrade process and administrative tasks your team will own going forward
- Documentation summarizing your PMM configuration, alerting thresholds, and operational practices covered

### Who it is for

Built for teams standing up PMM for the first time, or who have had it running without proper onboarding on the PostgreSQL-specific dashboards. Works with self-managed PostgreSQL and DBaaS such as RDS or Aurora; the prerequisite is a dedicated server and outbound access to the monitored databases.

### Outcome

Your team knows how to spot replication lag and autovacuum problems before they show up as an incident, and has alerting thresholds in place that reflect your actual workload, not generic defaults. You will leave with a documented owner for PMM upgrades and a shared understanding of what each dashboard is actually measuring.

**CTA:** Catch replication lag before your users do.

## Database Monitoring QuickStart for MongoDB

Deploy PMM against your replica set or sharded cluster, and have your team walk through the dashboards and query analytics specific to MongoDB.

We handle installation and configuration, then run your team through reading the oplog window, replica set lag, and chunk distribution without digging through MongoDB Shell output. For sharded clusters, that includes walking your team through the mongos and config server dashboards that most self-installs never touch.

### Deliverables

- PMM server installation and configuration for your environment
- Client setup for MongoDB monitoring and Query Analytics across replica set members or sharded cluster components
- Verification that monitoring user accounts and roles are correctly provisioned
- Knowledge transfer covering MongoDB dashboards, Query Analytics, alerting, troubleshooting, and Advisors
- Review of the PMM upgrade process and administrative tasks your team will own going forward
- Documentation summarizing your PMM configuration, alerting thresholds, and operational practices covered

### Who it is for

Built for teams standing up PMM for the first time against a MongoDB replica set or sharded cluster, or who have had it running without proper onboarding. Works with self-managed MongoDB; the prerequisite is a dedicated PMM server with outbound access to every monitored member.

### Outcome

Your team can see oplog window, replica set lag, and chunk distribution without digging through the MongoDB Shell output, and has alerting thresholds set for the metrics that actually predict trouble. You will leave with a documented owner for ongoing PMM maintenance and upgrades, and a shared reference for what each dashboard actually measures next time someone new joins the on-call rotation.

**CTA:** Get visibility into your oplog window before it runs out.
