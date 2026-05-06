/**
 * Scheduled PR reviewer-queue reminder (issue #16).
 * See AUTOMATION.md -> Reviewer queue SLA reminder.
 */

const upsertMarkerComment = require("./upsert_marker_comment.js");

const MARKER = "<!-- messaging-pr-review-sla-reminder -->";
const STATE_PREFIX = "<!-- messaging-pr-review-sla-state:v1 ";
const STATE_SUFFIX = " -->";

function skipLabelNames() {
  const raw = process.env.SKIP_LABELS || "no-review-sla-nudge";
  return raw
    .split(",")
    .map((s) => s.trim().toLowerCase())
    .filter(Boolean);
}

function businessDaysElapsedSince(sinceIso) {
  const since = new Date(sinceIso);
  const now = new Date();
  if (Number.isNaN(since.getTime())) {
    return 0;
  }
  let count = 0;
  const cursor = new Date(
    Date.UTC(since.getUTCFullYear(), since.getUTCMonth(), since.getUTCDate()),
  );
  const end = new Date(
    Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()),
  );
  cursor.setUTCDate(cursor.getUTCDate() + 1);
  while (cursor <= end) {
    const wd = cursor.getUTCDay();
    if (wd !== 0 && wd !== 6) {
      count += 1;
    }
    cursor.setUTCDate(cursor.getUTCDate() + 1);
  }
  return count;
}

function parseState(body) {
  if (!body || !body.includes(STATE_PREFIX)) {
    return null;
  }
  const start = body.indexOf(STATE_PREFIX);
  const end = body.indexOf(STATE_SUFFIX, start);
  if (end === -1) {
    return null;
  }
  try {
    const json = body.slice(start + STATE_PREFIX.length, end).trim();
    return JSON.parse(json);
  } catch {
    return null;
  }
}

function stripStateBlock(body) {
  const start = body.indexOf(STATE_PREFIX);
  if (start === -1) {
    return body.trimEnd();
  }
  const end = body.indexOf(STATE_SUFFIX, start);
  if (end === -1) {
    return body.trimEnd();
  }
  return (
    body.slice(0, start).trimEnd() + body.slice(end + STATE_SUFFIX.length).trimEnd()
  ).trimEnd();
}

function injectState(body, baselineIso) {
  const stripped = stripStateBlock(body);
  const payload = `${STATE_PREFIX}${JSON.stringify({
    stallBaseline: baselineIso,
  })}${STATE_SUFFIX}`;
  return `${stripped}\n\n${payload}\n`;
}

async function listOpenPulls({ github, owner, repo }) {
  return github.paginate(github.rest.pulls.list, {
    owner,
    repo,
    state: "open",
    per_page: 100,
  });
}

async function deleteMarkerComments({ github, owner, repo, issue_number }) {
  const comments = await github.paginate(github.rest.issues.listComments, {
    owner,
    repo,
    issue_number,
    per_page: 100,
  });
  const hits = comments.filter((c) => c.body && c.body.includes(MARKER));
  for (const c of hits) {
    await github.rest.issues.deleteComment({
      owner,
      repo,
      comment_id: c.id,
    });
    core.info(`Removed SLA reminder comment ${c.id} on PR #${issue_number}.`);
  }
}

function buildMentionLine(owner, requestedReviewers) {
  const users = (requestedReviewers.users || [])
    .map((u) => `@${u.login}`)
    .filter(Boolean);
  const teams = (requestedReviewers.teams || [])
    .map((t) => `@${owner}/${t.slug}`)
    .filter(Boolean);
  const all = [...users, ...teams];
  if (!all.length) {
    return "";
  }
  return `**Requested reviewers:** ${all.join(" ")}\n\n`;
}

