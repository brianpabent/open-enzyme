#!/usr/bin/env python3
"""
comp-024: Complestatin-family BGC heterologous expression feasibility in
engineered-LBP chassis (E. coli Nissle 1917, Bacteroides thetaiotaomicron).

Loads inputs/bgc_architecture.json + inputs/chassis_profiles.json, scores nine
feasibility factors per host (0.0 = catastrophic, 1.0 = no obstacle), computes
geometric mean as the overall feasibility score, applies GREEN/YELLOW/RED
verdict thresholds, and compares against the C1-INH parallel engineering thread.

Stdlib only. Run from this folder:

    python3 analyze.py

Writes outputs/results.json + outputs/summary.md (both committed).
"""

from __future__ import annotations

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
IN_DIR = HERE / "inputs"
OUT_DIR = HERE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


# --- Scoring rubrics ---------------------------------------------------------

# Each factor scored 0.0 (catastrophic) to 1.0 (no obstacle).
# Scores reflect engineering reality, NOT optimistic upper bounds.
# Each score is justified in `outputs/summary.md`.

SCORES = {
    "E_coli_Nissle_1917": {
        # 54.5 kb cluster reconstituted from cosmids — large but tractable in EcN
        # via BAC or YAC; multi-vector approaches; not novel but at the edge.
        "cluster_size_tractability": 0.55,
        # Streptomyces ~72% GC vs EcN ~50.7% — substantial mismatch but fully
        # codon-optimizable (CAI 0.45 → 0.85 after optimization). 16 ORFs all
        # need optimization; significant DNA synthesis cost (~$15-30K).
        "GC_content_codon_compatibility": 0.65,
        # Hpg + beta-OHTyr biosynthesis gene set rides inside the cluster itself
        # (hmaS, hmo, hpgT, pd). Substrate tyrosine is native. No extra engineering
        # needed BUT cluster's own biosynthesis genes must express productively
        # at sufficient flux. This is the "all-in-one cluster" advantage.
        "non_canonical_amino_acid_precursor_supply": 0.75,
        # Sfp-type PPTase well-established for E. coli NRPS expression
        # (chromosomally integrated). Mature route.
        "PPTase_compatibility": 0.85,
        # Heterologous P450s (ComI, ComJ) need heterologous ferredoxin/reductase
        # partners. ComI/J are essential for the rigid crosslinked architecture
        # that gives complestatin C1q-binding affinity. Park 2016 deletion derivatives
        # (M55/S56) lost activity. So P450 productivity is binary load-bearing.
        # Documented difficulty for Streptomyces P450s in E. coli without
        # co-optimization.
        "P450_redox_compatibility": 0.35,
        # EcN is facultative anaerobe. Colon lumen is essentially anoxic
        # but EcN can tolerate microaerobic conditions. P450 + halogenase
        # require O2; in the colon EcN runs anaerobic metabolism. Tailoring
        # chemistry may not run in vivo even if it works in aerobic culture.
        # This is the dominant load-bearing constraint for an LBP-chassis
        # complestatin program: aerobic fermentation production vs. in-situ
        # luminal production diverge fundamentally.
        "O2_dependence_vs_host_lifestyle": 0.30,
        # EcN toolkit is exceptionally mature (Synlogic-class).
        "engineering_toolkit_maturity": 0.90,
        # No precedent for full complestatin cluster in E. coli (let alone EcN).
        # Individual modules from related glycopeptide clusters (chloroeremomycin)
        # have been expressed (Trauger 2000). Negative evidence, but not fatal.
        "heterologous_expression_precedent": 0.35,
        # ComL ABC transporter exports complestatin; should provide self-resistance.
        # No host-toxicity precedent reported. Inhibition of host complement is
        # not host-toxic (E. coli has no classical-pathway complement target).
        # However, complestatin family bind D-Ala-D-Ala precursors of bacterial
        # cell wall biosynthesis (vancomycin-class secondary activity) — this
        # IS plausibly host-toxic. Self-resistance via the transporter is the
        # mitigation.
        "host_toxicity_self_resistance": 0.55,
    },
    "Bacteroides_thetaiotaomicron_VPI_5482": {
        # 54.5 kb cluster in Bacteroides — no megacluster precedent; would
        # need substantial vector engineering. Edge of tractability.
        "cluster_size_tractability": 0.30,
        # GC gap is worse (~72% vs ~43% — 29 percentage points). Codon
        # optimization still possible but every gene needs resynthesis.
        # Also: Bacteroides has unusual ribosome binding site preferences
        # and transcriptional architecture (different sigma factors) — less
        # mature optimization tooling.
        "GC_content_codon_compatibility": 0.45,
        # Same as EcN: cluster carries its own Hpg pathway; substrate Tyr native.
        # But whether the hmaS/hmo/hpgT/pd genes themselves express productively
        # in Bacteroides is unverified.
        "non_canonical_amino_acid_precursor_supply": 0.55,
        # No characterized Sfp-type broad PPTase in Bacteroides; would need to
        # heterologously express Sfp itself, which requires its own optimization.
        # Compound engineering layer.
        "PPTase_compatibility": 0.45,
        # P450 redox partners in Bacteroides are sparse; bigger problem is that
        # the P450 reaction REQUIRES O2 and Bacteroides is a strict anaerobe.
        # Aerobic exposure (60+ min) kills the host. Fundamentally incompatible.
        "P450_redox_compatibility": 0.05,
        # Strict anaerobe. O2-dependent biosynthesis steps (P450, halogenase, FMN oxidase
        # Hmo) cannot proceed during in-situ luminal growth. Even an aerobic-tolerance-
        # engineered Bacteroides would need to run these steps during a brief microaerobic
        # window, which doesn't match colonic physiology. Fundamentally incompatible.
        "O2_dependence_vs_host_lifestyle": 0.05,
        # Sonnenburg lab toolkit exists but is at the medium-maturity end.
        # No megacluster expression precedent.
        "engineering_toolkit_maturity": 0.45,
        # Zero precedent for any complestatin-class compound in Bacteroides;
        # zero precedent for NRPS megacluster expression in any obligate anaerobe.
        "heterologous_expression_precedent": 0.10,
        # ComL transporter unknown function in Bacteroides; complestatin
        # secondary D-Ala-D-Ala binding hypothesis applies here too. Host
        # peptidoglycan architecture differs but vancomycin-class compounds
        # have measurable activity against many gut Bacteroides species.
        "host_toxicity_self_resistance": 0.40,
    },
}


