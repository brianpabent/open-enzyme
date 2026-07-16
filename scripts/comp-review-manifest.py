#!/usr/bin/env python3
"""Create and verify hash-bound snapshots for COMP review gates.

``pre`` and ``post`` are the mandatory authoring-time gates. ``push`` binds
the independent daemon review to the exact committed artifact plus every
current wiki surface that explicitly references it. Review files are excluded
from all three manifests so replacing a receipt cannot invalidate itself.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_NAMES = {".DS_Store"}
IGNORED_SUFFIXES = {".pyc"}
IGNORED_DIRS = {"__pycache__", ".claude", ".venv", "venv", "node_modules"}


def repo_path(raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = Path.cwd() / path
    path = path.resolve()
    if path != ROOT and ROOT not in path.parents:
        raise SystemExit(f"Path escapes repository: {raw}")
    return path


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def entry(path: Path, kind: str) -> dict[str, object]:
    return {
        "path": relative(path),
        "kind": kind,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def ignored(path: Path) -> bool:
    return (
        path.name in IGNORED_NAMES
        or path.suffix in IGNORED_SUFFIXES
        or any(part in IGNORED_DIRS or part.endswith("-env") for part in path.parts)
    )


def comp_files(comp_dir: Path, *, tracked_only: bool = False) -> tuple[list[Path], list[Path]]:
    design: list[Path] = []
    outputs: list[Path] = []
    if tracked_only:
        result = subprocess.run(
            ["git", "ls-files", "--", relative(comp_dir)], cwd=ROOT,
            text=True, capture_output=True, check=True,
        )
        candidates = [ROOT / raw for raw in result.stdout.splitlines()]
    else:
        candidates = list(comp_dir.rglob("*"))
    for path in sorted(candidates):
        if not path.is_file() or ignored(path):
            continue
        rel = path.relative_to(comp_dir)
        if rel.parts[0] == "reviews":
            continue
        if rel.parts[0] == "outputs":
            outputs.append(path)
        else:
            design.append(path)
    return design, outputs


def comp_id(comp_dir: Path) -> str:
    match = re.match(r"^(comp-\d{3})(?:-|$)", comp_dir.name)
    if not match:
        raise SystemExit(f"Not a COMP directory: {comp_dir}")
    return match.group(1)


def referencing_wiki_files(identifier: str, comp_dir: Path) -> list[Path]:
    result = subprocess.run(
        [
            "git", "grep", "-l", "-F", identifier, "--",
            "wiki/*.md", "wiki/hypotheses/*.md",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    paths: list[Path] = []
    for raw in result.stdout.splitlines():
        path = repo_path(raw)
        rel = path.relative_to(ROOT)
        if (
            path.is_file()
            and "reviews" not in rel.parts
            and path != comp_dir
            and comp_dir not in path.parents
        ):
            paths.append(path)
    return sorted(set(paths))


def manifest_digest(payload: dict[str, object]) -> str:
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def create(args: argparse.Namespace) -> None:
    comp_dir = repo_path(args.comp_dir)
    if not comp_dir.is_dir() or not comp_dir.name.startswith("comp-"):
        raise SystemExit(f"Not a COMP directory: {comp_dir}")

    output = repo_path(args.output)
    reviews_dir = comp_dir / "reviews"
    if reviews_dir.resolve() not in output.parents:
        raise SystemExit("Manifest output must live under the COMP reviews/ directory")

    design_files, output_files = comp_files(comp_dir, tracked_only=args.phase == "push")
    proposed = [repo_path(raw) for raw in args.proposed_file]
    if args.phase == "push":
        proposed.extend(referencing_wiki_files(comp_id(comp_dir), comp_dir))
        proposed = sorted(set(proposed))
    if args.phase == "pre" and proposed:
        raise SystemExit("--proposed-file is valid only for post-run or push manifests")
    if args.phase == "post" and not proposed:
        raise SystemExit("Post-run manifest requires every proposed update via --proposed-file")
    if any(path == comp_dir or comp_dir in path.parents for path in proposed):
        raise SystemExit("--proposed-file paths must be outside the COMP directory")
    missing = [str(path) for path in proposed if not path.is_file()]
    if missing:
        raise SystemExit(f"Proposed files do not exist: {missing}")
    if len(set(proposed)) != len(proposed):
        raise SystemExit("Duplicate --proposed-file paths are not allowed")

    payload: dict[str, object] = {
        "schema_version": 2 if args.phase == "push" else 1,
        "phase": args.phase,
        "comp_dir": relative(comp_dir),
        "files": [entry(path, "design") for path in design_files]
        + (
            [entry(path, "generated_output") for path in output_files]
            if args.phase in {"post", "push"}
            else []
        )
        + [entry(path, "proposed_update") for path in sorted(proposed)],
        "prior_output_baseline": [
            entry(path, "prior_output") for path in output_files
        ] if args.phase == "pre" else [],
    }
    document = dict(payload)
    document["manifest_sha256"] = manifest_digest(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(document["manifest_sha256"])


def compare_entries(
    recorded: list[dict[str, object]], current: list[dict[str, object]], label: str
) -> list[str]:
    errors: list[str] = []
    recorded_by_path = {str(item["path"]): item for item in recorded}
    current_by_path = {str(item["path"]): item for item in current}
    for path in sorted(recorded_by_path.keys() - current_by_path.keys()):
        errors.append(f"{label} removed: {path}")
    for path in sorted(current_by_path.keys() - recorded_by_path.keys()):
        errors.append(f"{label} added: {path}")
    for path in sorted(recorded_by_path.keys() & current_by_path.keys()):
        old = recorded_by_path[path]
        new = current_by_path[path]
        if old.get("sha256") != new.get("sha256"):
            errors.append(f"{label} changed: {path}")
        elif old.get("bytes") != new.get("bytes"):
            errors.append(f"{label} size changed: {path}")
    return errors


def check(args: argparse.Namespace) -> None:
    manifest_path = repo_path(args.manifest)
    document = json.loads(manifest_path.read_text())
    expected_digest = document.pop("manifest_sha256", None)
    actual_digest = manifest_digest(document)
    errors: list[str] = []
    if expected_digest != actual_digest:
        errors.append("manifest payload digest does not match manifest_sha256")

    if bool(args.review) != bool(args.required_line):
        errors.append("--review and --required-line must be supplied together")
    elif args.review:
        review_path = repo_path(args.review)
        if not review_path.is_file():
            errors.append(f"review receipt is missing: {relative(review_path)}")
        else:
            review_text = review_path.read_text(errors="replace")
            review_lines = [line.strip() for line in review_text.splitlines() if line.strip()]
            first_line = review_lines[0] if review_lines else ""
            if first_line != args.required_line:
                errors.append(
                    f"review receipt first non-empty line is not: {args.required_line}"
                )
            snapshot_line = f"REVIEWED_SNAPSHOT: {expected_digest}"
            if len(review_lines) < 2 or review_lines[1] != snapshot_line:
                errors.append(
                    "review receipt second non-empty line is not the exact "
                    f"manifest binding: {snapshot_line}"
                )

    phase = document.get("phase")
    if phase not in {"pre", "post", "push"}:
        errors.append(f"invalid phase: {phase!r}")
    comp_dir = repo_path(str(document.get("comp_dir", "")))
    current_design, current_outputs = comp_files(comp_dir, tracked_only=phase == "push")

    recorded_files = list(document.get("files", []))
    recorded_design = [item for item in recorded_files if item.get("kind") == "design"]
    recorded_outputs = [
        item for item in recorded_files if item.get("kind") == "generated_output"
    ]
    recorded_proposed = [
        item for item in recorded_files if item.get("kind") == "proposed_update"
    ]
    current_design_entries = [entry(path, "design") for path in current_design]
    current_output_entries = [
        entry(path, "generated_output") for path in current_outputs
    ]
    current_proposed_entries: list[dict[str, object]] = []
    for item in recorded_proposed:
        path = repo_path(str(item.get("path", "")))
        if path.is_file():
            current_proposed_entries.append(entry(path, "proposed_update"))
    errors.extend(compare_entries(recorded_design, current_design_entries, "design file"))
    if phase in {"post", "push"}:
        errors.extend(
            compare_entries(recorded_outputs, current_output_entries, "generated output")
        )
    elif recorded_outputs:
        errors.append("pre-run manifest unexpectedly contains generated_output entries")
    errors.extend(
        compare_entries(recorded_proposed, current_proposed_entries, "proposed update")
    )

    recorded_baseline = list(document.get("prior_output_baseline", []))
    current_baseline = [entry(path, "prior_output") for path in current_outputs]
    if phase in {"post", "push"}:
        if recorded_baseline:
            errors.append("post-run manifest unexpectedly contains a prior-output baseline")
        current_baseline = []
    errors.extend(compare_entries(recorded_baseline, current_baseline, "prior output"))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(expected_digest)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    subparsers = root.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--phase", choices=("pre", "post", "push"), required=True)
    create_parser.add_argument("--comp-dir", required=True)
    create_parser.add_argument("--output", required=True)
    create_parser.add_argument("--proposed-file", action="append", default=[])
    create_parser.set_defaults(func=create)

    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--manifest", required=True)
    check_parser.add_argument("--review")
    check_parser.add_argument("--required-line")
    check_parser.set_defaults(func=check)
    return root


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
