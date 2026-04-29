#!/usr/bin/env python3
"""Ensure newly added markdown docs are discoverable from navigation docs."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

EXCLUDED_PREFIXES = (
    ".github/",
    ".cursor/",
)
INDEX_FILES = {
    "README.md",
    "CONTRIBUTING.md",
}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


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


def navigation_docs(md_files: list[Path]) -> list[Path]:
    return [md for md in md_files if md.name in INDEX_FILES and not md.as_posix().startswith(EXCLUDED_PREFIXES)]


def _normalize_link_target(target: str, nav_doc: Path) -> str | None:
    raw = target.strip()
    if not raw:
        return None
    parsed = urlparse(raw)
    if parsed.scheme or raw.startswith("#") or raw.startswith("mailto:"):
        return None
    cleaned = raw.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0].strip()
    if not cleaned:
        return None
    if cleaned.startswith("/"):
        rel = Path(cleaned.lstrip("/"))
    else:
        try:
            rel = (nav_doc.parent / cleaned).resolve().relative_to(Path(".").resolve())
        except ValueError:
            return None
    if rel.suffix != ".md":
        return None
    return rel.as_posix()


def collect_navigation_links(nav_docs: list[Path]) -> dict[str, set[str]]:
    links_to_docs: dict[str, set[str]] = {}
    for nav_doc in nav_docs:
        text = nav_doc.read_text(encoding="utf-8")
        nav_rel = nav_doc.as_posix()
        for match in LINK_PATTERN.findall(text):
            target = _normalize_link_target(match, nav_doc)
            if target is None:
                continue
            links_to_docs.setdefault(target, set()).add(nav_rel)
    return links_to_docs


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
    nav_docs = navigation_docs(md_files)
    linked_docs = collect_navigation_links(nav_docs)
    missing = [path for path in added if path not in linked_docs]

    lines = [
        "## Doc Coverage Check",
        "",
        f"- New markdown docs: {len(added)}",
        f"- Navigation docs scanned: {len(nav_docs)}",
    ]
    for path in added:
        linked_from = sorted(linked_docs.get(path, set()))
        if linked_from:
            lines.append(f"  - `{path}` (linked from: {', '.join(f'`{doc}`' for doc in linked_from)})")
        else:
            lines.append(f"  - `{path}` (missing navigation link)")
    lines.append("")
    if missing:
        lines.append("Docs missing discoverability links:")
        for path in missing:
            lines.append(f"- `{path}`")
        lines.append("")
        lines.append("Add at least one markdown link to each missing file from README.md or CONTRIBUTING.md.")
    else:
        lines.append("All new docs are linked from repository navigation docs.")
    report = "\n".join(lines).strip() + "\n"

    Path(args.output_md).write_text(report, encoding="utf-8")
    print(report)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
