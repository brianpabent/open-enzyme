#!/usr/bin/env python3
"""Verify that comp-019 can only reproduce explicitly invalidated history."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMP_DIR = HERE.parent
MODEL = HERE / "flux_model.py"
RESULTS = COMP_DIR / "outputs" / "flux_model_results.json"
SUMMARY = COMP_DIR / "outputs" / "flux_model_summary.md"
PHASE_A = COMP_DIR / "outputs" / "phase_a_table.md"
PHASE_A_INPUT = COMP_DIR / "inputs" / "phase_a_literature.json"
OUTPUTS = (RESULTS, SUMMARY, PHASE_A)

EXPECTED_NUMERICAL_PAYLOAD_SHA256 = (
    "75fb1cf2c6314bf2a143979713a6afaf12686cf1314401bced29fa4a52e2d18f"
)
EXPECTED_INVALIDATION_REASON = (
    "The model omitted physiological luminal-urate occupancy and finite "
    "residence/exposure time. Its quantitative verdict is not decision-usable."
)
EXPECTED_SURVIVING_SCOPE = [
    "Phase A found no Q141K-stratified uricase clinical outcome in the sources searched for comp-019 as of 2026-05-08."
]
REQUIRED_DO_NOT_USE = {
    "serum-urate effect prediction",
    "dose selection",
    "ABCG2 genotype-response ranking",
    "flat-dose or substrate-limited classification",
    "yield-priority decisions",
    "trial-arm design",
}


def fail(message: str) -> None:
    raise SystemExit(f"RETIREMENT CONTRACT FAILED: {message}")


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output_hashes() -> dict[str, str]:
    return {path.name: file_sha256(path) for path in OUTPUTS}


def numerical_payload_sha256(document: dict) -> str:
    payload = dict(document)
    payload.pop("_metadata", None)
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def first_nonempty_line(path: Path) -> str:
    return next((line.strip() for line in path.read_text().splitlines() if line.strip()), "")


def check_saved_contract() -> None:
    document = json.loads(RESULTS.read_text())
    metadata = document.get("_metadata", {})
    if metadata.get("status") != "invalidated":
        fail("JSON status is not invalidated")
    if metadata.get("superseded_by") != "comp-044":
        fail("JSON does not identify comp-044 as the superseding experiment")
    if metadata.get("invalidation_reason") != EXPECTED_INVALIDATION_REASON:
        fail("JSON invalidation reason is missing or changed")
    if metadata.get("surviving_result_scope") != EXPECTED_SURVIVING_SCOPE:
        fail("JSON surviving scope is missing, changed, or broadened")
    if set(metadata.get("do_not_use_for", [])) != REQUIRED_DO_NOT_USE:
        fail("JSON do_not_use_for scope is incomplete or changed")
    if numerical_payload_sha256(document) != EXPECTED_NUMERICAL_PAYLOAD_SHA256:
        fail("historical numerical payload changed")

    if not first_nonempty_line(SUMMARY).startswith("> **INVALIDATED / SUPERSEDED"):
        fail("generated summary lacks a leading invalidation warning")
    summary_text = SUMMARY.read_text()
    if "## Retired historical interpretation — invalid; do not use" not in summary_text:
        fail("generated summary lacks a section-local retirement label")
    if "## Headline interpretation" in summary_text:
        fail("generated summary restored an active interpretation heading")
    if not first_nonempty_line(PHASE_A).startswith("> **PARTIALLY SURVIVES;"):
        fail("Phase A table lacks a leading scoped-survival warning")
    phase_a_metadata = json.loads(PHASE_A_INPUT.read_text()).get("_metadata", {})
    if phase_a_metadata.get("search_date") != "2026-05-08":
        fail("Phase A machine record lacks the frozen search date")
    if phase_a_metadata.get("surviving_result_scope") != EXPECTED_SURVIVING_SCOPE[0]:
        fail("Phase A machine record is missing or broadens the surviving scope")
    miyazaki_design = json.loads(PHASE_A_INPUT.read_text()).get("miyazaki_2025", {}).get(
        "design", ""
    )
    if "30 Crohn's disease, 2 simple ulcer, 2 obscure GI bleeding" not in miyazaki_design:
        fail("Phase A machine record does not match the primary-source cohort composition")
    if "32 Crohn's disease" in miyazaki_design:
        fail("Phase A machine record retains the corrected cohort-count error")


def main() -> None:
    before = output_hashes()
    refused = subprocess.run(
        [sys.executable, str(MODEL)],
        cwd=COMP_DIR,
        text=True,
        capture_output=True,
        check=False,
    )
    if refused.returncode == 0:
        fail("unflagged model execution was not refused")
    if "invalidated and superseded by comp-044" not in refused.stderr:
        fail("unflagged refusal did not explain the supersession")
    if output_hashes() != before:
        fail("unflagged refusal modified an output")

    repeated_hashes: list[dict[str, str]] = []
    for _ in range(2):
        reproduced = subprocess.run(
            [sys.executable, str(MODEL), "--reproduce-invalidated-history"],
            cwd=COMP_DIR,
            text=True,
            capture_output=True,
            check=False,
        )
        if reproduced.returncode != 0:
            fail(f"flagged historical reproduction failed: {reproduced.stderr.strip()}")
        first_stdout = next(
            (line.strip() for line in reproduced.stdout.splitlines() if line.strip()), ""
        )
        if not first_stdout.startswith("WARNING: INVALIDATED / SUPERSEDED"):
            fail("terminal output exposes numbers before the invalidation warning")
        check_saved_contract()
        repeated_hashes.append(output_hashes())

    if repeated_hashes[0] != repeated_hashes[1]:
        fail("repeated flagged runs were not byte-identical")

    print(f"RETIREMENT CONTRACT: PASS (Python {sys.version.split()[0]})")
    print(f"NUMERICAL PAYLOAD: {EXPECTED_NUMERICAL_PAYLOAD_SHA256}")


if __name__ == "__main__":
    main()
