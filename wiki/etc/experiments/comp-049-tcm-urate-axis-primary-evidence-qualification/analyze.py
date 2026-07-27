#!/usr/bin/env python3
"""comp-049: qualify a fixed, mixed-source TCM urate-axis evidence set."""

from __future__ import annotations

import json
import pathlib
import re


ROOT = pathlib.Path(__file__).parent
INPUT = ROOT / "inputs" / "evidence_records.json"
OUTPUTS = ROOT / "outputs"

EXPECTED_RECORD_IDS = {
    "smilax-tfsg-2019",
    "emodin-2023",
    "coix-seed-oil-2025",
    "plantaginis-semen-2024",
    "modified-simiao-review-2017",
}
ALLOWED_MATERIAL_TYPES = {
    "isolated_compound",
    "defined_extract_fraction",
    "defined_extract",
    "multi_component_formula_family",
}
ALLOWED_SOURCE_KINDS = {
    "commercial_reagent",
    "plant_derived_fraction",
    "plant_derived_extract",
    "variable_formula_family",
}
ALLOWED_IDENTITY_STATUSES = {
    "sufficiently_specified_for_record",
    "variable_formula_family",
}
ALLOWED_MATERIAL_EVIDENCE_GAPS = {
    "preparation_not_verified",
    "reagent_purity_attribution",
    "botanical_authentication_not_verified",
}
SOURCE_DESIGN_CONTRACT = {
    "primary_animal_study": ("primary", "animal_model", "Animal Model"),
    "systematic_review_meta_analysis": (
        "secondary",
        "systematic_review",
        "Clinical Trial",
    ),
}
PHENOTYPE_STATUS_CONTRACT = {
    "primary_animal_study": "measured_in_primary_study",
    "systematic_review_meta_analysis": (
        "reported_by_secondary_review_not_independently_verified"
    ),
}
ALLOWED_WEAKNESSES = {
    "urate_production",
    "renal_urate_excretion",
    "renal_urate_reabsorption",
    "intestinal_urate_excretion",
    "serum_urate",
    "gout_inflammation",
}
MECHANISTIC_WEAKNESSES = {
    "urate_production",
    "renal_urate_excretion",
    "renal_urate_reabsorption",
    "intestinal_urate_excretion",
}
ALLOWED_MECHANISM_IDS = {
    "XOD",
    "OAT1",
    "OCTN2",
    "ABCG2",
    "URAT1",
    "URAT1_GLUT9",
    "FEUA",
    "SERUM_URATE",
}
ALLOWED_POLARITIES = {"increase", "decrease", "no_change", "mixed", "unknown"}
ALLOWED_ENDPOINT_KINDS = {
    "assay_signal",
    "enzyme_activity",
    "expression",
    "whole_animal_function",
    "clinical_biomarker",
    "transport_flux",
}
ALLOWED_COMPARTMENTS = {
    "hepatic",
    "renal",
    "intestinal",
    "renal_and_intestinal",
    "systemic",
    "clinical",
}
ALLOWED_DIRECTNESS = {
    "associated_measure",
    "direct_function",
    "expression",
    "whole_organism_function",
    "clinical_biomarker",
}
ALLOWED_TARGET_ATTRIBUTION = {
    "associated_target_measure",
    "unattributed_system_function",
}
ALLOWED_EFFECT_SCOPES = {
    "reported_in_one_tested_group",
    "reported_in_at_least_one_tested_group",
    "reported_no_change_in_tested_groups",
    "reported_in_meta_analyzed_trial_set",
}
ALLOWED_FUNCTION_EVIDENCE_STATUSES = {
    "present_in_verified_source",
    "not_reported_in_verified_source",
    "not_verified_in_available_source",
}
MECHANISM_WEAKNESS_COMPARTMENT_CONTRACT = {
    "XOD": ({"urate_production"}, {"hepatic", "systemic"}),
    "OAT1": ({"renal_urate_excretion"}, {"renal"}),
    "OCTN2": ({"renal_urate_excretion"}, {"renal"}),
    "ABCG2": (
        {"renal_urate_excretion", "intestinal_urate_excretion"},
        {"renal", "intestinal", "renal_and_intestinal"},
    ),
    "URAT1": ({"renal_urate_reabsorption"}, {"renal"}),
    "URAT1_GLUT9": ({"renal_urate_reabsorption"}, {"renal"}),
    "FEUA": ({"renal_urate_excretion"}, {"renal"}),
    "SERUM_URATE": ({"serum_urate"}, {"clinical"}),
}
PMID_RE = re.compile(r"^[1-9][0-9]{0,8}$")
PMCID_RE = re.compile(r"^PMC[1-9][0-9]*$")
DOI_RE = re.compile(r"^10\.[0-9]{4,9}/\S+$", re.IGNORECASE)

