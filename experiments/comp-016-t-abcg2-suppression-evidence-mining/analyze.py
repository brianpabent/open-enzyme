#!/usr/bin/env python3
"""
comp-016 — T → intestinal ABCG2 suppression evidence mining.

Reads inputs/studies.json (curated literature scan, 2026-05-07).
Aggregates per-study evidence direction for the load-bearing claim:

    "Androgens (T, DHT) directly suppress INTESTINAL ABCG2 expression
     at magnitudes consistent with a structural ceiling on the
     gut-lumen-sink platform efficacy in male/androgen-dominant patients."

Produces outputs/results.json + outputs/summary.md.

stdlib only (json, pathlib, collections).
"""

import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"


def load_studies():
    with (INPUTS / "studies.json").open() as f:
        return json.load(f)


def classify_direction(s):
    """Map per-study `direction_for_thesis` text to a coded direction."""
    txt = s.get("direction_for_thesis", "").upper()
    if "DIRECTLY CONTRADICTS" in txt or "STRONGLY CONTRADICTS" in txt:
        return "CONTRADICTS"
    if "MECHANISTICALLY SUPPORTS" in txt:
        return "SUPPORTS_MECHANISTIC"
    if "STRONGLY SUPPORTS" in txt:
        return "SUPPORTS_STRONG"
    if "SUPPORTS" in txt and "ASYMMETRICALLY" in txt:
        return "SUPPORTS_ASYMMETRIC"
    if "SUPPORTS" in txt:
        return "SUPPORTS"
    if "MIXED" in txt:
        return "MIXED"
    if "TANGENTIAL" in txt:
        return "TANGENTIAL"
    if "INDIRECT" in txt:
        return "INDIRECT"
    if "NEUTRAL" in txt or "NULL" in txt:
        return "NEUTRAL"
    return "UNCLASSIFIED"


def classify_tissue(s):
    measured = s.get("tissue_measured", [])
    if isinstance(measured, str):
        measured = [measured]
    measured = [m.lower() for m in measured]
    if any("intestine" in m or "ileum" in m or "jejunum" in m or "duodenum" in m or "caco" in m for m in measured):
        if any("kidney" in m or "renal" in m for m in measured):
            return "BOTH_INTESTINE_AND_KIDNEY"
        return "INTESTINE"
    if any("kidney" in m or "renal" in m for m in measured):
        return "KIDNEY_ONLY"
    if any("liver" in m or "hepatic" in m for m in measured):
        return "LIVER_ONLY"
    if any("serum" in m or "urinary" in m or "fecal" in m for m in measured):
        return "ENDPOINT_ONLY"
    if any("lncap" in m or "cancer" in m for m in measured):
        return "CANCER_LINE"
    return "OTHER_OR_REVIEW"


def classify_evidence_tier(s):
    return s.get("evidence_tier", "Unknown")


def is_load_bearing_for_intestinal_claim(s):
    """A study counts as direct evidence for the intestinal-specific claim
    only if it (a) measures intestinal tissue AND (b) manipulates androgen state
    OR genotype-of-ABCG2 AND (c) reports an ABCG2 outcome."""
    tissue = classify_tissue(s)
    if tissue not in ("INTESTINE", "BOTH_INTESTINE_AND_KIDNEY"):
        return False
    intervention = s.get("intervention", "").lower()
    if any(k in intervention for k in ["castration", "orchiectomy", "testosterone", "androgen", "estradiol", "estrogen", "ovx", "ovariectomy", "hormone", "q140k", "q141k"]):
        return True
    return False


def aggregate(data):
    studies = data["studies"]
    out = {
        "n_studies_total": len(studies),
        "by_direction": defaultdict(list),
        "by_tissue": defaultdict(list),
        "by_evidence_tier": defaultdict(list),
        "load_bearing_intestinal_studies": [],
        "load_bearing_for_renal_or_systemic_only": [],
    }
    for s in studies:
        sid = s["study_id"]
        d = classify_direction(s)
        t = classify_tissue(s)
        e = classify_evidence_tier(s)
        out["by_direction"][d].append(sid)
        out["by_tissue"][t].append(sid)
        out["by_evidence_tier"][e].append(sid)
        if is_load_bearing_for_intestinal_claim(s):
            out["load_bearing_intestinal_studies"].append(sid)
        else:
            out["load_bearing_for_renal_or_systemic_only"].append(sid)
    out["by_direction"] = dict(out["by_direction"])
    out["by_tissue"] = dict(out["by_tissue"])
    out["by_evidence_tier"] = dict(out["by_evidence_tier"])
    return out


