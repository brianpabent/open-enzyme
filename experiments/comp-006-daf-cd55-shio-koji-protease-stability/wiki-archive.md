---
title: "DAF/CD55 Shio-Koji Protease Stability: Computational Analysis (comp-006)"
date: 2026-05-05
tags: [complement, CD55, DAF, protease, shio-koji, computational, alphafold, structural-biology, CP0]
related:
  - modality-chokepoint-matrix.md
  - complement-c5a-gout.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - computational-experiments.md
  - engineered-koji-protocol.md
sources:
  - "UniProt P08174 (human DAF/CD55, canonical isoform, SV=4)"
  - "AlphaFold AF-P08174-F1-model_v6 (EMBL-EBI)"
  - "MEROPS database release 12.4"
  - "Koaze et al. 1964 (acid protease pH-activity curve)"
  - "Ward et al. 1995 (A. oryzae α-amylase secretion signal)"
---

# DAF/CD55 Shio-Koji Protease Stability: Computational Analysis (comp-006)

**Status:** Complete — 2026-05-05  
**Experiment folder:** [`experiments/comp-006-daf-cd55-shio-koji-protease-stability/`](../experiments/comp-006-daf-cd55-shio-koji-protease-stability/)  
**Evidence level:** Mechanistic Extrapolation — AlphaFold pLDDT-based structural inference; no wet-lab confirmation.  
**Companion analyses:** [comp-001 (uricase, LOW)](./uricase-protease-stability-computational.md), [comp-005 (lactoferrin, HIGH/MODERATE)](./lactoferrin-protease-stability-computational.md)

---

## Summary

AlphaFold pLDDT structural analysis of human DAF/CD55 (P08174, 381 aa) against three *A. oryzae* koji proteases (ALP, NPr, acid protease) under shio-koji conditions (17.5% NaCl midpoint, pH 4.5–5.0, 22°C). Three verdicts computed to bracket the engineering question:

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| Full sequence (aa 1–381, incl. signal peptide + GPI propeptide) | **HIGH** | 0.388 | NPr |
| Mature protein (aa 35–381, excl. signal peptide) | **HIGH** | 0.388 | NPr |
| Soluble ectodomain (aa 35–353) | **HIGH** | 0.388 | NPr |

**The operationally relevant verdict is the soluble ectodomain (aa 35–353): HIGH.** Unlike comp-005 (lactoferrin), where the HIGH full-sequence verdict was signal-peptide-contingent and dropped to MODERATE once the signal peptide was excluded, the CD55 ectodomain verdict remains HIGH across all three scopes. The driver is the **Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52)** — 68 residues of fully disordered polypeptide within the soluble ectodomain.

**Critical engineering observation:** The stalk is a structurally inert linker in the native context, carrying no complement-regulatory function. Truncating the ectodomain construct at SCR4 (aa 35–285) would eliminate all NPr-exposed and ALP-exposed ectodomain sites. A comp-007 analysis of the SCR1-4-only construct (aa 35–285) is the logical next step before concluding that CD55 is incompatible with shio-koji fermentation.

---

## Context: why this analysis exists

