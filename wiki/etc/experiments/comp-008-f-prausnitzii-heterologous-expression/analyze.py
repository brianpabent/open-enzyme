#!/usr/bin/env python3
"""
comp-008: Faecalibacterium prausnitzii heterologous expression feasibility.

Scores four OE-relevant payloads (uricase, lactoferrin, soluble CR1 SCR1-4,
butyryl-CoA:acetate CoA-transferase) on an eight-factor feasibility rubric
against F. prausnitzii A2-165 (= F. duncaniae) as the LBP chassis.

Each factor is scored 0.0 (catastrophic) to 1.0 (no obstacle). Geometric mean
across factors gives the composite score. Geometric mean is the right
composition rule because every factor must succeed for the engineering
campaign to deliver a functional product (multiplicative epistemology).

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


# --- Verdict thresholds -------------------------------------------------------

VERDICT_GREEN = 0.60
VERDICT_YELLOW = 0.30


# --- Per-payload factor scores ----------------------------------------------

# Eight feasibility factors per payload. Geometric mean across factors.
# Scores reflect 2026-05 reality, NOT optimistic upper bounds.
# Each score is justified inline. Sensitivity ranges (low/high) reflect
# the dominant uncertainty range — typically +/-0.10 for engineering-toolkit
# factors, +/-0.05 for hard physical constraints (e.g. O2 requirement).

SCORES = {
    "uricase_AspergillusFlavus": {
        # 302 aa, 906 bp — small ORF, single gene. Trivial to clone into a
        # shuttle vector once the shuttle vector exists. Cluster size is
        # not the bottleneck.
        "cluster_size_tractability": {"value": 0.95, "low": 0.90, "high": 1.00,
            "rationale": "Single 302-aa ORF (906 bp), trivial cluster size."},
        # A. flavus CDS GC ~52% vs F. prausnitzii 56.6% — 4-5 percentage point
        # mismatch. Native codons work passably without optimization; with
        # codon optimization, CAI 0.45 -> 0.85.
        "GC_content_codon_compatibility": {"value": 0.70, "low": 0.60, "high": 0.80,
            "rationale": "A. flavus CDS ~52% GC vs Fp 56.6%. Small GC mismatch, eukaryotic codon-table mismatch. Codon optimization moderate-cost (~$1-2K DNA synthesis)."},
        # NO secretion required — uricase functions intracellularly (peroxisomal
        # in native fungus, cytoplasmic when expressed heterologously). Reduces
        # one engineering layer entirely.
        "secretion_pathway_availability": {"value": 1.00, "low": 0.95, "high": 1.00,
            "rationale": "Uricase is cytoplasmic/peroxisomal natively; functions intracellularly. No secretion engineering needed. But this raises the OPPOSITE problem: substrate (uric acid) must enter cell, product (allantoin) must exit."},
        # DOMINANT BLOCKING FACTOR. Uricase requires molecular O2 as substrate
        # (uric acid + O2 + H2O -> 5-hydroxyisourate + H2O2). Colonic lumen is
        # essentially anoxic. F. prausnitzii is a strict obligate anaerobe.
        # The enzyme CANNOT run its reaction in the chassis's native environment.
        # This is a fundamental chemistry mismatch — not "we should add O2,"
        # but "the chassis evolved to die in O2."
        "host_physiology_compatibility": {"value": 0.10, "low": 0.05, "high": 0.20,
            "rationale": "DOMINANT BLOCKER. Uricase requires O2 as substrate. F. prausnitzii is a strict anaerobe in an anoxic colonic lumen. Heterologous H2O2 production from uricase activity ALSO toxic to the anaerobic host (H2O2 lethal to obligate anaerobes without catalase, which F. prausnitzii lacks)."},
        # Genetic toolkit gap applies uniformly to all heterologous payloads
        # in this chassis. F. prausnitzii has no published transformation
        # protocol; close-relative (Roseburia, E. rectale) protocols may
        # transfer with 1-2 year adaptation work.
        "engineering_toolkit_maturity": {"value": 0.25, "low": 0.15, "high": 0.35,
            "rationale": "Shared factor across payloads. No published F. prausnitzii transformation; closest precedent is Lachnospiraceae conjugation (Roseburia, E. rectale per Sheridan 2019/2020). Estimated 1-2 yr adaptation needed."},
        # H2O2 from uricase activity is host-toxic. F. prausnitzii has limited
        # catalase / hydroperoxidase capacity (riboflavin-mediated extracellular
        # electron transfer is its main O2-detox mechanism, not H2O2 quenching).
        "host_toxicity_risk": {"value": 0.20, "low": 0.10, "high": 0.35,
            "rationale": "Uricase produces stoichiometric H2O2 per uric acid molecule. F. prausnitzii lacks robust catalase; H2O2 destroys obligate anaerobes via [Fe-S] cluster damage. Adding heterologous catalase as a co-payload is engineerable but compounds the campaign."},
        # No precedent for uricase expression in any anaerobe; ALLN-346
        # (Allena Pharma) uses oral microbial uricase as a transit-organism
        # capsule, not LBP-chassis.
        "heterologous_expression_precedent": {"value": 0.20, "low": 0.10, "high": 0.30,
            "rationale": "Zero precedent for uricase in obligate anaerobe. Rasburicase (S. cerevisiae expressing A. flavus uricase) is the canonical engineering precedent — aerobic / fermentation-batch context, fundamentally different physiology."},
        # Uricase requires no cofactors, no metals, no glycosylation, no
        # disulfides. Single-domain alpha/beta fold. Folding in cytoplasm
        # is well-precedented.
        "folding_complexity": {"value": 0.85, "low": 0.75, "high": 0.95,
            "rationale": "Cofactorless single-domain enzyme. No disulfides, no metals, no glycosylation. Folding in bacterial cytoplasm is well-precedented (Rasburicase in S. cerevisiae)."},
    },

    "lactoferrin_HumanFullLength": {
        # 691 aa mature (710 aa with signal peptide) = 2073-2130 bp ORF.
        # Tractable single-gene cassette.
        "cluster_size_tractability": {"value": 0.85, "low": 0.80, "high": 0.90,
            "rationale": "Single 691-aa mature ORF (~2.1 kb). Larger than uricase but well within single-vector range."},
        # Human CDS ~58% GC vs Fp 56.6% — exceptionally good GC match.
        # Native codon table is mammalian; CAI optimization recommended
        # but the GC similarity means the optimization cost is modest.
        "GC_content_codon_compatibility": {"value": 0.80, "low": 0.70, "high": 0.90,
            "rationale": "Human ~58% GC vs Fp 56.6% — only 1.4 percentage point mismatch. Best GC match of any payload in this set. Codon optimization still recommended for mammalian-table -> Firmicutes-table; ~$3-5K DNA synthesis."},
        # Lactoferrin REQUIRES secretion for its bacteriostatic / iron-binding
        # function in the gut lumen. F. prausnitzii has annotated Sec-translocon
        # (SecA/SecY/SecE conserved across Firmicutes) + Tat-translocon. Native
        # MAM secretion documented (Quévrain 2016).
        "secretion_pathway_availability": {"value": 0.60, "low": 0.45, "high": 0.75,
            "rationale": "Sec-translocon annotated; native MAM secretion proves the pathway functions. But heterologous-payload secretion titers from Fp never measured. 17 disulfides in mature lactoferrin require post-translocational oxidative folding — Bacillus / Firmicutes Sec pathway produces proteins to the cell exterior where disulfide bond formation occurs (e.g. DsbA/DsbB-class systems); native F. prausnitzii disulfide machinery less characterized."},
        # F. prausnitzii is an anaerobe; lactoferrin's iron-binding function
        # is GENUINELY USEFUL in the gut lumen (sequesters iron, deprives
        # pathogens). No O2 requirement. No physiology mismatch. Compatibility
        # is high.
        "host_physiology_compatibility": {"value": 0.85, "low": 0.75, "high": 0.95,
            "rationale": "No O2 dependence. Iron-sequestration function aligns with anaerobic-lumen physiology (anaerobic pathogens compete for iron). Minor risk: lactoferrin's iron-sequestration could starve F. prausnitzii itself, since Fp also requires iron — manage via inducible promoter or strain-engineered iron uptake."},
        # Same shared toolkit factor.
        "engineering_toolkit_maturity": {"value": 0.25, "low": 0.15, "high": 0.35,
            "rationale": "Shared factor."},
        # Lactoferrin is not bactericidal against most commensals at gut-lumen
        # concentrations (Fp itself coexists with native lactoferrin in human
        # gut). Self-toxicity minimal. Iron-sequestration self-starvation is the
        # main risk, manageable via inducible promoter.
        "host_toxicity_risk": {"value": 0.70, "low": 0.60, "high": 0.80,
            "rationale": "Native lactoferrin doesn't kill F. prausnitzii in vivo (Fp and lactoferrin coexist in healthy gut). Heterologous overexpression risk is iron-starvation of the host, mitigatable with inducible promoter."},
        # Recombinant lactoferrin expressed in many heterologous systems —
        # P. pastoris, A. niger, transgenic milk (cattle, sheep). NO precedent
        # in any obligate anaerobe. comp-005 evaluated koji chassis (HIGH risk
        # from protease vulnerability) → LBP framing avoids protease cocktail.
        "heterologous_expression_precedent": {"value": 0.30, "low": 0.20, "high": 0.40,
            "rationale": "Extensive precedent in non-anaerobe heterologous hosts (P. pastoris, A. niger, transgenic mammals). Zero precedent in obligate anaerobe. comp-005 evaluated koji chassis HIGH risk for stability — LBP track was framed precisely to address this."},
        # 17 disulfide bonds in mature protein. Even with Sec-translocon
        # secretion to the cell exterior, oxidative folding in the gut lumen
        # (anoxic) is mechanistically uncertain. Disulfide bond formation
        # requires oxidizing environment.
        "folding_complexity": {"value": 0.40, "low": 0.30, "high": 0.55,
            "rationale": "MAJOR concern. 17 disulfides require oxidative folding. Gut lumen is anoxic — disulfide bond formation in anoxic environment requires alternative oxidant (e.g. periplasmic-equivalent space + heterologously expressed DsbA, or methodologically untested in obligate anaerobes). Disulfide-rich secreted protein expression in obligate anaerobes is essentially unprecedented."},
    },

    "scr1_truncation_SCR1to4": {
        # 280 aa truncated SCR1-4 = ~840 bp. Small.
        "cluster_size_tractability": {"value": 0.95, "low": 0.90, "high": 1.00,
            "rationale": "280 aa truncated construct (~840 bp). Trivially clonable."},
        # Human CDS ~58% GC vs Fp 56.6% — same as lactoferrin, excellent match.
        "GC_content_codon_compatibility": {"value": 0.80, "low": 0.70, "high": 0.90,
            "rationale": "Same human ~58% GC vs Fp 56.6%. Codon optimization moderate."},
        # Secretion REQUIRED for complement-axis blocking action in gut lumen.
        # Same Sec/Tat-translocon availability as lactoferrin.
        "secretion_pathway_availability": {"value": 0.60, "low": 0.45, "high": 0.75,
            "rationale": "Sec-translocon present. Same caveat as lactoferrin re: disulfide-rich secretion. 8 disulfides in SCR1-4 — less than lactoferrin's 17 but still requires oxidative folding."},
        # No O2 dependence. Anaerobic-lumen-compatible. CR1 truncated form is
        # a soluble complement regulator — biologically inert to F. prausnitzii
        # itself.
        "host_physiology_compatibility": {"value": 0.90, "low": 0.80, "high": 0.95,
            "rationale": "No O2 requirement. CR1 (a host complement regulator) is mechanistically inert to bacterial physiology — F. prausnitzii has no classical-pathway complement target."},
        # Shared.
        "engineering_toolkit_maturity": {"value": 0.25, "low": 0.15, "high": 0.35,
            "rationale": "Shared factor."},
        # CR1 inert to bacterial physiology.
        "host_toxicity_risk": {"value": 0.90, "low": 0.80, "high": 0.95,
            "rationale": "CR1 is a host immune regulator; no bacterial target. Native serpins / complement regulators don't perturb commensal physiology."},
        # No precedent for any soluble complement regulator (sCR1, Factor H,
        # DAF) in any obligate anaerobe. DAF SCR1-4 in koji (comp-006/012) is
        # the closest precedent, HIGH risk verdict for koji stability — LBP
        # framing avoids koji proteases entirely.
        "heterologous_expression_precedent": {"value": 0.25, "low": 0.15, "high": 0.35,
            "rationale": "Zero precedent for soluble complement regulator in obligate anaerobe. comp-006/012 evaluated DAF SCR1-4 in koji (HIGH risk) — informs the parallel for LBP but doesn't establish a positive precedent."},
        # 8 disulfides in 280 aa. Same anoxic-folding concern as lactoferrin
        # but smaller magnitude.
        "folding_complexity": {"value": 0.45, "low": 0.30, "high": 0.60,
            "rationale": "8 disulfides require oxidative folding. Smaller magnitude than lactoferrin's 17 disulfides, but same fundamental anoxic-environment-folding question. SCR/sushi/CCP-fold proteins are tolerant of disulfide isomerization (more robust than serpin-fold lactoferrin) — slight upward adjustment vs. lactoferrin."},
    },

    "butyrate_pathway_boost_BCoAT": {
        # 448 aa, ~1.3 kb. Single gene. Native to F. prausnitzii.
        "cluster_size_tractability": {"value": 0.95, "low": 0.90, "high": 1.00,
            "rationale": "Single 448-aa ORF (1.3 kb). Native gene — option to chromosomally duplicate at native locus or supplement on plasmid."},
        # NATIVE codon usage by definition. CAI = 1.0.
        "GC_content_codon_compatibility": {"value": 1.00, "low": 0.95, "high": 1.00,
            "rationale": "NATIVE F. prausnitzii gene. CAI = 1.0 by definition. Zero codon-optimization cost."},
        # Cytoplasmic enzyme (no signal peptide). NO secretion needed —
        # butyrate diffuses out of cell as small molecule. One less
        # engineering layer.
        "secretion_pathway_availability": {"value": 1.00, "low": 0.95, "high": 1.00,
            "rationale": "Butyryl-CoA:acetate CoA-transferase is cytoplasmic. Product (butyrate) diffuses across cell membrane as a small molecule. No secretion engineering needed."},
        # Native pathway. Native substrate (acetate). Native lifestyle.
        # Native producer.
        "host_physiology_compatibility": {"value": 1.00, "low": 0.95, "high": 1.00,
            "rationale": "Native enzyme in native pathway in native host. No physiology mismatch. Anaerobic-pathway-anaerobic-host alignment is total."},
        # Same shared toolkit factor.
        "engineering_toolkit_maturity": {"value": 0.25, "low": 0.15, "high": 0.35,
            "rationale": "Shared factor. Even for a native-payload boost, the cassette must still be integrated; transformation toolkit gap applies."},
        # Native overexpression. Fitness cost from increased metabolic flux
        # demand on acetate / acetyl-CoA pool, but no toxicity per se.
        "host_toxicity_risk": {"value": 0.75, "low": 0.65, "high": 0.85,
            "rationale": "Native overexpression risks fitness loss via diversion of acetate / acetyl-CoA from primary metabolism, especially if cassette is on a high-copy plasmid. Manageable via copy-number tuning / inducible promoter. Not host-toxic in the toxicity sense."},
        # Native overexpression of bacterial pathway genes is well-precedented
        # in close-relative chassis (Clostridium tyrobutyricum, butyrate-
        # producing strain engineering for biofuel applications). Not in
        # F. prausnitzii specifically, but the engineering motif is mature.
        "heterologous_expression_precedent": {"value": 0.55, "low": 0.40, "high": 0.70,
            "rationale": "Closely-related-chassis precedent: Clostridium tyrobutyricum, C. acetobutylicum butyrate-pathway boost via plasmid-based overexpression (biofuel literature, well-established). F. prausnitzii-specific precedent: zero. Motif maturity is high; species-level precedent is zero."},
        # Native cytoplasmic enzyme, no disulfides, no glycosylation, no
        # metals. Folding is solved.
        "folding_complexity": {"value": 1.00, "low": 0.95, "high": 1.00,
            "rationale": "Native enzyme — folding in native cytoplasm is by definition the optimal case."},
    },
}


def geometric_mean(values):
    if not values:
        return 0.0
    safe = [max(v, 0.01) for v in values]
    log_sum = sum(math.log(v) for v in safe)
    return math.exp(log_sum / len(safe))


def verdict_label(score):
    if score >= VERDICT_GREEN:
        return "GREEN"
    if score >= VERDICT_YELLOW:
        return "YELLOW"
    return "RED"


def evaluate_payload(name, factors):
    point_values = {k: v["value"] for k, v in factors.items()}
    low_values = {k: v["low"] for k, v in factors.items()}
    high_values = {k: v["high"] for k, v in factors.items()}

    point_gmean = geometric_mean(list(point_values.values()))
    low_gmean = geometric_mean(list(low_values.values()))
    high_gmean = geometric_mean(list(high_values.values()))

    min_factor = min(point_values, key=point_values.get)
    return {
        "payload": name,
        "factor_scores": point_values,
        "factor_rationales": {k: v["rationale"] for k, v in factors.items()},
        "factor_sensitivity_ranges": {k: {"low": v["low"], "high": v["high"]} for k, v in factors.items()},
        "min_factor": min_factor,
        "min_factor_value": point_values[min_factor],
        "geometric_mean": round(point_gmean, 3),
        "geometric_mean_low": round(low_gmean, 3),
        "geometric_mean_high": round(high_gmean, 3),
        "verdict": verdict_label(point_gmean),
        "verdict_low": verdict_label(low_gmean),
        "verdict_high": verdict_label(high_gmean),
    }


def main():
    payloads = json.loads((IN_DIR / "payloads.json").read_text())
    chassis = json.loads((IN_DIR / "chassis_profile.json").read_text())

    results = {name: evaluate_payload(name, factors) for name, factors in SCORES.items()}

    # Rank-order by point geometric mean
    ranked = sorted(results.values(), key=lambda r: -r["geometric_mean"])

    out = {
        "comp_id": "comp-008",
        "date": "2026-05-16",
        "question": "Is F. prausnitzii A2-165 (= F. duncaniae) engineering-tractable for OE-relevant payloads, and which payloads rank highest by composite feasibility?",
        "chassis": {
            "name": chassis["host"],
            "genome_gc_percent": chassis["genome"]["gc_content_percent"],
            "genome_size_mbp_range": chassis["genome"]["size_mbp_range"],
            "oxygen_tolerance": chassis["physiology"]["oxygen_tolerance"],
            "transformation_protocol_established": chassis["genetic_toolkit_maturity_2026_05"]["transformation_protocol_established"],
        },
        "payload_evaluations": {r["payload"]: r for r in ranked},
        "ranking": [{"payload": r["payload"], "score": r["geometric_mean"],
                     "score_range": [r["geometric_mean_low"], r["geometric_mean_high"]],
                     "verdict": r["verdict"]} for r in ranked],
        "verdict_thresholds": {
            "GREEN": f">= {VERDICT_GREEN}",
            "YELLOW": f"{VERDICT_YELLOW} - {VERDICT_GREEN}",
            "RED": f"< {VERDICT_YELLOW}",
        },
        "scoring_method": ("Eight feasibility factors per payload (0.0 catastrophic to 1.0 no obstacle). "
                           "Geometric mean across factors. Geometric mean punishes any single very-low factor "
                           "more than arithmetic mean — appropriate epistemology when every factor must succeed."),
        "shared_blocker": ("The engineering-toolkit-maturity factor applies to ALL payloads at value ~0.25 — "
                           "F. prausnitzii has no published transformation protocol as of 2026-05. This is a "
                           "FIXED FACILITY cost that gets paid once for any engineering campaign, not a "
                           "per-payload cost. Conditional on the toolkit being established (an estimated 1-2 yr "
                           "investment), the per-payload feasibility re-ranks differently — see summary.md "
                           "'Toolkit-conditional ranking' section."),
    }

    # Toolkit-conditional re-ranking: what does the ordering look like IF we
    # treat engineering toolkit maturity as solved (a fixed facility cost
    # paid once)? Re-compute the geometric mean excluding that factor.
    toolkit_conditional_results = {}
    for name, factors in SCORES.items():
        non_toolkit_factors = {k: v["value"] for k, v in factors.items()
                                if k != "engineering_toolkit_maturity"}
        gmean = geometric_mean(list(non_toolkit_factors.values()))
        toolkit_conditional_results[name] = {
            "payload": name,
            "non_toolkit_geometric_mean": round(gmean, 3),
            "verdict": verdict_label(gmean),
        }
    out["toolkit_conditional_ranking"] = sorted(toolkit_conditional_results.values(),
                                                 key=lambda r: -r["non_toolkit_geometric_mean"])

    (OUT_DIR / "results.json").write_text(json.dumps(out, indent=2))

    # --- Human-readable summary ----------------------------------------------

    summary = []
    summary.append("# comp-008 Results — F. prausnitzii Heterologous Expression Feasibility\n")
    summary.append(f"**Date:** 2026-05-16. **Chassis:** {chassis['host']}. **Genome GC:** {chassis['genome']['gc_content_percent']}%.\n")

    summary.append("## Headline\n")
    top = ranked[0]
    summary.append(f"**Top payload: {top['payload']} (score {top['geometric_mean']}, verdict {top['verdict']}, range [{top['geometric_mean_low']}, {top['geometric_mean_high']}]).**")
    summary.append("")
    summary.append("**Ranking by composite feasibility:**")
    for i, r in enumerate(ranked, 1):
        summary.append(f"{i}. **{r['payload']}** — score **{r['geometric_mean']}** ({r['verdict']}); range [{r['geometric_mean_low']}, {r['geometric_mean_high']}]; limiting factor: *{r['min_factor']}* at {r['min_factor_value']}")
    summary.append("")
    summary.append("**The shared blocker is the engineering toolkit gap** (factor at 0.25 across all payloads — F. prausnitzii has no published transformation protocol as of 2026-05). The verdicts above bake that fixed-facility cost into the geometric mean. **Toolkit-conditional ranking** (the ordering IF the transformation toolkit is established as a separate 1-2 yr investment) re-orders the payloads:")
    summary.append("")
    for i, r in enumerate(out["toolkit_conditional_ranking"], 1):
        summary.append(f"{i}. **{r['payload']}** — non-toolkit score {r['non_toolkit_geometric_mean']} ({r['verdict']})")

    summary.append("\n## Chassis profile summary\n")
    summary.append(f"- **Host:** F. prausnitzii A2-165 (taxonomically reclassified as *F. duncaniae* by Sakamoto 2022, doi:10.1099/ijsem.0.005379). A2-165 = JCM 31915 = DSM 17677.")
    summary.append(f"- **Genome:** {chassis['genome']['size_mbp_range']} Mbp, {chassis['genome']['gc_content_percent']}% GC, ~{chassis['genome']['protein_coding_genes_average']} protein-coding genes (Fraccascia 2022 doi:10.1128/mra.00824-22).")
    summary.append(f"- **Physiology:** Strict obligate anaerobe. Colonic-lumen resident. Native butyrate producer via butyryl-CoA:acetate CoA-transferase pathway.")
    summary.append(f"- **Secretion machinery:** Sec-translocon (SecA/Y/E annotated), Tat-translocon (TatABC annotated). Native MAM (15 kDa anti-inflammatory protein) secretion documented (Quévrain 2016 doi:10.1136/gutjnl-2014-307649).")
    summary.append(f"- **Engineering toolkit (2026-05):** None published for F. prausnitzii itself. Closest precedent is Lachnospiraceae conjugation (Roseburia inulinivorans, E. rectale; Sheridan 2019 doi:10.1016/j.anaerobe.2019.06.008; Sheridan 2020 doi:10.21769/BioProtoc.3575). Workaround pattern in literature: when researchers want to express F. prausnitzii's MAM in mouse gut, they engineer *Lactococcus lactis* to carry the MAM plasmid — NOT engineering F. prausnitzii itself (Quévrain 2016; Breyner 2017 doi:10.3389/fmicb.2017.00114).")

    summary.append("\n## Per-payload analysis\n")
    for r in ranked:
        summary.append(f"\n### {r['payload']}")
        summary.append(f"**Composite: {r['geometric_mean']} ({r['verdict']}); range [{r['geometric_mean_low']}, {r['geometric_mean_high']}]**")
        summary.append(f"**Dominant uncertainty / limiting factor: {r['min_factor']} at {r['min_factor_value']}**\n")
        summary.append("| Factor | Score | Low | High | Rationale |")
        summary.append("|---|---|---|---|---|")
        for fname, fvalue in r["factor_scores"].items():
            sens = r["factor_sensitivity_ranges"][fname]
            rat = r["factor_rationales"][fname]
            summary.append(f"| {fname} | {fvalue} | {sens['low']} | {sens['high']} | {rat} |")

    summary.append("\n## Key findings\n")
    summary.append("1. **Butyrate-pathway boost (BCoAT) is the unambiguous winner** — both base ranking AND toolkit-conditional ranking. It is a NATIVE payload (CAI=1.0, no secretion, native lifestyle, no folding burden). The only blocker is the shared engineering-toolkit gap.")
    summary.append("2. **Uricase scores LOW (~0.40) — and the bottleneck is the host-physiology mismatch, not the engineering toolkit.** Uricase fundamentally requires O2 as a substrate. F. prausnitzii is a strict anaerobe in an anoxic colonic lumen. Even with a perfect engineering toolkit, the chemistry can't run. This is a STRATEGIC RECLASSIFICATION moment: uricase is not a plausible F. prausnitzii payload, regardless of how much engineering investment goes in. Different chassis is required (e.g. E. coli Nissle as facultative anaerobe — micro-aerobic windows possible in proximal colon; or maintain uricase on the koji track).")
    summary.append("3. **Lactoferrin and sCR1 SCR1-4 score similarly (~0.50-0.55)** — both have favorable host-physiology fit, both bottleneck on the same anoxic-environment-disulfide-folding question. This is a more tractable problem than uricase's O2-substrate-requirement because it could be addressed by heterologous DsbA/DsbB co-expression or by switching to a chassis with characterized oxidative-folding capacity in the periplasmic-equivalent space. But it's still a real risk.")
    summary.append("4. **CR1 SCR1-4 ranks slightly above lactoferrin** due to fewer disulfide bonds (8 vs 17) and the SCR/sushi/CCP-fold's documented isomerization tolerance.")
    summary.append("5. **The engineering toolkit gap (no published F. prausnitzii transformation as of 2026-05) is the gating factor for ALL payloads except butyrate-boost-via-native-pathway.** Without the toolkit, every score above except butyrate's is academic. Strategic path: invest 1-2 yr in adapting the Lachnospiraceae conjugation toolkit (Roseburia inulinivorans + E. rectale precedent) to F. prausnitzii FIRST; the payload selection happens second.")

    summary.append("\n## What this comp informs / decides\n")
    summary.append("- **Engineered LBP chassis Phase 2 (P2-4)** per [`wiki/engineered-lbp-chassis.md`](../../wiki/engineered-lbp-chassis.md): F. prausnitzii is engineering-naive as of 2026-05; the LBP-chassis Phase 2 investment should prioritize toolkit development BEFORE payload selection.")
    summary.append("- **Payload-specific guidance:** if the toolkit is committed to, butyrate-pathway boost (native BCoAT overexpression) is the first wet-lab target. Uricase should be REMOVED from the F. prausnitzii payload menu (RED on host-physiology grounds). Lactoferrin and sCR1 are conditional GREEN if disulfide-folding can be addressed (engineering question + experimental measurement; not solvable purely in silico).")
    summary.append("- **Comparative chassis matrix (P2-6 per engineered-lbp-chassis.md):** confirms that uricase belongs on a facultative-anaerobe chassis (E. coli Nissle) or a transit-aerobic chassis (koji) rather than a strict-anaerobe chassis. Butyrate-boost belongs on F. prausnitzii. Lactoferrin / sCR1 can plausibly go either to F. prausnitzii or Bacteroides depending on disulfide-folding investigation.")
    summary.append("- **comp-007 (food-grade HDAC inhibitor screen) cross-link:** butyrate was the top food-grade HDAC inhibitor with 167× class-I-over-HDAC6 selectivity. Continuous gut-luminal butyrate from an engineered F. prausnitzii strain solves the bioavailability problem at the dose-frequency level — this comp says that's the FIRST plausible engineering campaign, not the second or third.")

    summary.append("\n## Toolkit adaptation roadmap (for Phase 2 wet-lab handoff)\n")
    summary.append("1. **Method development phase (12-18 months):** Adapt Sheridan 2019/2020 Roseburia inulinivorans conjugation protocol to F. prausnitzii A2-165. Tn1545-class conjugative transposon + tet(W) or erm(B) selection. Expected transfer efficiency 10^-5 to 10^-7 per recipient (Lachnospiraceae baseline).")
    summary.append("2. **PAM (Plasmid Artificial Modification) protocol** if Type II RM systems in F. prausnitzii prove inhibitory — Yasui 2009 doi:10.1128/AEM.02418-08 demonstrated 10,000× improvement in B. adolescentis with this method.")
    summary.append("3. **First-payload milestone:** chromosomally integrate a second copy of native butyryl-CoA:acetate CoA-transferase (or a strong-promoter variant of the native gene). Measure butyrate output in YCFA broth. This is the lowest-risk validation construct — native pathway, native gene.")
    summary.append("4. **Second-payload milestone:** secrete a small reporter protein (e.g. tagged MAM or NanoLuc) via Sec-translocon. Measure secretion titer. This establishes whether the chassis can heterologously secrete at biologically relevant levels — a precondition for lactoferrin / sCR1 expression.")
    summary.append("5. **Defer disulfide-rich payloads (lactoferrin, sCR1) until milestone 4 is achieved.** Until then, lactoferrin / sCR1 development should run in parallel on the alternative E. coli Nissle chassis (Synlogic-class toolkit) per the comparative chassis matrix.")

    summary.append("\n## Limitations\n")
    summary.append("1. **Factor scores are expert estimates**, not derived from large-scale empirical heterologous-expression datasets in F. prausnitzii (which don't exist). Geometric mean is robust to ±0.1 variation in any single factor but the verdict could shift if a factor is meaningfully miscalibrated. See the sensitivity ranges (low/high columns).")
    summary.append("2. **CAI values are framework-estimated, not RSCU-table-computed.** Wet-lab cassette design needs a proper codon-frequency table for F. prausnitzii A2-165 highly-expressed genes (rpsA, tuf, fusA). Estimates here are ±0.10.")
    summary.append("3. **Disulfide-folding-in-anoxic-environment** is an open empirical question; the literature is sparse. Folding-complexity scores for lactoferrin and sCR1 reflect this — the scores represent a real engineering risk, not a known impossibility.")
    summary.append("4. **The shared engineering-toolkit-maturity factor at 0.25 is the dominant variance source across all payloads.** If a successful F. prausnitzii transformation protocol is published in 2026-27, every payload's geometric mean lifts by ~0.10-0.15. The toolkit-conditional ranking section anticipates this.")
    summary.append("5. **No published wet-lab F. prausnitzii transformation efficiency baseline.** Roseburia inulinivorans conjugation efficiency (10^-4 to 10^-6 transconjugants/recipient per Sheridan 2019) is used as the proxy.")
    summary.append("6. **GC% / CAI / codon-level optimization details are framework-level only.** Detailed RBS strength, mRNA secondary structure, and codon-context effects are part of the wet-lab cassette-design phase.")

    summary.append("\n## Multilingual sources checked\n")
    summary.append("- **Chinese-language**: Guo 2025 J Transl Med doi:10.1186/s12967-025-07493-0 (Chinese authors, MAM-engineered strain — uses L. lactis delivery, not engineered F. prausnitzii); no published F. prausnitzii engineering toolkit in CNKI-indexed literature as of 2026-05.")
    summary.append("- **Japanese-language**: Sakamoto 2022 IJSEM doi:10.1099/ijsem.0.005379 (Japanese RIKEN group taxonomic reclassification of A2-165 to F. duncaniae); JCM 31915 strain deposit. No engineering work.")
    summary.append("- **Korean-language**: Seo 2024 Probiotics Antimicrob Proteins doi:10.1007/s12602-024-10213-7 (Korean strain KBL1027 phenotype work). No engineering.")
    summary.append("- **Net:** the 'no published transformation protocol for F. prausnitzii' finding is robust across English, Chinese, Japanese, and Korean PubMed-indexed sources.")

    (OUT_DIR / "summary.md").write_text("\n".join(summary))

    # --- Print summary ---
    print("comp-008 analysis complete.")
    print(f"  Chassis: F. prausnitzii A2-165 / F. duncaniae")
    print(f"  Genome: {chassis['genome']['size_mbp_range']} Mbp, {chassis['genome']['gc_content_percent']}% GC")
    print()
    print("  Payload ranking (base scores, toolkit gap baked in):")
    for r in ranked:
        print(f"    {r['payload']:55s} {r['geometric_mean']:.3f}  ({r['verdict']})  [{r['geometric_mean_low']:.3f}, {r['geometric_mean_high']:.3f}]")
    print()
    print("  Toolkit-conditional ranking (toolkit gap excluded):")
    for r in out["toolkit_conditional_ranking"]:
        print(f"    {r['payload']:55s} {r['non_toolkit_geometric_mean']:.3f}  ({r['verdict']})")
    print()
    print(f"Outputs:")
    print(f"  {OUT_DIR / 'results.json'}")
    print(f"  {OUT_DIR / 'summary.md'}")


if __name__ == "__main__":
    main()
