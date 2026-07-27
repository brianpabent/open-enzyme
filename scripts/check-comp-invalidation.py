#!/usr/bin/env python3
"""Validate a non-runnable COMP invalidation ledger against its retired Git tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMP_RE = re.compile(r"^(comp-\d{3})(?:-|$)")


def git_bytes(commit: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    if result.returncode:
        raise ValueError(f"retired file is unavailable at {commit}: {path}")
    return result.stdout


def canonical_digest(document: dict[str, object]) -> str:
    payload = {
        "retired_files": document["retired_files"],
        "invalidated_scope": document["invalidated_scope"],
        "surviving_scope": document["surviving_scope"],
        "current_evidence_home": document["current_evidence_home"],
        "runnable": document["runnable"],
    }
    if "successor" in document:
        payload["successor"] = document["successor"]
    for key in (
        "cascade",
        "decision_owner",
        "decision_ref",
        "disposition_review",
        "reviewed_artifact_manifest_sha256",
        "surviving_scope_homes",
        "unique_detail_audit",
    ):
        if key in document:
            payload[key] = document[key]
    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(canonical).hexdigest()


def tracked_live_files(comp_dir: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--", comp_dir.relative_to(ROOT).as_posix()],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    prefix = comp_dir.relative_to(ROOT).as_posix() + "/"
    return sorted(
        path.removeprefix(prefix)
        for path in result.stdout.splitlines()
        if path and "/reviews/" not in f"/{path}/"
    )


def validate(comp_dir: Path) -> list[str]:
    errors: list[str] = []
    match = COMP_RE.match(comp_dir.name)
    if not match:
        return [f"not a comp-NNN directory: {comp_dir}"]
    ledger_path = comp_dir / "invalidation.json"
    if not ledger_path.is_file():
        return [f"invalidation ledger is missing: {ledger_path}"]
    try:
        document = json.loads(ledger_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalidation ledger is unreadable: {exc}"]

    if document.get("schema_version") not in {1, 2}:
        errors.append("schema_version must be 1 or 2")
    if document.get("comp") != match.group(1):
        errors.append(f"comp must be {match.group(1)}")
    if document.get("status") != "invalidated_tombstone":
        errors.append("status must be invalidated_tombstone")
    if document.get("runnable") is not False:
        errors.append("runnable must be false")

    evidence_home = document.get("current_evidence_home")
    if not isinstance(evidence_home, str) or not evidence_home.startswith("wiki/"):
        errors.append("current_evidence_home must be a wiki/ path")
    elif not (ROOT / evidence_home).is_file():
        errors.append(f"current_evidence_home does not exist: {evidence_home}")

    live = tracked_live_files(comp_dir)
    if live != ["README.md", "invalidation.json"]:
        errors.append(
            "a tombstone may retain only README.md and invalidation.json outside reviews; "
            f"found {live}"
        )

    retired_commit = document.get("retired_tree_commit")
    retired_files = document.get("retired_files")
    if not isinstance(retired_commit, str):
        errors.append("retired_tree_commit must be a Git revision")
    else:
        resolved = subprocess.run(
            ["git", "rev-parse", f"{retired_commit}^{{commit}}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if resolved.returncode:
            errors.append(f"retired_tree_commit does not resolve: {retired_commit}")
        else:
            retired_commit = resolved.stdout.strip()
    if not isinstance(retired_files, list) or not retired_files:
        errors.append("retired_files must be a non-empty list")
    elif isinstance(retired_commit, str):
        seen: set[str] = set()
        for item in retired_files:
            if not isinstance(item, dict):
                errors.append("each retired_files entry must be an object")
                continue
            relative = item.get("path")
            if not isinstance(relative, str) or not relative or relative.startswith("/"):
                errors.append(f"invalid retired file path: {relative!r}")
                continue
            if relative in seen:
                errors.append(f"duplicate retired file path: {relative}")
                continue
            seen.add(relative)
            repo_path = f"{comp_dir.relative_to(ROOT).as_posix()}/{relative}"
            try:
                payload = git_bytes(retired_commit, repo_path)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if item.get("bytes") != len(payload):
                errors.append(f"retired byte count mismatch: {relative}")
            if item.get("sha256") != hashlib.sha256(payload).hexdigest():
                errors.append(f"retired SHA-256 mismatch: {relative}")

    digest = document.get("canonical_digest")
    # Some first-generation tombstones predate the self-digest. Their retired
    # byte inventory is still verified against the named immutable Git tree.
    if digest is not None:
        if not isinstance(digest, dict) or digest.get("algorithm") != "sha256":
            errors.append("canonical_digest must declare sha256")
            return errors
        try:
            actual = canonical_digest(document)
        except KeyError as exc:
            errors.append(f"canonical digest input is missing: {exc.args[0]}")
        else:
            if digest.get("sha256") != actual:
                errors.append("canonical invalidation digest mismatch")
    return errors


def resolve(raw: str) -> Path:
    path = (ROOT / raw).resolve()
    if path != ROOT and ROOT not in path.parents:
        raise SystemExit(f"path escapes repository: {raw}")
    if not path.is_dir():
        raise SystemExit(f"COMP directory does not exist: {raw}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comp-dir", action="append", default=[])
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()
    raw_dirs = list(args.comp_dir)
    if args.all:
        raw_dirs.extend(
            path.parent.relative_to(ROOT).as_posix()
            for path in sorted(
                (ROOT / "wiki" / "etc" / "experiments").glob(
                    "comp-*/invalidation.json"
                )
            )
        )
    if not raw_dirs:
        parser.error("provide --comp-dir or --all")

    failed = False
    for raw in dict.fromkeys(raw_dirs):
        comp_dir = resolve(raw)
        errors = validate(comp_dir)
        if errors:
            failed = True
            for error in errors:
                print(f"ERROR [{comp_dir.name}]: {error}")
        else:
            print(f"{comp_dir.name}: invalidation ledger valid")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