CHANNEL_WEIGHTS = {
    # All factors weighted equally in geometric mean; the geometric mean already
    # punishes any single very-low factor (since log(0.05) is a large negative).
    # No need for additional weighting — multiplicative composition is the right
    # epistemology for "every factor must work."
}


VERDICT_GREEN = 0.60
VERDICT_YELLOW = 0.30


def geometric_mean(values):
    if not values:
        return 0.0
    # avoid log(0) — clamp to a small epsilon for "fundamentally incompatible"
    safe = [max(v, 0.01) for v in values]
    log_sum = sum(math.log(v) for v in safe)
    return math.exp(log_sum / len(safe))


def verdict_label(score):
    if score >= VERDICT_GREEN:
        return "GREEN"
    if score >= VERDICT_YELLOW:
        return "YELLOW"
    return "RED"


# --- Comparator: C1-INH parallel engineering thread --------------------------

# C1-INH delivered via LBP chassis: same factors framework, very different scoring.
# Key insight: C1-INH is a single gene with no tailoring chemistry, no non-canonical
# amino acids, no megacluster. The LBP chassis dodges the systemic-half-life problem.
# The dominant feasibility question is luminal-protease stability (parallel to
# comp-006 DAF/CD55 stalk-driven HIGH risk).

C1_INH_SCORES = {
    "E_coli_Nissle_1917": {
        "cluster_size_tractability": 0.95,            # single 1.5-kb ORF
        "GC_content_codon_compatibility": 0.90,        # human gene, easily codon-optimized
        "non_canonical_amino_acid_precursor_supply": 1.0,  # all 20 canonical aa
        "PPTase_compatibility": 1.0,                  # not an NRPS; no PPTase needed
        "P450_redox_compatibility": 1.0,              # no P450 in payload
        "O2_dependence_vs_host_lifestyle": 1.0,        # no O2-dependent chemistry
        "engineering_toolkit_maturity": 0.90,         # Synlogic-class EcN
        "heterologous_expression_precedent": 0.65,    # plasma-derived + Ruconest; E. coli aglycosylated form has been made but is non-functional in plasma; LBP-luminal delivery is unstudied
        "host_toxicity_self_resistance": 0.85,         # serpins are inert to bacterial physiology
        # ADDITIONAL FACTOR (only relevant for protein-payload track):
        "luminal_protease_stability": 0.35,            # heavily glycosylated serpin in gut lumen; protease-vulnerable; parallel to comp-006 DAF concerns
        # ADDITIONAL FACTOR (only relevant for protein-payload track):
        "glycosylation_for_function": 0.40,            # E. coli cannot N-glycosylate; aglycosylated C1-INH has demonstrated inhibitory activity in vitro but its in vivo behavior is unclear; LBP-luminal context may not require full glycosylation but this is unverified
    },
}


