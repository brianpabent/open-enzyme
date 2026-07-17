#!/usr/bin/env python3
"""Validate compact literature-scan method receipts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "logs" / "lit-scans"
REQUIRED_KEYS = {
    "schema_version",
    "scan_id",
    "question",
    "started_at",
    "completed_at",
    "canonical_updates",
    "query_attempts",
    "source_ids_considered",
    "translation_checks",
    "load_bearing_verifications",
    "limitations",
    "errors",
    "workspace",
}
FORBIDDEN_NARRATIVE_KEYS = {"findings", "summary", "verdict", "recommendations", "narrative"}
QUERY_KEYS = {"source", "language", "frame", "query", "status", "result_count", "error"}
QUERY_STATUSES = {"success", "partial", "failed"}


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: unreadable JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: receipt must be a JSON object"]

    missing = sorted(REQUIRED_KEYS - set(data))
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(missing)}")
    forbidden = sorted(FORBIDDEN_NARRATIVE_KEYS & set(data))
    if forbidden:
        errors.append(
            f"{path}: scientific narrative belongs in wiki; remove keys: {', '.join(forbidden)}"
        )
    if data.get("schema_version") != 1:
        errors.append(f"{path}: schema_version must be 1")
    for key in ("scan_id", "question", "started_at", "completed_at"):
        if key in data and not _nonempty_string(data[key]):
            errors.append(f"{path}: {key} must be a non-empty string")

    updates = data.get("canonical_updates")
    if not isinstance(updates, list) or not updates or not all(
        _nonempty_string(item) and item.startswith("wiki/") for item in updates
    ):
        errors.append(f"{path}: canonical_updates must be a non-empty list of wiki/ paths")

    attempts = data.get("query_attempts")
    if not isinstance(attempts, list) or not attempts:
        errors.append(f"{path}: query_attempts must be a non-empty list")
    else:
        for index, attempt in enumerate(attempts):
            prefix = f"{path}: query_attempts[{index}]"
            if not isinstance(attempt, dict):
                errors.append(f"{prefix} must be an object")
                continue
            missing_query = sorted(QUERY_KEYS - set(attempt))
            if missing_query:
                errors.append(f"{prefix} missing keys: {', '.join(missing_query)}")
                continue
            for key in ("source", "language", "frame", "query"):
                if not _nonempty_string(attempt.get(key)):
                    errors.append(f"{prefix}.{key} must be a non-empty string")
            status = attempt.get("status")
            if status not in QUERY_STATUSES:
                errors.append(f"{prefix}.status must be success, partial, or failed")
            count = attempt.get("result_count")
            if count is not None and (not isinstance(count, int) or isinstance(count, bool) or count < 0):
                errors.append(f"{prefix}.result_count must be null or a non-negative integer")
            if status in {"partial", "failed"} and not _nonempty_string(attempt.get("error")):
                errors.append(f"{prefix}.error is required for partial or failed attempts")
            if status == "success" and attempt.get("error") not in {None, ""}:
                errors.append(f"{prefix}.error must be null for successful attempts")

    for key in (
        "source_ids_considered",
        "translation_checks",
        "load_bearing_verifications",
        "limitations",
        "errors",
    ):
        if key in data and not isinstance(data[key], list):
            errors.append(f"{path}: {key} must be a list")

    workspace = data.get("workspace")
    if not isinstance(workspace, dict):
        errors.append(f"{path}: workspace must be an object")
    else:
        workspace_path = workspace.get("path")
        if not _nonempty_string(workspace_path) or not workspace_path.startswith("operations/"):
            errors.append(f"{path}: workspace.path must be an operations/ path")
        if workspace.get("cleaned") is not True:
            errors.append(f"{path}: workspace.cleaned must be true before commit")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = [path if path.is_absolute() else ROOT / path for path in args.paths]
    if not paths:
        paths = sorted(DEFAULT_DIR.glob("*.json")) if DEFAULT_DIR.exists() else []
    errors = [error for path in paths for error in validate(path)]
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Literature-scan receipt validation passed for {len(paths)} file(s)")


if __name__ == "__main__":
    main()
