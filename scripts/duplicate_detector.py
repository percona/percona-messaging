#!/usr/bin/env python3
"""Detect high-overlap markdown content to reduce duplication."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

EXCLUDED_PREFIXES = (".github/", ".cursor/")


@dataclass
class SimilarityHit:
    source: str
    target: str
    score: float


def git_changed_markdown(base_ref: str, head_ref: str) -> list[str]:
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-status", f"{base_ref}...{head_ref}"],
            text=True,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        output = subprocess.check_output(["git", "diff", "--name-status"], text=True)

    paths: list[str] = []
    for line in output.splitlines():
        parts = line.split("\t", maxsplit=1)
        if len(parts) != 2:
            continue
        status, path = parts
        path = path.strip()
        if status[0] not in {"A", "M"}:
            continue
        if not path.endswith(".md") or path.endswith(".draft.md"):
            continue
        if path.startswith(EXCLUDED_PREFIXES):
            continue
        paths.append(path)
    return paths


def normalize(text: str) -> str:
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def all_markdown_paths() -> list[Path]:
    root = Path(".")
    return [p for p in root.rglob("*.md") if ".git" not in p.parts and ".venv" not in p.parts]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect duplicate markdown content overlap.")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--warn-threshold", type=float, default=0.72)
    parser.add_argument("--fail-threshold", type=float, default=0.86)
    parser.add_argument("--output-md", default="duplicate-detector-report.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = git_changed_markdown(args.base, args.head)
    if not changed:
        report = "## Duplicate Detector\n\nNo changed markdown docs detected.\n"
        Path(args.output_md).write_text(report, encoding="utf-8")
        print(report)
        return 0

    all_md = [p.as_posix() for p in all_markdown_paths()]
    content_cache = {}
    for path in all_md:
        content_cache[path] = normalize(Path(path).read_text(encoding="utf-8"))

    warn_hits: list[SimilarityHit] = []
    fail_hits: list[SimilarityHit] = []
    for source in changed:
        source_text = content_cache.get(source, "")
        for target in all_md:
            if target == source or target in changed:
                continue
            score = similarity(source_text, content_cache.get(target, ""))
            if score >= args.fail_threshold:
                fail_hits.append(SimilarityHit(source, target, score))
            elif score >= args.warn_threshold:
                warn_hits.append(SimilarityHit(source, target, score))

    lines = ["## Duplicate Detector", "", f"- Changed markdown docs: {len(changed)}", ""]
    if fail_hits:
        lines.append("### Blocking overlap hits")
        for hit in sorted(fail_hits, key=lambda h: h.score, reverse=True)[:25]:
            lines.append(f"- `{hit.source}` vs `{hit.target}`: {hit.score:.2f}")
        lines.append("")
    if warn_hits:
        lines.append("### Warning overlap hits")
        for hit in sorted(warn_hits, key=lambda h: h.score, reverse=True)[:25]:
            lines.append(f"- `{hit.source}` vs `{hit.target}`: {hit.score:.2f}")
        lines.append("")
    if not fail_hits and not warn_hits:
        lines.append("No significant overlap detected.")
    report = "\n".join(lines).strip() + "\n"

    Path(args.output_md).write_text(report, encoding="utf-8")
    print(report)
    return 1 if fail_hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
