#!/usr/bin/env python3
"""Require justification fields when PR adds markdown files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from governance_waiver import (
    CHECK_NEW_FILE_GATE,
    check_is_waived,
    load_governance_waiver,
    waiver_note_md,
)

REQUIRED_HEADINGS = [
    "### Existing files reviewed first",
    "### Exact gap not covered by existing files",
    "### Why this must be a new canonical file",
    "### Owner and maintenance plan",
    "### Decomposition and propagation plan",
]

EXCLUDED_PREFIXES = (".github/ISSUE_TEMPLATE/", ".cursor/")


def build_pr_body_scaffold() -> str:
    lines = ["## New markdown file gate (required only when adding new `.md` files)", ""]
    prompts = {
        "### Existing files reviewed first": "- List the specific files you reviewed and what each one does.",
        "### Exact gap not covered by existing files": "- Explain what is still missing after reviewing existing canonical files.",
        "### Why this must be a new canonical file": "- State why editing an existing file is not sufficient.",
        "### Owner and maintenance plan": "- Name the owner and how this file will stay accurate over time.",
        "### Decomposition and propagation plan": "- List related files and downstream assets that may need updates.",
    }
    for heading in REQUIRED_HEADINGS:
        lines.append(heading)
        lines.append("")
        lines.append(
            prompts.get(
                heading,
                "- Describe the required justification for this section with specific details.",
            )
        )
        lines.append("")
    return "\n".join(lines).rstrip()


def git_added_markdown(base_ref: str, head_ref: str) -> list[str]:
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-status", f"{base_ref}...{head_ref}"],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        output = subprocess.check_output(["git", "diff", "--name-status"], text=True)

    files: list[str] = []
    for line in output.splitlines():
        parts = line.split("\t", maxsplit=1)
        if len(parts) != 2:
            continue
        status, path = parts
        path = path.strip()
        if status.strip().startswith("A") and path.endswith(".md") and not path.endswith(".draft.md"):
            if path.startswith(EXCLUDED_PREFIXES):
                continue
            files.append(path)
    return files


def section_content(body: str, heading: str) -> str:
    escaped = re.escape(heading)
    pattern = re.compile(rf"{escaped}\s*\n(.*?)(?=\n### |\Z)", re.DOTALL)
    match = pattern.search(body)
    return (match.group(1).strip() if match else "").strip()


def is_meaningful(text: str) -> bool:
    if not text:
        return False
    lowered = re.sub(r"\s+", " ", text).strip().lower()
    if lowered in {"n/a", "na", "none", "tbd", "todo"}:
        return False
    if "<!--" in lowered:
        return False
    return len(lowered) >= 20


def build_report(files: list[str], missing_or_weak: list[str]) -> str:
    lines = ["## New File Governance Check", ""]
    lines.append(f"- Added markdown files: {len(files)}")
    for path in files:
        lines.append(f"  - `{path}`")
    lines.append("")
    if not missing_or_weak:
        lines.append("All required justification sections are present and non-empty.")
        return "\n".join(lines) + "\n"
    lines.append("Missing or insufficient required sections:")
    for item in missing_or_weak:
        lines.append(f"- {item}")
    lines.append("")
    lines.append(
        "Copy and paste the scaffold below into your PR body, then replace placeholders with specific details:"
    )
    lines.append("")
    lines.append("```md")
    lines.append(build_pr_body_scaffold())
    lines.append("```")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate PR template fields for new markdown files.")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--pr-body-file", required=True)
    parser.add_argument("--output-md", default="new-file-gate-report.md")
    parser.add_argument("--waiver-file", default="", help="Optional governance waiver JSON path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    body_path = Path(args.pr_body_file)
    body = body_path.read_text(encoding="utf-8") if body_path.exists() else ""

    added = git_added_markdown(args.base, args.head)
    if not added:
        report = "## New File Governance Check\n\nNo added markdown files detected.\n"
        Path(args.output_md).write_text(report, encoding="utf-8")
        print(report)
        return 0

    failed: list[str] = []
    for heading in REQUIRED_HEADINGS:
        content = section_content(body, heading)
        if not is_meaningful(content):
            failed.append(heading)

    report = build_report(added, failed)
    exit_code = 1 if failed else 0

    waiver_path = Path(args.waiver_file) if args.waiver_file else None
    waive_all, waived_checks, reset_checks = load_governance_waiver(waiver_path)
    if exit_code != 0 and check_is_waived(
        CHECK_NEW_FILE_GATE,
        waive_all,
        waived_checks,
        reset_checks,
    ):
        report = report.rstrip() + waiver_note_md(CHECK_NEW_FILE_GATE)
        exit_code = 0

    Path(args.output_md).write_text(report, encoding="utf-8")
    print(report)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