EXPECTED_OUTCOMES = {
    "smilax-tfsg-2019": {
        "disposition": "PREPARATION_VERIFICATION_REQUIRED",
        "gap_flags": {
            "preparation_not_verified",
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:renal_urate_excretion",
        },
        "deferred_gap_flags": {
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:renal_urate_excretion",
        },
        "missing_target_attribution_weaknesses": {
            "urate_production",
            "renal_urate_excretion",
        },
    },
    "emodin-2023": {
        "disposition": "REAGENT_PURITY_ATTRIBUTION_REQUIRED",
        "gap_flags": {
            "reagent_purity_attribution",
            "free_exposure",
            "molecular_target_attribution",
        },
        "deferred_gap_flags": {
            "free_exposure",
            "molecular_target_attribution",
        },
        "missing_target_attribution_weaknesses": {
            "renal_urate_excretion",
        },
    },
    "coix-seed-oil-2025": {
        "disposition": "BOTANICAL_AUTHENTICATION_REQUIRED",
        "gap_flags": {
            "botanical_authentication_not_verified",
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:intestinal_urate_excretion",
            "mechanism_matched_function:renal_urate_excretion",
            "intestinal_barrier_and_viability",
        },
        "deferred_gap_flags": {
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:intestinal_urate_excretion",
            "mechanism_matched_function:renal_urate_excretion",
            "intestinal_barrier_and_viability",
        },
        "missing_target_attribution_weaknesses": {
            "urate_production",
            "renal_urate_excretion",
            "intestinal_urate_excretion",
        },
    },
    "plantaginis-semen-2024": {
        "disposition": "MATERIAL_ATTRIBUTION_REQUIRED",
        "gap_flags": {
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:renal_urate_reabsorption",
            "mechanism_matched_function:urate_production",
        },
        "deferred_gap_flags": {
            "free_exposure",
            "molecular_target_attribution",
            "mechanism_matched_function:renal_urate_reabsorption",
            "mechanism_matched_function:urate_production",
        },
        "missing_target_attribution_weaknesses": {
            "urate_production",
            "renal_urate_reabsorption",
        },
    },
    "modified-simiao-review-2017": {
        "disposition": "PRIMARY_TRIAL_REVIEW_REQUIRED",
        "gap_flags": {
            "primary_trial_review",
            "tested_material_identity",
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
        },
        "deferred_gap_flags": {
            "tested_material_identity",
            "component_attribution",
            "free_exposure",
            "molecular_target_attribution",
        },
        "missing_target_attribution_weaknesses": {
            "serum_urate",
        },
    },
}

ALLOWED_EXPOSURE_STATUSES = {
    "measured",
    "not_measured",
    "not_verified_in_available_source",
}
ALLOWED_GENERAL_BARRIER_EVIDENCE = {
    "present_histology_and_tight_junction_markers",
    "absent",
    "not_applicable",
}
ALLOWED_DIRECT_FLUX_CONTROLS = {
    "present",
    "absent_no_direct_flux_assay",
    "absent",
    "not_applicable",
}


