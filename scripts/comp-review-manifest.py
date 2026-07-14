#!/usr/bin/env python3
"""Create and verify hash-bound snapshots for COMP review gates."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_NAMES = {".DS_Store"}
IGNORED_SUFFIXES = {".pyc"}


def repo_path(raw: str) -> Path:
    path = Path(raw)
    if not path.is_absolute():
        path = ROOT / path
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
        or "__pycache__" in path.parts
    )


def comp_files(comp_dir: Path, phase: str) -> tuple[list[Path], list[Path]]:
    design: list[Path] = []
    outputs: list[Path] = []
    for path in sorted(comp_dir.rglob("*")):
        if not path.is_file() or ignored(path):
            continue
        rel = path.relative_to(comp_dir)
        if rel.parts[0] == "reviews":
            continue
        if rel.parts[0] == "outputs":
            outputs.append(path)
        else:
            design.append(path)
    if phase == "post":
        return design + outputs, []
    return design, outputs


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

    current, prior_outputs = comp_files(comp_dir, args.phase)
    proposed = [repo_path(raw) for raw in args.proposed_file]
    if args.phase == "pre" and proposed:
        raise SystemExit("--proposed-file is valid only for a post-run manifest")
    if args.phase == "post" and not proposed:
        raise SystemExit("Post-run manifest requires every proposed update via --proposed-file")
    missing = [str(path) for path in proposed if not path.is_file()]
    if missing:
        raise SystemExit(f"Proposed files do not exist: {missing}")
    if len(set(proposed)) != len(proposed):
        raise SystemExit("Duplicate --proposed-file paths are not allowed")

    payload: dict[str, object] = {
        "schema_version": 1,
        "phase": args.phase,
        "comp_dir": relative(comp_dir),
        "files": [entry(path, "comp") for path in current]
        + [entry(path, "proposed_update") for path in sorted(proposed)],
        "prior_output_baseline": [
            entry(path, "prior_output") for path in prior_outputs
        ],
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

    phase = document.get("phase")
    if phase not in {"pre", "post"}:
        errors.append(f"invalid phase: {phase!r}")
    comp_dir = repo_path(str(document.get("comp_dir", "")))
    current_comp, current_prior_outputs = comp_files(comp_dir, str(phase))

    recorded_files = list(document.get("files", []))
    recorded_comp = [item for item in recorded_files if item.get("kind") == "comp"]
    recorded_proposed = [
        item for item in recorded_files if item.get("kind") == "proposed_update"
    ]
    current_comp_entries = [entry(path, "comp") for path in current_comp]
    current_proposed_entries: list[dict[str, object]] = []
    for item in recorded_proposed:
        path = repo_path(str(item.get("path", "")))
        if path.is_file():
            current_proposed_entries.append(entry(path, "proposed_update"))
    errors.extend(compare_entries(recorded_comp, current_comp_entries, "COMP file"))
    errors.extend(
        compare_entries(recorded_proposed, current_proposed_entries, "proposed update")
    )

    recorded_baseline = list(document.get("prior_output_baseline", []))
    current_baseline = [entry(path, "prior_output") for path in current_prior_outputs]
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
    create_parser.add_argument("--phase", choices=("pre", "post"), required=True)
    create_parser.add_argument("--comp-dir", required=True)
    create_parser.add_argument("--output", required=True)
    create_parser.add_argument("--proposed-file", action="append", default=[])
    create_parser.set_defaults(func=create)

    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("--manifest", required=True)
    check_parser.set_defaults(func=check)
    return root


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
