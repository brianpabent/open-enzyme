---
title: "DAF/CD55 SCR1-4 Truncated Construct: Shio-Koji Protease Stability (comp-012)"
date: 2026-05-05
tags: [complement, CD55, DAF, protease, shio-koji, computational, alphafold, structural-biology, CP0, SCR]
related:
  - daf-cd55-protease-stability-computational.md
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

# DAF/CD55 SCR1-4 Truncated Construct: Shio-Koji Protease Stability (comp-012)

**Status:** Complete — 2026-05-05  
**Experiment folder:** [`experiments/comp-012-daf-cd55-scr14-truncated/`](../experiments/comp-012-daf-cd55-scr14-truncated/)  
**Evidence level:** Mechanistic Extrapolation — AlphaFold pLDDT-based structural inference; no wet-lab confirmation.  
**Predecessor:** [comp-006 — full ectodomain (aa 35–353): HIGH](./daf-cd55-protease-stability-computational.md)  
**Companion analyses:** [comp-001 (uricase, LOW)](./uricase-protease-stability-computational.md), [comp-005 (lactoferrin, HIGH/MODERATE)](./lactoferrin-protease-stability-computational.md)

---

## Summary

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| comp-006: Full ectodomain (aa 35–353, SCR1-4 + Ser/Thr stalk) | **HIGH** | 0.388 | NPr |
| comp-012: SCR1-4 only (aa 35–285, stalk removed) | **LOW** | 0.039 | NPr |

**The SCR1-4-only construct (aa 35–285) is protease-stable under shio-koji conditions: LOW verdict, max risk score 0.039.** This is a 10-fold drop from the comp-006 full ectodomain result (HIGH, 0.388), driven entirely by removing the Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52). After truncation, zero exposed sites remain across all three A. oryzae proteases. All 242 recognition sites in the SCR1-4 construct are buried (pLDDT ≥ 80).

**Platform implication:** This closes the computational feasibility gate for the koji-CD55 engineering thesis. The SCR1-4-only construct is the first computationally validated complement regulator candidate compatible with shio-koji fermentation. Whether it provides meaningful CP0 coverage (C5a reduction in a gut-lumen assay) remains an open wet-lab question — but the protease stability objection is resolved.

---

## Context: this experiment completes the comp-006 decision tree

[comp-006](./daf-cd55-protease-stability-computational.md) found the full DAF/CD55 ectodomain (aa 35–353) is HIGH protease risk. The driver was unambiguous: the Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52) contributed 9 NPr-exposed sites, 48 ALP-exposed sites, and 1 acid_protease exposed site — all within 68 disordered residues. The SCR1–4 domains (aa 35–285, pLDDT 85–98) contributed zero exposed sites. comp-006's own Limitations section identified the stalk-truncated construct as the logical follow-up; the 2026-05-05 sweep formalized this into a wet-lab proposal. comp-012 runs the in silico verdict before any wet-lab resources are committed.

The platform context: [`complement-c5a-gout.md`](./complement-c5a-gout.md) establishes the CP0 chokepoint — complement priming via C5a is the only node in the gout-modulation framework with zero fermentable coverage. Avacopan (a small-molecule C5aR1 antagonist) is the current default, which is awkward for the "your microbe makes the medicine" thesis. DAF/CD55 expressed via koji is the leading candidate for closing this gap, but only if the ectodomain survives shio-koji fermentation.

---

## Method

Identical shared library to comp-001, comp-005, comp-006 (`experiments/lib/protease_stability.py`). Risk score per site:

```
risk_score = accessibility_weight × salt_residual_activity × ph_activity_factor
```

Accessibility weights: buried (pLDDT ≥ 80) = 0.1; partially exposed (pLDDT 65–80) = 0.4; exposed (pLDDT < 65) = 1.0.

**Truncation:** The full P08174 sequence (381 aa) and pLDDT dict (381 entries) are loaded, then subset to aa 35–285 (251 residues, 251 pLDDT values) in Python before passing to library functions. The library sees only the 251-residue SCR1-4 window. Position indices in the analysis are 1-indexed relative to the subsetted sequence; the summary table back-maps each site to its full-sequence coordinate for readability.

**Single verdict:** comp-006 computed three scopes (full sequence, mature protein, soluble ectodomain). comp-012 computes one scope — the SCR1-4 construct — which is the only engineering-relevant variant being tested.

---

## Structural context

**SCR1 (aa 35–96):** pLDDT 85–98 — well-folded. Three conserved disulfide bonds (6 Cys). Inter-SCR junction at aa 83–96 remains well-folded (pLDDT 89–96).

