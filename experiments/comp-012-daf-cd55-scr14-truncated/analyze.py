#!/usr/bin/env python3
"""
comp-012: DAF/CD55 SCR1-4 truncated construct — shio-koji protease stability

Orchestrator — loads inputs, subsets to the SCR1-4-only construct (aa 35-285),
calls shared library, writes comp-012-specific outputs.
Core algorithm lives in experiments/lib/protease_stability.py.

Usage: python3 analyze.py   (from this directory)
Outputs: outputs/cleavage_sites.json, outputs/summary.md

Motivation: comp-006 found the full DAF/CD55 ectodomain (aa 35-353) is HIGH protease
risk in shio-koji conditions. The driver was the Ser/Thr-rich stalk (aa 286-353,
pLDDT 30-52) — the SCR1-4 domains (aa 35-285, pLDDT 85-98) contributed ZERO exposed
sites across all three proteases. This experiment tests the stalk-truncated construct
and computes the verdict for SCR1-4 only.

Construct details:
  SCR14_START = 35  (first residue of SCR1; immediately follows signal peptide)
  SCR14_END   = 285 (last residue of SCR4; immediately precedes the stalk)
  Length: 251 residues (aa 35-285 inclusive)

  Signal peptide (aa 1-34): replaced by koji-native secretion signal in engineered construct
  Stalk (aa 286-353): truncated; present in comp-006 but absent here
  GPI propeptide (aa 354-381): absent (same as comp-006 ectodomain)

UniProt P08174 SV=4 SCR domain boundaries:
  SCR1: aa 35-96
  SCR2: aa 97-160
  SCR3: aa 161-222
  SCR4: aa 223-285
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
    find_cleavage_sites,
    summarize_protease,
)

INPUTS  = Path(__file__).parent / "inputs"
OUTPUTS = Path(__file__).parent / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# Truncation boundaries — the only construct analyzed in comp-012
SCR14_START = 35   # first residue of SCR1 (1-indexed, UniProt P08174)
SCR14_END   = 285  # last residue of SCR4 (1-indexed, UniProt P08174)

# Named SCR domain boundaries (1-indexed, from UniProt P08174 SV=4)
SCR_DOMAINS = {
    "SCR1": (35, 96),
    "SCR2": (97, 160),
    "SCR3": (161, 222),
    "SCR4": (223, 285),
}


def classify_cd55_scr14_region(position):
    """Map position (1-indexed, full-sequence coordinates) to SCR domain."""
    for name, (start, end) in SCR_DOMAINS.items():
        if start <= position <= end:
            return name
    return "unknown"


def verdict_label(max_score):
    if max_score < 0.15:
        return "LOW"
    elif max_score < 0.30:
        return "MODERATE"
    else:
        return "HIGH"


def main():
    # Load full-sequence data (381 aa)
    full_seq   = load_sequence(INPUTS / "P08174.fasta")
    full_plddt = load_plddt(INPUTS / "alphafold_P08174_plddt.json")
    proteases, conditions = load_proteases(INPUTS / "protease_specificities.json")

    # Subset to SCR1-4 (aa 35-285) — 251 residues
    # Python string is 0-indexed: seq[34:285] gives aa 35-285 (inclusive)
    scr14_seq = full_seq[SCR14_START - 1 : SCR14_END]
    assert len(scr14_seq) == SCR14_END - SCR14_START + 1, (
        f"Expected {SCR14_END - SCR14_START + 1} residues, got {len(scr14_seq)}"
    )

    # pLDDT subset: keys 35-285 (1-indexed in full_plddt)
    # find_cleavage_sites uses plddt keyed from 1 for the *provided* sequence.
    # We rebuild a 1-indexed pLDDT dict for the subsetted sequence.
    scr14_plddt = {
        (pos - SCR14_START + 1): full_plddt[pos]
        for pos in range(SCR14_START, SCR14_END + 1)
        if pos in full_plddt
    }
    assert len(scr14_plddt) == len(scr14_seq), (
        f"pLDDT key count {len(scr14_plddt)} does not match sequence length {len(scr14_seq)}"
    )

    # Sequence stats for the SCR1-4 subset only
    scr14_stats = compute_sequence_stats(scr14_plddt)

    nacl_pct = conditions["NaCl_pct"]

    # Run all proteases against the SCR1-4 subset
    protease_results = {}
    for name, pdata in proteases.items():
        sites = find_cleavage_sites(scr14_seq, pdata, scr14_plddt, nacl_pct)
        result = summarize_protease(sites, pdata, conditions)

        # Annotate top-5 sites with SCR domain (using 1-indexed coords within subsetted seq,
        # then mapping back to full-sequence coords for readability)
        for site in result["top_5_sites"]:
            local_pos   = site["position"]                       # 1-indexed within SCR1-4
            full_pos    = local_pos + SCR14_START - 1            # 1-indexed in full P08174 sequence
            site["full_sequence_position"] = full_pos
            site["region"] = classify_cd55_scr14_region(full_pos)

        protease_results[name] = result

    # Single verdict: the only construct is SCR1-4 (aa 35-285)
    max_risks = {n: r["max_risk_score"] for n, r in protease_results.items()}
    worst_protease = max(max_risks, key=max_risks.get)
    worst_score    = max_risks[worst_protease]
    verdict        = verdict_label(worst_score)

    output = {
        "experiment":         "comp-012",
        "protein":            "DAF/CD55 (complement decay-accelerating factor), Homo sapiens (P08174)",
        "alphafold_model":    "AF-P08174-F1-model_v6 (source; pLDDT subset to aa 35-285)",
        "construct":          f"SCR1-4 only (aa {SCR14_START}-{SCR14_END}; stalk aa 286-353 removed)",
        "construct_length_aa": len(scr14_seq),
        "conditions":         conditions,
        "scr14_sequence_stats": scr14_stats,
        "protease_results":   protease_results,
        "verdict":            verdict,
        "worst_score":        round(worst_score, 3),
        "worst_protease":     worst_protease,
        # Cross-reference to comp-006 (full ectodomain) for comparison
        "comp006_reference": {
            "full_ecto_verdict":        "HIGH",
            "full_ecto_worst_score":    0.388,
            "full_ecto_worst_protease": "NPr",
            "full_ecto_scope":          "aa 35-353 (SCR1-4 + stalk)",
            "stalk_exposed_sites_NPr":  9,
            "stalk_exposed_sites_ALP":  48,
            "stalk_exposed_sites_acid": 1,
        },
    }

    with open(OUTPUTS / "cleavage_sites.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output, OUTPUTS / "summary.md")
    print(f"Done. Construct length: {len(scr14_seq)} aa (aa 35-285). Outputs written to outputs/")
    print(f"Verdict: {verdict} (max risk score: {round(worst_score, 3)}, worst protease: {worst_protease})")


def write_summary(data, path):
    ss       = data["scr14_sequence_stats"]
    cond     = data["conditions"]
    pr       = data["protease_results"]
    verdict  = data["verdict"]
    score    = data["worst_score"]
    worst    = data["worst_protease"]
    c6       = data["comp006_reference"]

    def verdict_text(v):
        if v == "LOW":
            return ("protease degradation of the DAF/CD55 SCR1-4 construct is unlikely to "
                    "meaningfully reduce activity under shio-koji fermentation conditions. "
                    "The stalk truncation is validated as a stability-conferring engineering choice.")
        elif v == "MODERATE":
            return ("partial degradation of the DAF/CD55 SCR1-4 construct is possible. "
                    "Risk is lower than the full ectodomain but warrants caution. "
                    "Buried sites in the SCR domains remain the only cleavage targets.")
        else:
            return ("significant protease risk persists even in the stalk-truncated construct. "
                    "SCR domain sites are more accessible than expected from pLDDT alone — "
                    "disulfide geometry or extended subsite specificity may explain the discrepancy.")

    lines = [
        "# comp-012 — DAF/CD55 SCR1-4 Truncated Construct: Shio-Koji Protease Stability",
        "",
        f"**Protein:** {data['protein']}  ",
        f"**AlphaFold model:** {data['alphafold_model']}  ",
        f"**Construct:** {data['construct']}  ",
        f"**Construct length analyzed:** {data['construct_length_aa']} aa (aa 35–285 inclusive)  ",
        f"**Conditions modeled:** {cond['NaCl_pct']}% NaCl, pH {cond['pH_range'][0]}–{cond['pH_range'][1]}, {cond['temperature_C']}°C, {cond['duration_days'][0]}–{cond['duration_days'][1]} days  ",
        f"**Analysis date:** 2026-05-05  ",
        f"**Script:** `experiments/comp-012-daf-cd55-scr14-truncated/analyze.py`  ",
        f"**Library:** `experiments/lib/protease_stability.py`  ",
        "",
        "---",
        "",
        "## Overall Verdict",
        "",
        f"### DAF/CD55 SCR1-4 (aa 35–285): **{verdict}**",
        "",
        f"Max risk score: **{score}** (worst protease: `{worst}`)  ",
        "",
        verdict_text(verdict),
        "",
        "---",
        "",
        "## Comparison with comp-006 (Full Ectodomain aa 35–353)",
        "",
        "| Scope | Verdict | Max risk score | Worst protease |",
        "|---|---|---|---|",
        f"| comp-006: Soluble ectodomain (aa 35–353, SCR1-4 + stalk) | **{c6['full_ecto_verdict']}** | {c6['full_ecto_worst_score']} | `{c6['full_ecto_worst_protease']}` |",
        f"| comp-012: SCR1-4 only (aa 35–285, stalk removed) | **{verdict}** | {score} | `{worst}` |",
        "",
        "**Sites eliminated by the stalk truncation (comp-006 stalk-exposed sites removed in comp-012):**",
        "",
        f"| Protease | Stalk exposed sites removed | Outcome |",
        "|---|---|---|",
        f"| ALP (alkaline subtilisin) | {c6['stalk_exposed_sites_ALP']} | All eliminated |",
        f"| NPr (neutral metalloprotease) | {c6['stalk_exposed_sites_NPr']} | All eliminated |",
        f"| acid_protease (aspergillopepsin) | {c6['stalk_exposed_sites_acid']} | All eliminated |",
        "",
        "The stalk truncation removes every exposed site from every protease in the ectodomain analysis. "
        "Only buried and partially exposed SCR-domain sites remain in comp-012.",
        "",
        "---",
        "",
        "## Structural Overview — SCR1-4 Construct",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Sequence length analyzed | {ss['length']} aa (aa 35–285) |",
        f"| Mean pLDDT (AlphaFold confidence) | {ss['mean_plddt']} / 100 |",
        f"| Minimum pLDDT (most flexible residue) | {ss['min_plddt']} / 100 |",
        f"| % residues pLDDT > 80 (well-folded) | {ss['pct_residues_above_80']}% |",
        f"| % residues pLDDT > 90 (core-folded) | {ss['pct_residues_above_90']}% |",
        "",
        "**Structural notes:**",
        "",
        "- SCR1 (aa 35–96): pLDDT 85–98 — well-folded. Inter-SCR junction (aa 83–96) pLDDT 89–96.",
        "- SCR2 (aa 97–160): pLDDT 90–98 — well-folded. Minor dip at aa 99–102 (~91) at interdomain connection.",
        "- SCR3 (aa 161–222): pLDDT 97–98 — the most confidently modelled region. All sites buried.",
        "- SCR4 (aa 223–285): pLDDT 91–98 — well-folded. Minor reduction at aa 270–272 (~93–94).",
        "- Construct terminates at aa 285 (end of SCR4). No stalk, no GPI propeptide.",
        "- In the engineered A. oryzae construct, the human signal peptide (aa 1–34) is replaced by "
        "the koji-native α-amylase signal (Ward et al. 1995); aa 1–34 are not present in the expressed product.",
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
            f"| Recognition sites in SCR1-4 construct | {r['total_recognition_sites']} |",
            f"| Buried (pLDDT ≥ 80) | {r['buried_sites']} |",
            f"| Partially exposed (pLDDT 65–80) | {r['partially_exposed_sites']} |",
            f"| Exposed (pLDDT < 65) | {r['exposed_sites']} |",
            f"| Residual activity at {cond['NaCl_pct']}% NaCl | {r['salt_residual_activity_at_nacl']*100:.0f}% |",
            f"| pH activity factor (shio-koji pH) | {r['ph_activity_factor']*100:.0f}% |",
            f"| Effective protease activity (salt × pH) | {r['effective_activity']*100:.1f}% |",
            f"| Max risk score (SCR1-4 construct, 0–1) | {r['max_risk_score']} |",
            "",
        ]
        if r["top_5_sites"]:
            lines += [
                "**Top 5 highest-risk cleavage sites (SCR1-4 construct):**",
                "",
                "| Local pos | Full-seq pos | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |",
                "|---|---|---|---|---|---|---|---|",
            ]
            for s in r["top_5_sites"]:
                region   = s.get("region", "unknown")
                full_pos = s.get("full_sequence_position", "n/a")
                lines.append(
                    f"| {s['position']} | {full_pos} | {region} | {s['P1']} | {s['P1_prime']} | "
                    f"{s['mean_plddt_window']} | {s['accessibility']} | {s['risk_score']} |"
                )
            lines.append("")
        else:
            lines.append("*No recognition sites found in this construct.*\n")

    lines += [
        "---",
        "",
        "## Limitations",
        "",
        "- **Disulfide bonds not modelled.** Each SCR domain contains 3 conserved disulfide bonds "
        "(6 Cys per domain, 12 total in SCR1–4). Disulfide cross-linking reduces backbone flexibility "
        "and proteolytic accessibility substantially beyond what pLDDT captures. This analysis likely "
        "**overestimates risk in the SCR domains** — partially and even some 'exposed' sites may be "
        "disulfide-locked and inaccessible in the native fold.",
        "- **pLDDT ≠ solvent accessibility.** pLDDT 85–98 predicts well-folded regions but cannot "
        "distinguish buried residues from surface-exposed loops at domain interfaces. SASA calculation "
        "on the AlphaFold structure would refine the partially-exposed site count.",
        "- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled. May over-count "
        "recognition sites in the SCR domains where extended context is unfavorable.",
        "- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range "
        "(pH 6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge. True activity is lower; "
        "risk is conservatively overstated for both.",
        "- **CCP-regulatory activity not assessable in silico.** Whether the stalk-truncated SCR1-4 "
        "construct retains the ability to inhibit C3b deposition, accelerate CP/AP C3 convertase decay, "
        "or reduce C5a generation in a gut-lumen environment is a wet-lab question. Structural integrity "
        "is necessary but not sufficient for functional complement regulation.",
        "- **O-glycosylation not modelled.** The SCR domains carry N-linked glycans; stalk O-glycans "
        "are absent from this construct (by design). Glycosylation patterns in A. oryzae differ from "
        "human; net effect on stability and function is unknown.",
        "",
        "---",
        "",
        "### Comparison with uricase (comp-001), lactoferrin (comp-005), and CD55 ectodomain (comp-006)",
        "",
        "| Feature | Uricase (comp-001) | Lactoferrin (comp-005) | CD55 ectodomain (comp-006) | CD55 SCR1-4 (comp-012) |",
        "|---|---|---|---|---|",
        f"| Construct length | 301 aa | 710 aa | 319 aa (aa 35–353) | {ss['length']} aa (aa 35–285) |",
        f"| Mean pLDDT | 97.1 | 95.0 | 78.3 (full ecto) | {ss['mean_plddt']} |",
        f"| Min pLDDT | 80.5 | 35.8 | 29.9 (full ecto) | {ss['min_plddt']} |",
        f"| % pLDDT > 80 | 100% | 96.1% | 65.9% (full ecto) | {ss['pct_residues_above_80']}% |",
        "| Dominant disordered region | None | Signal peptide | Ser/Thr stalk (aa 286–353) | None (stalk removed) |",
        f"| Verdict | LOW | HIGH/MODERATE | HIGH | **{verdict}** |",
        "",
        "---",
        "",
        "*Generated by `analyze.py` on 2026-05-05. Uses experiments/lib/protease_stability.py. "
        "Re-run after any AlphaFold model update or MEROPS specificity revision. "
        "See inputs/provenance.md for data sources and the relationship to comp-006.*",
    ]

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
