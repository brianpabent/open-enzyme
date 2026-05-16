#!/usr/bin/env python3
"""
comp-007: Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue

Stage 1 in silico analysis: ranks food-grade HDAC inhibitor candidates on three axes:
  1. Class-I HDAC potency (HDAC1/2/3 — relevant to Q141K trafficking rescue via HSF1/Hsp90)
  2. HDAC6 selectivity (HDAC6 is off-target; pan-HDAC cardiotoxicity rationale)
  3. Gut-vs-systemic exposure proxy (low oral bioavailability → gut-selective)

Composite score = potency_score × selectivity_score × gut_selectivity_score

Each factor is 0-1 normalized. Score is 0 for compounds with no usable IC50 data.
Compounds with DATA_UNAVAILABLE confidence are ranked but flagged; their scores are
based on mechanistic extrapolation or are set to 0.

Relevant to: validation-experiments.md §1.22
Run: python3 analyze.py
Outputs: outputs/ranking.json, outputs/summary.md
"""

import json
import math
import pathlib

ROOT = pathlib.Path(__file__).parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# --- Scoring parameters ---

# Potency normalization: highest-potency compound gets score 1.0.
# We use the geometric mean IC50 of HDAC1, HDAC2, HDAC3 (lower = more potent = higher score).
# If isoform data is absent, use the estimated effective class I IC50.
# If no estimate available, compound is scored 0 on this axis.

# Selectivity: HDAC6_IC50 / mean(HDAC1/2/3_IC50)
# Higher ratio = more class-I-selective vs HDAC6 = higher score.
# Normalized: ratio / (ratio + ratio_ref) where ratio_ref = 10 (compounds with ~10x selectivity get 0.5 score).
# HDAC6 IC50 unavailable → selectivity unknown → score set to SELECTIVITY_UNKNOWN_PENALTY (0.3).
# This penalizes compounds with unknown HDAC6 profile relative to butyrate (222x selectivity → ~1.0).
SELECTIVITY_NORMALIZATION_MIDPOINT = 10.0
SELECTIVITY_UNKNOWN_PENALTY = 0.3

# Gut selectivity: 1 - oral_bioavailability_fraction
# Fully gut-retained (BA=0) → score 1.0; fully absorbed (BA=1) → score 0.
# This is the proxy for gut-enriched activity; low BA = compound stays in GI lumen.
# Note: for butyrate, low systemic BA reflects colonocyte consumption — still favorable for gut activity.


def load_json(path):
    with open(path) as f:
        return json.load(f)


def geomean_ic50(ic50_list):
    """Geometric mean of a list of IC50 values (nM). Returns None if list is empty."""
    valid = [v for v in ic50_list if v is not None]
    if not valid:
        return None
    log_mean = sum(math.log(v) for v in valid) / len(valid)
    return math.exp(log_mean)


def potency_score_raw(mean_ic50_nM):
    """Convert mean class-I IC50 (nM) to a raw potency value: 1/IC50 (higher = more potent)."""
    if mean_ic50_nM is None:
        return 0.0
    return 1.0 / mean_ic50_nM


def selectivity_ratio(hdac123_mean_nM, hdac6_ic50_nM):
    """HDAC6_IC50 / mean(HDAC1/2/3_IC50). Higher = more class-I-selective."""
    if hdac123_mean_nM is None or hdac6_ic50_nM is None:
        return None
    return hdac6_ic50_nM / hdac123_mean_nM


def selectivity_score_from_ratio(ratio):
    """Normalize selectivity ratio to 0-1 using sigmoid-like transform.
    ratio / (ratio + MIDPOINT): midpoint = 10 → score 0.5; ratio = 222 → score ~0.957."""
    if ratio is None:
        return SELECTIVITY_UNKNOWN_PENALTY
    return ratio / (ratio + SELECTIVITY_NORMALIZATION_MIDPOINT)


def gut_selectivity_score(oral_ba):
    """1 - bioavailability. Low BA → compound stays in gut → high gut-selectivity score."""
    return max(0.0, 1.0 - oral_ba)


def normalize(values):
    """Min-max normalize a list to [0, 1]. Returns list of same length."""
    nonzero = [v for v in values if v > 0]
    if not nonzero:
        return [0.0] * len(values)
    vmax = max(nonzero)
    if vmax == 0:
        return [0.0] * len(values)
    return [v / vmax for v in values]


