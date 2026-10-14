# Products

This directory contains product and database-specific messaging.

## Structure

Each product area includes `messaging.md` for canonical product framing. Competitive positioning and internal talk tracks belong in private execution systems, not in this repository (see [reference/content-governance.md](../reference/content-governance.md)).

Current product areas include MySQL, MariaDB, PostgreSQL, MongoDB, key/value workloads (Valkey and Redis siblings under `products/key-value/`), PMM, Operators, and Percona Database Service ([messaging](database-service/messaging.md)). Percona Database Service (PDS) is a separate tool. This early look creates a MySQL database on a Kubernetes cluster you connect, with the Percona Operator for MySQL underneath. It is not a finished product. MySQL only, not PostgreSQL or MongoDB. It does not replace Percona Monitoring and Management (PMM).

Engine-specific Support, ExpertOps, or Consulting differentiators belong in the relevant product `messaging.md` pillar bullets (what ships in the distribution, what experts cover in production, and customer outcomes). Keep `offerings/` files cross-engine.

The key/value family uses a shared parent (`products/key-value/messaging.md`) with separate Valkey and Redis modules.