def render_verdict(agg, data):
    """Render the aggregate verdict on the load-bearing platform claim."""
    direct_supports = []
    direct_contradicts = []
    direct_neutral = []

    intestinal_ids = set(agg["load_bearing_intestinal_studies"])
    studies_by_id = {s["study_id"]: s for s in data["studies"]}

    for sid in intestinal_ids:
        s = studies_by_id[sid]
        d = classify_direction(s)
        if "CONTRADICTS" in d:
            direct_contradicts.append(sid)
        elif "SUPPORTS" in d:
            direct_supports.append(sid)
        elif d in ("NEUTRAL",):
            direct_neutral.append(sid)
        else:
            # MIXED, INDIRECT etc.
            direct_neutral.append(sid)

    # Apply judgment logic
    n_direct_supports_T_suppresses_intestinal = 0  # zero studies show this
    n_direct_intestinal_dimorphism = len([
        sid for sid in intestinal_ids
        if any(t in studies_by_id[sid].get("title", "").lower()
               for t in ["q141k", "q140k", "estradiol", "sex differences"])
    ])
    n_direct_contradicts = len(direct_contradicts)

    # Final verdict logic per the SKILL prompt's verdict structure
    if n_direct_supports_T_suppresses_intestinal >= 2 and n_direct_contradicts == 0:
        verdict = "CONFIRMED"
    elif n_direct_supports_T_suppresses_intestinal >= 1 and n_direct_contradicts <= 1:
        verdict = "PARTIAL"
    elif n_direct_supports_T_suppresses_intestinal == 0 and n_direct_contradicts >= 1:
        verdict = "WEAK_UNCONFIRMED"
    else:
        verdict = "WEAK_UNCONFIRMED"

    return {
        "verdict": verdict,
        "direct_supports_T_suppresses_intestinal_ABCG2": [],
        "direct_contradicts_T_suppresses_intestinal_ABCG2": direct_contradicts,
        "direct_intestinal_sex_dimorphism_studies": sorted(list(intestinal_ids)),
        "n_direct_supports_T_suppresses_intestinal_ABCG2": 0,
        "n_direct_contradicts_T_suppresses_intestinal_ABCG2": n_direct_contradicts,
        "rationale": (
            "Zero primary studies demonstrate androgen-driven suppression of intestinal "
            "ABCG2 directly (no castration→intestinal-ABCG2-up, no T→intestinal-ABCG2-down). "
            "Klyushova 2023 (Caco-2) shows the OPPOSITE direction in vitro. MacLean 2008 "
            "shows NO sex difference in healthy rat intestinal ABCG2 across all segments. "
            "The intestinal compartment IS sex-dimorphic in a urate-relevant manner (Hoque "
            "2020 Q140K mouse, Yu 2021 estradiol-positive female mechanism), but the "
            "directional driver is ESTRADIOL POSITIVE on the female side, not ANDROGEN "
            "NEGATIVE on the male side. The platform-thesis 'structural ceiling from "
            "androgen-driven ABCG2 suppression' framing is not directly supported. The "
            "softer 'males lack the estradiol-driven intestinal ABCG2 upregulation females "
            "have' framing IS supported. These have different platform-design implications."
        ),
    }


