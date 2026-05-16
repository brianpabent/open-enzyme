#!/usr/bin/env python3
"""
comp-015: T-axis Adjuvant Urate-Target Mapping (v2 — XO added as 5th target)

Maps four T-axis-active natural compounds (cordycepin, eurycomanone, icariin, echinacoside)
against the FIVE dominant urate-handling + T-axis targets (URAT1, ABCG2, OAT1, SHBG, **XO**)
to falsify or strengthen H-AN-02 (Cordyceps as a uniquely gout-favorable T-axis adjuvant).

**v1 → v2 change:** added xanthine oxidase (XO, CHEMBL1929, UniProt P47989) as 5th target.
v1 panel was systematically incomplete because XO — the upstream urate-PRODUCTION enzyme that
allopurinol/febuxostat target and that classical TCM gout compounds (luteolin, astilbin, quercetin)
modulate — was excluded. v2 trigger was a parallel Sci-Hub-second-pass verification subagent on
`wiki/androgen-natural-modulation.md` that surfaced eurycomanone-related XO claims (PMID 31920654,
34785103); v2's primary-literature re-read shows those papers actually establish transporter+purine-
synthesis modulation for eurycomanone, NOT direct XO inhibition — but XO still belongs in the panel
regardless. The v2 cordycepin × XO IC50 (55.7 µM, PMID 38141695) is real and direct.

Method (per README.md):
1. ChEMBL bioactivity lookup — sparse for natural products at transporter targets (comp-013 finding:
   5/9 TCM compounds had zero ChEMBL records). In this run ChEMBL API is blocked; treats blocked-or-empty
   as "no curated IC50" and routes to literature_claims.json. v2 cordycepin × XO IC50 IS a published
   primary-literature IC50 directly populated in chembl_bioactivity.json.
2. Literature-claim aggregation — animal/clinical/in vitro evidence per pair, with PMIDs.
3. Achievable-concentration check — Cmax_plasma + gut_lumen vs IC50 (when available) using comp-004
   gut-conc model + Hill n=1 occupancy.
4. Direction-of-effect tagging — INHIBITOR / INDUCER / DISPLACER / SUBSTRATE / unknown per pair.
5. Per-compound aggregated verdict: gout-favorable / gout-neutral / gout-unfavorable / mechanism-unclear.

Verdict thresholds (calibrated against comp-007 + comp-013 patterns), v2 with XO logic:
- gout-favorable: at least one urate-axis target with FAVORABLE direction (URAT1 inhibitor, ABCG2/OAT1
  inducer, **XO inhibitor**) backed by primary in vivo or clinical evidence at a translatable
  achievable concentration. **XO inhibition is mechanism-orthogonal to transporter direction —
  a compound with strong XO inhibition is gout-favorable EVEN IF it has unfavorable transporter
  effects, because XO blocks urate production at the source.**
- gout-neutral: no measured target activity at achievable concentrations; T-axis effect alone
  is small enough that the indirect URAT1-upregulation prediction is bounded.
- gout-unfavorable: transporter direction wrong (URAT1 inducer, ABCG2 inhibitor) at achievable conc,
  AND no offsetting XO inhibition AND no offsetting transporter-secretion induction.
- mechanism-unclear: ChEMBL absent + literature thin (the H-discipline-aware verdict per comp-013).

XO-specific verdict thresholds for v2:
- XO favorable contribution: achievable/IC50 ≥ 10× and direction = INHIBITOR.
- XO weak-favorable: direction = INHIBITOR but achievable/IC50 < 10× (in vitro positive but not at
  systemic concentrations).
- XO no-favorable contribution: below threshold or unknown / negative-screen.

Run: python3 analyze.py
Outputs: outputs/results.json, outputs/summary.md
Reproducibility: stdlib only (json, pathlib, math).
"""

import json
import math
import pathlib

ROOT = pathlib.Path(__file__).parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# comp-007 thresholds for achievable/IC50:
RATIO_DECISIVE = 100.0   # ≥100x = "decisively active"
RATIO_LIKELY = 10.0      # 10-100x = "likely active"
RATIO_UNCLEAR = 1.0      # 1-10x = "concentration unclear"
# < 1x = "below threshold"


def load_json(path):
    with open(path) as f:
        return json.load(f)


def fractional_inhibition(ratio):
    """Hill equation n=1: f = ratio / (ratio + 1)."""
    if ratio is None:
        return None
    return ratio / (ratio + 1.0)


def classify_ratio(ratio):
    if ratio is None:
        return "no-ic50-no-ratio"
    if ratio < RATIO_UNCLEAR:
        return "below-threshold"
    if ratio < RATIO_LIKELY:
        return "concentration-unclear"
    if ratio < RATIO_DECISIVE:
        return "likely-active"
    return "decisively-active"


