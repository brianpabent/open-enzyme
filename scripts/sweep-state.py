#!/usr/bin/env python3
"""
sweep-state.py — read/write the sweep automation state registry.

Component #2 of the sweep automation architecture (see
scripts/SWEEP-ARCHITECTURE.md). Replaces the brittle
`git log --grep='^sweep' -n 1` regex with an atomic file-based cursor.

The registry lives at `logs/sweep-state.json` and records:
  - last_successful_sweep: exact corpus-coverage commit + timestamp +
    synthesis/review provenance for the most recent Pass 3 that completed.
    The coverage cursor is the snapshot Pass 2 actually read, not the later
    review commit, so concurrent post-snapshot wiki edits remain pending.
  - recent_runs: bounded list (last 20) of workflow runs with outcome,
    failed phase, and trigger metadata. Used by /sweep-status and the
    watchdog cron.

Subcommands:
  read                            — print the registry as JSON.
  update-success                  — record Pass 3 success; update
                                    last_successful_sweep + append a
                                    recent_runs entry.
  record-recovery                 — record a supplemental exact-artifact
                                    review without advancing the cursor.
  rebind-review-commit            — repair review-commit provenance after a
                                    successful git rebase; cursor is unchanged.
  record-failure                  — append a failed-run entry to
                                    recent_runs without touching
                                    last_successful_sweep.
  pending-paths                   — print wiki/*.md files modified since
                                    last_successful_sweep.commit (excluding
                                    synthesis/queue/).
  init                            — initialize the registry from the most
                                    recent existing v4-synthesis-*.md log
                                    and sweep-3-review commit. One-time
                                    backfill.

The registry is a small JSON file. The workflow has a top-level
`concurrency` group preventing two sweeps simultaneously, so reads and
writes don't race against each other within the daemon. Hand-runs (e.g.
manual /sweep-catchup) and the daemon may interleave but never write
concurrently because workflow_dispatch and push triggers share the same
concurrency group.

Schema is versioned (`schema_version: 1`); future migrations bump the
version and add a `migrate_v1_to_v2` path here.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from synthesis_normalize import NormalizationError, verify_manifest

REGISTRY_PATH = Path("logs/sweep-state.json")
SCHEMA_VERSION = 1
MAX_RECENT_RUNS = 20


def _now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _empty_registry() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "last_successful_sweep": None,
        "recent_runs": [],
    }


def read_registry() -> dict:
    if not REGISTRY_PATH.exists():
        return _empty_registry()
    with REGISTRY_PATH.open() as f:
        data = json.load(f)
    if data.get("schema_version") != SCHEMA_VERSION:
        sys.exit(f"sweep-state.py: unknown schema_version {data.get('schema_version')!r}; "
                 f"expected {SCHEMA_VERSION}. Migrate manually.")
    return data


def write_registry(data: dict) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = REGISTRY_PATH.with_suffix(".json.tmp")
    with tmp_path.open("w") as f:
        json.dump(data, f, indent=2, sort_keys=False)
        f.write("\n")
    os.replace(tmp_path, REGISTRY_PATH)


def _trim_recent(runs: list, keep: int = MAX_RECENT_RUNS) -> list:
    return runs[-keep:]


def cmd_read(_args: argparse.Namespace) -> None:
    data = read_registry()
    print(json.dumps(data, indent=2))


def cmd_update_success(args: argparse.Namespace) -> None:
    data = read_registry()
    try:
        manifest = verify_manifest(Path(args.normalized_manifest))
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        sys.exit(f"sweep-state.py: refusing cursor advance; manifest validation failed: {exc}")

    source = manifest["source"]
    if source["synthesis_log"] != args.synthesis_log:
        sys.exit("sweep-state.py: synthesis log does not match normalized manifest source")
    if source["diff_base"] != args.expected_diff_base:
        sys.exit(
            "sweep-state.py: diff-base mismatch between workflow and manifest: "
            f"{args.expected_diff_base!r} != {source['diff_base']!r}"
        )
    workflow_triggers = [p for p in args.trigger_files.split(",") if p]
    if workflow_triggers != source["trigger_files"]:
        sys.exit("sweep-state.py: trigger-file list does not match normalized manifest")
    current_cursor = (data.get("last_successful_sweep") or {}).get("commit")
    if args.expected_diff_base != "manual" and current_cursor != args.expected_diff_base:
        sys.exit(
            "sweep-state.py: cursor changed since this synthesis batch began; "
            f"current={current_cursor!r}, expected={args.expected_diff_base!r}. "
            "Refusing to bless a stale or superseded artifact."
        )
    coverage_commit = source["corpus_commit_sha"]
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", coverage_commit, args.commit],
        capture_output=True,
    )
    if ancestry.returncode != 0:
        sys.exit(
            "sweep-state.py: review commit does not descend from the manifest's corpus snapshot"
        )

    data["last_successful_sweep"] = {
        # The cursor is the exact corpus snapshot Pass 2 read, not the later
        # review commit. If unrelated wiki work lands while the model is
        # running and Pass 3 rebases over it, that work therefore remains
        # visible to pending-paths instead of being silently blessed.
        "commit": coverage_commit,
        "coverage_commit": coverage_commit,
        "timestamp": _now_iso(),
        "synthesis_log": args.synthesis_log,
        "normalized_manifest": args.normalized_manifest,
        "sweep_id": manifest["sweep_id"],
        "source_commit": source["commit_sha"],
        "trigger_commit": source["trigger_commit_sha"],
        "source_synthesis_sha256": source["sha256"],
        "canonical_items_sha256": manifest["canonical_items_sha256"],
        "normalized_status": manifest["status"],
        "normalized_item_count": len(manifest["items"]),
        "review_commit": args.commit,
        "trigger_files": source["trigger_files"],
        "run_id": args.run_id,
    }
    data["recent_runs"].append({
        "run_id": args.run_id,
        "trigger": args.trigger,
        "completed_at": _now_iso(),
        "outcome": "success",
        "failed_phase": None,
        "trigger_paths_count": len(source["trigger_files"]),
        "synthesis_log": args.synthesis_log,
        "normalized_manifest": args.normalized_manifest,
        "sweep_id": manifest["sweep_id"],
        "normalized_status": manifest["status"],
        "normalized_item_count": len(manifest["items"]),
        "coverage_commit": coverage_commit,
        "review_commit": args.commit,
    })
    data["recent_runs"] = _trim_recent(data["recent_runs"])
    write_registry(data)
    print(
        f"sweep-state.py: recorded success for run {args.run_id}; "
        f"coverage={coverage_commit[:8]} review={args.commit[:8]}"
    )


def _validated_recovery_manifest(args: argparse.Namespace) -> dict:
    try:
        manifest = verify_manifest(Path(args.normalized_manifest))
    except (OSError, json.JSONDecodeError, NormalizationError) as exc:
        sys.exit(f"sweep-state.py: recovery manifest validation failed: {exc}")
    if manifest["source"]["synthesis_log"] != args.synthesis_log:
        sys.exit("sweep-state.py: recovery synthesis log does not match manifest source")
    return manifest


def cmd_record_recovery(args: argparse.Namespace) -> None:
    """Record exact-artifact review while deliberately preserving the cursor."""
    data = read_registry()
    manifest = _validated_recovery_manifest(args)
    coverage_commit = manifest["source"]["corpus_commit_sha"]
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", coverage_commit, args.review_commit],
        capture_output=True,
    )
    if ancestry.returncode != 0:
        sys.exit("sweep-state.py: recovery review commit does not descend from corpus snapshot")
    cursor_before = (data.get("last_successful_sweep") or {}).get("commit")
    data["recent_runs"].append({
        "run_id": args.run_id,
        "trigger": args.trigger,
        "completed_at": _now_iso(),
        "outcome": "supplemental_recovery",
        "failed_phase": None,
        "cursor_advanced": False,
        "cursor_preserved": cursor_before,
        "review_commit": args.review_commit,
        "synthesis_log": args.synthesis_log,
        "normalized_manifest": args.normalized_manifest,
        "sweep_id": manifest["sweep_id"],
        "normalized_status": manifest["status"],
        "normalized_item_count": len(manifest["items"]),
    })
    data["recent_runs"] = _trim_recent(data["recent_runs"])
    write_registry(data)
    print(
        f"sweep-state.py: recorded supplemental recovery {manifest['sweep_id']} "
        f"without advancing cursor {str(cursor_before)[:8]}"
    )


def cmd_rebind_review_commit(args: argparse.Namespace) -> None:
    """Update review provenance after rebase; never move the coverage cursor."""
    data = read_registry()
    last = data.get("last_successful_sweep") or {}
    rebound = False
    if last.get("review_commit") == args.old_commit:
        last["review_commit"] = args.new_commit
        rebound = True
    for run in reversed(data.get("recent_runs", [])):
        if run.get("review_commit") == args.old_commit:
            run["review_commit"] = args.new_commit
            rebound = True
            break
    if not rebound:
        sys.exit(
            "sweep-state.py: review rebind old SHA is absent from current and recent state: "
            f"{args.old_commit!r}"
        )
    write_registry(data)
    print(
        f"sweep-state.py: rebound review provenance "
        f"{args.old_commit[:8]} -> {args.new_commit[:8]}; cursor unchanged"
    )


def cmd_record_failure(args: argparse.Namespace) -> None:
    data = read_registry()
    data["recent_runs"].append({
        "run_id": args.run_id,
        "trigger": args.trigger,
        "completed_at": _now_iso(),
        "outcome": "failure",
        "failed_phase": args.failed_phase,
        "error_summary": args.error_summary,
        "trigger_paths_count": args.trigger_paths_count,
    })
    data["recent_runs"] = _trim_recent(data["recent_runs"])
    write_registry(data)
    print(f"sweep-state.py: recorded failure for run {args.run_id} (phase {args.failed_phase})")


def cmd_pending_paths(_args: argparse.Namespace) -> None:
    data = read_registry()
    last = data.get("last_successful_sweep") or {}
    base = last.get("commit")
    if not base:
        sys.exit("sweep-state.py: no last_successful_sweep recorded; run `init` first.")
    r = subprocess.run(
        ["git", "diff", "--name-only", base, "HEAD", "--", "wiki/*.md"],
        capture_output=True, text=True, check=True,
    )
    paths = [
        p for p in r.stdout.strip().splitlines()
        if p
    ]
    for p in sorted(set(paths)):
        print(p)


def cmd_should_sweep(_args: argparse.Namespace) -> None:
    """Decide whether the workflow should run a sweep on the current HEAD.

    Prints `run` or `skip` (and a one-line rationale to stderr) based on:
      - last_successful_sweep cursor in the registry
      - commits between cursor and HEAD that touched wiki/*.md
      - exclusion of daemon-self-writes (subject starts with sweep-1-/sweep-2-/sweep-3-)
      - exclusion of commits whose full message contains [skip-wiki-sweep]

    A sweep runs iff at least one wiki-touching commit since cursor is neither
    a daemon-self-write nor explicitly skip-marked. This replaces the original
    head-commit-only [skip-wiki-sweep] check that silently dropped wiki content
    when a non-wiki-touching tooling commit with the marker landed on top of a
    push that also contained user wiki commits.
    """
    data = read_registry()
    last = data.get("last_successful_sweep") or {}
    base = last.get("commit")
    if not base:
        print("run")
        print("sweep-state.py should-sweep: no cursor recorded; defaulting to run", file=sys.stderr)
        return

    # Subject + full body for each wiki-touching commit since cursor.  Use
    # NUL-separated records so commit messages with newlines parse cleanly.
    sep = "\x1e"  # ASCII record separator, unlikely in commit messages
    r = subprocess.run(
        ["git", "log", f"--format=%H%x00%s%x00%B{sep}", f"{base}..HEAD", "--", "wiki/*.md"],
        capture_output=True, text=True, check=True,
    )
    records = [rec for rec in r.stdout.split(sep) if rec.strip()]
    if not records:
        print("skip")
        print("sweep-state.py should-sweep: no wiki/*.md commits since cursor", file=sys.stderr)
        return

    DAEMON_PREFIXES = ("sweep-1-", "sweep-2-", "sweep-3-")
    SKIP_MARKER = "[skip-wiki-sweep]"
    sweepable = []
    for rec in records:
        parts = rec.lstrip("\n").split("\x00", 2)
        if len(parts) < 3:
            continue
        sha, subject, body = parts
        if subject.startswith(DAEMON_PREFIXES):
            continue
        if SKIP_MARKER in subject or SKIP_MARKER in body:
            continue
        sweepable.append((sha[:8], subject))

    if sweepable:
        print("run")
        print(f"sweep-state.py should-sweep: {len(sweepable)} sweepable wiki commit(s) since cursor:",
              file=sys.stderr)
        for sha, subject in sweepable:
            print(f"  {sha} {subject}", file=sys.stderr)
    else:
        print("skip")
        print(f"sweep-state.py should-sweep: {len(records)} wiki commit(s) since cursor; "
              "all are daemon-self-writes or marked [skip-wiki-sweep]", file=sys.stderr)


def cmd_init(args: argparse.Namespace) -> None:
    """One-time backfill from existing logs/v4-synthesis-*.md + last sweep-3-review commit."""
    if REGISTRY_PATH.exists() and not args.force:
        sys.exit(f"sweep-state.py: {REGISTRY_PATH} already exists; pass --force to overwrite.")

    # Find most recent v4-synthesis-*.md log
    logs_dir = Path("logs")
    synthesis_logs = sorted(
        [p for p in logs_dir.glob("v4-synthesis-*.md")],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not synthesis_logs:
        sys.exit("sweep-state.py: no logs/v4-synthesis-*.md files; cannot backfill.")
    latest_log = synthesis_logs[0]

    # Find most recent sweep-3-review commit on main
    r = subprocess.run(
        ["git", "log", "--grep=^sweep-3-review:", "-n", "1",
         "--format=%H %cI", "main"],
        capture_output=True, text=True, check=True,
    )
    line = r.stdout.strip()
    if not line:
        sys.exit("sweep-state.py: no sweep-3-review: commit found on main; cannot backfill.")
    parts = line.split(" ", 1)
    if len(parts) != 2:
        sys.exit(f"sweep-state.py: malformed git log output: {line!r}")
    commit, timestamp = parts

    data = _empty_registry()
    data["last_successful_sweep"] = {
        "commit": commit,
        "timestamp": timestamp,
        "synthesis_log": str(latest_log),
        "review_commit": commit,
        "trigger_files": [],
        "run_id": None,
        "_backfilled": True,
        "_backfilled_at": _now_iso(),
    }
    write_registry(data)
    print(f"sweep-state.py: initialized {REGISTRY_PATH}")
    print(f"  last_successful_sweep.commit = {commit[:8]} ({timestamp})")
    print(f"  synthesis_log = {latest_log}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("read", help="print the registry as JSON")

    s_us = sub.add_parser("update-success", help="record Pass 3 success")
    s_us.add_argument("--commit", required=True)
    s_us.add_argument("--synthesis-log", required=True)
    s_us.add_argument("--normalized-manifest", required=True)
    s_us.add_argument("--expected-diff-base", required=True)
    s_us.add_argument("--trigger-files", default="")
    s_us.add_argument("--run-id", required=True)
    s_us.add_argument("--trigger", default="push", choices=["push", "workflow_dispatch", "watchdog"])

    s_rr = sub.add_parser(
        "record-recovery",
        help="record supplemental exact-artifact recovery without advancing cursor",
    )
    s_rr.add_argument("--review-commit", required=True)
    s_rr.add_argument("--synthesis-log", required=True)
    s_rr.add_argument("--normalized-manifest", required=True)
    s_rr.add_argument("--run-id", required=True)
    s_rr.add_argument("--trigger", default="workflow_dispatch",
                      choices=["push", "workflow_dispatch", "watchdog"])

    s_rb = sub.add_parser(
        "rebind-review-commit",
        help="repair review provenance after rebase without moving coverage cursor",
    )
    s_rb.add_argument("--old-commit", required=True)
    s_rb.add_argument("--new-commit", required=True)

    s_rf = sub.add_parser("record-failure", help="record a failed run")
    s_rf.add_argument("--run-id", required=True)
    s_rf.add_argument("--failed-phase", required=True,
                      choices=["pass-1-propagate", "pass-1-push", "pass-2-synthesize",
                               "pass-2-push", "pass-3-review", "pass-3-push", "trigger-detection"])
    s_rf.add_argument("--error-summary", default="")
    s_rf.add_argument("--trigger", default="push", choices=["push", "workflow_dispatch", "watchdog"])
    s_rf.add_argument("--trigger-paths-count", type=int, default=0)

    sub.add_parser("pending-paths", help="print wiki/*.md files since last successful sweep")

    sub.add_parser("should-sweep", help="print 'run' or 'skip' based on registry + commit-prefix + skip-marker analysis")

    s_init = sub.add_parser("init", help="backfill the registry from existing logs + git history")
    s_init.add_argument("--force", action="store_true")

    args = p.parse_args()

    handlers = {
        "read": cmd_read,
        "update-success": cmd_update_success,
        "record-recovery": cmd_record_recovery,
        "rebind-review-commit": cmd_rebind_review_commit,
        "record-failure": cmd_record_failure,
        "pending-paths": cmd_pending_paths,
        "should-sweep": cmd_should_sweep,
        "init": cmd_init,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