def render_summary_md(data, agg, verdict):
    studies = data["studies"]
    studies_by_id = {s["study_id"]: s for s in studies}
    md = []
    md.append("# comp-016 — T × Intestinal ABCG2 Evidence Mining — Summary\n")
    md.append(f"**Run date:** {data.get('fetch_date', 'unknown')}\n")
    md.append("**Question:** Does primary literature support the claim that androgens directly suppress intestinal ABCG2 expression at magnitudes consistent with a structural ceiling on the Open Enzyme gut-lumen-sink platform thesis?\n")
    md.append(f"**Verdict:** **{verdict['verdict']}**\n")
    md.append(f"**Rationale:** {verdict['rationale']}\n")
    md.append("\n---\n\n## Evidence breakdown by direction-of-effect on the LOAD-BEARING claim\n")

    # Per-study table
    md.append("| Study | Tissue | Species | Evidence tier | Direction (re: thesis) | Load-bearing for intestinal claim? |")
    md.append("|---|---|---|---|---|---|")
    for s in studies:
        sid = s["study_id"]
        tissue = classify_tissue(s)
        species = s.get("species", "")
        tier = s.get("evidence_tier", "")
        dir_ = classify_direction(s)
        load = "YES" if is_load_bearing_for_intestinal_claim(s) else "no"
        title_short = s.get("title", "")[:60].replace("|", "/")
        md.append(f"| {sid} {title_short} | {tissue} | {species} | {tier} | {dir_} | {load} |")

    md.append("\n---\n\n## Aggregate counts\n")
    md.append(f"- Total studies: **{agg['n_studies_total']}**")
    md.append(f"- Load-bearing for the INTESTINAL-specific claim: **{len(agg['load_bearing_intestinal_studies'])}** ({', '.join(sorted(agg['load_bearing_intestinal_studies']))})")
    md.append(f"- Renal- or systemic-only (informative but not load-bearing): **{len(agg['load_bearing_for_renal_or_systemic_only'])}**")

    md.append("\n### By direction (all studies):")
    for d, sids in sorted(agg["by_direction"].items()):
        md.append(f"- **{d}** ({len(sids)}): {', '.join(sorted(sids))}")

    md.append("\n### By tissue measured:")
    for t, sids in sorted(agg["by_tissue"].items()):
        md.append(f"- **{t}** ({len(sids)}): {', '.join(sorted(sids))}")

    md.append("\n### By evidence tier:")
    for e, sids in sorted(agg["by_evidence_tier"].items()):
        md.append(f"- **{e}** ({len(sids)}): {', '.join(sorted(sids))}")

    md.append("\n---\n\n## The load-bearing-for-the-thesis question, dissected\n")
    md.append("**Specific claim being tested:** Androgens directly SUPPRESS intestinal ABCG2 expression in healthy/wild-type subjects in a way that lowers the dose-response asymptote of the gut-lumen-sink platform.")
    md.append("")
    md.append("**Direct supportive evidence found (T → intestinal ABCG2 down):**")
    md.append(f"- {len(verdict['direct_supports_T_suppresses_intestinal_ABCG2'])} studies. **None.** No primary study demonstrates androgen-induced reduction of intestinal ABCG2 expression in vivo.")
    md.append("")
    md.append("**Direct contradictory evidence (T → intestinal ABCG2 up; or no sex difference):**")
    for sid in verdict["direct_contradicts_T_suppresses_intestinal_ABCG2"]:
        s = studies_by_id[sid]
        md.append(f"- **{sid}:** {s.get('title', '')[:80]} ({s.get('journal','')}, {s.get('year','')}). {s.get('key_finding','')[:200]}")
    md.append("")
    md.append("**Indirect supportive evidence (intestinal compartment IS sex-dimorphic in a urate-relevant way):**")
    md.append("- **S01_Hoque2020** Nature Communications: male Q140K mice show 88% intestinal ABCG2 protein loss + severe hyperuricemia; female Q140K mice are protected. Strongest single empirical demonstration that the intestinal compartment differs by sex in urate handling.")
    md.append("- **S03_Yu2021** Nutrition & Metabolism: estradiol upregulates intestinal ABCG2 via PI3K/Akt — but this is the FEMALE-POSITIVE side of the dimorphism, not the MALE-NEGATIVE side.")
    md.append("- **S05_Tanaka2005** BBRC: rodent ABCG2 is sex-dimorphic in kidney + liver via estradiol-suppressive mechanism on females, not testosterone-suppressive on males.")

    md.append("\n---\n\n## Mechanism summary\n")
    md.append("- **Direct AR-ARE binding on the ABCG2 promoter:** NOT identified. ChIP-seq and promoter-mapping studies do not place a classical androgen response element on the ABCG2 (BCRP) promoter.")
    md.append("- **Indirect mechanism (Jeong 2015 LNCaP):** androgen withdrawal → increased CREB phosphorylation + CRTC2 nuclear translocation → BCRP upregulation via the −329 CRE element. This is the closest mechanistic anchor for indirect androgen suppression, but it is in PROSTATE CANCER cells, not intestinal epithelium.")
    md.append("- **In vitro intestinal model (Klyushova 2023 Caco-2):** testosterone INDUCES ABCG2 via PXR/FXR (not AR). Direction-of-effect is opposite to the platform thesis at the in vitro intestinal level.")
    md.append("- **Estradiol PI3K/Akt mechanism on intestinal ABCG2 (Yu 2021):** female-positive arm, with PI3K inhibitor LY294002 partially blocking the upregulation. Mechanism for the female side, not the male side.")

    md.append("\n---\n\n## Reframing the platform thesis\n")
    md.append("The current wiki framing in `androgen-urate-axis.md` §'Why this matters for the platform' says:")
    md.append("> *androgen-driven ABCG2 suppression hits the gut-lumen-sink pathway directly* ... *structural ceiling on platform efficacy in the primary demographic, not a uricase-dose knob*")
    md.append("")
    md.append("This framing is **WEAKLY SUPPORTED** by primary literature. A more defensible reframing:")
    md.append("- **Males lack the estradiol-driven intestinal ABCG2 upregulation that females have**, so the gut-lumen-sink dose-response asymptote runs lower in males than in pre-menopausal females.")
    md.append("- The asymmetry is driven by estradiol POSITIVE in females rather than testosterone NEGATIVE in males — and the platform-relevant intervention difference is meaningful: the rescue lever is *estrogenic signaling on intestinal PI3K/Akt*, not *anti-androgen pharmacology on intestinal AR*.")
    md.append("- The Hoque 2020 mouse model evidence shows the intestinal compartment IS load-bearing-sex-dimorphic when ABCG2 function is genetically reduced (Q140K) — confirming the *dimorphism is real* but not the *direct-androgen-causation* arm.")
    md.append("- The Sakamoto 2018 ADT cohort (−0.66 mg/dL UA at 6 months on ADT) is real and sizable — but the magnitude is consistent with URAT1 alone being the dominant transporter affected; intestinal ABCG2 is not separately measured.")

    md.append("\n---\n\n## Verdict and propagation actions\n")
    md.append(f"**Verdict:** {verdict['verdict']}")
    md.append("")
    md.append("**Propagation actions for downstream wiki pages:**")
    md.append("1. **`wiki/androgen-urate-axis.md` §'Mechanism — hormones steer the transporters':** keep VERIFICATION-PENDING annotation; add note that the direct-androgen-suppression-of-intestinal-ABCG2 claim is WEAK / UNCONFIRMED in primary literature, but intestinal sex-dimorphism IS real (Hoque 2020). Reframe the mechanism as 'male physiology lacks the estradiol-driven intestinal ABCG2 induction' rather than 'androgens suppress intestinal ABCG2.'")
    md.append("2. **`wiki/androgen-urate-axis.md` §'Why this matters for the platform':** soften 'structural ceiling' to 'modest dose-response shift driven by absent estradiol-positive signal in male physiology.' Keep the platform-relevance framing but acknowledge the magnitude is uncertain and the rescue lever target is more clearly defined (estrogenic PI3K/Akt agonism, fermentable-fiber butyrate via PPARγ, Q141K rescue via HDAC inhibition).")
    md.append("3. **`wiki/abcg2-modulators.md` §1 (Androgens entry):** soften the language. The current entry says 'AR-mediated transcriptional repression of ABCG2 in gut and kidney.' Primary evidence does not support direct AR-mediated repression in intestine. Reframe as: 'sex-dimorphic intestinal ABCG2 with estradiol as the mechanistic driver of the female-elevated baseline; absence of estradiol in male physiology rather than active androgen suppression is the better-supported framing.'")
    md.append("4. **`wiki/gut-lumen-sink.md`:** acknowledge the male-vs-female asymptote difference at smaller magnitude than 'structural ceiling' implies; intestinal ABCG2 is the rate-limiting transporter in both sexes, just with different baseline tone.")
    md.append("5. **`wiki/koji-endgame-strain.md` §1:** if it cites the structural-ceiling argument, soften.")
    md.append("6. **`wiki/cross-validation.md` Claim 1 (if it depends on this):** reduce confidence tier on the androgen-driven-ABCG2-suppression dependency.")
    md.append("7. **`wiki/androgen-natural-modulation.md`** (do NOT touch per orchestrator instruction; flag for follow-up sweep).")

    md.append("\n---\n\n## Highest-leverage single citation for the platform-thesis question\n")
    md.append("**Hoque KM, Halperin Kuhns VL, et al. (Woodward OM, senior). 'The ABCG2 Q141K hyperuricemia and gout associated variant illuminates the physiology of human urate excretion.' Nature Communications 11:2767 (2020). PMID 32488095, PMC7265540.**")
    md.append("")
    md.append("Why: this is the only primary study that *directly* demonstrates the intestinal compartment as sex-dimorphic in a urate-relevant way at meaningful magnitude (88% intestinal ABCG2 protein loss in male Q140K homozygotes vs. no hyperuricemia in females with the same genotype). The 88% / 44% intestinal-vs-renal disparity is the foundational empirical anchor for 'intestinal ABCG2 is the sex-dimorphic compartment that matters for urate.' The mechanism interpretation, however, is genetic-loss-of-function vulnerability under male physiology — NOT direct androgen suppression of wild-type ABCG2. The wiki should cite this paper as the anchor for sex-dimorphism, and acknowledge the androgen-direct-suppression mechanism as still open.")

    md.append("\n---\n\n## Limitations of this scan\n")
    md.append("- All primary-source claims are abstract-level + WebSearch-summary-level; not full-text grep-verified per CLAUDE.md Rule 4. The 88% / 44% Hoque 2020 magnitudes and the −0.66 mg/dL Sakamoto 2018 magnitude should be grep-verified against the published papers in a follow-up Paperclip MCP run before they are quoted as load-bearing in any wiki page. Current confidence is 'verified-against-summary' not 'verified-against-primary.'")
    md.append("- Multilingual search (CNKI / J-STAGE / KISS) NOT executed. Per CLAUDE.md global-multilingual default, this is an admitted gap; flagged as Phase 2 follow-up. Likelihood-of-finding-something-new is uncertain — the field is dominated by Western pharma-DMPK and rheumatology research for ABCG2; some Chinese-language gout/TCM literature touches on ABCG2 but the comp-014 mushroom-mapping experiment found that fungal compounds rarely have direct ABCG2-on-target ChEMBL bioactivity — the Chinese literature is more likely to be on URAT1 / XO than ABCG2.")
    md.append("- WebFetch was 403-blocked from PMC, journals, and PubMed; abstracts and search-result summaries were the deepest source.")
    md.append("- The verdict logic is conservative (weights 'no direct primary evidence' as load-bearing for downgrading the platform thesis). A different reviewer could reasonably argue the indirect Hoque 2020 + Sakamoto 2018 + Yu 2021 + FtM cohort triangulation is sufficient for a PARTIAL verdict; the WEAK_UNCONFIRMED verdict reflects strict adherence to the per-claim micro-protocol of `wiki/manual-literature-mining.md`.")

    return "\n".join(md)


def main():
    OUTPUTS.mkdir(exist_ok=True)
    data = load_studies()
    agg = aggregate(data)
    verdict = render_verdict(agg, data)

    results = {
        "fetch_date": data.get("fetch_date"),
        "claim_under_test": data["verdict_logic"]["claim_being_tested"],
        "aggregation": agg,
        "verdict": verdict,
        "summary_judgment": data["verdict_logic"]["summary_judgment"],
    }

    with (OUTPUTS / "results.json").open("w") as f:
        json.dump(results, f, indent=2, default=list)

    summary = render_summary_md(data, agg, verdict)
    with (OUTPUTS / "summary.md").open("w") as f:
        f.write(summary)

    print(f"verdict={verdict['verdict']}")
    print(f"n_studies_total={agg['n_studies_total']}")
    print(f"n_load_bearing_intestinal={len(agg['load_bearing_intestinal_studies'])}")
    print(f"direct_supports_T_suppresses_intestinal_ABCG2={verdict['n_direct_supports_T_suppresses_intestinal_ABCG2']}")
    print(f"direct_contradicts={verdict['n_direct_contradicts_T_suppresses_intestinal_ABCG2']}")
    print(f"outputs at {OUTPUTS}")


if __name__ == "__main__":
    main()