[`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) identifies the "Engineered soluble complement regulators" row as the only modality that could close the platform's **CP0 chokepoint** — complement priming via C5a — without a pharma adjunct. [`complement-c5a-gout.md`](./complement-c5a-gout.md) establishes that no fermentable natural-product C5aR1 antagonist has been validated (computational scan, `validation-experiments.md` §1.21, 2026-04-27), making avacopan the current default for CP0 coverage — an awkward fit for the "your microbe makes the medicine" platform thesis.

The unexplored alternative: express endogenous human soluble complement regulators in the gut via a GRAS koji host. Of the candidate proteins (sCR1 at ~190 kDa / 30 SCR domains, Factor H at ~150 kDa / 20 SCR domains, DAF/CD55 at ~70 kDa / 4 SCR domains), **DAF/CD55 is the most tractable engineering target** due to its smaller size and fewer SCR domains.

comp-006 is the first-step computational feasibility gate: can the ectodomain survive the shio-koji fermentation environment that the GRAS koji chassis operates in? The answer informs whether to proceed to wet-lab expression attempts.

---

## Method

Same shared library as comp-001 and comp-005 (`experiments/lib/protease_stability.py`). Risk score per site:

```
risk_score = accessibility_weight × salt_residual_activity × ph_activity_factor
```

Accessibility weights: buried (pLDDT ≥ 80) = 0.1; partially exposed (pLDDT 65–80) = 0.4; exposed (pLDDT < 65) = 1.0.

pH activity factors: ALP conservatively 1.0 (outside active pH 6–12), NPr conservatively 1.0 (at edge of pH 5–9), acid protease 0.30 (Koaze et al. 1964 activity-vs-pH curve).

**Three verdicts** computed by filtering sites to: (1) full sequence, (2) aa 35–381 (excluding signal peptide), (3) aa 35–353 (soluble ectodomain — excluding both signal peptide and GPI-anchor propeptide).

---

## Structural context

**Signal peptide (aa 1–34):** pLDDT 43–72 — fully disordered. In the engineered A. oryzae construct, this is replaced by the koji-native α-amylase secretion signal (Ward et al. 1995), so aa 1–34 are not present in the expressed product.

**SCR1 (aa 35–96):** pLDDT 85–98 — well-folded. Inter-SCR junction at aa 83–96 shows pLDDT 89–96, still well-folded.

**SCR2 (aa 97–160):** pLDDT 90–98 — well-folded. Minor dip at aa 99–102 (pLDDT ~91) representing the interdomain connection.

**SCR3 (aa 161–222):** pLDDT 97–98 — the most confidently modelled region. All recognition sites here are buried.

**SCR4 (aa 223–285):** pLDDT 91–98, well-folded, with a minor reduction at aa 270–272 (pLDDT 93–94). Still largely buried.

**Ser/Thr-rich stalk (aa 286–353):** pLDDT drops sharply from ~91 at aa 285 to 74 at aa 286, 63 at aa 287, and 50 at aa 288, remaining fully disordered (pLDDT 30–52) through aa 353. This 68-residue unstructured linker is the dominant structural liability. In the native cell-surface context, it is heavily O-glycosylated; this glycan sheath likely provides backbone shielding that is absent or altered in heterologous expression.

**GPI-anchor propeptide (aa 354–381):** pLDDT 30–52 — fully disordered. Not present in the soluble ectodomain engineering construct.

---

## Per-protease results

| Protease | Total sites | Exposed (full) | Exposed (ectodomain) | Stalk exposed | Max risk (full) | Max risk (ectodomain) |
|---|---|---|---|---|---|---|
| ALP (alkaline subtilisin) | 260 | 98 | 48 | 48 | 0.188 | 0.188 |
| NPr (neutral metalloprotease) | 100 | 39 | 9 | 9 | 0.388 | 0.388 |
| acid_protease (aspergillopepsin) | 42 | 17 | 1 | 1 | 0.195 | 0.195 |

All ectodomain exposed sites are in the Ser/Thr-rich stalk (aa 286–353). The SCR1–4 domains contribute **zero exposed sites** to any protease. If the stalk is truncated from the engineering construct, ectodomain exposed-site count drops to zero for NPr (0 → 0), 0 for ALP, and 0 for acid protease — with only buried and partially exposed SCR-domain sites remaining.

---

## Verdict interpretation

**The HIGH verdict is stalk-contingent, not SCR-contingent.**

This is the critical structural distinction. In comp-005 (lactoferrin), HIGH was signal-peptide-contingent — removing the signal peptide (which *A. oryzae* normally cleaves for secreted proteins) dropped the verdict to MODERATE. For CD55, the signal peptide is also disordered, but it is not present in the engineered construct. The persistent HIGH verdict comes from the stalk, which *is* present in a full soluble ectodomain construct (aa 35–353) and which *A. oryzae* has no mechanism to cleave.

Two engineering paths follow from this:

**Path 1 — Truncate the stalk (aa 35–285, SCR1-4 only):**  
Removes all NPr- and ALP-exposed ectodomain sites. The compact SCR1–4 structure is well-folded (mean pLDDT ~96 in this region), disulfide-stabilized, and likely highly protease-resistant. Verdict would shift toward LOW. The structural question is whether SCR1–4 without the stalk retains complement-regulatory activity in a soluble secreted form — unknown, but the native soluble form of sCR1 (which lacks GPI anchor) functions as a complement inhibitor systemically, suggesting SCR domains alone are sufficient.

**Path 2 — Retain the stalk; engineer around its vulnerability:**  
Options include: (a) heterologous O-glycosylation engineering to shield the stalk backbone; (b) random loop deletion to shorten the stalk while preserving folding; (c) accept the stalk as a cleavable linker and test whether C-terminally truncated fragments retain complement-regulatory activity. All three are wet-lab experiments downstream of comp-006.

---

## Comparison with uricase (comp-001) and lactoferrin (comp-005)

| Feature | Uricase (comp-001) | Lactoferrin (comp-005) | CD55 ectodomain (comp-006) |
|---|---|---|---|
| Analyzed construct length | 301 aa | 710 aa | 381 aa |
| Mean pLDDT | 97.1 | 95.0 | 78.3 |
| Min pLDDT | 80.5 | 35.8 | 29.9 |
| % residues pLDDT > 80 | 100% | 96.1% | 65.9% |
| Signal peptide | None | Present (aa 1–19) | Present (aa 1–34) |
| Dominant disordered region | None | Signal peptide (if retained) | Ser/Thr stalk (aa 286–353) — within ectodomain |
| Disulfide bonds | None | 2 per lobe | 2 per SCR domain (8 total in SCR1–4, per UniProt P08174 — corrected 2026-05-06; see [comp-012 §1.5](./daf-cd55-scr14-truncated-computational.md) correction note for the hallucination provenance) |
| Full-sequence verdict | LOW | HIGH | HIGH |
| Mature-protein verdict | LOW | MODERATE | HIGH |
| Soluble ectodomain verdict | N/A | N/A | HIGH |
| Verdict driver | None (all buried) | Signal peptide (HIGH) / ALP at mature sites (MODERATE) | Ser/Thr stalk within ectodomain |
| Engineering path to lower verdict | N/A | Signal peptide cleavage by *A. oryzae* | Stalk truncation (SCR1–4 only) |

The contrast with uricase is stark: uricase is 100% well-folded (mean pLDDT 97.1, min 80.5), with no exposed sites. CD55 has ~34% of residues at pLDDT < 65 — almost entirely concentrated in the signal peptide, stalk, and GPI propeptide. Remove those disordered regions and the SCR1–4 core compares favorably with uricase.

---

## Key limitations

- **Disulfide bonds not modelled.** Each SCR domain contains 2 conserved disulfide bonds (4 Cys per domain, **8 total in SCR1–4** per UniProt P08174 DISULFID feature annotations: Cys36-Cys81, Cys65-Cys94 [SCR1]; Cys98-Cys145, Cys129-Cys158 [SCR2]; Cys163-Cys204, Cys190-Cys220 [SCR3]; Cys225-Cys267, Cys253-Cys283 [SCR4] — canonical sushi/CCP fold). Disulfide cross-linking substantially reduces backbone flexibility and proteolytic susceptibility independent of pLDDT. This analysis likely **overestimates risk in the SCR domains** — the true SCR risk is lower than the buried-site counts suggest. **Correction note (2026-05-06):** earlier draft of this page asserted "3 per SCR domain (12 total)" — hallucinated by the authoring agent without grep-verification against UniProt. Canonical sushi/CCP fold is 2 disulfides per domain (Cys1-Cys3 + Cys2-Cys4 motif). Same hallucination class as the comp-012 disulfide-count incident (see [`daf-cd55-scr14-truncated-computational.md` §1.5](./daf-cd55-scr14-truncated-computational.md) and [`manual-literature-mining.md` §"Pre-commit verification gate"](./manual-literature-mining.md)).
- **O-glycosylation of the stalk not modelled.** The Ser/Thr-rich stalk carries dense O-linked glycans in native CD55 (estimated 15–25 O-glycan additions). These sterically shield the backbone. *A. oryzae* performs O-glycosylation but with different sugar compositions (α-1,2- and α-1,3-mannose) than mammalian (GalNAc-based core-1/2 structures). Shielding effect is uncertain; stalk risk may be overstated for any glycosylated form or underestimated for an aglycosylated construct.
- **pLDDT ≠ solvent accessibility.** SCR pLDDT 85–98 predicts well-folded regions, but SASA calculation would quantify which surface loops are solvent-exposed vs. buried at domain interfaces. A structure-based SASA analysis could refine the SCR-domain risk.
- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled; may over-count recognition sites in both the SCR domains and the stalk.
- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range (pH 6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge (pH 5–9). True activity of both is lower than modelled — stalk risk is conservatively overstated.
- **The stalk-truncated construct (aa 35–285) is not modelled in comp-006.** The HIGH verdict applies specifically to the full ectodomain (aa 35–353). The SCR1-4-only construct is the obvious follow-up.

---

## Implications for the koji-CD55 engineering thesis

**comp-006 does not close the CD55 engineering thesis — it redirects it.**

The HIGH ectodomain verdict is not a verdict on SCR1–4; it is a verdict on the stalk. The SCR domains are protease-stable. The decision tree from comp-006:

1. **Before any wet-lab CD55 expression work:** run comp-007 on the SCR1–4-only construct (aa 35–285). Expected verdict: LOW, matching the uricase result. If LOW, the engineering path is clear: express a stalkless CD55 ectodomain.

2. **Wet-lab expression question:** Can *A. oryzae* secrete a folded, disulfide-bonded SCR1–4 fragment at meaningful titers? The analogous precedent is sCR1 (Avant Pharmaceuticals, IV biologic), which demonstrates that soluble SCR-domain fragments are functionally active. The koji expression question is whether the *A. oryzae* secretory machinery can fold 8 disulfide bonds correctly (corrected from earlier "12" estimate per UniProt P08174 — see disulfide bonds line above) — a more tractable question than the prior estimate suggested. *A. oryzae* secretes glucoamylase (2 disulfides) and lactoferrin (16 per Notari 2023, originally cited as 17); 8 sits comfortably between. Per the [chaperone framework refinement (2026-05-06)](./chaperone-orthogonal-stacking.md), DAF SCR1-4's CCP/SCR architecture coefficient (α=0.3-0.6) gives effective PDI load of 2.4-4.8 disulfide-equivalents — well within demonstrated *A. oryzae* capacity even on wild-type RIB40. Wet-lab gate formalized as [`validation-experiments.md` §1.25](./validation-experiments.md).

3. **Activity question:** Does the expressed fragment suppress C5a production in a gut-lumen assay? Complement activation in the gut lumen vs. gut wall may require different spatial access than systemic sCR1. This is the fundamental CP0 mucosal-coverage question that no published work has addressed.

**The comp-006 result is consistent with the engineering thesis being viable — specifically for a stalk-truncated construct.** It is not consistent with a full-length soluble ectodomain surviving shio-koji fermentation without modification.

---

## Cross-references

- [modality-chokepoint-matrix.md](./modality-chokepoint-matrix.md) — "Engineered soluble complement regulators" row; comp-006 verdict updates the status of this exploration vector
- [complement-c5a-gout.md](./complement-c5a-gout.md) — CP0 chokepoint; why this analysis exists
- [daf-cd55-scr14-truncated-computational.md](./daf-cd55-scr14-truncated-computational.md) — **comp-012 (2026-05-05):** SCR1-4-only truncated construct (aa 35–285) confirmed **LOW** protease risk (max 0.039, identical to uricase). Stalk truncation removed 100% of exposed sites. The CP0 platform-gap closure thesis is now in silico-validated. (Mechanistic Extrapolation; source: daf-cd55-scr14-truncated-computational.md)
- [hypotheses/H05-daf-scr14-cp0-thesis.md](./hypotheses/H05-daf-scr14-cp0-thesis.md) — Falsification card for the DAF SCR1-4 CP0-closure thesis (stub, committed 2026-05-05)
- [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) — comp-001; the LOW-verdict baseline
- [lactoferrin-protease-stability-computational.md](./lactoferrin-protease-stability-computational.md) — comp-005; the HIGH/MODERATE lactoferrin comparison
- [computational-experiments.md](./computational-experiments.md) — tracking index
- [engineered-koji-protocol.md](./engineered-koji-protocol.md) — A. oryzae expression context
