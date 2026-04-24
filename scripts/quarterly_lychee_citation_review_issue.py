#!/usr/bin/env python3
"""Build markdown body for the quarterly CI-excluded citation link review issue."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "automation" / "lychee-quarterly-review-citations.json"


def quarter_label(now: dt.datetime) -> str:
    q = (now.month - 1) // 3 + 1
    return f"{now.year} Q{q}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help="Path to lychee-quarterly-review-citations.json",
    )
    parser.add_argument("--output", type=Path, default=Path("quarterly-citation-review-issue.md"))
    parser.add_argument(
        "--json-meta",
        type=Path,
        default=Path("quarterly-citation-review-meta.json"),
        help="Write assignee + title for github-script",
    )
    args = parser.parse_args()

    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    assignee = str(cfg.get("assignee", "")).strip()
    citations = cfg.get("citations")
    if not isinstance(citations, list) or not citations:
        print("No citations configured.", file=sys.stderr)
        return 1

    now = dt.datetime.now(dt.timezone.utc)
    q = quarter_label(now)
    marker = "<!-- quarterly-lychee-citation-review -->"

    lines = [
        marker,
        "",
        f"**Quarter:** {q} (UTC `{now.strftime('%Y-%m-%d')}`)",
        "",
        "These URLs are **excluded from lychee in CI** because they often return **403** (or similar) to **automated / datacenter** requests, even when they work in a normal browser. They are still cited in canonical markdown.",
        "",
        "### Human checklist",
        "",
        "For each row: open the URL in a browser, confirm it still supports the claim in the listed file(s), and check the box in a follow-up comment or PR.",
        "",
        "| Done | URL | Rationale | Markdown |",
        "| --- | --- | --- | --- |",
    ]

    for row in citations:
        if not isinstance(row, dict):
            continue
        url = str(row.get("url", "")).strip()
        rationale = str(row.get("rationale", "")).strip().replace("|", "\\|")
        md_files = row.get("markdown_files") or []
        if isinstance(md_files, list):
            md_cell = ", ".join(f"`{p}`" for p in md_files if p)
        else:
            md_cell = ""
        if not url:
            continue
        lines.append(f"| [ ] | {url} | {rationale} | {md_cell} |")

    rel_config = args.config.resolve().relative_to(REPO_ROOT)
    lines.extend(
        [
            "",
            "### Maintainer sync",
            "",
            f"When you add or remove a CI-only exclude in `.lychee.toml`, update **`{rel_config}`** so this list stays accurate.",
            "",
        ]
    )
    if assignee:
        lines.append(f"cc @{assignee}")
        lines.append("")

    body = "\n".join(lines).rstrip() + "\n"
    args.output.write_text(body, encoding="utf-8")

    title = f"Quarterly review: CI-excluded citation links ({q})"
    meta = {"title": title, "assignee": assignee, "marker": marker}
    args.json_meta.write_text(json.dumps(meta), encoding="utf-8")

    print(f"Wrote {args.output} and {args.json_meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
