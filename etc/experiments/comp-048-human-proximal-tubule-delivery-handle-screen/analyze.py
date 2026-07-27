#!/usr/bin/env python3
"""Deterministic COMP-048 human proximal-tubule surface-candidate screen.

The computation keeps expression, selectivity, topology, surface evidence,
protein localization, disease stability, internalization evidence, and
membrane polarity as separate axes. It never computes a composite score or
establishes receptor status, internalization, polarity, or delivery.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.metadata
import json
import math
import re
import shutil
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp
import xlrd


HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
RUNTIME_ENV = HERE / ".comp-runtime-env"
WORK_INPUTS = RUNTIME_ENV / "inputs"
OUTPUTS = HERE / "outputs"
STAGING = RUNTIME_ENV / "output-staging"
MANIFEST = json.loads((INPUTS / "source-manifest.json").read_text())
RULES = json.loads((INPUTS / "design-rules.json").read_text())

RUNTIME = RULES["runtime"]
SCHEMA = RULES["required_input_schema"]
LABELS = RULES["labels"]
CORRECTIONS = RULES["count_corrections"]
SUMMARY = RULES["summary_statistics"]
TARGET = str(LABELS["target_gene"])
PRIMARY_CONDITION = str(LABELS["primary_condition"])
DISEASE_CONDITIONS = [str(value) for value in LABELS["disease_conditions"]]
CONDITIONS = [PRIMARY_CONDITION, *DISEASE_CONDITIONS]
HASH_CHUNK_BYTES = int(RUNTIME["hash_chunk_bytes"])
CANDIDATE_BATCH_SIZE = int(RUNTIME["candidate_batch_size"])
DETECTION_THRESHOLD = float(
    RULES["expression_detection"]["detected_if_value_strictly_greater_than"]
)
MEDIAN_Q = float(SUMMARY["median_quantile"])
LOWER_QUARTILE_Q = float(SUMMARY["lower_quartile_quantile"])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(HASH_CHUNK_BYTES), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_by_id(identifier: str) -> dict[str, Any]:
    matches = [item for item in MANIFEST["sources"] if item["id"] == identifier]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one source named {identifier!r}, found {len(matches)}")
    return matches[0]


def clear_output_state() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    if bool(RULES["failure_output_contract"]["clear_stale_outputs_before_preflight"]):
        OUTPUTS.mkdir(exist_ok=True)
        for existing in OUTPUTS.iterdir():
            if existing.name == ".gitkeep":
                continue
            if existing.is_dir():
                shutil.rmtree(existing)
            else:
                existing.unlink()


def locked_packages() -> dict[str, str]:
    locked: dict[str, str] = {}
    for raw in (HERE / "requirements.lock.txt").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "==" not in line:
            raise RuntimeError(f"Unpinned dependency in requirements.lock.txt: {line}")
        name, version = line.split("==", 1)
        if not name or not version or name in locked:
            raise RuntimeError(f"Invalid dependency pin: {line}")
        locked[name] = version
    return locked


def verify_runtime() -> tuple[dict[str, str], list[str]]:
    installed: dict[str, str] = {}
    failures: list[str] = []
    actual_python = sys.version.split()[0]
    if actual_python != str(RUNTIME["python_exact"]):
        failures.append(
            f"Python {actual_python} does not match frozen {RUNTIME['python_exact']}"
        )
    for name, expected in sorted(locked_packages().items()):
        try:
            actual = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"Missing locked dependency: {name}=={expected}")
            continue
        installed[name] = actual
        if actual != expected:
            failures.append(
                f"Dependency {name}=={actual} does not match frozen {expected}"
            )
    return installed, failures


def verify_inputs() -> list[dict[str, Any]]:
    receipt: list[dict[str, Any]] = []
    for source in MANIFEST["sources"]:
        path = WORK_INPUTS / str(source["local_name"])
        if not path.is_file():
            raise RuntimeError(f"Missing frozen input: {path.name}; run fetch_inputs.py")
        actual = {"bytes": path.stat().st_size, "sha256": sha256(path)}
        if actual["bytes"] != source["bytes"] or actual["sha256"] != source["sha256"]:
            raise RuntimeError(f"Frozen input mismatch: {path.name}: {actual}")
        receipt.append({"id": source["id"], **actual})
    return receipt


def read_zip_tsv(identifier: str, configured_columns: list[str]) -> pd.DataFrame:
    source = source_by_id(identifier)
    source_columns = [str(value) for value in source["required_header"]]
    if source_columns != configured_columns:
        raise RuntimeError(
            f"{identifier}: source-manifest and design-rules headers disagree"
        )
    path = WORK_INPUTS / str(source["local_name"])
    with zipfile.ZipFile(path) as archive:
        member = str(source["archive_member"])
        if member not in archive.namelist():
            raise RuntimeError(f"{path.name} lacks {member}")
        with archive.open(member) as handle:
            frame = pd.read_csv(handle, sep="\t", low_memory=False)
    missing = [column for column in configured_columns if column not in frame.columns]
    if missing:
        raise RuntimeError(f"{identifier}: missing columns {missing}")
    primary_key = [str(value) for value in source["primary_key"]]
    if frame.duplicated(subset=primary_key, keep=False).any():
        examples = (
            frame.loc[frame.duplicated(subset=primary_key, keep=False), primary_key]
            .head()
            .to_dict(orient="records")
        )
        raise RuntimeError(f"{identifier}: duplicate primary-key rows: {examples}")
    return frame


def require_categories(
    frame: pd.DataFrame, column: str, required: Iterable[str], label: str
) -> None:
    present = set(frame[column].dropna().astype(str))
    missing = sorted(set(required) - present)
    if missing:
        raise RuntimeError(f"{label}: required categories absent: {missing}")


def topology_noncytoplasmic_residues(value: object) -> int:
    prefix = str(RULES["surface_evidence"]["topology_noncytoplasmic_prefix"])
    total = 0
    for raw_segment in str(value or "").split(";"):
        segment = raw_segment.strip()
        if not segment.startswith(prefix):
            continue
        try:
            start, end = segment[len(prefix) :].split("-", 1)
            total += int(end) - int(start) + 1
        except (ValueError, TypeError):
            raise RuntimeError(f"Unparseable noncytoplasmic topology: {value!r}")
    return total


def surface_evidence(row: dict[str, Any]) -> tuple[str, int]:
    cspa = str(row.get("CSPA category", "") or "").strip()
    label_source = str(row.get("Surfaceome Label Source", "") or "").strip().lower()
    for rule in RULES["surface_evidence"]["classes"]:
        matcher = str(rule["matcher"])
        matched = False
        if matcher == "cspa_prefix":
            matched = cspa.startswith(str(rule["value"]))
        elif matcher == "cspa_nonempty":
            matched = bool(cspa)
        elif matcher == "label_source_contains_any":
            matched = any(
                str(value).lower() in label_source for value in rule["values"]
            )
        elif matcher == "fallback":
            matched = True
        else:
            raise RuntimeError(f"Unknown surface-evidence matcher: {matcher}")
        if matched:
            return str(rule["name"]), int(rule["ordinal"])
    raise RuntimeError("Surface-evidence rules have no matching fallback")


def read_surfaceome() -> list[dict[str, Any]]:
    source = source_by_id("bausch_fluck_surfaceome")
    book = xlrd.open_workbook(
        str(WORK_INPUTS / str(source["local_name"])), on_demand=True
    )
    sheet = book.sheet_by_name(str(source["sheet"]))
    header_row = int(SCHEMA["surfaceome_header_row"])
    headers = [str(value).strip() for value in sheet.row_values(header_row)]
    required = [str(value) for value in SCHEMA["surfaceome_required_columns"]]
    missing = [column for column in required if column not in headers]
    if missing:
        raise RuntimeError(f"Surfaceome is missing required columns: {missing}")
    rows: list[dict[str, Any]] = []
    required_label = str(LABELS["required_surfaceome_label"]).lower()
    for index in range(header_row + 1, sheet.nrows):
        row = dict(zip(headers, sheet.row_values(index), strict=True))
        if str(row.get("Surfaceome Label", "")).strip().lower() != required_label:
            continue
        gene = str(row.get("UniProt gene", "")).strip()
        if not gene:
            continue
        evidence_class, evidence_ordinal = surface_evidence(row)
        rows.append(
            {
                "gene": gene,
                "ensembl_gene": str(row.get("Ensembl gene", "")).strip(),
                "uniprot": str(row.get("UniProt accession", "")).strip(),
                "description": str(row.get("UniProt description", "")).strip(),
                "surface_label_source": str(
                    row.get("Surfaceome Label Source", "")
                ).strip(),
                "surface_evidence_class": evidence_class,
                "surface_evidence_ordinal": evidence_ordinal,
                "direct_surface_evidence": evidence_class
                in set(RULES["surface_evidence"]["direct_classes"]),
                "cspa_category": str(row.get("CSPA category", "")).strip(),
                "topology": str(row.get("topology", "")).strip(),
                "topology_source": str(row.get("topology source", "")).strip(),
                "noncytoplasmic_residue_count": topology_noncytoplasmic_residues(
                    row.get("topology", "")
                ),
                "uniprot_subcellular": str(
                    row.get("UniProt subcellular", "")
                ).strip(),
                "uniprot_keywords": str(row.get("UniProt keywords", "")).strip(),
            }
        )
    counts = pd.Series([row["gene"] for row in rows]).value_counts()
    duplicate_genes = sorted(str(gene) for gene, count in counts.items() if count > 1)
    if duplicate_genes:
        raise RuntimeError(
            "Surfaceome has duplicate gene symbols; explicit resolution required: "
            + ", ".join(duplicate_genes[:20])
        )
    return sorted(rows, key=lambda row: row["gene"])


def read_controls() -> dict[str, dict[str, str]]:
    with (INPUTS / "controls.tsv").open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {
        "gene",
        "role",
        "expected_observation",
        "interpretation",
        "direct_internalization_evidence",
        "evidence_id",
        "evidence_scope",
    }
    if not rows or set(rows[0]) != required:
        raise RuntimeError("controls.tsv schema mismatch")
    genes = [row["gene"] for row in rows]
    if len(genes) != len(set(genes)):
        raise RuntimeError("controls.tsv contains duplicate genes")
    positive = sorted(
        row["gene"] for row in rows if row["role"] == "positive_pattern"
    )
    negative = sorted(
        row["gene"] for row in rows if row["role"] == "negative_surface"
    )
    if positive != sorted(RULES["method_controls"]["positive_pattern_genes"]):
        raise RuntimeError("Positive-pattern controls disagree with design-rules.json")
    if negative != sorted(RULES["method_controls"]["negative_surface_genes"]):
        raise RuntimeError("Negative-surface controls disagree with design-rules.json")
    for row in rows:
        if row["direct_internalization_evidence"] not in {"true", "false"}:
            raise RuntimeError(
                f"{row['gene']}: direct_internalization_evidence must be true/false"
            )
        if (
            row["direct_internalization_evidence"] == "true"
            and row["evidence_id"] in {"", "NA"}
        ):
            raise RuntimeError(f"{row['gene']}: direct evidence lacks a source ID")
    return {row["gene"]: row for row in rows}


def hpa_value_map(
    frame: pd.DataFrame, category_column: str, value_column: str
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = defaultdict(dict)
    for gene_id, category, value in frame[
        ["Gene", category_column, value_column]
    ].itertuples(index=False, name=None):
        numeric = float(value)
        if not math.isfinite(numeric) or numeric < DETECTION_THRESHOLD:
            raise RuntimeError(
                f"HPA {value_column} contains an invalid value for "
                f"{gene_id}/{category}: {value!r}"
            )
        output[str(gene_id)][str(category)] = numeric
    return output


def hpa_ids_by_symbol(frame: pd.DataFrame) -> dict[str, list[str]]:
    result: dict[str, set[str]] = defaultdict(set)
    for gene_id, symbol in frame[["Gene", "Gene name"]].itertuples(
        index=False, name=None
    ):
        result[str(symbol)].add(str(gene_id))
    return {symbol: sorted(ids) for symbol, ids in result.items()}


def values_for_ids(
    values: dict[str, dict[str, float]], gene_ids: Iterable[str]
) -> dict[str, float]:
    if (
        RULES["expression_detection"]["multi_ensembl_hpa_policy"]
        != "maximum value across the same mapped Ensembl IDs within each HPA category"
    ):
        raise RuntimeError("Unsupported HPA multi-Ensembl aggregation policy")
    aggregated: dict[str, float] = {}
    for gene_id in gene_ids:
        for category, value in values.get(gene_id, {}).items():
            aggregated[category] = max(value, aggregated.get(category, value))
    return aggregated


def ratio_to_next(
    values: dict[str, float], target: str, pseudocount: float
) -> tuple[float | None, float | None, str | None, str]:
    if not values:
        return None, None, None, "no_hpa_data"
    if target not in values:
        return None, None, None, "required_target_category_absent"
    other = [(name, value) for name, value in values.items() if name != target]
    if not other:
        return None, None, None, "non_target_comparison_category_absent"
    next_name, next_value = max(other, key=lambda item: (item[1], item[0]))
    return (
        (values[target] + pseudocount) / (next_value + pseudocount),
        next_value,
        next_name,
        "ok",
    )


def dense_detection(matrix: Any) -> np.ndarray:
    values = matrix.toarray() if sp.issparse(matrix) else np.asarray(matrix)
    return values > DETECTION_THRESHOLD


def quantile(values: Iterable[float], q: float) -> float | None:
    sequence = list(values)
    return (
        float(np.quantile(sequence, q, method=str(SUMMARY["quantile_method"])))
        if sequence
        else None
    )


def corrected_ratio(
    positive_hits: int, positive_total: int, background_hits: int, background_total: int
) -> float:
    hit_pc = float(CORRECTIONS["binomial_hits_pseudocount"])
    total_pc = float(CORRECTIONS["binomial_total_pseudocount"])
    positive = (positive_hits + hit_pc) / (positive_total + total_pc)
    background = (background_hits + hit_pc) / (background_total + total_pc)
    return positive / background


def explicit_ensembl_ids(value: object) -> list[str]:
    return sorted(
        set(
            item
            for item in re.split(r"[;,|\s]+", str(value or "").strip())
            if item
        )
    )


def resolve_ensembl(
    surface: list[dict[str, Any]], adata: ad.AnnData
) -> tuple[dict[str, list[str]], dict[str, str]]:
    if (
        RULES["expression_detection"]["gene_mapping_policy"]
        != "when a row supplies explicit surfaceome Ensembl IDs, require every supplied ID to be present in KPMP and use all of them; use all exact feature_name symbol matches only when that row supplies no explicit ID; never use a partial explicit-ID set or symbol fallback after an explicit-ID failure"
    ):
        raise RuntimeError("Unsupported gene-mapping policy")
    var = adata.var.copy()
    var["ensembl"] = adata.var_names.astype(str)
    by_symbol: dict[str, list[str]] = defaultdict(list)
    for symbol, ensembl in zip(
        var["feature_name"].astype(str), var["ensembl"], strict=True
    ):
        by_symbol[symbol].append(ensembl)
    available = set(var["ensembl"])
    mapping: dict[str, list[str]] = {}
    failures: dict[str, str] = {}
    rows = list(surface)
    if TARGET not in {str(row["gene"]) for row in surface}:
        rows.append({"gene": TARGET, "ensembl_gene": ""})
    for row in rows:
        gene = str(row["gene"])
        explicit = explicit_ensembl_ids(row.get("ensembl_gene", ""))
        if explicit:
            missing = sorted(set(explicit) - available)
            if missing:
                failures[gene] = f"explicit Ensembl IDs absent from kidney input: {missing}"
            else:
                mapping[gene] = explicit
            continue
        matches = sorted(set(by_symbol.get(gene, [])))
        if matches:
            mapping[gene] = matches
        else:
            failures[gene] = "absent from kidney expression input"
    if set(mapping) & set(failures):
        raise RuntimeError("Gene mapping and failure states are not disjoint")
    surface_genes = {str(row["gene"]) for row in surface}
    expected = surface_genes | {TARGET}
    classified = set(mapping) | set(failures)
    if classified != expected:
        raise RuntimeError(
            "Gene mapping did not classify every surfaceome candidate and target "
            f"exactly once: missing={sorted(expected - classified)}, "
            f"unexpected={sorted(classified - expected)}"
        )
    unresolved_surface = surface_genes - set(mapping)
    if unresolved_surface != (set(failures) & surface_genes):
        raise RuntimeError(
            "Every unresolved surfaceome candidate must have exactly one "
            "recorded mapping-failure reason"
        )
    return mapping, failures


def candidate_detection(
    adata: ad.AnnData,
    batch: list[dict[str, Any]],
    mapping: dict[str, list[str]],
) -> dict[str, np.ndarray]:
    ordered_ids = sorted(
        set(gene_id for row in batch for gene_id in mapping[row["gene"]])
    )
    matrix = dense_detection(adata[:, ordered_ids].X)
    index = {gene_id: column for column, gene_id in enumerate(ordered_ids)}
    result: dict[str, np.ndarray] = {}
    for row in batch:
        columns = [index[gene_id] for gene_id in mapping[row["gene"]]]
        result[row["gene"]] = np.any(matrix[:, columns], axis=1)
    return result


def proximal_tubule_assignment(obs: pd.DataFrame) -> tuple[np.ndarray, dict[str, Any]]:
    cell_series = obs["cell_type"]
    cell_text = cell_series.fillna("").astype(str).str.strip()
    missing_tokens = {
        str(value).strip().lower() for value in LABELS["cell_type_missing_tokens"]
    }
    cell_missing = cell_series.isna().to_numpy() | cell_text.str.lower().isin(
        missing_tokens
    ).to_numpy()
    exact = (
        cell_text.to_numpy() == str(LABELS["exact_pt_cell_type"])
    )
    subclass = (
        obs["subclass.l1"].fillna("").astype(str).str.strip().to_numpy()
        == str(LABELS["pt_subclass"])
    )
    pt = exact | (cell_missing & subclass)
    conflicts = (~cell_missing) & (~exact) & subclass
    denominator = int(np.sum(subclass))
    fraction = float(np.sum(conflicts) / denominator) if denominator else 0.0
    return pt, {
        "policy": RULES["pt_assignment"]["policy"],
        "exact_count": int(np.sum(exact)),
        "fallback_count": int(np.sum(cell_missing & subclass)),
        "conflict_count": int(np.sum(conflicts)),
        "subclass_pt_count": denominator,
        "conflict_fraction": fraction,
    }


def eligible_donors(
    obs_donor: np.ndarray,
    obs_condition: np.ndarray,
    pt: np.ndarray,
    target_positive: np.ndarray,
    target_negative: np.ndarray,
    condition: str,
) -> tuple[list[str], dict[str, dict[str, int | bool]]]:
    rules = RULES["eligible_donor_rules"]
    result: list[str] = []
    diagnostics: dict[str, dict[str, int | bool]] = {}
    for donor in sorted(set(obs_donor[obs_condition == condition])):
        donor_mask = (obs_donor == donor) & (obs_condition == condition)
        pt_count = int(np.sum(donor_mask & pt))
        positive_count = int(np.sum(donor_mask & target_positive))
        negative_count = int(np.sum(donor_mask & target_negative))
        eligible = (
            pt_count >= int(rules["minimum_proximal_tubule_cells"])
            and positive_count >= int(rules["minimum_slc22a12_positive_cells"])
        )
        diagnostics[str(donor)] = {
            "proximal_tubule_cells": pt_count,
            "slc22a12_positive_cells": positive_count,
            "slc22a12_negative_pt_cells": negative_count,
            "eligible": eligible,
            "target_negative_diagnostic_eligible": negative_count
            >= int(rules["minimum_slc22a12_negative_pt_cells_for_diagnostic"]),
        }
        if eligible:
            result.append(str(donor))
    return result, diagnostics


def pass_thresholds(row: dict[str, Any], thresholds: dict[str, float]) -> bool:
    required = {
        "median_reference_donor_target_coverage": (
            ">=",
            thresholds["coverage_median"],
        ),
        "q25_reference_donor_target_coverage": (
            ">=",
            thresholds["coverage_q25"],
        ),
        "median_target_to_non_pt_detection_ratio": (
            ">=",
            thresholds["target_to_non_pt_ratio"],
        ),
        "median_reference_donor_non_pt_detection_fraction": (
            "<=",
            thresholds["non_pt_median_max"],
        ),
        "maximum_reference_non_pt_cell_type_detection_fraction": (
            "<=",
            thresholds["non_pt_cell_type_max"],
        ),
        "hpa_proximal_tubule_to_next_cell_type_ratio": (
            ">=",
            thresholds["hpa_cell_type_ratio"],
        ),
        "hpa_kidney_to_next_tissue_ratio": (
            ">=",
            thresholds["hpa_tissue_ratio"],
        ),
    }
    if row["noncytoplasmic_residue_count"] < int(
        RULES["surface_evidence"]["minimum_noncytoplasmic_residues"]
    ):
        return False
    for field, (operator, boundary) in required.items():
        value = row.get(field)
        if value is None:
            return False
        if operator == ">=" and value < boundary:
            return False
        if operator == "<=" and value > boundary:
            return False
    return True


def pareto_front(rows: list[dict[str, Any]]) -> set[str]:
    maximize = RULES["pareto_axes"]["maximize"]
    minimize = RULES["pareto_axes"]["minimize"]
    result: set[str] = set()
    for candidate in rows:
        dominated = False
        for challenger in rows:
            if challenger is candidate:
                continue
            no_worse = all(
                challenger[key] >= candidate[key] for key in maximize
            ) and all(challenger[key] <= candidate[key] for key in minimize)
            strictly_better = any(
                challenger[key] > candidate[key] for key in maximize
            ) or any(challenger[key] < candidate[key] for key in minimize)
            if no_worse and strictly_better:
                dominated = True
                break
        if not dominated:
            result.add(str(candidate["gene"]))
    return result


def group_metrics(
    detected: np.ndarray,
    mask: np.ndarray,
    target_positive: np.ndarray,
    target_negative: np.ndarray,
    pt: np.ndarray,
) -> dict[str, Any]:
    positive_mask = mask & target_positive
    negative_mask = mask & target_negative
    non_pt_mask = mask & ~pt
    positive_hits = int(np.sum(detected[positive_mask]))
    positive_total = int(np.sum(positive_mask))
    negative_hits = int(np.sum(detected[negative_mask]))
    negative_total = int(np.sum(negative_mask))
    non_pt_hits = int(np.sum(detected[non_pt_mask]))
    non_pt_total = int(np.sum(non_pt_mask))
    minimum_negative = int(
        RULES["eligible_donor_rules"][
            "minimum_slc22a12_negative_pt_cells_for_diagnostic"
        ]
    )
    return {
        "target_positive_cells": positive_total,
        "candidate_positive_target_cells": positive_hits,
        "target_coverage": positive_hits / positive_total
        if positive_total
        else None,
        "target_negative_pt_cells": negative_total,
        "candidate_positive_target_negative_pt_cells": negative_hits,
        "target_negative_pt_detection_fraction": negative_hits / negative_total
        if negative_total
        else None,
        "target_positive_to_target_negative_pt_detection_ratio": corrected_ratio(
            positive_hits, positive_total, negative_hits, negative_total
        )
        if positive_total and negative_total >= minimum_negative
        else None,
        "target_negative_diagnostic_eligible": negative_total >= minimum_negative,
        "non_pt_cells": non_pt_total,
        "candidate_positive_non_pt_cells": non_pt_hits,
        "non_pt_detection_fraction": non_pt_hits / non_pt_total
        if non_pt_total
        else None,
        "corrected_target_to_non_pt_detection_ratio": corrected_ratio(
            positive_hits, positive_total, non_pt_hits, non_pt_total
        )
        if positive_total and non_pt_total
        else None,
    }


def disease_stability(
    per_condition_coverages: dict[str, list[float]],
    eligible: dict[str, list[str]],
    reference_median: float | None,
) -> dict[str, dict[str, Any]]:
    config = RULES["disease_stability_axis"]
    pseudocount = float(CORRECTIONS["disease_coverage_ratio_pseudocount"])
    result: dict[str, dict[str, Any]] = {}
    for condition in DISEASE_CONDITIONS:
        condition_median = quantile(per_condition_coverages[condition], MEDIAN_Q)
        ratio = (
            (condition_median + pseudocount) / (reference_median + pseudocount)
            if condition_median is not None and reference_median is not None
            else None
        )
        if (
            len(eligible[condition])
            < int(config["minimum_eligible_donors_per_condition"])
            or ratio is None
        ):
            state = "insufficient"
        elif ratio >= float(
            config["stable_if_condition_to_reference_median_coverage_ratio_at_least"]
        ):
            state = "stable"
        else:
            state = "unstable"
        if state not in config["states"]:
            raise RuntimeError(f"Undeclared disease-stability state: {state}")
        result[condition] = {
            "state": state,
            "eligible_donors": len(eligible[condition]),
            "median_target_coverage": condition_median,
            "condition_to_reference_ratio": ratio,
        }
    return result


def write_csv(path: Path, rows: list[dict[str, Any]], sort_key: Any) -> None:
    if not rows:
        path.write_text("")
        return
    fields = sorted({key for row in rows for key in row})
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=sort_key))


def publish_staging() -> None:
    OUTPUTS.mkdir(exist_ok=True)
    for existing in OUTPUTS.iterdir():
        if existing.name == ".gitkeep":
            continue
        if existing.is_dir():
            shutil.rmtree(existing)
        else:
            existing.unlink()
    for generated in sorted(STAGING.iterdir()):
        generated.replace(OUTPUTS / generated.name)
    STAGING.rmdir()


def run_manifest(
    input_receipt: list[dict[str, Any]],
    packages: dict[str, str],
    status: str,
    failure: dict[str, str] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "status": status,
        "inputs": input_receipt,
        "packages": packages,
        "python": sys.version.split()[0],
        "design_rules_sha256": sha256(INPUTS / "design-rules.json"),
        "source_manifest_sha256": sha256(INPUTS / "source-manifest.json"),
        "randomness": "none",
        "composite_score": "prohibited",
        "failure": failure,
    }


def write_completed_audit_outputs(
    candidates: list[dict[str, Any]],
    donor_rows: list[dict[str, Any]],
    stratum_rows: list[dict[str, Any]],
    controls: dict[str, Any],
    missingness: dict[str, Any],
    result: dict[str, Any],
    input_receipt: list[dict[str, Any]],
    packages: dict[str, str],
) -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    write_csv(
        STAGING / "candidates.csv",
        candidates,
        lambda row: str(row["gene"]),
    )
    write_csv(
        STAGING / "donor-metrics.csv",
        donor_rows,
        lambda row: (
            str(row["gene"]),
            str(row["condition"]),
            str(row["donor_id"]),
        ),
    )
    write_csv(
        STAGING / "stratum-metrics.csv",
        stratum_rows,
        lambda row: (
            str(row["gene"]),
            str(row["condition"]),
            str(row["donor_id"]),
            str(row["assay"]),
            str(row["specimen"]),
        ),
    )
    run_status = (
        "METHOD_FAILURE_COMPLETED_AUDIT"
        if result["verdict"] == "METHOD_FAILURE"
        else "COMPLETE"
    )
    if (
        result["verdict"] == "METHOD_FAILURE"
        and run_status
        != RULES["failure_output_contract"]["completed_audit"][
            "method_failure_status"
        ]
    ):
        raise RuntimeError("Completed-audit method-failure status mismatch")
    run_failure = (
        {
            "type": "CompletedAuditMethodFailure",
            "message": "; ".join(result["method_failures"]),
        }
        if result["verdict"] == "METHOD_FAILURE"
        else None
    )
    for name, payload in [
        ("controls.json", controls),
        ("missingness.json", missingness),
        ("results.json", result),
        (
            "run-manifest.json",
            run_manifest(input_receipt, packages, run_status, run_failure),
        ),
    ]:
        (STAGING / name).write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n"
        )
    lines = [
        "# COMP-048 result",
        "",
        f"**Verdict:** `{result['verdict']}`",
        "",
        "## Sensitivity sets",
        "",
    ]
    for name in sorted(result["sensitivity_sets"]):
        record = result["sensitivity_sets"][name]
        lines.append(
            f"- **{name}:** {record['gate_candidate_count']} gate candidates; "
            f"Pareto set: {record['pareto_genes'] or 'none'}."
        )
    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            result["interpretation"],
            "",
            "Expression and surface/topology evidence nominate follow-up "
            "candidates only. This run does not establish receptor status, "
            "ligand binding, internalization, membrane polarity, blood or "
            "urinary access, endosomal escape, siRNA delivery, SLC22A12 "
            "knockdown, urate transport change, safety, dose, or efficacy.",
            "",
        ]
    )
    (STAGING / "summary.md").write_text("\n".join(lines))
    expected = set(
        RULES["failure_output_contract"]["completed_audit"]["required_files"]
    )
    actual = {path.name for path in STAGING.iterdir()}
    if actual != expected:
        raise RuntimeError(
            f"Completed-audit output contract mismatch: expected "
            f"{sorted(expected)}, wrote {sorted(actual)}"
        )
    publish_staging()


def write_failure_outputs(
    exc: Exception,
    input_receipt: list[dict[str, Any]],
    packages: dict[str, str],
) -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    failure = {"type": type(exc).__name__, "message": str(exc)}
    result = {
        "schema_version": 1,
        "verdict": "METHOD_FAILURE",
        "interpretation": (
            "Preflight failed. No biological absence, candidate-selection, or "
            "delivery conclusion is permitted."
        ),
        "method_failures": [str(exc)],
        "technical_failures": [],
        "primary_gate_candidate_count": 0,
        "primary_gate_genes": [],
        "sensitivity_sets": {},
        "nonclaims": ["all biological and engineering conclusions"],
    }
    payloads = {
        "results.json": result,
        "controls.json": {"status": "METHOD_FAILURE", "genes": {}},
        "missingness.json": {
            "status": "METHOD_FAILURE",
            "failure_before_complete_missingness_audit": True,
        },
        "run-manifest.json": run_manifest(
            input_receipt, packages, "METHOD_FAILURE", failure
        ),
    }
    for name, payload in payloads.items():
        (STAGING / name).write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n"
        )
    (STAGING / "summary.md").write_text(
        "# COMP-048 result\n\n"
        "**Verdict:** `METHOD_FAILURE`\n\n"
        "Preflight failed. No biological absence, candidate-selection, or "
        "delivery conclusion is permitted.\n"
    )
    expected = set(
        RULES["failure_output_contract"]["preflight_exception"][
            "required_files"
        ]
    )
    actual = {path.name for path in STAGING.iterdir()}
    if actual != expected:
        raise RuntimeError(
            f"Failure-output contract mismatch: expected {sorted(expected)}, "
            f"wrote {sorted(actual)}"
        )
    if not bool(RULES["failure_output_contract"]["no_biological_interpretation"]):
        raise RuntimeError("Failure-output contract permits biological interpretation")
    publish_staging()


def run_analysis(
    input_receipt: list[dict[str, Any]],
    packages: dict[str, str],
    runtime_failures: list[str],
) -> tuple[str, int]:
    completeness = RULES["technical_completeness"]
    for policy_name in [
        "duplicate_hpa_gene_category_rows",
        "duplicate_surfaceome_gene_rows",
        "duplicate_kpmp_observation_ids",
        "duplicate_kpmp_feature_ids",
        "missing_donor_ids",
    ]:
        if completeness[policy_name] != "METHOD_FAILURE":
            raise RuntimeError(
                f"Unsupported technical-completeness policy: {policy_name}"
            )
    for policy_name in [
        "hpa_ratio_requires_any_data",
        "hpa_ratio_requires_target_category",
        "hpa_ratio_requires_non_target_comparison_category",
    ]:
        if bool(completeness[policy_name]) is not True:
            raise RuntimeError(
                f"HPA ratio completeness policy must be enabled: {policy_name}"
            )
    if (
        RULES["expression_detection"]["candidate_csv_row_policy"]
        != "one row per frozen surfaceome candidate; unresolved candidates retain mapping status and failure reason with all computed axes blank and all gates false"
    ):
        raise RuntimeError("Unsupported candidate-CSV row policy")
    surface = read_surfaceome()
    surface_by_gene = {row["gene"]: row for row in surface}
    controls_table = read_controls()

    hpa_cell = read_zip_tsv(
        "hpa_single_cell_type",
        [str(value) for value in SCHEMA["hpa_cell_columns"]],
    )
    hpa_tissue = read_zip_tsv(
        "hpa_tissue_consensus",
        [str(value) for value in SCHEMA["hpa_tissue_columns"]],
    )
    hpa_ihc = read_zip_tsv(
        "hpa_normal_ihc",
        [str(value) for value in SCHEMA["hpa_ihc_columns"]],
    )
    require_categories(
        hpa_cell,
        "Cell type",
        [
            str(LABELS["hpa_proximal_tubule_cell_type"]),
            str(LABELS["hpa_hepatocyte_cell_type"]),
        ],
        "HPA cell-type RNA",
    )
    require_categories(
        hpa_tissue,
        "Tissue",
        [str(LABELS["hpa_kidney_tissue"]), str(LABELS["hpa_liver_tissue"])],
        "HPA tissue RNA",
    )
    require_categories(
        hpa_ihc,
        "Tissue",
        [str(LABELS["hpa_ihc_kidney_tissue"])],
        "HPA normal IHC",
    )
    cell_values_by_id = hpa_value_map(hpa_cell, "Cell type", "nCPM")
    tissue_values_by_id = hpa_value_map(hpa_tissue, "Tissue", "nTPM")
    hpa_cell_ids_by_symbol = hpa_ids_by_symbol(hpa_cell)
    hpa_tissue_ids_by_symbol = hpa_ids_by_symbol(hpa_tissue)

    kpmp = source_by_id("kpmp_cellxgene_integrated_human_kidney")
    adata = ad.read_h5ad(WORK_INPUTS / str(kpmp["local_name"]), backed="r")
    try:
        method_failures = list(runtime_failures)
        if list(adata.shape) != [int(value) for value in SCHEMA["kpmp_shape"]]:
            method_failures.append(
                f"KPMP shape {list(adata.shape)} differs from {SCHEMA['kpmp_shape']}"
            )
        actual_schema = str(adata.uns.get("schema_version", ""))
        if actual_schema != str(SCHEMA["kpmp_schema_version"]):
            method_failures.append(
                f"KPMP schema version {actual_schema!r} differs from "
                f"{SCHEMA['kpmp_schema_version']!r}"
            )
        missing_obs = [
            column
            for column in SCHEMA["kpmp_obs_columns"]
            if column not in adata.obs.columns
        ]
        missing_var = [
            column
            for column in SCHEMA["kpmp_var_columns"]
            if column not in adata.var.columns
        ]
        if missing_obs or missing_var:
            raise RuntimeError(
                f"KPMP schema columns missing: obs={missing_obs}, var={missing_var}"
            )
        if adata.obs_names.duplicated().any():
            raise RuntimeError("KPMP contains duplicate observation IDs")
        if adata.var_names.duplicated().any():
            raise RuntimeError("KPMP contains duplicate feature IDs")
        obs = adata.obs.copy()
        if obs["donor_id"].isna().any() or (
            obs["donor_id"].astype(str).str.strip() == ""
        ).any():
            raise RuntimeError("KPMP contains missing donor IDs")
        present_conditions = set(obs["condition.l1"].astype(str))
        missing_conditions = sorted(set(SCHEMA["kpmp_required_conditions"]) - present_conditions)
        if missing_conditions:
            raise RuntimeError(f"KPMP conditions absent: {missing_conditions}")

        pt, pt_assignment = proximal_tubule_assignment(obs)
        if (
            pt_assignment["conflict_fraction"]
            > float(
                RULES["pt_assignment"][
                    "maximum_conflict_fraction_before_method_failure"
                ]
            )
        ):
            method_failures.append(
                "PT exact/fallback label-conflict fraction exceeds the frozen limit"
            )

        mapping, mapping_failures = resolve_ensembl(surface, adata)
        if TARGET not in mapping:
            raise RuntimeError(
                f"{TARGET} cannot be mapped: {mapping_failures.get(TARGET)}"
            )
        target_detection = candidate_detection(
            adata, [{"gene": TARGET}], mapping
        )[TARGET]
        target_positive = pt & target_detection
        target_negative = pt & ~target_detection

        obs_donor = obs["donor_id"].astype(str).to_numpy()
        obs_condition = obs["condition.l1"].astype(str).to_numpy()
        obs_cell_type = obs["cell_type"].fillna("").astype(str).to_numpy()
        eligible: dict[str, list[str]] = {}
        donor_eligibility: dict[str, dict[str, dict[str, int | bool]]] = {}
        for condition in CONDITIONS:
            eligible[condition], donor_eligibility[condition] = eligible_donors(
                obs_donor,
                obs_condition,
                pt,
                target_positive,
                target_negative,
                condition,
            )

        min_reference = int(
            RULES["eligible_donor_rules"]["minimum_eligible_reference_donors"]
        )
        if len(eligible[PRIMARY_CONDITION]) < min_reference:
            method_failures.append(
                f"Only {len(eligible[PRIMARY_CONDITION])} eligible reference "
                f"donors; require {min_reference}"
            )
        reference_target_detection: list[float] = []
        for donor in eligible[PRIMARY_CONDITION]:
            donor_pt = (
                (obs_donor == donor)
                & (obs_condition == PRIMARY_CONDITION)
                & pt
            )
            reference_target_detection.append(
                float(np.mean(target_detection[donor_pt]))
            )
        if (
            reference_target_detection
            and float(np.median(reference_target_detection))
            < float(
                RULES["method_controls"][
                    "slc22a12_min_reference_donor_detection_fraction"
                ]
            )
        ):
            method_failures.append(
                "SLC22A12 reference-donor detection control failed"
            )

        resolvable = [row for row in surface if row["gene"] in mapping]
        mapping_fraction = len(resolvable) / len(surface) if surface else 0.0
        hpa_pt_label = str(LABELS["hpa_proximal_tubule_cell_type"])
        hpa_kidney_label = str(LABELS["hpa_kidney_tissue"])
        hpa_pc = float(CORRECTIONS["hpa_ratio_pseudocount"])
        hpa_axis_audit: dict[str, dict[str, dict[str, Any]]] = {}
        for row in resolvable:
            gene = str(row["gene"])
            gene_ids = mapping[gene]
            cell_values = values_for_ids(cell_values_by_id, gene_ids)
            tissue_values = values_for_ids(tissue_values_by_id, gene_ids)
            _, _, _, cell_reason = ratio_to_next(
                cell_values, hpa_pt_label, hpa_pc
            )
            _, _, _, tissue_reason = ratio_to_next(
                tissue_values, hpa_kidney_label, hpa_pc
            )
            hpa_axis_audit[gene] = {
                "cell_type": {
                    "any_data": bool(cell_values),
                    "required_target_category": hpa_pt_label,
                    "required_target_category_present": (
                        hpa_pt_label in cell_values
                    ),
                    "non_target_comparison_category_present": any(
                        category != hpa_pt_label for category in cell_values
                    ),
                    "ratio_input_status": cell_reason,
                },
                "tissue": {
                    "any_data": bool(tissue_values),
                    "required_target_category": hpa_kidney_label,
                    "required_target_category_present": (
                        hpa_kidney_label in tissue_values
                    ),
                    "non_target_comparison_category_present": any(
                        category != hpa_kidney_label for category in tissue_values
                    ),
                    "ratio_input_status": tissue_reason,
                },
            }
        incomplete_hpa_cell_ratio_inputs = sorted(
            gene
            for gene, audit in hpa_axis_audit.items()
            if audit["cell_type"]["ratio_input_status"] != "ok"
        )
        incomplete_hpa_tissue_ratio_inputs = sorted(
            gene
            for gene, audit in hpa_axis_audit.items()
            if audit["tissue"]["ratio_input_status"] != "ok"
        )
        hpa_cell_fraction = (
            (
                len(resolvable)
                - len(incomplete_hpa_cell_ratio_inputs)
            )
            / len(resolvable)
            if resolvable
            else 0.0
        )
        hpa_tissue_fraction = (
            (
                len(resolvable)
                - len(incomplete_hpa_tissue_ratio_inputs)
            )
            / len(resolvable)
            if resolvable
            else 0.0
        )
        technical_failures: list[str] = []
        if mapping_fraction < float(
            completeness["minimum_surfaceome_to_kpmp_mapping_fraction"]
        ):
            technical_failures.append(
                "Surfaceome-to-KPMP mapping fraction is below the frozen minimum"
            )
        if hpa_cell_fraction < float(
            completeness[
                "minimum_mapped_candidates_with_complete_hpa_cell_ratio_inputs_fraction"
            ]
        ):
            technical_failures.append(
                "Mapped-candidate complete HPA cell-ratio input fraction is "
                "below the frozen minimum"
            )
        if hpa_tissue_fraction < float(
            completeness[
                "minimum_mapped_candidates_with_complete_hpa_tissue_ratio_inputs_fraction"
            ]
        ):
            technical_failures.append(
                "Mapped-candidate complete HPA tissue-ratio input fraction is "
                "below the frozen minimum"
            )

        diagnostic_columns = [
            str(value) for value in RULES["stratification"]["diagnostic_columns"]
        ]
        for column in diagnostic_columns:
            if column not in obs.columns:
                raise RuntimeError(f"Missing stratification column: {column}")
        if RULES["stratification"]["empty_strata"] != "not emitted":
            raise RuntimeError("Unsupported empty-stratum policy")
        if bool(RULES["stratification"]["stratum_metrics_are_gating"]):
            raise RuntimeError("Stratum diagnostics may not silently become gates")
        if (
            RULES["expression_detection"]["matrix"] != "X"
            or RULES["expression_detection"]["multi_ensembl_policy"]
            != "union_nonzero"
        ):
            raise RuntimeError("Unsupported expression-detection contract")

        obs_assay = obs["assay"].fillna("").astype(str).to_numpy()
        obs_specimen = obs["specimen"].fillna("").astype(str).to_numpy()
        minimum_group = int(
            RULES["eligible_donor_rules"][
                "minimum_cells_per_non_target_cell_type"
            ]
        )
        donor_rows: list[dict[str, Any]] = []
        stratum_rows: list[dict[str, Any]] = []
        candidates: list[dict[str, Any]] = []

        for start in range(0, len(resolvable), CANDIDATE_BATCH_SIZE):
            batch = resolvable[start : start + CANDIDATE_BATCH_SIZE]
            batch_detection = candidate_detection(adata, batch, mapping)
            for surface_row in batch:
                gene = str(surface_row["gene"])
                detected = batch_detection[gene]
                per_condition_coverages: dict[str, list[float]] = defaultdict(list)
                reference_ratios: list[float] = []
                reference_non_pt: list[float] = []
                reference_target_negative: list[float] = []
                reference_target_positive_to_negative: list[float] = []

                for condition in CONDITIONS:
                    for donor in eligible[condition]:
                        donor_mask = (obs_donor == donor) & (
                            obs_condition == condition
                        )
                        strata = sorted(
                            set(
                                zip(
                                    obs_assay[donor_mask],
                                    obs_specimen[donor_mask],
                                    strict=True,
                                )
                            )
                        )
                        for assay, specimen in strata:
                            stratum_mask = (
                                donor_mask
                                & (obs_assay == assay)
                                & (obs_specimen == specimen)
                            )
                            stratum_rows.append(
                                {
                                    "gene": gene,
                                    "condition": condition,
                                    "donor_id": donor,
                                    "assay": assay,
                                    "specimen": specimen,
                                    **group_metrics(
                                        detected,
                                        stratum_mask,
                                        target_positive,
                                        target_negative,
                                        pt,
                                    ),
                                }
                            )
                        pooled = group_metrics(
                            detected,
                            donor_mask,
                            target_positive,
                            target_negative,
                            pt,
                        )
                        donor_rows.append(
                            {
                                "gene": gene,
                                "condition": condition,
                                "donor_id": donor,
                                **pooled,
                            }
                        )
                        coverage = pooled["target_coverage"]
                        if coverage is not None:
                            per_condition_coverages[condition].append(coverage)
                        if condition == PRIMARY_CONDITION:
                            if pooled["non_pt_detection_fraction"] is not None:
                                reference_non_pt.append(
                                    pooled["non_pt_detection_fraction"]
                                )
                            if (
                                pooled[
                                    "corrected_target_to_non_pt_detection_ratio"
                                ]
                                is not None
                            ):
                                reference_ratios.append(
                                    pooled[
                                        "corrected_target_to_non_pt_detection_ratio"
                                    ]
                                )
                            if (
                                pooled["target_negative_pt_detection_fraction"]
                                is not None
                            ):
                                reference_target_negative.append(
                                    pooled[
                                        "target_negative_pt_detection_fraction"
                                    ]
                                )
                            if (
                                pooled[
                                    "target_positive_to_target_negative_pt_detection_ratio"
                                ]
                                is not None
                            ):
                                reference_target_positive_to_negative.append(
                                    pooled[
                                        "target_positive_to_target_negative_pt_detection_ratio"
                                    ]
                                )

                ref_pool = (
                    np.isin(obs_donor, eligible[PRIMARY_CONDITION])
                    & (obs_condition == PRIMARY_CONDITION)
                    & ~pt
                )
                non_pt_cell_type_fractions: list[tuple[str, float]] = []
                for cell_type in sorted(set(obs_cell_type[ref_pool])):
                    group = ref_pool & (obs_cell_type == cell_type)
                    if int(np.sum(group)) >= minimum_group:
                        non_pt_cell_type_fractions.append(
                            (cell_type, float(np.mean(detected[group])))
                        )
                worst_cell_type, worst_cell_fraction = (
                    max(
                        non_pt_cell_type_fractions,
                        key=lambda item: (item[1], item[0]),
                    )
                    if non_pt_cell_type_fractions
                    else (None, None)
                )

                gene_ids = mapping[gene]
                cell_values = values_for_ids(cell_values_by_id, gene_ids)
                tissue_values = values_for_ids(tissue_values_by_id, gene_ids)
                (
                    hpa_cell_ratio,
                    hpa_cell_next,
                    hpa_cell_next_name,
                    hpa_cell_ratio_reason,
                ) = ratio_to_next(cell_values, hpa_pt_label, hpa_pc)
                (
                    hpa_tissue_ratio,
                    hpa_tissue_next,
                    hpa_tissue_next_name,
                    hpa_tissue_ratio_reason,
                ) = ratio_to_next(tissue_values, hpa_kidney_label, hpa_pc)
                kidney_ihc = hpa_ihc[
                    hpa_ihc["Gene"].astype(str).isin(gene_ids)
                    & (
                        hpa_ihc["Tissue"].astype(str)
                        == str(LABELS["hpa_ihc_kidney_tissue"])
                    )
                ]
                ihc_records = [
                    {
                        "gene_id": str(row["Gene"]),
                        "cell_type": str(row["Cell type"]),
                        "level": str(row["Level"]),
                        "reliability": str(row["Reliability"]),
                    }
                    for row in kidney_ihc.to_dict(orient="records")
                ]
                control = controls_table.get(gene, {})
                ref_median = quantile(
                    per_condition_coverages[PRIMARY_CONDITION], MEDIAN_Q
                )
                disease_axis = disease_stability(
                    per_condition_coverages, eligible, ref_median
                )
                direct_internalization = (
                    control.get("direct_internalization_evidence") == "true"
                )
                candidate: dict[str, Any] = {
                    **surface_row,
                    "mapping_status": "resolved",
                    "mapping_failure": None,
                    "ensembl_genes_used": ";".join(gene_ids),
                    "ensembl_gene_count": len(gene_ids),
                    "median_reference_donor_target_coverage": ref_median,
                    "q25_reference_donor_target_coverage": quantile(
                        per_condition_coverages[PRIMARY_CONDITION],
                        LOWER_QUARTILE_Q,
                    ),
                    "median_target_to_non_pt_detection_ratio": quantile(
                        reference_ratios, MEDIAN_Q
                    ),
                    "median_reference_donor_non_pt_detection_fraction": quantile(
                        reference_non_pt, MEDIAN_Q
                    ),
                    "median_reference_donor_target_negative_pt_detection_fraction": quantile(
                        reference_target_negative, MEDIAN_Q
                    ),
                    "median_target_positive_to_target_negative_pt_detection_ratio": quantile(
                        reference_target_positive_to_negative, MEDIAN_Q
                    ),
                    "maximum_reference_non_pt_cell_type_detection_fraction": worst_cell_fraction,
                    "worst_reference_non_pt_cell_type": worst_cell_type,
                    "hpa_proximal_tubule_ncpm": cell_values.get(hpa_pt_label),
                    "hpa_proximal_tubule_to_next_cell_type_ratio": hpa_cell_ratio,
                    "hpa_cell_type_ratio_input_status": hpa_cell_ratio_reason,
                    "hpa_next_cell_type": hpa_cell_next_name,
                    "hpa_next_cell_type_ncpm": hpa_cell_next,
                    "hpa_kidney_ntpm": tissue_values.get(hpa_kidney_label),
                    "hpa_kidney_to_next_tissue_ratio": hpa_tissue_ratio,
                    "hpa_tissue_ratio_input_status": hpa_tissue_ratio_reason,
                    "hpa_next_tissue": hpa_tissue_next_name,
                    "hpa_next_tissue_ntpm": hpa_tissue_next,
                    "hpa_kidney_ihc": json.dumps(
                        sorted(
                            ihc_records,
                            key=lambda row: (
                                row["gene_id"],
                                row["cell_type"],
                                row["level"],
                                row["reliability"],
                            ),
                        ),
                        sort_keys=True,
                    ),
                    "disease_stability": json.dumps(
                        disease_axis, sort_keys=True
                    ),
                    "direct_internalization_evidence": direct_internalization,
                    "internalization_evidence_id": (
                        control.get("evidence_id")
                        if direct_internalization
                        and control.get("evidence_id") not in {"", "NA", None}
                        else None
                    ),
                    "internalization_evidence_scope": (
                        control.get("evidence_scope")
                        if direct_internalization
                        else "unknown; candidate-specific primary-source review required"
                    ),
                    "membrane_polarity": "unknown",
                }
                for sensitivity in RULES["sensitivity_sets"]:
                    candidate[
                        f"passes_{sensitivity['name']}_gates"
                    ] = pass_thresholds(candidate, sensitivity)
                candidates.append(candidate)

        for surface_row in surface:
            gene = str(surface_row["gene"])
            if gene in mapping:
                continue
            candidate = {
                **surface_row,
                "mapping_status": "unresolved",
                "mapping_failure": mapping_failures.get(
                    gene, "unresolved without a recorded reason"
                ),
                "ensembl_genes_used": "",
                "ensembl_gene_count": 0,
                "direct_internalization_evidence": False,
                "internalization_evidence_id": None,
                "internalization_evidence_scope": (
                    "unknown; candidate-specific primary-source review required"
                ),
                "membrane_polarity": "unknown",
            }
            for sensitivity in RULES["sensitivity_sets"]:
                candidate[f"passes_{sensitivity['name']}_gates"] = False
            candidates.append(candidate)
        if len(candidates) != len(surface):
            raise RuntimeError(
                "Candidate CSV row contract failed to preserve the surfaceome universe"
            )

        candidate_by_gene = {row["gene"]: row for row in candidates}
        control_results: dict[str, Any] = {
            "eligible_donors": eligible,
            "donor_eligibility": donor_eligibility,
            "pt_assignment": pt_assignment,
            "slc22a12_reference_donor_detection_fractions": reference_target_detection,
            "mapping_failures": mapping_failures,
            "genes": {},
        }
        hpa_hepatocyte = str(LABELS["hpa_hepatocyte_cell_type"])
        hpa_liver = str(LABELS["hpa_liver_tissue"])
        for gene, control in sorted(controls_table.items()):
            control_cell_ids = hpa_cell_ids_by_symbol.get(gene, [])
            control_tissue_ids = hpa_tissue_ids_by_symbol.get(gene, [])
            cell_values = values_for_ids(cell_values_by_id, control_cell_ids)
            tissue_values = values_for_ids(
                tissue_values_by_id, control_tissue_ids
            )
            cell_ratio, _, cell_next, cell_ratio_reason = ratio_to_next(
                cell_values, hpa_hepatocyte, hpa_pc
            )
            tissue_ratio, _, tissue_next, tissue_ratio_reason = ratio_to_next(
                tissue_values, hpa_liver, hpa_pc
            )
            in_surfaceome = gene in surface_by_gene
            candidate = candidate_by_gene.get(gene)
            record = {
                "role": control["role"],
                "expected_observation": control["expected_observation"],
                "interpretation": control["interpretation"],
                "in_surfaceome": in_surfaceome,
                "hpa_hepatocyte_to_next_cell_type_ratio": cell_ratio,
                "hpa_cell_type_ratio_input_status": cell_ratio_reason,
                "hpa_next_cell_type": cell_next,
                "hpa_liver_to_next_tissue_ratio": tissue_ratio,
                "hpa_tissue_ratio_input_status": tissue_ratio_reason,
                "hpa_next_tissue": tissue_next,
                "hpa_proximal_tubule_ncpm": candidate.get(
                    "hpa_proximal_tubule_ncpm"
                )
                if candidate
                else None,
                "hpa_kidney_ntpm": candidate.get("hpa_kidney_ntpm")
                if candidate
                else None,
                "median_reference_donor_target_coverage": candidate.get(
                    "median_reference_donor_target_coverage"
                )
                if candidate
                else None,
                "direct_internalization_evidence": (
                    control["direct_internalization_evidence"] == "true"
                ),
                "evidence_id": control["evidence_id"],
                "evidence_scope": control["evidence_scope"],
            }
            control_results["genes"][gene] = record
            if control["role"] == "positive_pattern":
                if not in_surfaceome:
                    method_failures.append(
                        f"{gene} absent from surfaceome positive control"
                    )
                if (
                    cell_ratio is None
                    or cell_ratio
                    < float(
                        RULES["method_controls"][
                            "positive_pattern_min_hpa_hepatocyte_to_next_cell_type_ratio"
                        ]
                    )
                ):
                    method_failures.append(
                        f"{gene} hepatocyte pattern control failed"
                    )
                if (
                    tissue_ratio is None
                    or tissue_ratio
                    < float(
                        RULES["method_controls"][
                            "positive_pattern_min_hpa_liver_to_next_tissue_ratio"
                        ]
                    )
                ):
                    method_failures.append(f"{gene} liver pattern control failed")
            elif control["role"] == "negative_surface" and in_surfaceome:
                method_failures.append(
                    f"{gene} entered the transmembrane surfaceome universe"
                )
            elif control["role"] == "kidney_context":
                if (
                    candidate is None
                    or candidate["median_reference_donor_target_coverage"]
                    is None
                    or candidate["median_reference_donor_target_coverage"]
                    <= DETECTION_THRESHOLD
                    or candidate["hpa_proximal_tubule_ncpm"] is None
                    or candidate["hpa_proximal_tubule_ncpm"]
                    <= DETECTION_THRESHOLD
                    or candidate["hpa_kidney_ntpm"] is None
                    or candidate["hpa_kidney_ntpm"] <= DETECTION_THRESHOLD
                ):
                    method_failures.append(
                        f"{gene} proximal-tubule/kidney context control failed"
                    )

        if bool(RULES["pareto_axes"]["no_weighted_sum"]) is not True:
            raise RuntimeError("Weighted scores are not permitted")
        if bool(RULES["pareto_axes"]["required_for_every_sensitivity_set"]) is not True:
            raise RuntimeError("Pareto output must cover every sensitivity set")
        sensitivity_results: dict[str, dict[str, Any]] = {}
        for sensitivity in RULES["sensitivity_sets"]:
            name = str(sensitivity["name"])
            passing = [
                row for row in candidates if row[f"passes_{name}_gates"]
            ]
            front = pareto_front(passing)
            for candidate in candidates:
                candidate[f"pareto_{name}"] = candidate["gene"] in front
            sensitivity_results[name] = {
                "gate_candidate_count": len(passing),
                "gate_genes": sorted(row["gene"] for row in passing),
                "pareto_genes": sorted(front),
            }

        primary = sensitivity_results["primary"]
        if (
            primary["gate_candidate_count"] == 0
            and bool(
                completeness[
                    "negative_verdict_requires_zero_unresolved_candidate_mappings"
                ]
            )
            and mapping_failures
        ):
            technical_failures.append(
                "A negative verdict is blocked by unresolved candidate mappings"
            )
        if (
            primary["gate_candidate_count"] == 0
            and bool(
                completeness[
                    "negative_verdict_requires_zero_incomplete_hpa_cell_ratio_inputs"
                ]
            )
            and incomplete_hpa_cell_ratio_inputs
        ):
            technical_failures.append(
                "A negative verdict is blocked by incomplete HPA cell-ratio inputs"
            )
        if (
            primary["gate_candidate_count"] == 0
            and bool(
                completeness[
                    "negative_verdict_requires_zero_incomplete_hpa_tissue_ratio_inputs"
                ]
            )
            and incomplete_hpa_tissue_ratio_inputs
        ):
            technical_failures.append(
                "A negative verdict is blocked by incomplete HPA tissue-ratio inputs"
            )

        if bool(
            RULES["disease_stability_axis"]["not_used_in_primary_reference_gate"]
        ) is not True:
            raise RuntimeError("Disease stability may not enter the primary gate")
        primary_rows = [
            candidate_by_gene[gene] for gene in primary["gate_genes"]
        ]
        if method_failures:
            verdict = "METHOD_FAILURE"
            interpretation = (
                "One or more preregistered method controls failed. No "
                "biological absence or candidate-selection conclusion is permitted."
            )
        elif technical_failures:
            verdict = "SCREEN_INCOMPLETE_TECHNICAL_MISSINGNESS"
            interpretation = (
                "The frozen screen did not meet its completeness contract. No "
                "bounded negative or complete candidate-set conclusion is permitted."
            )
        elif not primary_rows:
            verdict = (
                "NO_SURFACE_EXPRESSION_TOPOLOGY_CANDIDATE_AT_PRIMARY_GATES"
            )
            interpretation = (
                "No member of the fully resolved frozen surfaceome passed every "
                "primary expression, selectivity, and topology gate. This is a "
                "bounded negative result, not a rejection of URAT1 or siRNA."
            )
        else:
            verdict = (
                "SURFACE_EXPRESSION_TOPOLOGY_CANDIDATES_NEED_RECEPTOR_INTERNALIZATION_AND_POLARITY_VALIDATION"
            )
            interpretation = (
                "At least one surface-expression/topology follow-up candidate "
                "warrants candidate-specific receptor status, ligand and "
                "internalization, and membrane-polarity investigation."
            )
        if verdict not in RULES["verdict_order"]:
            raise RuntimeError(f"Undeclared verdict: {verdict}")

        missingness = {
            "schema_version": 1,
            "surfaceome_candidate_count": len(surface),
            "kpmp_resolvable_candidate_count": len(resolvable),
            "surfaceome_to_kpmp_mapping_fraction": mapping_fraction,
            "mapping_failures": mapping_failures,
            "hpa_axis_audit": hpa_axis_audit,
            "mapped_candidates_with_incomplete_hpa_cell_ratio_inputs": (
                incomplete_hpa_cell_ratio_inputs
            ),
            "mapped_candidates_with_complete_hpa_cell_ratio_inputs_fraction": (
                hpa_cell_fraction
            ),
            "mapped_candidates_with_incomplete_hpa_tissue_ratio_inputs": (
                incomplete_hpa_tissue_ratio_inputs
            ),
            "mapped_candidates_with_complete_hpa_tissue_ratio_inputs_fraction": (
                hpa_tissue_fraction
            ),
            "technical_failures": sorted(set(technical_failures)),
            "pt_assignment": pt_assignment,
        }
        result = {
            "schema_version": 1,
            "question": (
                "Does the frozen human surfaceome contain proximal-tubule "
                "surface-expression/topology follow-up candidates?"
            ),
            "verdict": verdict,
            "interpretation": interpretation,
            "method_failures": sorted(set(method_failures)),
            "technical_failures": sorted(set(technical_failures)),
            "candidate_universe_count": len(surface),
            "resolvable_candidate_count": len(resolvable),
            "candidate_csv_row_policy": RULES["expression_detection"][
                "candidate_csv_row_policy"
            ],
            "primary_gate_candidate_count": primary["gate_candidate_count"],
            "primary_gate_genes": primary["gate_genes"],
            "primary_pareto_genes": primary["pareto_genes"],
            "sensitivity_sets": sensitivity_results,
            "eligible_donor_counts": {
                condition: len(donors) for condition, donors in eligible.items()
            },
            "stratification_contract": RULES["stratification"][
                "primary_gate_pooling"
            ],
            "mapping_contract": RULES["expression_detection"][
                "multi_ensembl_note"
            ],
            "rules": RULES,
            "nonclaims": [
                "ligand binding",
                "receptor-mediated internalization",
                "basolateral or apical membrane polarity",
                "blood or urinary access",
                "endosomal escape",
                "siRNA delivery or release",
                "SLC22A12 knockdown",
                "urate transport change",
                "dose",
                "safety",
                "efficacy",
            ],
            "invalidation_boundary": (
                "A negative result applies only to the frozen surfaceome, "
                "expression datasets, detection definition, and preregistered "
                "thresholds."
            ),
        }
        write_completed_audit_outputs(
            candidates,
            donor_rows,
            stratum_rows,
            control_results,
            missingness,
            result,
            input_receipt,
            packages,
        )
        exit_code = (
            int(RULES["failure_output_contract"]["exit_code"])
            if verdict == "METHOD_FAILURE"
            else 0
        )
        return verdict, exit_code
    finally:
        adata.file.close()


def main() -> int:
    clear_output_state()
    input_receipt: list[dict[str, Any]] = []
    packages: dict[str, str] = {}
    try:
        packages, runtime_failures = verify_runtime()
        if runtime_failures:
            raise RuntimeError("; ".join(runtime_failures))
        input_receipt = verify_inputs()
        verdict, exit_code = run_analysis(
            input_receipt, packages, runtime_failures
        )
        print(verdict)
        return exit_code
    except Exception as exc:
        write_failure_outputs(exc, input_receipt, packages)
        print(f"METHOD_FAILURE: {exc}", file=sys.stderr)
        return int(RULES["failure_output_contract"]["exit_code"])


if __name__ == "__main__":
    sys.exit(main())
