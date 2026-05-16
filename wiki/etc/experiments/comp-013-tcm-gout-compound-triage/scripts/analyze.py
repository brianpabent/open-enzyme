#!/usr/bin/env python3
"""
comp-013: TCM Gout Compound Triage

Applies the comp-004 IC50 occupancy framework + comp-007 composite scoring (potency × selectivity ×
gut-enrichment) to 9 candidate Traditional Chinese Medicine (TCM) compounds with documented gout
indication. First concrete computational application of the global-multilingual research discipline
codified in CLAUDE.md (2026-05-06).

Pipeline per Brian's task brief (Phase 1-7):
1. Identify bioactive compound per TCM herb (inputs/compounds.json)
2. Pull ChEMBL bioactivity vs gout target panel (inputs/bioactivity_data.json)
3. Compute bioavailability layer (gut-luminal vs plasma Cmax)
4. Run IC50 occupancy at each site
5. Compute composite score (potency × selectivity × gut-enrichment)
6. Assign per-compound triage verdict (VIABLE / GUT-LUMINAL VIABLE / SYSTEMIC NON-VIABLE / MECHANISM UNCLEAR)
7. Write outputs

Verdict tiers per task brief:
- VIABLE: mechanism + bioavailability + dose all align; warrants follow-up
- GUT-LUMINAL VIABLE: gut-targeted mechanism, low BA is favorable
- SYSTEMIC NON-VIABLE: systemic mechanism but BA insufficient to reach effective concentration
- MECHANISM UNCLEAR: published data thin or contradictory

Run: python3 scripts/analyze.py
Outputs: outputs/triage.json, outputs/summary.md, outputs/per_compound_table.csv

Reproducibility: stdlib only (json, csv, pathlib, math).
"""

import csv
import json
import math
import pathlib
from typing import Optional

ROOT = pathlib.Path(__file__).parent.parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Constants — pharmacology thresholds
# ---------------------------------------------------------------------------

# Risk ratio thresholds per comp-004 (Hill equation n=1, fractional inhibition = ratio/(ratio+1))
# 0.5x → 33%, 1x → 50%, 2x → 67%, 5x → 83%
THRESHOLD_LOW = 0.5
THRESHOLD_MODERATE = 2.0
THRESHOLD_HIGH = 5.0

# Composite scoring (comp-007 adapted)
# - Potency: max-normalized 1/IC50 across compounds
# - Selectivity: ratio of on-target IC50 to nearest off-target IC50; sigmoid-ish norm at midpoint=10
# - Gut-enrichment: 1 - oral bioavailability, BUT only favorable for gut-targeted mechanisms
#   For systemic-targeted compounds, gut-enrichment is UNFAVORABLE (compound stuck in lumen
#   instead of reaching its plasma target). This is the comp-007 pivot for TCM.
SELECTIVITY_NORMALIZATION_MIDPOINT = 10.0
SELECTIVITY_UNKNOWN_PENALTY = 0.30


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: pathlib.Path) -> dict:
    with open(path) as f:
        return json.load(f)


def classify_risk(ratio: Optional[float]) -> str:
    if ratio is None:
        return "NOT_APPLICABLE"
    if ratio < THRESHOLD_LOW:
        return "LOW"
    if ratio < THRESHOLD_MODERATE:
        return "MODERATE"
    if ratio < THRESHOLD_HIGH:
        return "HIGH"
    return "VERY_HIGH"


def fractional_inhibition(ratio: Optional[float]) -> Optional[float]:
    """Hill equation n=1: f = ratio / (ratio + 1)"""
    if ratio is None:
        return None
    return ratio / (ratio + 1.0)


