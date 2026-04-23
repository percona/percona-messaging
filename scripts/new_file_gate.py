#!/usr/bin/env python3
"""Require justification fields when PR adds markdown files."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

REQUIRED_HEADINGS = [
    "### Existing files reviewed first",
    "### Exact gap not covered by existing files",
    "### Why this must be a new canonical file",
    "### Owner and maintenance plan",
    "### Decomposition and propagation plan",
]

EXCLUDED_PREFIXES = (".github/ISSUE_TEMPLATE/", ".cursor/")


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
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate PR template fields for new markdown files.")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--pr-body-file", required=True)
    parser.add_argument("--output-md", default="new-file-gate-report.md")
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
    Path(args.output_md).write_text(report, encoding="utf-8")
    print(report)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
