#!/usr/bin/env python3
"""
comp-005: Lactoferrin protease stability in shio-koji fermentation

Orchestrator — loads inputs, calls shared library, writes comp-005-specific outputs.
Core algorithm lives in experiments/lib/protease_stability.py.

Usage: python3 analyze.py   (from this directory)
Outputs: outputs/cleavage_sites.json, outputs/summary.md

Key structural difference from comp-001 (uricase):
  Lactoferrin (P02788) is a 710 aa glycoprotein with two bilobal domains connected
  by a linker region. The signal peptide (aa 1-19) is disordered (pLDDT 35-54),
  and the inter-lobe linker (approx aa 432-445) shows reduced pLDDT (68-81) relative
  to the well-folded lobe cores. These are the structural soft spots uricase lacked.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
from protease_stability import (
    load_sequence,
    load_plddt,
    load_proteases,
    compute_sequence_stats,
    run_all_proteases,
    find_cleavage_sites,
)

INPUTS  = Path(__file__).parent / "inputs"
OUTPUTS = Path(__file__).parent / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# Signal peptide boundary (UniProt P02788 annotation: aa 1-19)
SIGNAL_PEPTIDE_END = 19


def main():
    seq       = load_sequence(INPUTS / "P02788.fasta")
    plddt     = load_plddt(INPUTS / "alphafold_P02788_plddt.json")
    proteases, conditions = load_proteases(INPUTS / "protease_specificities.json")

    sequence_stats   = compute_sequence_stats(plddt)
    protease_results = run_all_proteases(seq, plddt, proteases, conditions)

    # Annotate top-5 sites with region; also compute mature-protein-only risk scores.
    # The signal peptide (aa 1-19) is fully disordered and dominates all top-5 lists.
    # Mature-protein scores are the operationally relevant figures for §1.10 framing.
    nacl_pct = conditions["NaCl_pct"]
    for name, result in protease_results.items():
        for site in result["top_5_sites"]:
            site["region"] = "signal_peptide" if site["position"] <= SIGNAL_PEPTIDE_END else "mature_protein"
        all_sites = find_cleavage_sites(seq, proteases[name], plddt, nacl_pct)
        mature_sites = [s for s in all_sites if s["position"] > SIGNAL_PEPTIDE_END]
        result["mature_protein_max_risk_score"] = round(mature_sites[0]["risk_score"], 3) if mature_sites else 0
        result["mature_protein_exposed_sites"]  = sum(1 for s in mature_sites if s["accessibility"] == "exposed")

    # Mature-protein verdict (excluding signal peptide sites — the operationally relevant score)
    mature_max_risks  = {n: r["mature_protein_max_risk_score"] for n, r in protease_results.items()}
    mature_worst      = max(mature_max_risks, key=mature_max_risks.get)
    mature_worst_score = mature_max_risks[mature_worst]
    if mature_worst_score < 0.15:
        mature_verdict_label = "LOW"
    elif mature_worst_score < 0.30:
        mature_verdict_label = "MODERATE"
    else:
        mature_verdict_label = "HIGH"

    output = {
        "protein":                   "Lactoferrin (lactotransferrin), Homo sapiens (P02788)",
        "alphafold_model":           "AF-P02788-F1-model_v6",
        "signal_peptide_aa":         f"1-{SIGNAL_PEPTIDE_END} (cleaved during mammalian secretion; "
                                     "retention in A. oryzae expression context uncertain)",
        "conditions":                conditions,
        "sequence_stats":            sequence_stats,
        "protease_results":          protease_results,
        "mature_protein_verdict":    mature_verdict_label,
        "mature_protein_worst_score": mature_worst_score,
        "mature_protein_worst_protease": mature_worst,
    }

    with open(OUTPUTS / "cleavage_sites.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output, OUTPUTS / "summary.md")
    print("Done. Outputs written to outputs/")


def write_summary(data, path):
    ss              = data["sequence_stats"]
    cond            = data["conditions"]
    pr              = data["protease_results"]
    mature_verdict  = data["mature_protein_verdict"]
    mature_score    = data["mature_protein_worst_score"]
    mature_worst    = data["mature_protein_worst_protease"]

    lines = [
        "# comp-005 — Lactoferrin Shio-Koji Protease Stability: Summary",
        "",
        f"**Protein:** {data['protein']}  ",
        f"**AlphaFold model:** {data['alphafold_model']}  ",
        f"**Signal peptide:** {data['signal_peptide_aa']}  ",
        f"**Conditions modeled:** {cond['NaCl_pct']}% NaCl, pH {cond['pH_range'][0]}–{cond['pH_range'][1]}, {cond['temperature_C']}°C, {cond['duration_days'][0]}–{cond['duration_days'][1]} days  ",
        f"**Analysis date:** 2026-05-05  ",
        f"**Script:** `experiments/comp-005-lactoferrin-shio-koji-protease-stability/analyze.py`  ",
        f"**Library:** `experiments/lib/protease_stability.py`  ",
        "",
        "---",
        "",
        "## Structural Overview",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Sequence length | {ss['length']} aa (incl. signal peptide aa 1–19) |",
        f"| Mean pLDDT (AlphaFold confidence) | {ss['mean_plddt']} / 100 |",
        f"| Minimum pLDDT (most flexible residue) | {ss['min_plddt']} / 100 |",
        f"| % residues pLDDT > 80 (well-folded) | {ss['pct_residues_above_80']}% |",
        f"| % residues pLDDT > 90 (core-folded) | {ss['pct_residues_above_90']}% |",
        "",
        "**Contrast with uricase (comp-001):** Uricase had mean pLDDT 97.1 and minimum 80.5 — 100% of residues well-folded. "
        f"Lactoferrin's mean of {ss['mean_plddt']} and minimum of {ss['min_plddt']} reflect two structurally distinct soft spots: "
        "(1) the signal peptide (aa 1–19, pLDDT 35–54, fully disordered) and "
        "(2) the inter-lobe linker (approx aa 432–445, pLDDT 68–81, partially exposed). "
        "These are the structural entry points uricase lacked entirely.",
        "",
        "---",
        "",
        "## Per-Protease Risk Assessment",
        "",
    ]

    for name, r in pr.items():
        lines += [
            f"### {r['full_name']} (`{name}`)",
            "",
            "| Parameter | Value |",
            "|---|---|",
            f"| Recognition sites in sequence | {r['total_recognition_sites']} |",
            f"| Buried (pLDDT ≥ 80) | {r['buried_sites']} |",
            f"| Partially exposed (pLDDT 65–80) | {r['partially_exposed_sites']} |",
            f"| Exposed (pLDDT < 65) | {r['exposed_sites']} |",
            f"| Residual activity at 17.5% NaCl | {r['salt_residual_activity_at_nacl']*100:.0f}% |",
            f"| pH activity factor (shio-koji pH) | {r['ph_activity_factor']*100:.0f}% |",
            f"| Effective protease activity (salt × pH) | {r['effective_activity']*100:.1f}% |",
            f"| Max risk score (0–1) | {r['max_risk_score']} |",
            "",
        ]
        mature_max = r.get("mature_protein_max_risk_score", "n/a")
        mature_exp = r.get("mature_protein_exposed_sites", "n/a")
        lines += [
            f"| Mature-protein max risk score (excl. signal peptide) | {mature_max} |",
            f"| Mature-protein exposed sites (excl. signal peptide) | {mature_exp} |",
            "",
        ]
        if r["top_5_sites"]:
            lines += [
                "**Top 5 highest-risk cleavage sites (full sequence incl. signal peptide):**",
                "",
                "| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |",
                "|---|---|---|---|---|---|---|",
            ]
            for s in r["top_5_sites"]:
                region = s.get("region", "mature_protein")
                lines.append(
                    f"| {s['position']} | {region} | {s['P1']} | {s['P1_prime']} | "
                    f"{s['mean_plddt_window']} | {s['accessibility']} | {s['risk_score']} |"
                )
            lines.append("")

    # Determine overall verdict (full sequence, incl. signal peptide)
    max_risks   = {n: r["max_risk_score"] for n, r in pr.items()}
    worst       = max(max_risks, key=max_risks.get)
    worst_score = max_risks[worst]

    if worst_score < 0.15:
        verdict_label = "LOW"
        verdict_text  = "protease degradation in shio-koji is unlikely to meaningfully reduce lactoferrin activity"
    elif worst_score < 0.30:
        verdict_label = "MODERATE"
        verdict_text  = "partial degradation is possible, particularly at exposed sites; wet-lab confirmation (§1.10) required"
    else:
        verdict_label = "HIGH"
        verdict_text  = "significant protease risk; shio-koji format is likely to degrade lactoferrin"

    if mature_verdict == "LOW":
        mature_text = "mature lactoferrin (aa 20–710) is structurally resistant; risk is signal-peptide-contingent"
    elif mature_verdict == "MODERATE":
        mature_text = "partial degradation of the mature protein is possible even after signal peptide cleavage"
    else:
        mature_text = "significant risk to mature lactoferrin independent of signal peptide processing"

    lines += [
        "---",
        "",
        "## Overall Risk Verdict",
        "",
        "| Scope | Verdict | Max risk score | Worst protease |",
        "|---|---|---|---|",
        f"| Full sequence (incl. signal peptide) | **{verdict_label}** | {worst_score} | `{worst}` |",
        f"| Mature protein only (aa 20–710) | **{mature_verdict}** | {mature_score} | `{mature_worst}` |",
        "",
        f"**Full-sequence verdict: {verdict_label}** — {verdict_text}",
        "",
        f"**Mature-protein verdict: {mature_verdict}** — {mature_text}",
        "",
        f"All full-sequence top-5 sites are in the signal peptide (aa 1–19, pLDDT 35–54). "
        f"If A. oryzae signal peptidase processes the heterologous lactoferrin signal peptide, "
        f"the operative risk is {mature_verdict} ({mature_score} max). "
        f"If signal peptide is retained (uncertain), full-sequence verdict ({verdict_label}) applies.",
        "",
        "### Key structural factors",
        "",
        "**Signal peptide (aa 1–19):** pLDDT 35–54 throughout — fully disordered. "
        "If the signal peptide is retained in the A. oryzae expression product (i.e., not cleaved by the host secretory machinery), "
        "these residues are fully exposed and represent high-accessibility cleavage targets. "
        "In the native mammalian context the signal peptide is co-translationally cleaved; "
        "A. oryzae has its own signal peptidase activity but processing of heterologous signal sequences is not guaranteed.",
        "",
        "**Inter-lobe linker (approx aa 432–445):** pLDDT 68–81 — partially exposed. "
        "This region connects the N-lobe and C-lobe of lactoferrin and is structurally less constrained than either lobe core. "
        "Partial exposure here means recognition sites in this window have non-trivial accessibility scores, "
        "unlike the buried sites that dominate the uricase analysis.",
        "",
        "**Lobe cores (majority of residues):** pLDDT 88–99 — well-folded. "
        "The two lobes themselves are tightly folded, comparable to uricase. "
        "Protease risk within the lobe cores is low.",
        "",
        "### Limitations",
        "",
        "- pLDDT ≠ solvent accessibility. Signal peptide pLDDT scores accurately predict disorder; "
        "linker region pLDDT 68–81 indicates partial exposure but SASA calculation would quantify it.",
        "- Signal peptide processing in A. oryzae is uncertain. "
        "If cleaved, the exposed aa 1–19 region is removed and risk drops. "
        "If retained, it is the dominant vulnerability.",
        "- Glycosylation not modelled. Native lactoferrin carries N-linked glycans that may shield "
        "surface-accessible sites; heterologously expressed lactoferrin in A. oryzae may have different "
        "glycosylation patterns than the native human protein.",
        "- P1/P1' rules only. Extended subsite specificity (P2–P4) not modelled.",
        "- ALP and NPr pH factors conservatively set to 1.0 (see comp-001 limitations). "
        "True risk from ALP/NPr is lower than computed.",
        "- Iron-binding state not modelled. Apo-lactoferrin (iron-free) adopts a more open conformation "
        "than holo-lactoferrin, potentially exposing additional surface residues. "
        "Iron availability in shio-koji is uncertain; this analysis models the AlphaFold holo-like structure.",
        "",
        "### Comparison with comp-001 (uricase)",
        "",
        "| Feature | Uricase (comp-001) | Lactoferrin (comp-005) |",
        "|---|---|---|",
        f"| Mean pLDDT | 97.1 | {ss['mean_plddt']} |",
        f"| Min pLDDT | 80.5 | {ss['min_plddt']} |",
        f"| % residues pLDDT > 80 | 100% | {ss['pct_residues_above_80']}% |",
        "| Exposed sites (any protease) | 0 | see per-protease table |",
        "| Signal peptide risk | None (not present in mature form) | Present if unprocessed |",
        "| Inter-lobe linker | N/A (homotetramer, no bilobal structure) | Partially exposed |",
        f"| Full-sequence verdict | LOW (provisional) | {verdict_label} |",
        f"| Mature-protein verdict (excl. signal peptide) | LOW (provisional) | {mature_verdict} |",
        "",
        "### Impact on §1.10 experimental framing",
        "",
        "Unlike uricase, this analysis does **not** shift §1.10's lactoferrin arm from a feasibility gate "
        "to a confirmation experiment. Exposed sites in the signal peptide and partially exposed sites in the "
        "inter-lobe linker represent genuine structural vulnerability. The wet-lab §1.10 result for lactoferrin "
        "is the primary determination — this computational analysis identifies *where* to look (signal peptide "
        "cleavage, linker degradation) if degradation is observed.",
        "",
        "---",
        "",
        "*Generated by `analyze.py` on 2026-05-05. Uses experiments/lib/protease_stability.py. "
        "Re-run after any AlphaFold model update or MEROPS specificity revision. "
        "See inputs/provenance.md for data sources.*",
    ]

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
