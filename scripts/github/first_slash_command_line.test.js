"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const {
  firstNonEmptyLine,
  isImpactCommandLine,
  isGovernanceCommandLine,
  impactWaiverIntent,
} = require("./first_slash_command_line.js");

test("Feranmi second comment: leading CRLF still waives all", () => {
  const body = "\r\n/impact-ok all\r\n\r\n";
  assert.equal(firstNonEmptyLine(body), "/impact-ok all");
  assert.equal(isImpactCommandLine(firstNonEmptyLine(body)), true);
  const intent = impactWaiverIntent(body);
  assert.deepEqual(intent, {
    kind: "command",
    command: "ok",
    all: true,
    arg: "",
  });
});

test("Feranmi first comment: /ok-impact all waives all", () => {
  const intent = impactWaiverIntent("/ok-impact all");
  assert.deepEqual(intent, {
    kind: "command",
    command: "ok",
    all: true,
    arg: "",
  });
});

test("Briana comment: no leading newline still waives all", () => {
  const intent = impactWaiverIntent("/impact-ok all");
  assert.equal(intent.all, true);
  assert.equal(intent.command, "ok");
});

test("job would skip quoted command below prose", () => {
  assert.equal(isImpactCommandLine(firstNonEmptyLine("Please run\n/impact-ok all\n")), false);
  assert.equal(impactWaiverIntent("Please run\n/impact-ok all\n").kind, "skip");
});

test("GitHub contains() still matches leading-blank impact comments", () => {
  const body = "\r\n/impact-ok all\r\n\r\n";
  const jobIf =
    body.toLowerCase().includes("/impact-ok") ||
    body.toLowerCase().includes("/impact-reset") ||
    body.toLowerCase().includes("/impact-all") ||
    body.toLowerCase().includes("/ok-impact");
  assert.equal(jobIf, true);
});

test("GitHub contains() matches /ok-impact without /impact-ok as a prefix", () => {
  const body = "/ok-impact all";
  const jobIf =
    body.toLowerCase().includes("/impact-ok") ||
    body.toLowerCase().includes("/impact-reset") ||
    body.toLowerCase().includes("/impact-all") ||
    body.toLowerCase().includes("/ok-impact");
  assert.equal(jobIf, true);
});

test("governance first non-empty line, no reversed alias", () => {
  const line = firstNonEmptyLine("\r\n/governance-ok all\r\n");
  assert.equal(isGovernanceCommandLine(line), true);
  assert.equal(isGovernanceCommandLine("/ok-governance all"), false);
});

test("path waiver still works after a leading blank line", () => {
  const intent = impactWaiverIntent(
    "\n/impact-ok reference/canonical-naming.md extra note",
  );
  assert.deepEqual(intent, {
    kind: "command",
    command: "ok",
    all: false,
    arg: "reference/canonical-naming.md",
  });
});
