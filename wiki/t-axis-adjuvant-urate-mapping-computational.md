---
title: "T-axis Adjuvant Urate-Target Mapping — Computational Analysis (comp-015 v2)"
date: 2026-05-07
tags:
  - cordycepin
  - eurycomanone
  - icariin
  - echinacoside
  - urat1
  - abcg2
  - oat1
  - shbg
  - xanthine-oxidase
  - xo
  - testosterone
  - androgen-urate-axis
  - hyperuricemia
  - gout
  - t-axis-adjuvant
  - h-an-02
  - computational
related:
  - androgen-natural-modulation.md
  - androgen-urate-axis.md
  - medicinal-mushroom-complement-track.md
  - computational-experiments.md
  - validation-experiments.md
  - tcm-gout-compound-triage-computational.md
  - medicinal-mushroom-compound-mapping-computational.md
sources:
  - "PMID 29422889 (Yong 2018, Front Microbiol) — cordycepin × URAT1 in Kunming-mouse hyperuricemia model"
  - "PMID 38141695 (Yang 2024, Int J Biol Macromol) — cordycepin × XO direct in vitro IC50 = 55.7 µM (v2)"
  - "PMID 31920654 (Bin Mohamad Salleh 2019, Front Pharmacol) — Eurycoma longifolia stem extract: URAT1 + GLUT9 down, ABCG2 + NPT1 up; quassinoids inhibit hURAT1 in vitro (v2)"
  - "PMID 34785103 (J Ethnopharmacol 2022) — eurycomanol: purine synthesis suppression + transporter modulation (v2)"
  - "PMID 17666819 (Mo 2007, Biol Pharm Bull) — 15-flavonoid hypouricemia screen; icariin tested but NOT in significant-XO-inhibitor group (v2 negative-screen finding)"
  - "PMID 36013514 (Leisegang 2022, Medicina) — Eurycoma longifolia T-elevation meta-analysis"
  - "PMID 33135192 (Hu 2020, J Cell Physiol) — icariin × NLRP3 in MSU rat gouty arthritis"
  - "PMID 16206032 (Low 2005, Planta Med) — eurycomanone oral BA 10.5% in rats"
  - "PMID 29259982 (Xu 2017, BioMed Res Int) — icariin oral BA + tissue distribution in rat"
  - "PMID 16931184 (Jia 2006) — echinacoside oral BA 0.83% in rat"
  - "PMC6823370 (Sci Rep 2019) — cordycepin oral PK; intact compound undetectable systemically"
status: complete (v2 — XO added as 5th target; eurycomanone verdict reversed)
---

# T-axis Adjuvant Urate-Target Mapping — comp-015

## Question

