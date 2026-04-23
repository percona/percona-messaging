#!/usr/bin/env python3
"""Ensure newly added markdown docs are discoverable from navigation docs."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

EXCLUDED_PREFIXES = (
    ".github/",
    ".cursor/",
)
INDEX_FILES = {
    "README.md",
    "CONTRIBUTING.md",
}


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
        if not status.startswith("A"):
            continue
        if not path.endswith(".md") or path.endswith(".draft.md"):
            continue
        if path.startswith(EXCLUDED_PREFIXES):
            continue
        files.append(path)
    return files


def all_markdown_files() -> list[Path]:
    root = Path(".")
    return [p for p in root.rglob("*.md") if ".git" not in p.parts and ".venv" not in p.parts]


def path_is_discoverable(doc_path: str, md_files: list[Path]) -> bool:
    for md in md_files:
        rel = md.as_posix()
        if rel == doc_path:
            continue
        text = md.read_text(encoding="utf-8")
        if doc_path in text:
            return True
        if md.name in INDEX_FILES and Path(doc_path).name in text:
            return True
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check that new docs are linked from index docs.")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--output-md", default="doc-coverage-report.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    added = git_added_markdown(args.base, args.head)
    if not added:
        report = "## Doc Coverage Check\n\nNo new markdown docs detected.\n"
        Path(args.output_md).write_text(report, encoding="utf-8")
        print(report)
        return 0

    md_files = all_markdown_files()
    missing = [path for path in added if not path_is_discoverable(path, md_files)]

    lines = ["## Doc Coverage Check", "", f"- New markdown docs: {len(added)}"]
    for path in added:
        lines.append(f"  - `{path}`")
    lines.append("")
    if missing:
        lines.append("Docs missing discoverability links:")
        for path in missing:
            lines.append(f"- `{path}`")
        lines.append("")
        lines.append("Add at least one reference in README-style navigation docs.")
    else:
        lines.append("All new docs are referenced from at least one repository markdown file.")
    report = "\n".join(lines).strip() + "\n"

    Path(args.output_md).write_text(report, encoding="utf-8")
    print(report)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
