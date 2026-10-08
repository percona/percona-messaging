# Percona Toolkit: Messaging

## Percona Toolkit {#percona-toolkit}

In-house database engineers and DBAs use Percona Toolkit to change a large MySQL table, confirm a replica before failover, archive old rows, or rank a slow log. Anyone can install and run the same commands.

Percona Toolkit changes a large MySQL table by copying rows into a new table and swapping it in, so reads and writes continue on the original. A blocking `ALTER` holds that table for the length of the change, and a failover onto an unchecked replica puts data at risk. [Percona Toolkit](https://docs.percona.com/percona-toolkit/) is the command-line set Percona maintains for schema change, replica checks, and slow-log review. Confirm backups and read the [`pt-online-schema-change`](https://docs.percona.com/percona-toolkit/pt-online-schema-change.html) documentation before running it. On [Percona XtraDB Cluster](https://docs.percona.com/percona-xtradb-cluster/8.4/online-schema-upgrade.html), the documented path is InnoDB tables with `wsrep_OSU_method` set to `TOI`.

Percona publishes Percona Toolkit under the [GPL version 2 or the Perl Artistic License](https://docs.percona.com/percona-toolkit/copyright_license_and_warranty.html), with no runtime license. The same commands run on bare metal, on virtual machines, and against MySQL on AWS, Google Cloud, and Azure. Community contributions are reviewed, regression-tested, and named in the [release notes](https://docs.percona.com/percona-toolkit/release_notes.html). Support engineers use the same commands customers run.

Online schema change and replica checksums are MySQL tools. The same install also includes:

- MongoDB server summary, query digest, and index checks
- `pt-pg-summary` for a PostgreSQL server
- `pt-k8s-debug-collector` for Percona Operators for MySQL, MongoDB, and PostgreSQL
- MariaDB Server recognition in Percona Toolkit 3.7.1 ([Percona Toolkit 3.7.1](https://percona.community/blog/2025/12/17/what-is-new-in-percona-toolkit-3.7.1/))

For MySQL 9.7, install Percona Toolkit 3.7.0 or later from the Toolkit packages.

### Customer Challenges and Value Alignment: Percona Toolkit

**Optimized TCO**

- **Ships with the MySQL distribution:** Teams get the commands with no runtime license. Percona Distribution for MySQL 8.4 (Percona Server-based) includes Percona Toolkit 3.7.1-3.
- **Row archival in chunks:** A large table can shrink without one statement locking it for the whole job. [`pt-archiver`](https://docs.percona.com/percona-toolkit/pt-archiver.html) archives or purges rows in chunks.

**Performance and Reliability at Scale**

- **Live schema change:** Reads and writes continue on the original table during a large `ALTER`. Confirm backups before [`pt-online-schema-change`](https://docs.percona.com/percona-toolkit/pt-online-schema-change.html). On [Percona XtraDB Cluster](https://docs.percona.com/percona-xtradb-cluster/8.4/online-schema-upgrade.html), use InnoDB and `wsrep_OSU_method=TOI`.
- **Checked replicas and slow logs:** Teams find drift before failover and see which statements cost the most time. `pt-table-checksum` finds drift between source and replicas, `pt-table-sync` reconciles the rows, and `pt-heartbeat` measures lag from a heartbeat table. `pt-query-digest` ranks slow-log statements by time.

**Security, Sovereignty, and Compliance**

- **TLS on servers customers operate:** Toolkit 3.7.1 connects when the server requires TLS or `caching_sha2_password`. MySQL 9.7 removes `mysql_native_password`, so clients need that plugin. Certificate paths stay in the client configuration on the database host. For `pt-online-schema-change`, `pt-table-checksum`, and `pt-table-sync`, `--recursion-method=dsn` gives each server its own certificate paths when replicas do not share one certificate ([TLS in Percona Toolkit](https://www.percona.com/blog/unlocking-secure-connections-ssl-tls-support-in-percona-toolkit/)). `pt-secure-collect` encrypts a diagnostic bundle on the host. Toolkit 3.7.0 and earlier builds cannot decrypt each other's `pt-secure-collect` bundles. `pt-show-grants` exports accounts as SQL teams can review and replay.

**Adaptability for Emerging Workloads**

- **Before MySQL 8.4 or 9.7:** Teams install Percona Toolkit 3.7.0 or later so the commands match the new server. For MySQL 9.7, install that release from the Toolkit packages ([9.7 components](https://docs.percona.com/percona-distribution-for-mysql/9.7/components.html), [9.7 Toolkit updates](https://docs.percona.com/percona-server/9.7/percona-toolkit-9.7-updates.html)). `pt-upgrade` replays source logs on the candidate and reports row, warning, and timing differences. Use `pt-replica-find` and `pt-replica-restart` (`pt-slave-find` and `pt-slave-restart` still work). On 9.7, set `SOURCE_DELAY` instead of `pt-slave-delay` ([Toolkit updates for 9.7](https://docs.percona.com/percona-server/9.7/percona-toolkit-9.7-updates.html)).

### Sales enablement

**Elevator pitch**

Percona Toolkit changes a large MySQL table by copying rows into a new table and swapping it in, so reads and writes continue on the original. In-house database engineers run these commands, and so does the wider community. Contributions are reviewed, regression-tested, and named in the release notes. Replica checks and slow-log review use the same open source set, with no runtime license. Confirm backups before a schema change.

**Best-fit customer profiles**

- In-house database experts who already change large MySQL tables, check replicas before failover, and rank slow logs
- Practitioners who install and run those same commands on their own
- Teams whose schema-change, checksum, or archive commands live with one person
- Teams moving to MySQL 8.4 or 9.7, and estates that include MariaDB Server and need Toolkit to recognize it on connect

**Why bring it up**

A seller, a customer success manager, or an account executive brings this up when the account is planning a large schema change, a failover, an archive, a slow-log review, or a move to MySQL 8.4 or 9.7.

The customer keeps reads and writes moving during the `ALTER`, sees replica drift before failover, and has commands the whole team can run. There is no runtime license. Support engineers use the same commands, so a ticket starts from the procedure the customer already runs.

The account team hears about that work while the date is still a plan. The conversation shows whether the team they have can cover it, whether the commands live with one person, and whether Toolkit is current before the upgrade. When the change spans many tables and needs a rehearsal, Percona Expert Consulting and Services can scope it.

**Conversation starters**

- How do you change a large table without blocking reads and writes for the whole `ALTER`? (`pt-online-schema-change` copies rows to a new table and swaps it in. Confirm backups first. On Percona XtraDB Cluster, use InnoDB and `wsrep_OSU_method=TOI`.)
- How do you know a replica matches its source before you fail over? (`pt-table-checksum` finds drift, `pt-table-sync` reconciles it, and `pt-heartbeat` measures lag from a heartbeat table.)
- Is the schema change one table, or a program of many? (Treat the set as one rehearsed change. Confirm backups, then run `pt-online-schema-change`. On Percona XtraDB Cluster, use InnoDB and `wsrep_OSU_method=TOI`.)

**Public resources**

- [Percona Toolkit](https://www.percona.com/software/database-tools/percona-toolkit)
- [Percona Toolkit documentation](https://docs.percona.com/percona-toolkit/)
- [Percona Toolkit 3.7.1](https://percona.community/blog/2025/12/17/what-is-new-in-percona-toolkit-3.7.1/)
- [Percona Toolkit updates for MySQL 9.7](https://docs.percona.com/percona-server/9.7/percona-toolkit-9.7-updates.html)