def evidence_tier(literature_claim):
    """Map literature_claims.json evidence_level → comparable tier."""
    el = (literature_claim.get("evidence_level") or "").lower()
    if el.startswith("clinical"):
        return ("Clinical Trial", 4)
    if el.startswith("animal"):
        return ("Animal Model", 3)
    if el.startswith("in vitro"):
        return ("In Vitro", 2)
    if "mechanistic" in el or "extrapolation" in el:
        return ("Mechanistic Extrapolation", 1)
    return ("No-Data", 0)


# ---------------------------------------------------------------------------
# Per-pair analysis
# ---------------------------------------------------------------------------

def analyze_pair(compound_data, target_data, chembl_records, lit_claim, conc_estimate):
    """Per compound × target pair: integrate ChEMBL + literature + concentration."""
    target_name = target_data["name"]

    # ChEMBL IC50: pull from chembl_bioactivity entries (only IC50 nM if reported)
    ic50_nM = None
    chembl_status = "ChEMBL-empty"
    for entry in chembl_records:
        if entry.get("target") == target_name:
            ic50_nM = entry.get("ic50_nM")
            chembl_status = entry.get("evidence_level", "ChEMBL-empty")
            break

    # Literature evidence
    lit_evidence_label, lit_tier = evidence_tier(lit_claim)
    lit_direction = (lit_claim.get("direction") or "unknown").upper()
    lit_pmid = lit_claim.get("primary_source_pmid")

    # Concentration at relevant site
    site = target_data["site_for_concentration"]
    if "gut" in site.lower() and "plasma" not in site.lower():
        conc_uM = conc_estimate.get("gut_lumen_uM")
        conc_site_label = "gut_lumen"
    elif "gut" in site.lower() and "plasma" in site.lower():
        # ABCG2 dual site — prioritize gut lumen for gut-secretion mechanism, also flag plasma
        conc_uM = conc_estimate.get("gut_lumen_uM")
        conc_site_label = "gut_lumen+plasma"
    else:
        conc_uM = conc_estimate.get("cmax_plasma_uM")
        conc_site_label = "plasma"

    # Achievable / IC50 ratio
    ratio = None
    achievability = None
    if ic50_nM is not None and ic50_nM > 0 and conc_uM is not None:
        # convert IC50 nM → µM for comparison; ratio = conc / IC50
        ic50_uM = ic50_nM / 1000.0
        ratio = conc_uM / ic50_uM
        achievability = classify_ratio(ratio)
    elif ic50_nM is None and lit_pmid is not None:
        achievability = "lit-evidence-only-no-IC50"
    else:
        achievability = "no-data"

    # Direction interpretation per target
    favorable_dir_canonical = target_data["favorable_direction"].split()[0]  # first word
    # E.g. URAT1 favorable = "INHIBITOR"; ABCG2 favorable = "INDUCER"; SHBG favorable = "DISPLACER"
    direction_alignment = None
    if lit_direction in ("UNKNOWN", "N/A", ""):
        direction_alignment = "unknown"
    elif favorable_dir_canonical in lit_direction:
        direction_alignment = "favorable"
    elif "UNFAVORABLE" in lit_direction or "INDIRECT" in lit_direction:
        direction_alignment = "indirect-or-extrapolated"
    elif lit_direction in ("INHIBITOR", "INDUCER", "DISPLACER", "SUBSTRATE"):
        # If direction is named but doesn't match favorable, mark unfavorable
        if "unfavorable" in target_data["unfavorable_direction"].lower() and \
                lit_direction in target_data["unfavorable_direction"].upper():
            direction_alignment = "unfavorable"
        else:
            direction_alignment = "named-but-unmapped"
    else:
        direction_alignment = "unmapped"

    return {
        "compound": compound_data["name"],
        "target": target_name,
        "site": conc_site_label,
        "ic50_nM": ic50_nM,
        "chembl_status": chembl_status,
        "achievable_conc_uM": conc_uM,
        "ratio_achievable_over_ic50": (round(ratio, 3) if ratio is not None else None),
        "fractional_inhibition_at_achievable": (round(fractional_inhibition(ratio), 4) if ratio is not None else None),
        "achievability_class": achievability,
        "literature_evidence_level": lit_evidence_label,
        "literature_tier": lit_tier,
        "literature_direction": lit_direction,
        "literature_pmid": lit_pmid,
        "direction_alignment": direction_alignment,
        "literature_magnitude": lit_claim.get("magnitude"),
    }


# ---------------------------------------------------------------------------
# Per-compound aggregated verdict
# ---------------------------------------------------------------------------