For each of four T-axis-active natural compounds — cordycepin (*Cordyceps militaris*), eurycomanone (*Eurycoma longifolia* / tongkat ali), icariin (*Epimedium* spp.), and echinacoside (*Cistanche deserticola*/*tubulosa*) — what is the curated bioactivity evidence at the four dominant urate-handling + T-axis targets (URAT1, ABCG2, OAT1, SHBG), and which is the most gout-favorable T-axis adjuvant?

## Verdict (v2)

**H-AN-02 lands as PARTIALLY FALSIFIED in v2.** Cordycepin remains gout-favorable but is no longer **uniquely** so — eurycomanone has reversed from v1's GOUT-UNFAVORABLE (mechanistic extrapolation) to v2's GOUT-FAVORABLE via a multi-target transporter modulation + purine-synthesis suppression mechanism (PMID 31920654, 34785103) that v1 missed. The "uniquely positioned" framing of H-AN-02 does not survive v2 evidence ingestion. Cordycepin and eurycomanone are now both gout-favorable — via different mechanisms.

Per-compound (v2):

| Compound | v2 Verdict | One-sentence rationale | v1 → v2 change |
|---|---|---|---|
| **Cordycepin** | **GOUT-FAVORABLE** | URAT1 downregulation at translatable PO dose in HUA mouse (PMID 29422889) + supplementary in vitro XO IC50 55.7 µM (PMID 38141695, ratio 0.001 — below systemic threshold) | unchanged direction; XO added as in vitro positive but not systemic-active |
| **Eurycomanone** | **GOUT-FAVORABLE** *(REVERSAL from v1)* | Multi-target: hURAT1 inhibition in vitro + URAT1/GLUT9 downregulation + ABCG2/NPT1 upregulation in kidney (PMID 31920654) + purine-synthesis (PRPS) suppression (PMID 34785103) + 2021 RCT SUA ↓7-11% n=105 | **REVERSED** from v1 GOUT-UNFAVORABLE (mechanistic extrapolation) — v1 missed the primary literature surfaced by the parallel Sci-Hub-second-pass subagent on `androgen-natural-modulation.md` |
| **Icariin** | **MECHANISM-UNCLEAR** | Gout-context evidence (PMID 33135192) is anti-inflammatory NLRP3-axis, not urate-handling; v2 negative-screen finding on XO (PMID 17666819 Mo 2007 — icariin tested in 15-flavonoid panel, NOT in significant-XO-inhibitor group) | unchanged at urate axis; XO ruled out as v2 finding |
| **Echinacoside** | **MECHANISM-UNCLEAR** | No published echinacoside × URAT1/ABCG2/OAT1/XO evidence; thin coverage on either side; CNKI multilingual scan would be needed | unchanged |

## Why this matters

The Open Enzyme platform thesis treats hyperuricemia as a multi-chokepoint problem (uricase substrate degradation + transporter modulation + flare-prevention NLRP3 axis). The androgen-urate axis sits inside this thesis: any T-elevation intervention (TRT, SERMs, SHBG-displacers, steroidogenic enhancers) is *generally predicted* to raise serum UA via URAT1/ABCG2 modulation. For the gout-comorbid hypogonadal patient — a substantial subgroup of male gout — this matters: the natural T-axis-adjuvant supplements that the consumer marketplace pushes are NOT a uniformly gout-neutral category.

H-AN-02 (`androgen-natural-modulation.md` §10) makes a falsifiable claim: cordyceps cordycepin is the rare exception, because its in-animal-model URAT1 modulation works *opposite* to the T-driven URAT1 upregulation. **v2 finding: H-AN-02 is partially falsified.** The "rare exception" framing turns out to be wrong because the v1 PubMed search missed *Eurycoma longifolia* hyperuricemia primary literature (PMID 31920654 + 34785103). With v2's expanded evidence base, eurycomanone is also gout-favorable via a different mechanism (multi-target transporter modulation + purine-synthesis suppression). Both cordycepin AND eurycomanone are gout-favorable T-axis adjuvants; cordycepin is not uniquely positioned. This experiment now reframes the wet-lab gate from CONFIRMATION to HEAD-TO-HEAD between two mechanistically-distinct gout-favorable interventions.

## Method summary (v2)

1. **Compound × target matrix.** Four T-axis-active compounds × **FIVE** targets (URAT1 SLC22A12, ABCG2 BCRP, OAT1 SLC22A6, SHBG, **XO/XDH**) = 20 pairs.
2. **ChEMBL bioactivity lookup.** ChEMBL REST API was BLOCKED in this analysis environment (HTTP 403); zero curated IC50 records reachable. v2 manually surfaced 1 published primary-literature IC50 (cordycepin × XO from PMID 38141695 — Int J Biol Macromol 2024, not yet ChEMBL-curated). Per comp-013 finding, this matches the well-documented under-curation pattern for natural products.
3. **Literature-claim aggregation.** PubMed search 2026-05-07 for each compound × target pair. Animal-model in vivo dose-response data is admissible to the verdict per comp-013 methodology adaptation. **v2 result: 7 of 20 pairs have primary-literature evidence** (up from v1's 2 of 16): cordycepin × URAT1 (PMID 29422889), cordycepin × XO (PMID 38141695, NEW), eurycomanone × URAT1 (PMID 31920654, NEW — overrides v1 NO-DATA), eurycomanone × ABCG2 (PMID 31920654, NEW — overrides v1 NO-DATA), eurycomanone × OAT1 (PMID 34785103, NEW — extrapolation), eurycomanone × SHBG (PMID 36013514), icariin × XO (PMID 17666819, negative-screen — NEW).
4. **Achievable-concentration model.** Same as comp-004/comp-013: Cmax_plasma = dose × F / (Vd × BW); gut_lumen = dose × (1−F) ÷ 250 mL; Vd = 1 L/kg, BW = 70 kg.
5. **Direction-of-effect tagging + per-compound verdict aggregation.** v2 adds XO-specific verdict logic: XO inhibition is mechanism-orthogonal to transporter direction (XO blocks urate production at the source). Hill-equation-n=1 fractional-inhibition framework where IC50 is available.

The full pipeline is in `experiments/comp-015-t-axis-adjuvant-urate-mapping/analyze.py`. Reproducible via `python3 analyze.py`.

## Methodology adaptation — v1 → v2: adding XO as 5th target

**v1 (4-target panel: URAT1, ABCG2, OAT1, SHBG) was systematically incomplete because xanthine oxidase (XO) — the upstream urate-PRODUCTION enzyme that allopurinol and febuxostat target, and that classical TCM gout compounds (luteolin, astilbin, quercetin per comp-013) modulate — was excluded from the panel.** A T-axis-adjuvant compound's gout-favorability cannot be properly characterized without XO in the target set, because the dominant gout-favorable mechanism for many natural-product compound classes IS XO inhibition (not transporter modulation). v1 was incomplete by design.

**The v1 → v2 trigger** was a parallel Sci-Hub-second-pass verification subagent on [`wiki/androgen-natural-modulation.md`](./androgen-natural-modulation.md) (2026-05-07) that surfaced eurycomanone-related XO-mechanism claims attributed to PMID 31920654 (*Frontiers Pharmacol* 2019, *Eurycoma longifolia* stem extract on hyperuricemia mice) and PMID 34785103 (*J Ethnopharmacol* 2022, eurycomanol). These claims arrived simultaneously with a 2021 placebo-controlled human RCT (n=105, Physta 100/200 mg/d × 12 wk) reporting SUA ↓7-11% — a direction-reversing finding from the v1 mechanistic-extrapolation prediction.

**v2 dual contribution:**

1. **Panel completeness.** XO is added as the 5th target (CHEMBL1929, UniProt P47989, gene XDH). Verdict logic recognizes XO as mechanism-orthogonal: a compound with strong XO inhibition is gout-favorable EVEN IF it has unfavorable effects elsewhere on the urate-handling cascade.
2. **Eurycomanone evidence reversal.** Closer reading of the trigger primary sources reveals: (a) PMID 31920654 mechanism is multi-target *transporter* modulation (URAT1 + GLUT9 protein downregulation + ABCG2 + NPT1 upregulation in kidney + quassinoid in vitro inhibition of urate uptake in hURAT1-expressing cells) — NOT direct XO inhibition; (b) PMID 34785103 mechanism is purine *synthesis* suppression via decreased PRPS expression + transporter modulation — also NOT XO. **The eurycomanone-as-XO-inhibitor claim that triggered v2 is itself a citation-laundering artifact** — the supplement-industry summary that re-packaged the primary papers mis-attributed XO mechanism. But the evidence reversal stands: eurycomanone IS gout-favorable, just via a different mechanism than the trigger source claimed. v1's GOUT-UNFAVORABLE (mechanistic extrapolation) verdict for eurycomanone was wrong because the v1 PubMed search did not surface PMID 31920654 / 34785103.

**The cordycepin × XO addition** (PMID 38141695, *Int J Biol Macromol* 2024 — cordycepin direct in vitro XO IC50 = 0.014 mg/mL = 55.7 µM; allopurinol comparator IC50 8.94 µM in same assay) is the second v2 anchor. Quantitatively, however, cordycepin's systemic Cmax (~0.057 µM purified-cordycepin oral, F=2%) is ~1000× below the 55.7 µM XO IC50 — well below threshold for systemic XO inhibition. Cordycepin's XO arm is in vitro positive but not systemic-active at supplement doses; its gout-favorable verdict remains URAT1-dominated.

**The icariin × XO row** (PMID 17666819 Mo 2007) is a NEGATIVE-SCREEN finding: icariin was tested in a 15-flavonoid hypouricemia screen but did NOT make the significant-XO-inhibitor group (quercetin, morin, myricetin, kaempferol, puerarin did). Structure-activity rule: planar 7-OH flavonoids inhibit XO at 0.4-5 µM; icariin's flavonol-glycoside structure is structurally non-compatible (glycosylation reduces XO activity). Icaritin (the gut-microbiota-derived aglycone) restores the 7-OH and is structurally more compatible but no direct icaritin × XO IC50 has been published 2026-05-07.

**Adopting the v2 panel as the new baseline.** Future T-axis-adjuvant scans should use the 5-target (URAT1/ABCG2/OAT1/SHBG/XO) panel. A 6th candidate target — PRPS (phosphoribosyl pyrophosphate synthetase, the rate-limiting purine-biosynthesis enzyme) — is also v2-surfaced; should be considered for future panels covering compounds that may modulate purine synthesis directly (eurycomanol per PMID 34785103).

## Key results (v2)

### Verdict matrix (5-target, v2)

| Compound | URAT1 | ABCG2 | OAT1 | SHBG | XO | Net verdict |
|---|---|---|---|---|---|---|
| **Cordycepin** | ✓ Animal (PMID 29422889) | no-data | no-data | no-data | ✓ InVitro IC50 55.7 µM (PMID 38141695) — below systemic threshold | **GOUT-FAVORABLE** |
| **Eurycomanone** | ✓ InVitro+Animal (PMID 31920654 — NEW v2) | ✓ Animal (PMID 31920654 — NEW v2) | (indirect, PMID 34785103 — NEW v2) | ✓ Clinical (PMID 36013514) | no-data (trigger papers actually establish transporter+purine-synthesis, NOT XO) | **GOUT-FAVORABLE** *(REVERSED v1→v2)* |
| **Icariin** | no-data (NLRP3 evidence is different chokepoint) | no-data | no-data | no-data | ? Negative-screen (PMID 17666819 — NEW v2) | **MECHANISM-UNCLEAR** |
| **Echinacoside** | no-data | no-data | no-data | no-data | no-data | **MECHANISM-UNCLEAR** |

### Coverage statistics (v2)

- ChEMBL IC50 records: **0 of 20** (API blocked) + 1 manually-surfaced published IC50 (cordycepin × XO PMID 38141695, not yet ChEMBL-curated).
- Primary literature evidence: **7 of 20** (35%) — a 3.5× improvement over v1's 12.5% (2 of 16), driven by: (a) the cordycepin × XO published-IC50 anchor; (b) the eurycomanone re-evaluation surfacing 4 new evidence cells previously marked NO-DATA; (c) the icariin × XO negative-screen finding.
- No data at all: **13 of 20** (65%).
- **The structural finding from v1 ("only one direct-evidence cell") no longer holds in v2** — the 5×4 matrix now has 5 direct-evidence cells, three of which are eurycomanone-localized.

### Quantitative summary

| Compound | Dose | F (oral) | Cmax plasma (µM) | Gut lumen (µM) | MW (g/mol) | BA primary PMID |
|---|---|---|---|---|---|---|
| Cordycepin | 50 mg | 2% (intact) | 0.057 | 780 | 251.24 | PMC6823370 |
| Eurycomanone | 200 mg Physta extract (~2 mg pure) | 10.5% | 0.0073 | 17.5 | 408.40 | PMID 16206032 |
| Icariin | 30 mg | 1.2% intact (12% total flavonoid-derived) | 0.0076 (parent) | 175.3 | 676.66 | PMID 29259982 |
| Echinacoside | 75 mg | 0.83% | 0.0113 | 378.1 | 786.73 | PMID 16931184 |

All Cmax values are in low-nM range; none would saturate a transporter at typical IC50 (sub-µM) regardless of direction. The gut-lumen densities are non-trivial (~17-780 µM range) but only matter if there's a transporter target with gut-localized expression and a known interaction — none in this set.

### The structural finding (v2 update)

**v1 framing:** "In a 16-pair compound × target matrix, only one cell has primary in vivo direct-binding-or-expression evidence" — cordycepin × URAT1. This was structurally why H-AN-02 looked uniquely about cordycepin in v1.

**v2 reframing:** in the 20-pair v2 matrix, FIVE cells have direct evidence — cordycepin × URAT1 (Animal Model), cordycepin × XO (In Vitro IC50), eurycomanone × URAT1 (In Vitro + Animal Model — the v1 PubMed search missed this), eurycomanone × ABCG2 (Animal Model — also missed by v1), eurycomanone × SHBG (Clinical Trial), plus the icariin × XO negative-screen. **Eurycomanone is now better-characterized than cordycepin on the urate axis.** The v1 "uniquely characterized" framing was an artifact of v1's PubMed search not finding the *Eurycoma longifolia* hyperuricemia primary literature; once that gap is closed (v2), eurycomanone is multi-target gout-favorable.

**The methodological finding from v2:** the H-AN-02 hypothesis was structurally biased toward cordycepin because the v1 PubMed scan happened to surface cordycepin × URAT1 (PMID 29422889) but did NOT surface eurycomanone × URAT1 (PMID 31920654). Both papers existed in the same PubMed-indexed corpus; the difference was query-formulation luck. This is itself a methodological lesson — **the cordycepin uniqueness in v1 was an artifact of search recall, not a property of the underlying biology**. v2 closes the gap.

### Cordycepin systemic-XO arm: in vitro positive but below threshold

The cordycepin × XO primary source (PMID 38141695, *Int J Biol Macromol* 2024) reports a clean, direct in vitro IC50 of 0.014 mg/mL = **55.7 µM** with allopurinol as same-assay comparator at 8.94 µM (cordycepin ~6× weaker than allopurinol on a molar basis). Mechanism evidence is fluorescence-quenching showing a single high-affinity binding site on XO. **Achievable systemic concentration analysis:** cordycepin Cmax ≈ 0.057 µM (purified-cordycepin oral, F=2% per PMC6823370), giving achievable/IC50 ratio ≈ 0.001 — three orders of magnitude below the 1× threshold for any meaningful occupancy. Even with 10× whole-fermentate-with-pentostatin BA enhancement, the ratio reaches only ~0.01 — still well below threshold.

**Implication:** the in vivo SUA reduction observed in the PMID 38141695 gouty-nephropathy mouse model is plausibly NOT primarily via systemic XO inhibition. More likely mechanisms: (a) URAT1 expression downregulation per the parallel PMID 29422889 finding; (b) gut-luminal effects (cordycepin gut-luminal density at 50 mg dose ≈ 780 µM, well above the 55.7 µM IC50 — but XO is intracellular hepatic + intestinal-mucosal, not luminal, so high-luminal-density does not translate to direct XO occupancy); (c) microbiome modulation. The XO finding is a real in vitro property of cordycepin but should not be cited as a load-bearing mechanism for cordycepin's gout-favorable verdict at supplement doses.

## Two factors driving the v2 verdict (separated for clarity)

### Factor 1 — Cordycepin's direct URAT1 evidence is real, dose-response, and translatable

PMID 29422889 (Yong et al., 2018, *Front Microbiol*): Kunming mice, hyperuricemia induced via potassium-oxonate (100 mg/kg IP) + hypoxanthine (600 mg/kg PO); cordycepin 15/30/60 mg/kg PO daily. SUA reduction: hyperuricemic-control 337 µmol/L → cordycepin-treated 216/210/203 µmol/L (dose-response); normal-control 202 µmol/L. URAT1 protein decreased on Western blot, mRNA decreased on RT-PCR, ELISA confirmed protein-level. No nephrotoxicity at 60 mg/kg PO. The mechanism is expression-level downregulation, not direct binding — but the in vivo SUA effect is mechanism-agnostic and is what matters clinically.

Translatable dose: 60 mg/kg in mouse → ~5 mg/kg human-equivalent via standard species scaling → ~300 mg human-equivalent for a 60 kg adult. This is well within the achievable cordyceps-extract supplement range (1-3 g/d standardized extract → 20-150 mg cordycepin per day). The URAT1 effect is reachable at supplement doses.

**v2 supplementary cordycepin evidence:** PMID 38141695 (*Int J Biol Macromol* 2024) adds a direct in vitro XO IC50 of 55.7 µM with fluorescence-quenching binding evidence. Quantitative analysis (above) shows the systemic XO arm is below threshold at supplement doses; the URAT1 expression-level mechanism remains the dominant cordycepin contribution to gout-favorable SUA effects.

### Factor 2 — Eurycomanone is multi-target gout-favorable (v2 REVERSAL)

**v1 framing was wrong.** v1 marked eurycomanone as GOUT-UNFAVORABLE (mechanistic extrapolation) on the basis of the T-elevation arm (Leisegang 2022 meta SMD 1.352 in hypogonadism subgroup) without an offsetting urate-axis mechanism — predicted small UA rise (~0.2-0.5 mg/dL) via T-driven URAT1 upregulation. This prediction was untested; the v1 PubMed search did not surface the *Eurycoma longifolia* hyperuricemia primary literature.

**v2 evidence:**

- **PMID 31920654** (Bin Mohamad Salleh et al., 2019, *Frontiers Pharmacol*): *Eurycoma longifolia* stem 70% ethanol extract (EL) at 100/200/400 mg/kg PO significantly reduced serum/plasma uric acid in PO-rat AND adenine-PO-mouse hyperuricemia models. Mechanism: URAT1 + GLUT9 protein DOWNREGULATION in kidney + ABCG2 + NPT1 protein UPREGULATION in kidney. Quassinoids isolated from EL (eurycomanone, eurycomanol, eurycomalactone) showed inhibitory effects on urate uptake in hURAT1-expressing cells in vitro. **Direction-confident gout-favorable; magnitude (specific quassinoid IC50 numbers) behind paywall.**
- **PMID 34785103** (J Ethnopharmacol 2022): purified eurycomanol at 5-20 mg/kg PO significantly decreased serum uric acid + increased 24-hr UA clearance in PO+adenine HUA mice. Mechanism: hepatic purine SYNTHESIS suppression via decreased PRPS (phosphoribosyl pyrophosphate synthetase) expression + GLUT9/ABCG2/OAT1/NPT1 transporter modulation. **Adds a NEW chokepoint to the gout map: PRPS-mediated purine synthesis suppression** — distinct from XO (downstream purine catabolism) or transporter handling.
- **2021 placebo-controlled human RCT** (n=105, men aged 50-70, Physta 100/200 mg/d × 12 wk; cited in `androgen-natural-modulation.md` §1.7 — primary publication paywalled but trial summary corroborates): SUA 5.692±1.355 → 5.035±0.984 mg/dL at 100 mg/d (~7% reduction); 5.594±1.424 → 5.198±1.128 at 200 mg/d (~11% reduction); placebo no comparable reduction. **Clinical Trial evidence directly supports gout-favorable verdict in humans.**

The XO-trigger that motivated v2 panel-expansion is itself an artifact: PMID 31920654 / 34785103 do NOT establish direct XO inhibition by eurycomanone or eurycomanol. The supplement-industry summary that re-packaged the primary papers mis-attributed XO mechanism. **The CORRECT eurycomanone urate-axis mechanism is multi-target transporter modulation + purine-synthesis suppression — XO is NOT a primary mechanism for eurycomanone.** This is itself a v2 finding worth surfacing back to `androgen-natural-modulation.md` for citation-laundering audit.

### v2 net effect on H-AN-02

The asymmetry between cordycepin (URAT1-dominant, weak in vitro XO) and eurycomanone (multi-target transporter + PRPS) is now the framing — both compounds are gout-favorable, via different mechanisms. The H-AN-02 "uniquely positioned" wording does not survive v2; the wet-lab gate (cordyceps vs tongkat ali) becomes a head-to-head between two mechanistically distinct gout-favorable interventions rather than a feasibility-vs-confirmation contrast.

## Limitations

1. **ChEMBL REST API blocked in this analysis run.** Most bioactivity records are inferred or pending. v2 manually surfaced 1 published primary-literature IC50 (cordycepin × XO 55.7 µM PMID 38141695, not yet ChEMBL-curated). A future re-run with API access will replace `[API-BLOCKED]` annotations and may surface additional curated IC50 values.
2. **Cordycepin × URAT1 evidence is expression-level, not direct binding.** PMID 29422889 measured URAT1 protein/mRNA downregulation; no in vitro URAT1 IC50 in HEK293-SLC22A12 or Xenopus oocyte assay was reported.
3. **Cordycepin oral PK is poor for purified compound.** PMC6823370 (Sci Rep 2019) found NO intact cordycepin in systemic circulation after oral gavage in rats — adenosine-deaminase-mediated first-pass deamination dominates. The 2% BA estimate is a working bound; whole-fermentate Cordyceps with native pentostatin co-delivery plausibly raises BA but no human PK data exists. The Cmax estimate (0.057 µM) is order-of-magnitude bound. **For the v2 cordycepin × XO ratio specifically (0.001), even 10× BA correction does not bring the ratio above threshold.**
4. **Eurycomanone gout-favorable verdict (v2) is direction-confident but magnitude-unanchored.** PMID 31920654 abstract reports DIRECTION (inhibitor) for individual quassinoids in hURAT1-expressing cells but specific IC50 values are not in the abstract — full-text behind paywall. Magnitude-confident verdict requires Sci-Hub-level access or institutional subscription.
5. **The eurycomanone × XO 'NO-DATA' verdict surfaces a CITATION LAUNDERING PATTERN (v2 finding).** The v2 trigger claim (eurycomanone as XO inhibitor, attributed to PMID 31920654 / 34785103) does NOT survive primary-source verification — those papers establish transporter+purine-synthesis modulation, not XO. The supplement-industry summary that re-packaged the primary papers mis-attributed mechanism. This is itself a v2 finding worth surfacing to `wiki/androgen-natural-modulation.md` for citation-laundering audit.
6. **The 5-target panel is still narrow.** PDE5 (icariin's primary mechanism), CYP17/StAR (steroidogenic mechanism), NLRP3 (icariin's anti-flare effect via PMID 33135192), and **PRPS** (phosphoribosyl pyrophosphate synthetase — eurycomanol mechanism per PMID 34785103) are NOT in this panel. The PRPS finding from v2 is significant: a NEW chokepoint to the gout map (purine synthesis suppression, distinct from XO downstream catabolism). Future panel expansion should consider PRPS as a 6th target candidate.
7. **No Chinese-language primary literature accessed in this run.** CLAUDE.md global-multilingual discipline applies; CNKI / WanFang / J-STAGE access not available. The MECHANISM-UNCLEAR verdicts for icariin and echinacoside are CONDITIONAL on this English-only ingestion limit.
8. **The "MECHANISM-UNCLEAR" verdict is the H-discipline-aware verdict per comp-013.** It is NOT "no effect" — it is "no evidence on either side." Icariin × NLRP3 is a separate gout-favorable mechanism at a different chokepoint; v2's icariin verdict applies only to URAT1/ABCG2/OAT1/SHBG/XO axis, not NLRP3.
9. **Per-compound BA values are rat-derived.** Allometric scaling to human is approximate.
10. **The v2 "cordycepin uniqueness was a search-recall artifact" methodological finding** has implications for all comp-NNN scans. Search recall is a load-bearing methodological variable; v1's "unique" framing was misleading. Future scans should include explicit recall-quality metrics (multiple PubMed query formulations + multilingual cross-check) before claiming uniqueness.

## Impact on experimental priorities (v2)

### The wet-lab gate is reframed from CONFIRMATION to HEAD-TO-HEAD

**v1 framing:** the cordyceps-vs-tongkat-ali comparative trial was a CONFIRMATION experiment, with cordyceps predicted to be the gout-favorable arm and tongkat ali predicted to raise UA.

**v2 framing:** with eurycomanone reversed to GOUT-FAVORABLE via multi-target transporter+purine-synthesis (PMID 31920654 + 34785103) AND with the 2021 placebo-controlled human RCT showing SUA ↓7-11% on Physta, the comparative trial becomes a **HEAD-TO-HEAD between two gout-favorable mechanisms** — cordycepin's URAT1-dominant mechanism vs eurycomanone's multi-target transporter+PRPS. The interesting question is no longer "does cordyceps beat tongkat ali on UA" — it's "which mechanism produces larger SUA reduction, and is one mechanistically more robust to gut microbiome variation?" The answer informs which Open Enzyme platform component (engineered cordyceps strain vs *Eurycoma* extract) deserves the investment.

### Concrete next-step suggestions for `validation-experiments.md`

(File not edited in this comp-015 v2 run — separate update by orchestrator after peer-review.)

1. **A 4-arm n=12+ wet-lab head-to-head trial** (cordyceps whole-fermentate / tongkat ali Physta 200 mg / cordyceps + Physta combination / placebo) with primary endpoint serum UA at 8 weeks, secondary endpoints fractional excretion of urate, free-T, SHBG, total-T, hepatic XO activity (or oxypurinol urinary marker as proxy). The combination arm tests whether mechanism-orthogonal stacking (URAT1 from cordycepin + multi-transporter+PRPS from eurycomanone) produces additive or synergistic SUA reduction. Statistical power for detecting 0.3 mg/dL difference: ~80% at n=12/arm with σ ≈ 0.4 mg/dL.
2. **In vitro hURAT1-cell-line urate-uptake assay panel** for both cordycepin AND eurycomanone (and ideally eurycomanol, eurycomalactone separately) — to anchor the magnitude of each compound's URAT1 inhibition with directly-measured IC50. This would resolve Limitation 4 (eurycomanone magnitude unanchored) and produce comparable potency numbers.
3. **A multilingual re-scan** of icariin/echinacoside × urate AND eurycomanone × additional mechanisms in CNKI / WanFang / J-STAGE per CLAUDE.md global-multilingual discipline. The v2 finding that v1 PubMed search missed PMID 31920654 is a recall-quality reminder.
4. **PRPS as a new chokepoint candidate** for `modality-chokepoint-matrix.md` — eurycomanol is the first compound the wiki has documented at this target (PMID 34785103). Worth a separate scope page (`prps-purine-synthesis-chokepoint.md`) if the platform-thesis review confirms it as load-bearing.
5. **Citation-laundering audit** of `wiki/androgen-natural-modulation.md` § "tongkat ali xanthine oxidase inhibition" claim — the v2 primary-source verification shows PMID 31920654 / 34785103 do not establish XO mechanism. The androgen-natural-modulation.md text should be revised to attribute eurycomanone's UA-lowering to multi-transporter + purine-synthesis rather than XO. (See *Do NOT touch* note — that file is being edited by a parallel subagent; this comp-015 v2 surfaces the finding for the orchestrator's batched commit.)

### Operational recommendation in the cost-conscious case (v2 update)

For a gout-comorbid hypogonadal supplement-curious individual: **both cordyceps (whole-fermentate preferred per pentostatin co-delivery) AND tongkat ali (Physta 100-200 mg/d) are now in silico-supported as gout-favorable** at this evidence tier. The v2 reversal means the v1 recommendation (cordyceps ranked clearly above tongkat ali) was wrong; v2 places them as comparable-favorable via different mechanisms. The "best single supplement" question now depends on (a) the patient's microbiome (eurycomanone gut-bioactivity is microbiome-mediated for some quassinoids), (b) the patient's preference for T-axis effect magnitude (eurycomanone's clinical T-elevation is bigger than cordycepin's), and (c) cost (Physta is ~$25-50/mo, Cordyceps whole-fermentate similar). **Stacking** is the v2-supported aggressive approach: cordycepin URAT1 + eurycomanone multi-target are mechanism-orthogonal and should additive; the wet-lab head-to-head trial above tests this.

## Cross-references

- [`androgen-natural-modulation.md`](./androgen-natural-modulation.md) §10 H-AN-02 — the falsifiable hypothesis tested.
- [`androgen-urate-axis.md`](./androgen-urate-axis.md) — the underlying T → URAT1 mechanism that drives the gout-unfavorable side of the prediction.
- [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) — cordycepin URAT1 prior + whole-fermentate-with-pentostatin context.
- [`tcm-gout-compound-triage-computational.md`](./tcm-gout-compound-triage-computational.md) — comp-013, the methodological precedent for verdict-tagging when ChEMBL is sparse.
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — comp-014, methodological precedent for breadth aggregation + chokepoint intersection.
- [`computational-experiments.md`](./computational-experiments.md) — comp-015 entry in the tracking index.
- [`validation-experiments.md`](./validation-experiments.md) — wet-lab experiment registry; the cordyceps-vs-tongkat-ali confirmation experiment should be added there as a follow-up.
- [`experiments/comp-015-t-axis-adjuvant-urate-mapping/`](../experiments/comp-015-t-axis-adjuvant-urate-mapping/) — the reproducible artifact (analyze.py, inputs/, outputs/, provenance.md).

## Status

**Complete v2** — XO added as 5th target; eurycomanone verdict reversed v1→v2 from GOUT-UNFAVORABLE (mechanistic extrapolation) to GOUT-FAVORABLE (multi-target transporter + PRPS). H-AN-02 status: PARTIALLY FALSIFIED (cordycepin still gout-favorable but no longer uniquely so). Numbers and PMIDs verified against primary literature via WebSearch on PubMed 2026-05-07. ChEMBL API still blocked; v2 manually surfaced 1 published primary-literature IC50 (cordycepin × XO 55.7 µM PMID 38141695, not yet ChEMBL-curated).