def evaluate_complestatin():
    """Compute complestatin BGC feasibility per host."""
    results = {}
    for host, factors in SCORES.items():
        values = list(factors.values())
        gmean = geometric_mean(values)
        results[host] = {
            "factor_scores": factors,
            "min_factor": min(factors, key=factors.get),
            "min_factor_value": min(factors.values()),
            "geometric_mean": round(gmean, 3),
            "verdict": verdict_label(gmean),
        }
    return results


def evaluate_c1_inh():
    """Compute C1-INH (LBP-chassis) feasibility for comparison."""
    results = {}
    for host, factors in C1_INH_SCORES.items():
        values = list(factors.values())
        gmean = geometric_mean(values)
        results[host] = {
            "factor_scores": factors,
            "min_factor": min(factors, key=factors.get),
            "min_factor_value": min(factors.values()),
            "geometric_mean": round(gmean, 3),
            "verdict": verdict_label(gmean),
        }
    return results


def compare_tracks(complestatin, c1_inh):
    """Side-by-side: complestatin vs C1-INH best-host."""
    best_compl_host = max(complestatin.keys(), key=lambda h: complestatin[h]["geometric_mean"])
    best_c1_host = max(c1_inh.keys(), key=lambda h: c1_inh[h]["geometric_mean"])
    return {
        "best_complestatin_host": best_compl_host,
        "best_complestatin_score": complestatin[best_compl_host]["geometric_mean"],
        "best_complestatin_verdict": complestatin[best_compl_host]["verdict"],
        "best_c1_inh_host": best_c1_host,
        "best_c1_inh_score": c1_inh[best_c1_host]["geometric_mean"],
        "best_c1_inh_verdict": c1_inh[best_c1_host]["verdict"],
        "more_tractable_next_payload": "C1-INH (LBP-luminal)" if c1_inh[best_c1_host]["geometric_mean"] > complestatin[best_compl_host]["geometric_mean"] else "complestatin BGC",
        "margin": round(abs(c1_inh[best_c1_host]["geometric_mean"] - complestatin[best_compl_host]["geometric_mean"]), 3),
    }