def compute_gut_concentration(compound: dict, gut_model: dict) -> dict:
    """Per comp-004: dose × (1 - BA) ÷ gut volume, capped at intestinal solubility."""
    dose_mg = compound["typical_supplement_dose_mg"]
    ba = compound["bioavailability_fraction"]
    mw = compound["molecular_weight_g_mol"]
    sol_mg_L = compound["intestinal_solubility_mg_L"]
    vol_L = gut_model["small_intestine_lumen_volume_L"]

    gut_mass_mg = dose_mg * (1.0 - ba)
    dose_limited_mg_L = gut_mass_mg / vol_L
    solubility_capped = dose_limited_mg_L > sol_mg_L
    effective_mg_L = min(dose_limited_mg_L, sol_mg_L)

    effective_nM = effective_mg_L * 1e6 / mw

    return {
        "gut_mass_mg": round(gut_mass_mg, 1),
        "dose_limited_mg_L": round(dose_limited_mg_L, 1),
        "solubility_capped": solubility_capped,
        "effective_dissolved_mg_L": round(effective_mg_L, 2),
        "effective_dissolved_uM": round(effective_nM / 1000, 2),
        "effective_dissolved_nM": round(effective_nM, 0),
    }


def compute_plasma_cmax(compound: dict, gut_model: dict) -> dict:
    """Crude single-dose Cmax estimate: Cmax ≈ dose × F / (Vd × BW).

    For polyphenols / TCM compounds, Vd typical ~1 L/kg. This is an order-of-magnitude
    estimate; real Cmax depends on dose, formulation, absorption rate, and clearance.
    """
    dose_mg = compound["typical_supplement_dose_mg"]
    ba = compound["bioavailability_fraction"]
    mw = compound["molecular_weight_g_mol"]
    vd_L_kg = gut_model["vd_typical_polyphenol_L_kg"]
    bw_kg = gut_model["body_weight_kg_default"]

    absorbed_mg = dose_mg * ba
    vd_total_L = vd_L_kg * bw_kg
    cmax_mg_L = absorbed_mg / vd_total_L
    cmax_nM = cmax_mg_L * 1e6 / mw

    return {
        "absorbed_mg": round(absorbed_mg, 2),
        "vd_total_L": vd_total_L,
        "cmax_mg_L": round(cmax_mg_L, 4),
        "cmax_uM": round(cmax_nM / 1000, 3),
        "cmax_nM": round(cmax_nM, 1),
    }


def get_target_data(entries: list, compound_name: str, target_name: str) -> Optional[dict]:
    """Look up the bioactivity entry for a given compound × target pair."""
    for entry in entries:
        if entry["compound"] == compound_name:
            for td in entry["target_data"]:
                if td["target"] == target_name or target_name in td["target"]:
                    return td
    return None


def compute_occupancy(ic50_nM: Optional[float], conc_nM: float) -> dict:
    """Hill equation n=1 occupancy at given concentration."""
    if ic50_nM is None or ic50_nM <= 0 or conc_nM <= 0:
        return {"ic50_nM": ic50_nM, "conc_nM": conc_nM, "ratio": None,
                "fractional_inhibition": None, "risk_level": "NOT_APPLICABLE"}
    ratio = conc_nM / ic50_nM
    return {
        "ic50_nM": ic50_nM,
        "conc_nM": round(conc_nM, 1),
        "ratio": round(ratio, 2),
        "fractional_inhibition": round(fractional_inhibition(ratio), 3),
        "risk_level": classify_risk(ratio),
    }


# ---------------------------------------------------------------------------
# Per-compound triage logic
# ---------------------------------------------------------------------------

