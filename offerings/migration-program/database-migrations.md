# Database Migrations

**SKU:** CONS-MIG  
**Starting from:** $26,000 for the least complex environments

Nobody books a maintenance window expecting to use the rollback plan. The teams that come out clean are the ones that rehearsed both. Migrations fail in the gap between the plan and the cutover: untested rollback procedures, missed replication lag, application changes nobody scoped, or a maintenance window that runs long because nobody tested the actual cutover steps beforehand.

This engagement covers MySQL, MariaDB Server, PostgreSQL, MongoDB, and Valkey/Redis migrations across on-prem, cloud, or DBaaS, and builds a fully tested target environment before cutover ever happens. It is one packaged path under [Migration and Modernization](messaging.md), not the full migration and modernization catalog. For proprietary exits such as Oracle or SQL Server to PostgreSQL, start with the [Proprietary Database Migration to PostgreSQL](proprietary-to-postgresql.md) assessment. For Galera roadmap risk, see [MySQL Galera Cluster Migration](mysql-galera-cluster-migration.md). Broader multi-phase or proprietary-estate programs are scoped as a full Migration and Modernization engagement.

## FAQ

### Which databases and platforms do you migrate?

We assist with homogeneous migrations (MySQL, MariaDB Server, PostgreSQL, MongoDB, and Valkey/Redis across on-prem, cloud, and DBaaS in any direction: on-prem to cloud, DBaaS to self-managed, version upgrades, or engine to engine) as well as heterogeneous migrations (for example moving Oracle or SQL Server workloads to PostgreSQL). Heterogeneous proprietary exits typically start with the proprietary assessment engagement.

### How do you keep the cutover from going wrong?

By making the real cutover the second time it happens. We build a test environment representative of your target, migrate data into it, validate the back end, support your application-level acceptance testing, and rehearse the migration process there. The production cutover runs against a tested plan with a documented rollback path, scheduled with off-hours support and emergency rollback assistance.

### What happens after the cutover?

Three things: two days of monitoring and assistance starting the next business day, a follow-up health audit 2 to 4 weeks out, and a PDF findings report. The migration is not done when the DNS flips; it is done when the follow-up audit says the new environment is healthy.

### Why does the price "start from" $26,000?

Because migration scope varies more than any other engagement we run. The starting price covers the least complex environments; actual scope depends on the source and target engines, data volume, and cutover complexity, and is refined with you during the planning phase. For proprietary to open source assessment, the initial assessment starts at $5,000 so you can find out what your migration involves before committing to a bigger number.

## Deliverables

- Joint planning session covering performance requirements, scalability concerns, growth projections, HA needs, and maintenance activities, informing and defining the migration process
- PMM setup and configuration for the migration environment, with knowledge transfer available throughout
- Test environment build representative of the target architecture or version, with data migration to the test environment and back-end validation
- Application-level acceptance testing support, with documentation of the final environment configuration incorporating lessons learned from testing
- Production target setup and configuration based on planning and testing outputs, with back-end testing to confirm it is set up correctly
- Tested database migration process and documented rollback plan, plus scheduling and layout of the migration and cutover
- Scheduled cutover with off-hours support and emergency rollback assistance
- Post-migration review: 2 days of monitoring and assistance beginning the next business day, a follow-up health audit 2–4 weeks out, and a PDF findings report

## Who it is for

The actual scope depends on the source/target engines, data volume, and cutover complexity, and is refined during the planning phase. Applicable across MySQL, MariaDB Server, PostgreSQL, MongoDB, and Valkey/Redis, whether self-managed, cloud, or DBaaS.

## Outcome

A migration executed against a tested plan with a documented rollback path, not a maintenance window you are hoping goes smoothly. You will know the cutover works before you schedule it, because we tested it in a representative environment first.

**CTA:** Plan your migration before you schedule the maintenance window.
