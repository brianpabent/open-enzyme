#!/usr/bin/env python3
"""
comp-004: Supplement ABCG2 Antagonism Risk Assessment

Pharmacological IC50 occupancy framework evaluating whether dietary polyphenol supplements
(quercetin, EGCG, curcumin) reach gut-lumen concentrations sufficient to inhibit ABCG2-mediated
urate efflux from blood into gut. ABCG2 accounts for ~33% of gut urate secretion; its inhibition
could elevate serum urate in gout-susceptible patients.

Relevant to: validation-experiments.md §1.14 (Caco-2 urate flux + supplement antagonism arms)

Run: python3 analyze.py
Outputs: outputs/risk_assessment.json, outputs/summary.md
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

# Risk ratio thresholds (ratio = [compound]_gut / IC50_ABCG2)
# Based on Hill equation n=1: fractional_inhibition = ratio / (ratio + 1)
# 0.5x IC50 → 33% inhibition; 1x → 50%; 2x → 67%; 5x → 83%; 10x → 91%
THRESHOLD_LOW = 0.5
THRESHOLD_MODERATE = 2.0
THRESHOLD_HIGH = 5.0
# >= HIGH threshold → VERY_HIGH (>83% predicted inhibition)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def classify_risk(ratio):
    if ratio is None:
        return "NOT_APPLICABLE"
    if ratio < THRESHOLD_LOW:
        return "LOW"
    if ratio < THRESHOLD_MODERATE:
        return "MODERATE"
    if ratio < THRESHOLD_HIGH:
        return "HIGH"
    return "VERY_HIGH"


def fractional_inhibition(ratio):
    """Hill equation, n=1: f = ratio / (ratio + 1)"""
    if ratio is None:
        return None
    return ratio / (ratio + 1.0)


def compute_gut_concentration(compound, gut_model):
    """
    Two-step gut-lumen dissolved concentration model.

    Step 1 — Dose-limited: fraction of dose remaining in gut lumen after absorption.
    Step 2 — Solubility-limited: cap at intestinal solubility.
    Effective = min(dose-limited, solubility cap).

    Unit derivation for nM conversion:
      mg/L × 1e6 / (g/mol) = nmol/L = nM
      (because mg/g = 1e-3, mol/nmol = 1e-9, ratio = 1e6)
    """
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
        "effective_dissolved_uM": round(effective_nM / 1000, 1),
        "effective_dissolved_nM": round(effective_nM, 0),
    }


def main():
    compounds_data = load_json(INPUTS / "compounds.json")
    ic50_raw = load_json(INPUTS / "ic50_data.json")
    gut_model = load_json(INPUTS / "gut_model.json")

    ic50_by_compound = {entry["compound"]: entry for entry in ic50_raw["ic50_data"]}

    results = []
    for compound in compounds_data["compounds"]:
        name = compound["name"]
        ic50_entry = ic50_by_compound[name]

        conc = compute_gut_concentration(compound, gut_model)

        ic50_nM = ic50_entry.get("ic50_nM")
        mechanism = ic50_entry["mechanism"]

        if ic50_nM is not None and mechanism == "direct_transport_inhibition":
            risk_ratio = conc["effective_dissolved_nM"] / ic50_nM
            frac_inh = fractional_inhibition(risk_ratio)
            risk_level = classify_risk(risk_ratio)
        else:
            risk_ratio = None
            frac_inh = None
            risk_level = "NOT_APPLICABLE"

        results.append({
            "compound": name,
            "chembl_id": compound["chembl_id"],
            "dose_mg": compound["typical_supplement_dose_mg"],
            "bioavailability_fraction": compound["bioavailability_fraction"],
            "mw_g_mol": compound["molecular_weight_g_mol"],
            "intestinal_solubility_mg_L": compound["intestinal_solubility_mg_L"],
            "gut_lumen_concentration": conc,
            "ic50_nM": ic50_nM,
            "mechanism": mechanism,
            "risk_ratio": round(risk_ratio, 2) if risk_ratio is not None else None,
            "predicted_fractional_inhibition": round(frac_inh, 3) if frac_inh is not None else None,
            "risk_level": risk_level,
            "assay_type": ic50_entry.get("assay_type"),
            "source": ic50_entry.get("source_citation"),
            "data_note": ic50_entry.get("notes", ""),
            "mechanism_note": ic50_entry.get("mechanism_detail") or compound.get("mechanism_note", ""),
        })

    output = {
        "experiment": "comp-004",
        "title": "Supplement ABCG2 Antagonism — Pharmacological Risk Assessment",
        "target": ic50_raw["target"],
        "gut_model_parameters": gut_model,
        "risk_thresholds": {
            "LOW": f"risk_ratio < {THRESHOLD_LOW} (< 33% predicted inhibition)",
            "MODERATE": f"{THRESHOLD_LOW} <= risk_ratio < {THRESHOLD_MODERATE} (33-67% predicted inhibition)",
            "HIGH": f"{THRESHOLD_MODERATE} <= risk_ratio < {THRESHOLD_HIGH} (67-83% predicted inhibition)",
            "VERY_HIGH": f"risk_ratio >= {THRESHOLD_HIGH} (> 83% predicted inhibition)",
            "NOT_APPLICABLE": "Expression-regulation mechanism; IC50 occupancy framework not applicable",
        },
        "results": results,
    }

    with open(OUTPUTS / "risk_assessment.json", "w") as f:
        json.dump(output, f, indent=2)

    write_summary(output)
    print("comp-004 complete. Outputs written to outputs/")
    print_table(results)


def print_table(results):
    print("\n| Compound | Dose (mg) | Gut conc (µM) | Solubility-capped | IC50 (nM) | Risk ratio | Pred. inhibition | Risk level |")
    print("|---|---|---|---|---|---|---|---|")
    for r in results:
        c = r["gut_lumen_concentration"]
        ic50_str = str(r["ic50_nM"]) if r["ic50_nM"] else "N/A"
        ratio_str = f"{r['risk_ratio']:.1f}x" if r["risk_ratio"] is not None else "N/A"
        inh_str = f"{r['predicted_fractional_inhibition']:.0%}" if r["predicted_fractional_inhibition"] is not None else "N/A"
        cap = "Yes" if c["solubility_capped"] else "No"
        print(f"| {r['compound']} | {r['dose_mg']} | {c['effective_dissolved_uM']} | {cap} | {ic50_str} | {ratio_str} | {inh_str} | **{r['risk_level']}** |")


def write_summary(output):
    results = output["results"]
    lines = [
        "# comp-004: Supplement ABCG2 Antagonism — Risk Assessment Summary",
        "",
        f"**Target:** {output['target']['name']} ({output['target']['chembl_id']})",
        f"**Function:** {output['target']['function']}",
        f"**Gut volume model:** {output['gut_model_parameters']['small_intestine_lumen_volume_L']} L (small intestine lumen, fasted estimate)",
        "",
        "## Risk ratio table",
        "",
        "Risk ratio = effective gut-lumen dissolved concentration ÷ ABCG2 IC50",
        "Predicted inhibition from Hill equation (n=1): ratio / (ratio + 1)",
        "",
        "| Compound | Dose (mg) | Gut conc (µM) | Solubility-capped? | IC50 (nM) | Risk ratio | Pred. inhibition | Risk level |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for r in results:
        c = r["gut_lumen_concentration"]
        ic50_str = str(r["ic50_nM"]) if r["ic50_nM"] else "N/A (expression mechanism)"
        ratio_str = f"{r['risk_ratio']:.1f}×" if r["risk_ratio"] is not None else "N/A"
        inh_str = f"{r['predicted_fractional_inhibition']:.0%}" if r["predicted_fractional_inhibition"] is not None else "N/A"
        cap = "Yes" if c["solubility_capped"] else "No"
        lines.append(
            f"| {r['compound']} | {r['dose_mg']} | {c['effective_dissolved_uM']} | {cap} | {ic50_str} | {ratio_str} | {inh_str} | **{r['risk_level']}** |"
        )

    lines += ["", "## Per-compound breakdown", ""]

    for r in results:
        c = r["gut_lumen_concentration"]
        lines += [
            f"### {r['compound']} ({r['chembl_id']})",
            f"- Dose: {r['dose_mg']} mg | Bioavailability: {r['bioavailability_fraction']*100:.0f}% | MW: {r['mw_g_mol']} g/mol",
            f"- Gut mass (unabsorbed): {c['gut_mass_mg']} mg",
            f"- Dose-limited concentration: {c['dose_limited_mg_L']} mg/L",
            f"- Intestinal solubility: {r['intestinal_solubility_mg_L']} mg/L",
            f"- Solubility cap applied: {'Yes → effective concentration = ' + str(r['intestinal_solubility_mg_L']) + ' mg/L' if c['solubility_capped'] else 'No → dose-limited'}",
            f"- Effective dissolved: **{c['effective_dissolved_uM']} µM** ({c['effective_dissolved_nM']:.0f} nM)",
            f"- ABCG2 IC50: {r['ic50_nM']} nM | Assay: {r['assay_type'] or 'N/A (expression mechanism)'}",
            f"- Risk ratio: {r['risk_ratio']}× | Predicted inhibition: {r['predicted_fractional_inhibition']:.0%}" if r["risk_ratio"] is not None else "- Risk ratio: N/A | Framework not applicable",
            f"- **Risk level: {r['risk_level']}**",
        ]
        if r["mechanism_note"]:
            lines.append(f"- Mechanism: {r['mechanism_note']}")
        if r["data_note"]:
            lines.append(f"- Data note: {r['data_note']}")
        lines += [
            f"- IC50 source: {r['source']}",
            "",
        ]

    lines += [
        "## Key findings",
        "",
        "**Curcumin is the highest-risk compound** despite being perceived as systemically safe.",
        "Its extreme insolubility (< 1% bioavailability) concentrates effectively all oral dose in the",
        "gut lumen, where it reaches the solubility ceiling at ~13.6 µM — 8.3× its ABCG2 IC50 (1630 nM).",
        "Predicted inhibition: ~89% of maximal ABCG2 activity.",
        "",
        "**Quercetin** is moderately-to-highly risk at standard 500 mg doses. Gut-lumen concentration",
        "is solubility-limited at ~49.6 µM, which is ~6.8× its ABCG2 IC50 (7250 nM).",
        "Predicted inhibition: ~87% of maximal ABCG2 activity.",
        "",
        "**EGCG** cannot be scored by this framework. Its ABCG2 modulation is transcriptional",
        "(mRNA/protein downregulation over 24-72h), not acute transport inhibition.",
        "The §1.14 48h transwell assay would miss this mechanism; a 72h arm with Western blot is needed.",
        "",
        "## Impact on §1.14 experimental framing",
        "",
        "Before comp-004: supplement arms in §1.14 were purely screening for whether an effect exists.",
        "After comp-004: IC50 occupancy strongly predicts substantial inhibition for quercetin and curcumin.",
        "§1.14 supplement arms now test a pharmacologically-predicted effect — the question shifts from",
        "'is there an effect?' to 'how large is it and does it match predictions?' The IC50 translation",
        "uncertainties (cell line vs. enterocyte, substrate dependence, self-aggregation) mean the Caco-2",
        "arm remains genuinely informative rather than a foregone conclusion.",
        "",
        "The strategic implication: gout patients taking curcumin or quercetin supplements may",
        "paradoxically worsen their condition by inhibiting gut ABCG2-mediated urate excretion,",
        "even if these compounds have anti-inflammatory effects on other pathways.",
        "",
        "## Limitations",
        "",
        "- Solubility values are estimates; actual intestinal solubility varies with meal fat content,",
        "  bile salt concentration, and supplement formulation (phospholipid complexes, nanoparticles,",
        "  piperine co-administration). Enhanced-bioavailability curcumin formulations (Meriva, BCM-95)",
        "  increase intestinal solubility 5-20×, potentially raising curcumin risk ratio to 40-160×.",
        "- IC50 values from cancer cell lines (MCF7, MCF7-VP) overexpressing ABCG2 at 10-100× enterocyte",
        "  levels. Substrate-to-transporter stoichiometry affects apparent IC50; functional inhibition in",
        "  primary enterocytes may differ quantitatively from cell-line data.",
        "- Substrate-dependent IC50: quercetin IC50 was measured with Hoechst 33342; curcumin with",
        "  mitoxantrone. Both are high-affinity ABCG2 substrates. ABCG2 displays substrate-dependent",
        "  inhibitor binding — IC50 against urate transport specifically may differ; urate is a",
        "  lower-affinity physiological substrate handled via a different binding mode.",
        "- Quercetin self-aggregation: quercetin forms colloidal aggregates above ~10 µM in aqueous",
        "  solution. Effective free monomeric concentration may be lower than the 49.6 µM nominal gut",
        "  concentration — aggregates may not inhibit ABCG2 and can produce artifactual inhibition in",
        "  cell-based assays. True free inhibitor concentration is uncertain.",
        "- Single-dose reporting: one representative supplement dose used per compound. At 1-3 g",
        "  quercetin (commercially available), risk ratio is identical (solubility-capped). For curcumin,",
        "  enhanced-solubility formulations are the variable to watch, not dose.",
        "- Gut volume model (250 mL whole SI) overestimates dilution relative to the proximal",
        "  small intestine where ABCG2 is most expressed — concentrations in duodenum/jejunum",
        "  may be 2-3× higher than reported, pushing risk ratios further into VERY_HIGH.",
        "- Hill equation n=1 assumes simple 1:1 competitive inhibition. ABCG2 inhibitor",
        "  mechanisms vary (ATP hydrolysis interference, substrate competition, conformational locking);",
        "  true dose-response curves may be steeper (n > 1) or shallower.",
        "- Q141K (rs2231142) amplified risk subgroup: Q141K carriers have ~50% reduced ABCG2 surface",
        "  expression at baseline, reducing gut urate secretion capacity before any supplement exposure.",
        "  Pharmacological inhibition on top of genetically-reduced ABCG2 drives total gut urate",
        "  excretion toward zero — this is an amplified-risk subgroup, not just a variant of interest.",
        "  ~27% of East Asian-ancestry individuals carry this variant.",
        "- EGCG cannot be assessed by this framework; a 72h treatment arm with ABCG2 Western blot",
        "  is needed in §1.14 to detect expression-level changes.",
        "- Transit dynamics not modelled: peak concentration window in proximal SI may be",
        "  shorter than total transit time, limiting total exposure.",
    ]

    with open(OUTPUTS / "summary.md", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
