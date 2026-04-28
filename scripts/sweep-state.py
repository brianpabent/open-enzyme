#!/usr/bin/env python3
"""
sweep-state.py — read/write the sweep automation state registry.

Component #2 of the sweep automation architecture (see
scripts/SWEEP-ARCHITECTURE.md). Replaces the brittle
`git log --grep='^sweep' -n 1` regex with an atomic file-based cursor.

The registry lives at `logs/sweep-state.json` and records:
  - last_successful_sweep: commit + timestamp + synthesis log of the most
    recent Pass 3 that completed successfully. Updated only by the workflow's
    Pass 3 step, only on push success.
  - recent_runs: bounded list (last 20) of workflow runs with outcome,
    failed phase, and trigger metadata. Used by /sweep-status and the
    watchdog cron.

Subcommands:
  read                            — print the registry as JSON.
  update-success                  — record Pass 3 success; update
                                    last_successful_sweep + append a
                                    recent_runs entry.
  record-failure                  — append a failed-run entry to
                                    recent_runs without touching
                                    last_successful_sweep.
  pending-paths                   — print wiki/*.md files modified since
                                    last_successful_sweep.commit (excluding
                                    wiki/synthesis.md).
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
    data["last_successful_sweep"] = {
        "commit": args.commit,
        "timestamp": _now_iso(),
        "synthesis_log": args.synthesis_log,
        "review_commit": args.commit,
        "trigger_files": args.trigger_files.split(",") if args.trigger_files else [],
        "run_id": args.run_id,
    }
    data["recent_runs"].append({
        "run_id": args.run_id,
        "trigger": args.trigger,
        "completed_at": _now_iso(),
        "outcome": "success",
        "failed_phase": None,
        "trigger_paths_count": len(args.trigger_files.split(",")) if args.trigger_files else 0,
        "synthesis_log": args.synthesis_log,
    })
    data["recent_runs"] = _trim_recent(data["recent_runs"])
    write_registry(data)
    print(f"sweep-state.py: recorded success for run {args.run_id} at commit {args.commit[:8]}")


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
        if p and p != "wiki/synthesis.md"
    ]
    for p in sorted(set(paths)):
        print(p)


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
    s_us.add_argument("--trigger-files", default="")
    s_us.add_argument("--run-id", required=True)
    s_us.add_argument("--trigger", default="push", choices=["push", "workflow_dispatch", "watchdog"])

    s_rf = sub.add_parser("record-failure", help="record a failed run")
    s_rf.add_argument("--run-id", required=True)
    s_rf.add_argument("--failed-phase", required=True,
                      choices=["pass-1-propagate", "pass-1-push", "pass-2-synthesize",
                               "pass-2-push", "pass-3-review", "pass-3-push", "trigger-detection"])
    s_rf.add_argument("--error-summary", default="")
    s_rf.add_argument("--trigger", default="push", choices=["push", "workflow_dispatch", "watchdog"])
    s_rf.add_argument("--trigger-paths-count", type=int, default=0)

    sub.add_parser("pending-paths", help="print wiki/*.md files since last successful sweep")

    s_init = sub.add_parser("init", help="backfill the registry from existing logs + git history")
    s_init.add_argument("--force", action="store_true")

    args = p.parse_args()

    handlers = {
        "read": cmd_read,
        "update-success": cmd_update_success,
        "record-failure": cmd_record_failure,
        "pending-paths": cmd_pending_paths,
        "init": cmd_init,
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
