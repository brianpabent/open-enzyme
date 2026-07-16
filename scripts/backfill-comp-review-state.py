#!/usr/bin/env python3
"""Create explicit blocked baselines for legacy COMPs lacking current push reviews.

This does not pretend that an independent review occurred. It binds each legacy
artifact to an exact push manifest and records that propagation and synthesis
remain blocked until the normal COMP review replaces the baseline.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "wiki" / "etc" / "experiments"
STATE = ROOT / "logs" / "sweep-state.json"


def run(*args: str) -> str:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def comp_id(path: Path) -> str:
    match = re.match(r"^(comp-\d{3})(?:-|$)", path.name)
    if not match:
        raise ValueError(path)
    return match.group(1)


def receipt_document(identifier: str, comp_rel: str, commit: str, manifest: dict) -> dict:
    derived = sorted(
        str(item["path"]) for item in manifest["files"]
        if item.get("kind") == "proposed_update"
    )
    return {
        "schema_version": 1,
        "comp": identifier,
        "comp_dir": comp_rel,
        "source_commit": commit,
        "artifact_manifest_sha256": manifest["manifest_sha256"],
        "reviewer_model": None,
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "comp_verdict": "legacy_review_pending",
        "propagation_eligibility": "blocked",
        "synthesis_eligibility": "blocked",
        "action_required": False,
        "derived_paths": derived,
        "actual_cost_usd": 0.0,
        "note": "Deterministic migration baseline only; no independent push review has occurred.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write manifests, receipts, and state")
    args = parser.parse_args()
    commit = run("git", "rev-parse", "HEAD")
    state = json.loads(STATE.read_text())
    pending = []

    for comp_dir in sorted(EXPERIMENTS.glob("comp-*")):
        if not comp_dir.is_dir():
            continue
        identifier = comp_id(comp_dir)
        if identifier in state.get("comp_reviews", {}):
            continue
        pending.append(identifier)
        if not args.write:
            continue
        reviews = comp_dir / "reviews"
        reviews.mkdir(exist_ok=True)
        manifest_path = reviews / "push-review.manifest.json"
        manifest_sha = run(
            "python3", "scripts/comp-review-manifest.py", "create", "--phase", "push",
            "--comp-dir", str(comp_dir.relative_to(ROOT)), "--output", str(manifest_path.relative_to(ROOT)),
        )
        manifest = json.loads(manifest_path.read_text())
        if manifest_sha != manifest["manifest_sha256"]:
            raise RuntimeError(f"manifest digest mismatch for {identifier}")
        comp_rel = comp_dir.relative_to(ROOT).as_posix()
        document = receipt_document(identifier, comp_rel, commit, manifest)
        json_path = reviews / "push-review.json"
        md_path = reviews / "push-review.md"
        json_path.write_text(json.dumps(document, indent=2) + "\n")
        md_path.write_text(
            f"COMP_VERDICT: legacy_review_pending\n"
            f"PROPAGATION_ELIGIBILITY: blocked\n"
            f"SYNTHESIS_ELIGIBILITY: blocked\n"
            f"ACTION_REQUIRED: no\n"
            f"REVIEWED_SNAPSHOT: manifest:{manifest_sha}\n\n"
            "This is a deterministic migration baseline, not an independent review. "
            "Run the current COMP push review before using this artifact for propagation or synthesis.\n"
        )
        state.setdefault("comp_reviews", {})[identifier] = {
            "comp_dir": comp_rel,
            "artifact_manifest_sha256": manifest_sha,
            "source_commit": commit,
            "review_receipt": md_path.relative_to(ROOT).as_posix(),
            "comp_verdict": "legacy_review_pending",
            "propagation_eligibility": "blocked",
            "synthesis_eligibility": "blocked",
            "derived_paths": document["derived_paths"],
            "timestamp": document["timestamp"],
            "cost_usd": 0.0,
        }

    if args.write:
        STATE.write_text(json.dumps(state, indent=2) + "\n")
    print(json.dumps({"source_commit": commit, "legacy_review_pending": pending, "count": len(pending)}))


if __name__ == "__main__":
    main()
