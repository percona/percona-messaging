function ensureString(value, name) {
  if (typeof value !== "string" || !value.trim()) {
    throw new Error(`Expected non-empty string for ${name}`);
  }
}

module.exports = async function upsertMarkerComment({
  github,
  core,
  owner,
  repo,
  issue_number,
  marker,
  body,
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

  const comments = await github.paginate(github.rest.issues.listComments, {
    owner,
    repo,
    issue_number,
    per_page: perPage,
  });
  const markerComments = comments
    .filter((c) => c.body && c.body.includes(marker))
    .sort((a, b) => {
      const aTime = Date.parse(a.updated_at || a.created_at || "") || 0;
      const bTime = Date.parse(b.updated_at || b.created_at || "") || 0;
      return bTime - aTime;
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
      body,
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
    body,
  });
  core.info(
    `Created marker comment ${created.data.id} for issue ${issue_number} (${marker}).`,
  );
  return { action: "create", comment_id: created.data.id };
};
