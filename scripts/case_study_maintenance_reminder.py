#!/usr/bin/env python3
"""Build markdown body for the monthly case study proof-point maintenance issue."""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

from case_study_registry import load_registry, normalize_entry, status_summary

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

STATUS_LABELS = {
    "adopted_in_messaging": "Adopted in messaging",
    "candidate": "Candidate (not yet cited)",
    "published": "Published (tracking only)",
    "retired": "Retired",
}


def _escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|")


def _format_locations(locations: list[str] | None) -> str:
    if not locations:
        return "—"
    return "<br>".join(_escape_table_cell(str(item)) for item in locations)


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
            "- [ ] Set `status` to `candidate` for published stories not yet cited, or `adopted_in_messaging` when cited",
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
    counts = status_summary(studies)
    lines.extend(
        [
            "",
            "### Tracked registry (`data/case-studies.json`)",
            "",
            f"Last reviewed (UTC): `{last_reviewed}`",
            "",
            "Adoption summary:",
            "",
            f"- Adopted in messaging: **{counts['adopted_in_messaging']}**",
            f"- Candidate (not yet cited): **{counts['candidate']}**",
            f"- Published (tracking only): **{counts['published']}**",
            f"- Retired: **{counts['retired']}**",
            "",
        ]
    )

    if studies:
        adopted = []
        candidates = []
        other = []
        for item in studies:
            if not isinstance(item, dict):
                continue
            entry = normalize_entry(item)
            status = str(entry.get("status") or "published").strip()
            if status == "adopted_in_messaging":
                adopted.append(entry)
            elif status == "candidate":
                candidates.append(entry)
            else:
                other.append(entry)

        if adopted:
            lines.extend(
                [
                    "#### Adopted in messaging",
                    "",
                    "| Customer | Pillar | Locations | URL |",
                    "| --- | --- | --- | --- |",
                ]
            )
            for entry in adopted:
                customer = _escape_table_cell(str(entry.get("customer") or "(untitled)"))
                pillar = _escape_table_cell(str(entry.get("primary_pillar") or "—"))
                locations = _format_locations(entry.get("canonical_locations"))
                url = str(entry.get("url") or "").strip()
                url_cell = f"[link]({url})" if url else "*(missing URL)*"
                lines.append(f"| {customer} | {pillar} | {locations} | {url_cell} |")

        if candidates:
            lines.extend(
                [
                    "",
                    "#### Candidates (published, not yet cited)",
                    "",
                    "| Customer | Products | URL |",
                    "| --- | --- | --- |",
                ]
            )
            for entry in candidates:
                customer = _escape_table_cell(str(entry.get("customer") or "(untitled)"))
                products = _escape_table_cell(", ".join(entry.get("products") or []) or "—")
                url = str(entry.get("url") or "").strip()
                url_cell = f"[link]({url})" if url else "*(missing URL)*"
                lines.append(f"| {customer} | {products} | {url_cell} |")

        if other:
            lines.extend(
                [
                    "",
                    "#### Other tracked stories",
                    "",
                    "| Customer | Status | URL |",
                    "| --- | --- | --- |",
                ]
            )
            for entry in other:
                customer = _escape_table_cell(str(entry.get("customer") or "(untitled)"))
                status = STATUS_LABELS.get(str(entry.get("status") or ""), str(entry.get("status") or "—"))
                url = str(entry.get("url") or "").strip()
                url_cell = f"[link]({url})" if url else "*(missing URL)*"
                lines.append(f"| {customer} | {status} | {url_cell} |")
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
