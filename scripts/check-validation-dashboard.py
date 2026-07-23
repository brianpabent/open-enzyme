#!/usr/bin/env python3
"""Verify that every validation section appears once in the dashboard.

The dashboard is a compact planning view, while the numbered sections own the
protocols. This guard prevents newly added experiments or revised cost/timeline
metadata from drifting between those two surfaces.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_PATH = Path("wiki/validation-experiments.md")
SECTION_RE = re.compile(r"^###\s+(\d+\.\d+)\s+")
DASHBOARD_ID_RE = re.compile(r"^\[§(\d+\.\d+)\]\(")
METADATA_RE = re.compile(
    r"\*\*(Status|Cost|Weeks):?\*\*\s*:?\s*(.*?)\s*(?=\|\s*\*\*|$)"
)


def parse_dashboard(lines: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    rows: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    in_dashboard = False

    for line_number, line in enumerate(lines, start=1):
        if line.startswith("| ID | Title | Category | Cost | Weeks | Status | Wiki refs |"):
            in_dashboard = True
            continue
        if not in_dashboard:
            continue
        if not line.startswith("|"):
            if rows:
                break
            continue
        if line.startswith("|----"):
            continue

        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 7:
            errors.append(
                f"line {line_number}: dashboard row has {len(cells)} columns; expected 7"
            )
            continue
        match = DASHBOARD_ID_RE.match(cells[0])
        if not match:
            errors.append(f"line {line_number}: dashboard row has no §N.N ID")
            continue
        experiment_id = match.group(1)
        if experiment_id in rows:
            errors.append(f"line {line_number}: duplicate dashboard row §{experiment_id}")
            continue
        rows[experiment_id] = {
            "cost": cells[3],
            "weeks": cells[4],
            "line": str(line_number),
        }
        if not cells[3] or not cells[4]:
            errors.append(
                f"line {line_number}: dashboard §{experiment_id} must declare "
                "both Cost and Weeks"
            )

    if not rows:
        errors.append("validation dashboard table was not found or contains no rows")
    return rows, errors


def parse_sections(lines: list[str]) -> tuple[dict[str, dict[str, str]], list[str]]:
    sections: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    current_id: str | None = None
    current_line = 0

    for line_number, line in enumerate(lines, start=1):
        heading = SECTION_RE.match(line)
        if heading:
            if current_id is not None:
                errors.append(
                    f"line {current_line}: section §{current_id} has no status line"
                )
            current_id = heading.group(1)
            current_line = line_number
            if current_id in sections:
                errors.append(f"line {line_number}: duplicate section §{current_id}")
            else:
                sections[current_id] = {
                    "cost": "",
                    "weeks": "",
                    "line": str(line_number),
                }
            continue

        if current_id is None or not line.strip():
            continue
        if not line.startswith("**Status"):
            errors.append(
                f"line {current_line}: section §{current_id} must put its status line "
                "immediately after the heading"
            )
            current_id = None
            continue
        metadata = dict(METADATA_RE.findall(line))
        sections[current_id]["cost"] = metadata.get("Cost", "")
        sections[current_id]["weeks"] = metadata.get("Weeks", "")
        if not sections[current_id]["cost"] or not sections[current_id]["weeks"]:
            errors.append(
                f"line {current_line}: section §{current_id} status line must declare "
                "both Cost and Weeks"
            )
        current_id = None

    if current_id is not None:
        errors.append(f"line {current_line}: section §{current_id} has no status line")
    if not sections:
        errors.append("no numbered validation sections were found")
    return sections, errors


def check(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    dashboard, errors = parse_dashboard(lines)
    sections, section_errors = parse_sections(lines)
    errors.extend(section_errors)

    dashboard_ids = set(dashboard)
    section_ids = set(sections)
    for experiment_id in sorted(section_ids - dashboard_ids):
        errors.append(f"section §{experiment_id} is missing from the dashboard")
    for experiment_id in sorted(dashboard_ids - section_ids):
        errors.append(f"dashboard §{experiment_id} has no numbered section")

    for experiment_id in sorted(dashboard_ids & section_ids):
        for field in ("cost", "weeks"):
            dashboard_value = dashboard[experiment_id][field]
            section_value = sections[experiment_id][field]
            if dashboard_value != section_value:
                errors.append(
                    f"§{experiment_id} {field} mismatch: dashboard "
                    f"{dashboard_value!r} (line {dashboard[experiment_id]['line']}) != "
                    f"section {section_value!r} (line {sections[experiment_id]['line']})"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check validation dashboard completeness and cost/timeline fidelity."
    )
    parser.add_argument("path", nargs="?", type=Path, default=DEFAULT_PATH)
    args = parser.parse_args()

    errors = check(args.path)
    if errors:
        print(f"validation dashboard check failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"validation dashboard check passed: {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