module.exports = async function run({ github, core, context, threshold }) {
  const { owner, repo } = context.repo;
  const skipLabels = skipLabelNames();

  const pulls = await listOpenPulls({ github, owner, repo });
  core.info(`Scanning ${pulls.length} open pull requests.`);

  let nudged = 0;
  let skipped = 0;
  let cleaned = 0;

  for (const pr of pulls) {
    const issue_number = pr.number;

    if (pr.draft) {
      skipped += 1;
      continue;
    }

    if (
      pr.head &&
      pr.base &&
      pr.head.repo &&
      pr.base.repo &&
      pr.head.repo.full_name !== pr.base.repo.full_name
    ) {
      core.info(`Skipping fork PR #${issue_number}.`);
      skipped += 1;
      continue;
    }

    const labels = (pr.labels || []).map((l) =>
      String(l.name || "").toLowerCase(),
    );
    if (skipLabels.some((s) => labels.includes(s))) {
      core.info(`Skipping PR #${issue_number} (skip label).`);
      skipped += 1;
      continue;
    }

    const reviews = await github.paginate(github.rest.pulls.listReviews, {
      owner,
      repo,
      pull_number: issue_number,
      per_page: 100,
    });

    let lastReviewAtMs = 0;
    for (const r of reviews) {
      if (!r.submitted_at) {
        continue;
      }
      const t = Date.parse(r.submitted_at);
      if (!Number.isNaN(t) && t > lastReviewAtMs) {
        lastReviewAtMs = t;
      }
    }

    const baselineIso =
      lastReviewAtMs > 0
        ? new Date(lastReviewAtMs).toISOString()
        : new Date(pr.created_at).toISOString();

    const bizDays = businessDaysElapsedSince(baselineIso);
    const stalled = bizDays >= threshold;

    if (!stalled) {
      await deleteMarkerComments({ github, owner, repo, issue_number });
      cleaned += 1;
      continue;
    }

    const detail = await github.rest.pulls.get({
      owner,
      repo,
      pull_number: issue_number,
    });

    const comments = await github.paginate(github.rest.issues.listComments, {
      owner,
      repo,
      issue_number,
      per_page: 100,
    });
    const markerComments = comments
      .filter((c) => c.body && c.body.includes(MARKER))
      .sort((a, b) => {
        const aTime = Date.parse(a.created_at || "") || 0;
        const bTime = Date.parse(b.created_at || "") || 0;
        if (bTime !== aTime) {
          return bTime - aTime;
        }
        return (Number(b.id) || 0) - (Number(a.id) || 0);
      });
    const existing = markerComments[0];
    const prevState = existing ? parseState(existing.body) : null;
    if (
      prevState &&
      typeof prevState.stallBaseline === "string" &&
      prevState.stallBaseline === baselineIso
    ) {
      core.info(
        `PR #${issue_number} still stalled; reminder already sent for baseline ${baselineIso}.`,
      );
      skipped += 1;
      continue;
    }

    const reviewers = detail.data.requested_reviewers || [];
    const requestedTeams = detail.data.requested_teams || [];
    const mentions = buildMentionLine(owner, {
      users: reviewers,
      teams: requestedTeams,
    });

    const checklist =
      `This pull request has been waiting for reviewer activity for **${bizDays}** business days ` +
      `(threshold **${threshold}**). Please take a look when you can.\n\n` +
      "**Quick checklist for reviewers**\n\n" +
      "- [ ] Diff matches the stated intent of the PR\n" +
      "- [ ] Canonical messaging rules and governance checks are addressed\n" +
      "- [ ] Approve, comment, or request changes so the author gets a clear signal\n\n";

    let body = `${MARKER}\n${mentions}${checklist}`;
    body = injectState(body, baselineIso);

    await upsertMarkerComment({
      github,
      core,
      owner,
      repo,
      issue_number,
      marker: MARKER,
      body,
      automationFooter: {
        workflowFile: "pr-reviewer-sla-reminder.yml",
        eventName: context.eventName,
      },
    });
    nudged += 1;
  }

  core.info(
    `Done. Nudged: ${nudged}, skipped (no action): ${skipped}, cleaned/unstalled passes: ${cleaned}.`,
  );
};
