#!/usr/bin/env python3
"""Create a hash-bound invalidation ledger from an exact Git tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comp-dir", required=True)
    parser.add_argument("--comp", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--current-evidence-home", required=True)
    parser.add_argument("--invalidated", action="append", default=[])
    parser.add_argument("--surviving", action="append", default=[])
    args = parser.parse_args()

    prefix = args.comp_dir.rstrip("/") + "/"
    listed = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", args.commit, "--", args.comp_dir],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    paths = [path for path in listed if "/reviews/" not in path]

    retired_files = []
    for path in paths:
        payload = git_bytes(args.commit, path)
        retired_files.append(
            {
                "path": path.removeprefix(prefix),
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        )

    push_manifest_path = prefix + "reviews/push-review.manifest.json"
    push_manifest_sha256 = None
    if push_manifest_path in listed:
        push_manifest_sha256 = hashlib.sha256(
            git_bytes(args.commit, push_manifest_path)
        ).hexdigest()

    surviving_scope = {
        "kind": "bounded_historical_inventory_and_research_conjecture",
        "statements": args.surviving,
        "predictive_or_decision_use": False,
    }
    digest_payload = {
        "retired_files": retired_files,
        "invalidated_scope": args.invalidated,
        "surviving_scope": surviving_scope,
        "current_evidence_home": args.current_evidence_home,
        "runnable": False,
    }
    canonical = json.dumps(
        digest_payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    ledger = {
        "schema_version": 1,
        "comp": args.comp,
        "status": "invalidated_tombstone",
        "runnable": False,
        "retired_tree_commit": args.commit,
        "last_push_review_manifest_sha256": push_manifest_sha256,
        "retired_files": retired_files,
        "invalidated_scope": args.invalidated,
        "surviving_scope": surviving_scope,
        "current_evidence_home": args.current_evidence_home,
        "canonical_digest": {
            "algorithm": "sha256",
            "canonical_json": (
                "UTF-8 JSON object containing exactly retired_files, "
                "invalidated_scope, surviving_scope, current_evidence_home, "
                "and runnable; object keys are sorted recursively, arrays "
                "preserve listed order, ensure_ascii is false, and separators "
                "are ',' and ':'."
            ),
            "sha256": hashlib.sha256(canonical).hexdigest(),
        },
    }
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    print(ledger["canonical_digest"]["sha256"])


if __name__ == "__main__":
    main()
