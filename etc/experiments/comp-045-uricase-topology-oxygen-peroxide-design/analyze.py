#!/usr/bin/env python3
"""comp-045: graded-evidence topology × oxygen × peroxide design."""

from __future__ import annotations

import itertools
import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT / "inputs" / "design_factors.json").read_text())
OUT = ROOT / "outputs"


def grade(topology, peroxide, oxygen_support, oxygen_context):
    intracellular = topology["uox_compartment"] == "cytoplasm"
    ecn = topology["chassis"] == "EcN"

    substrate_status = "direct_empirical_support" if intracellular else "proposed_direct_test"

    if peroxide == "none":
        peroxide_status = "unsupported"
    elif peroxide == "compartment_matched_catalase":
        peroxide_status = "direct_empirical_support" if intracellular else "proposed_direct_test"
    elif intracellular:
        peroxide_status = "direct_empirical_support"
    elif ecn:
        # PULSE observed benefit from the joint KatG+VHb module in secreted and
        # displayed strains, but did not isolate KatG or prove epithelial closure —
        # so an isolated KatG-only arm inherits only joint-module precedent, NOT
        # isolated empirical support (corrected 2026-07-14, comp-review audit).
        peroxide_status = "joint_module_precedent_isolated_unresolved"
    else:
        peroxide_status = "unresolved"

    if oxygen_context == "oxic":
        oxygen_status = "controlled_context_not_proven_sufficient"
    elif oxygen_support == "none":
        oxygen_status = "unresolved"
    elif intracellular:
        oxygen_status = "direct_empirical_support"
    elif ecn:
        # VHb was introduced only within the joint KatG+VHb module; an isolated
        # VHb-only arm inherits joint-module precedent, NOT isolated support
        # (corrected 2026-07-14, comp-review audit).
        oxygen_status = "joint_module_precedent_isolated_unresolved"
    else:
        oxygen_status = "unsupported"

    return {
        "substrate_status": substrate_status,
        "peroxide_status": peroxide_status,
        "oxygen_status": oxygen_status,
        "interpretation": "joint_empirical_comparison_required"
    }


def well_name(index):
    return f"{'ABCDEFGH'[index // 12]}{index % 12 + 1}"