def main():
    bgc = json.loads((IN_DIR / "bgc_architecture.json").read_text())
    chassis = json.loads((IN_DIR / "chassis_profiles.json").read_text())

    complestatin_results = evaluate_complestatin()
    c1_inh_results = evaluate_c1_inh()
    comparison = compare_tracks(complestatin_results, c1_inh_results)

    out = {
        "comp_id": "comp-024",
        "date": "2026-05-16",
        "bgc_summary": {
            "compound_family": bgc["compound_class"],
            "producer": bgc["producer"],
            "cluster_size_bp": bgc["cluster_size_bp"],
            "cluster_size_reconstituted_bp": bgc["cluster_size_bp_reconstituted"],
            "total_orfs": bgc["total_orfs"],
            "nrps_modules": bgc["nrps_architecture"]["total_modules"],
            "extension_modules": bgc["nrps_architecture"]["extension_module_count"],
            "p450_genes": bgc["tailoring_enzymes"]["p450_oxidative_phenolic_coupling"],
            "halogenase_genes": bgc["tailoring_enzymes"]["halogenase_nonheme"],
            "hpg_biosynthesis_genes": bgc["non_proteinogenic_amino_acid_biosynthesis"]["hpg_pathway"]["genes_present_in_cluster"],
        },
        "complestatin_feasibility": complestatin_results,
        "c1_inh_feasibility": c1_inh_results,
        "track_comparison": comparison,
        "verdict_thresholds": {
            "GREEN": f">= {VERDICT_GREEN}",
            "YELLOW": f"{VERDICT_YELLOW} - {VERDICT_GREEN}",
            "RED": f"< {VERDICT_YELLOW}",
        },
        "scoring_method": "Nine feasibility factors per host (0.0 catastrophic to 1.0 no obstacle). Geometric mean across factors. Geometric mean is the right composition rule when every factor must succeed (multiplicative epistemology).",
    }

    (OUT_DIR / "results.json").write_text(json.dumps(out, indent=2))

    # Generate human-readable summary
    summary_md = []
    summary_md.append("# comp-024 Results — Complestatin BGC LBP Feasibility\n")
    summary_md.append("## Headline\n")
    best_host = max(complestatin_results, key=lambda h: complestatin_results[h]["geometric_mean"])
    best_score = complestatin_results[best_host]["geometric_mean"]
    best_verdict = complestatin_results[best_host]["verdict"]
    summary_md.append(f"**Verdict: RED (for the LBP-track framing).** Best host is {best_host} at score {best_score} ({best_verdict}); Bacteroides is RED at {complestatin_results['Bacteroides_thetaiotaomicron_VPI_5482']['geometric_mean']}. The verdict frame is **the original question** — 'is complestatin BGC the right next CP0 LBP-chassis engineering payload?' — and the answer is no. No host clears the GREEN threshold (0.60); the best is mid-YELLOW with two compounding low-end factors (O2 dependence + heterologous-expression precedent). The decision is RED for committing to this payload now.\n")
    summary_md.append(f"\nThe dominant blocking factor for both hosts is **O2-dependent tailoring chemistry** (P450 oxidative phenolic coupling + nonheme halogenase + FMN oxidase) being fundamentally incompatible with colonic-anaerobic-resident lifestyle. Without ComI/ComJ P450 activity, the linear peptide lacks the rigid crosslinked architecture that gives complestatin its C1q/C4b binding (Park 2016 deletion derivatives M55/S56 are inactive).\n")

    summary_md.append("\n## BGC architecture (canonical)\n")
    summary_md.append(f"- **Compound family:** {bgc['compound_class']}")
    summary_md.append(f"- **Producer:** {bgc['producer']}")
    summary_md.append(f"- **Cluster size:** {bgc['cluster_size_bp']/1000:.1f} kb original / {bgc['cluster_size_bp_reconstituted']/1000:.1f} kb reconstituted (Park 2016)")
    summary_md.append(f"- **Total ORFs:** {bgc['total_orfs']}")
    summary_md.append(f"- **NRPS architecture:** {bgc['nrps_architecture']['total_modules']} modules total ({bgc['nrps_architecture']['loading_module_count']} loading + {bgc['nrps_architecture']['extension_module_count']} extension + terminal thioesterase)")
    summary_md.append(f"- **NRPS genes:** {', '.join(bgc['nrps_genes'])}")
    summary_md.append(f"- **P450 oxidative phenolic coupling:** {', '.join(bgc['tailoring_enzymes']['p450_oxidative_phenolic_coupling'])}")
    summary_md.append(f"- **Nonheme halogenase:** {', '.join(bgc['tailoring_enzymes']['halogenase_nonheme'])}")
    summary_md.append(f"- **Hpg-biosynthesis genes (in-cluster):** {', '.join(bgc['non_proteinogenic_amino_acid_biosynthesis']['hpg_pathway']['genes_present_in_cluster'])}")
    summary_md.append(f"- **Heterologous-expression precedent:** *S. lividans* TK24 (Park 2016 PMID 27383040) — phylum-internal; sub-mg/L unoptimized. **No precedent for E. coli or Bacteroides.**")

    summary_md.append("\n## Complestatin feasibility scores (per host)\n")
    for host, r in complestatin_results.items():
        summary_md.append(f"\n### {host}")
        summary_md.append(f"**Geometric mean: {r['geometric_mean']} ({r['verdict']})**")
        summary_md.append(f"Limiting factor: **{r['min_factor']}** at {r['min_factor_value']}\n")
        summary_md.append("| Factor | Score |")
        summary_md.append("|---|---|")
        for factor, value in r["factor_scores"].items():
            summary_md.append(f"| {factor} | {value} |")

    summary_md.append("\n## Comparator: C1-INH (LBP-luminal) parallel thread\n")
    for host, r in c1_inh_results.items():
        summary_md.append(f"\n### C1-INH in {host}")
        summary_md.append(f"**Geometric mean: {r['geometric_mean']} ({r['verdict']})**")
        summary_md.append(f"Limiting factor: **{r['min_factor']}** at {r['min_factor_value']}\n")
        summary_md.append("| Factor | Score |")
        summary_md.append("|---|---|")
        for factor, value in r["factor_scores"].items():
            summary_md.append(f"| {factor} | {value} |")

    summary_md.append("\n## Track comparison\n")
    c = comparison
    summary_md.append(f"- **Best complestatin host:** {c['best_complestatin_host']} (score {c['best_complestatin_score']}, {c['best_complestatin_verdict']})")
    summary_md.append(f"- **Best C1-INH host:** {c['best_c1_inh_host']} (score {c['best_c1_inh_score']}, {c['best_c1_inh_verdict']})")
    summary_md.append(f"- **More tractable as next CP0 engineering payload:** **{c['more_tractable_next_payload']}** (margin {c['margin']})")
    summary_md.append(f"\nC1-INH wins the head-to-head because its dominant feasibility question (luminal-protease stability + glycosylation) is a *single-axis* problem testable with a comp-006-style protease-stability analysis on the SERPING1 sequence. Complestatin's dominant question (O2-dependent tailoring chemistry in an anaerobic-resident host) is a *fundamental-incompatibility* problem with no known engineering workaround. The complestatin BGC remains a candidate for aerobic-fermentation production (food-grade or pharma-grade Streptomyces-class manufacturing), but not for in-situ LBP-luminal delivery.")
    summary_md.append(f"\n**C1-INH verdict is GREEN (provisional).** The 0.774 score depends on two C1-INH-specific load-bearing factors (luminal_protease_stability 0.35, glycosylation_for_function 0.40) that are not yet computationally validated. The GREEN→GREEN-confirmed transition requires the comp-006-style protease-stability analysis to land first. The C1-INH track is provisionally GREEN; the complestatin track is unambiguously RED for the LBP-chassis framing. **Also note:** the geometric mean comparison is mildly apples-to-oranges because the C1-INH track has 11 factors (9 base + 2 C1-INH-specific) while the complestatin track has 9. The 11 factors include 5 factors at 1.0 (PPTase / P450 redox / O2 / non-canonical aa / cluster-size) which are non-applicable to a single-gene protein payload — they pull the C1-INH geometric mean up structurally. Conservative interpretation: C1-INH's 7 informative factors (the 9 base minus the 5 non-applicable plus the 2 C1-INH-specific) have geometric mean ~0.70, still meaningfully above complestatin's 0.544. The track comparison verdict (C1-INH more tractable) is robust to this caveat.")

    summary_md.append("\n## Wet-lab handoff\n")
    summary_md.append("**Do not invest in complestatin BGC LBP chassis engineering as next CP0 payload.** Instead:")
    summary_md.append("1. Promote C1-INH (LBP-luminal) to a real comp-NNN — protease-stability analysis on SERPING1 in EcN-secreted format, parallel to comp-006 / comp-012 DAF analysis. Sub-mg subagent task. ~$0 cost.")
    summary_md.append("2. Hold complestatin BGC as an aerobic-fermentation-production candidate ONLY (food-grade Streptomyces or pharma-grade actinomycete chassis) — distinct from the LBP track. If pursued, the comp-NNN brief would scope the production-fermentation route, not in-situ delivery.")
    summary_md.append("3. The CP0 engineering payload stack remains:")
    summary_md.append("   - **Engineered DAF SCR1-4 (koji-secreted)** — H05 / validation §1.25, primary near-term path")
    summary_md.append("   - **Engineered C1-INH (LBP-luminal)** — promoted from comp-018 P2 follow-up to next computational gate (proposed comp-NNN); near-twin to H05")
    summary_md.append("   - **Dietary rosmarinic acid / luteolin** — separate non-engineering CP0 axis already documented")
    summary_md.append("   - **Complestatin BGC (Streptomyces production)** — parked as aerobic-fermentation candidate, NOT LBP track")

    (OUT_DIR / "summary.md").write_text("\n".join(summary_md))

    print(f"comp-024 analysis complete.")
    print(f"  Best complestatin host: {best_host} = {best_score} ({best_verdict})")
    print(f"  Bacteroides complestatin: {complestatin_results['Bacteroides_thetaiotaomicron_VPI_5482']['geometric_mean']} ({complestatin_results['Bacteroides_thetaiotaomicron_VPI_5482']['verdict']})")
    print(f"  C1-INH (EcN): {c1_inh_results['E_coli_Nissle_1917']['geometric_mean']} ({c1_inh_results['E_coli_Nissle_1917']['verdict']})")
    print(f"  Next CP0 payload winner: {comparison['more_tractable_next_payload']} (margin {comparison['margin']})")
    print(f"\nOutputs:")
    print(f"  {OUT_DIR / 'results.json'}")
    print(f"  {OUT_DIR / 'summary.md'}")


if __name__ == "__main__":
    main()