**SCR2 (aa 97–160):** pLDDT 90–98 — well-folded. Minor dip at aa 99–102 (~91) at the interdomain connection.

**SCR3 (aa 161–222):** pLDDT 97–98 — the most confidently modelled region. All recognition sites buried.

**SCR4 (aa 223–285):** pLDDT 91–98 — well-folded, with a minor reduction at aa 270–272 (~93–94). Terminates at aa 285; the disordered stalk begins at aa 286 (pLDDT drops to 74 at aa 286, 63 at aa 287, 50 at aa 288).

**Stalk (aa 286–353) — excluded:** Fully disordered (pLDDT 30–52). This was the entirety of the protease risk in comp-006. Not present in this construct.

**Summary statistics (SCR1-4 only, 251 aa):** mean pLDDT 96.7, min pLDDT 85.6, 100% residues pLDDT > 80, 98.8% pLDDT > 90.

---

## Per-protease results

| Protease | Sites in SCR1-4 | Buried | Partially exposed | Exposed | Max risk score |
|---|---|---|---|---|---|
| ALP (alkaline subtilisin) | 157 | 157 | 0 | 0 | 0.019 |
| NPr (neutral metalloprotease) | 60 | 60 | 0 | 0 | 0.039 |
| acid_protease (aspergillopepsin) | 25 | 25 | 0 | 0 | 0.020 |

**Zero exposed or partially exposed sites across all three proteases.** The max risk score is determined purely by buried-site risk: accessibility_weight (0.1) × effective protease activity. NPr drives the max at 0.039 because it has higher salt tolerance (39% residual at 17.5% NaCl) than ALP (19%) or acid_protease (19.5%).

The risk score floor of 0.039 is the mathematical minimum given the protease parameters — no further structural improvement is possible once all sites are buried.

---

## Verdict interpretation

**The LOW verdict is not surprising — it was structurally predicted by comp-006.**

comp-006 established that the SCR1–4 domains contribute zero exposed sites. comp-012 confirms that a construct containing only those domains scores LOW. The 10-fold risk-score drop (0.388 → 0.039) maps directly to the stalk removal: 9 NPr exposed sites → 0, 48 ALP exposed sites → 0, 1 acid_protease exposed site → 0.

**Structural comparison to uricase (comp-001), the benchmark LOW:**

| Feature | Uricase (comp-001) | CD55 SCR1-4 (comp-012) |
|---|---|---|
| Construct length | 301 aa | 251 aa |
| Mean pLDDT | 97.1 | 96.7 |
| Min pLDDT | 80.5 | 85.6 |
| % pLDDT > 80 | 100% | 100% |
| Exposed sites | 0 | 0 |
| Verdict | LOW (0.039 max) | LOW (0.039 max) |

The SCR1-4 construct matches uricase on every structural metric. The max risk scores are identical (both 0.039) because both have only buried sites and the NPr effective activity (0.388) sets the buried-site ceiling for the same conditions.

**Important caveat on the disulfide contribution:** The SCR domains contain 12 conserved disulfide bonds (3 per domain). This analysis treats them as standard polypeptide — disulfide cross-linking further reduces backbone flexibility and proteolytic accessibility relative to what pLDDT alone captures. The true risk in the SCR domains is therefore lower than 0.039 for any correctly folded construct. The LOW verdict likely *underestimates* the actual protease resistance of a disulfide-intact SCR1-4 fragment.

---

## The CP0 gap question

The computational feasibility gate is resolved in favor of the SCR1-4 construct. The remaining open questions before this becomes a real wet-lab proposal:

**1. Does SCR1-4 without the stalk retain complement-regulatory activity?**  
Native DAF/CD55 requires SCR2–4 for C3b/C4b binding and C3 convertase decay-accelerating activity; SCR1 contributes primarily to cofactor function. The stalk is a GPI-anchor linker with no known enzymatic or binding activity. Soluble forms of related proteins (sCR1, which lacks a GPI anchor) retain full complement-inhibitory function, suggesting SCR domains function independently of the stalk. However, this is a mechanistic extrapolation — the specific CD55 SCR1-4 soluble fragment has not been validated functionally in a gut-lumen complement assay (Mechanistic Extrapolation).

**2. Can A. oryzae fold 12 intrachain disulfide bonds in a secreted protein?**  
A. oryzae has protein disulfide isomerase (PDI) activity in its ER. The organism secretes disulfide-containing proteins (e.g., glucoamylase, which has 2 disulfide bonds). Whether it can fold 12 intrachain disulfides in an SCR repeat array is unknown. This is a non-trivial question — misfolded SCR domains would be non-functional even if protease-stable. Small-scale expression in A. oryzae with SDS-PAGE under reducing vs. non-reducing conditions would answer this.

