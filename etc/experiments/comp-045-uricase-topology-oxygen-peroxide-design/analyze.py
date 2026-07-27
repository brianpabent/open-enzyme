#!/usr/bin/env python3
"""comp-045: exact-configuration evidence matrix and candidate plate layout."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INPUT_PATH = ROOT / "inputs" / "design_factors.json"
OUTPUT_DIR = ROOT / "outputs"
ALLOWED_MODULES = {
    "katg",
    "vhb",
    "secreted_compartment_catalase",
    "surface_compartment_catalase",
}
REQUIRED_ROOT_KEYS = {
    "schema_version",
    "output_schema_version",
    "output_migration",
    "purpose",
    "topologies",
    "exact_configuration_precedents",
    "related_configuration_precedents",
    "configurations",
    "configuration_blocks",
    "allowed_repeated_comparator_ids",
    "planned_contrasts",
    "oxygen_contexts",
    "urate_concentrations",
    "biological_runs",
    "layout_seed",
    "shared_anchors_per_plate",
    "control_policy",
    "sampling_contract",
    "wet_lab_readiness",
    "primary_readouts",
    "state_vocabulary",
}


def fail(message: str) -> None:
    raise ValueError(message)


def require_unique(values: list[str], label: str) -> None:
    if len(values) != len(set(values)):
        fail(f"{label} must be unique")


def module_signature(modules: list[str]) -> tuple[str, ...]:
    if not isinstance(modules, list) or any(not isinstance(x, str) for x in modules):
        fail("modules must be a list of strings")
    require_unique(modules, "modules within a configuration")
    unknown = set(modules) - ALLOWED_MODULES
    if unknown:
        fail(f"unknown modules: {sorted(unknown)}")
    return tuple(sorted(modules))


def validate_and_index(parameters: dict) -> dict:
    missing = REQUIRED_ROOT_KEYS - set(parameters)
    if missing:
        fail(f"missing root keys: {sorted(missing)}")

    if parameters["schema_version"] != 2 or parameters["output_schema_version"] != 2:
        fail("input and output schema versions must both be 2")
    if not isinstance(parameters["output_migration"], str) or not parameters["output_migration"]:
        fail("output_migration must describe the replaced historical schema")

    vocabulary = parameters["state_vocabulary"]
    expected_vocabulary_values = {
        "topology_activity_evidence": {
            "direct_activity_precedent_at_250_uM",
            "no_direct_uox_precedent",
        },
        "localization_evidence": {
            "published_intracellular_configuration",
            "supernatant_associated_activity_precedent",
            "fusion_and_whole_cell_activity_reported_surface_accessibility_not_directly_assayed",
            "proposed_novel_configuration",
        },
        "source_relationship": {
            "exact_pulse_configuration",
            "related_intracellular_configuration",
        },
        "evidence_tier": {"In Vitro"},
        "exact_comparison_type": {
            "activity_configuration_at_250_uM",
            "joint_module_vs_no_joint_module_at_250_uM",
        },
        "related_comparison_type": {
            "related_activity_configuration",
            "related_joint_module_vs_no_joint_module",
        },
        "urate_role": {
            "matched_no_urate_control",
            "direct_human_terminal_ileum_prior_not_tested_in_published_uox_configurations",
            "sensitivity_scenario_not_evidence",
            "lowest_published_pulse_topology_assay_concentration",
        },
        "anchor_role": {
            "chassis_control",
            "cross_plate_anchor_not_source_positive_control",
            "assay_blank",
        },
        "configuration_precedent": {
            "direct_exact_configuration_precedent",
            "proposed_configuration_from_published_topology",
            "no_direct_uox_precedent",
        },
        "component_attribution": {
            "not_applicable",
            "proposed_isolation_test_from_joint_module_precedent",
            "direct_joint_module_effect_component_attribution_unresolved",
            "proposed_novel_module_configuration",
        },
        "peroxide_reaction_site_status": {
            "peroxide_closure_not_measured",
            "intracellular_alignment_by_design_empirical_closure_unresolved",
            "intracellular_katg_not_at_extracellular_uox_reaction_site",
            "proposed_reaction_site_aligned_configuration",
            "native_intracellular_background_not_a_tested_secreted_uox_closure",
        },
        "oxygen_status": {
            "oxygen_sufficiency_not_established",
            "proposed_vhb_isolation_test_from_joint_module_precedent",
            "joint_katg_vhb_observation_oxygen_component_attribution_unresolved",
            "proposed_vhb_contrast_within_novel_module_background",
        },
        "source_regime_match": {
            "not_exactly_matched_wet_lab_do_target_must_be_predeclared",
        },
    }
    if set(vocabulary) != set(expected_vocabulary_values):
        fail("state_vocabulary keys do not match all load-bearing categorical fields")
    for axis, states in vocabulary.items():
        if not states or any(not isinstance(state, str) for state in states):
            fail(f"invalid state vocabulary for {axis}")
        require_unique(states, f"states for {axis}")
        if set(states) != expected_vocabulary_values[axis]:
            fail(f"state vocabulary changed without preregistration: {axis}")

    topologies = parameters["topologies"]
    topology_ids = [row["id"] for row in topologies]
    require_unique(topology_ids, "topology ids")
    topology_by_id = {row["id"]: row for row in topologies}
    allowed_locations = {
        "cytoplasm",
        "extracellular_bulk",
        "outer_surface_candidate",
        "extracellular_bulk_candidate",
    }
    expected_topology_contracts = {
        "pulse_intracellular_ygfu": {
            "chassis": "EcN",
            "uox_location": "cytoplasm",
            "catalytic_substrate_access": "ygfu_import_required",
            "regulatory_sensor_uses_ygfu": True,
            "topology_activity_evidence": "direct_activity_precedent_at_250_uM",
            "localization_evidence": "published_intracellular_configuration",
        },
        "pulse_lamb_secreted": {
            "chassis": "EcN",
            "uox_location": "extracellular_bulk",
            "catalytic_substrate_access": "no_importer_required_for_extracellular_catalysis",
            "regulatory_sensor_uses_ygfu": True,
            "topology_activity_evidence": "direct_activity_precedent_at_250_uM",
            "localization_evidence": "supernatant_associated_activity_precedent",
        },
        "pulse_inakn_display": {
            "chassis": "EcN",
            "uox_location": "outer_surface_candidate",
            "catalytic_substrate_access": "no_importer_required_if_surface_accessible",
            "regulatory_sensor_uses_ygfu": True,
            "topology_activity_evidence": "direct_activity_precedent_at_250_uM",
            "localization_evidence": "fusion_and_whole_cell_activity_reported_surface_accessibility_not_directly_assayed",
        },
        "koji_secreted_candidate": {
            "chassis": "A_oryzae",
            "uox_location": "extracellular_bulk_candidate",
            "catalytic_substrate_access": "no_importer_required_if_active_uox_is_secreted",
            "regulatory_sensor_uses_ygfu": False,
            "topology_activity_evidence": "no_direct_uox_precedent",
            "localization_evidence": "proposed_novel_configuration",
        },
    }
    if set(topology_ids) != set(expected_topology_contracts):
        fail("topology ids do not match the preregistered set")
    for topology in topologies:
        if topology["uox_location"] not in allowed_locations:
            fail(f"unknown UOX location in {topology['id']}")
        if not isinstance(topology["regulatory_sensor_uses_ygfu"], bool):
            fail(f"regulatory_sensor_uses_ygfu must be boolean in {topology['id']}")
        for field in ("catalytic_substrate_access",):
            if not isinstance(topology[field], str) or not topology[field]:
                fail(f"{field} must be a nonempty string in {topology['id']}")
        if topology["topology_activity_evidence"] not in vocabulary["topology_activity_evidence"]:
            fail(f"unknown topology activity evidence in {topology['id']}")
        if topology["localization_evidence"] not in vocabulary["localization_evidence"]:
            fail(f"unknown localization evidence in {topology['id']}")
        observed_contract = {
            key: topology[key] for key in expected_topology_contracts[topology["id"]]
        }
        if observed_contract != expected_topology_contracts[topology["id"]]:
            fail(f"topology contract changed without preregistration: {topology['id']}")

    configurations = parameters["configurations"]
    configuration_ids = [row["id"] for row in configurations]
    require_unique(configuration_ids, "configuration ids")
    configuration_by_id = {row["id"]: row for row in configurations}
    configuration_signatures: set[tuple[str, tuple[str, ...]]] = set()
    for configuration in configurations:
        topology_id = configuration["topology"]
        if topology_id not in topology_by_id:
            fail(f"unknown topology in {configuration['id']}")
        signature = module_signature(configuration["modules"])
        combined_signature = (topology_id, signature)
        if combined_signature in configuration_signatures:
            fail(f"duplicate physical configuration: {combined_signature}")
        configuration_signatures.add(combined_signature)

        location = topology_by_id[topology_id]["uox_location"]
        chassis = topology_by_id[topology_id]["chassis"]
        if chassis != "EcN" and ({"katg", "vhb"} & set(signature)):
            fail(f"EcN support module assigned outside EcN in {configuration['id']}")
        if "secreted_compartment_catalase" in signature and location not in {
            "extracellular_bulk",
            "extracellular_bulk_candidate",
        }:
            fail(f"secreted catalase is incompatible with {configuration['id']}")
        if "surface_compartment_catalase" in signature and location != "outer_surface_candidate":
            fail(f"surface catalase is incompatible with {configuration['id']}")

    precedents = parameters["exact_configuration_precedents"]
    precedent_by_signature = {}
    exact_source_ids = []
    expected_exact_sources = {
        ("pulse_intracellular_ygfu", ()): "gao_2025_pulse_baseline_intracellular",
        ("pulse_intracellular_ygfu", ("katg", "vhb")): "gao_2025_pulse_intracellular_kv",
        ("pulse_lamb_secreted", ()): "gao_2025_pulse_baseline_lamb",
        ("pulse_lamb_secreted", ("katg", "vhb")): "gao_2025_pulse_lamb_kv",
        ("pulse_inakn_display", ()): "gao_2025_pulse_baseline_inakn",
        ("pulse_inakn_display", ("katg", "vhb")): "gao_2025_pulse_inakn_kv",
    }
    for precedent in precedents:
        topology_id = precedent["topology"]
        if topology_id not in topology_by_id:
            fail("exact precedent references an unknown topology")
        signature = (topology_id, module_signature(precedent["modules"]))
        if signature in precedent_by_signature:
            fail(f"duplicate exact precedent signature: {signature}")
        if signature not in configuration_signatures:
            fail(f"exact precedent has no planned configuration: {signature}")
        exact_source_ids.append(precedent["source_id"])
        if expected_exact_sources.get(signature) != precedent["source_id"]:
            fail(f"exact precedent source does not match the preregistered signature: {signature}")
        if precedent["source_relationship"] != "exact_pulse_configuration":
            fail(f"non-exact source in exact precedent table: {signature}")
        if precedent["source_relationship"] not in vocabulary["source_relationship"]:
            fail(f"unknown source relationship in exact precedent: {signature}")
        if precedent["evidence_tier"] not in vocabulary["evidence_tier"]:
            fail(f"unknown evidence tier in exact precedent: {signature}")
        if precedent["comparison_type"] not in vocabulary["exact_comparison_type"]:
            fail(f"unknown exact comparison type: {signature}")
        context = precedent["source_context"]
        if context != {
            "urate_uM": 250.0,
            "oxygen": "filled_sealed_tubes_without_reported_do_target",
        }:
            fail(f"exact PULSE source context is not the frozen 250 uM context: {signature}")
        if precedent["comparison_type"] == "joint_module_vs_no_joint_module_at_250_uM":
            if signature[1] != ("katg", "vhb"):
                fail(f"joint comparison lacks the joint module signature: {signature}")
            if module_signature(precedent["comparator_modules"]) != ():
                fail(f"joint comparison must use the no-module comparator: {signature}")
            if (topology_id, ()) not in configuration_signatures:
                fail(f"joint comparison lacks a planned no-module comparator: {signature}")
        elif precedent["comparator_modules"] is not None:
            fail(f"activity-only exact precedent must not invent a comparator: {signature}")
        precedent_by_signature[signature] = precedent
    require_unique(exact_source_ids, "exact precedent source ids")
    if set(precedent_by_signature) != set(expected_exact_sources):
        fail("exact precedent signatures do not match the preregistered set")

    related_precedents = parameters["related_configuration_precedents"]
    related_source_ids = []
    related_by_signature: dict[tuple[str, tuple[str, ...]], list[dict]] = {}
    expected_related_sources = {
        ("pulse_intracellular_ygfu", ()): "li_2023_puclm_ygfu_related_intracellular",
        ("pulse_intracellular_ygfu", ("katg", "vhb")): "zhao_2022_related_intracellular_joint_katg_vhb",
    }
    for precedent in related_precedents:
        topology_id = precedent["planned_topology"]
        if topology_id not in topology_by_id:
            fail("related precedent references an unknown planned topology")
        signature = (topology_id, module_signature(precedent["modules"]))
        related_source_ids.append(precedent["source_id"])
        if expected_related_sources.get(signature) != precedent["source_id"]:
            fail(f"related precedent source does not match the preregistered signature: {signature}")
        if precedent["source_relationship"] != "related_intracellular_configuration":
            fail("related precedent is not labeled as related")
        if precedent["source_relationship"] not in vocabulary["source_relationship"]:
            fail("unknown related source relationship")
        if precedent["evidence_tier"] not in vocabulary["evidence_tier"]:
            fail("unknown related evidence tier")
        if precedent["comparison_type"] not in vocabulary["related_comparison_type"]:
            fail("unknown related comparison type")
        if not isinstance(precedent["relationship_limit"], str) or not precedent["relationship_limit"]:
            fail("related precedent lacks its relationship limit")
        related_by_signature.setdefault(signature, []).append(precedent)
    require_unique(related_source_ids, "related precedent source ids")
    if set(related_by_signature) != set(expected_related_sources):
        fail("related precedent signatures do not match the preregistered set")
    if set(exact_source_ids) & set(related_source_ids):
        fail("a source cannot be both exact and related")

    blocks = parameters["configuration_blocks"]
    block_ids = [row["id"] for row in blocks]
    require_unique(block_ids, "configuration block ids")
    block_by_id = {row["id"]: row for row in blocks}
    for block in blocks:
        require_unique(block["configuration_ids"], f"configuration ids in {block['id']}")
        unknown = set(block["configuration_ids"]) - set(configuration_ids)
        if unknown:
            fail(f"unknown configurations in {block['id']}: {sorted(unknown)}")
    blocked_ids = [value for block in blocks for value in block["configuration_ids"]]
    if set(blocked_ids) != set(configuration_ids):
        fail("configuration blocks must cover every configuration")
    if len({len(block["configuration_ids"]) for block in blocks}) != 1:
        fail("configuration blocks must be equal in size")
    block_counts = Counter(blocked_ids)
    allowed_repeats = parameters["allowed_repeated_comparator_ids"]
    require_unique(allowed_repeats, "allowed repeated comparator ids")
    if not set(allowed_repeats) <= set(configuration_ids):
        fail("allowed repeated comparators include an unknown configuration")
    actual_repeats = {key for key, count in block_counts.items() if count > 1}
    if actual_repeats != set(allowed_repeats):
        fail("only declared comparator configurations may repeat across blocks")
    if any(count != 2 for key, count in block_counts.items() if key in allowed_repeats):
        fail("each declared repeated comparator must appear in exactly two blocks")
    if any(count != 1 for key, count in block_counts.items() if key not in allowed_repeats):
        fail("non-comparator configurations must appear in exactly one block")

    contrasts = parameters["planned_contrasts"]
    contrast_ids = [row["id"] for row in contrasts]
    require_unique(contrast_ids, "planned contrast ids")
    expected_contrasts = {
        "intracellular_katg_isolation": (
            "intracellular_katg_only",
            "intracellular_no_support",
            "block_a",
        ),
        "intracellular_vhb_isolation": (
            "intracellular_vhb_only",
            "intracellular_no_support",
            "block_a",
        ),
        "intracellular_joint_module": (
            "intracellular_katg_vhb",
            "intracellular_no_support",
            "block_a",
        ),
        "lamb_katg_isolation": (
            "lamb_katg_only",
            "lamb_no_support",
            "block_a",
        ),
        "lamb_vhb_isolation": (
            "lamb_vhb_only",
            "lamb_no_support",
            "block_a",
        ),
        "lamb_joint_module": (
            "lamb_katg_vhb",
            "lamb_no_support",
            "block_a",
        ),
        "lamb_reaction_site_catalase": (
            "lamb_compartment_catalase_only",
            "lamb_no_support",
            "block_b",
        ),
        "lamb_reaction_site_catalase_with_vhb": (
            "lamb_compartment_catalase_vhb",
            "lamb_vhb_only",
            "block_b",
        ),
        "inakn_katg_isolation": (
            "inakn_katg_only",
            "inakn_no_support",
            "block_b",
        ),
        "inakn_vhb_isolation": (
            "inakn_vhb_only",
            "inakn_no_support",
            "block_b",
        ),
        "inakn_joint_module": (
            "inakn_katg_vhb",
            "inakn_no_support",
            "block_b",
        ),
        "inakn_reaction_site_catalase": (
            "inakn_compartment_catalase_only",
            "inakn_no_support",
            "block_b",
        ),
        "inakn_reaction_site_catalase_with_vhb": (
            "inakn_compartment_catalase_vhb",
            "inakn_vhb_only",
            "block_b",
        ),
        "koji_reaction_site_catalase": (
            "koji_compartment_catalase",
            "koji_no_engineered_support",
            "block_a",
        ),
    }
    observed_contrasts = {
        row["id"]: (row["test"], row["comparator"], row["required_block"])
        for row in contrasts
    }
    if observed_contrasts != expected_contrasts:
        fail("planned contrast mapping changed without preregistration")
    for contrast in contrasts:
        if contrast["test"] not in configuration_by_id:
            fail(f"unknown test configuration in contrast {contrast['id']}")
        if contrast["comparator"] not in configuration_by_id:
            fail(f"unknown comparator in contrast {contrast['id']}")
        required_block = contrast["required_block"]
        if required_block not in block_by_id:
            fail(f"unknown required block in contrast {contrast['id']}")
        members = set(block_by_id[required_block]["configuration_ids"])
        if not {contrast["test"], contrast["comparator"]} <= members:
            fail(f"contrast is not within one declared block: {contrast['id']}")

    oxygen_contexts = parameters["oxygen_contexts"]
    oxygen_ids = [row["id"] for row in oxygen_contexts]
    require_unique(oxygen_ids, "oxygen context ids")
    if set(oxygen_ids) != {"microoxic_screen", "oxic_screen"}:
        fail("oxygen contexts must be the preregistered microoxic and oxic screens")
    expected_oxygen_definitions = {
        "microoxic_screen": "wet-lab dissolved-oxygen target must be predeclared and measured; PULSE and Zhao do not supply one interchangeable microoxic regime",
        "oxic_screen": "wet-lab dissolved-oxygen target must be predeclared and measured; an oxic label does not establish oxygen sufficiency",
    }
    for context in oxygen_contexts:
        if not isinstance(context["definition"], str) or not context["definition"]:
            fail(f"oxygen context lacks a definition: {context['id']}")
        if context["definition"] != expected_oxygen_definitions[context["id"]]:
            fail(f"oxygen context definition changed without preregistration: {context['id']}")

    concentrations = parameters["urate_concentrations"]
    values = [row["uM"] for row in concentrations]
    if any(not isinstance(value, (int, float)) or value < 0 for value in values):
        fail("urate concentrations must be nonnegative numbers")
    if len(values) != len(set(values)):
        fail("urate concentrations must be unique")
    expected_concentrations = {
        0.0: "matched_no_urate_control",
        0.59: "direct_human_terminal_ileum_prior_not_tested_in_published_uox_configurations",
        50.0: "sensitivity_scenario_not_evidence",
        250.0: "lowest_published_pulse_topology_assay_concentration",
    }
    if {row["uM"]: row["role"] for row in concentrations} != expected_concentrations:
        fail("urate concentration values and roles do not match the preregistered set")
    if any(row["role"] not in vocabulary["urate_role"] for row in concentrations):
        fail("unknown urate concentration role")

    if not isinstance(parameters["biological_runs"], int) or parameters["biological_runs"] < 1:
        fail("biological_runs must be a positive integer")
    if not isinstance(parameters["layout_seed"], str) or not parameters["layout_seed"]:
        fail("layout_seed must be a nonempty string")

    anchors = parameters["shared_anchors_per_plate"]
    anchor_ids = [row["id"] for row in anchors]
    require_unique(anchor_ids, "shared anchor ids")
    expected_anchor_contracts = {
        "unengineered_ecn": {
            "role": "chassis_control",
            "physical_definition": "parental EcN 1917; exact stock identity must be bound before wet-lab execution",
        },
        "unengineered_koji": {
            "role": "chassis_control",
            "physical_definition": "parental A. oryzae; exact strain and stock identity must be bound before wet-lab execution",
        },
        "pulse_kv_three_topology_mixture": {
            "role": "cross_plate_anchor_not_source_positive_control",
            "physical_definition": "equal-cell mixture of the exact intracellular, LamB, and InaK-N PULSE joint KatG+VHb configurations; exact stocks and cell normalization must be bound before wet-lab execution",
        },
        "medium_blank": {
            "role": "assay_blank",
            "physical_definition": "assay medium without cells; exact medium must be bound before wet-lab execution",
        },
    }
    if set(anchor_ids) != set(expected_anchor_contracts):
        fail("shared anchor ids do not match the preregistered set")
    for anchor in anchors:
        if anchor["role"] not in vocabulary["anchor_role"]:
            fail(f"unknown anchor role in {anchor['id']}")
        if not isinstance(anchor["physical_definition"], str) or not anchor["physical_definition"]:
            fail(f"anchor lacks a physical definition: {anchor['id']}")
        observed = {
            "role": anchor["role"],
            "physical_definition": anchor["physical_definition"],
        }
        if observed != expected_anchor_contracts[anchor["id"]]:
            fail(f"anchor contract changed without preregistration: {anchor['id']}")

    expected_control_policy = {
        "factorial_control_type": "inactive_uox_expression_and_localization_matched",
        "factorial_control_scope": "each active-UOX configuration is paired with the same support modules and a qualified inactive UOX at every urate concentration, including zero",
        "inactive_uox_identity_status": "unresolved_exact_mutation_and_expression_localization_equivalence_block_wet_lab_execution",
        "plate_anchor_scope": "all four shared anchors appear at every urate concentration on every plate",
        "source_benchmark_boundary": "250 uM is a PULSE topology assay concentration; the mixed-cell anchor is not a published in-vitro positive control",
    }
    if parameters["control_policy"] != expected_control_policy:
        fail("control_policy does not exactly match the preregistered contract")

    expected_sampling_contract = {
        "culture_unit": "one culture well per configuration, UOX state, concentration, biological run, oxygen context, and block assignment",
        "timepoint_status": "unresolved_predeclared_sampling_times_required_before_wet_lab_execution",
        "assay_compatibility_status": "unresolved_same_well_aliquot_or_separate_plate_plan_required_before_wet_lab_execution",
    }
    if parameters["sampling_contract"] != expected_sampling_contract:
        fail("sampling_contract does not exactly match the preregistered contract")

    readiness = parameters["wet_lab_readiness"]
    if readiness["status"] != "BLOCKED_PENDING_EXACT_CONTROL_AND_SAMPLING_QUALIFICATION":
        fail("wet-lab readiness must remain blocked at this design stage")
    expected_readiness_blockers = {
        "exact active and inactive UOX construct identities and matched expression/localization criteria",
        "active-UOX retained-activity qualification for every exact configuration",
        "exact KatG and VHb support-module constructs and their expression and retained-function qualification",
        "exact reaction-site-catalase construction, retained activity, localization, and co-secretion or co-display compatibility",
        "exact chassis and PULSE-mixture stock identities and cell normalization",
        "dissolved-oxygen targets",
        "sampling times, well volume, aliquoting, and destructive-assay compatibility",
        "assay sensitivity and quantification limits at the 0.59 uM terminal-ileum prior",
    }
    if set(readiness["blockers"]) != expected_readiness_blockers:
        fail("wet-lab blockers do not match the complete preregistered set")
    require_unique(readiness["blockers"], "wet-lab readiness blockers")

    expected_readouts = {
        "urate",
        "allantoin_or_pathway_product",
        "hydrogen_peroxide",
        "dissolved_oxygen",
        "viability",
        "uox_localization",
    }
    if set(parameters["primary_readouts"]) != expected_readouts:
        fail("primary readouts do not match the preregistered set")
    require_unique(parameters["primary_readouts"], "primary readouts")

    return {
        "topology_by_id": topology_by_id,
        "configuration_by_id": configuration_by_id,
        "precedent_by_signature": precedent_by_signature,
        "related_by_signature": related_by_signature,
        "block_by_id": block_by_id,
    }


def grade_configuration(configuration: dict, indexes: dict) -> dict:
    topology = indexes["topology_by_id"][configuration["topology"]]
    modules = set(configuration["modules"])
    signature = (configuration["topology"], tuple(sorted(modules)))
    precedent = indexes["precedent_by_signature"].get(signature)

    if precedent is not None:
        configuration_precedent = "direct_exact_configuration_precedent"
    elif topology["topology_activity_evidence"] == "no_direct_uox_precedent":
        configuration_precedent = "no_direct_uox_precedent"
    else:
        configuration_precedent = "proposed_configuration_from_published_topology"

    if not modules:
        component_attribution = "not_applicable"
    elif modules in ({"katg"}, {"vhb"}):
        component_attribution = "proposed_isolation_test_from_joint_module_precedent"
    elif (
        modules == {"katg", "vhb"}
        and precedent is not None
        and precedent["comparison_type"] == "joint_module_vs_no_joint_module_at_250_uM"
        and precedent["comparator_modules"] == []
    ):
        component_attribution = "direct_joint_module_effect_component_attribution_unresolved"
    else:
        component_attribution = "proposed_novel_module_configuration"

    location = topology["uox_location"]
    if "secreted_compartment_catalase" in modules or "surface_compartment_catalase" in modules:
        peroxide_status = "proposed_reaction_site_aligned_configuration"
    elif topology["chassis"] == "A_oryzae":
        peroxide_status = "native_intracellular_background_not_a_tested_secreted_uox_closure"
    elif location == "cytoplasm" and "katg" in modules:
        peroxide_status = "intracellular_alignment_by_design_empirical_closure_unresolved"
    elif location != "cytoplasm" and "katg" in modules:
        peroxide_status = "intracellular_katg_not_at_extracellular_uox_reaction_site"
    else:
        peroxide_status = "peroxide_closure_not_measured"

    return {
        "configuration_precedent": configuration_precedent,
        "component_attribution": component_attribution,
        "peroxide_reaction_site_status": peroxide_status,
        "exact_precedent": precedent,
        "related_precedents": indexes["related_by_signature"].get(signature, []),
    }


def oxygen_status(configuration: dict, static_grade: dict) -> str:
    modules = set(configuration["modules"])
    if "vhb" not in modules:
        return "oxygen_sufficiency_not_established"
    if (
        modules == {"katg", "vhb"}
        and static_grade["configuration_precedent"] == "direct_exact_configuration_precedent"
    ):
        return "joint_katg_vhb_observation_oxygen_component_attribution_unresolved"
    if {
        "secreted_compartment_catalase",
        "surface_compartment_catalase",
    } & modules:
        return "proposed_vhb_contrast_within_novel_module_background"
    return "proposed_vhb_isolation_test_from_joint_module_precedent"


def validate_emitted_states(row: dict, vocabulary: dict) -> None:
    for axis in (
        "configuration_precedent",
        "component_attribution",
        "peroxide_reaction_site_status",
        "oxygen_status",
        "source_regime_match",
    ):
        if row[axis] not in vocabulary[axis]:
            fail(f"emitted state outside vocabulary: {axis}={row[axis]}")


def well_name(index: int) -> str:
    if not 0 <= index < 96:
        fail("well index outside a 96-well plate")
    return f"{'ABCDEFGH'[index // 12]}{index % 12 + 1}"


def allocation_key(seed: str, plate_key: str, sample_id: str) -> tuple[str, str]:
    payload = f"{seed}|{plate_key}|{sample_id}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest(), sample_id


def build_plate(
    parameters: dict,
    indexes: dict,
    block: dict,
    oxygen_context: dict,
    biological_run: int,
    plate_number: int,
) -> dict:
    samples = []
    for configuration_id in block["configuration_ids"]:
        configuration = indexes["configuration_by_id"][configuration_id]
        for uox_state in ("active_uox", "inactive_uox_matched_control"):
            for concentration in parameters["urate_concentrations"]:
                sample_id = (
                    f"factorial|{configuration_id}|{uox_state}|"
                    f"{concentration['uM']:g}_uM"
                )
                samples.append(
                    {
                        "sample_id": sample_id,
                        "kind": "factorial" if uox_state == "active_uox" else "matched_control",
                        "configuration_id": configuration_id,
                        "uox_state": uox_state,
                        "uox_control_definition": (
                            None
                            if uox_state == "active_uox"
                            else parameters["control_policy"]["factorial_control_type"]
                        ),
                        "uox_control_identity_status": (
                            None
                            if uox_state == "active_uox"
                            else parameters["control_policy"]["inactive_uox_identity_status"]
                        ),
                        "urate_uM": concentration["uM"],
                        "urate_role": concentration["role"],
                    }
                )

    for anchor in parameters["shared_anchors_per_plate"]:
        for concentration in parameters["urate_concentrations"]:
            sample_id = f"anchor|{anchor['id']}|{concentration['uM']:g}_uM"
            samples.append(
                {
                    "sample_id": sample_id,
                    "kind": "shared_anchor",
                    "anchor_id": anchor["id"],
                    "anchor_role": anchor["role"],
                    "anchor_physical_definition": anchor["physical_definition"],
                    "urate_uM": concentration["uM"],
                    "urate_role": concentration["role"],
                }
            )

    require_unique([row["sample_id"] for row in samples], "sample ids within a plate")
    if len(samples) > 96:
        fail(f"plate {plate_number} requires {len(samples)} wells")
    empty_count = 96 - len(samples)
    for index in range(1, empty_count + 1):
        samples.append(
            {
                "sample_id": f"empty|{index:02d}",
                "kind": "empty",
            }
        )

    plate_key = (
        f"run_{biological_run}|{oxygen_context['id']}|{block['id']}|plate_{plate_number}"
    )
    samples.sort(
        key=lambda row: allocation_key(
            parameters["layout_seed"],
            plate_key,
            row["sample_id"],
        )
    )
    wells = []
    for index, sample in enumerate(samples):
        wells.append({"well": well_name(index), **sample})

    return {
        "plate": plate_number,
        "biological_run": biological_run,
        "oxygen_context": oxygen_context["id"],
        "oxygen_context_definition": oxygen_context["definition"],
        "configuration_block": block["id"],
        "n_used_wells": 96 - empty_count,
        "n_empty_wells": empty_count,
        "wells": wells,
    }


def render_summary(results: dict, parameters: dict) -> str:
    precedent_counts = Counter(
        row["configuration_precedent"] for row in results["configuration_table"]
    )
    lines = [
        "# comp-045 summary — uricase topology × oxygen × peroxide",
        "",
        "**Design disposition: CANDIDATE_LAYOUT_GENERATED. Biological verdict: NOT_EVALUATED.**",
        "",
        "This computation validates an evidence vocabulary and generates a randomized candidate plate layout. It contains no biological measurements and therefore does not advance, eliminate, or rank a topology.",
        "",
        f"**Wet-lab readiness: {results['wet_lab_readiness']['status']}.** The layout is a blocked template until the listed control, stock, oxygen, and sampling identities are fixed and reviewed.",
        "",
        "## Evidence boundary",
        "",
        f"- {precedent_counts['direct_exact_configuration_precedent']} configurations reproduce exact published baseline or joint KatG+VHb construct signatures.",
        "- KatG-only and VHb-only rows are proposed isolation tests from joint-module precedent; neither component was isolated in the cited PULSE or Zhao comparisons.",
        "- The PULSE LamB and InaK-N joint constructs are direct whole-configuration precedents, but they do not establish extracellular reaction-site peroxide closure.",
        "- The koji-secreted UOX rows are proposed configurations without a cited direct UOX precedent.",
        "- The InaK-N fusion has whole-cell activity precedent; dedicated surface-accessibility localization was not reported.",
        "",
        "## Candidate layout",
        "",
        f"- {results['n_configurations']} unique physical configurations and {results['n_block_assignments']} block assignments in {results['n_configuration_blocks']} balanced blocks",
        f"- {results['n_planned_within_block_contrasts']} preregistered contrasts, each with its comparator on the same plate block",
        f"- {results['n_biological_runs']} biological runs × {results['n_oxygen_contexts']} oxygen contexts × {results['n_configuration_blocks']} blocks = {results['n_plates']} plates",
        f"- {results['used_wells_per_plate']} used and {results['empty_wells_per_plate']} empty wells per 96-well plate",
        "- Every active-UOX configuration has a planned support-module-matched inactive-UOX control at every urate concentration, including zero; the exact inactive mutation and equivalence criteria remain a wet-lab blocker.",
        "- All samples are allocated across the full plate by a stable SHA-256 key.",
        "",
        "## Urate roles",
        "",
    ]
    for concentration in parameters["urate_concentrations"]:
        lines.append(f"- {concentration['uM']:g} µM — `{concentration['role']}`")
    lines += [
        "",
        "## Wet-lab gates",
        "",
        "- Predeclare and measure the actual dissolved-oxygen target for each oxygen context; PULSE sealed-tube and Zhao ~15%-normal-DO conditions are not interchangeable.",
        "- Bind exact active/inactive constructs, expression/localization equivalence criteria, strain stocks, cell normalization, sampling times, and assay compatibility before wet-lab execution.",
        "- Interpret 250 µM as a published PULSE assay concentration, 0.59 µM as a terminal-ileal human-fluid prior not tested in the published UOX configurations, and 50 µM as sensitivity only.",
        "- The mixed PULSE-KV composition is a proposed cross-plate anchor, not a published in-vitro positive control.",
        "",
        "### Blocking qualifications",
        "",
    ]
    lines.extend(
        f"- {blocker}" for blocker in results["wet_lab_readiness"]["blockers"]
    )
    lines += [
        "",
        "## Required readouts",
        "",
    ]
    lines.extend(f"- {readout}" for readout in results["required_readouts"])
    lines += ["", "## Limitations", ""]
    lines.extend(f"- {limitation}" for limitation in results["limitations"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parameters = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    indexes = validate_and_index(parameters)

    configuration_table = []
    static_grades = {}
    for configuration in parameters["configurations"]:
        topology = indexes["topology_by_id"][configuration["topology"]]
        grade = grade_configuration(configuration, indexes)
        static_grades[configuration["id"]] = grade
        row = {
            "configuration_id": configuration["id"],
            "topology": configuration["topology"],
            "chassis": topology["chassis"],
            "uox_location": topology["uox_location"],
            "modules": sorted(configuration["modules"]),
            "catalytic_substrate_access": topology["catalytic_substrate_access"],
            "regulatory_sensor_uses_ygfu": topology["regulatory_sensor_uses_ygfu"],
            "topology_activity_evidence": topology["topology_activity_evidence"],
            "localization_evidence": topology["localization_evidence"],
            **grade,
        }
        configuration_table.append(row)

    evidence_matrix = []
    for configuration in parameters["configurations"]:
        for context in parameters["oxygen_contexts"]:
            grade = static_grades[configuration["id"]]
            row = {
                "configuration_id": configuration["id"],
                "oxygen_context": context["id"],
                "configuration_precedent": grade["configuration_precedent"],
                "component_attribution": grade["component_attribution"],
                "peroxide_reaction_site_status": grade["peroxide_reaction_site_status"],
                "oxygen_status": oxygen_status(configuration, grade),
                "source_regime_match": "not_exactly_matched_wet_lab_do_target_must_be_predeclared",
            }
            validate_emitted_states(row, parameters["state_vocabulary"])
            evidence_matrix.append(row)

    expected_matrix_rows = len(parameters["configurations"]) * len(
        parameters["oxygen_contexts"]
    )
    if len(evidence_matrix) != expected_matrix_rows:
        fail("evidence matrix is not one row per configuration and oxygen context")
    require_unique(
        [
            f"{row['configuration_id']}|{row['oxygen_context']}"
            for row in evidence_matrix
        ],
        "configuration and oxygen evidence keys",
    )

    plates = []
    plate_number = 0
    for biological_run in range(1, parameters["biological_runs"] + 1):
        for oxygen_context in parameters["oxygen_contexts"]:
            for block in parameters["configuration_blocks"]:
                plate_number += 1
                plates.append(
                    build_plate(
                        parameters,
                        indexes,
                        block,
                        oxygen_context,
                        biological_run,
                        plate_number,
                    )
                )

    used_well_counts = {plate["n_used_wells"] for plate in plates}
    empty_well_counts = {plate["n_empty_wells"] for plate in plates}
    if len(used_well_counts) != 1 or len(empty_well_counts) != 1:
        fail("all plates must use the same number of wells")

    results = {
        "schema_version": parameters["output_schema_version"],
        "schema_migration": parameters["output_migration"],
        "experiment": "comp-045",
        "artifact_type": "evidence_matrix_and_candidate_plate_layout",
        "design_disposition": "CANDIDATE_LAYOUT_GENERATED",
        "biological_verdict": "NOT_EVALUATED",
        "wet_lab_readiness": parameters["wet_lab_readiness"],
        "n_configurations": len(parameters["configurations"]),
        "n_block_assignments": sum(
            len(block["configuration_ids"])
            for block in parameters["configuration_blocks"]
        ),
        "n_configuration_blocks": len(parameters["configuration_blocks"]),
        "n_planned_within_block_contrasts": len(parameters["planned_contrasts"]),
        "n_oxygen_contexts": len(parameters["oxygen_contexts"]),
        "n_urate_concentrations_including_zero": len(
            parameters["urate_concentrations"]
        ),
        "n_biological_runs": parameters["biological_runs"],
        "n_plates": len(plates),
        "used_wells_per_plate": next(iter(used_well_counts)),
        "empty_wells_per_plate": next(iter(empty_well_counts)),
        "configuration_table": configuration_table,
        "evidence_matrix": evidence_matrix,
        "planned_contrasts": parameters["planned_contrasts"],
        "plate_maps": plates,
        "control_policy": parameters["control_policy"],
        "sampling_contract": parameters["sampling_contract"],
        "required_readouts": parameters["primary_readouts"],
        "limitations": [
            "The artifact contains no biological outcomes and cannot select or eliminate a topology.",
            "Published evidence applies to exact whole configurations and source regimes, not isolated KatG or VHb effects.",
            "A construct signature precedent does not establish activity at 0.59 or 50 uM or at a newly chosen dissolved-oxygen target.",
            "Proposed secreted and surface catalase modules require expression, localization, activity, and safety qualification.",
            "The candidate layout does not model expression burden, proteolysis, mucus residence, colonization, oxygen kinetics, or epithelial injury.",
            "Only the preregistered same-block contrasts are supported by the layout; other cross-block comparisons remain confounded with plate block.",
            "The inactive-UOX identities, sampling times, and assay multiplexing plan are intentionally unresolved and block wet-lab execution.",
        ],
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    result_text = json.dumps(results, indent=2, sort_keys=True) + "\n"
    (OUTPUT_DIR / "results.json").write_text(result_text, encoding="utf-8")
    (OUTPUT_DIR / "summary.md").write_text(
        render_summary(results, parameters),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
