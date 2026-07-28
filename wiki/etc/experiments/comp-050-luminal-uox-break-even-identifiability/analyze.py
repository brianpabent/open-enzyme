#!/usr/bin/env python3
"""Derive conditional luminal-UOX capacity and structural-identifiability maps."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "inputs" / "model_contract.json"
OUTPUTS = ROOT / "outputs"
getcontext().prec = 40


def q(value: str | int) -> Fraction:
    return Fraction(str(value))


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def fraction_decimal_text(value: Fraction) -> str:
    rendered = Decimal(value.numerator) / Decimal(value.denominator)
    return format(rendered, ".12g")


def require_unique_strings(values: object, label: str) -> list[str]:
    if not isinstance(values, list) or not values:
        raise ValueError(f"{label} must be a non-empty list")
    if not all(isinstance(value, str) and value for value in values):
        raise ValueError(f"{label} must contain non-empty strings")
    if len(values) != len(set(values)):
        raise ValueError(f"{label} must be unique")
    return values


def coefficient_vector(
    coefficients: object, unknown_index: dict[str, int], label: str
) -> list[Fraction]:
    if not isinstance(coefficients, dict) or not coefficients:
        raise ValueError(f"{label} must be a non-empty coefficient object")
    vector = [Fraction(0) for _ in unknown_index]
    for name, raw_value in coefficients.items():
        if name not in unknown_index:
            raise ValueError(f"{label} references unknown variable {name}")
        value = q(raw_value)
        if value == 0:
            raise ValueError(f"{label} contains a zero coefficient for {name}")
        vector[unknown_index[name]] = value
    return vector


def load_contract() -> tuple[dict, str]:
    raw = INPUT.read_bytes()
    contract = json.loads(raw)
    if contract.get("schema_version") != 2:
        raise ValueError("unsupported schema_version")
    if contract.get("python_minimum") != "3.11":
        raise ValueError("python_minimum must be 3.11")
    if sys.version_info < (3, 11):
        raise RuntimeError("comp-050 requires CPython 3.11 or newer")

    convention = contract.get("window_and_volume_convention")
    if not isinstance(convention, dict):
        raise ValueError("window_and_volume_convention must be an object")
    for key in (
        "window_duration_symbol",
        "ledger_basis",
        "concentration_conversion",
        "counterexample_volume",
    ):
        if not isinstance(convention.get(key), str) or not convention[key]:
            raise ValueError(f"window_and_volume_convention.{key} is required")

    surface = contract["response_surface"]
    if surface.get("denominator") != "mean_total_local_urate_influx":
        raise ValueError("response surface denominator must be mean total local influx")
    ratios = [q(x) for x in surface["substrate_to_km_ratios"]]
    time_areas = [q(x) for x in surface["active_capacity_time_area_fractions"]]
    targets = [q(x) for x in surface["gross_removal_target_fractions"]]
    if not ratios or any(value <= 0 for value in ratios):
        raise ValueError("substrate_to_km_ratios must be positive")
    if not time_areas or any(value <= 0 or value > 1 for value in time_areas):
        raise ValueError("active_capacity_time_area_fractions must be in (0,1]")
    if not targets or any(value <= 0 or value > 1 for value in targets):
        raise ValueError("gross_removal_target_fractions must be in (0,1]")
    if ratios != sorted(set(ratios)):
        raise ValueError("substrate_to_km_ratios must be unique and sorted")
    if time_areas != sorted(set(time_areas)):
        raise ValueError(
            "active_capacity_time_area_fractions must be unique and sorted"
        )
    if targets != sorted(set(targets)):
        raise ValueError("gross_removal_target_fractions must be unique and sorted")
    if Fraction(1) not in targets:
        raise ValueError("gross_removal_target_fractions must include one")

    examples = contract["same_concentration_counterexamples"]
    if examples.get("constant_volume") is not True:
        raise ValueError("counterexamples require constant_volume true")
    concentration = q(examples["concentration"])
    km = q(examples["km"])
    supply = q(examples["mean_total_local_influx_rate"])
    if concentration <= 0 or km <= 0 or supply <= 0:
        raise ValueError("counterexample concentration, Km, and influx must be positive")
    scenarios = examples.get("scenarios")
    if not isinstance(scenarios, list) or len(scenarios) < 2:
        raise ValueError("at least two counterexample scenarios are required")
    scenario_names = require_unique_strings(
        [scenario.get("name") for scenario in scenarios],
        "counterexample scenario names",
    )
    if len(scenario_names) != len(scenarios):
        raise ValueError("counterexample scenario names are incomplete")
    for scenario in scenarios:
        if q(scenario["active_uox_vmax"]) < 0:
            raise ValueError("counterexample active_uox_vmax must be nonnegative")
        if q(scenario["non_uox_first_order_loss_rate"]) < 0:
            raise ValueError(
                "counterexample non_uox_first_order_loss_rate must be nonnegative"
            )

    model = contract["identifiability_model"]
    unknowns = require_unique_strings(model.get("unknowns"), "identifiability unknowns")
    unknown_index = {name: index for index, name in enumerate(unknowns)}

    equations = model.get("governing_equations")
    if not isinstance(equations, list) or not equations:
        raise ValueError("governing_equations must be a non-empty list")
    require_unique_strings(
        [equation.get("name") for equation in equations],
        "governing equation names",
    )
    for equation in equations:
        coefficient_vector(
            equation.get("coefficients"),
            unknown_index,
            f"governing equation {equation.get('name')}",
        )

    product = contract["product_observation_contract"]
    conditional_variables = require_unique_strings(
        product.get("conditional_observations"),
        "product conditional observations",
    )
    if not set(conditional_variables).issubset(unknown_index):
        raise ValueError("product conditional observations must be model unknowns")
    if (
        product.get("status_in_this_comp")
        != "ideal_assumption_only_not_empirically_evaluated"
    ):
        raise ValueError("product observation status must remain ideal-assumption-only")
    if product.get("failure_sensitivity") != "remove_conditional_observation":
        raise ValueError("product failure sensitivity must remove observations")
    product_equations = product.get("equations")
    if (
        not isinstance(product_equations, dict)
        or set(product_equations)
        != {"total_uox_removal", "systemic_origin_uox_removal"}
        or not all(isinstance(value, str) and value for value in product_equations.values())
    ):
        raise ValueError("total and systemic-origin product observation equations are required")
    prerequisites = require_unique_strings(
        product.get("required_prerequisites"),
        "product observation prerequisites",
    )
    if len(prerequisites) < 7:
        raise ValueError("product observation prerequisites are incomplete")

    combinations = model.get("measurement_combinations")
    if not isinstance(combinations, list) or not combinations:
        raise ValueError("measurement_combinations must be a non-empty list")
    require_unique_strings(
        [combination.get("name") for combination in combinations],
        "measurement combination names",
    )
    prior_observations: set[str] = set()
    seen_conditional: set[str] = set()
    for expected_order, combination in enumerate(combinations, start=1):
        if combination.get("order") != expected_order:
            raise ValueError("measurement combination order must be consecutive")
        direct = combination.get("direct_observations")
        conditional = combination.get("conditional_observations")
        if not isinstance(direct, list) or not isinstance(conditional, list):
            raise ValueError("measurement observations must be lists")
        if len(direct) != len(set(direct)) or len(conditional) != len(set(conditional)):
            raise ValueError("observations within each measurement combination must be unique")
        if not set(direct).issubset(unknown_index):
            raise ValueError("direct observation references an unknown variable")
        if not set(conditional).issubset(conditional_variables):
            raise ValueError(
                "conditional observation is not governed by the product contract"
            )
        observations = set(direct) | set(conditional)
        if not prior_observations.issubset(observations):
            raise ValueError("measurement combinations must be cumulative")
        prior_observations = observations
        seen_conditional.update(conditional)
    if seen_conditional != set(conditional_variables):
        raise ValueError("every product conditional observation must be used")

    targets_config = model.get("targets")
    if not isinstance(targets_config, list) or not targets_config:
        raise ValueError("identifiability targets must be a non-empty list")
    require_unique_strings(
        [target.get("name") for target in targets_config],
        "identifiability target names",
    )
    for target in targets_config:
        has_coefficients = "coefficients" in target
        has_required = "requires_identifiable_variables" in target
        if has_coefficients == has_required:
            raise ValueError(
                "each target requires exactly one coefficient or grouped-variable rule"
            )
        if has_coefficients:
            coefficient_vector(
                target["coefficients"],
                unknown_index,
                f"target {target.get('name')}",
            )
        else:
            required = require_unique_strings(
                target["requires_identifiable_variables"],
                f"target {target.get('name')} required variables",
            )
            if not set(required).issubset(unknown_index):
                raise ValueError("grouped target references an unknown variable")

    return contract, hashlib.sha256(raw).hexdigest()


def break_even_rows(contract: dict) -> list[dict[str, str]]:
    surface = contract["response_surface"]
    rows: list[dict[str, str]] = []
    for ratio_raw in surface["substrate_to_km_ratios"]:
        ratio = q(ratio_raw)
        occupancy = ratio / (Fraction(1) + ratio)
        for area_raw in surface["active_capacity_time_area_fractions"]:
            area = q(area_raw)
            for target_raw in surface["gross_removal_target_fractions"]:
                target = q(target_raw)
                required = target / (occupancy * area)
                rows.append(
                    {
                        "substrate_to_km_ratio": fraction_decimal_text(ratio),
                        "substrate_occupancy_exact": fraction_text(occupancy),
                        "substrate_occupancy_decimal": fraction_decimal_text(occupancy),
                        "active_capacity_time_area_fraction": fraction_decimal_text(
                            area
                        ),
                        "gross_removal_target_fraction_of_total_local_influx": fraction_decimal_text(
                            target
                        ),
                        "required_capacity_multiple_exact": fraction_text(required),
                        "required_capacity_multiple_decimal": fraction_decimal_text(
                            required
                        ),
                        "boundary_type": (
                            "integrated_capacity_equals_total_local_influx"
                            if target == Fraction(1)
                            else "descriptive_partial_gross_removal_slice"
                        ),
                    }
                )
    return rows


def verify_surface_monotonicity(rows: list[dict[str, str]]) -> dict[str, bool]:
    indexed = {
        (
            q(row["substrate_to_km_ratio"]),
            q(row["active_capacity_time_area_fraction"]),
            q(row["gross_removal_target_fraction_of_total_local_influx"]),
        ): q(row["required_capacity_multiple_exact"])
        for row in rows
    }
    ratios = sorted({key[0] for key in indexed})
    areas = sorted({key[1] for key in indexed})
    targets = sorted({key[2] for key in indexed})
    return {
        "required_capacity_decreases_as_substrate_to_km_increases": all(
            indexed[(ratios[index + 1], area, target)]
            < indexed[(ratios[index], area, target)]
            for index in range(len(ratios) - 1)
            for area in areas
            for target in targets
        ),
        "required_capacity_decreases_as_active_time_area_increases": all(
            indexed[(ratio, areas[index + 1], target)]
            < indexed[(ratio, areas[index], target)]
            for ratio in ratios
            for index in range(len(areas) - 1)
            for target in targets
        ),
        "required_capacity_increases_as_gross_removal_target_increases": all(
            indexed[(ratio, area, targets[index + 1])]
            > indexed[(ratio, area, targets[index])]
            for ratio in ratios
            for area in areas
            for index in range(len(targets) - 1)
        ),
    }


def counterexample_rows(contract: dict) -> tuple[list[dict[str, str]], dict[str, bool]]:
    block = contract["same_concentration_counterexamples"]
    concentration = q(block["concentration"])
    km = q(block["km"])
    supply = q(block["mean_total_local_influx_rate"])
    rows: list[dict[str, str]] = []
    for scenario in block["scenarios"]:
        vmax = q(scenario["active_uox_vmax"])
        non_uox_loss = q(scenario["non_uox_first_order_loss_rate"])
        uox_flux = vmax * concentration / (km + concentration)
        non_uox_flux = non_uox_loss * concentration
        derivative = supply - uox_flux - non_uox_flux
        rows.append(
            {
                "scenario": scenario["name"],
                "constant_volume": "true",
                "concentration": fraction_decimal_text(concentration),
                "km": fraction_decimal_text(km),
                "mean_total_local_influx_rate": fraction_decimal_text(supply),
                "active_uox_vmax": fraction_decimal_text(vmax),
                "non_uox_first_order_loss_rate": fraction_decimal_text(non_uox_loss),
                "uox_attributed_product_equivalent_flux_exact": fraction_text(
                    uox_flux
                ),
                "uox_attributed_product_equivalent_flux_decimal": fraction_decimal_text(
                    uox_flux
                ),
                "non_uox_loss_flux_exact": fraction_text(non_uox_flux),
                "non_uox_loss_flux_decimal": fraction_decimal_text(non_uox_flux),
                "concentration_derivative_exact": fraction_text(derivative),
            }
        )
    derivatives_zero = all(
        q(row["concentration_derivative_exact"]) == 0 for row in rows
    )
    uox_fluxes = {
        q(row["uox_attributed_product_equivalent_flux_exact"]) for row in rows
    }
    return rows, {
        "constant_volume_declared": block["constant_volume"] is True,
        "all_concentration_derivatives_equal_zero": derivatives_zero,
        "uox_attributed_fluxes_are_not_identical": len(uox_fluxes) > 1,
    }


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def observation_row(variable: str, unknown_index: dict[str, int]) -> list[Fraction]:
    row = [Fraction(0) for _ in unknown_index]
    row[unknown_index[variable]] = Fraction(1)
    return row


def target_test(
    target: dict,
    matrix: list[list[Fraction]],
    unknown_index: dict[str, int],
) -> tuple[bool, list[int]]:
    base_rank = matrix_rank(matrix)
    if "coefficients" in target:
        test_vectors = [
            coefficient_vector(
                target["coefficients"],
                unknown_index,
                f"target {target['name']}",
            )
        ]
    else:
        test_vectors = [
            observation_row(variable, unknown_index)
            for variable in target["requires_identifiable_variables"]
        ]
    augmented_ranks = [matrix_rank(matrix + [vector]) for vector in test_vectors]
    return all(rank == base_rank for rank in augmented_ranks), augmented_ranks


def structural_audit(
    contract: dict, include_conditional_observations: bool
) -> tuple[list[dict[str, str]], list[dict]]:
    model = contract["identifiability_model"]
    unknowns = model["unknowns"]
    unknown_index = {name: index for index, name in enumerate(unknowns)}
    governing_rows = [
        coefficient_vector(
            equation["coefficients"],
            unknown_index,
            f"governing equation {equation['name']}",
        )
        for equation in model["governing_equations"]
    ]
    governing_names = [
        f"governing:{equation['name']}" for equation in model["governing_equations"]
    ]
    mode = (
        "ideal_product_observation"
        if include_conditional_observations
        else "product_prerequisites_failed"
    )
    csv_rows: list[dict[str, str]] = []
    details: list[dict] = []
    for combination in model["measurement_combinations"]:
        matrix = [row[:] for row in governing_rows]
        equation_names = governing_names[:]
        for variable in combination["direct_observations"]:
            matrix.append(observation_row(variable, unknown_index))
            equation_names.append(f"direct_observation:{variable}")
        if include_conditional_observations:
            for variable in combination["conditional_observations"]:
                matrix.append(observation_row(variable, unknown_index))
                equation_names.append(f"conditional_product_observation:{variable}")
        base_rank = matrix_rank(matrix)
        target_results = []
        for target in model["targets"]:
            identifiable, augmented_ranks = target_test(
                target, matrix, unknown_index
            )
            status = (
                "STRUCTURALLY_IDENTIFIABLE_UNDER_IDEAL_OBSERVATION"
                if identifiable and include_conditional_observations
                else (
                    "STRUCTURALLY_IDENTIFIABLE_WITHOUT_PRODUCT_OBSERVATION"
                    if identifiable
                    else "NOT_IDENTIFIABLE"
                )
            )
            csv_rows.append(
                {
                    "product_observation_mode": mode,
                    "measurement_order": str(combination["order"]),
                    "measurement_combination": combination["name"],
                    "target": target["name"],
                    "unknown_count": str(len(unknowns)),
                    "equation_count": str(len(matrix)),
                    "matrix_rank": str(base_rank),
                    "augmented_ranks": ";".join(
                        str(rank) for rank in augmented_ranks
                    ),
                    "status": status,
                }
            )
            target_results.append(
                {
                    "target": target["name"],
                    "status": status,
                    "augmented_ranks": augmented_ranks,
                }
            )
        details.append(
            {
                "order": combination["order"],
                "measurement_combination": combination["name"],
                "product_observation_mode": mode,
                "direct_observations": combination["direct_observations"],
                "conditional_observations_included": (
                    combination["conditional_observations"]
                    if include_conditional_observations
                    else []
                ),
                "equations": equation_names,
                "coefficient_matrix": [
                    [fraction_text(value) for value in row] for row in matrix
                ],
                "unknown_order": unknowns,
                "matrix_rank": base_rank,
                "targets": target_results,
            }
        )
    return csv_rows, details


def status_for(
    rows: list[dict[str, str]], combination: str, target: str
) -> str:
    matches = [
        row["status"]
        for row in rows
        if row["measurement_combination"] == combination and row["target"] == target
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one identifiability row for {combination}/{target}"
        )
    return matches[0]


def identifiability_checks(
    ideal_rows: list[dict[str, str]], failed_rows: list[dict[str, str]]
) -> dict[str, bool]:
    identified = "STRUCTURALLY_IDENTIFIABLE_UNDER_IDEAL_OBSERVATION"
    not_identified = "NOT_IDENTIFIABLE"
    return {
        "terminal_urate_alone_does_not_identify_local_uox_removal": status_for(
            ideal_rows, "terminal_urate_amount_only", "local_uox_removal"
        )
        == not_identified,
        "qualified_product_conditionally_identifies_local_uox_removal": status_for(
            ideal_rows,
            "inventory_plus_qualified_product_equivalent",
            "local_uox_removal",
        )
        == identified,
        "qualified_product_does_not_close_local_ledger": status_for(
            ideal_rows,
            "inventory_plus_qualified_product_equivalent",
            "local_ledger_closed",
        )
        == not_identified,
        "calibrated_capacity_combination_identifies_active_capacity": status_for(
            ideal_rows,
            "add_calibrated_reaction_site_capacity",
            "integrated_active_capacity",
        )
        == identified,
        "source_and_boundary_combination_closes_declared_ledger": status_for(
            ideal_rows, "add_source_and_boundary_fate", "local_ledger_closed"
        )
        == identified,
        "source_resolved_product_fate_identifies_systemic_origin_uox_removal": status_for(
            ideal_rows,
            "add_source_and_boundary_fate",
            "systemic_origin_uox_removal",
        )
        == identified,
        "product_failure_blocks_local_uox_attribution_in_every_combination": all(
            row["status"] == not_identified
            for row in failed_rows
            if row["target"] == "local_uox_removal"
        ),
        "product_failure_blocks_systemic_origin_uox_attribution": status_for(
            failed_rows,
            "add_source_and_boundary_fate",
            "systemic_origin_uox_removal",
        )
        == not_identified,
        "product_failure_prevents_declared_ledger_closure": status_for(
            failed_rows, "add_source_and_boundary_fate", "local_ledger_closed"
        )
        == not_identified,
    }


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError(f"no rows for {path.name}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    contract, contract_sha256 = load_contract()
    surface = break_even_rows(contract)
    surface_checks = verify_surface_monotonicity(surface)
    counterexamples, counterexample_checks = counterexample_rows(contract)
    ideal_rows, ideal_details = structural_audit(
        contract, include_conditional_observations=True
    )
    failed_rows, failed_details = structural_audit(
        contract, include_conditional_observations=False
    )
    measurement_checks = identifiability_checks(ideal_rows, failed_rows)
    checks = {
        **surface_checks,
        **counterexample_checks,
        **measurement_checks,
        "integrated_capacity_equals_influx_boundary_present": any(
            row["boundary_type"]
            == "integrated_capacity_equals_total_local_influx"
            for row in surface
        ),
    }
    algebra_ok = all(surface_checks.values()) and checks[
        "integrated_capacity_equals_influx_boundary_present"
    ]
    counterexample_ok = all(counterexample_checks.values())
    measurement_ok = all(measurement_checks.values())
    verdict = (
        "METHOD_MAP_DERIVED"
        if algebra_ok and counterexample_ok and measurement_ok
        else "METHOD_FAILURE"
    )
    method_statuses = {
        "conditional_capacity_algebra": (
            "DERIVED" if algebra_ok else "METHOD_FAILURE"
        ),
        "concentration_only_nonidentifiability": (
            "DEMONSTRATED" if counterexample_ok else "METHOD_FAILURE"
        ),
        "measurement_structural_audit": (
            "COMPLETED" if measurement_ok else "METHOD_FAILURE"
        ),
        "product_prerequisite_failure_sensitivity": (
            "PASSED"
            if measurement_checks[
                "product_failure_blocks_local_uox_attribution_in_every_combination"
            ]
            and measurement_checks[
                "product_failure_blocks_systemic_origin_uox_attribution"
            ]
            and measurement_checks[
                "product_failure_prevents_declared_ledger_closure"
            ]
            else "FAILED"
        ),
        "biological_regime": "NOT_EVALUATED",
    }
    results = {
        "schema_version": 2,
        "experiment": "comp-050",
        "contract_sha256": contract_sha256,
        "verdict": verdict,
        "method_statuses": method_statuses,
        "definitions": {
            "ledger_basis": contract["window_and_volume_convention"][
                "ledger_basis"
            ],
            "response_surface_denominator": contract["response_surface"][
                "denominator"
            ],
            "local_gross_removal_fraction": "R_UOX / (I_systemic + I_other)",
            "systemic_attributed_fraction": "R_UOX,systemic / I_systemic; requires source-resolved fate",
            "global_minimality_claim": False,
        },
        "equations": {
            "integrated_local_mass_balance": "U_T - U_0 = I_systemic + I_other - R_UOX - R_reabsorption - R_outflow - R_unattributed",
            "conditional_occupancy": "occupancy = (C/Km) / (1 + C/Km)",
            "active_capacity_time_area": "A_time = integral(Vmax_active(t) dt) / (Vmax_initial * T)",
            "integrated_conditional_capacity": "R_capacity = Vmax_initial * T * occupancy * A_time",
            "conditional_capacity_boundary": "Vmax_initial/J_total_mean = q / (occupancy * A_time)",
            "qualified_product_observations": contract[
                "product_observation_contract"
            ]["equations"],
        },
        "product_observation_contract": {
            "status": contract["product_observation_contract"][
                "status_in_this_comp"
            ],
            "required_prerequisites": contract["product_observation_contract"][
                "required_prerequisites"
            ],
            "empirically_evaluated": False,
        },
        "checks": checks,
        "response_surface": {
            "row_count": len(surface),
            "minimum_required_capacity_multiple_exact": fraction_text(
                min(q(row["required_capacity_multiple_exact"]) for row in surface)
            ),
            "minimum_required_capacity_multiple_decimal": fraction_decimal_text(
                min(q(row["required_capacity_multiple_exact"]) for row in surface)
            ),
            "maximum_required_capacity_multiple_exact": fraction_text(
                max(q(row["required_capacity_multiple_exact"]) for row in surface)
            ),
            "maximum_required_capacity_multiple_decimal": fraction_decimal_text(
                max(q(row["required_capacity_multiple_exact"]) for row in surface)
            ),
            "scope": "conditional dimensionless capacity map; not a solved dynamic mass balance or biological target",
        },
        "same_concentration_counterexample": {
            "scenario_count": len(counterexamples),
            "minimum_uox_attributed_flux_exact": fraction_text(
                min(
                    q(row["uox_attributed_product_equivalent_flux_exact"])
                    for row in counterexamples
                )
            ),
            "minimum_uox_attributed_flux_decimal": fraction_decimal_text(
                min(
                    q(row["uox_attributed_product_equivalent_flux_exact"])
                    for row in counterexamples
                )
            ),
            "maximum_uox_attributed_flux_exact": fraction_text(
                max(
                    q(row["uox_attributed_product_equivalent_flux_exact"])
                    for row in counterexamples
                )
            ),
            "maximum_uox_attributed_flux_decimal": fraction_decimal_text(
                max(
                    q(row["uox_attributed_product_equivalent_flux_exact"])
                    for row in counterexamples
                )
            ),
            "interpretation": "under the declared constant-volume rate law, the same concentration trajectory does not identify UOX removal flux",
        },
        "measurement_structural_audit": {
            "unknowns": contract["identifiability_model"]["unknowns"],
            "governing_equations": contract["identifiability_model"][
                "governing_equations"
            ],
            "ideal_product_observation": ideal_details,
            "product_prerequisites_failed": failed_details,
            "scope": "exact structural identifiability under ideal noiseless observation equations; not practical identifiability or assay validation",
        },
        "interpretation": (
            "The conditional capacity identity, concentration-only negative counterexample, "
            "and exact structural-identifiability audit passed their preregistered method checks. "
            "Positive identifiability is conditional on the named ideal observations; the biological "
            "regime and assay performance were not evaluated."
            if verdict == "METHOD_MAP_DERIVED"
            else "A preregistered schema, algebra, counterexample, or rank check failed; no interpretation is permitted."
        ),
        "limitations": [
            "The response surface holds C/Km fixed and does not solve a dynamic concentration trajectory.",
            "No human supply, reabsorption, outflow, oxygen, residence, active-UOX, dose, or serum-urate parameter is estimated.",
            "The qualified product and source-resolved observations are ideal assumptions, not validated assays.",
            "Structural identifiability under noiseless equations does not establish practical identifiability, precision, recovery, or a usable biological regime.",
            "The cumulative measurement combinations are not claimed to be globally minimal.",
            "A practical local ledger requires a prespecified acceptance bound for unattributed residual loss.",
            "Peroxide generation, scavenging, tissue exposure, and safety remain assigned to validation section 1.36.",
            "A measured dynamic compartmental model remains blocked until exact-configuration and boundary-fate data exist.",
        ],
    }

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUTS / "break-even-surface.csv", surface)
    write_csv(OUTPUTS / "same-concentration-counterexamples.csv", counterexamples)
    write_csv(
        OUTPUTS / "measurement-identifiability.csv", ideal_rows + failed_rows
    )
    (OUTPUTS / "results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# comp-050 summary — luminal UOX conditional capacity and measurement identifiability",
        "",
        f"**Verdict: {verdict}. Biological regime: NOT_EVALUATED.**",
        "",
    ]
    if verdict == "METHOD_MAP_DERIVED":
        lines += [
            "The run derived a conditional dimensionless capacity boundary, demonstrated a concentration-only structural non-identifiability counterexample, and completed an exact row-space audit of the declared measurement combinations. It did not estimate a biological operating regime or validate an assay.",
            "",
            "## Conditional capacity boundary",
            "",
            "`Vmax_initial / J_total_mean = q / (occupancy × A_time)`",
            "",
            "`J_total_mean` is mean total local urate influx, not systemic-origin influx. At `q = 1`, integrated conditional UOX capacity equals total local influx over the window; this is not a closed dynamic mass balance, dose, or efficacy result.",
            "",
            "## Structural results",
            "",
            "- The same constant-volume concentration trajectory is compatible with different UOX-removal fluxes.",
            "- Initial/terminal urate plus a qualified UOX-product-equivalent observation conditionally identifies local UOX removal, but does not close the local ledger.",
            "- Calibrated reaction-site capacity is a separate observation needed to map an exact configuration onto the conditional capacity term.",
            "- The complete declared source/boundary-fate combination closes the structural ledger and identifies systemic-origin UOX removal only under qualified total and source-resolved product observations.",
            "- Removing the product observations after prerequisite failure makes local and systemic-origin UOX removal non-identifiable and prevents declared ledger closure.",
            "",
            "These are structural results under ideal noiseless observation equations. They are not assay validation, practical identifiability, a minimum-measurement proof, or a biological verdict.",
        ]
    else:
        lines.append(
            "A preregistered schema, algebra, counterexample, or rank check failed. No scientific interpretation is permitted."
        )
    lines += ["", "## Limitations", ""]
    lines.extend(f"- {item}" for item in results["limitations"])
    (OUTPUTS / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"comp-050 complete: {verdict}")


if __name__ == "__main__":
    main()
