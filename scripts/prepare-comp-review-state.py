#!/usr/bin/env python3
"""Fail closed before COMP push review and remove non-result artifacts from review scope."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "logs" / "sweep-state.json"
PUSH_RECEIPTS = (
    "push-review.json",
    "push-review.md",
    "push-review.manifest.json",
    "push-review.preflight.manifest.json",
)


def now_iso() -> str:
    return (
        dt.datetime.now(dt.timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def comp_id(comp_dir: Path) -> str:
    return comp_dir.name[:8]


def resolve(raw: str) -> Path:
    path = (ROOT / raw).resolve()
    if path != ROOT and ROOT not in path.parents:
        raise SystemExit(f"path escapes repository: {raw}")
    if not path.is_dir() or not path.name.startswith("comp-"):
        raise SystemExit(f"not a COMP directory: {raw}")
    return path


def remove_push_receipts(comp_dir: Path) -> None:
    reviews = comp_dir / "reviews"
    for name in PUSH_RECEIPTS:
        (reviews / name).unlink(missing_ok=True)


def proposed_paths(comp_dir: Path) -> list[str]:
    manifest_path = comp_dir / "reviews" / "post-run.manifest.json"
    if not manifest_path.is_file():
        return []
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError:
        return []
    return sorted(
        {
            str(item["path"])
            for item in manifest.get("files", [])
            if item.get("kind") == "proposed_update"
            and isinstance(item.get("path"), str)
            and (ROOT / str(item["path"])).is_file()
        }
    )


def pre_run_only(comp_dir: Path) -> bool:
    reviews = comp_dir / "reviews"
    pre_manifest = reviews / "pre-run.manifest.json"
    pre_review = reviews / "pre-run.md"
    post_manifest = reviews / "post-run.manifest.json"
    post_review = reviews / "post-run.md"
    if not (
        pre_manifest.is_file()
        and pre_review.is_file()
        and not post_manifest.exists()
        and not post_review.exists()
    ):
        return False
    result = run(
        [
            "python3",
            "scripts/comp-review-manifest.py",
            "check",
            "--manifest",
            str(pre_manifest.relative_to(ROOT)),
            "--review",
            str(pre_review.relative_to(ROOT)),
            "--required-line",
            "PRE_RUN_GATE: GO",
        ]
    )
    if result.returncode:
        raise SystemExit(
            f"{comp_id(comp_dir)} has an invalid pre-run-only lifecycle:\n"
            + (result.stderr or result.stdout)
        )
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="newline-delimited COMP directories")
    parser.add_argument("--comp-dir", action="append", default=[])
    parser.add_argument("--review-output", required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()

    if not args.input and not args.comp_dir:
        parser.error("provide --input or at least one --comp-dir")
    input_lines = []
    if args.input:
        input_lines.extend(Path(args.input).read_text().splitlines())
    input_lines.extend(args.comp_dir)
    selected = [
        resolve(line.strip())
        for line in input_lines
        if line.strip()
    ]
    state = json.loads(STATE_PATH.read_text())
    records = state.setdefault("comp_reviews", {})
    review_candidates: list[str] = []
    counts = {"tombstone": 0, "pre_run_only": 0, "pending_review": 0}

    for comp_dir in selected:
        identifier = comp_id(comp_dir)
        relative = comp_dir.relative_to(ROOT).as_posix()
        prior = records.get(identifier, {})

        if (comp_dir / "invalidation.json").is_file():
            result = run(
                [
                    "python3",
                    "scripts/check-comp-invalidation.py",
                    "--comp-dir",
                    relative,
                ]
            )
            if result.returncode:
                raise SystemExit(result.stdout + result.stderr)
            records.pop(identifier, None)
            remove_push_receipts(comp_dir)
            counts["tombstone"] += 1
            continue

        if pre_run_only(comp_dir):
            records.pop(identifier, None)
            remove_push_receipts(comp_dir)
            counts["pre_run_only"] += 1
            continue

        derived = sorted(
            set(prior.get("derived_paths", [])) | set(proposed_paths(comp_dir))
        )
        remove_push_receipts(comp_dir)
        records[identifier] = {
            "comp_dir": relative,
            "artifact_manifest_sha256": None,
            "source_commit": args.source_commit,
            "review_receipt": None,
            "comp_verdict": "review_pending_exact_push",
            "propagation_eligibility": "blocked",
            "synthesis_eligibility": "blocked",
            "derived_paths": derived,
            "timestamp": now_iso(),
            "cost_usd": None,
            "pending_reason": "changed completed artifact awaits exact push review",
        }
        review_candidates.append(relative)
        counts["pending_review"] += 1

    temporary = STATE_PATH.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(state, indent=2) + "\n")
    temporary.replace(STATE_PATH)
    Path(args.review_output).write_text(
        "".join(f"{path}\n" for path in review_candidates)
    )
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
