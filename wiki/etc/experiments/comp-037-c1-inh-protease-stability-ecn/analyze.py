#!/usr/bin/env python3
"""
comp-037: Human C1-INH (SERPING1, UniProt P05155) protease-stability + glycosylation feasibility
         in an engineered E. coli Nissle 1917 (EcN) luminal-secreted format.

Orchestrator — loads inputs, calls the shared protease-stability library, computes per-scope
risk + glycosylation-feasibility verdict, writes comp-037-specific outputs.

Same pipeline pattern as comp-006 (DAF/CD55 / koji) and comp-012 (DAF SCR1-4 truncated / koji).
Different chassis (EcN, not koji) → different protease panel (pancreatic + EcN-native) and
different environment (colonic lumen pH 6-7, ~0.15 M NaCl, 37 °C; bile-acid exposure
not modeled).

Usage: python3 analyze.py   (from this directory)
Outputs: outputs/cleavage_sites.json, outputs/summary.md

Three scopes computed (matches comp-006 framing):
  1. Full sequence (aa 1-500): includes signal peptide.
  2. Mature protein (aa 23-500): excludes signal peptide (replaced by EcN-native signal in engineered construct).
  3. Serpin-core construct (aa 123-500): excludes the heavily-O-glycosylated mucin-like
     domain (aa 23-119) — the candidate truncation analogous to CD55's stalk-truncation
     rescue in comp-006 → comp-012. The serpin core retains the reactive-center loop
     (aa ~452-467) and the inhibitor mechanism.

UniProt P05155 SV=2 annotation boundaries (grep-verified against the text-format flatfile,
fetch date 2026-05-17):
  SIGNAL peptide: aa 1-22
  CHAIN (mature): aa 23-500
  SITE reactive bond: 466..467 (R466-T467, cleavage by C1S — pseudo-substrate mechanism)
  DISULFID:   C123-C428, C130-C205  (2 bonds total — verified)
  CARBOHYD N-linked: 25, 69, 81, 238, 253, 272 (variant TA), 352
  CARBOHYD O-linked: 47, 48, 64, 71, 83, 88, 92, 96  (all in mucin-like tandem-repeat region)
  REGION 20-43: Disordered (MobiDB-lite)
  REGION 65-118: Disordered (MobiDB-lite)
  REPEAT 85-119: 7 × 4-aa tandem repeats of [QE]-P-T-[TQ]

Verdict vocabulary:
  LOW       max_risk_score < 0.15
  MODERATE  0.15 ≤ max_risk_score < 0.30
  HIGH      0.30 ≤ max_risk_score < 0.50
  RED       max_risk_score ≥ 0.50  OR  glycosylation-feasibility is hard-blocking

The glycosylation-feasibility verdict is computed independently from the protease
score because EcN cannot N-glycosylate by default — that is a categorical, not
quantitative, consideration.
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

# Deterministic seed — no stochastic components in this analysis (lib is fully deterministic
# given inputs), but we set seeds anyway as belt-and-braces for any future extension.
import random
random.seed(20260517)

# UniProt P05155 SV=2 annotation boundaries (grep-verified)
SIGNAL_PEPTIDE_END   = 22    # aa 1-22 cleaved during secretion in native context
MATURE_START         = 23    # first residue of mature chain
MATURE_END           = 500   # last residue (C-terminus of mature serpin)
MUCIN_DOMAIN_END     = 119   # end of mucin-like O-glycan tandem-repeat region
SERPIN_CORE_START    = 123   # start of the serpin-core construct (mucin domain truncated).
                              # Set at aa 123 = position of the first canonical disulfide Cys (C123-C428),
                              # which is the natural N-terminal anchor of the folded serpin body.
                              # AlphaFold pLDDT confirms the well-folded region starts at aa 122-123
                              # (pLDDT > 80 from aa 123 onward); aa 120-122 is a transition zone with
                              # pLDDT 43-78. Truncating at aa 123 eliminates two elastase-vulnerable
                              # boundary residues (G120-S121, S121-F122) without compromising the
                              # disulfide-anchored fold core.
RCL_START            = 452   # start of reactive-center loop (approximate)
RCL_END              = 467   # end of RCL through P1-P1' reactive bond R466-T467

# N-glycosylation sites (full-sequence numbering, UniProt CARBOHYD)
N_GLYC_SITES = [25, 69, 81, 238, 253, 272, 352]
# O-glycosylation sites (full-sequence numbering, UniProt CARBOHYD)
O_GLYC_SITES = [47, 48, 64, 71, 83, 88, 92, 96]

# Disulfide bonds (full-sequence numbering, UniProt DISULFID)
DISULFIDES = [(123, 428), (130, 205)]


def classify_c1inh_region(position):
    """Map a full-sequence position to a C1-INH structural region."""
    if position <= SIGNAL_PEPTIDE_END:
        return "signal_peptide"
    elif position <= MUCIN_DOMAIN_END:
        return "mucin_like_O_glycan_domain"
    elif RCL_START <= position <= RCL_END:
        return "RCL_reactive_loop"
    elif position <= MATURE_END:
        return "serpin_core"
    else:
        return "unknown"


def verdict_label(max_score):
    """Verdict thresholds — matches comp-006/12 with explicit RED tier added."""
    if max_score < 0.15:
        return "LOW"
    elif max_score < 0.30:
        return "MODERATE"
    elif max_score < 0.50:
        return "HIGH"
    else:
        return "RED"


def glycosylation_feasibility_verdict(seq, n_sites, o_sites,
                                      serpin_core_only=False):
    """
    Categorical verdict on whether C1-INH can functionally tolerate bacterial expression.

    Key facts (cited in inputs/provenance.md):
      - C1-INH carries ~26 kDa of glycan on a ~52 kDa polypeptide (Bos 1998, Stavenhagen 2018).
      - N-glycans are required for native plasma half-life (~30 h in circulation) and
        for protease-inhibitor activity stability (Bos 1998 PMID 9799502; Stavenhagen 2018).
      - O-glycans in the mucin-like domain (aa 47-96) shield that region from proteolysis
        in vivo; their absence in a bacterial host removes that shielding.
      - EcN does NOT have an endogenous N-glycosylation system. The C. jejuni pgl pathway
        can be transplanted but produces non-mammalian glycan structures (Wacker 2002).
      - For a LUMINAL-secreted format (this scope), plasma half-life is irrelevant —
        the inhibitor acts in the gut lumen on locally-generated C1r/C1s/MASP-2 at
        crystal-surface and mucin-interface sites. Functional activity (the serpin
        suicide mechanism) does not strictly require glycosylation.

    Verdict logic:
      GREEN  — glycosylation-independent activity is mechanistically supported AND
               the construct truncates the mucin-like O-glycan domain (serpin-core
               construct), avoiding the disordered unglycosylated region.
      YELLOW — glycosylation-independent activity is mechanistically supported but
               the construct retains the mucin-like domain (full mature) — the
               unglycosylated mucin region is a major protease liability.
      RED    — glycosylation is mechanistically required for inhibitor function.
               (Not the case for C1-INH luminal format — but reserved for the
               scope where this verdict could be defended on first principles.)
    """
    n_count = sum(1 for s in n_sites if MATURE_START <= s <= MATURE_END)
    o_count = sum(1 for s in o_sites if MATURE_START <= s <= MATURE_END)

    if serpin_core_only:
        n_count_in_construct = sum(1 for s in n_sites if SERPIN_CORE_START <= s <= MATURE_END)
        o_count_in_construct = sum(1 for s in o_sites if SERPIN_CORE_START <= s <= MATURE_END)
        verdict = "GREEN"
        rationale = (
            f"Serpin-core construct (aa {SERPIN_CORE_START}-{MATURE_END}) truncates the "
            f"mucin-like O-glycan domain entirely. {n_count_in_construct} N-glycan sites "
            f"remain in the construct (N238, N253, N272-variant, N352 — all in the serpin "
            f"core, none glycosylated by EcN). {o_count_in_construct} O-glycan sites remain "
            "(all 8 O-sites are in the truncated mucin domain). For luminal-secreted "
            "topology, plasma half-life is not a concern; serpin suicide-mechanism "
            "activity does not strictly require glycosylation. The major risk is "
            "loss of N-glycan-mediated folding-quality-control during EcN secretion "
            "— addressable with disulfide-bond-aware folding partners (DsbA/DsbC in "
            "the EcN periplasm) and signal-peptide / chassis tuning."
        )
    else:
        verdict = "YELLOW"
        rationale = (
            f"Full mature construct (aa {MATURE_START}-{MATURE_END}) retains the "
            f"mucin-like O-glycan domain (aa 47-96) with {o_count} O-glycan sites — "
            f"all unglycosylated in EcN expression. The disordered, unglycosylated "
            f"mucin region is a major protease liability (see protease-scoring "
            f"above). {n_count} N-glycan sites in mature chain, none glycosylated. "
            "Plasma half-life concern is moot for luminal topology, but the "
            "unshielded mucin domain is the dominant degradation risk."
        )
    return {
        "verdict": verdict,
        "rationale": rationale,
        "n_glyc_sites_in_mature": n_count,
        "o_glyc_sites_in_mature": o_count,
    }


def main():
    seq       = load_sequence(INPUTS / "P05155.fasta")
    plddt     = load_plddt(INPUTS / "alphafold_P05155_plddt.json")
    proteases, conditions = load_proteases(INPUTS / "protease_specificities.json")

    assert len(seq) == 500, f"Expected 500 aa for P05155, got {len(seq)}"

    # Verify load-bearing residues against UniProt features (sanity grep-gate)
    assert seq[465] == "R" and seq[466] == "T", (
        f"Reactive bond P1-P1' verification failed: expected R466-T467, "
        f"got {seq[465]}-{seq[466]}"
    )
    for (a, b) in DISULFIDES:
        assert seq[a - 1] == "C" and seq[b - 1] == "C", (
            f"Disulfide verification failed: expected C{a}-C{b}, "
            f"got {seq[a-1]}{a}-{seq[b-1]}{b}"
        )

    sequence_stats   = compute_sequence_stats(plddt)
    protease_results = run_all_proteases(seq, plddt, proteases, conditions)

    nacl_pct = conditions["NaCl_pct"]

    # Annotate top-5 sites and compute per-scope risk scores.
    for name, result in protease_results.items():
        for site in result["top_5_sites"]:
            site["region"] = classify_c1inh_region(site["position"])

        all_sites = find_cleavage_sites(seq, proteases[name], plddt, nacl_pct)

        # Mature protein scope: aa 23-500
        mature_sites = [s for s in all_sites if MATURE_START <= s["position"] <= MATURE_END]
        result["mature_max_risk_score"]   = round(mature_sites[0]["risk_score"], 3) if mature_sites else 0
        result["mature_exposed_sites"]    = sum(1 for s in mature_sites if s["accessibility"] == "exposed")

        # Serpin-core scope (mucin domain truncated): aa 123-500
        core_sites = [s for s in all_sites if SERPIN_CORE_START <= s["position"] <= MATURE_END]
        result["core_max_risk_score"]    = round(core_sites[0]["risk_score"], 3) if core_sites else 0
        result["core_exposed_sites"]     = sum(1 for s in core_sites if s["accessibility"] == "exposed")
        result["core_partially_exposed_sites"] = sum(1 for s in core_sites
                                                     if s["accessibility"] == "partially_exposed")

        # Serpin-core EXCLUDING the RCL (aa 452-467): the operationally relevant
        # protease-risk figure, because RCL exposure is REQUIRED for the inhibitor
        # mechanism (serpin presents RCL as pseudo-substrate to target proteases).
        # Cleavage by colonic / EcN proteases at the RCL is "mechanism-overlapping"
        # rather than purely degradative — the inhibitor's own design includes RCL
        # accessibility. The non-RCL serpin core captures the strictly-degradative
        # risk.
        core_non_rcl_sites = [s for s in core_sites
                              if not (RCL_START <= s["position"] <= RCL_END)]
        result["core_non_rcl_max_risk_score"]  = round(core_non_rcl_sites[0]["risk_score"], 3) if core_non_rcl_sites else 0
        result["core_non_rcl_exposed_sites"]   = sum(1 for s in core_non_rcl_sites if s["accessibility"] == "exposed")
        result["core_non_rcl_partially_exposed_sites"] = sum(1 for s in core_non_rcl_sites
                                                              if s["accessibility"] == "partially_exposed")

        # Mucin-domain scope: aa 23-119 (the truncated region — what's removed in core construct)
        mucin_sites = [s for s in all_sites
                       if MATURE_START <= s["position"] <= MUCIN_DOMAIN_END]
        result["mucin_max_risk_score"]  = round(mucin_sites[0]["risk_score"], 3) if mucin_sites else 0
        result["mucin_exposed_sites"]   = sum(1 for s in mucin_sites if s["accessibility"] == "exposed")

        # RCL scope (always at-risk by design; reported separately)
        rcl_sites = [s for s in all_sites if RCL_START <= s["position"] <= RCL_END]
        result["rcl_max_risk_score"]    = round(rcl_sites[0]["risk_score"], 3) if rcl_sites else 0
        result["rcl_exposed_sites"]     = sum(1 for s in rcl_sites if s["accessibility"] == "exposed")

    # Per-scope verdicts
    full_max_risks   = {n: r["max_risk_score"] for n, r in protease_results.items()}
    full_worst       = max(full_max_risks, key=full_max_risks.get)
    full_worst_score = full_max_risks[full_worst]
    full_verdict     = verdict_label(full_worst_score)

    mature_max_risks   = {n: r["mature_max_risk_score"] for n, r in protease_results.items()}
    mature_worst       = max(mature_max_risks, key=mature_max_risks.get)
    mature_worst_score = mature_max_risks[mature_worst]
    mature_verdict     = verdict_label(mature_worst_score)

    core_max_risks   = {n: r["core_max_risk_score"] for n, r in protease_results.items()}
    core_worst       = max(core_max_risks, key=core_max_risks.get)
    core_worst_score = core_max_risks[core_worst]
    core_verdict     = verdict_label(core_worst_score)

    # Non-RCL serpin core: the strictly-degradative risk figure
    core_non_rcl_max_risks   = {n: r["core_non_rcl_max_risk_score"] for n, r in protease_results.items()}
    core_non_rcl_worst       = max(core_non_rcl_max_risks, key=core_non_rcl_max_risks.get)
    core_non_rcl_worst_score = core_non_rcl_max_risks[core_non_rcl_worst]
    core_non_rcl_verdict     = verdict_label(core_non_rcl_worst_score)

    # Glycosylation feasibility verdicts (independent of protease score)
    glyco_mature = glycosylation_feasibility_verdict(
        seq, N_GLYC_SITES, O_GLYC_SITES, serpin_core_only=False
    )
    glyco_core = glycosylation_feasibility_verdict(
        seq, N_GLYC_SITES, O_GLYC_SITES, serpin_core_only=True
    )

    output = {
        "experiment":                "comp-037",
        "protein":                   "Plasma protease C1 inhibitor (SERPING1 / C1-INH), Homo sapiens (P05155)",
        "alphafold_model":           "AF-P05155-F1-model_v6",
        "signal_peptide_aa":         f"1-{SIGNAL_PEPTIDE_END} (cleaved during secretion in native context; "
                                     "replaced by EcN-native secretion signal in engineered LBP construct)",
        "mature_chain_aa":           f"{MATURE_START}-{MATURE_END}",
        "mucin_domain_aa":           f"{MATURE_START}-{MUCIN_DOMAIN_END} (heavily O-glycosylated tandem-repeat region in vivo; "
                                     "unglycosylated in EcN expression; candidate truncation)",
        "serpin_core_aa":            f"{SERPIN_CORE_START}-{MATURE_END} (mucin-truncated construct, retains RCL R466-T467)",
        "rcl_aa":                    f"{RCL_START}-{RCL_END} (reactive-center loop; P1-P1' R466-T467)",
        "n_glyc_sites":              N_GLYC_SITES,
        "o_glyc_sites":              O_GLYC_SITES,
        "disulfides":                DISULFIDES,
        "conditions":                conditions,
        "sequence_stats":            sequence_stats,
        "protease_results":          protease_results,
        "full_sequence_verdict":     full_verdict,
        "full_sequence_worst_score": full_worst_score,
        "full_sequence_worst_protease": full_worst,
        "mature_verdict":            mature_verdict,
        "mature_worst_score":        mature_worst_score,
        "mature_worst_protease":     mature_worst,
        "serpin_core_verdict":       core_verdict,
        "serpin_core_worst_score":   core_worst_score,
        "serpin_core_worst_protease": core_worst,
        "serpin_core_non_rcl_verdict":      core_non_rcl_verdict,
        "serpin_core_non_rcl_worst_score":  core_non_rcl_worst_score,
        "serpin_core_non_rcl_worst_protease": core_non_rcl_worst,
        "glyco_feasibility_mature":  glyco_mature,
        "glyco_feasibility_serpin_core": glyco_core,
    }

    with open(OUTPUTS / "cleavage_sites.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output, OUTPUTS / "summary.md")
    print(f"Done. Outputs written to {OUTPUTS}/")
    print(f"  Full-sequence:   {full_verdict} (max risk {full_worst_score}, worst: {full_worst})")
    print(f"  Mature (aa 23-500): {mature_verdict} (max risk {mature_worst_score}, worst: {mature_worst})")
    print(f"  Serpin-core (aa {SERPIN_CORE_START}-{MATURE_END}, incl RCL): {core_verdict} (max risk {core_worst_score}, worst: {core_worst})")
    print(f"  Serpin-core non-RCL (degradative only): {core_non_rcl_verdict} (max risk {core_non_rcl_worst_score}, worst: {core_non_rcl_worst})")
    print(f"  Glycosylation (mature):       {glyco_mature['verdict']}")
    print(f"  Glycosylation (serpin-core):  {glyco_core['verdict']}")


def write_summary(data, path):
    ss     = data["sequence_stats"]
    cond   = data["conditions"]
    pr     = data["protease_results"]
    full_verdict   = data["full_sequence_verdict"]
    full_score     = data["full_sequence_worst_score"]
    full_worst     = data["full_sequence_worst_protease"]
    mature_verdict = data["mature_verdict"]
    mature_score   = data["mature_worst_score"]
    mature_worst   = data["mature_worst_protease"]
    core_verdict   = data["serpin_core_verdict"]
    core_score     = data["serpin_core_worst_score"]
    core_worst     = data["serpin_core_worst_protease"]
    core_non_rcl_verdict = data["serpin_core_non_rcl_verdict"]
    core_non_rcl_score   = data["serpin_core_non_rcl_worst_score"]
    core_non_rcl_worst   = data["serpin_core_non_rcl_worst_protease"]
    gm = data["glyco_feasibility_mature"]
    gc = data["glyco_feasibility_serpin_core"]

    lines = [
        "# comp-037 — C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN LBP",
        "",
        f"**Protein:** {data['protein']}  ",
        f"**AlphaFold model:** {data['alphafold_model']}  ",
        f"**Signal peptide:** {data['signal_peptide_aa']}  ",
        f"**Mature chain:** {data['mature_chain_aa']}  ",
        f"**Mucin-like O-glycan domain (candidate truncation):** {data['mucin_domain_aa']}  ",
        f"**Serpin-core construct (mucin-truncated):** {data['serpin_core_aa']}  ",
        f"**RCL (reactive-center loop):** {data['rcl_aa']}  ",
        f"**N-glycosylation sites (UniProt CARBOHYD, full-seq numbering):** {data['n_glyc_sites']}  ",
        f"**O-glycosylation sites (UniProt CARBOHYD, full-seq numbering):** {data['o_glyc_sites']}  ",
        f"**Disulfide bonds (UniProt DISULFID):** {data['disulfides']} — 2 bonds total (verified)  ",
        f"**Conditions modeled:** colonic lumen, pH {cond['pH_range'][0]}-{cond['pH_range'][1]}, "
        f"{cond['temperature_C']}°C, {cond['duration_days'][0]}-{cond['duration_days'][1]} days  ",
        f"**Chassis:** Engineered E. coli Nissle 1917 (EcN) LBP, luminal-secreted format  ",
        f"**Analysis date:** 2026-05-17  ",
        f"**Script:** `experiments/comp-037-c1-inh-protease-stability-ecn/analyze.py`  ",
        f"**Library:** `experiments/lib/protease_stability.py`  ",
        "",
        "---",
        "",
        "## Structural Overview",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Sequence length | {ss['length']} aa (incl. signal peptide aa 1-22) |",
        f"| Mean pLDDT (AlphaFold confidence) | {ss['mean_plddt']} / 100 |",
        f"| Minimum pLDDT | {ss['min_plddt']} / 100 |",
        f"| % residues pLDDT > 80 (well-folded) | {ss['pct_residues_above_80']}% |",
        f"| % residues pLDDT > 90 (core-folded) | {ss['pct_residues_above_90']}% |",
        "",
        "**C1-INH structural notes:**",
        "",
        "- Signal peptide (aa 1-22): disordered, low pLDDT. Replaced by EcN-native signal in the engineered construct.",
        "- Mucin-like N-terminal domain (aa 23-119): disordered (UniProt MobiDB-lite REGION annotations at "
        "aa 20-43 and aa 65-118, with REPEAT 85-119 being 7 × [QE]-P-T-[TQ] tandem repeats). "
        "Heavily O-glycosylated in vivo; **completely unglycosylated when expressed in EcN.** This is the "
        "dominant disordered liability in a bacterial-expression context — directly analogous to the CD55 "
        "Ser/Thr stalk in comp-006.",
        "- Serpin core (aa ~120-450): canonical serpin fold (β-sheet + α-helices), well-folded "
        "(pLDDT > 80 across most of this region). Contains both disulfides (C123-C428, C130-C205) and "
        "the four canonical N-glycan sites of the serpin body (N238, N253, N272-variant, N352).",
        "- Reactive-center loop (RCL, aa ~452-467): exposed flexible loop ending at the P1-P1' R466-T467 "
        "scissile bond. **Inherently protease-accessible by design** — this is how the suicide-substrate "
        "inhibitor mechanism works. The RCL must be cleavable for the inhibitor to function.",
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
            f"| Recognition sites (full sequence) | {r['total_recognition_sites']} |",
            f"| Buried (pLDDT ≥ 80) | {r['buried_sites']} |",
            f"| Partially exposed (pLDDT 65-80) | {r['partially_exposed_sites']} |",
            f"| Exposed (pLDDT < 65) | {r['exposed_sites']} |",
            f"| Residual activity at modeled NaCl | {r['salt_residual_activity_at_nacl']*100:.0f}% |",
            f"| pH activity factor at colonic pH | {r['ph_activity_factor']*100:.0f}% |",
            f"| Effective protease activity | {r['effective_activity']*100:.1f}% |",
            f"| Max risk (full sequence) | {r['max_risk_score']} |",
            f"| Max risk (mature, aa 23-500) | {r['mature_max_risk_score']} |",
            f"| Max risk (mucin domain, aa 23-119) | {r['mucin_max_risk_score']} |",
            f"| Max risk (serpin core, aa 123-500) | {r['core_max_risk_score']} |",
            f"| Max risk (RCL, aa 452-467) | {r['rcl_max_risk_score']} |",
            f"| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | {r['core_non_rcl_max_risk_score']} |",
            f"| Mucin-domain exposed sites | {r['mucin_exposed_sites']} |",
            f"| Serpin-core exposed sites (incl RCL) | {r['core_exposed_sites']} |",
            f"| Serpin-core exposed sites (excl RCL — strictly-degradative) | {r['core_non_rcl_exposed_sites']} |",
            f"| RCL exposed sites (inherent inhibitor-mechanism risk) | {r['rcl_exposed_sites']} |",
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

    def verdict_text(v):
        if v == "LOW":
            return "protease degradation under the modeled colonic-luminal EcN conditions is unlikely to meaningfully reduce activity"
        elif v == "MODERATE":
            return "partial degradation is possible; dominant risk regions warrant engineering attention"
        elif v == "HIGH":
            return "significant protease risk; disordered regions are high-accessibility targets"
        else:  # RED
            return "severe protease risk; this scope is not viable without major engineering"

    lines += [
        "---",
        "",
        "## Per-Scope Verdicts (Protease Risk)",
        "",
        "| Scope | Verdict | Max risk | Worst protease |",
        "|---|---|---|---|",
        f"| Full sequence (aa 1-500) | **{full_verdict}** | {full_score} | `{full_worst}` |",
        f"| Mature protein (aa 23-500, signal peptide removed) | **{mature_verdict}** | {mature_score} | `{mature_worst}` |",
        f"| Serpin core (aa 123-500, mucin truncated, **includes RCL**) | **{core_verdict}** | {core_score} | `{core_worst}` |",
        f"| Serpin core **non-RCL** (strictly-degradative scope) | **{core_non_rcl_verdict}** | {core_non_rcl_score} | `{core_non_rcl_worst}` |",
        "",
        f"**Full-sequence verdict: {full_verdict}** — {verdict_text(full_verdict)}.",
        "",
        f"**Mature-protein verdict: {mature_verdict}** — {verdict_text(mature_verdict)}.",
        "",
        f"**Serpin-core (engineered construct, includes RCL) verdict: {core_verdict}** — {verdict_text(core_verdict)}.",
        "",
        f"**Serpin-core non-RCL (strictly-degradative) verdict: {core_non_rcl_verdict}** — {verdict_text(core_non_rcl_verdict)}.",
        "",
        "**Why two serpin-core verdicts.** The reactive-center loop (RCL, aa 452-467) is **exposed by "
        "design** — the serpin suicide-substrate mechanism requires the RCL to be cleavable by target "
        "proteases (C1r, C1s, MASP-2 in this case). Cleavage of the RCL by C1r/C1s is the inhibitor "
        "mechanism itself. RCL cleavage by *off-target* proteases (DegP, elastase, chymotrypsin) is "
        "different — it consumes the inhibitor without productive trapping of a complement protease. "
        "The 'serpin-core including RCL' verdict reflects the full risk (both productive and "
        "unproductive RCL cleavage); the 'serpin-core non-RCL' verdict reflects the strictly-"
        "degradative risk to the inhibitor body. **The non-RCL verdict is the better measure of "
        "whether the protein folds and persists; the RCL exposure-vs-engagement question is a "
        "kinetic-competition wet-lab question (k_C1s_engagement vs k_DegP_cleavage on the RCL).**",
        "",
        "The serpin-core construct (aa 123-500) replaces aa 1-22 (human signal peptide) with an "
        "EcN-native secretion signal and truncates the mucin-like O-glycan domain (aa 23-119), which "
        "is unglycosylated in EcN and would otherwise be the dominant protease liability — directly "
        "analogous to the CD55 stalk truncation in comp-006 → comp-012.",
        "",
        "---",
        "",
        "## Glycosylation Feasibility (Independent Axis)",
        "",
        "### Mature-protein construct (aa 23-500, mucin domain retained)",
        "",
        f"**Verdict: {gm['verdict']}**",
        "",
        gm['rationale'],
        "",
        "### Serpin-core construct (aa 123-500, mucin domain truncated)",
        "",
        f"**Verdict: {gc['verdict']}**",
        "",
        gc['rationale'],
        "",
        "**Key supporting facts:**",
        "",
        "- C1-INH carries ~26 kDa of glycan on a ~52 kDa polypeptide chain (Bos 1998 PMID 9799502; "
        "Stavenhagen 2018 PMID 29381136 mass-spec characterization).",
        "- In the **plasma / IV** context, N-glycans are critical for the ~30 h circulating half-life. "
        "Bos 1998 showed deglycosylated C1-INH is functionally inhibitory but is cleared rapidly.",
        "- For a **luminal-secreted** format (this scope), plasma half-life is irrelevant — "
        "the inhibitor acts in the gut lumen on locally generated C1r / C1s / MASP-2 at MSU-crystal "
        "interfaces and submucosal CP0 sites. The serpin suicide-mechanism (RCL presentation → "
        "acyl-enzyme covalent trap) does not strictly require glycosylation; the catalytic mechanism "
        "is encoded in the polypeptide.",
        "- EcN does not have an endogenous N-glycosylation system. The *C. jejuni* pgl pathway can be "
        "heterologously transplanted (Wacker 2002), but produces a bacterial-glycan structure distinct "
        "from mammalian biantennary complex N-glycans. The added engineering complexity is substantial "
        "and not warranted unless wet-lab data shows non-glycosylated C1-INH has unacceptable folding "
        "or stability behavior in EcN.",
        "- The mucin-like O-glycan domain (aa 47-96) carries 8 O-linked GalNAc sites in vivo. In an "
        "EcN expression context all are absent. This region is then a disordered hydrophobic-rich "
        "stretch directly accessible to luminal proteases (especially elastase / DegP for the "
        "hydrophobic-prone subsites, and OmpT for any basic-residue pairs).",
        "",
        "---",
        "",
        "## Combined Verdict — Recommendation for the LBP Engineering Track",
        "",
        f"**Protease verdict (serpin-core construct, includes RCL):** {core_verdict}  ",
        f"**Protease verdict (serpin-core non-RCL, strictly-degradative):** {core_non_rcl_verdict}  ",
        f"**Glycosylation feasibility (serpin-core construct):** {gc['verdict']}  ",
        "",
        "The two protease verdicts and the glycosylation verdict are computed independently and are "
        "all load-bearing for the engineering decision. The serpin-core construct (aa 123-500) is the "
        "recommended engineering scope for EcN-LBP luminal C1-INH expression. The headline finding: "
        f"strictly-degradative protease risk on the serpin body is {core_non_rcl_verdict}; the "
        "additional RCL-cleavage risk by off-target proteases is the kinetic-competition wet-lab "
        "question that decides ultimate effectiveness.",
        "",
        "**What this analysis does NOT establish:**",
        "",
        "- Whether the truncated serpin-core construct retains full inhibitor activity (i.e., still "
        "engages C1r / C1s / MASP-2 productively). The reactive-center loop and serpin body fold are "
        "retained in the construct, but the contribution of the N-terminal mucin domain to inhibitor "
        "function (vs. purely a plasma-half-life function) is not fully resolved in the primary "
        "literature. Wet-lab assay against C1r / C1s / MASP-2 substrates is the gate.",
        "- Whether EcN can fold the serpin-core construct with both disulfides correctly formed. "
        "EcN periplasmic DsbA / DsbC can in principle catalyze the two C123-C428 and C130-C205 "
        "bonds, but serpin-fold quality in a bacterial chassis is a known wet-lab risk (Bottomley "
        "2000-era literature on bacterial serpin expression).",
        "- Whether luminal C1-INH can productively reach the CP0 priming sites (submucosal "
        "macrophages, MSU-crystal-interface convertases) at functionally relevant concentrations. "
        "This is the same H05-class wet-lab gate question facing the DAF SCR1-4 koji track.",
        "",
        "---",
        "",
        "## Limitations",
        "",
        "- **Disulfides not modeled.** The C123-C428 and C130-C205 bonds substantially reduce backbone "
        "flexibility in the serpin core. This analysis likely **overestimates risk in the serpin core**. "
        "Note that C1-INH has only 2 disulfides — far less stabilization than CD55 SCR1-4 (8 bonds) — "
        "so the over-estimate is modest.",
        "- **O-glycosylation of the mucin domain not modeled in the native baseline.** In a glycosylated "
        "native context, the mucin domain is sterically shielded by O-GalNAc / sialylated chains. The "
        "scoring here treats the mucin domain as an unglycosylated polypeptide — which is the correct "
        "model for the EcN expression context, but means the score is NOT directly comparable to the "
        "in vivo (heavily glycosylated) protease-stability profile of native serum C1-INH.",
        "- **pLDDT ≠ solvent accessibility.** Surface-exposed loops on a well-folded serpin core may "
        "have high pLDDT but still be protease-accessible. SASA-based refinement would tighten the "
        "score.",
        "- **P1/P1' rules only.** Extended subsite specificity (P2-P4) not modeled. Trypsin and OmpT "
        "in particular have non-trivial P2 preferences (e.g., trypsin K/R-P bonds resist cleavage) "
        "which would refine site counts downward.",
        "- **Commensal-bacterial protease load not modeled.** The five-protease panel covers the "
        "dominant identifiable risks (pancreatic + EcN-native) but the colonic microbiome contributes "
        "a diffuse additional protease landscape that is not enzyme-level characterized for this scope.",
        "- **Bile-acid effects not modeled.** Bile acids in the upper colon can partially unfold "
        "proteins and may enhance protease access to otherwise-buried sites — treated here as "
        "out-of-model.",
        "- **EcN secretion topology not directly modeled.** Whether the construct is exported via "
        "Type I (HlyA-like), Type II (secretome), Sec/YebF (extracellular), or signal-peptide-driven "
        "periplasmic + outer-membrane-permeabilized release is an engineering choice that will affect "
        "exposure to OmpT and DegP. This analysis pools both risks but does not condition on a specific "
        "export pathway.",
        "",
        "---",
        "",
        "## Comparison with comp-006 / comp-012 (DAF/CD55 on koji)",
        "",
        "| Feature | DAF/CD55 (comp-006, koji) | DAF/CD55 SCR1-4 (comp-012, koji) | C1-INH (comp-037, EcN) |",
        "|---|---|---|---|",
        "| Chassis | A. oryzae koji | A. oryzae koji | E. coli Nissle 1917 LBP |",
        "| Environment | Shio-koji (17.5% NaCl, pH 4.5-5) | Shio-koji | Colonic lumen (~0.15 M NaCl, pH 6-7) |",
        "| Mechanism | Convertase decay (surface) | Convertase decay (surface) | C1r / C1s / MASP-2 inhibition (entry) |",
        "| Protease panel | ALP, NPr, acid_protease | ALP, NPr, acid_protease | trypsin, chymotrypsin, elastase, OmpT, DegP |",
        "| Construct (engineered) | aa 35-353 (ectodomain) | aa 35-285 (SCR1-4 only) | aa 123-500 (serpin core, mucin truncated) |",
        f"| Verdict (engineered construct) | HIGH (stalk-driven) | LOW | **{core_verdict}** |",
        "| Glycosylation issue | O-glyc stalk (koji can O-glyc but differently) | O-glyc stalk removed | N-glyc (EcN cannot N-glyc); O-glyc (mucin removed) |",
        "| Disulfide load | 8 bonds in SCR1-4 (canonical CCP) | 8 bonds in SCR1-4 | 2 bonds in serpin body |",
        "",
        "**Architectural read:** comp-037 + comp-012 together support the two-chassis CP0 architecture "
        "surfaced 2026-05-16 in [`complement-c5a-gout.md` §9.8](../../../complement-c5a-gout.md): "
        "C1-INH on EcN at classical/lectin entry, DAF SCR1-4 on koji at surface convertase decay. "
        "Two independent mechanisms at two cascade points via two independent chassis.",
        "",
        "---",
        "",
        "*Generated by `analyze.py` on 2026-05-17. Uses experiments/lib/protease_stability.py. "
        "Re-run after any AlphaFold model update or MEROPS specificity revision. "
        "See inputs/provenance.md for data sources and citations.*",
    ]

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
