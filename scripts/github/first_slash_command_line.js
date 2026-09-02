"use strict";

/**
 * First non-empty line of a PR comment. A leading blank line used to skip the
 * slash-command job because the workflow `if` used startsWith on the raw body.
 */
function firstNonEmptyLine(body) {
  return (
    String(body || "")
      .split(/\r?\n/)
      .map((line) => line.replace(/^\uFEFF/, "").trim())
      .find(Boolean) || ""
  );
}

/** `/ok-impact` is the only reversed alias. `/impact-all` is handled later. */
function normalizeImpactLine(line) {
  return String(line || "").replace(/^\/ok-impact\b/i, "/impact-ok");
}

function isImpactCommandLine(line) {
  return /^\/impact-(ok|reset|all)\b/i.test(normalizeImpactLine(line));
}

function isGovernanceCommandLine(line) {
  return /^\/governance-(ok|reset|all)\b/i.test(String(line || ""));
}

/**
 * Same argument rules as the merge step: first token after the verb, `all` if
 * missing or the word all. Used so tests can check the real comment payloads.
 */
function impactWaiverIntent(body) {
  let line = normalizeImpactLine(firstNonEmptyLine(body));
  if (!isImpactCommandLine(line)) {
    return { kind: "skip" };
  }
  if (/^\/impact-all\b/i.test(line)) {
    line = line.replace(/^\/impact-all\b\s*/i, "/impact-ok all ");
  }
  const match = line.match(/^\/impact-(ok|reset)\b\s*(.*)$/i);
  if (!match) {
    return { kind: "unsupported" };
  }
  const command = match[1].toLowerCase();
  const firstToken =
    (match[2] || "").trim().split(/\s+/).filter(Boolean)[0] || "";
  const all = !firstToken || firstToken.toLowerCase() === "all";
  return { kind: "command", command, all, arg: all ? "" : firstToken };
}

module.exports = {
  firstNonEmptyLine,
  normalizeImpactLine,
  isImpactCommandLine,
  isGovernanceCommandLine,
  impactWaiverIntent,
};