def main():
    base_conditions = []
    for topo, peroxide, oxygen_support in itertools.product(
        P["topologies"], P["peroxide_strategies"], P["oxygen_support"]
    ):
        if oxygen_support == "vhb" and not topo["supports_vhb"]:
            continue
        # For intracellular UOX, "intracellular KatG/native catalase" already
        # is the compartment-matched construct. Do not count the same physical
        # design twice under two labels.
        if (
            topo["uox_compartment"] == "cytoplasm"
            and peroxide["id"] == "compartment_matched_catalase"
        ):
            continue
        base_conditions.append({
            "condition_id": len(base_conditions) + 1,
            "topology": topo["id"],
            "chassis": topo["chassis"],
            "peroxide_strategy": peroxide["id"],
            "oxygen_support": oxygen_support
        })

    graded = []
    plates = []
    for run in range(1, P["biological_runs"] + 1):
        for context_index, oxygen_context in enumerate(P["oxygen_contexts"]):
            plate_id = (run - 1) * len(P["oxygen_contexts"]) + context_index + 1
            wells = []
            for condition in base_conditions:
                topo = next(x for x in P["topologies"] if x["id"] == condition["topology"])
                peroxide = condition["peroxide_strategy"]
                evidence = grade(topo, peroxide, condition["oxygen_support"], oxygen_context)
                graded.append({**condition, "oxygen_context": oxygen_context, **evidence})
                for urate in P["urate_concentrations_uM"]:
                    wells.append({
                        "kind": "factorial",
                        "condition_id": condition["condition_id"],
                        "urate_uM": urate,
                        "oxygen_context": oxygen_context,
                        "biological_run": run
                    })
            for control in P["shared_controls_per_plate"]:
                urate_values = (
                    P["urate_concentrations_uM"]
                    if control["urate_mode"] == "all_concentrations"
                    else [0.0]
                )
                for urate in urate_values:
                    wells.append({
                        "kind": "control",
                        "control": control["id"],
                        "urate_uM": urate,
                        "oxygen_context": oxygen_context,
                        "biological_run": run
                    })
            rng = random.Random(P["random_seed"] + plate_id)
            rng.shuffle(wells)
            assert len(wells) <= 96
            for index, well in enumerate(wells):
                well["well"] = well_name(index)
            plates.append({
                "plate": plate_id,
                "biological_run": run,
                "oxygen_context": oxygen_context,
                "n_used_wells": len(wells),
                "wells": wells
            })

    results = {
        "experiment": "comp-045",
        "verdict": "JOINT EMPIRICAL COMPARISON REQUIRED; NO TOPOLOGY ELIMINATED",
        "n_base_factorial_conditions": len(base_conditions),
        "n_urate_concentrations": len(P["urate_concentrations_uM"]),
        "n_biological_runs": P["biological_runs"],
        "n_plates": len(plates),
        "used_wells_per_plate": plates[0]["n_used_wells"],
        "graded_conditions": graded,
        "plate_maps": plates,
        "required_readouts": P["primary_readouts"],
        "limitations": [
            "Evidence states summarize topology-specific support; they are not efficacy grades.",
            "KatG and VHb were introduced jointly in key precedents, so their independent effects require the proposed separate arms.",
            "Compartment-matched extracellular and surface catalase constructs are proposed engineering tests, not published PULSE constructs.",
            "VHb improves cellular oxygen utilization but cannot create oxygen; dissolved oxygen and demand must be measured in every condition.",
            "Intracellular KatG may lower cell-associated ROS after peroxide diffusion without preventing extracellular epithelial exposure.",
            "Each plate is one biological run within one oxygen context; cross-plate anchors support normalization but do not remove run effects.",
            "Inactive-UOX, chassis-only, and PULSE-mixture controls are substrate-matched at every nonzero urate concentration; no-urate and blank controls are explicitly 0 µM.",
        ]
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")

    lines = [
        "# comp-045 summary — uricase topology × oxygen × peroxide", "",
        "**Verdict: JOINT EMPIRICAL COMPARISON REQUIRED; NO TOPOLOGY ELIMINATED.** Published systems support several topologies, but none was tested across the full substrate × oxygen × peroxide matrix at physiological jejunal urate. Compartment matching remains a mechanistic concern, not a binary computational gate.", "",
        "## Experimental design", "",
        f"- {len(base_conditions)} valid topology × peroxide × VHb conditions",
        f"- {len(P['urate_concentrations_uM'])} urate concentrations: 0.59 µM human-baseline prior, 50 µM sensitivity, 250 µM PULSE benchmark",
        f"- {P['biological_runs']} independent biological runs × {len(P['oxygen_contexts'])} oxygen contexts = {len(plates)} randomized 96-well plates",
        f"- {plates[0]['n_used_wells']} used wells per plate, including substrate-matched inactive-UOX, chassis, PULSE-mixture, explicit no-urate, and medium controls",
        "- Oxic and microoxic conditions are on separate plates; every plate carries the same cross-plate anchors", "",
        "## Interpretation", "",
        "Intracellular UOX+YgfU has direct precedent for substrate import and co-localized KatG/VHb support. Secreted and displayed UOX avoid the importer gate and showed empirical benefit from the joint KatG+VHb module in PULSE, but extracellular peroxide exposure and the source of low-oxygen benefit remain unresolved. Proposed compartment-matched catalase arms test that distinction directly. The PULSE 1:1:1 mixture is retained as a positive benchmark, not substituted for the individual topologies.", "",
        "## Required readouts", ""
    ]
    lines += [f"- {x}" for x in P["primary_readouts"]]
    lines += ["", "## Limitations", ""] + [f"- {x}" for x in results["limitations"]]
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
