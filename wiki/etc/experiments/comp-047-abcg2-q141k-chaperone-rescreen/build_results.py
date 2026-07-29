#!/usr/bin/env python3
"""Deterministically merge the frozen COMP-047 docking run with both Axis-2 checks.

This repair does not dock molecules. It consumes the existing result-bearing
artifacts and rewrites only the annotated result and human-readable reports:

  outputs/results.json
  outputs/controls.md
  outputs/summary.md

Axis 2a is the bounded ChEMBL inhibition check. Axis 2b is the broader
UniProt/DrugBank ABCG2-relationship check. A relationship flag is conservative
exclusion evidence for this screen; it is not relabeled as proof that every
flagged molecule is an ABCG2 substrate.
"""
import json
from pathlib import Path
from statistics import median

import verify_receptors

HERE = Path(__file__).resolve().parent


def load_json(relative_path):
    path = HERE / relative_path
    if not path.exists():
        raise FileNotFoundError(f"required frozen artifact is missing: {path}")
    return json.loads(path.read_text())


def fmt(value):
    return f"{value:.2f}" if isinstance(value, (int, float)) else "n/a"


def activity_record_status(value):
    if value is True:
        return "record present"
    if value is False:
        return "no bounded record"
    return "unqueried"


def main():
    # Fail closed: no corrected report may be written unless the exact frozen
    # receptor snapshot passes the bound integrity contract in this same process.
    receptor_verification = verify_receptors.verify_and_write()
    if receptor_verification.get("status") != "PASS_WITH_DECLARED_WARNING":
        raise RuntimeError("receptor verification did not pass")

    result_doc = load_json("outputs/results.json")
    chembl = load_json("outputs/chembl_axis2.json")
    drugbank_doc = load_json("outputs/drugbank_substrate_axis.json")
    sensitivity = load_json("outputs/sensitivity.json")

    meta = result_doc["_meta"]
    results = result_doc["results"]
    drugbank_flagged = drugbank_doc.get("flagged", {})
    artifact_date = str(meta.get("generated", "undated")).split()[0]
    attempted = meta.get("n_molecules")
    complete_names = [
        name
        for name, row in results.items()
        if all(
            isinstance(row.get(field), (int, float))
            for field in (
                "fold_q141k_affinity",
                "fold_wt_affinity",
                "transport_affinity",
            )
        )
    ]
    complete_name_set = set(complete_names)
    incomplete_names = sorted(set(results) - complete_name_set)
    if attempted != len(results):
        raise RuntimeError(
            "attempted-molecule metadata does not match the result-row count"
        )

    # Axis 2 is a conservative exclusion layer, not a positive chaperone score.
    for name, row in results.items():
        chembl_row = chembl.get(name, {})
        drugbank_row = drugbank_flagged.get(name, {})
        curated = bool(row.get("known_inhibitor_flag"))
        chembl_activity = chembl_row.get("has_activity")
        substrate_disqualified = bool(chembl_row.get("substrate_disqualified"))
        drugbank_relationship = bool(
            drugbank_row.get("drugbank_abcg2_interacting")
        )

        reasons = []
        if curated:
            reasons.append("curated ABCG2 inhibitor/substrate control")
        if chembl_activity is True:
            reasons.append("ChEMBL ABCG2 activity")
        if substrate_disqualified:
            reasons.append("independently identified ABCG2 substrate")
        if drugbank_relationship:
            reasons.append("UniProt/DrugBank ABCG2 relationship")

        final_known = bool(reasons)
        row["chembl_abcg2_empirical"] = chembl_activity
        row["chembl_best_pchembl"] = chembl_row.get("best_pchembl")
        row["chembl_note"] = chembl_row.get("note")
        row["drugbank_abcg2_interacting"] = drugbank_relationship
        row["substrate_disqualified"] = substrate_disqualified
        row["final_known_abcg2"] = final_known
        row["final_disqualify_reasons"] = reasons

        tier = row.get("chaperone_tier")
        row["wetlab_candidate"] = (
            tier if tier in ("yes", "uncertain") and not final_known else "no"
        )

    result_doc["_postprocessing"] = {
        "contract": "frozen docking + ChEMBL inhibition + UniProt/DrugBank relationship exclusion",
        "axis2a": "outputs/chembl_axis2.json",
        "axis2b": "outputs/drugbank_substrate_axis.json",
        "sensitivity": "outputs/sensitivity.json",
        "artifact_date": artifact_date,
    }

    def sort_key(item):
        _, row = item
        tier_rank = {"yes": 0, "uncertain": 1, "no": 2}.get(
            row.get("wetlab_candidate"), 3
        )
        affinity = row.get("fold_q141k_affinity")
        return (tier_rank, affinity if isinstance(affinity, (int, float)) else 0)

    ordered = sorted(results.items(), key=sort_key)
    executable_rows = [
        (name, row)
        for name, row in ordered
        if row.get("wetlab_candidate") in ("yes", "uncertain")
    ]

    (HERE / "outputs/results.json").write_text(
        json.dumps(result_doc, indent=2) + "\n"
    )

    valid = [
        (name, row)
        for name, row in results.items()
        if name in complete_name_set
    ]
    fold_rank = {
        name: index + 1
        for index, (name, _) in enumerate(
            sorted(valid, key=lambda item: item[1]["fold_q141k_affinity"])
        )
    }
    n_valid = len(valid)
    cftr = [
        (name, row)
        for name, row in results.items()
        if row.get("role_tag") == "cftr_corrector"
    ]
    negative_controls = [
        (name, row)
        for name, row in results.items()
        if row.get("role_tag") == "abcg2_inhibitor"
    ]

    control_lines = [
        "# comp-047 — Control and exclusion read-out",
        "",
        f"Frozen docking run date: {artifact_date}. Attempted {attempted}; "
        f"{n_valid} complete docking-score rows; incomplete: "
        f"{', '.join(incomplete_names) if incomplete_names else 'none'}.",
        "",
        "Affinities are Vina scores in kcal/mol (more negative = stronger). "
        "Margin = transport − fold@Q141K (>0 favors the modeled fold-site box). "
        "These are method diagnostics, not binding or rescue measurements.",
        "",
        "## Cross-protein chaperone mechanism comparators",
        "",
        "CFTR correctors are not validated ABCG2 fold-site binders. Their failure "
        "to earn rank shows that this setup did not recover these cross-protein "
        "chaperone comparators; it is not proof that ABCG2 lacks a rescuable site.",
        "",
        "| molecule | fold@Q141K | fold@WT | Walker A | margin | base-run fold rank | docking tier | executable row |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for name, row in sorted(cftr, key=lambda item: fold_rank.get(item[0], 999)):
        control_lines.append(
            f"| {name} | {fmt(row.get('fold_q141k_affinity'))} "
            f"| {fmt(row.get('fold_wt_affinity'))} "
            f"| {fmt(row.get('transport_affinity'))} "
            f"| {fmt(row.get('fold_vs_transport_margin'))} "
            f"| {fold_rank.get(name, '?')}/{n_valid} "
            f"| {row.get('chaperone_tier')} | {row.get('wetlab_candidate')} |"
        )

    control_lines += [
        "",
        "## Curated ABCG2 negative controls",
        "",
        "| molecule | fold@Q141K | Walker A | margin | base-run fold rank | ChEMBL activity | DrugBank relationship | executable row |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for name, row in sorted(
        negative_controls, key=lambda item: fold_rank.get(item[0], 999)
    ):
        control_lines.append(
            f"| {name} | {fmt(row.get('fold_q141k_affinity'))} "
            f"| {fmt(row.get('transport_affinity'))} "
            f"| {fmt(row.get('fold_vs_transport_margin'))} "
            f"| {fold_rank.get(name, '?')}/{n_valid} "
            f"| {activity_record_status(row.get('chembl_abcg2_empirical'))} "
            f"| {'yes' if row.get('drugbank_abcg2_interacting') else 'no'} "
            f"| {row.get('wetlab_candidate')} |"
        )

    axis2_impact = [
        (name, row)
        for name, row in results.items()
        if row.get("chaperone_tier") in ("yes", "uncertain")
    ]
    control_lines += [
        "",
        "## Axis-2 impact on docking-tier survivors",
        "",
        "| molecule | docking tier | ChEMBL activity | substrate exclusion | DrugBank relationship | final executable row |",
        "|---|---|---|---|---|---|",
    ]
    for name, row in sorted(axis2_impact):
        control_lines.append(
            f"| {name} | {row.get('chaperone_tier')} "
            f"| {activity_record_status(row.get('chembl_abcg2_empirical'))} "
            f"| {'yes' if row.get('substrate_disqualified') else 'no'} "
            f"| {'yes' if row.get('drugbank_abcg2_interacting') else 'no'} "
            f"| {row.get('wetlab_candidate')} |"
        )

    cftr_rows = [
        name
        for name, row in cftr
        if row.get("wetlab_candidate") in ("yes", "uncertain")
    ]
    negative_rows = [
        name
        for name, row in negative_controls
        if row.get("wetlab_candidate") in ("yes", "uncertain")
    ]
    control_lines += [
        "",
        "## Diagnostic interpretation",
        "",
        f"- Cross-protein chaperone comparators reaching an executable tier: "
        f"**{len(cftr_rows)}** ({cftr_rows if cftr_rows else 'none'}).",
        f"- Curated ABCG2 negative controls left as executable rows after Axis 2: "
        f"**{len(negative_rows)}** ({negative_rows if negative_rows else 'none'}).",
        "- The first result does not validate sensitivity, because the comparator "
        "molecules are established for CFTR rather than ABCG2. The second shows "
        "that the exclusion layer works for the declared controls; it does not "
        "validate the fold-site ranking.",
    ]
    (HERE / "outputs/controls.md").write_text("\n".join(control_lines) + "\n")

    n_yes = sum(
        1 for row in results.values() if row.get("wetlab_candidate") == "yes"
    )
    n_uncertain = sum(
        1 for row in results.values() if row.get("wetlab_candidate") == "uncertain"
    )
    if n_yes:
        verdict = "DOCKING SHORTLIST GENERATED — REQUIRES BIOLOGICAL VALIDATION"
    else:
        verdict = "INCONCLUSIVE — NO DEFENSIBLE DOCKING-BACKED RANKING"

    summary = [
        "# comp-047 — Summary",
        "",
        f"**Frozen docking run date:** {artifact_date}",
        "",
        "**Method:** static-receptor AutoDock Vina at a modeled residue-141 region "
        "and Walker-A comparison box, followed by ChEMBL inhibition and "
        "UniProt/DrugBank relationship exclusion.",
        "",
        f"**Vina:** seed {meta['seed']}, exhaustiveness {meta['exhaustiveness']}, "
        f"cpu {meta['cpu']}; {attempted} attempted and {n_valid} complete "
        f"docking-score rows; incomplete: "
        f"{', '.join(incomplete_names) if incomplete_names else 'none'}.",
        "",
        f"## VERDICT: {verdict}",
        "",
        f"Executable rule output after both Axis-2 checks: **{n_yes} yes**, "
        f"**{n_uncertain} uncertain**. An executable row is not a wet-lab "
        "priority: the screen has no validated ABCG2 chaperone positive control, "
        "uses a static conformation, and produced unstable fold-site rankings "
        "under the recorded perturbations.",
        "",
        "## Executable marginal rows (not wet-lab priorities)",
        "",
        "| rank | molecule | class | fold@Q141K | Walker A | margin | Q141K−WT proxy | ChEMBL activity | DrugBank relationship | tier |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for index, (name, row) in enumerate(executable_rows, 1):
        summary.append(
            f"| {index} | {name} | {row.get('drug_class', '')} "
            f"| {fmt(row.get('fold_q141k_affinity'))} "
            f"| {fmt(row.get('transport_affinity'))} "
            f"| {fmt(row.get('fold_vs_transport_margin'))} "
            f"| {fmt(row.get('q141k_vs_wt_selectivity'))} "
            f"| {activity_record_status(row.get('chembl_abcg2_empirical'))} "
            f"| {'yes' if row.get('drugbank_abcg2_interacting') else 'no'} "
            f"| {row.get('wetlab_candidate')} |"
        )
    if not executable_rows:
        summary.append("| — | (none) | | | | | | | | |")

    fold_sorted = sorted(valid, key=lambda item: item[1]["fold_q141k_affinity"])
    summary += [
        "",
        "## Base-run fold-site scores (descriptive, not a robust ranking)",
        "",
        "The table records the strongest scores in the original box. It is not a "
        "fallback shortlist: the sensitivity artifact shows material rank changes "
        "under box, seed, and protonation perturbations, and Axis 2 remains an "
        "exclusion layer rather than evidence of chaperone activity.",
        "",
        "| rank | molecule | class | fold@Q141K | Walker A | margin | excluded by Axis 2? |",
        "|---|---|---|---|---|---|---|",
    ]
    for index, (name, row) in enumerate(fold_sorted[:15], 1):
        summary.append(
            f"| {index} | {name} | {row.get('drug_class', '')} "
            f"| {fmt(row.get('fold_q141k_affinity'))} "
            f"| {fmt(row.get('transport_affinity'))} "
            f"| {fmt(row.get('fold_vs_transport_margin'))} "
            f"| {'yes' if row.get('final_known_abcg2') else 'no'} |"
        )

    transport_values = [
        row["transport_affinity"]
        for _, row in valid
        if isinstance(row.get("transport_affinity"), (int, float))
    ]
    fold_values = [row["fold_q141k_affinity"] for _, row in valid]
    if transport_values:
        summary += [
            "",
            f"**Walker-A comparison diagnostic:** scores span "
            f"{min(transport_values):.2f}..{max(transport_values):.2f} "
            f"(median {median(transport_values):.2f}); modeled fold-site scores span "
            f"{min(fold_values):.2f}..{max(fold_values):.2f} "
            f"(median {median(fold_values):.2f}). The substantial overlap makes "
            "the margin rule non-discriminating in this configuration; it does not "
            "establish a selective fold-site interaction.",
        ]

    changed_counts = [
        item.get("positions_changed")
        for item in sensitivity.get("rank_stability", {})
        .get("per_perturbation", {})
        .values()
        if isinstance(item.get("positions_changed"), int)
    ]
    if changed_counts:
        summary += [
            "",
            f"**Sensitivity diagnostic:** the recorded panel re-docked only the "
            f"Q141K fold-site box using x +2 Å, x -2 Å, y +2 Å, a +3 Å xyz "
            f"diagonal, two box sizes, two alternate seeds, and a neutral-ligand "
            f"condition. It did not test y -2 Å, either z direction, the Walker-A "
            f"box, or the complete margin rule. Within that limited panel, "
            f"{min(changed_counts)}–{max(changed_counts)} of the eight tracked "
            "candidate positions changed. The base-run fold ranking is therefore "
            "not treated as robust; this diagnostic does not establish robustness "
            "of the executable classification.",
        ]

    summary += [
        "",
        "## Interpretation boundary",
        "",
        "- Rosuvastatin is removed from the executable shortlist because it is "
        "independently identified as a BCRP substrate and is also present in the "
        "UniProt/DrugBank ABCG2 relationship set.",
        "- Vorinostat is the sole marginal executable row. Its direct Q141K rescue "
        "precedent is phenotypic and independent of this docking result; it does "
        "not validate the modeled pocket or make the docking row a wet-lab priority.",
        "- Failure to recover the CFTR comparators is a setup-specific diagnostic, "
        "not evidence that ABCG2 cannot be pharmacologically rescued.",
        "- The decisive next observation is the registered Q141K surface-trafficking "
        "+ urate-flux + ABCG2-inhibition counterscreen in validation experiment §1.22, "
        "not another pass through the same docking configuration.",
        "",
        "## Load-bearing limitations",
        "",
        "- Q141K is a static side-chain substitution, not a folding-ΔΔG model.",
        "- A folding intermediate and mutant-selective stabilization are not modeled.",
        "- The receptor is an apo monomer; the Walker-A box is not the physiological "
        "composite ATP site or the transmembrane substrate cavity.",
        "- Vina scores and close margins are not binding-affinity measurements.",
        "- Exposure at the intracellular folding compartment is not modeled.",
        "",
        "See `controls.md`, `sensitivity.json`, `receptor_verification.json`, and the README.",
    ]
    (HERE / "outputs/summary.md").write_text("\n".join(summary) + "\n")

    print(f"verdict: {verdict}")
    print(f"executable rows: {n_yes} yes, {n_uncertain} uncertain")
    print("wrote outputs/results.json, controls.md, summary.md")


if __name__ == "__main__":
    main()
