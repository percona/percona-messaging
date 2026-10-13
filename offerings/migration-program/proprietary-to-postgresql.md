# Proprietary Database Migration to PostgreSQL

**Starting from:** $5,000 for the initial assessment

The Oracle or SQL Server renewal invoice, with its per-core licensing, RAC, and Enterprise Edition support, finally became harder to justify than the risk of moving off it. PostgreSQL is a strong open source migration target. The hard part is knowing what is actually in the schema: PL/SQL or T-SQL procedures, custom data types, and the dependencies wired across it all. Some applications also do not support PostgreSQL out of the box.

We start with a detailed assessment, delivered through the Database Migration Assessment Tool (DMAT) via our migration partnership with HexaCluster, to give you that picture in code-level detail before you commit to a migration timeline or budget. The assessment adds the data component to the initial cost-based migration decision: how long a fleet move is likely to take, and how much software and expertise it will require.

This assessment is one packaged entry point under [Migration and Modernization](messaging.md), not the full migration and modernization catalog. Full cutover and build are scoped separately after the assessment, often as a [Database Migrations](database-migrations.md) engagement or a broader custom Migration and Modernization program.

## FAQ

### What is DMAT, and why start with the assessment for Oracle, SQL Server, or DB2?

These projects can be very complex. DMAT is the Database Migration Assessment Tool, delivered through our migration partnership with HexaCluster. It analyzes your schema in code-level detail: object counts, stored procedure and trigger complexity, proprietary data type usage, and compatibility scoring for what converts cleanly to PostgreSQL versus what needs manual rework. You get an effort estimate built from your actual environment, not a vendor's average case, before you commit budget or a timeline. The default path afterward is native, fully open source PostgreSQL; where DMAT finds heavy stored-procedure dependency, a compatibility layer is available to fast-track cutover.

### Does this include the full migration?

No. This is an assessment engagement. Cutover and the full migration build are scoped separately based on what the assessment finds.

## Deliverables

- Assessment of your Oracle, SQL Server, or DB2 schema, covering object counts, stored procedure and trigger complexity, and proprietary data type usage
- Dependent applications code and compatibility analysis
- Compatibility scoring, identifying which objects convert cleanly to PostgreSQL and which require manual rework (if any)
- Effort estimation and complexity report, broken down by schema object type (tables, views, procedures, packages, triggers)
- Migration path recommendation, including where HexaCluster's Oracle-compatibility tooling applies to reduce application-side rework
- Findings rundown with your team, plus a scoped proposal for the full migration engagement if you choose to proceed

## Who it is for

Built for teams running Oracle, Microsoft SQL Server, or IBM DB2 who are evaluating a move to PostgreSQL to get out from under proprietary licensing costs. The default path is native PostgreSQL: rewriting PL/SQL or T-SQL logic into standard, fully open source PostgreSQL, no compatibility layer required. Where the assessment turns up heavy stored-procedure or proprietary-type dependency and a full rewrite is not realistic on your timeline, you will have the option to add HexaCluster's HexaBridge compatibility layer as a way to fast-track cutover without rewriting the application.

## Outcome

A concrete, code-level answer to how hard this migration actually is, before you have committed a budget or a timeline to leadership. You will know which parts of your schema convert cleanly and which parts need real expert effort, so the migration proposal that follows is based on your actual environment, not a vendor's average case.

**CTA:** Price the migration before you commit.
