function ensureString(value, name) {
  if (typeof value !== "string" || !value.trim()) {
    throw new Error(`Expected non-empty string for ${name}`);
  }
}

/**
 * Appended to visible marker comments so readers can see trigger + docs.
 * Do not use with hidden machine-readable marker payloads (for example waiver JSON).
 */
function buildAutomationFooter(owner, repo, { workflowFile, eventName }) {
  ensureString(workflowFile, "automationFooter.workflowFile");
  if (!/^[a-z0-9][a-z0-9_.-]*\.ya?ml$/i.test(workflowFile)) {
    throw new Error(
      "automationFooter.workflowFile must be a workflow filename (example: smart-suggestions.yml)",
    );
  }

  const base = `https://github.com/${owner}/${repo}`;
  const wfUrl = `${base}/blob/main/.github/workflows/${workflowFile}`;
  const automationDocUrl = `${base}/blob/main/AUTOMATION.md#pr-comment-upsert-standard`;
  const automationReadmeUrl = `${base}/blob/main/automation/README.md`;

  const trigger =
    typeof eventName === "string" && eventName.trim()
      ? `Triggered by \`${eventName.trim()}\`. `
      : "";

  return (
    `\n\n---\n\n<sub>${trigger}` +
    `Workflow [\`${workflowFile}\`](${wfUrl}). ` +
    `Docs: [AUTOMATION.md](${automationDocUrl}), [\`automation/README.md\`](${automationReadmeUrl}).</sub>`
  );
}

module.exports = async function upsertMarkerComment({
  github,
  core,
  owner,
  repo,
  issue_number,
  marker,
  body,
  automationFooter,
  perPage = 100,
}) {
  if (!github) {
    throw new Error("Expected github client");
  }
  if (!core) {
    throw new Error("Expected core client");
  }

  ensureString(owner, "owner");
  ensureString(repo, "repo");
  ensureString(marker, "marker");
  ensureString(body, "body");

  if (!Number.isInteger(issue_number) || issue_number <= 0) {
    throw new Error("Expected positive integer issue_number");
  }

  const effectiveBody = automationFooter
    ? body + buildAutomationFooter(owner, repo, automationFooter)
    : body;

  const comments = await github.paginate(github.rest.issues.listComments, {
    owner,
    repo,
    issue_number,
    per_page: perPage,
  });
  const markerComments = comments
    .filter((c) => c.body && c.body.includes(marker))
    .sort((a, b) => {
      // Marker comments are append-only state records, select the latest created
      // comment to avoid stale payloads winning due to incidental edits.
      const aTime = Date.parse(a.created_at || "") || 0;
      const bTime = Date.parse(b.created_at || "") || 0;
      if (bTime !== aTime) {
        return bTime - aTime;
      }
      return (Number(b.id) || 0) - (Number(a.id) || 0);
    });
  const existing = markerComments[0];

  if (markerComments.length > 1) {
    core.warning(
      `Found ${markerComments.length} comments with marker ${marker}; updating latest comment ${existing.id}.`,
    );
  }

  if (existing) {
    await github.rest.issues.updateComment({
      owner,
      repo,
      comment_id: existing.id,
      body: effectiveBody,
    });
    core.info(
      `Updated marker comment ${existing.id} for issue ${issue_number} (${marker}).`,
    );
    return { action: "update", comment_id: existing.id };
  }

  const created = await github.rest.issues.createComment({
    owner,
    repo,
    issue_number,
    body: effectiveBody,
  });
  core.info(
    `Created marker comment ${created.data.id} for issue ${issue_number} (${marker}).`,
  );
  return { action: "create", comment_id: created.data.id };
};