def main():
    candidates_data = load_json(INPUTS / "candidates.json")
    bioactivity_data = load_json(INPUTS / "bioactivity_data.json")
    targets_data = load_json(INPUTS / "hdac_targets.json")

    bio_by_compound = {e["compound"]: e for e in bioactivity_data["entries"]}

    results = []
    for c in candidates_data["candidates"]:
        name = c["name"]
        bio = bio_by_compound.get(name, {})

        confidence = bio.get("confidence", "DATA_UNAVAILABLE")
        data_unavailable = confidence == "DATA_UNAVAILABLE"

        # --- Axis 1: Class-I HDAC potency ---
        hdac1 = bio.get("HDAC1_IC50_nM")
        hdac2 = bio.get("HDAC2_IC50_nM")
        hdac3 = bio.get("HDAC3_IC50_nM")
        hdac6 = bio.get("HDAC6_IC50_nM")

        # Fall back to estimate if direct IC50 absent
        if all(v is None for v in [hdac1, hdac2, hdac3]):
            est = bio.get("effective_HDAC_class_I_IC50_estimate_nM")
            mean_class_i = est
            used_estimate = True
        else:
            available = [v for v in [hdac1, hdac2, hdac3] if v is not None]
            mean_class_i = geomean_ic50(available)
            used_estimate = False

        potency_raw = potency_score_raw(mean_class_i)

        # --- Axis 2: HDAC6 selectivity ---
        if hdac6 is None and mean_class_i is not None:
            ratio = None
            sel_score = SELECTIVITY_UNKNOWN_PENALTY
        elif hdac6 is not None and mean_class_i is not None:
            ratio = selectivity_ratio(mean_class_i, hdac6)
            sel_score = selectivity_score_from_ratio(ratio)
        else:
            ratio = None
            sel_score = 0.0 if data_unavailable else SELECTIVITY_UNKNOWN_PENALTY

        # --- Axis 3: Gut selectivity ---
        oral_ba = c["oral_bioavailability_fraction"]
        gut_score = gut_selectivity_score(oral_ba)

        results.append({
            "compound": name,
            "chembl_id": c.get("chembl_id"),
            "food_source": c["food_source"],
            "gras_status": c["gras_status"],
            "confidence": confidence,
            "used_estimate": used_estimate,
            "data_unavailable": data_unavailable,
            "hdac1_ic50_nM": hdac1,
            "hdac2_ic50_nM": hdac2,
            "hdac3_ic50_nM": hdac3,
            "hdac6_ic50_nM": hdac6,
            "mean_class_i_ic50_nM": round(mean_class_i, 1) if mean_class_i else None,
            "hdac6_selectivity_ratio": round(ratio, 1) if ratio else None,
            "potency_raw": potency_raw,
            "selectivity_score_raw": round(sel_score, 4),
            "gut_selectivity_score_raw": round(gut_score, 4),
            "oral_bioavailability_fraction": oral_ba,
            "hdac_mechanism": c["hdac_mechanism"],
            "typical_gut_concentration_uM": c["typical_gut_concentration_uM"],
        })

    # --- Normalize potency scores ---
    potency_raws = [r["potency_raw"] for r in results]
    potency_normalized = normalize(potency_raws)

    # --- Compute composite scores ---
    for i, r in enumerate(results):
        p = potency_normalized[i]
        s = r["selectivity_score_raw"]
        g = r["gut_selectivity_score_raw"]

        # Compounds with no usable data (DATA_UNAVAILABLE) get composite = 0
        if r["data_unavailable"]:
            composite = 0.0
        else:
            composite = p * s * g

        r["potency_score_normalized"] = round(p, 4)
        r["composite_score"] = round(composite, 4)

    # --- Rank by composite score descending ---
    results.sort(key=lambda x: x["composite_score"], reverse=True)
    for i, r in enumerate(results):
        r["rank"] = i + 1

    # --- Build output ---
    output = {
        "experiment": "comp-007",
        "title": "Food-Grade HDAC Inhibitor Screen for Q141K-ABCG2 Trafficking Rescue",
        "date": "2026-05-05",
        "scoring_formula": {
            "description": "composite_score = potency_score_normalized × selectivity_score × gut_selectivity_score",
            "potency_score": "1/mean(HDAC1/2/3 geometric-mean IC50 nM), then max-normalized to [0,1] across candidates with data",
            "selectivity_score": "HDAC6_IC50 / (HDAC6_IC50 + mean_class_I_IC50) normalized via ratio/(ratio+10); compounds with unknown HDAC6 receive penalty score 0.30; DATA_UNAVAILABLE compounds score 0",
            "gut_selectivity_score": "1 - oral_bioavailability_fraction (proxy: low BA = compound stays in gut lumen)",
            "composite_zero": "Compounds with DATA_UNAVAILABLE confidence (no usable IC50 or estimate) receive composite_score = 0",
            "normalization_midpoint_selectivity": SELECTIVITY_NORMALIZATION_MIDPOINT,
            "selectivity_unknown_penalty": SELECTIVITY_UNKNOWN_PENALTY,
        },
        "targets": {
            "HDAC1": "CHEMBL325",
            "HDAC2": "CHEMBL1937",
            "HDAC3": "CHEMBL1829",
            "HDAC6": "CHEMBL1865",
        },
        "results": results,
        "data_gaps_summary": [
            "Sulforaphane: no isoform-specific IC50; effective estimate used (LOW confidence); HDAC6 selectivity unknown (penalty applied)",
            "Allyl Mercaptan: no ChEMBL entry; estimated from bulk nuclear extract (LOW confidence); HDAC6 selectivity unknown",
            "DADS: no ChEMBL entry; estimated from bulk nuclear extract (LOW confidence); HDAC6 selectivity unknown",
            "PEITC: no ChEMBL entry; estimated by analogy with sulforaphane (LOW confidence); HDAC6 selectivity unknown",
            "Caffeic Acid: no isoform IC50 available in ChEMBL or primary literature; scored 0 (DATA_UNAVAILABLE)",
            "Ferulic Acid: no isoform IC50 available in ChEMBL or primary literature; scored 0 (DATA_UNAVAILABLE)",
        ],
        "limitations": [
            "Heterogeneous assay formats: butyrate IC50 values from biochemical recombinant assay (highest confidence); sulforaphane/AM/DADS from nuclear extract or cellular protein level (lower confidence). Direct comparison is approximate.",
            "HDAC6 selectivity data absent for sulforaphane, AM, DADS, PEITC. Unknown penalty (0.30) penalizes these compounds vs butyrate (confirmed 222x selectivity). If HDAC6 IC50 were measured and found to be >1 mM for these compounds, their scores would increase substantially.",
            "Gut-vs-systemic proxy (1 - oral BA) is a coarse surrogate. High oral BA (sulforaphane) reduces gut-selectivity score, but SFN reaches enterocytes before portal absorption — the gut mucosal cell may still have substantial SFN exposure. This proxy underestimates SFN's enterocyte-level activity.",
            "Oral bioavailability values are estimates from literature rather than direct human PK measurements at food-achievable doses.",
            "Q141K trafficking rescue (the key outcome) has not been tested for any compound except the vorinostat class-I reference compound (Basseville 2012). Butyrate's class-I selectivity and IC50 predict rescue, but direct demonstration is Stage 3.",
            "Evidence level: all analyses are Mechanistic Extrapolation per Open Enzyme wiki evidence-level convention. No wet-lab confirmation at Stage 1.",
        ],
    }

    with open(OUTPUTS / "ranking.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output)
    print("comp-007 complete. Outputs written to outputs/")
    print_table(results)


def print_table(results):
    print("\n| Rank | Compound | Mean HDAC1-3 IC50 | HDAC6 IC50 | Sel. ratio | Gut BA | Composite | Confidence |")
    print("|---|---|---|---|---|---|---|---|")
    for r in results:
        ic50_str = f"{r['mean_class_i_ic50_nM']:,.0f} nM" if r["mean_class_i_ic50_nM"] else "N/A"
        hdac6_str = f"{r['hdac6_ic50_nM']:,.0f} nM" if r["hdac6_ic50_nM"] else "N/A"
        ratio_str = f"{r['hdac6_selectivity_ratio']:.0f}x" if r["hdac6_selectivity_ratio"] else "unknown"
        est_flag = "*" if r["used_estimate"] else ""
        print(
            f"| {r['rank']} | {r['compound']} | {ic50_str}{est_flag} | {hdac6_str} | "
            f"{ratio_str} | {r['oral_bioavailability_fraction']:.0%} | {r['composite_score']:.4f} | {r['confidence']} |"
        )
    print("\n* = estimated value (see provenance.md); actual IC50 unavailable")


def write_summary(output):
    results = output["results"]
    lines = [
        "# comp-007: Food-Grade HDAC Inhibitor Screen — Summary",
        "",
        f"**Date:** {output['date']}",
        f"**Experiment:** {output['title']}",
        "**Informs:** [`validation-experiments.md` §1.22](../../wiki/validation-experiments.md#122-gut-selective-food-grade-hdac-inhibitor-screen-for-q141k-abcg2-trafficking-rescue)",
        "**Interpretive wiki page:** [`wiki/food-grade-hdaci-screen-computational.md`](../../wiki/food-grade-hdaci-screen-computational.md)",
        "",
        "## Scoring formula",
        "",
        "```",
        "composite_score = potency_score × selectivity_score × gut_selectivity_score",
        "```",
        "",
        "| Factor | Definition | Range |",
        "|---|---|---|",
        "| **potency_score** | 1/mean(HDAC1/2/3 geometric-mean IC50 nM), max-normalized | 0–1 |",
        "| **selectivity_score** | HDAC6_IC50 / (HDAC6_IC50 + mean_class_I_IC50), normalized at midpoint ratio=10 | 0–1 |",
        "| **gut_selectivity_score** | 1 − oral bioavailability fraction | 0–1 |",
        "",
        "Compounds with DATA_UNAVAILABLE confidence (no usable IC50 or estimate) receive composite_score = 0.",
        "Compounds with unknown HDAC6 selectivity receive selectivity_score = 0.30 (penalty vs butyrate's confirmed 222× selectivity).",
        "",
        "## Ranking table",
        "",
        "| Rank | Compound | Mean HDAC1-3 IC50 (nM) | HDAC6 IC50 (nM) | Sel. ratio | Oral BA | Potency (norm) | Sel. score | Gut score | Composite | Confidence |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    for r in results:
        ic50_str = f"{r['mean_class_i_ic50_nM']:,.0f}*" if r["mean_class_i_ic50_nM"] and r["used_estimate"] else (f"{r['mean_class_i_ic50_nM']:,.0f}" if r["mean_class_i_ic50_nM"] else "N/A")
        hdac6_str = f"{r['hdac6_ic50_nM']:,.0f}" if r["hdac6_ic50_nM"] else "N/A"
        ratio_str = f"{r['hdac6_selectivity_ratio']:.0f}×" if r["hdac6_selectivity_ratio"] else "unknown"
        lines.append(
            f"| {r['rank']} | **{r['compound']}** | {ic50_str} | {hdac6_str} | "
            f"{ratio_str} | {r['oral_bioavailability_fraction']:.0%} | "
            f"{r['potency_score_normalized']:.3f} | {r['selectivity_score_raw']:.3f} | "
            f"{r['gut_selectivity_score_raw']:.3f} | **{r['composite_score']:.4f}** | {r['confidence']} |"
        )

    lines += [
        "",
        "\\* = estimated value (see `inputs/provenance.md`); actual IC50 unavailable from ChEMBL or primary literature",
        "",
        "## Top candidates and Stage 2 recommendation",
        "",
    ]

    scored = [r for r in results if r["composite_score"] > 0]
    unscored = [r for r in results if r["composite_score"] == 0]

    if scored:
        top = scored[0]
        lines += [
            f"### Rank 1: {top['compound']} (composite {top['composite_score']:.4f})",
            "",
            f"- **Mean HDAC1/2/3 IC50:** {'estimated ' if top['used_estimate'] else ''}{top['mean_class_i_ic50_nM']:,.0f} nM (confidence: {top['confidence']})" if top['mean_class_i_ic50_nM'] else "- **Mean HDAC1/2/3 IC50:** N/A",
            f"- **HDAC6 IC50:** {top['hdac6_ic50_nM']:,.0f} nM" if top['hdac6_ic50_nM'] else "- **HDAC6 IC50:** Not measured",
            f"- **HDAC6 selectivity ratio:** {top['hdac6_selectivity_ratio']:.0f}×" if top['hdac6_selectivity_ratio'] else "- **HDAC6 selectivity ratio:** Unknown",
            f"- **Oral bioavailability:** {top['oral_bioavailability_fraction']:.0%}",
            f"- **Food source:** {top['food_source']}",
            f"- **HDAC mechanism:** {top['hdac_mechanism'][:200]}...",
            "",
        ]

    for i, r in enumerate(scored[1:], 2):
        lines += [
            f"### Rank {r['rank']}: {r['compound']} (composite {r['composite_score']:.4f})",
            "",
            f"- **Mean HDAC1/2/3 IC50:** {'estimated ' if r['used_estimate'] else ''}{r['mean_class_i_ic50_nM']:,.0f} nM" if r['mean_class_i_ic50_nM'] else "- **Mean HDAC1/2/3 IC50:** N/A",
            f"- **HDAC6 selectivity ratio:** {r['hdac6_selectivity_ratio']:.0f}×" if r['hdac6_selectivity_ratio'] else "- **HDAC6 selectivity ratio:** Unknown (penalty score 0.30 applied)",
            f"- **Oral bioavailability:** {r['oral_bioavailability_fraction']:.0%}",
            f"- **Food source:** {r['food_source']}",
            "",
        ]

    if unscored:
        lines += [
            "### Compounds scored 0 (DATA_UNAVAILABLE — Stage 1 gap)",
            "",
            "The following candidates have no usable isoform-specific IC50 data from ChEMBL or primary literature.",
            "They are not ranked but are not excluded — they require a targeted biochemical screen at Stage 2 to obtain scoreable data.",
            "",
        ]
        for r in unscored:
            lines.append(f"- **{r['compound']}** — {r['food_source']}. {r['hdac_mechanism'][:120]}...")
        lines.append("")

    lines += [
        "## Stage 2 advancement decision",
        "",
        "**Advance to Stage 2 (paired Caco-2 / HepG2 HDAC activity assay):**",
        "",
    ]
    advance = [r for r in scored if r["composite_score"] > 0]
    for r in advance[:3]:
        rationale = ""
        if r["hdac6_ic50_nM"] is not None:
            rationale = f"Confirmed class-I selectivity ({r['hdac6_selectivity_ratio']:.0f}×). "
        else:
            rationale = "HDAC6 selectivity unconfirmed — Stage 2 must include HDAC6 isoform-selective substrate assay. "
        if r["used_estimate"]:
            rationale += "IC50 is estimated (Stage 2 will confirm or falsify the ranking position)."
        else:
            rationale += "IC50 from biochemical assay (high confidence)."
        lines.append(f"- **{r['compound']}** (rank {r['rank']}, score {r['composite_score']:.4f}) — {rationale}")

    lines += [
        "",
        "**Drop from Stage 2 (DATA_UNAVAILABLE — redirect to biochemical IC50 screen first):**",
        "",
    ]
    for r in unscored:
        lines.append(f"- **{r['compound']}** — no isoform-specific IC50 data available. Recommend targeted HDAC1/2/3 biochemical assay before Stage 2 cellular work.")

    lines += [
        "",
        "## Data gaps materially affecting the ranking",
        "",
    ]
    for gap in output["data_gaps_summary"]:
        lines.append(f"- {gap}")

    lines += [
        "",
        "## Limitations",
        "",
    ]
    for lim in output["limitations"]:
        lines.append(f"- {lim}")

    lines += [
        "",
        "## Provenance",
        "",
        "All source data, ChEMBL activity IDs, and PubMed citations: [`inputs/provenance.md`](../inputs/provenance.md)",
        "",
        "**Evidence level:** Mechanistic Extrapolation (per Open Enzyme wiki evidence-level convention). "
        "No wet-lab data has been generated for comp-007. Rankings reflect published biochemical and cellular IC50 data "
        "plus literature-derived estimates where primary IC50 data is absent.",
    ]

    with open(OUTPUTS / "summary.md", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