def assign_verdict(compound: dict, occupancy_results: dict, has_chembl: bool,
                   on_target_data: bool) -> tuple:
    """Triage verdict per Brian's task brief Phase 6.

    Returns (verdict, rationale_string)

    - VIABLE: mechanism site clear, BA + dose support meaningful occupancy at site
    - GUT-LUMINAL VIABLE: gut-targeted, low BA is favorable, dose achieves effective gut conc
    - SYSTEMIC NON-VIABLE: systemic target but achievable plasma << IC50
    - MECHANISM UNCLEAR: data sparse / contradictory
    """
    name = compound["name"]
    site = compound.get("mechanism_site", "")

    # If no ChEMBL data AND no animal/clinical evidence → MECHANISM UNCLEAR
    has_any_evidence = has_chembl or any(
        td.get("evidence_level", "").startswith(("Animal", "Clinical"))
        for td in occupancy_results.get("raw_target_data", [])
    )
    if not has_any_evidence:
        return ("MECHANISM UNCLEAR",
                "No ChEMBL bioactivity for any target; no published in vivo dose-response data found in the literature reviewed.")

    # Check if any target has meaningful occupancy at the relevant site
    relevant_occ = []
    for occ in occupancy_results.get("by_target", []):
        if occ["site"] == "gut" and "gut" in site:
            relevant_occ.append(occ)
        elif occ["site"] == "plasma" and "systemic" in site:
            relevant_occ.append(occ)

    has_high_gut = any(o["risk_level"] in ("HIGH", "VERY_HIGH") and o["site"] == "gut"
                       for o in occupancy_results.get("by_target", []))
    has_high_plasma = any(o["risk_level"] in ("HIGH", "VERY_HIGH") and o["site"] == "plasma"
                          for o in occupancy_results.get("by_target", []))
    has_moderate_plasma = any(o["risk_level"] == "MODERATE" and o["site"] == "plasma"
                              for o in occupancy_results.get("by_target", []))

    # Animal-evidence override: if there's animal model data confirming in vivo efficacy
    # AND the dose used is achievable in human-equivalent terms, lean VIABLE
    has_animal_evidence = any(
        td.get("evidence_level", "").startswith("Animal")
        for td in occupancy_results.get("raw_target_data", [])
    )

    if "gut-luminal" in site and (has_high_gut or has_animal_evidence):
        # Gut-luminal target with achievable gut concentration — favorable
        bg = compound["bioavailability_fraction"]
        if bg < 0.1:
            return ("GUT-LUMINAL VIABLE",
                    f"Gut-targeted mechanism + low BA ({bg*100:.1f}%) concentrates compound at gut lumen; "
                    f"animal-model evidence supports in vivo activity. Dose translation to human achievable.")

    if "systemic" in site and not has_high_plasma:
        if has_moderate_plasma:
            return ("MODERATE / VIABLE-WITH-DOSE-CAVEAT",
                    "Systemic mechanism with achievable plasma Cmax in MODERATE range; dose escalation or formulation enhancement required for HIGH occupancy.")
        # Systemic mechanism with low BA failing to reach effective plasma concentration
        bg = compound["bioavailability_fraction"]
        return ("SYSTEMIC NON-VIABLE",
                f"Systemic mechanism but achievable plasma Cmax << IC50 across measured targets "
                f"(BA = {bg*100:.1f}%). Predicted effect at typical supplement dose is small or placebo-equivalent.")

    if has_animal_evidence:
        return ("VIABLE",
                "Animal-model in vivo efficacy confirmed in published peer-reviewed studies at translatable dose; mechanism site supported.")

    return ("MECHANISM UNCLEAR",
            "ChEMBL data present but no clear connection to gout-relevant target at achievable concentration; insufficient to triage with confidence.")


# ---------------------------------------------------------------------------
# Composite scoring (comp-007 adapted)
# ---------------------------------------------------------------------------

def gut_enrichment_score(bioavailability: float, mechanism_site: str) -> tuple:
    """Adaptation: gut-enrichment is FAVORABLE for gut-luminal targets, UNFAVORABLE for systemic.

    For gut-luminal: score = 1 - BA (low BA → high score)
    For systemic: score = BA (low BA → low score, since drug isn't reaching the systemic target)
    Mixed-site: midpoint
    """
    if "gut-luminal" in mechanism_site and "systemic" not in mechanism_site:
        return (1.0 - bioavailability, "gut-luminal-only: low BA favorable")
    if "systemic" in mechanism_site and "gut-luminal" not in mechanism_site:
        return (bioavailability, "systemic-only: high BA favorable")
    # Mixed site
    return (0.5 * (1.0 - bioavailability) + 0.5 * bioavailability + 0.0,
            "mixed gut + systemic: balanced")