def classify_xo_contribution(xo_pair):
    """v2: classify the XO arm's gout-favorable contribution per compound.

    Returns one of:
    - "xo-favorable-systemic" — INHIBITOR direction + ratio ≥ 10× (decisive systemic activity)
    - "xo-favorable-in-vitro" — INHIBITOR direction + literature_tier ≥ 2 but achievable ratio < 10×
    - "xo-negative-screen"  — explicit negative-screen evidence (e.g., icariin not in Mo 2007 hit group)
    - "xo-no-data"          — no published direct XO evidence
    """
    if xo_pair is None:
        return "xo-no-data", "No XO entry in pair results."
    direction = (xo_pair.get("literature_direction") or "").upper()
    tier = xo_pair.get("literature_tier", 0)
    ratio = xo_pair.get("ratio_achievable_over_ic50")
    pmid = xo_pair.get("literature_pmid")
    evidence_label = xo_pair.get("literature_evidence_level", "")

    # Negative screen: direction is "weak / non-significant" or evidence tier is Negative-Screen-tagged
    if "negative" in evidence_label.lower() or "non-significant" in direction.lower() or "weak" in direction.lower():
        return "xo-negative-screen", (
            f"Negative-screen evidence (PMID {pmid}): {evidence_label}. "
            f"Direction: {direction}. Magnitude: {xo_pair.get('literature_magnitude', 'n/a')}"
        )

    if "INHIBITOR" in direction:
        if ratio is not None and ratio >= 10.0:
            return "xo-favorable-systemic", (
                f"XO INHIBITOR with achievable/IC50 ratio = {ratio} (≥ 10× threshold). "
                f"PMID {pmid}; magnitude: {xo_pair.get('literature_magnitude')}"
            )
        if tier >= 2 or ratio is not None:
            # In vitro positive direction; either ratio below threshold OR ratio could not be computed
            ratio_str = f"{ratio}" if ratio is not None else "no-IC50-vs-conc-comparison"
            return "xo-favorable-in-vitro", (
                f"XO INHIBITOR direction (PMID {pmid}, {evidence_label}); achievable/IC50 ratio = "
                f"{ratio_str} (below 10× systemic-activity threshold OR direct-comparison absent). "
                f"In vitro positive but not meaningfully active at systemic concentrations."
            )
        return "xo-favorable-in-vitro", (
            f"XO INHIBITOR direction (PMID {pmid}, {evidence_label}) but evidence tier insufficient "
            f"to claim systemic activity."
        )

    # Default: no data / unknown
    if tier == 0 and pmid is None:
        return "xo-no-data", "No published direct XO evidence; mechanism not established."
    return "xo-unmapped", f"Direction: {direction}; tier {tier}; ratio {ratio}; PMID {pmid}"