**3. Is gut-lumen complement relevant to gout flare suppression?**  
The CP0 hypothesis (complement priming via C5a) is established in synovial fluid and joint tissue. Gut-lumen complement activation, and whether mucosal-expressed CD55 can suppress it meaningfully, is less characterized. Complement activity in the gut lumen is documented (particularly in inflammatory states), but whether gut-lumen DAF expression can modulate systemic C5a-mediated joint inflammation requires direct evidence. This is the fundamental CP0 mucosal-coverage question.

**4. Expression titers and activity per gram of koji:**  
Even a correctly folded, protease-stable, functionally active SCR1-4 fragment needs to be expressed at levels sufficient for gut-lumen therapeutic effect. The ACS Syn Bio 2025 engineered lipase benchmark (365 μmol/h/OD in S. boulardii) sets a reference point for heterologous enzyme expression, but complement regulators are not enzymes — their functional unit is dose-dependent suppression, not catalytic turnover. Dosing calculations require knowing both expression titer and in vivo effective dose.

---

## Key limitations

- **Disulfide bonds not modelled.** 12 conserved disulfide bonds in SCR1-4 (3 per domain) substantially reduce backbone flexibility and proteolytic susceptibility beyond pLDDT. This analysis likely **overestimates** the already-low risk in the SCR domains. The true risk for a correctly-folded construct is lower than 0.039.
- **pLDDT ≠ solvent accessibility.** All 242 SCR-domain sites are classified as buried (pLDDT ≥ 80), but SASA calculation on the AlphaFold structure would identify which surface loops are actually solvent-exposed at domain interfaces. Some "buried" sites may be accessible at the protein surface. A structure-based SASA analysis would refine this.
- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled. May over-count recognition sites; extended context in the compact SCR fold may disfavor cleavage at many nominal sites.
- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range (pH 6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge. True activity is lower — risk is conservatively overstated. If corrected, max risk score would fall below 0.039.
- **CCP-regulatory activity not assessable in silico.** Whether the stalk-truncated SCR1-4 construct inhibits C3b deposition, accelerates C3 convertase decay, or reduces C5a generation in a gut-lumen assay is entirely a wet-lab question. Structural protease stability is necessary but not sufficient for function.
- **O-glycosylation not modelled.** Native SCR domains carry N-linked glycans; stalk O-glycans are absent by design. A. oryzae glycosylation differs from human; net effect on stability and function is unknown.

---

## Next step: wet-lab proposal

The computational feasibility gate is cleared. The logical next step is a minimal wet-lab expression test:

**Expression screen:** Clone DAF/CD55 SCR1-4 (aa 35–285) with an A. oryzae α-amylase signal peptide (Ward et al. 1995) into an A. oryzae expression vector (e.g., pANe-based system). Express under standard koji fermentation conditions. Assess: (a) secretion (SDS-PAGE of culture supernatant), (b) correct folding (non-reducing vs. reducing SDS-PAGE for disulfide bond count), (c) protease stability in shio-koji-conditioned medium over 7–14 days.

**Complexity:** Medium. Standard A. oryzae transformation protocols are well-established; the expression construct is a 750 bp insert with no unusual features beyond the 12 disulfide bonds. The disulfide folding question is the primary unknown.

**Collaboration context:** comp-006 cross-references Rheinallt Jones (Emory, immunology) and Lauren Collier-Hyams (Emory, epithelial biology) as potential collaborators for functional complement assays. Expression screen could be a Phase 0 co-experiment if collaboration is established.

---

## Cross-references

- [daf-cd55-protease-stability-computational.md](./daf-cd55-protease-stability-computational.md) — comp-006; the full ectodomain HIGH result that motivated this analysis
- [modality-chokepoint-matrix.md](./modality-chokepoint-matrix.md) — "Engineered soluble complement regulators" row; CP0 platform gap
- [complement-c5a-gout.md](./complement-c5a-gout.md) — CP0 chokepoint; why complement regulation matters for gout
- [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) — comp-001; the LOW-verdict structural benchmark
- [lactoferrin-protease-stability-computational.md](./lactoferrin-protease-stability-computational.md) — comp-005; the HIGH/MODERATE comparison
- [computational-experiments.md](./computational-experiments.md) — tracking index
- [engineered-koji-protocol.md](./engineered-koji-protocol.md) — A. oryzae expression context
