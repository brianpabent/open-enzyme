#!/usr/bin/env python3
"""Create or refresh a deterministic COMP quarantine marker."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER_PATH = ROOT / "scripts" / "check-comp-disposition.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("comp_disposition", CHECKER_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load disposition checker")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comp-dir", required=True)
    parser.add_argument("--comp", required=True)
    parser.add_argument("--owner", default="brian")
    parser.add_argument("--reason", required=True)
    parser.add_argument("--entered-on", default=dt.date.today().isoformat())
    parser.add_argument("--expires-on", required=True)
    parser.add_argument("--decision-status", default="pending_re_review")
    parser.add_argument("--current-evidence-home", required=True)
    parser.add_argument("--blocked-scope", action="append", required=True)
    parser.add_argument("--restored-from-commit")
    parser.add_argument("--disposition-review")
    args = parser.parse_args()

    checker = load_checker()
    comp_dir = checker.resolve_comp(args.comp_dir)
    if (comp_dir / "invalidation.json").exists():
        raise SystemExit(
            "remove invalidation.json only after the complete artifact has been "
            "restored; quarantine and tombstone may not coexist"
        )

    marker = comp_dir / "quarantine.json"
    manifest = checker.artifact_manifest(comp_dir)
    dependencies = checker.artifact_dependencies(comp_dir)
    document = {
        "schema_version": 1,
        "comp": args.comp,
        "status": "quarantined",
        "runnable": False,
        "owner": args.owner,
        "entered_on": args.entered_on,
        "expires_on": args.expires_on,
        "decision_status": args.decision_status,
        "reason": args.reason,
        "blocked_scope": args.blocked_scope,
        "current_evidence_home": args.current_evidence_home,
        "artifact_manifest": manifest,
        "artifact_dependencies": dependencies,
        "artifact_manifest_sha256": checker.canonical_quarantine_sha256(
            manifest,
            dependencies,
        ),
    }
    if args.restored_from_commit:
        document["restored_from_commit"] = args.restored_from_commit
    if args.disposition_review:
        review_path = (ROOT / args.disposition_review).resolve()
        if review_path != ROOT and ROOT not in review_path.parents:
            raise SystemExit("disposition review escapes repository")
        if not review_path.is_file():
            raise SystemExit(f"disposition review does not exist: {args.disposition_review}")
        document["disposition_review"] = {
            "path": review_path.relative_to(ROOT).as_posix(),
            "sha256": checker.sha256(review_path),
        }
    previous = marker.read_bytes() if marker.is_file() else None
    marker.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    errors = checker.validate_quarantine(comp_dir)
    if errors:
        if previous is None:
            marker.unlink(missing_ok=True)
        else:
            marker.write_bytes(previous)
        raise SystemExit("\n".join(errors))
    print(marker.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
