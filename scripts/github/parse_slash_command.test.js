"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const {
  parseSlashCommand,
  canonicalCommandLine,
} = require("./parse_slash_command.js");

function parseImpact(body) {
  const parsed = parseSlashCommand(body, "impact");
  return { ...parsed, canonical: canonicalCommandLine(parsed, "impact") };
}

test("leading blank lines and CRLF still resolve to waive-all", () => {
  const parsed = parseImpact("\r\n/impact-ok all\r\n\r\n");
  assert.equal(parsed.kind, "command");
  assert.equal(parsed.all, true);
  assert.equal(parsed.canonical, "/impact-ok all");
});

test("reversed alias /ok-impact is accepted", () => {
  const parsed = parseImpact("/ok-impact all");
  assert.equal(parsed.kind, "command");
  assert.equal(parsed.verb, "ok");
  assert.equal(parsed.canonical, "/impact-ok all");
});

test("/impact-all is shorthand for the waive-all form of ok", () => {
  const parsed = parseImpact("/impact-all because the rule misfires");
  assert.equal(parsed.verb, "ok");
  assert.equal(parsed.all, true);
  assert.equal(parsed.canonical, "/impact-ok all");
});

test("bare command with no argument waives all", () => {
  assert.equal(parseImpact("/impact-ok").canonical, "/impact-ok all");
});

test("path argument survives and trailing notes are dropped", () => {
  const parsed = parseImpact(
    "/impact-ok reference/canonical-naming.md no edit needed here",
  );
  assert.equal(parsed.all, false);
  assert.equal(parsed.argument, "reference/canonical-naming.md");
  assert.equal(parsed.canonical, "/impact-ok reference/canonical-naming.md");
});

test("reset keeps its verb and path", () => {
  const parsed = parseImpact("/impact-reset reference/banned-terms.md");
  assert.equal(parsed.verb, "reset");
  assert.equal(parsed.canonical, "/impact-reset reference/banned-terms.md");
});

test("unknown suffix is a near miss so the workflow can hint", () => {
  const parsed = parseImpact("/impact-approve all");
  assert.equal(parsed.kind, "near-miss");
  assert.equal(parsed.canonical, "");
});

test("prose mentioning a command is ignored, not hinted", () => {
  assert.equal(parseImpact("Please run\n/impact-ok all\n").kind, "none");
});

test("governance shares the parser and its aliases", () => {
  const parsed = parseSlashCommand("\r\n/ok-governance new-file\r\n", "governance");
  assert.equal(parsed.verb, "ok");
  assert.equal(parsed.argument, "new-file");
  assert.equal(
    canonicalCommandLine(parsed, "governance"),
    "/governance-ok new-file",
  );
});
