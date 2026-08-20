## Valkey / Redis Performance Tuning

Latency spikes in Redis or Valkey are usually about data structure choice or persistence overhead, not the command itself. A command that is fast in isolation can still cause latency spikes if it is colliding with an AOF rewrite or a poorly sized eviction policy.

This engagement targets up to 5 specific issues you have already identified, and tests every fix in your environment before it goes to production.

## Deliverables

- Review of up to 5 identified performance issues or command patterns you specify at kickoff
- Analysis of data structure usage, eviction policy, persistence configuration (RDB/AOF), and metrics via PMM
- Review of command complexity (O(N) operations on large collections) contributing to latency
- Testing of proposed changes in your provided test environment
- Document detailing suggested changes and results achieved in testing
- Production review of recommended changes with your points of contact, plus a findings and recommendations report
- Optional: assistance implementing recommendations in production during a scheduled time

## Who it is for

Scoped to 1–5 specific performance issues you can name at kickoff. If you do not yet know what is causing the latency, our [Health Audit](../health-audit/messaging.md) is a better starting point. This engagement assumes that production access and a representative test environment are both available from day one.

## Outcome

Specific, tested fixes for the latency or memory issues you flagged. You will know whether the spike is a data structure choice, a persistence operation colliding with your traffic, or a command that is O(N) on a collection that has grown past what it was designed for.

**CTA:** Fix the latency spike before it becomes a pattern.
