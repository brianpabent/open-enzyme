#!/usr/bin/env python3
"""Validate COMP quarantine and retirement-governance state.

`quarantine.json` is a deterministic, non-runnable holding state. It retains
the complete artifact in HEAD while excluding it from execution, propagation,
push review, and synthesis. Entering or persisting in quarantine spends no
model tokens.

`invalidation.json` is a final deletion state. Schema-v1 ledgers are preserved
as historical baselines, but every new retirement must use schema v2 with a
bound independent disposition review, explicit decision ownership, mapped
surviving scope, a unique-detail audit, and a closed dependency cascade.
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "wiki" / "etc" / "experiments"
COMP_RE = re.compile(r"^(comp-\d{3})(?:-|$)")
ALLOWED_DETAIL_DISPOSITIONS = {
    "canonicalized",
    "invalidated",
    "historical_git_only",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_comp(raw: str) -> Path:
    path = (ROOT / raw).resolve()
    if path != ROOT and ROOT not in path.parents:
        raise SystemExit(f"path escapes repository: {raw}")
    if not path.is_dir() or not COMP_RE.match(path.name):
        raise SystemExit(f"not a comp-NNN directory: {raw}")
    return path


def artifact_paths(comp_dir: Path) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "--",
            relative(comp_dir),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    paths: list[Path] = []
    for raw in result.stdout.splitlines():
        path = ROOT / raw
        if not path.is_file():
            continue
        local = path.relative_to(comp_dir)
        if local.parts[0] == "reviews":
            continue
        if local.as_posix() in {"quarantine.json", "invalidation.json"}:
            continue
        paths.append(path)
    return sorted(paths)


def artifact_manifest(comp_dir: Path) -> list[dict[str, object]]:
    return [
        {
            "path": path.relative_to(comp_dir).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in artifact_paths(comp_dir)
    ]


def artifact_dependencies(comp_dir: Path) -> list[dict[str, object]]:
    """Bind imported modules from the experiments-level shared library.

    Several legacy COMPs insert ``../lib`` into ``sys.path`` and then import a
    scoring module. Those modules are part of the computational object even
    though they live outside the COMP directory.
    """
    shared_lib = comp_dir.parent / "lib"
    if not shared_lib.is_dir():
        return []
    dependencies: set[Path] = set()
    pending = [
        path for path in artifact_paths(comp_dir)
        if path.suffix == ".py"
    ]
    inspected: set[Path] = set()
    while pending:
        path = pending.pop()
        if path in inspected:
            continue
        inspected.add(path)
        if path.suffix != ".py":
            continue
        try:
            tree = ast.parse(path.read_text(errors="replace"))
        except SyntaxError:
            continue
        modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                modules.add(node.module.split(".", 1)[0])
        for module in modules:
            candidate = shared_lib / f"{module}.py"
            if candidate.is_file() and candidate not in dependencies:
                dependencies.add(candidate)
                pending.append(candidate)
    return [
        {
            "path": relative(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sorted(dependencies)
    ]


def canonical_manifest_sha256(manifest: list[dict[str, object]]) -> str:
    payload = json.dumps(
        manifest,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def canonical_quarantine_sha256(
    manifest: list[dict[str, object]],
    dependencies: list[dict[str, object]],
) -> str:
    payload = {
        "artifact_manifest": manifest,
        "artifact_dependencies": dependencies,
    }
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()


def _date(value: object, field: str, errors: list[str]) -> dt.date | None:
    if not isinstance(value, str):
        errors.append(f"{field} must be an ISO date")
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"{field} must be an ISO date")
        return None


def _existing_wiki_path(value: object, field: str, errors: list[str]) -> Path | None:
    if not isinstance(value, str) or not value.startswith("wiki/"):
        errors.append(f"{field} must be a repo-relative wiki/ path")
        return None
    path = ROOT / value
    if not path.is_file():
        errors.append(f"{field} does not exist: {value}")
        return None
    return path


def _repo_file(value: object, field: str, errors: list[str]) -> Path | None:
    if not isinstance(value, str):
        errors.append(f"{field} must be a repo-relative path")
        return None
    path = (ROOT / value).resolve()
    if path == ROOT or ROOT not in path.parents:
        errors.append(f"{field} escapes the repository")
        return None
    if not path.is_file():
        errors.append(f"{field} does not exist: {value}")
        return None
    return path


def _heading_exists(path: Path, heading: object) -> bool:
    if not isinstance(heading, str) or not heading.startswith("#"):
        return False
    return heading in path.read_text(errors="replace").splitlines()


def surviving_items(document: dict[str, object]) -> list[str]:
    scope = document.get("surviving_scope")
    if not isinstance(scope, dict):
        return []
    values = scope.get("statements")
    if values is None:
        values = scope.get("questions")
    if values is None and isinstance(scope.get("statement"), str):
        values = [scope["statement"]]
    if values is None and isinstance(scope.get("observation"), str):
        values = [scope["observation"]]
    if not isinstance(values, list):
        return []
    return [str(value) for value in values if str(value).strip()]


def validate_quarantine(comp_dir: Path, *, today: dt.date | None = None) -> list[str]:
    errors: list[str] = []
    marker = comp_dir / "quarantine.json"
    if not marker.is_file():
        return ["quarantine.json is missing"]
    try:
        document = json.loads(marker.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"quarantine.json is unreadable: {exc}"]

    match = COMP_RE.match(comp_dir.name)
    expected = match.group(1) if match else ""
    if document.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if document.get("comp") != expected:
        errors.append(f"comp must be {expected}")
    if document.get("status") != "quarantined":
        errors.append("status must be quarantined")
    if document.get("runnable") is not False:
        errors.append("runnable must be false")
    if (comp_dir / "invalidation.json").exists():
        errors.append("quarantine.json and invalidation.json may not coexist")
    if not isinstance(document.get("owner"), str) or not document["owner"].strip():
        errors.append("owner is required")
    if not isinstance(document.get("reason"), str) or not document["reason"].strip():
        errors.append("reason is required")
    if document.get("decision_status") not in {
        "pending_re_review",
        "repair_in_progress",
        "final_disposition_pending",
    }:
        errors.append("decision_status is invalid")
    blocked = document.get("blocked_scope")
    if not isinstance(blocked, list) or not blocked or not all(
        isinstance(item, str) and item.strip() for item in blocked
    ):
        errors.append("blocked_scope must contain at least one non-empty statement")
    _existing_wiki_path(
        document.get("current_evidence_home"),
        "current_evidence_home",
        errors,
    )
    entered = _date(document.get("entered_on"), "entered_on", errors)
    expires = _date(document.get("expires_on"), "expires_on", errors)
    if entered and expires and expires <= entered:
        errors.append("expires_on must be after entered_on")
    check_date = today or dt.date.today()
    if expires and expires < check_date:
        errors.append(
            f"quarantine expired on {expires.isoformat()}; restore, renew with a "
            "bounded rationale, or complete the approved retirement"
        )

    recorded = document.get("artifact_manifest")
    recorded_dependencies = document.get("artifact_dependencies")
    live_manifest_sha: str | None = None
    if not isinstance(recorded, list) or not recorded:
        errors.append("artifact_manifest must retain the complete non-review artifact")
    elif not isinstance(recorded_dependencies, list):
        errors.append("artifact_dependencies must be a list")
    else:
        actual = artifact_manifest(comp_dir)
        actual_dependencies = artifact_dependencies(comp_dir)
        if recorded != actual:
            errors.append("artifact_manifest does not match the complete live artifact")
        if recorded_dependencies != actual_dependencies:
            errors.append(
                "artifact_dependencies do not match imported shared-library code"
            )
        live_manifest_sha = canonical_quarantine_sha256(
            actual,
            actual_dependencies,
        )
        if document.get("artifact_manifest_sha256") != live_manifest_sha:
            errors.append("artifact_manifest_sha256 does not bind the live artifact")
        names = {str(item.get("path")) for item in recorded if isinstance(item, dict)}
        if "README.md" not in names:
            errors.append("artifact_manifest must include README.md")
        if not any(
            name.startswith(("inputs/", "outputs/"))
            or name.endswith((".py", ".R", ".ipynb"))
            for name in names
        ):
            errors.append("quarantine must retain code, inputs, or outputs beyond README.md")

    disposition_review = document.get("disposition_review")
    if disposition_review is not None:
        if not isinstance(disposition_review, dict):
            errors.append("disposition_review must be an object")
        else:
            review_path_raw = disposition_review.get("path")
            if not isinstance(review_path_raw, str):
                errors.append("disposition_review.path is required")
            else:
                review_path = _repo_file(
                    review_path_raw,
                    "disposition_review.path",
                    errors,
                )
                if review_path:
                    review_text = review_path.read_text(errors="replace")
                    if disposition_review.get("sha256") != sha256(review_path):
                        errors.append("disposition review SHA-256 mismatch")
                    if live_manifest_sha and (
                        f"ARTIFACT_MANIFEST_SHA256: {live_manifest_sha}"
                        not in review_text
                    ):
                        errors.append(
                            "disposition review does not bind the live artifact"
                        )
                    if not re.search(
                        r"^DISPOSITION_REVIEW: "
                        r"(REPAIRABLE|RETIREMENT_JUSTIFIED|INSUFFICIENT)$",
                        review_text,
                        re.MULTILINE,
                    ):
                        errors.append(
                            "disposition review lacks a recognized disposition"
                        )
    if (
        document.get("decision_status") == "final_disposition_pending"
        and disposition_review is None
    ):
        errors.append(
            "final_disposition_pending requires a bound disposition_review"
        )

    restored_from = document.get("restored_from_commit")
    if restored_from is not None:
        result = subprocess.run(
            ["git", "rev-parse", f"{restored_from}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            errors.append("restored_from_commit does not resolve")
    return errors


def validate_invalidation_governance(comp_dir: Path) -> list[str]:
    errors: list[str] = []
    marker = comp_dir / "invalidation.json"
    try:
        document = json.loads(marker.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalidation.json is unreadable: {exc}"]

    invalidated = document.get("invalidated_scope")
    if not isinstance(invalidated, list) or not invalidated or not all(
        isinstance(item, str) and item.strip() for item in invalidated
    ):
        errors.append("invalidated_scope must contain claim-class statements")

    scope = document.get("surviving_scope")
    if not isinstance(scope, dict) or not isinstance(scope.get("kind"), str):
        errors.append("surviving_scope must declare a kind")
    elif scope.get("kind") == "none":
        if not isinstance(scope.get("justification"), str) or not scope["justification"].strip():
            errors.append("surviving_scope kind none requires a justification")
    elif not surviving_items(document):
        errors.append(
            "surviving_scope must contain statements, questions, or one observation"
        )
    _existing_wiki_path(
        document.get("current_evidence_home"),
        "current_evidence_home",
        errors,
    )

    # Schema-v1 tombstones are historical baselines. They remain hash-checked
    # by check-comp-invalidation.py but cannot be used as templates for a new
    # retirement.
    if document.get("schema_version") != 2:
        return errors

    if document.get("decision_owner") != "brian":
        errors.append("schema-v2 retirement requires decision_owner brian")
    if not isinstance(document.get("decision_ref"), str) or not document["decision_ref"].strip():
        errors.append("schema-v2 retirement requires decision_ref")

    review = document.get("disposition_review")
    if not isinstance(review, dict):
        errors.append("schema-v2 retirement requires disposition_review")
    else:
        review_path_raw = review.get("path")
        if not isinstance(review_path_raw, str):
            errors.append("disposition_review.path is required")
        else:
            review_path = _repo_file(
                review_path_raw,
                "disposition_review.path",
                errors,
            )
            if review_path:
                if review.get("sha256") != sha256(review_path):
                    errors.append("disposition review SHA-256 mismatch")
                text = review_path.read_text(errors="replace")
                if "RETIREMENT_REVIEW: GO" not in text:
                    errors.append("disposition review must contain RETIREMENT_REVIEW: GO")
                if "UNIQUE_DETAIL_COVERAGE: complete" not in text:
                    errors.append(
                        "disposition review must contain UNIQUE_DETAIL_COVERAGE: complete"
                    )
                manifest_sha = document.get(
                    "reviewed_artifact_manifest_sha256"
                )
                if not isinstance(manifest_sha, str) or not re.fullmatch(
                    r"[0-9a-f]{64}",
                    manifest_sha,
                ):
                    errors.append(
                        "schema-v2 retirement requires "
                        "reviewed_artifact_manifest_sha256"
                    )
                elif (
                    f"ARTIFACT_MANIFEST_SHA256: {manifest_sha}"
                    not in text
                ):
                    errors.append(
                        "disposition review does not bind the retired artifact manifest"
                    )

    homes = document.get("surviving_scope_homes")
    items = surviving_items(document)
    if not isinstance(homes, list) or len(homes) != len(items):
        errors.append("surviving_scope_homes must map every surviving item exactly once")
    else:
        indexes: set[int] = set()
        for home in homes:
            if not isinstance(home, dict) or not isinstance(home.get("item_index"), int):
                errors.append("each surviving_scope_home requires item_index")
                continue
            indexes.add(home["item_index"])
            path = _existing_wiki_path(home.get("path"), "surviving_scope_home.path", errors)
            if path and not _heading_exists(path, home.get("heading")):
                errors.append(
                    f"surviving scope heading does not exist: {home.get('heading')!r}"
                )
        if indexes != set(range(len(items))):
            errors.append("surviving_scope_homes item indexes are incomplete or duplicated")

    detail_audit = document.get("unique_detail_audit")
    if not isinstance(detail_audit, list) or not detail_audit:
        errors.append("unique_detail_audit must disposition every unique detail class")
    else:
        for item in detail_audit:
            if not isinstance(item, dict):
                errors.append("unique_detail_audit entries must be objects")
                continue
            if item.get("disposition") not in ALLOWED_DETAIL_DISPOSITIONS:
                errors.append("unique_detail_audit disposition is invalid")
            if not isinstance(item.get("description"), str) or not item["description"].strip():
                errors.append("unique_detail_audit description is required")
            if not isinstance(item.get("source_paths"), list) or not item["source_paths"]:
                errors.append("unique_detail_audit source_paths are required")
            if not isinstance(item.get("rationale"), str) or not item["rationale"].strip():
                errors.append("unique_detail_audit rationale is required")
            if item.get("disposition") == "canonicalized":
                path = _existing_wiki_path(
                    item.get("canonical_path"),
                    "unique_detail_audit.canonical_path",
                    errors,
                )
                if path and not _heading_exists(path, item.get("canonical_heading")):
                    errors.append("canonicalized detail heading does not exist")

    cascade = document.get("cascade")
    if not isinstance(cascade, dict) or cascade.get("status") != "closed":
        errors.append("schema-v2 retirement requires a closed dependency cascade")
    elif not isinstance(cascade.get("paths"), list):
        errors.append("cascade.paths must be a list")
    return errors


def new_retirement_paths(base: str) -> list[Path]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--diff-filter=AM",
            "--name-only",
            base,
            "HEAD",
            "--",
            "wiki/etc/experiments/comp-*/invalidation.json",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [ROOT / raw for raw in result.stdout.splitlines() if raw]


def validate_retirement_batch(base: str) -> list[str]:
    paths = new_retirement_paths(base)
    open_cascades = sorted(
        (ROOT / "synthesis" / "queue").glob("comp-retirement-cascade-*.md")
    )
    return validate_retirement_batch_paths(paths, open_cascades)


def validate_retirement_batch_paths(
    paths: list[Path],
    open_cascades: list[Path],
) -> list[str]:
    errors: list[str] = []
    if len(paths) > 3:
        errors.append(
            f"retirement batch adds {len(paths)} tombstones; maximum is 3"
        )
    if paths and open_cascades:
        names = ", ".join(relative(path) for path in open_cascades)
        errors.append(f"new retirement blocked by open cascade items: {names}")
    for path in paths:
        try:
            document = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if document.get("schema_version") != 2:
            errors.append(
                f"{relative(path)}: every new retirement must use schema_version 2"
            )
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comp-dir", action="append", default=[])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--base", help="Git base for new-retirement batch checks")
    args = parser.parse_args()

    comp_dirs = [resolve_comp(raw) for raw in args.comp_dir]
    if args.all:
        comp_dirs.extend(
            path.parent
            for pattern in ("comp-*/quarantine.json", "comp-*/invalidation.json")
            for path in sorted(EXPERIMENTS.glob(pattern))
        )
    if not comp_dirs and not args.base:
        parser.error("provide --comp-dir, --all, or --base")

    failed = False
    for comp_dir in dict.fromkeys(comp_dirs):
        errors: list[str] = []
        if (comp_dir / "quarantine.json").is_file():
            errors.extend(validate_quarantine(comp_dir))
        if (comp_dir / "invalidation.json").is_file():
            errors.extend(validate_invalidation_governance(comp_dir))
        if errors:
            failed = True
            for error in errors:
                print(f"ERROR [{comp_dir.name}]: {error}")
        else:
            print(f"{comp_dir.name}: disposition state valid")
    if args.base:
        for error in validate_retirement_batch(args.base):
            failed = True
            print(f"ERROR [retirement-batch]: {error}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
