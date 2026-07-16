#!/usr/bin/env python3
"""Maintain the Open Enzyme knowledge-system coverage registry.

Schema v2 separates cheap push-time propagation from deliberate full-corpus
synthesis and records the current eligibility of each computational experiment.
Git and GitHub Actions retain run history; this file retains only current state
and unresolved failures.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import subprocess
import sys
from pathlib import Path

from synthesis_normalize import NormalizationError, verify_manifest


REGISTRY_PATH = Path("logs/sweep-state.json")
SCHEMA_VERSION = 2
ELIGIBILITY = {"eligible", "eligible_with_warning", "blocked"}


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _empty_registry() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "last_successful_propagation": None,
        "last_successful_synthesis": None,
        "comp_reviews": {},
        "unresolved_failures": [],
    }


def migrate_v1_to_v2(data: dict) -> dict:
    """Deterministically split the v1 sweep cursor into two v2 cursors."""
    if data.get("schema_version") != 1:
        raise ValueError("migration input is not schema v1")
    old = data.get("last_successful_sweep") or None
    synthesis = None
    propagation = None
    if old:
        coverage = old.get("coverage_commit") or old.get("commit")
        timestamp = old.get("timestamp")
        synthesis = {
            "coverage_commit": coverage,
            "corpus_sha256": old.get("source_synthesis_sha256"),
            "timestamp": timestamp,
            "trigger_paths": old.get("trigger_files", []),
            "coverage_receipt_sha256": old.get("canonical_items_sha256"),
            "queue_items_emitted": old.get("normalized_item_count"),
            "cost_usd": old.get("cost_usd"),
            "result_commit": old.get("review_commit"),
            "sweep_id": old.get("sweep_id"),
            "_migrated_from_v1": True,
        }
        # The old three-pass workflow propagated the same semantic batch before
        # synthesis, so the old coverage snapshot is the only honest initial
        # propagation cursor. Later push runs move it independently.
        propagation = {
            "coverage_commit": coverage,
            "result_commit": old.get("review_commit") or coverage,
            "timestamp": timestamp,
            "changed_paths": old.get("trigger_files", []),
            "affected_paths": [],
            "blocked_paths": [],
            "cost_usd": None,
            "_migrated_from_v1": True,
        }
    failures = []
    for run in data.get("recent_runs", []):
        if run.get("outcome") == "failure":
            failures.append({
                "id": str(run.get("run_id") or f"legacy-{len(failures) + 1}"),
                "lane": run.get("failed_phase", "legacy-sweep"),
                "recorded_at": run.get("completed_at"),
                "summary": run.get("error_summary", "Migrated unresolved v1 failure"),
            })
    return {
        "schema_version": SCHEMA_VERSION,
        "last_successful_propagation": propagation,
        "last_successful_synthesis": synthesis,
        "comp_reviews": {},
        "unresolved_failures": failures,
    }


def read_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return _empty_registry()
    data = json.loads(REGISTRY_PATH.read_text())
    if data.get("schema_version") == 1:
        return migrate_v1_to_v2(data)
    if data.get("schema_version") != SCHEMA_VERSION:
        sys.exit(
            f"sweep-state.py: unknown schema_version {data.get('schema_version')!r}; "
            f"expected {SCHEMA_VERSION}"
        )
    return data


def write_registry(data: dict) -> None:
    data["schema_version"] = SCHEMA_VERSION
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = REGISTRY_PATH.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n")
    os.replace(tmp_path, REGISTRY_PATH)


def _cursor(data: dict, lane: str) -> str | None:
    key = f"last_successful_{lane}"
    return (data.get(key) or {}).get("coverage_commit")


def _git_changed_paths(base: str, patterns: list[str]) -> list[str]:
    command = ["git", "diff", "--name-only", base, "HEAD", "--", *patterns]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return sorted({p for p in result.stdout.splitlines() if p})


def _blocked_paths(data: dict) -> set[str]:
    blocked: set[str] = set()
    for review in data.get("comp_reviews", {}).values():
        if review.get("propagation_eligibility") != "blocked":
            continue
        blocked.add(review.get("comp_dir", ""))
        blocked.update(review.get("derived_paths", []))
    return {path for path in blocked if path}


def cmd_read(_args: argparse.Namespace) -> None:
    print(json.dumps(read_registry(), indent=2))


def cmd_migrate(_args: argparse.Namespace) -> None:
    if not REGISTRY_PATH.exists():
        sys.exit(f"sweep-state.py: {REGISTRY_PATH} does not exist")
    raw = json.loads(REGISTRY_PATH.read_text())
    if raw.get("schema_version") == SCHEMA_VERSION:
        print("sweep-state.py: registry is already schema v2")
        return
    migrated = migrate_v1_to_v2(raw)
    write_registry(migrated)
    print("sweep-state.py: migrated registry from schema v1 to v2")


def cmd_pending_propagation_paths(_args: argparse.Namespace) -> None:
    data = read_registry()
    base = _cursor(data, "propagation")
    if not base:
        sys.exit("sweep-state.py: no propagation cursor recorded")
    paths = set(_git_changed_paths(base, ["wiki/*.md", "wiki/hypotheses/*.md", "wiki/etc/experiments/comp-*/**"]))
    # A cursor may move past a blocked mixed push so unrelated work can finish.
    # Keep the blocked subset explicitly pending until a later clean receipt
    # releases it.
    paths.update((data.get("last_successful_propagation") or {}).get("blocked_paths", []))
    blocked = _blocked_paths(data)
    for path in sorted(paths):
        if any(path == b or path.startswith(f"{b}/") for b in blocked):
            continue
        print(path)


def cmd_pending_synthesis_paths(_args: argparse.Namespace) -> None:
    data = read_registry()
    base = _cursor(data, "synthesis")
    if not base:
        sys.exit("sweep-state.py: no synthesis cursor recorded")
    for path in _git_changed_paths(base, ["wiki/*.md", "wiki/hypotheses/*.md", "wiki/etc/experiments/comp-*/**"]):
        print(path)


def cmd_update_propagation(args: argparse.Namespace) -> None:
    data = read_registry()
    current = _cursor(data, "propagation")
    if args.expected_cursor and current != args.expected_cursor:
        sys.exit(f"sweep-state.py: propagation cursor changed: {current!r} != {args.expected_cursor!r}")
    changed = [p for p in args.changed_paths.split(",") if p]
    affected = [p for p in args.affected_paths.split(",") if p]
    blocked = [p for p in args.blocked_paths.split(",") if p]
    data["last_successful_propagation"] = {
        "coverage_commit": args.coverage_commit,
        "result_commit": args.result_commit,
        "timestamp": _now_iso(),
        "changed_paths": changed,
        "affected_paths": affected,
        "blocked_paths": blocked,
        "cost_usd": args.cost_usd,
    }
    write_registry(data)
    print(f"sweep-state.py: propagation coverage advanced to {args.coverage_commit[:8]}")


def cmd_record_comp_review(args: argparse.Namespace) -> None:
    if args.propagation_eligibility not in ELIGIBILITY or args.synthesis_eligibility not in ELIGIBILITY:
        sys.exit("sweep-state.py: invalid COMP eligibility")
    data = read_registry()
    derived = [p for p in args.derived_paths.split(",") if p]
    data["comp_reviews"][args.comp_id] = {
        "comp_dir": args.comp_dir,
        "artifact_manifest_sha256": args.artifact_manifest_sha256,
        "source_commit": args.source_commit,
        "review_receipt": args.review_receipt,
        "comp_verdict": args.comp_verdict,
        "propagation_eligibility": args.propagation_eligibility,
        "synthesis_eligibility": args.synthesis_eligibility,
        "derived_paths": derived,
        "timestamp": _now_iso(),
        "cost_usd": args.cost_usd,
    }
    write_registry(data)
    print(f"sweep-state.py: recorded current review for {args.comp_id}")


def cmd_comp_eligibility(args: argparse.Namespace) -> None:
    data = read_registry()
    record = data.get("comp_reviews", {}).get(args.comp_id)
    if not record:
        print("blocked")
        return
    print(record[f"{args.lane}_eligibility"])


def cmd_record_failure(args: argparse.Namespace) -> None:
    data = read_registry()
    failures = [f for f in data["unresolved_failures"] if f.get("id") != args.failure_id]
    failures.append({
        "id": args.failure_id,
        "lane": args.lane,
        "recorded_at": _now_iso(),
        "summary": args.error_summary,
        "paths": [p for p in args.paths.split(",") if p],
    })
    data["unresolved_failures"] = failures
    write_registry(data)


def cmd_resolve_failure(args: argparse.Namespace) -> None:
    data = read_registry()
    before = len(data["unresolved_failures"])
    data["unresolved_failures"] = [f for f in data["unresolved_failures"] if f.get("id") != args.failure_id]
    if len(data["unresolved_failures"]) == before:
        sys.exit(f"sweep-state.py: unresolved failure {args.failure_id!r} not found")
    write_registry(data)


def cmd_update_success(args: argparse.Namespace) -> None:
    """Compatibility entry point: record a completed full synthesis as v2 state."""
    data = read_registry()
    try:
        manifest = verify_manifest(Path(args.normalized_manifest))
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        sys.exit(f"sweep-state.py: refusing synthesis cursor advance: {exc}")
    source = manifest["source"]
    if source["synthesis_log"] != args.synthesis_log:
        sys.exit("sweep-state.py: synthesis log does not match normalized manifest")
    if source["diff_base"] != args.expected_diff_base:
        sys.exit("sweep-state.py: synthesis diff base does not match manifest")
    current = _cursor(data, "synthesis")
    if args.expected_diff_base != "manual" and current != args.expected_diff_base:
        sys.exit("sweep-state.py: synthesis cursor changed while run was active")
    workflow_triggers = [p for p in args.trigger_files.split(",") if p]
    if workflow_triggers != source["trigger_files"]:
        sys.exit("sweep-state.py: trigger paths do not match normalized manifest")
    coverage = source["corpus_commit_sha"]
    ancestry = subprocess.run(["git", "merge-base", "--is-ancestor", coverage, args.commit])
    if ancestry.returncode != 0:
        sys.exit("sweep-state.py: result commit does not descend from corpus snapshot")
    data["last_successful_synthesis"] = {
        "coverage_commit": coverage,
        "corpus_sha256": source.get("sha256"),
        "timestamp": _now_iso(),
        "trigger_paths": source["trigger_files"],
        "coverage_receipt_sha256": manifest["canonical_items_sha256"],
        "queue_items_emitted": len(manifest["items"]),
        "cost_usd": None,
        "result_commit": args.commit,
        "sweep_id": manifest["sweep_id"],
    }
    write_registry(data)
    print(f"sweep-state.py: synthesis coverage advanced to {coverage[:8]}")


def cmd_rebind_review_commit(args: argparse.Namespace) -> None:
    data = read_registry()
    current = data.get("last_successful_synthesis") or {}
    if current.get("result_commit") != args.old_commit:
        sys.exit("sweep-state.py: old synthesis result commit is not current")
    current["result_commit"] = args.new_commit
    write_registry(data)


def cmd_record_recovery(args: argparse.Namespace) -> None:
    # A recovery validates the preserved artifact but deliberately does not
    # claim new corpus coverage. GitHub Actions retains its run history.
    try:
        manifest = verify_manifest(Path(args.normalized_manifest))
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        sys.exit(f"sweep-state.py: recovery manifest validation failed: {exc}")
    if manifest["source"]["synthesis_log"] != args.synthesis_log:
        sys.exit("sweep-state.py: recovery source mismatch")
    print(f"sweep-state.py: validated supplemental recovery {manifest['sweep_id']}; cursor unchanged")


def cmd_should_sweep(_args: argparse.Namespace) -> None:
    # Retained for old callers. It now answers whether synthesis has pending
    # semantic paths; it never authorizes an automatic run.
    data = read_registry()
    base = _cursor(data, "synthesis")
    if not base:
        print("run")
        return
    print("run" if _git_changed_paths(base, ["wiki/*.md", "wiki/hypotheses/*.md"]) else "skip")


def cmd_init(args: argparse.Namespace) -> None:
    if REGISTRY_PATH.exists() and not args.force:
        sys.exit(f"sweep-state.py: {REGISTRY_PATH} exists; use migrate or --force")
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    now = _now_iso()
    data = _empty_registry()
    data["last_successful_propagation"] = {
        "coverage_commit": head, "result_commit": head, "timestamp": now,
        "changed_paths": [], "affected_paths": [], "blocked_paths": [], "cost_usd": 0.0,
    }
    data["last_successful_synthesis"] = {
        "coverage_commit": head, "corpus_sha256": None, "timestamp": now,
        "trigger_paths": [], "coverage_receipt_sha256": None,
        "queue_items_emitted": 0, "cost_usd": 0.0, "result_commit": head,
    }
    write_registry(data)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("read")
    sub.add_parser("migrate")
    sub.add_parser("pending-propagation-paths")
    sub.add_parser("pending-synthesis-paths")
    sub.add_parser("pending-paths", help="compatibility alias for pending synthesis paths")
    sub.add_parser("should-sweep")

    prop = sub.add_parser("update-propagation")
    prop.add_argument("--coverage-commit", required=True)
    prop.add_argument("--result-commit", required=True)
    prop.add_argument("--expected-cursor", default="")
    prop.add_argument("--changed-paths", default="")
    prop.add_argument("--affected-paths", default="")
    prop.add_argument("--blocked-paths", default="")
    prop.add_argument("--cost-usd", type=float, default=0.0)

    comp = sub.add_parser("record-comp-review")
    comp.add_argument("--comp-id", required=True)
    comp.add_argument("--comp-dir", required=True)
    comp.add_argument("--artifact-manifest-sha256", required=True)
    comp.add_argument("--source-commit", required=True)
    comp.add_argument("--review-receipt", required=True)
    comp.add_argument("--comp-verdict", required=True)
    comp.add_argument("--propagation-eligibility", required=True)
    comp.add_argument("--synthesis-eligibility", required=True)
    comp.add_argument("--derived-paths", default="")
    comp.add_argument("--cost-usd", type=float, default=0.0)

    elig = sub.add_parser("comp-eligibility")
    elig.add_argument("--comp-id", required=True)
    elig.add_argument("--lane", choices=["propagation", "synthesis"], required=True)

    failure = sub.add_parser("record-failure")
    failure.add_argument("--failure-id", "--run-id", dest="failure_id", required=True)
    failure.add_argument("--lane", "--failed-phase", dest="lane", required=True)
    failure.add_argument("--error-summary", default="")
    failure.add_argument("--paths", default="")
    # Ignored compatibility options from schema v1 workflows.
    failure.add_argument("--trigger", default="")
    failure.add_argument("--trigger-paths-count", type=int, default=0)

    resolve = sub.add_parser("resolve-failure")
    resolve.add_argument("--failure-id", required=True)

    success = sub.add_parser("update-success")
    success.add_argument("--commit", required=True)
    success.add_argument("--synthesis-log", required=True)
    success.add_argument("--normalized-manifest", required=True)
    success.add_argument("--expected-diff-base", required=True)
    success.add_argument("--trigger-files", default="")
    success.add_argument("--run-id", required=True)
    success.add_argument("--trigger", default="workflow_dispatch")

    recovery = sub.add_parser("record-recovery")
    recovery.add_argument("--review-commit", required=True)
    recovery.add_argument("--synthesis-log", required=True)
    recovery.add_argument("--normalized-manifest", required=True)
    recovery.add_argument("--run-id", required=True)
    recovery.add_argument("--trigger", default="workflow_dispatch")

    rebind = sub.add_parser("rebind-review-commit")
    rebind.add_argument("--old-commit", required=True)
    rebind.add_argument("--new-commit", required=True)

    init = sub.add_parser("init")
    init.add_argument("--force", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    handlers = {
        "read": cmd_read,
        "migrate": cmd_migrate,
        "pending-propagation-paths": cmd_pending_propagation_paths,
        "pending-synthesis-paths": cmd_pending_synthesis_paths,
        "pending-paths": cmd_pending_synthesis_paths,
        "update-propagation": cmd_update_propagation,
        "record-comp-review": cmd_record_comp_review,
        "comp-eligibility": cmd_comp_eligibility,
        "record-failure": cmd_record_failure,
        "resolve-failure": cmd_resolve_failure,
        "update-success": cmd_update_success,
        "record-recovery": cmd_record_recovery,
        "rebind-review-commit": cmd_rebind_review_commit,
        "should-sweep": cmd_should_sweep,
        "init": cmd_init,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