def require_string(value: object, field: str, record_id: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{record_id}: {field} must be a non-empty string")
    return value.strip()


def require_bool(value: object, field: str, record_id: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{record_id}: {field} must be Boolean")
    return value


def require_choice(
    value: object, field: str, record_id: str, allowed: set[str]
) -> str:
    selected = require_string(value, field, record_id)
    if selected not in allowed:
        raise ValueError(f"{record_id}: unsupported {field} {selected!r}")
    return selected


def require_string_list(value: object, field: str, record_id: str) -> list[str]:
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        raise ValueError(f"{record_id}: {field} must contain non-empty strings")
    normalized = [item.strip() for item in value]
    if len(normalized) != len(set(normalized)):
        raise ValueError(f"{record_id}: {field} contains duplicate values")
    return normalized


def require_optional_choice_list(
    value: object, field: str, record_id: str, allowed: set[str]
) -> list[str]:
    if not isinstance(value, list):
        raise ValueError(f"{record_id}: {field} must be a list")
    if any(not isinstance(item, str) or item not in allowed for item in value):
        raise ValueError(f"{record_id}: {field} contains an unsupported value")
    if len(value) != len(set(value)):
        raise ValueError(f"{record_id}: {field} contains duplicate values")
    return value


def validate_source(source: object, record_id: str) -> dict[str, object]:
    if not isinstance(source, dict):
        raise ValueError(f"{record_id}: source must be an object")
    require_string(source.get("citation"), "source.citation", record_id)
    require_string(source.get("verified_location"), "source.verified_location", record_id)
    pmid = source.get("pmid")
    pmcid = source.get("pmcid")
    doi = source.get("doi")
    if pmid is not None and (not isinstance(pmid, str) or not PMID_RE.fullmatch(pmid)):
        raise ValueError(f"{record_id}: source.pmid has invalid syntax")
    if pmcid is not None and (
        not isinstance(pmcid, str) or not PMCID_RE.fullmatch(pmcid)
    ):
        raise ValueError(f"{record_id}: source.pmcid has invalid syntax")
    if doi is not None and (not isinstance(doi, str) or not DOI_RE.fullmatch(doi)):
        raise ValueError(f"{record_id}: source.doi has invalid syntax")
    if not any((pmid, pmcid, doi)):
        raise ValueError(f"{record_id}: source requires PMID, PMCID, or DOI")
    return source


def validate_material(material: object, record_id: str) -> dict[str, object]:
    if not isinstance(material, dict):
        raise ValueError(f"{record_id}: material must be an object")
    require_string(material.get("name"), "material.name", record_id)
    require_choice(
        material.get("type"),
        "material.type",
        record_id,
        ALLOWED_MATERIAL_TYPES,
    )
    tested = material.get("tested_material")
    if not isinstance(tested, dict):
        raise ValueError(f"{record_id}: material.tested_material must be an object")
    source_kind = require_choice(
        tested.get("source_kind"),
        "material.tested_material.source_kind",
        record_id,
        ALLOWED_SOURCE_KINDS,
    )
    for field in ("identity", "preparation_or_composition", "authentication_boundary"):
        require_string(
            tested.get(field),
            f"material.tested_material.{field}",
            record_id,
        )
    require_string_list(
        material.get("traditional_occurrence_or_formula_context"),
        "material.traditional_occurrence_or_formula_context",
        record_id,
    )
    require_bool(
        material.get("individual_component_causality_established"),
        "material.individual_component_causality_established",
        record_id,
    )
    material_gaps = require_optional_choice_list(
        material.get("material_evidence_gaps"),
        "material.material_evidence_gaps",
        record_id,
        ALLOWED_MATERIAL_EVIDENCE_GAPS,
    )
    gap_contract = {
        "commercial_reagent": {"reagent_purity_attribution"},
        "plant_derived_fraction": {"preparation_not_verified"},
        "plant_derived_extract": {"botanical_authentication_not_verified"},
        "variable_formula_family": set(),
    }
    if set(material_gaps) - gap_contract[source_kind]:
        raise ValueError(
            f"{record_id}: material evidence gap is incompatible with source kind"
        )
    require_choice(
        material.get("identity_status"),
        "material.identity_status",
        record_id,
        ALLOWED_IDENTITY_STATUSES,
    )
    return material


def validate_observation(
    observation: object, record_id: str
) -> dict[str, object]:
    if not isinstance(observation, dict):
        raise ValueError(f"{record_id}: each mechanism observation must be an object")
    require_choice(
        observation.get("mechanism_id"),
        "mechanism_observations.mechanism_id",
        record_id,
        ALLOWED_MECHANISM_IDS,
    )
    require_string(
        observation.get("target_or_endpoint"),
        "mechanism_observations.target_or_endpoint",
        record_id,
    )
    polarity = require_choice(
        observation.get("effect_polarity"),
        "mechanism_observations.effect_polarity",
        record_id,
        ALLOWED_POLARITIES,
    )
    endpoint_kind = require_choice(
        observation.get("endpoint_kind"),
        "mechanism_observations.endpoint_kind",
        record_id,
        ALLOWED_ENDPOINT_KINDS,
    )
    require_choice(
        observation.get("compartment"),
        "mechanism_observations.compartment",
        record_id,
        ALLOWED_COMPARTMENTS,
    )
    directness = require_choice(
        observation.get("measurement_directness"),
        "mechanism_observations.measurement_directness",
        record_id,
        ALLOWED_DIRECTNESS,
    )
    attribution = require_choice(
        observation.get("target_attribution"),
        "mechanism_observations.target_attribution",
        record_id,
        ALLOWED_TARGET_ATTRIBUTION,
    )
    effect_scope = require_choice(
        observation.get("effect_scope"),
        "mechanism_observations.effect_scope",
        record_id,
        ALLOWED_EFFECT_SCOPES,
    )
    relevant = require_string_list(
        observation.get("relevant_weaknesses"),
        "mechanism_observations.relevant_weaknesses",
        record_id,
    )
    unknown_weaknesses = set(relevant) - ALLOWED_WEAKNESSES
    if unknown_weaknesses:
        raise ValueError(
            f"{record_id}: unsupported relevant weakness(es) "
            f"{sorted(unknown_weaknesses)}"
        )
    mechanism_id = str(observation["mechanism_id"])
    allowed_weaknesses, allowed_compartments = (
        MECHANISM_WEAKNESS_COMPARTMENT_CONTRACT[mechanism_id]
    )
    if set(relevant) - allowed_weaknesses:
        raise ValueError(
            f"{record_id}: {mechanism_id} maps to an incompatible weakness"
        )
    if observation["compartment"] not in allowed_compartments:
        raise ValueError(
            f"{record_id}: {mechanism_id} maps to an incompatible compartment"
        )
    if directness == "expression" and endpoint_kind != "expression":
        raise ValueError(f"{record_id}: expression directness requires expression endpoint")
    if directness == "direct_function" and endpoint_kind not in {
        "enzyme_activity",
        "transport_flux",
    }:
        raise ValueError(
            f"{record_id}: direct function requires enzyme_activity or transport_flux"
        )
    if (polarity == "no_change") != (
        effect_scope == "reported_no_change_in_tested_groups"
    ):
        raise ValueError(
            f"{record_id}: no-change polarity and effect scope must agree"
        )
    return observation


def validate_observation_consistency(
    observations: list[dict[str, object]], record_id: str
) -> None:
    seen: dict[tuple[object, ...], str] = {}
    for observation in observations:
        key = (
            observation["mechanism_id"],
            observation["target_or_endpoint"],
            observation["endpoint_kind"],
            observation["compartment"],
            observation["effect_scope"],
            tuple(sorted(observation["relevant_weaknesses"])),
        )
        polarity = str(observation["effect_polarity"])
        if key in seen:
            if seen[key] == polarity:
                raise ValueError(f"{record_id}: duplicate mechanism observation")
            raise ValueError(
                f"{record_id}: conflicting polarities for one scoped observation"
            )
        seen[key] = polarity


def validate_function_evidence(
    value: object,
    record_id: str,
    declared_weaknesses: set[str],
    observations: list[dict[str, object]],
) -> list[dict[str, object]]:
    if not isinstance(value, list):
        raise ValueError(
            f"{record_id}: mechanism_function_evidence must be a list"
        )
    required_weaknesses = declared_weaknesses & MECHANISTIC_WEAKNESSES
    encoded_weaknesses: set[str] = set()
    for index, entry in enumerate(value):
        if not isinstance(entry, dict):
            raise ValueError(
                f"{record_id}: mechanism_function_evidence[{index}] must be an object"
            )
        weakness = require_choice(
            entry.get("weakness"),
            f"mechanism_function_evidence[{index}].weakness",
            record_id,
            MECHANISTIC_WEAKNESSES,
        )
        if weakness not in required_weaknesses:
            raise ValueError(
                f"{record_id}: function-evidence weakness is not declared"
            )
        if weakness in encoded_weaknesses:
            raise ValueError(
                f"{record_id}: duplicate mechanism-function evidence for {weakness}"
            )
        encoded_weaknesses.add(weakness)
        status = require_choice(
            entry.get("status"),
            f"mechanism_function_evidence[{index}].status",
            record_id,
            ALLOWED_FUNCTION_EVIDENCE_STATUSES,
        )
        require_string(
            entry.get("boundary"),
            f"mechanism_function_evidence[{index}].boundary",
            record_id,
        )
        has_matching_observation = any(
            observation_matches_weakness_function(observation, weakness)
            for observation in observations
        )
        if (status == "present_in_verified_source") != has_matching_observation:
            raise ValueError(
                f"{record_id}: function-evidence status disagrees with observations "
                f"for {weakness}"
            )
    if encoded_weaknesses != required_weaknesses:
        raise ValueError(
            f"{record_id}: mechanism-function evidence must cover every "
            "declared mechanistic weakness"
        )
    return value


def validate_free_exposure(
    value: object, record_id: str, declared_weaknesses: set[str]
) -> list[dict[str, object]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{record_id}: free_exposure must be a non-empty list")
    validated: list[dict[str, object]] = []
    covered_weaknesses: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for index, entry in enumerate(value):
        if not isinstance(entry, dict):
            raise ValueError(f"{record_id}: free_exposure[{index}] must be an object")
        compartment = require_choice(
            entry.get("compartment"),
            f"free_exposure[{index}].compartment",
            record_id,
            ALLOWED_COMPARTMENTS,
        )
        require_choice(
            entry.get("status"),
            f"free_exposure[{index}].status",
            record_id,
            ALLOWED_EXPOSURE_STATUSES,
        )
        relevant = require_string_list(
            entry.get("relevant_weaknesses"),
            f"free_exposure[{index}].relevant_weaknesses",
            record_id,
        )
        if set(relevant) - declared_weaknesses:
            raise ValueError(
                f"{record_id}: free exposure maps outside the declared gout weaknesses"
            )
        for weakness in relevant:
            pair = (compartment, weakness)
            if pair in seen_pairs:
                raise ValueError(
                    f"{record_id}: duplicate free-exposure compartment/weakness mapping"
                )
            seen_pairs.add(pair)
        covered_weaknesses.update(relevant)
        validated.append(entry)
    if covered_weaknesses != declared_weaknesses:
        raise ValueError(
            f"{record_id}: free exposure must map every declared gout weakness exactly"
        )
    return validated


def validate_intestinal_controls(
    value: object, record_id: str, has_intestinal_weakness: bool
) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{record_id}: intestinal_controls must be an object")
    general = require_choice(
        value.get("general_barrier_evidence"),
        "intestinal_controls.general_barrier_evidence",
        record_id,
        ALLOWED_GENERAL_BARRIER_EVIDENCE,
    )
    barrier = require_choice(
        value.get("direct_flux_assay_barrier_control"),
        "intestinal_controls.direct_flux_assay_barrier_control",
        record_id,
        ALLOWED_DIRECT_FLUX_CONTROLS,
    )
    viability = require_choice(
        value.get("direct_flux_assay_viability_control"),
        "intestinal_controls.direct_flux_assay_viability_control",
        record_id,
        ALLOWED_DIRECT_FLUX_CONTROLS,
    )
    require_string(
        value.get("boundary"), "intestinal_controls.boundary", record_id
    )
    if has_intestinal_weakness and any(
        status == "not_applicable" for status in (general, barrier, viability)
    ):
        raise ValueError(
            f"{record_id}: intestinal-weakness records cannot mark controls not applicable"
        )
    if not has_intestinal_weakness and any(
        status != "not_applicable" for status in (general, barrier, viability)
    ):
        raise ValueError(
            f"{record_id}: non-intestinal records must mark intestinal controls not applicable"
        )
    return value


def validate_record(record: object) -> dict[str, object]:
    if not isinstance(record, dict):
        raise ValueError("every record must be an object")
    record_id = require_string(record.get("record_id"), "record_id", "record")
    validate_material(record.get("material"), record_id)

    weaknesses = require_string_list(record.get("gout_weakness"), "gout_weakness", record_id)
    unknown_weaknesses = set(weaknesses) - ALLOWED_WEAKNESSES
    if unknown_weaknesses:
        raise ValueError(
            f"{record_id}: unsupported gout weakness(es) {sorted(unknown_weaknesses)}"
        )

    source_design = require_string(
        record.get("source_design"), "source_design", record_id
    )
    if source_design not in SOURCE_DESIGN_CONTRACT:
        raise ValueError(f"{record_id}: unsupported source_design {source_design!r}")
    contract = (
        require_string(record.get("source_tier"), "source_tier", record_id),
        require_string(record.get("assay_type"), "assay_type", record_id),
        require_string(
            record.get("underlying_evidence_level"),
            "underlying_evidence_level",
            record_id,
        ),
    )
    if contract != SOURCE_DESIGN_CONTRACT[source_design]:
        raise ValueError(
            f"{record_id}: source design, source tier, assay, and evidence level disagree"
        )
    phenotype_status = require_string(
        record.get("phenotype_status"), "phenotype_status", record_id
    )
    if phenotype_status != PHENOTYPE_STATUS_CONTRACT[source_design]:
        raise ValueError(
            f"{record_id}: phenotype status disagrees with source design"
        )

    require_string(record.get("biological_system"), "biological_system", record_id)
    validate_free_exposure(record.get("free_exposure"), record_id, set(weaknesses))
    validate_intestinal_controls(
        record.get("intestinal_controls"),
        record_id,
        "intestinal_urate_excretion" in weaknesses,
    )

    observations = record.get("mechanism_observations")
    if not isinstance(observations, list) or not observations:
        raise ValueError(f"{record_id}: mechanism_observations must be non-empty")
    for observation in observations:
        validate_observation(observation, record_id)
    validate_observation_consistency(observations, record_id)
    secondary_scope = "reported_in_meta_analyzed_trial_set"
    if source_design == "systematic_review_meta_analysis" and any(
        observation["effect_scope"] != secondary_scope
        for observation in observations
    ):
        raise ValueError(
            f"{record_id}: secondary-review observations require review-level scope"
        )
    if source_design == "primary_animal_study" and any(
        observation["effect_scope"] == secondary_scope
        for observation in observations
    ):
        raise ValueError(
            f"{record_id}: primary-study observations cannot use review-level scope"
        )
    covered_by_observations = {
        weakness
        for observation in observations
        for weakness in observation["relevant_weaknesses"]
        if weakness in set(weaknesses)
    }
    if covered_by_observations != set(weaknesses):
        raise ValueError(
            f"{record_id}: every declared gout weakness requires an observation mapping"
        )
    validate_function_evidence(
        record.get("mechanism_function_evidence"),
        record_id,
        set(weaknesses),
        observations,
    )

    require_string(record.get("attribution_boundary"), "attribution_boundary", record_id)
    validate_source(record.get("source"), record_id)
    return record


def load_records() -> tuple[dict[str, object], list[dict[str, object]]]:
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 2:
        raise ValueError("unsupported schema_version")
    evidence_set = payload.get("evidence_set")
    if not isinstance(evidence_set, dict):
        raise ValueError("evidence_set must be an object")
    for field in ("scope", "cutoff_date", "selection_rule"):
        require_string(evidence_set.get(field), f"evidence_set.{field}", "input")
    declared_ids = require_string_list(
        evidence_set.get("record_ids"), "evidence_set.record_ids", "input"
    )
    if set(declared_ids) != EXPECTED_RECORD_IDS or len(declared_ids) != len(
        EXPECTED_RECORD_IDS
    ):
        raise ValueError("evidence_set.record_ids must contain the exact fixed record set")

    raw_records = payload.get("records")
    if not isinstance(raw_records, list) or not raw_records:
        raise ValueError("records must be a non-empty list")
    records = [validate_record(record) for record in raw_records]
    ids = [str(record["record_id"]) for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("record_id values must be unique")
    if set(ids) != EXPECTED_RECORD_IDS:
        raise ValueError("records must contain the exact fixed record set")
    return evidence_set, records


def observation_matches_weakness_function(
    observation: dict[str, object], weakness: str
) -> bool:
    if (
        weakness not in observation["relevant_weaknesses"]
        or observation["effect_polarity"] in {"no_change", "unknown"}
    ):
        return False
    molecular_function = (
        observation["measurement_directness"] == "direct_function"
        and observation["endpoint_kind"] in {"enzyme_activity", "transport_flux"}
    )
    physiological_function = (
        weakness == "renal_urate_excretion"
        and observation["mechanism_id"] == "FEUA"
        and observation["measurement_directness"] == "whole_organism_function"
        and observation["endpoint_kind"] == "whole_animal_function"
    )
    return molecular_function or physiological_function


def missing_target_attribution_weaknesses(
    record: dict[str, object],
) -> set[str]:
    # This fixed-set design admits associated and unattributed observations only.
    # Adding a causally attributed record requires a new Gate 1 design and schema.
    return set(record["gout_weakness"])


def free_exposure_complete(record: dict[str, object]) -> bool:
    return all(
        exposure["status"] == "measured" for exposure in record["free_exposure"]
    )


def collect_gaps(record: dict[str, object]) -> list[dict[str, str]]:
    gaps: list[dict[str, str]] = []

    def add(flag: str, reason: str) -> None:
        gaps.append({"flag": flag, "reason": reason})

    material = record["material"]
    if record["source_tier"] == "secondary":
        add(
            "primary_trial_review",
            "the supplied source is secondary; underlying trials require independent review",
        )
    if material["identity_status"] == "variable_formula_family":
        add(
            "tested_material_identity",
            "the source covers a variable formula family rather than one standardized material",
        )
    material_gap_reasons = {
        "preparation_not_verified": (
            "the available verified source does not establish the full tested-material "
            "preparation"
        ),
        "reagent_purity_attribution": (
            "the stated reagent purity does not exclude an impurity contribution"
        ),
        "botanical_authentication_not_verified": (
            "independent botanical authentication was not verified for the tested lot"
        ),
    }
    for material_gap in material["material_evidence_gaps"]:
        add(material_gap, material_gap_reasons[material_gap])
    if (
        material["type"] != "isolated_compound"
        and not material["individual_component_causality_established"]
    ):
        add(
            "component_attribution",
            "the tested material does not establish an individual causal component",
        )
    if not free_exposure_complete(record):
        exposure_statuses = {
            exposure["status"] for exposure in record["free_exposure"]
        }
        if "not_verified_in_available_source" in exposure_statuses:
            exposure_reason = (
                "the available verified source does not establish free exposure "
                "in every mechanism-relevant compartment"
            )
        else:
            exposure_reason = (
                "free exposure in the mechanism-relevant compartment was not measured"
            )
        add(
            "free_exposure",
            exposure_reason,
        )
    missing_target_weaknesses = missing_target_attribution_weaknesses(record)
    if missing_target_weaknesses:
        add(
            "molecular_target_attribution",
            "direct causal molecular-target attribution is absent or unverified for "
            f"these declared weaknesses: {', '.join(sorted(missing_target_weaknesses))}",
        )

    function_evidence = {
        entry["weakness"]: entry
        for entry in record["mechanism_function_evidence"]
    }
    for weakness in sorted(set(record["gout_weakness"]) & MECHANISTIC_WEAKNESSES):
        entry = function_evidence[weakness]
        if entry["status"] != "present_in_verified_source":
            if entry["status"] == "not_verified_in_available_source":
                reason = (
                    "the available verified source does not establish a non-null "
                    f"direct functional measurement matching {weakness}"
                )
            else:
                reason = (
                    "the verified source does not report a non-null direct "
                    f"functional measurement matching {weakness}"
                )
            add(
                f"mechanism_matched_function:{weakness}",
                reason,
            )

    if (
        "intestinal_urate_excretion" in record["gout_weakness"]
        and (
            record["intestinal_controls"]["direct_flux_assay_barrier_control"]
            != "present"
            or record["intestinal_controls"]["direct_flux_assay_viability_control"]
            != "present"
        )
    ):
        add(
            "intestinal_barrier_and_viability",
            "general intestinal histology or tight-junction markers do not substitute "
            "for barrier-integrity and viability controls in a direct urate-flux assay",
        )
    return gaps


def select_disposition(
    record: dict[str, object], gap_flags: set[str]
) -> tuple[str, str | None, list[str]]:
    priority = (
        ("primary_trial_review", "PRIMARY_TRIAL_REVIEW_REQUIRED"),
        ("tested_material_identity", "TESTED_MATERIAL_IDENTITY_REQUIRED"),
        ("preparation_not_verified", "PREPARATION_VERIFICATION_REQUIRED"),
        (
            "reagent_purity_attribution",
            "REAGENT_PURITY_ATTRIBUTION_REQUIRED",
        ),
        (
            "botanical_authentication_not_verified",
            "BOTANICAL_AUTHENTICATION_REQUIRED",
        ),
        ("component_attribution", "MATERIAL_ATTRIBUTION_REQUIRED"),
        ("molecular_target_attribution", "TARGET_ATTRIBUTION_REQUIRED"),
    )
    for flag, disposition in priority:
        if flag in gap_flags:
            return disposition, flag, sorted(gap_flags - {flag})
    mechanism_gaps = sorted(
        flag for flag in gap_flags if flag.startswith("mechanism_matched_function:")
    )
    if mechanism_gaps:
        selected = mechanism_gaps[0]
        return (
            "MECHANISM_MATCHED_FUNCTION_REQUIRED",
            selected,
            sorted(gap_flags - {selected}),
        )
    if "free_exposure" in gap_flags:
        return (
            "FREE_EXPOSURE_REQUIRED",
            "free_exposure",
            sorted(gap_flags - {"free_exposure"}),
        )
    if "intestinal_barrier_and_viability" in gap_flags:
        return (
            "INTESTINAL_BARRIER_AND_VIABILITY_REQUIRED",
            "intestinal_barrier_and_viability",
            sorted(gap_flags - {"intestinal_barrier_and_viability"}),
        )
    return "EVIDENCE_RECORD_COMPLETE_REVIEW_REQUIRED", None, []


def verify_preregistered_outcome(
    record_id: str,
    disposition: str,
    gap_flags: set[str],
    deferred_gap_flags: set[str],
    missing_target_weaknesses: set[str],
) -> None:
    expected = EXPECTED_OUTCOMES[record_id]
    if disposition != expected["disposition"]:
        raise AssertionError(
            f"{record_id}: expected {expected['disposition']}, got {disposition}"
        )
    if gap_flags != expected["gap_flags"]:
        raise AssertionError(
            f"{record_id}: expected gaps {sorted(expected['gap_flags'])}, "
            f"got {sorted(gap_flags)}"
        )
    if deferred_gap_flags != expected["deferred_gap_flags"]:
        raise AssertionError(
            f"{record_id}: expected deferred gaps "
            f"{sorted(expected['deferred_gap_flags'])}, "
            f"got {sorted(deferred_gap_flags)}"
        )
    if (
        missing_target_weaknesses
        != expected["missing_target_attribution_weaknesses"]
    ):
        raise AssertionError(
            f"{record_id}: expected missing target-attribution weaknesses "
            f"{sorted(expected['missing_target_attribution_weaknesses'])}, "
            f"got {sorted(missing_target_weaknesses)}"
        )
def render_summary(result: dict[str, object]) -> str:
    lines = [
        "# comp-049 — TCM urate-axis evidence qualification",
        "",
        "**Boundary:** fixed-set evidence qualification and experiment routing only.",
        "No compound rank, viability label, dose, occupancy, clinical-risk tier,",
        "efficacy inference, or delivery recommendation is produced.",
        "",
    ]
    for record in result["records"]:
        source = record["source"]
        source_ids = [
            value
            for value in (
                f"PMID {source['pmid']}" if source.get("pmid") else None,
                source.get("pmcid"),
                f"DOI {source['doi']}" if source.get("doi") else None,
            )
            if value
        ]
        lines += [
            f"## {record['material']['name']}",
            "",
            f"- **Source / tier:** {source['citation']} ({record['source_tier']}; "
            f"{record['source_design']}; {record['underlying_evidence_level']}; "
            f"{', '.join(source_ids)})",
            f"- **Verified source location:** {source['verified_location']}",
            f"- **Assay / system:** {record['assay_type']}; "
            f"{record['biological_system']}",
            f"- **Phenotype provenance:** {record['phenotype_status']}",
            f"- **Declared gout weaknesses:** "
            f"{', '.join(record['gout_weakness'])}",
            f"- **Tested material:** "
            f"{record['material']['tested_material']['source_kind']}; "
            f"{record['material']['tested_material']['identity']}; "
            f"{record['material']['tested_material']['preparation_or_composition']}",
            f"- **Material-authentication boundary:** "
            f"{record['material']['tested_material']['authentication_boundary']}",
            f"- **Explicit material evidence gaps:** "
            f"{', '.join(record['material']['material_evidence_gaps']) or 'none'}",
            f"- **Traditional occurrence / formula context:** "
            f"{'; '.join(record['material']['traditional_occurrence_or_formula_context'])}",
            "- **Free exposure by compartment:**",
        ]
        for exposure in record["free_exposure"]:
            lines.append(
                f"  - {exposure['compartment']}: {exposure['status']}; "
                f"weaknesses = {', '.join(exposure['relevant_weaknesses'])}"
            )
        controls = record["intestinal_controls"]
        lines += [
            f"- **Intestinal controls:** general barrier evidence = "
            f"{controls['general_barrier_evidence']}; direct-flux barrier control = "
            f"{controls['direct_flux_assay_barrier_control']}; direct-flux viability "
            f"control = {controls['direct_flux_assay_viability_control']}",
            f"- **Intestinal-control boundary:** {controls['boundary']}",
            f"- **Attribution boundary:** {record['attribution_boundary']}",
            "- **Observations:**",
        ]
        for observation in record["mechanism_observations"]:
            lines.append(
                f"  - {observation['mechanism_id']} — "
                f"{observation['target_or_endpoint']}: "
                f"{observation['effect_polarity']}; {observation['endpoint_kind']}; "
                f"{observation['compartment']}; "
                f"{observation['measurement_directness']}; "
                f"{observation['target_attribution']}; weaknesses = "
                f"{', '.join(observation['relevant_weaknesses'])}; effect scope = "
                f"{observation['effect_scope']}"
            )
        lines.append("- **Mechanism-function evidence by weakness:**")
        if record["mechanism_function_evidence"]:
            for function_entry in record["mechanism_function_evidence"]:
                lines.append(
                    f"  - {function_entry['weakness']}: "
                    f"{function_entry['status']}; {function_entry['boundary']}"
                )
        else:
            lines.append("  - not applicable to the declared non-mechanistic endpoint")
        gap_text = "; ".join(
            f"{gap['flag']} — {gap['reason']}" for gap in record["gap_assessment"]
        )
        deferred = ", ".join(record["deferred_gap_flags"]) or "none"
        lines += [
            f"- **All detected gaps:** {gap_text or 'none'}",
            f"- **Selected next route:** {record['disposition']}",
            f"- **Selected gap:** {record['selected_gap_flag'] or 'none'}",
            f"- **Deferred gaps retained:** {deferred}",
            f"- **Weaknesses lacking direct target attribution:** "
            f"{', '.join(record['missing_target_attribution_weaknesses']) or 'none'}",
            "",
        ]
    lines += [
        "A missing measurement is not evidence that a material is ineffective. An",
        "animal or formula-level phenotype does not by itself establish a component,",
        "causal target, human effect, exposure, or delivery route.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    evidence_set, source_records = load_records()
    qualified_records = []
    for source_record in source_records:
        gaps = collect_gaps(source_record)
        gap_flags = {gap["flag"] for gap in gaps}
        missing_target_weaknesses = missing_target_attribution_weaknesses(
            source_record
        )
        disposition, selected_gap, deferred = select_disposition(
            source_record, gap_flags
        )
        verify_preregistered_outcome(
            str(source_record["record_id"]),
            disposition,
            gap_flags,
            set(deferred),
            missing_target_weaknesses,
        )
        qualified_records.append(
            {
                **source_record,
                "gap_assessment": gaps,
                "disposition": disposition,
                "selected_gap_flag": selected_gap,
                "deferred_gap_flags": deferred,
                "missing_target_attribution_weaknesses": sorted(
                    missing_target_weaknesses
                ),
                "rank_allowed": False,
                "dose_or_delivery_inference_allowed": False,
            }
        )
    result = {
        "schema_version": 2,
        "experiment": "comp-049",
        "title": "TCM urate-axis evidence qualification",
        "evidence_set": evidence_set,
        "decision_rule": (
            "Emit every independently detected gap, then select one next route by the "
            "preregistered priority while retaining all deferred gaps."
        ),
        "records": qualified_records,
        "forbidden_outputs": [
            "compound or formula rank",
            "viability label",
            "target occupancy or percent inhibition",
            "dose feasibility",
            "clinical-risk tier",
            "delivery or production recommendation",
            "clinical efficacy inference",
        ],
    }
    OUTPUTS.mkdir(exist_ok=True)
    (OUTPUTS / "evidence_qualification.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (OUTPUTS / "summary.md").write_text(
        render_summary(result), encoding="utf-8"
    )
    print("comp-049 complete. Evidence qualification outputs written to outputs/.")


if __name__ == "__main__":
    main()