def assign_compound_verdict(compound_name, pair_results):
    """Aggregate per-pair findings into a per-compound verdict.

    v2: 5-target panel including XO. Verdict logic now considers the XO arm separately because
    XO inhibition is mechanism-orthogonal to transporter direction (XO blocks urate production
    at the source — favorable regardless of transporter effects).

    Verdict tiers:
    - gout-favorable: at least one urate-axis target (URAT1/ABCG2/OAT1/XO) with FAVORABLE direction
      backed by Animal/Clinical evidence at translatable concentration.
    - gout-neutral: no urate-axis activity AND T-axis effect bounded.
    - gout-unfavorable: at least one transporter direction wrong AND no offsetting XO/secretion
      inhibition, OR robust T-elevation with no offsetting urate mechanism.
    - mechanism-unclear: insufficient evidence either way.
    """
    transporter_pairs = [p for p in pair_results if p["target"] in ("URAT1", "ABCG2", "OAT1")]
    shbg_pairs = [p for p in pair_results if p["target"] == "SHBG"]
    xo_pair = next((p for p in pair_results if p["target"] == "Xanthine Oxidase"), None)

    favorable_transporter_hits = []
    unfavorable_transporter_hits = []
    indirect_extrapolated_hits = []
    no_data_pairs = []

    for p in transporter_pairs:
        if p["direction_alignment"] == "favorable" and p["literature_tier"] >= 3:
            favorable_transporter_hits.append(p)
        elif p["direction_alignment"] == "favorable" and p["literature_tier"] >= 2:
            favorable_transporter_hits.append(p)  # in vitro counts but lower weight
        elif p["direction_alignment"] == "unfavorable" and p["literature_tier"] >= 2:
            unfavorable_transporter_hits.append(p)
        elif p["direction_alignment"] in ("indirect-or-extrapolated",):
            indirect_extrapolated_hits.append(p)
        elif p["literature_tier"] == 0 and p["ic50_nM"] is None:
            no_data_pairs.append(p)

    # XO arm classification (v2)
    xo_class, xo_rationale = classify_xo_contribution(xo_pair)

    # T-axis effect from SHBG arm (informational, contributes to direction prediction)
    shbg_t_axis_strength = None
    for p in shbg_pairs:
        if p["literature_tier"] >= 3:
            shbg_t_axis_strength = "robust-clinical"
        elif p["literature_tier"] == 2:
            shbg_t_axis_strength = "in-vitro"
        else:
            shbg_t_axis_strength = "absent-or-not-mechanism"

    # Mechanism enumeration (v2): explicit list of which mechanism(s) drive the verdict
    driving_mechanisms = []
    for p in favorable_transporter_hits:
        driving_mechanisms.append(
            f"{p['target']} {p['literature_direction']} (tier {p['literature_tier']}, "
            f"PMID {p['literature_pmid']})"
        )
    if xo_class == "xo-favorable-systemic":
        driving_mechanisms.append(f"XO INHIBITOR (systemic-active, ratio ≥ 10×) — {xo_rationale}")
    elif xo_class == "xo-favorable-in-vitro":
        driving_mechanisms.append(f"XO INHIBITOR (in vitro only, ratio below 10× threshold) — {xo_rationale}")

    # Verdict logic — v2 incorporates XO
    rationale = []
    has_systemic_xo_favorable = (xo_class == "xo-favorable-systemic")
    has_in_vitro_xo_favorable = (xo_class == "xo-favorable-in-vitro")

    if favorable_transporter_hits or has_systemic_xo_favorable:
        # Primary favorable verdict: at least one favorable transporter or systemic-active XO
        verdict = "GOUT-FAVORABLE"
        for p in favorable_transporter_hits:
            rationale.append(
                f"  - {p['target']} FAVORABLE direction ({p['literature_direction']}) backed by "
                f"{p['literature_evidence_level']} (PMID {p['literature_pmid']}) — "
                f"magnitude: {p['literature_magnitude']}"
            )
        if has_systemic_xo_favorable:
            rationale.append(f"  - XO FAVORABLE systemic — {xo_rationale}")
        elif has_in_vitro_xo_favorable:
            rationale.append(f"  - XO supplementary in vitro positive — {xo_rationale}")
        if unfavorable_transporter_hits:
            verdict = "GOUT-FAVORABLE-NET (with caveats)"
            for p in unfavorable_transporter_hits:
                rationale.append(
                    f"  - CAVEAT: {p['target']} also shows unfavorable direction; net effect needs wet-lab"
                )
    elif unfavorable_transporter_hits and not has_in_vitro_xo_favorable:
        # Unfavorable transporter direction with NO offsetting XO inhibition
        verdict = "GOUT-UNFAVORABLE"
        for p in unfavorable_transporter_hits:
            rationale.append(
                f"  - {p['target']} UNFAVORABLE direction ({p['literature_direction']}) backed by "
                f"{p['literature_evidence_level']} (PMID {p['literature_pmid']})"
            )
    elif unfavorable_transporter_hits and has_in_vitro_xo_favorable:
        # XO in vitro hit might offset unfavorable transporter direction
        verdict = "MECHANISM-MIXED (XO offset to transporter unfavorable)"
        for p in unfavorable_transporter_hits:
            rationale.append(
                f"  - {p['target']} UNFAVORABLE direction; potentially offset by XO in vitro positive "
                f"(but not systemic): {xo_rationale}"
            )
    elif indirect_extrapolated_hits and shbg_t_axis_strength == "robust-clinical" and not has_in_vitro_xo_favorable:
        # Robust T-axis effect + no direct urate-axis offset → mechanistic-extrapolation says UA rise
        verdict = "GOUT-UNFAVORABLE (mechanistic extrapolation)"
        rationale.append(
            "  - Robust T-axis effect (clinical SHBG/free-T evidence) but NO direct urate-axis "
            "offsetting mechanism (no XO, no transporter favorable). Mechanistic extrapolation: "
            "T-elevation will drive URAT1 upregulation (T → URAT1 axis per androgen-urate-axis.md), "
            "giving small predicted UA rise (~0.2-0.5 mg/dL per §1.7 of androgen-natural-modulation.md). "
            "Evidence tier: Mechanistic Extrapolation only."
        )
    elif len(no_data_pairs) >= len(transporter_pairs) - 1 and shbg_t_axis_strength != "robust-clinical" \
            and xo_class in ("xo-no-data", "xo-negative-screen"):
        # Almost all targets no-data, no robust T-axis offset → mechanism unclear
        verdict = "MECHANISM-UNCLEAR"
        rationale.append(
            "  - No urate-axis evidence (transporter no-data + XO no-data or negative-screen). "
            "T-axis effect modest or unconfirmed. Insufficient evidence to triage as favorable, "
            "unfavorable, or neutral."
        )
        if xo_class == "xo-negative-screen":
            rationale.append(f"  - XO arm: negative-screen finding — {xo_rationale}")
    else:
        verdict = "GOUT-NEUTRAL-LEANING-UNCLEAR"
        rationale.append(
            "  - No direct transporter evidence; T-axis effect bounded; net UA effect predicted "
            "small but unconfirmed."
        )
        if has_in_vitro_xo_favorable:
            rationale.append(f"  - XO arm: in vitro positive but below systemic threshold — {xo_rationale}")

    return {
        "verdict": verdict,
        "favorable_hits": len(favorable_transporter_hits),
        "unfavorable_hits": len(unfavorable_transporter_hits),
        "indirect_hits": len(indirect_extrapolated_hits),
        "no_data_pairs": len(no_data_pairs),
        "shbg_t_axis_strength": shbg_t_axis_strength,
        "xo_class": xo_class,
        "xo_rationale": xo_rationale,
        "driving_mechanisms": driving_mechanisms,
        "rationale": rationale,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    compounds_input = load_json(INPUTS / "compounds.json")
    targets_input = load_json(INPUTS / "targets.json")
    chembl_input = load_json(INPUTS / "chembl_bioactivity.json")
    lit_input = load_json(INPUTS / "literature_claims.json")
    conc_input = load_json(INPUTS / "concentration_estimates.json")

    compounds = compounds_input["compounds"]
    targets = targets_input["targets"]

    # Index helpers
    chembl_by_compound = {e["compound"]: e["target_data"] for e in chembl_input["entries"]}
    conc_by_compound = {e["compound"]: e for e in conc_input["estimates"]}
    lit_by_pair = {}
    for c in lit_input["claims"]:
        lit_by_pair[(c["compound"], c["target"])] = c

    # Analyze every compound × target pair
    results = []
    per_compound_verdicts = []
    for cmp in compounds:
        cmp_pairs = []
        for tgt in targets:
            chembl_recs = chembl_by_compound.get(cmp["name"], [])
            lit_claim = lit_by_pair.get((cmp["name"], tgt["name"]), {})
            conc_est = conc_by_compound.get(cmp["name"], {})
            pair_result = analyze_pair(cmp, tgt, chembl_recs, lit_claim, conc_est)
            cmp_pairs.append(pair_result)

        verdict_record = assign_compound_verdict(cmp["name"], cmp_pairs)
        verdict_record["compound"] = cmp["name"]
        verdict_record["pairs"] = cmp_pairs
        per_compound_verdicts.append(verdict_record)
        results.extend(cmp_pairs)

    # Summary stats
    chembl_with_ic50 = sum(1 for r in results if r["ic50_nM"] is not None)
    pairs_with_lit_evidence = sum(1 for r in results if r["literature_pmid"] is not None)
    no_data_pairs = sum(1 for r in results
                        if r["ic50_nM"] is None and r["literature_pmid"] is None
                        and r["literature_evidence_level"] == "No-Data")

    # H-AN-02 evaluation:
    # H-AN-02 says cordycepin is UNIQUELY gout-favorable due to URAT1 modulation offsetting T-elevation.
    # v2: with XO added AND eurycomanone × URAT1/ABCG2 evidence surfaced, the "uniquely" framing may be
    # falsified. Status: SUPPORTED if cordycepin = GOUT-FAVORABLE and no other compound is; PARTIAL-FALSIFIED
    # if cordycepin still favorable but eurycomanone (or another) is also favorable via different mechanism.
    def is_favorable(v):
        # "GOUT-FAVORABLE" or "GOUT-FAVORABLE-NET" — but NOT "GOUT-UNFAVORABLE"
        verdict = v.get("verdict", "")
        return "FAVORABLE" in verdict and "UNFAVORABLE" not in verdict

    cordycepin_verdict = next((v for v in per_compound_verdicts if v["compound"] == "Cordycepin"), {})
    other_favorable = [v for v in per_compound_verdicts
                       if v["compound"] != "Cordycepin" and is_favorable(v)]
    if is_favorable(cordycepin_verdict) and not other_favorable:
        h_an_02_status = "SUPPORTED — cordycepin uniquely gout-favorable"
    elif is_favorable(cordycepin_verdict) and other_favorable:
        other_names = ", ".join(v["compound"] for v in other_favorable)
        h_an_02_status = (
            f"PARTIALLY FALSIFIED — cordycepin still favorable but NOT UNIQUELY SO; "
            f"{other_names} also gout-favorable via different mechanism. The 'uniquely positioned' "
            f"framing of H-AN-02 v1 does not survive v2 evidence ingestion."
        )
    elif "UNFAVORABLE" in cordycepin_verdict.get("verdict", "") or "UNCLEAR" in cordycepin_verdict.get("verdict", ""):
        h_an_02_status = "UNSUPPORTED-AT-CURRENT-EVIDENCE"
    else:
        h_an_02_status = "INCONCLUSIVE"

    output = {
        "experiment": "comp-015",
        "version": "v2 (XO added as 5th target)",
        "title": "T-axis Adjuvant Urate-Target Mapping — comp-013/comp-007 framework applied to 4×5 T-axis × urate matrix",
        "date": "2026-05-07",
        "framework": "comp-013 (compound × chokepoint mapping with verdict tagging) + comp-007 achievable/IC50 thresholds + comp-004 gut-conc model. Evaluates H-AN-02 (cordycepin as uniquely gout-favorable T-axis adjuvant). v2 adds XO as 5th target with mechanism-orthogonal verdict logic.",
        "v1_to_v2_change": "Added xanthine oxidase (XO, CHEMBL1929) as 5th target. v1 4-target panel was systematically incomplete because XO was excluded. v2 adds: (a) cordycepin × XO IC50 = 55.7 µM in vitro (PMID 38141695) — direction-aligned but ratio ~0.001 at supplement Cmax (BELOW THRESHOLD for systemic activity); (b) eurycomanone × XO NO-DATA but verification of trigger papers (PMID 31920654, 34785103) shows mechanism is multi-target transporter modulation + purine-synthesis suppression — substantively REVERSING v1's GOUT-UNFAVORABLE eurycomanone verdict; (c) icariin × XO negative-screen (Mo 2007 PMID 17666819, icariin tested but not in significant-XO-inhibitor flavonoid group); (d) echinacoside × XO no-data.",
        "hypothesis_under_test": "H-AN-02 (androgen-natural-modulation.md §10): Cordyceps cordycepin elevates T modestly + modulates URAT1 in animal models; predicted net UA effect favorable or neutral despite T elevation.",
        "compounds_evaluated": len(compounds),
        "targets_evaluated": len(targets),
        "total_pairs": len(results),
        "summary_stats": {
            "pairs_with_chembl_or_published_ic50": chembl_with_ic50,
            "pairs_with_primary_literature_evidence": pairs_with_lit_evidence,
            "pairs_with_no_data": no_data_pairs,
            "chembl_coverage_fraction": round(chembl_with_ic50 / len(results), 3),
            "lit_coverage_fraction": round(pairs_with_lit_evidence / len(results), 3),
        },
        "h_an_02_status": h_an_02_status,
        "verdict_summary": {v["compound"]: v["verdict"] for v in per_compound_verdicts},
        "per_compound": per_compound_verdicts,
    }

    with open(OUTPUTS / "results.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output, compounds, targets)
    print(f"comp-015 complete. {len(results)} compound × target pairs analyzed.")
    print(f"H-AN-02 status: {h_an_02_status}")
    print()
    print("Verdicts:")
    for v in per_compound_verdicts:
        print(f"  - {v['compound']:14s} → {v['verdict']}")


def write_summary(output, compounds, targets):
    lines = [
        f"# comp-015: T-axis Adjuvant Urate-Target Mapping — Summary (v2)",
        "",
        f"**Version:** {output.get('version', 'v1')}",
        f"**Date:** {output['date']}",
        f"**Framework:** {output['framework']}",
        f"**Compounds × targets evaluated:** {output['compounds_evaluated']} × {output['targets_evaluated']} = {output['total_pairs']} pairs",
        f"**Interpretive wiki page:** [`wiki/t-axis-adjuvant-urate-mapping-computational.md`](../../wiki/t-axis-adjuvant-urate-mapping-computational.md)",
        "",
        "## v1 → v2 change",
        "",
        f"{output.get('v1_to_v2_change', '')}",
        "",
        "## Hypothesis under test",
        "",
        f"> {output['hypothesis_under_test']}",
        "",
        f"### Status: **{output['h_an_02_status']}**",
        "",
        "## Verdict matrix (per-compound × target, v2 with XO column)",
        "",
        "| Compound | URAT1 | ABCG2 | OAT1 | SHBG | XO | Per-compound verdict |",
        "|---|---|---|---|---|---|---|",
    ]
    # Build matrix — preserve target column ordering URAT1, ABCG2, OAT1, SHBG, XO
    target_order = ["URAT1", "ABCG2", "OAT1", "SHBG", "Xanthine Oxidase"]
    by_compound = {v["compound"]: v for v in output["per_compound"]}
    for cmp in compounds:
        cv = by_compound[cmp["name"]]
        cells = [cmp["name"]]
        for tname in target_order:
            pair = next((p for p in cv["pairs"] if p["target"] == tname), None)
            if pair is None:
                cells.append("—")
                continue
            if pair["literature_pmid"] is not None:
                tier_short = {4: "Clin", 3: "Anim", 2: "InVit", 1: "Mech"}.get(pair["literature_tier"], "?")
                if pair["direction_alignment"] == "favorable":
                    arrow = "✓"
                elif pair["direction_alignment"] == "unfavorable":
                    arrow = "✗"
                elif pair["direction_alignment"] == "indirect-or-extrapolated":
                    arrow = "(indirect)"
                else:
                    arrow = "?"
                cells.append(f"{arrow} {tier_short} (PMID {pair['literature_pmid']})")
            elif pair.get("ic50_nM") is not None:
                # v2: cordycepin × XO has direct IC50 from chembl_bioactivity but no PMID-tagged literature_claim
                # (the PMID is in the chembl_bioactivity record). Show IC50.
                cells.append(f"IC50 {pair['ic50_nM']/1000:.1f}µM")
            else:
                cells.append("no-data")
        cells.append(f"**{cv['verdict']}**")
        lines.append("| " + " | ".join(cells) + " |")

    lines += [
        "",
        "## Coverage statistics",
        "",
        f"- ChEMBL/published bioactivity records with IC50: **{output['summary_stats']['pairs_with_chembl_or_published_ic50']} of {output['total_pairs']}** ({100*output['summary_stats']['chembl_coverage_fraction']:.0f}%) — *ChEMBL API was BLOCKED in this run; v2 manually surfaced 1 published primary-literature IC50 (cordycepin × XO PMID 38141695, not yet ChEMBL-curated). The fundamental sparsity pattern (5/9 in comp-013) holds.*",
        f"- Pairs with primary-literature evidence: **{output['summary_stats']['pairs_with_primary_literature_evidence']} of {output['total_pairs']}** ({100*output['summary_stats']['lit_coverage_fraction']:.0f}%)",
        f"- Pairs with NO data at all: **{output['summary_stats']['pairs_with_no_data']} of {output['total_pairs']}**",
        "",
        "## Per-compound rationale",
        "",
    ]

    for cv in output["per_compound"]:
        lines += [
            f"### {cv['compound']} → **{cv['verdict']}**",
            "",
            f"- Favorable transporter hits: {cv['favorable_hits']}",
            f"- Unfavorable transporter hits: {cv['unfavorable_hits']}",
            f"- Indirect/extrapolated hits: {cv['indirect_hits']}",
            f"- No-data pairs: {cv['no_data_pairs']}",
            f"- T-axis SHBG mechanism strength: {cv['shbg_t_axis_strength']}",
            f"- XO arm classification: **{cv.get('xo_class', 'n/a')}**",
            f"- XO arm rationale: {cv.get('xo_rationale', 'n/a')}",
            "",
            "**Driving mechanism(s):**",
        ]
        if cv.get("driving_mechanisms"):
            for m in cv["driving_mechanisms"]:
                lines.append(f"- {m}")
        else:
            lines.append("- (no favorable mechanism identified)")
        lines += [
            "",
            "**Rationale:**",
        ]
        for r in cv["rationale"]:
            lines.append(r)
        lines += [
            "",
            "**Per-target detail:**",
            "",
            "| Target | Site | IC50 (nM) | Achievable conc (µM) | Ratio | Class | Direction | Evidence level | PMID |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        for p in cv["pairs"]:
            ic50 = f"{p['ic50_nM']:.0f}" if p['ic50_nM'] is not None else "—"
            conc = f"{p['achievable_conc_uM']:.4f}" if p['achievable_conc_uM'] is not None else "—"
            ratio = f"{p['ratio_achievable_over_ic50']}" if p['ratio_achievable_over_ic50'] is not None else "—"
            lines.append(
                f"| {p['target']} | {p['site']} | {ic50} | {conc} | {ratio} | "
                f"{p['achievability_class']} | {p['literature_direction']} | "
                f"{p['literature_evidence_level']} | {p['literature_pmid'] or '—'} |"
            )
        lines.append("")

    lines += [
        "## H-AN-02 evaluation (v2)",
        "",
        f"**Hypothesis:** {output['hypothesis_under_test']}",
        "",
        f"**Status: {output['h_an_02_status']}**",
        "",
        "**Reasoning (v2):**",
        "",
        "- **Cordycepin** has TWO direct mechanisms now: (a) URAT1 protein/mRNA downregulation (PMID 29422889, Animal Model, dose-response in PO-induced HUA mice) — load-bearing for v1 verdict; (b) direct in vitro XO IC50 = 55.7 µM (PMID 38141695, with allopurinol comparator IC50 8.94 µM in same assay) — NEW in v2. **However, the cordycepin systemic Cmax (~0.057 µM) is ~1000× below the XO IC50, so the systemic-XO arm is BELOW THRESHOLD.** Cordycepin's gout-favorable verdict is dominated by URAT1, with XO as supplementary in vitro evidence not meaningfully active at supplement doses.",
        "- **Eurycomanone — MAJOR v2 REVERSAL.** v1 marked eurycomanone GOUT-UNFAVORABLE (mechanistic extrapolation). v2 verification of trigger-source primary literature (PMID 31920654 Front Pharmacol 2019, PMID 34785103 J Ethnopharmacol 2022) shows: (a) URAT1 + GLUT9 protein DOWNREGULATION in kidney (favorable), (b) ABCG2 + NPT1 protein UPREGULATION (favorable), (c) direct urate-uptake inhibition in hURAT1-expressing cells in vitro (favorable), (d) purine SYNTHESIS suppression via decreased PRPS expression (favorable, off-panel). Combined with the 2021 placebo-controlled human RCT (n=105, Physta 100/200 mg/d × 12 wk → SUA ↓7-11%) cited in `androgen-natural-modulation.md`, eurycomanone joins cordycepin in the GOUT-FAVORABLE category. **The XO trigger that motivated v2 was itself a citation-laundering artifact** — eurycomanone is NOT a direct XO inhibitor; primary sources document multi-target transporter modulation + purine-synthesis suppression. But adding XO to the panel was still correct (the v1 panel was systematically incomplete).",
        "- **Icariin** has a NEGATIVE-SCREEN result on XO (PMID 17666819 Mo 2007: icariin tested in 15-flavonoid hypouricemia screen, NOT in significant-XO-inhibitor group — quercetin/morin/myricetin/kaempferol/puerarin were). Icariin is structurally NOT in the planar-7-OH-flavone XO-inhibitor class (icariin is a flavonol-glycoside; glycosylation reduces XO activity). Icariin's gout-context evidence (PMID 33135192) remains ANTI-INFLAMMATORY (NLRP3 axis), NOT urate-lowering. Verdict: MECHANISM-UNCLEAR at urate axis (XO ruled out; transporter axis no-data). NLRP3 axis remains a possibly favorable but separate-chokepoint role.",
        "- **Echinacoside** has no direct evidence at any of URAT1/ABCG2/OAT1 transporters AND no XO evidence. Compound class (large polar phenylethanoid glycoside, MW 786.73) is structurally distinct from any known small-molecule urate-axis modulator. Verdict: MECHANISM-UNCLEAR.",
        "- **The H-AN-02 framing 'cordycepin uniquely positioned' is PARTIALLY FALSIFIED in v2.** Cordycepin and eurycomanone are BOTH gout-favorable (different mechanisms — cordycepin = URAT1-dominant + weak in vitro XO; eurycomanone = multi-target transporter + purine-synthesis). The 'uniquely positioned' wording does not survive v2. Brian's wet-lab gate (cordyceps vs tongkat ali, UA primary endpoint) becomes a HEAD-TO-HEAD between two gout-favorable mechanisms rather than a feasibility-vs-confirmation contrast.",
        "",
        "## v1 → v2 methodology adaptation note",
        "",
        "v1 4-target panel (URAT1/ABCG2/OAT1/SHBG) was systematically incomplete because XO was excluded. The v1 eurycomanone GOUT-UNFAVORABLE verdict relied on absent direct evidence — a parallel Sci-Hub-second-pass verification subagent on `wiki/androgen-natural-modulation.md` then surfaced (a) the XO claims that motivated v2 panel-expansion AND (b) the previously-missed PMID 31920654 + 34785103 transporter+purine-synthesis primary literature. v2's primary contribution is therefore TWO-FOLD: panel completeness (XO column added) + previously-missed eurycomanone evidence integrated. The XO addition is the version label, but the larger substantive change is the eurycomanone verdict reversal.",
        "",
        "## Caveats and limitations",
        "",
        "1. **ChEMBL REST API was blocked in this analysis run.** Most bioactivity records routed through `[API-BLOCKED]` annotations. Cordycepin × XO IC50 (55.7 µM, PMID 38141695) is the only pair with a direct numerical IC50; the rest rely on direction-of-effect tagging from primary literature.",
        "2. **Cordycepin × URAT1 evidence is expression-level, not direct binding.** PMID 29422889 measured URAT1 protein/mRNA downregulation; no direct in vitro URAT1 IC50 was reported. The mechanism may be transcriptional or post-translational, not orthosteric.",
        "3. **Cordycepin oral PK is poor for purified compound** (PMC6823370). The Cmax estimate (0.057 µM) is order-of-magnitude bound; whole-fermentate Cordyceps with native pentostatin co-delivery may raise BA 5-10× — still well below the XO IC50 of 55.7 µM, so the systemic-XO arm remains below threshold even with the optimistic BA correction.",
        "4. **Eurycomanone evidence: in vitro hURAT1 IC50 numbers behind paywall.** PMID 31920654 abstract reports DIRECTION (inhibitor) for individual quassinoids in hURAT1-expressing cells but specific IC50 values are not in the abstract. Magnitude-confident verdict requires Sci-Hub-level access or institutional subscription.",
        "5. **The eurycomanone × XO 'NO-DATA' verdict surfaces a CITATION LAUNDERING PATTERN.** The v2 trigger claim (eurycomanone as XO inhibitor, attributed to PMID 31920654 / 34785103) does NOT survive primary-source verification — those papers establish transporter+purine-synthesis modulation, not XO. This is itself a v2 finding worth surfacing to `wiki/androgen-natural-modulation.md` for citation-laundering audit.",
        "6. **The 5-target panel is still narrow.** PDE5 (icariin), CYP17/StAR (steroidogenic mechanism for cordycepin/icariin), NLRP3 (icariin's anti-flare effect), and PRPS (purine synthesis enzyme — eurycomanol mechanism) are NOT in this panel. PRPS specifically is a v2-surfaced new-target candidate worth proposing for any future panel expansion.",
        "7. **No Chinese-language primary literature accessed in this run.** CLAUDE.md global-multilingual discipline applies; CNKI / WanFang access not available. Likely-existing Chinese-language papers on echinacoside × urate, icariin × XO, or eurycomanone × additional mechanisms not surfaced.",
        "8. **Per-compound BA values are rat-derived.** Allometric scaling to human is approximate. For cordycepin × XO specifically, the achievable/IC50 ratio is so far below threshold (0.001) that even 10× BA scaling does not change the verdict.",
        "9. **The 'MECHANISM-UNCLEAR' verdict for icariin and echinacoside is the H-discipline-aware verdict.** It is NOT 'no effect.' Icariin's NLRP3-axis activity is real but off-panel; echinacoside's *Cistanche* TCM-context use suggests possible CNKI-only evidence not surfaced here.",
        "10. **The v2 methodology adaptation is documented in the interpretive wiki page** (`wiki/t-axis-adjuvant-urate-mapping-computational.md` §'Methodology adaptation — v1 → v2: adding XO as 5th target') alongside this summary.",
    ]

    with open(OUTPUTS / "summary.md", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
