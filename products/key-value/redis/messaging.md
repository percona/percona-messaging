# Percona for Redis: Messaging

## Percona for Redis {#percona-for-redis}

For platform, SRE, and DevOps teams running traditional key/value and in-memory workloads on Redis across on-premises, cloud, and hybrid environments, Percona provides Expert Support, Expert Consulting and Services, operational guidance, PMM observability, and an optional path to Valkey when the customer chooses it. Unlike a forced migration mandate or treating Redis as only a temporary stop, Percona supports stay on Redis, migrate to Valkey, or run hybrid, based on stability, cost, and compliance. Percona supports Redis users with operational expertise; Percona does not develop Redis software.

Staying on Redis is a first-class outcome. Transitioning to Valkey remains available when the customer chooses it.

See also the [key/value overview](../messaging.md). For Valkey-led messaging (Redis is not framed as the destination), see [Percona for Valkey](../valkey/messaging.md).

### Customer Challenges and Value Alignment: Redis

**Optimized TCO**

- **Keep using Redis:** Teams that are happy with Redis the way it is, want to stay with their Redis vendor, use Azure’s managed Redis, or don’t need to share Redis with others can keep running Redis. Percona can still help: Expert Support when needed, and PMM so teams can see how things are running.
- **Redis costs more when everything lives in memory**: Redis keeps its data in RAM, and RAM is expensive. Percona Experts help teams use less of it by tuning how memory is set aside, what gets removed when space runs out, and how copies of the data stay in sync. Teams can still hit the same speed goals, whether they stay on Redis or look at Valkey later.

**Performance and Reliability at Scale**

- **Same jobs as Valkey:** Caching, sessions, pub/sub, queues, rate limiting, and fast key/value work. On important systems, the cache is required for production. It is not an optional speed boost.
- **Less load on the main database:** Redis often sits in front of MySQL, PostgreSQL, or MongoDB-compatible systems. A well-tuned cache helps the app handle more traffic and cuts read load on those databases. That can delay expensive scale-out.
- **Tuning and high availability:** Percona Experts tune production Redis so it stays steady under heavy use and during failures. Most platform teams do not have deep in-memory ops skills. 24×7 Expert Support and consulting cover escalation, architecture, migration, and health checks.
- **PMM visibility:** PMM has Redis dashboards for commands, memory, clients, latency, replication, and slowlog.

**Security, Sovereignty, and Compliance**

- **Support on customer-controlled Redis:** Encryption, access controls, and data location stay on infrastructure the customer runs. Expert Support helps with setup and incident response.
- **Clear licensing, no forced move:** Redis 7.4–7.9 stay source-available. Redis 8 and later use AGPLv3 (open source), plus RSALv2/SSPLv1 options. Teams that accept that can stay on Redis. Teams that want Linux Foundation multi-vendor governance and BSD 3-Clause licensing can evaluate at Valkey on their own timeline.

**AI, Future Readiness, and Portability**

- **Evaluate, validate, and migrate:** Percona supports Redis and Valkey during the move, so production risk stays under control for those who choose to move.
- **Version gate:** Persistence formats split at the Redis 7.2.4 fork. Redis 7.4 and later cannot cleanly file-copy into Valkey. The clean path is a replication cutover from Redis 7.2 or earlier, with high availability and a rollback rehearsal before cutover.

### Sales enablement

**Elevator pitch**

Percona supports Redis for traditional key/value work with Expert Support and PMM on platform-led estates. When governance, memory cost, or operating model favor an open alternative, Percona offers a paced path to Valkey: evaluate, validate, then migrate. Staying on Redis is still a valid outcome.

**Conversation starters**

Would support for both Redis and Valkey during a staged move lower cutover risk for this estate?
For Azure-managed Redis, or a strong Redis vendor relationship, what would “good” look like if you stay on Redis with Percona Expert Support?
- Who runs Redis today: platform engineering, SRE, or a database team?
- Are you embedding or redistributing Redis (product/SaaS), or is it internal-only?
- Are you on self-managed, Redis Enterprise, or a cloud managed service (Azure / AWS / GCP)?
- Is Redis fine in day-to-day ops, or is the pressure from cost, governance, missing modules, or a managed-service lock-in?
- What is the main pressure this quarter: RAM cost, support coverage, governance / license trust, or vendor lock-in?
- Is the cache required for production? How much memory are you buying relative to the traffic it handles?
- Do you need Search, JSON, or active-active geo? Would those needs make Redis the safer near-term choice?
- Which Redis version are you on?
- For Azure-managed Redis or strong vendor-relationship cases, what would "good" look like if you stay on Redis with Percona Expert Support?

**Public resources**

- [Percona Support for Valkey and Redis](https://www.percona.com/valkey-redis/support/)
- [Percona Expert Consulting and Services](https://www.percona.com/services/consulting)
- [PMM Valkey and Redis monitoring](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/install-pmm-client/connect-database/valkey-redis.html)