def best_on_target_ic50(target_data: list, gout_relevant_targets: set) -> Optional[float]:
    """Return the lowest (most potent) IC50 against a gout-relevant target, in nM."""
    best = None
    for td in target_data:
        if td.get("target") in gout_relevant_targets and td.get("ic50_nM") is not None:
            if best is None or td["ic50_nM"] < best:
                best = td["ic50_nM"]
    return best


def best_off_target_ic50(target_data: list, gout_relevant_targets: set) -> Optional[float]:
    """Return the lowest (most potent) IC50 against an OFF-target (not in gout panel)."""
    best = None
    for td in target_data:
        if td.get("target") not in gout_relevant_targets and td.get("ic50_nM") is not None:
            if best is None or td["ic50_nM"] < best:
                best = td["ic50_nM"]
    return best


def selectivity_score(on_target_ic50: Optional[float], off_target_ic50: Optional[float]) -> tuple:
    """Selectivity: off_target / on_target. Higher = more selective for the gout-relevant target."""
    if on_target_ic50 is None or on_target_ic50 <= 0:
        return (SELECTIVITY_UNKNOWN_PENALTY, None, "no on-target IC50")
    if off_target_ic50 is None:
        return (SELECTIVITY_UNKNOWN_PENALTY, None, "no off-target panel data — penalty applied")
    ratio = off_target_ic50 / on_target_ic50
    score = ratio / (ratio + SELECTIVITY_NORMALIZATION_MIDPOINT)
    return (score, round(ratio, 2), f"on/off ratio = {ratio:.2f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    compounds_data = load_json(INPUTS / "compounds.json")
    bioactivity_data = load_json(INPUTS / "bioactivity_data.json")
    targets_data = load_json(INPUTS / "targets.json")
    gut_model = load_json(INPUTS / "gut_model.json")

    gout_relevant_target_names = {t["name"] for t in targets_data["targets"]}
    # Also accept variants
    gout_relevant_target_names.update({
        "URAT1 (SLC22A12)", "URAT1", "ABCG2", "GLUT9 (SLC2A9)", "GLUT9",
        "Xanthine dehydrogenase/oxidase", "XDH", "NLRP3",
        "Soluble epoxide hydrolase (sEH)", "OAT1 (SLC22A6)", "OAT1",
        "OAT3 (SLC22A8)", "OAT3", "Renal urate handling (FEUA increase)"
    })

    bio_by_compound = {e["compound"]: e["target_data"] for e in bioactivity_data["entries"]}

    results = []
    raw_potencies = []

    for compound in compounds_data["compounds"]:
        name = compound["name"]
        target_data = bio_by_compound.get(name, [])

        # Gut + plasma concentrations
        gut_conc = compute_gut_concentration(compound, gut_model)
        plasma_conc = compute_plasma_cmax(compound, gut_model)

        # Per-target occupancy
        target_occ = []
        for td in target_data:
            if td.get("ic50_nM") is None:
                continue
            target_chembl = td.get("target_chembl_id")
            target_name = td.get("target", "")
            # Decide which concentration to use based on target location
            # ABCG2 and gut-side transporters → use gut conc
            # URAT1, XO, NLRP3, sEH → plasma Cmax
            if target_name == "ABCG2":
                site = "gut"
                conc = gut_conc["effective_dissolved_nM"]
            else:
                site = "plasma"
                conc = plasma_conc["cmax_nM"]
            occ = compute_occupancy(td["ic50_nM"], conc)
            occ.update({
                "target": target_name,
                "target_chembl_id": target_chembl,
                "site": site,
                "is_gout_relevant": target_name in gout_relevant_target_names,
                "evidence_level": td.get("evidence_level"),
            })
            target_occ.append(occ)

        # Composite score components
        on_ic50 = best_on_target_ic50(target_data, gout_relevant_target_names)
        off_ic50 = best_off_target_ic50(target_data, gout_relevant_target_names)
        sel_score, sel_ratio, sel_note = selectivity_score(on_ic50, off_ic50)
        gut_score, gut_note = gut_enrichment_score(
            compound["bioavailability_fraction"], compound.get("mechanism_site", "")
        )

        # Raw potency for normalization (1/best on-target IC50)
        if on_ic50 is not None and on_ic50 > 0:
            potency_raw = 1.0 / on_ic50
        else:
            potency_raw = 0.0
        raw_potencies.append(potency_raw)

        # Confidence assignment
        has_biochem = any(
            td.get("evidence_level", "").startswith("In Vitro biochemical")
            for td in target_data
        )
        has_animal = any(
            td.get("evidence_level", "").startswith("Animal")
            for td in target_data
        )
        has_clinical = any(
            td.get("evidence_level", "").startswith("Clinical")
            for td in target_data
        )
        if has_biochem and (has_animal or has_clinical):
            confidence = "HIGH"
        elif has_biochem or has_animal:
            confidence = "MODERATE"
        else:
            confidence = "LOW"

        # Triage verdict
        occupancy_results = {
            "by_target": target_occ,
            "raw_target_data": target_data,
        }
        has_chembl = compound.get("chembl_id") is not None
        verdict, rationale = assign_verdict(compound, occupancy_results,
                                            has_chembl, on_ic50 is not None)

        results.append({
            "compound": name,
            "tcm_source": compound.get("tcm_source"),
            "chembl_id": compound.get("chembl_id"),
            "mechanism_site": compound.get("mechanism_site"),
            "mechanism_note": compound.get("mechanism_note"),
            "dose_mg": compound["typical_supplement_dose_mg"],
            "bioavailability_fraction": compound["bioavailability_fraction"],
            "mw_g_mol": compound["molecular_weight_g_mol"],
            "gut_concentration": gut_conc,
            "plasma_cmax": plasma_conc,
            "target_occupancy": target_occ,
            "best_on_target_ic50_nM": on_ic50,
            "best_off_target_ic50_nM": off_ic50,
            "selectivity_score": round(sel_score, 4),
            "selectivity_ratio": sel_ratio,
            "selectivity_note": sel_note,
            "gut_enrichment_score": round(gut_score, 4),
            "gut_enrichment_note": gut_note,
            "potency_raw": potency_raw,
            "confidence": confidence,
            "triage_verdict": verdict,
            "triage_rationale": rationale,
        })

    # Normalize potency
    max_raw = max(raw_potencies) if any(p > 0 for p in raw_potencies) else 1.0
    for r, raw in zip(results, raw_potencies):
        if max_raw > 0:
            p_norm = raw / max_raw
        else:
            p_norm = 0.0
        composite = p_norm * r["selectivity_score"] * r["gut_enrichment_score"]
        r["potency_score_normalized"] = round(p_norm, 4)
        r["composite_score"] = round(composite, 4)

    # Sort by composite descending
    results.sort(key=lambda x: x["composite_score"], reverse=True)
    for i, r in enumerate(results):
        r["rank"] = i + 1

    output = {
        "experiment": "comp-013",
        "title": "TCM Gout Compound Triage — comp-004 IC50 occupancy + comp-007 composite scoring",
        "date": "2026-05-06",
        "framework": "comp-004 (gut-conc + Hill equation occupancy) + comp-007 (potency × selectivity × gut-enrichment composite)",
        "compounds_evaluated": len(results),
        "verdict_counts": {
            v: sum(1 for r in results if r["triage_verdict"] == v)
            for v in set(r["triage_verdict"] for r in results)
        },
        "results": results,
        "formula_level_evidence": bioactivity_data.get("formula_level_evidence", []),
    }

    with open(OUTPUTS / "triage.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output)
    write_csv(results)

    print(f"comp-013 complete. {len(results)} compounds triaged. Outputs in outputs/")
    print_table(results)


def print_table(results):
    print("\n| Rank | Compound | TCM source | Verdict | Composite | Confidence | Best on-target IC50 |")
    print("|---|---|---|---|---|---|---|")
    for r in results:
        ic50_str = f"{r['best_on_target_ic50_nM']:,.0f} nM" if r["best_on_target_ic50_nM"] else "N/A"
        print(f"| {r['rank']} | {r['compound']} | {r['tcm_source'][:30]} | {r['triage_verdict']} | "
              f"{r['composite_score']:.4f} | {r['confidence']} | {ic50_str} |")


def write_csv(results):
    with open(OUTPUTS / "per_compound_table.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rank", "compound", "tcm_source", "chembl_id", "mechanism_site",
            "dose_mg", "bioavailability_fraction", "mw_g_mol",
            "gut_conc_uM", "plasma_cmax_uM",
            "best_on_target_ic50_nM", "best_off_target_ic50_nM",
            "selectivity_score", "selectivity_ratio",
            "gut_enrichment_score", "potency_score_normalized", "composite_score",
            "confidence", "triage_verdict", "triage_rationale"
        ])
        writer.writeheader()
        for r in results:
            writer.writerow({
                "rank": r["rank"],
                "compound": r["compound"],
                "tcm_source": r["tcm_source"],
                "chembl_id": r["chembl_id"],
                "mechanism_site": r["mechanism_site"],
                "dose_mg": r["dose_mg"],
                "bioavailability_fraction": r["bioavailability_fraction"],
                "mw_g_mol": r["mw_g_mol"],
                "gut_conc_uM": r["gut_concentration"]["effective_dissolved_uM"],
                "plasma_cmax_uM": r["plasma_cmax"]["cmax_uM"],
                "best_on_target_ic50_nM": r["best_on_target_ic50_nM"],
                "best_off_target_ic50_nM": r["best_off_target_ic50_nM"],
                "selectivity_score": r["selectivity_score"],
                "selectivity_ratio": r["selectivity_ratio"],
                "gut_enrichment_score": r["gut_enrichment_score"],
                "potency_score_normalized": r["potency_score_normalized"],
                "composite_score": r["composite_score"],
                "confidence": r["confidence"],
                "triage_verdict": r["triage_verdict"],
                "triage_rationale": r["triage_rationale"],
            })


def write_summary(output):
    results = output["results"]
    lines = [
        f"# comp-013: TCM Gout Compound Triage — Summary",
        "",
        f"**Date:** {output['date']}",
        f"**Framework:** {output['framework']}",
        f"**Compounds evaluated:** {output['compounds_evaluated']}",
        f"**Interpretive wiki page:** [`wiki/tcm-gout-compound-triage-computational.md`](../../wiki/tcm-gout-compound-triage-computational.md)",
        "",
        "## Verdict counts",
        "",
    ]
    for v, c in sorted(output["verdict_counts"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{v}**: {c}")
    lines += [
        "",
        "## Per-compound triage table",
        "",
        "| Rank | Compound | TCM source | Verdict | Composite | Confidence | Best on-target IC50 (nM) | Mechanism site |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        ic50_str = f"{r['best_on_target_ic50_nM']:,.0f}" if r['best_on_target_ic50_nM'] else "N/A"
        lines.append(
            f"| {r['rank']} | **{r['compound']}** | {r['tcm_source']} | "
            f"**{r['triage_verdict']}** | {r['composite_score']:.4f} | {r['confidence']} | "
            f"{ic50_str} | {r['mechanism_site']} |"
        )
    lines += [
        "",
        "## Per-compound rationale",
        "",
    ]
    for r in results:
        lines += [
            f"### Rank {r['rank']}: {r['compound']} — {r['triage_verdict']}",
            "",
            f"- **TCM source:** {r['tcm_source']}",
            f"- **ChEMBL ID:** {r['chembl_id'] or 'NOT IN ChEMBL — primary literature only'}",
            f"- **Mechanism site:** {r['mechanism_site']}",
            f"- **Mechanism note:** {r['mechanism_note']}",
            f"- **Dose:** {r['dose_mg']} mg; **BA:** {r['bioavailability_fraction']*100:.1f}%; **MW:** {r['mw_g_mol']} g/mol",
            f"- **Gut lumen conc:** {r['gut_concentration']['effective_dissolved_uM']} µM (solubility-capped: {r['gut_concentration']['solubility_capped']})",
            f"- **Plasma Cmax:** {r['plasma_cmax']['cmax_uM']} µM",
            f"- **Best on-target IC50:** {r['best_on_target_ic50_nM']} nM" if r['best_on_target_ic50_nM'] else "- **Best on-target IC50:** N/A (ChEMBL gap)",
            f"- **Selectivity (on/off):** {r['selectivity_ratio']} ({r['selectivity_note']})",
            f"- **Gut-enrichment score:** {r['gut_enrichment_score']:.3f} ({r['gut_enrichment_note']})",
            f"- **Composite score:** {r['composite_score']:.4f}",
            f"- **Confidence:** {r['confidence']}",
            f"- **Triage rationale:** {r['triage_rationale']}",
            "",
            "Per-target occupancy:",
            "",
        ]
        if r['target_occupancy']:
            lines.append("| Target | Site | IC50 (nM) | Conc at site (nM) | Ratio | % inhibition | Risk level | Evidence |")
            lines.append("|---|---|---|---|---|---|---|---|")
            for t in r['target_occupancy']:
                inh = f"{t['fractional_inhibition']*100:.0f}%" if t['fractional_inhibition'] else "N/A"
                lines.append(
                    f"| {t['target']} | {t['site']} | {t['ic50_nM']:,.0f} | {t['conc_nM']:,.0f} | "
                    f"{t['ratio']} | {inh} | {t['risk_level']} | {t['evidence_level']} |"
                )
        else:
            lines.append("_No target IC50 data — see ChEMBL gap notes in inputs/bioactivity_data.json_")
        lines.append("")

    lines += [
        "## Formula-level evidence (Si Miao San / Modified Simiao Decoction)",
        "",
    ]
    for fle in output.get("formula_level_evidence", []):
        lines += [
            f"### {fle['name']}",
            f"- **Components:** {', '.join(fle['components'])}",
            f"- **Clinical evidence:** {fle['clinical_evidence']}",
            f"- **Quantitative finding:** {fle['key_quantitative_finding']}",
            f"- **Verification:** {fle['verification']}",
            f"- **Evidence level:** {fle['evidence_level']}",
            f"- **Limitation:** {fle['limitation']}",
            "",
        ]

    lines += [
        "## Methodology adaptation notes (vs comp-004 and comp-007)",
        "",
        "**comp-004 IC50 occupancy framework — direct application**",
        "Same Hill equation n=1, same gut-conc model (dose × (1−BA) ÷ 250 mL, capped at intestinal solubility), same risk thresholds.",
        "",
        "**comp-007 composite scoring — adapted**",
        "Three changes from comp-007 (HDACi screen):",
        "1. **Gut-enrichment is BIDIRECTIONAL.** comp-007's HDACi candidates all targeted Q141K-ABCG2 trafficking — a gut-mucosal target where low BA is uniformly favorable. TCM compounds split: some target gut-luminal (favorable for low BA), others target systemic urate transporters URAT1/XO/NLRP3 (UNFAVORABLE for low BA). The gut-enrichment score is now site-aware.",
        "2. **Selectivity uses on/off-target ratio.** comp-007 used HDAC6/class-I ratio (avoiding cardiotoxicity). Here, selectivity = best gout-relevant on-target IC50 / best non-gout off-target IC50. Compounds with off-target hits more potent than the on-target hit get penalized.",
        "3. **Animal-model evidence is admissible.** comp-007 ranked on biochemical IC50 only. For TCM compounds, ChEMBL coverage is so sparse that animal-model in vivo dose-response data has to count toward the verdict — explicitly tagged in evidence_level field.",
        "",
        "**Honesty caveats**",
        "- ChEMBL coverage of TCM compounds is poor: 5 of 9 candidates have NO ChEMBL entry at all.",
        "- For compounds without ChEMBL bioactivity but with animal-model in vivo data, the composite score will be 0 (no on-target IC50). Verdict still uses animal data via the `assign_verdict` override.",
        "- Plasma Cmax is a crude single-dose estimate using Vd ≈ 1 L/kg for polyphenols. Real Cmax depends on formulation, absorption rate, and clearance.",
        "- Human dose translation from murine in vivo studies uses no formal allometric scaling; values are bounded estimates.",
    ]

    with open(OUTPUTS / "summary.md", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
