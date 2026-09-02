"use strict";

/**
 * Shared parser for maintainer slash commands (`/impact-*`, `/governance-*`).
 *
 * Two behaviors exist because both have burned maintainers on real PRs:
 * the command is read from the first non-empty line (a comment that starts
 * with a blank line used to skip the job), and reversed forms such as
 * `/ok-impact` are accepted as aliases for `/impact-ok`.
 */

const VERBS = "ok|reset|all";

function firstNonEmptyLine(body) {
  return (
    String(body || "")
      .split(/\r?\n/)
      .map((line) => line.replace(/^\uFEFF/, "").trim())
      .find(Boolean) || ""
  );
}

function commandPattern(namespace) {
  return new RegExp(
    `^\\/(?:${namespace}-(${VERBS})|(${VERBS})-${namespace})\\b\\s*(.*)$`,
    "i",
  );
}

/**
 * @returns {{kind: "command"|"near-miss"|"none", verb: string, argument: string,
 *   all: boolean, line: string}} `near-miss` means the line looks like an
 *   attempt at this command family but is not usable, so callers can hint.
 */
function parseSlashCommand(body, namespace) {
  const line = firstNonEmptyLine(body);
  const match = line.match(commandPattern(namespace));

  if (!match) {
    const looksLikeAttempt =
      line.startsWith("/") && line.toLowerCase().includes(namespace);
    return {
      kind: looksLikeAttempt ? "near-miss" : "none",
      verb: "",
      argument: "",
      all: false,
      line,
    };
  }

  let verb = (match[1] || match[2]).toLowerCase();
  const argument = (match[3] || "").trim().split(/\s+/).filter(Boolean)[0] || "";

  // `/<namespace>-all` is shorthand for the waive-all form of `ok`.
  if (verb === "all") {
    return { kind: "command", verb: "ok", argument: "", all: true, line };
  }

  const all = !argument || argument.toLowerCase() === "all";
  return { kind: "command", verb, argument: all ? "" : argument, all, line };
}

/**
 * Canonical `/<namespace>-<verb> <argument>` form, so downstream workflow
 * parsers never see aliases, leading blank lines, or trailing discussion text.
 */
function canonicalCommandLine(parsed, namespace) {
  if (!parsed || parsed.kind !== "command") {
    return "";
  }
  const argument = parsed.all ? "all" : parsed.argument;
  return `/${namespace}-${parsed.verb} ${argument}`;
}

module.exports = {
  firstNonEmptyLine,
  parseSlashCommand,
  canonicalCommandLine,
};
