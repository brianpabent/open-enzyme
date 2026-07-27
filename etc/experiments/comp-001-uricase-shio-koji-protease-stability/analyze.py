#!/usr/bin/env python3
"""
COMP-001: Q00511 legacy preference-filter and pLDDT-context audit.

This analysis enumerates adjacent residue pairs that match three fixed legacy
filters and reports AlphaFold confidence around each pair. The filters are not
treated as exhaustive protease specificity models. The analysis does not model
accessibility, cleavage, retained activity, or fermentation survival.

Usage: python3 analyze.py
Outputs: outputs/cleavage_sites.json, outputs/summary.md
"""

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

CANONICAL_AA = set("ACDEFGHIKLMNPQRSTVWY")
EXPECTED_SEQUENCE_SHA256 = (
    "cb5dbe78672345fa69aa22b22567f43efc9977817af32cb2cf2c98ec1852f877"
)
EXPECTED_POSITION_RESIDUE_PLDDT_SHA256 = (
    "90abb3e1a8ea932f71231e742c22f00a34ebc7c864bf7680c022b19555662f80"
)
FLANK_RESIDUES = 3

METHOD_CAVEAT = (
    "Adjacent-pair matches to unverified legacy preference filters plus "
    "AlphaFold pLDDT context only. The filters are not established exhaustive "
    "protease specificity rules, and pLDDT is model confidence rather than "
    "solvent accessibility. This output does not estimate cleavage, "
    "protease-survival risk, retained activity, or fermentation performance."
)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_sequence(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    sequence = "".join(line.strip() for line in lines if not line.startswith(">"))
    if not sequence or any(residue not in CANONICAL_AA for residue in sequence):
        raise ValueError("FASTA must contain one nonempty canonical protein sequence")
    if sha256_text(sequence) != EXPECTED_SEQUENCE_SHA256:
        raise ValueError("Q00511 sequence does not match the reviewed input")
    return sequence


def load_plddt(path, sequence):
    raw = json.loads(path.read_text(encoding="utf-8"))
    try:
        plddt = {int(position): float(value) for position, value in raw.items()}
    except (TypeError, ValueError) as exc:
        raise ValueError("pLDDT JSON must map integer positions to numbers") from exc

    expected_positions = list(range(1, len(sequence) + 1))
    if sorted(plddt) != expected_positions:
        raise ValueError("pLDDT positions must cover the sequence exactly")
    if any(not math.isfinite(value) or not 0 <= value <= 100 for value in plddt.values()):
        raise ValueError("Every pLDDT value must be finite and between 0 and 100")

    canonical = "\n".join(
        f"{position}\t{sequence[position - 1]}\t{plddt[position]:.2f}"
        for position in expected_positions
    ) + "\n"
    if sha256_text(canonical) != EXPECTED_POSITION_RESIDUE_PLDDT_SHA256:
        raise ValueError("pLDDT vector is not aligned to the reviewed Q00511 mapping")
    return plddt


def load_filters(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported preference-filter schema")
    if data.get("provenance_status") != "legacy_encoding_not_claim_level_verified":
        raise ValueError("Legacy filter provenance status must remain explicit")

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        raise ValueError("At least one preference filter is required")

    seen_ids = set()
    for rule in rules:
        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not rule_id or rule_id in seen_ids:
            raise ValueError("Preference-filter IDs must be unique nonempty strings")
        seen_ids.add(rule_id)
        for field in ("p1_filter", "p1_prime_filter"):
            residues = rule.get(field)
            if not isinstance(residues, list):
                raise ValueError(f"{rule_id}.{field} must be a list")
            if len(residues) != len(set(residues)):
                raise ValueError(f"{rule_id}.{field} contains duplicate residues")
            if any(residue not in CANONICAL_AA for residue in residues):
                raise ValueError(f"{rule_id}.{field} contains a noncanonical residue")
        if not rule["p1_filter"] and not rule["p1_prime_filter"]:
            raise ValueError(f"{rule_id} cannot leave both sides unrestricted")
    return data


def motif_window_bounds(p1_position, sequence_length, flank=FLANK_RESIDUES):
    """
    Return inclusive bounds containing the P1/P1' pair plus up to `flank`
    residues before P1 and after P1'.
    """
    if not 1 <= p1_position < sequence_length:
        raise ValueError("P1 position must identify an internal peptide bond")
    start = max(1, p1_position - flank)
    end = min(sequence_length, p1_position + 1 + flank)
    return start, end


def local_plddt(plddt, p1_position, sequence_length):
    start, end = motif_window_bounds(p1_position, sequence_length)
    values = [plddt[position] for position in range(start, end + 1)]
    return {
        "window_start": start,
        "window_end": end,
        "window_residue_count": len(values),
        "mean_plddt_window": sum(values) / len(values),
    }


def matches_filter(p1, p1_prime, rule):
    p1_match = not rule["p1_filter"] or p1 in rule["p1_filter"]
    p1_prime_match = (
        not rule["p1_prime_filter"] or p1_prime in rule["p1_prime_filter"]
    )
    return p1_match and p1_prime_match


def map_filter_matches(sequence, plddt, rule):
    matches = []
    for index in range(len(sequence) - 1):
        p1 = sequence[index]
        p1_prime = sequence[index + 1]
        if not matches_filter(p1, p1_prime, rule):
            continue
        p1_position = index + 1
        matches.append(
            {
                "p1_position": p1_position,
                "p1_prime_position": p1_position + 1,
                "P1": p1,
                "P1_prime": p1_prime,
                **local_plddt(plddt, p1_position, len(sequence)),
            }
        )
    return matches


def sequence_stats(plddt):
    values = list(plddt.values())
    return {
        "length": len(values),
        "mean_plddt": sum(values) / len(values),
        "minimum_plddt": min(values),
        "maximum_plddt": max(values),
        "residues_plddt_at_least_90": sum(value >= 90 for value in values),
        "residues_plddt_70_to_below_90": sum(
            70 <= value < 90 for value in values
        ),
        "residues_plddt_50_to_below_70": sum(
            50 <= value < 70 for value in values
        ),
        "residues_plddt_below_50": sum(value < 50 for value in values),
    }


def run_self_checks():
    assert motif_window_bounds(1, 302) == (1, 5)
    assert motif_window_bounds(100, 302) == (97, 104)
    assert motif_window_bounds(301, 302) == (298, 302)
    assert local_plddt(
        {position: float(position) for position in range(1, 9)}, 4, 8
    ) == {
        "window_start": 1,
        "window_end": 8,
        "window_residue_count": 8,
        "mean_plddt_window": 4.5,
    }


def build_output():
    run_self_checks()
    sequence = load_sequence(INPUTS / "Q00511.fasta")
    plddt = load_plddt(INPUTS / "alphafold_Q00511_plddt.json", sequence)
    filter_data = load_filters(INPUTS / "legacy_preference_filters.json")

    results = []
    for rule in filter_data["rules"]:
        matches = map_filter_matches(sequence, plddt, rule)
        results.append(
            {
                "filter_id": rule["id"],
                "legacy_label": rule["legacy_label"],
                "provenance_status": filter_data["provenance_status"],
                "p1_filter": rule["p1_filter"],
                "p1_prime_filter": rule["p1_prime_filter"],
                "empty_filter_semantics": "unrestricted",
                "total_adjacent_pair_matches": len(matches),
                "minimum_mean_plddt_window": (
                    min(match["mean_plddt_window"] for match in matches)
                    if matches
                    else None
                ),
                "lowest_plddt_matches": sorted(
                    matches,
                    key=lambda match: (
                        match["mean_plddt_window"],
                        match["p1_position"],
                    ),
                )[:5],
                "encoded_preference_filter_matches": matches,
            }
        )

    return {
        "schema_version": 2,
        "analysis_scope": "legacy_preference_filter_and_plddt_context_only",
        "method_caveat": METHOD_CAVEAT,
        "protein": "Uricase (urate oxidase), Aspergillus flavus (Q00511)",
        "input_integrity": {
            "sequence_sha256": EXPECTED_SEQUENCE_SHA256,
            "position_residue_plddt_sha256": (
                EXPECTED_POSITION_RESIDUE_PLDDT_SHA256
            ),
        },
        "plddt_window": {
            "definition": (
                "P1 and P1' plus up to three flanking residues on each side"
            ),
            "flank_residues": FLANK_RESIDUES,
            "boundary_behavior": "truncate at sequence termini",
        },
        "sequence_stats": sequence_stats(plddt),
        "preference_filter_results": results,
        "verdict": "PROXY ONLY — EMPIRICAL PROTEASE RISK UNRESOLVED",
        "decision_boundary": {
            "supported": [
                "adjacent Q00511 sequence pairs matching the fixed legacy filters",
                "AlphaFold pLDDT context around each matching pair",
            ],
            "not_supported": [
                "exhaustive protease recognition or cleavage specificity",
                "solvent accessibility or burial",
                "cleavage probability or protease-survival risk",
                "retained uricase activity",
                "shio-koji fermentation performance",
            ],
            "empirical_gate": "wiki/validation-experiments.md section 1.10",
            "all_possible_results": (
                "Proxy only; empirical protease risk unresolved; section 1.10 "
                "remains the feasibility gate."
            ),
        },
        "sensitivity_plan": {
            "current_run": "No inferential sensitivity analysis.",
            "reason": (
                "This run is an exact enumeration of fixed legacy filters and "
                "one prespecified descriptive pLDDT window."
            ),
            "change_control": (
                "Any alternative filter encoding or window width is a new "
                "design requiring a fresh pre-run review."
            ),
        },
    }


def display(value):
    return f"{value:.2f}"


def write_summary(data, path):
    stats = data["sequence_stats"]
    lines = [
        "# COMP-001 — Q00511 Legacy Preference-Filter and pLDDT-Context Audit",
        "",
        f"**Verdict:** **{data['verdict']}**",
        "",
        f"**Method boundary:** {data['method_caveat']}",
        "",
        "## Question",
        "",
        "Which adjacent residue pairs in *A. flavus* UOX (Q00511) match "
        "three fixed legacy preference filters, and what AlphaFold confidence "
        "surrounds each match?",
        "",
        "## Sequence-confidence snapshot",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Sequence length | {stats['length']} aa |",
        f"| Mean pLDDT | {display(stats['mean_plddt'])} |",
        f"| Minimum pLDDT | {display(stats['minimum_plddt'])} |",
        f"| Residues with pLDDT ≥90 | {stats['residues_plddt_at_least_90']} |",
        f"| Residues with pLDDT 70–<90 | "
        f"{stats['residues_plddt_70_to_below_90']} |",
        f"| Residues with pLDDT 50–<70 | "
        f"{stats['residues_plddt_50_to_below_70']} |",
        f"| Residues with pLDDT <50 | {stats['residues_plddt_below_50']} |",
        "",
        "pLDDT reports local prediction confidence. It does not establish "
        "burial or protease accessibility.",
        "",
        "## Encoded preference-filter inventory",
        "",
        "| Legacy filter label | Adjacent-pair matches | "
        "Lowest local mean pLDDT |",
        "|---|---:|---:|",
    ]

    for result in data["preference_filter_results"]:
        minimum = result["minimum_mean_plddt_window"]
        minimum_text = "n/a" if minimum is None else display(minimum)
        lines.append(
            f"| {result['legacy_label']} | "
            f"{result['total_adjacent_pair_matches']} | {minimum_text} |"
        )

    lines += [
        "",
        "The complete pair inventory, exact filter arrays, window bounds, "
        "included-residue counts, and unrounded means are in "
        "`cleavage_sites.json`. The legacy arrays lack claim-level provenance "
        "and are not treated as exhaustive biological specificity rules.",
        "",
        "## Decision",
        "",
        "COMP-001 supplies an auditable sequence-filter inventory and pLDDT "
        "context only. Every possible output leaves protease susceptibility "
        "unresolved. The §1.10 shio-koji retained-activity assay remains the "
        "feasibility gate.",
        "",
        "No inferential sensitivity analysis is warranted for this exact "
        "enumeration. A different filter encoding or window width would be a "
        "new design requiring fresh review.",
        "",
        "## Reproduction",
        "",
        "Run `python3 analyze.py` from the COMP directory. The script uses "
        "Python standard-library code and fixed committed inputs. Two runs "
        "must produce byte-identical outputs.",
        "",
        "---",
        "",
        "*Generated from the fixed COMP-001 inputs. Source accessions, "
        "versions, transformations, and limitations are recorded in "
        "`inputs/provenance.md`.*",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    output = build_output()
    (OUTPUTS / "cleavage_sites.json").write_text(
        json.dumps(output, indent=2) + "\n",
        encoding="utf-8",
    )
    write_summary(output, OUTPUTS / "summary.md")
    print("Done. Outputs written to outputs/")


if __name__ == "__main__":
    main()
