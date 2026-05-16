#!/usr/bin/env python3
"""
comp-006: DAF/CD55 protease stability in shio-koji fermentation

Orchestrator — loads inputs, calls shared library, writes comp-006-specific outputs.
Core algorithm lives in experiments/lib/protease_stability.py.

Usage: python3 analyze.py   (from this directory)
Outputs: outputs/cleavage_sites.json, outputs/summary.md

Three verdicts are computed — this is the key extension beyond comp-005's two-verdict logic:
  1. Full sequence (aa 1-381): includes signal peptide + propeptide; worst-case.
  2. Mature protein (aa 35-381): excludes signal peptide (aa 1-34); propeptide still present.
  3. Soluble ectodomain (aa 35-353): the operationally relevant construct for A. oryzae expression.
     Excludes the signal peptide (replaced by koji-native signal in engineered construct) and the
     GPI-anchor propeptide (aa 354-381, truncated to produce a secreted soluble protein).
     The Ser/Thr-rich stalk (aa 286-353) is fully disordered in this window — the dominant risk region.

UniProt P08174 SV=4 annotation boundaries:
  Signal peptide: aa 1-34
  Mature chain:   aa 35-353
  Propeptide (GPI-anchor signal): aa 354-381
  GPI-anchor amidation: Ser353

SCR domain boundaries:
  SCR1: aa 35-96
  SCR2: aa 97-160
  SCR3: aa 161-222
  SCR4: aa 223-285
  Ser/Thr-rich stalk: aa 286-353 (disordered, heavily O-glycosylated in vivo)
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

# UniProt P08174 annotation boundaries (verified against SV=4)
SIGNAL_PEPTIDE_END   = 34   # aa 1-34 cleaved during secretion
PROPEPTIDE_START     = 354  # aa 354-381: GPI-anchor signal, cleaved in vivo; omitted in soluble construct
ECTODOMAIN_START     = 35   # first residue of mature chain
ECTODOMAIN_END       = 353  # last residue of soluble ectodomain (Ser353, GPI-amidation site in native protein)

# Stalk region (Ser/Thr-rich, heavily O-glycosylated, fully disordered in AlphaFold)
STALK_START = 286
STALK_END   = 353


def classify_cd55_region(position):
    """Map position to CD55 structural region for site annotation."""
    if position <= SIGNAL_PEPTIDE_END:
        return "signal_peptide"
    elif position <= 96:
        return "SCR1"
    elif position <= 160:
        return "SCR2"
    elif position <= 222:
        return "SCR3"
    elif position <= 285:
        return "SCR4"
    elif position <= ECTODOMAIN_END:
        return "Ser/Thr_stalk"
    else:
        return "GPI_propeptide"


def verdict_label(max_score):
    if max_score < 0.15:
        return "LOW"
    elif max_score < 0.30:
        return "MODERATE"
    else:
        return "HIGH"


def main():
    seq       = load_sequence(INPUTS / "P08174.fasta")
    plddt     = load_plddt(INPUTS / "alphafold_P08174_plddt.json")
    proteases, conditions = load_proteases(INPUTS / "protease_specificities.json")

    sequence_stats   = compute_sequence_stats(plddt)
    protease_results = run_all_proteases(seq, plddt, proteases, conditions)

    nacl_pct = conditions["NaCl_pct"]

    # Annotate top-5 sites with CD55 structural region; compute per-scope risk scores.
    for name, result in protease_results.items():
        for site in result["top_5_sites"]:
            site["region"] = classify_cd55_region(site["position"])

        all_sites = find_cleavage_sites(seq, proteases[name], plddt, nacl_pct)

        # Mature protein: exclude signal peptide (aa 1-34); propeptide retained
        mature_sites = [s for s in all_sites if s["position"] > SIGNAL_PEPTIDE_END]
        result["mature_protein_max_risk_score"]   = round(mature_sites[0]["risk_score"], 3) if mature_sites else 0
        result["mature_protein_exposed_sites"]    = sum(1 for s in mature_sites if s["accessibility"] == "exposed")

        # Soluble ectodomain: aa 35-353 only — the engineered construct
        ecto_sites = [s for s in all_sites
                      if ECTODOMAIN_START <= s["position"] <= ECTODOMAIN_END]
        result["ecto_max_risk_score"]   = round(ecto_sites[0]["risk_score"], 3) if ecto_sites else 0
        result["ecto_exposed_sites"]    = sum(1 for s in ecto_sites if s["accessibility"] == "exposed")
        result["ecto_partially_exposed_sites"] = sum(1 for s in ecto_sites if s["accessibility"] == "partially_exposed")

        # Stalk-only (aa 286-353): most disordered sub-region within ectodomain
        stalk_sites = [s for s in ecto_sites
                       if STALK_START <= s["position"] <= STALK_END]
        result["stalk_max_risk_score"]  = round(stalk_sites[0]["risk_score"], 3) if stalk_sites else 0
        result["stalk_exposed_sites"]   = sum(1 for s in stalk_sites if s["accessibility"] == "exposed")

    # Full-sequence verdict (includes signal peptide + propeptide)
    full_max_risks  = {n: r["max_risk_score"] for n, r in protease_results.items()}
    full_worst      = max(full_max_risks, key=full_max_risks.get)
    full_worst_score = full_max_risks[full_worst]
    full_verdict    = verdict_label(full_worst_score)

    # Mature protein verdict (excludes signal peptide only)
    mature_max_risks   = {n: r["mature_protein_max_risk_score"] for n, r in protease_results.items()}
    mature_worst       = max(mature_max_risks, key=mature_max_risks.get)
    mature_worst_score = mature_max_risks[mature_worst]
    mature_verdict     = verdict_label(mature_worst_score)

    # Soluble ectodomain verdict (aa 35-353; the engineering-relevant scope)
    ecto_max_risks   = {n: r["ecto_max_risk_score"] for n, r in protease_results.items()}
    ecto_worst       = max(ecto_max_risks, key=ecto_max_risks.get)
    ecto_worst_score = ecto_max_risks[ecto_worst]
    ecto_verdict     = verdict_label(ecto_worst_score)

    output = {
        "protein":                    "DAF/CD55 (complement decay-accelerating factor), Homo sapiens (P08174)",
        "alphafold_model":            "AF-P08174-F1-model_v6",
        "signal_peptide_aa":          f"1-{SIGNAL_PEPTIDE_END} (cleaved during secretion; "
                                      "replaced by koji-native signal in engineered construct)",
        "gpi_propeptide_aa":          f"{PROPEPTIDE_START}-381 (cleaved during GPI attachment in vivo; "
                                      "truncated in soluble ectodomain engineering construct)",
        "soluble_ectodomain_aa":      f"{ECTODOMAIN_START}-{ECTODOMAIN_END} (SCR1-4 + Ser/Thr stalk; "
                                      "the operationally relevant construct for koji expression)",
        "conditions":                 conditions,
        "sequence_stats":             sequence_stats,
        "protease_results":           protease_results,
        "full_sequence_verdict":       full_verdict,
        "full_sequence_worst_score":   full_worst_score,
        "full_sequence_worst_protease": full_worst,
        "mature_protein_verdict":      mature_verdict,
        "mature_protein_worst_score":  mature_worst_score,
        "mature_protein_worst_protease": mature_worst,
        "ecto_verdict":                ecto_verdict,
        "ecto_worst_score":            ecto_worst_score,
        "ecto_worst_protease":         ecto_worst,
    }

    with open(OUTPUTS / "cleavage_sites.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output, OUTPUTS / "summary.md")
    print("Done. Outputs written to outputs/")


def write_summary(data, path):
    ss              = data["sequence_stats"]
    cond            = data["conditions"]
    pr              = data["protease_results"]
    full_verdict    = data["full_sequence_verdict"]
    full_score      = data["full_sequence_worst_score"]
    full_worst      = data["full_sequence_worst_protease"]
    mature_verdict  = data["mature_protein_verdict"]
    mature_score    = data["mature_protein_worst_score"]
    mature_worst    = data["mature_protein_worst_protease"]
    ecto_verdict    = data["ecto_verdict"]
    ecto_score      = data["ecto_worst_score"]
    ecto_worst      = data["ecto_worst_protease"]

    lines = [
        "# comp-006 — DAF/CD55 Shio-Koji Protease Stability: Summary",
        "",
        f"**Protein:** {data['protein']}  ",
        f"**AlphaFold model:** {data['alphafold_model']}  ",
        f"**Signal peptide:** {data['signal_peptide_aa']}  ",
        f"**GPI-anchor propeptide:** {data['gpi_propeptide_aa']}  ",
        f"**Soluble ectodomain:** {data['soluble_ectodomain_aa']}  ",
        f"**Conditions modeled:** {cond['NaCl_pct']}% NaCl, pH {cond['pH_range'][0]}–{cond['pH_range'][1]}, {cond['temperature_C']}°C, {cond['duration_days'][0]}–{cond['duration_days'][1]} days  ",
        f"**Analysis date:** 2026-05-05  ",
        f"**Script:** `experiments/comp-006-daf-cd55-shio-koji-protease-stability/analyze.py`  ",
        f"**Library:** `experiments/lib/protease_stability.py`  ",
        "",
        "---",
        "",
        "## Structural Overview",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Sequence length | {ss['length']} aa (incl. signal peptide aa 1–34 and GPI propeptide aa 354–381) |",
        f"| Mean pLDDT (AlphaFold confidence) | {ss['mean_plddt']} / 100 |",
        f"| Minimum pLDDT (most flexible residue) | {ss['min_plddt']} / 100 |",
        f"| % residues pLDDT > 80 (well-folded) | {ss['pct_residues_above_80']}% |",
        f"| % residues pLDDT > 90 (core-folded) | {ss['pct_residues_above_90']}% |",
        "",
        "**CD55 structural notes:**",
        "",
        "- Signal peptide (aa 1–34): pLDDT 43–72 — disordered throughout. "
        "Residue 34 (pLDDT 71.6) is partially exposed at the border; aa 1–33 are fully disordered.",
        "- SCR1–SCR4 (aa 35–285): pLDDT 85–98 — well-folded. "
        "The four sushi/SCR domains are compact and structurally similar to the comp-001 uricase core.",
        "- Ser/Thr-rich stalk (aa 286–353): pLDDT progressively drops from ~91 at aa 285 to <50 below "
        "aa 288 — fully disordered. This is the dominant structural liability for the ectodomain verdict.",
        "- GPI-anchor propeptide (aa 354–381): pLDDT 30–52 — fully disordered. Absent from the "
        "soluble ectodomain engineering construct.",
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
            f"| Max risk score (full sequence, 0–1) | {r['max_risk_score']} |",
            f"| Mature protein max risk score (excl. signal peptide) | {r.get('mature_protein_max_risk_score', 'n/a')} |",
            f"| Soluble ectodomain max risk score (aa 35–353) | {r.get('ecto_max_risk_score', 'n/a')} |",
            f"| Ectodomain exposed sites | {r.get('ecto_exposed_sites', 'n/a')} |",
            f"| Stalk max risk score (aa 286–353) | {r.get('stalk_max_risk_score', 'n/a')} |",
            f"| Stalk exposed sites | {r.get('stalk_exposed_sites', 'n/a')} |",
            "",
        ]
        if r["top_5_sites"]:
            lines += [
                "**Top 5 highest-risk cleavage sites (full sequence):**",
                "",
                "| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |",
                "|---|---|---|---|---|---|---|",
            ]
            for s in r["top_5_sites"]:
                region = s.get("region", "unknown")
                lines.append(
                    f"| {s['position']} | {region} | {s['P1']} | {s['P1_prime']} | "
                    f"{s['mean_plddt_window']} | {s['accessibility']} | {s['risk_score']} |"
                )
            lines.append("")

    # Verdict text
    def full_text(v):
        if v == "LOW":
            return "protease degradation of DAF/CD55 in shio-koji is unlikely to meaningfully reduce activity"
        elif v == "MODERATE":
            return "partial degradation is possible, particularly at disordered stalk and signal-peptide sites"
        else:
            return "significant protease risk; disordered regions are high-accessibility targets"

    def mature_text(v):
        if v == "LOW":
            return "mature CD55 (aa 35–381, incl. propeptide) is largely resistant once signal peptide is removed"
        elif v == "MODERATE":
            return "partial degradation of mature CD55 is possible even after signal peptide cleavage"
        else:
            return "significant risk to mature CD55 independent of signal peptide processing"

    def ecto_text(v):
        if v == "LOW":
            return "the soluble ectodomain (SCR1–4 + stalk, aa 35–353) is protease-stable under shio-koji conditions; the SCR domains are well-folded and the stalk is the dominant but still-limited vulnerability"
        elif v == "MODERATE":
            return "partial degradation of the soluble ectodomain is possible; the fully disordered stalk (aa 286–353) is the primary vulnerability, not the SCR domains"
        else:
            return "significant risk to the soluble ectodomain; the stalk region drives the verdict and warrants engineering attention"

    lines += [
        "---",
        "",
        "## Overall Risk Verdict",
        "",
        "| Scope | Verdict | Max risk score | Worst protease |",
        "|---|---|---|---|",
        f"| Full sequence (aa 1–381, incl. signal peptide + propeptide) | **{full_verdict}** | {full_score} | `{full_worst}` |",
        f"| Mature protein (aa 35–381, excl. signal peptide) | **{mature_verdict}** | {mature_score} | `{mature_worst}` |",
        f"| Soluble ectodomain (aa 35–353, excl. signal peptide + propeptide) | **{ecto_verdict}** | {ecto_score} | `{ecto_worst}` |",
        "",
        f"**Full-sequence verdict: {full_verdict}** — {full_text(full_verdict)}",
        "",
        f"**Mature-protein verdict: {mature_verdict}** — {mature_text(mature_verdict)}",
        "",
        f"**Soluble ectodomain verdict: {ecto_verdict}** — {ecto_text(ecto_verdict)}",
        "",
        "The soluble ectodomain verdict is the operationally relevant figure for the koji engineering question. "
        "The engineered construct replaces aa 1–34 (human signal peptide) with a koji-native secretion signal "
        "and terminates at aa 353, omitting the GPI-anchor propeptide (aa 354–381). "
        "Whether the stalk (aa 286–353) is retained or truncated further is an engineering choice — "
        "the stalk is required for membrane-proximal complement regulation in the native context but "
        "its requirement for ectodomain folding or activity in a soluble secreted form is unknown.",
        "",
        "### Key structural factors",
        "",
        "**Signal peptide (aa 1–34):** pLDDT 43–72 throughout — fully disordered. "
        "Highest-risk sites in the full-sequence analysis map here. "
        "In the engineered construct, the human signal peptide is replaced with the koji-native "
        "α-amylase signal (Ward 1995), so this region is not present in the expressed product.",
        "",
        "**SCR1–SCR4 (aa 35–285):** pLDDT 85–98 — well-folded, comparable to uricase (comp-001). "
        "The four sushi domains are compact, disulfide-stabilized (3 disulfides per SCR), "
        "and represent structurally resistant regions. Recognition sites here are largely buried. "
        "Note: disulfide bonds are not modelled in this analysis — see Limitations.",
        "",
        "**Ser/Thr-rich stalk (aa 286–353):** pLDDT drops sharply from ~91 at aa 285 to <65 by aa 288, "
        "and remains fully disordered (pLDDT 30–52) through aa 353. "
        "This is the dominant structural liability within the soluble ectodomain. "
        "In vivo, this region carries extensive O-linked glycans that likely shield the backbone; "
        "A. oryzae O-glycosylation patterns differ substantially from mammalian and may not provide "
        "the same shielding.",
        "",
        "**GPI-anchor propeptide (aa 354–381):** pLDDT 30–52 — fully disordered. "
        "Present in the full-sequence and mature-protein verdicts, absent in the soluble ectodomain verdict. "
        "In the native context, this region is post-translationally cleaved during GPI attachment.",
        "",
        "### Limitations",
        "",
        "- **Disulfide bonds not modelled.** Each SCR domain contains 3 conserved disulfide bonds "
        "(6 Cys per domain). Disulfide cross-linking substantially reduces backbone flexibility and "
        "proteolytic accessibility beyond what pLDDT alone captures. This analysis likely "
        "**overestimates risk in the SCR domains** relative to the disulfide-bonded native fold.",
        "- **O-glycosylation of the stalk not modelled.** The Ser/Thr-rich stalk (aa 286–353) carries "
        "dense O-linked glycans in the native context. Glycans sterically shield the polypeptide backbone; "
        "A. oryzae O-glycosylation may differ from mammalian. If the stalk is expressed without glycans "
        "or with non-shielding glycans, backbone accessibility increases. Stalk risk is likely "
        "**underestimated by this analysis for non-glycosylated constructs** and possibly overestimated "
        "for fully glycosylated constructs.",
        "- **Stalk engineering option.** The stalk (aa 286–353) is a linker between SCR4 and the "
        "GPI anchor — it has no known enzymatic or binding function. A soluble ectodomain construct "
        "could truncate at aa 285 (end of SCR4), removing the stalk entirely. "
        "This would eliminate the dominant disordered region and likely shift the verdict toward LOW. "
        "comp-006 does not model the truncated variant; a comp-007 analysis of the SCR1-4-only "
        "construct (aa 35–285) would be the logical follow-up.",
        "- **pLDDT ≠ solvent accessibility.** Stalk pLDDT accurately predicts disorder; "
        "SCR pLDDT 85–98 predicts well-folded but SASA calculation would quantify surface exposure of "
        "buried-vs-solvent-accessible loops more precisely.",
        "- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled; may over-count "
        "recognition sites in the SCR domains.",
        "- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range "
        "(6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge. True activity of both is lower "
        "than modelled; risk is conservatively overstated for both.",
        "",
        "### Comparison with comp-001 (uricase) and comp-005 (lactoferrin)",
        "",
        "| Feature | Uricase (comp-001) | Lactoferrin (comp-005) | CD55 ectodomain (comp-006) |",
        "|---|---|---|---|",
        f"| Analyzed length | 301 aa | 710 aa | 381 aa |",
        f"| Mean pLDDT | 97.1 | 95.0 | {ss['mean_plddt']} |",
        f"| Min pLDDT | 80.5 | 35.8 | {ss['min_plddt']} |",
        f"| % residues pLDDT > 80 | 100% | 96.1% | {ss['pct_residues_above_80']}% |",
        "| Signal peptide | None | Present (aa 1–19) | Present (aa 1–34) |",
        "| GPI propeptide / other disordered region | None | Inter-lobe linker (partial) | GPI propeptide + stalk (both fully disordered) |",
        "| Disulfide bonds | Uricase has no Cys | 2 per lobe (functional) | 3 per SCR domain (12 total in SCR1-4) |",
        "| Full-sequence verdict | LOW | HIGH | see output |",
        "| Mature-protein verdict | LOW | MODERATE | see output |",
        f"| Soluble ectodomain verdict | N/A | N/A | **{ecto_verdict}** (max {ecto_score}) |",
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
