#!/usr/bin/env python3
"""Build markdown body for the monthly case study proof-point maintenance issue."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

MARKER = "<!-- messaging-case-study-maintenance -->"

PUBLIC_CATALOGS = [
    ("Percona case studies (index)", "https://www.percona.com/about-percona/case-studies"),
    ("Experience hub (interactive)", "https://experience.percona.com/"),
]

CANONICAL_LOCATIONS = [
    "`framework/why-percona.md`",
    "`use-cases-value-pillars/`",
    "`offerings/`",
    "Other product or pillar pages with customer proof",
]


def load_registry(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "last_reviewed_utc": "", "case_studies": []}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"version": 1, "last_reviewed_utc": "", "case_studies": []}
    if not isinstance(payload, dict):
        return {"version": 1, "last_reviewed_utc": "", "case_studies": []}
    studies = payload.get("case_studies")
    if not isinstance(studies, list):
        studies = []
    last_reviewed = str(payload.get("last_reviewed_utc") or payload.get("last_synced_utc") or "").strip()
    return {
        "version": payload.get("version", 1),
        "last_reviewed_utc": last_reviewed,
        "case_studies": studies,
    }


def build_body(registry: dict, now: dt.datetime) -> str:
    lines = [
        MARKER,
        "",
        f"**Run (UTC):** `{now.strftime('%Y-%m-%d')}`",
        "",
        "Percona publishes new customer proof on the public web, but there is no machine-readable feed. "
        "This issue is a monthly reminder to compare published case studies against canonical messaging in this repo.",
        "",
        "### Public catalogs to review",
        "",
    ]
    for label, url in PUBLIC_CATALOGS:
        lines.append(f"- [{label}]({url})")

    lines.extend(
        [
            "",
            "### Maintainer checklist",
            "",
            "- [ ] Scan the catalogs above for case studies published or promoted since the last review",
            "- [ ] For each new or updated study, confirm whether canonical copy should cite it",
            "- [ ] Update proof in the locations below when claims are defensible and approved for use",
            "- [ ] Add or refresh entries in `data/case-studies.json` when proof is adopted (manual registry)",
            "- [ ] Close this issue when the review is complete, or note follow-ups in comments",
            "",
            "### Canonical locations to check",
            "",
        ]
    )
    for location in CANONICAL_LOCATIONS:
        lines.append(f"- {location}")

    last_reviewed = registry.get("last_reviewed_utc") or "(not recorded)"
    studies = registry.get("case_studies") or []
    lines.extend(
        [
            "",
            "### Tracked registry (`data/case-studies.json`)",
            "",
            f"Last reviewed (UTC): `{last_reviewed}`",
            "",
        ]
    )
    if studies:
        lines.extend(
            [
                "| Title | URL |",
                "| --- | --- |",
            ]
        )
        for item in studies:
            if not isinstance(item, dict):
                continue
            title = str(item.get("title") or "(untitled)").replace("|", "\\|")
            url = str(item.get("url") or "").strip()
            if url:
                lines.append(f"| {title} | {url} |")
            else:
                lines.append(f"| {title} | *(missing URL)* |")
    else:
        lines.append("_No case studies tracked yet. Add entries via pull request when proof is adopted._")

    lines.extend(
        [
            "",
            "### Related backlog",
            "",
            "Customer-name audit vs published studies: see backlog item **C3** in "
            "[reference/launch-and-automation-backlog.md](reference/launch-and-automation-backlog.md).",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--registry",
        type=Path,
        default=Path("data/case-studies.json"),
        help="Manual case study registry JSON",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("case-study-maintenance-issue.md"),
        help="Markdown issue body output path",
    )
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    registry = load_registry(args.registry)
    args.output.write_text(build_body(registry, now), encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
