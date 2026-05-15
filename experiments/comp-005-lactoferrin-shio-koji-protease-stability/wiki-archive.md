---
title: "Lactoferrin Shio-Koji Protease Stability: Computational Analysis (comp-005)"
date: 2026-05-05
tags: [lactoferrin, protease, shio-koji, computational, alphafold, structural-biology]
related:
  - lactoferrin.md
  - uricase-protease-stability-computational.md
  - computational-experiments.md
  - validation-experiments.md
  - engineered-koji-protocol.md
  - koji-endgame-strain.md
sources:
  - "UniProt P02788 (human lactoferrin, canonical isoform, SV=6)"
  - "AlphaFold AF-P02788-F1-model_v6 (EMBL-EBI)"
  - "MEROPS database release 12.4"
  - "Koaze et al. 1964 (acid protease pH-activity curve)"
---

# Lactoferrin Shio-Koji Protease Stability: Computational Analysis (comp-005)

**Status:** Complete — 2026-05-05  
**Experiment folder:** [`experiments/comp-005-lactoferrin-shio-koji-protease-stability/`](../experiments/comp-005-lactoferrin-shio-koji-protease-stability/)  
**Companion analysis:** [comp-001 (uricase)](./uricase-protease-stability-computational.md)

---

## Summary

AlphaFold pLDDT structural analysis of human lactoferrin (P02788, 710 aa) against three *A. oryzae* koji proteases (ALP, NPr, acid protease) under shio-koji conditions (17.5% NaCl midpoint, pH 4.5–5.0, 22°C).

**Two verdicts:**

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| Full sequence (incl. signal peptide) | **HIGH** | 0.388 | NPr |
| Mature protein only (aa 20–710) | **MODERATE** | 0.188 | ALP |

The distinction is critical: **all top-5 cleavage sites across all three proteases are in the signal peptide (aa 1–19, pLDDT 35–54).** If *A. oryzae* signal peptidase cleaves the heterologous signal sequence (which it commonly does for secreted proteins), the operative risk for the mature protein is MODERATE. If signal peptide is retained, full-sequence verdict (HIGH) applies.

**The §1.10 lactoferrin arm remains a feasibility gate** — this analysis identifies *where* to look if degradation is observed, but the wet-lab result is the primary determination. Contrast with comp-001 (uricase), which produced a LOW verdict and reframed §1.10's uricase arm as a confirmation experiment.

---

## Method

Same shared library as comp-001 (`experiments/lib/protease_stability.py`). Risk score per site:

```
risk_score = accessibility_weight × salt_residual_activity × ph_activity_factor
```

Accessibility weights: buried (pLDDT ≥ 80) = 0.1; partially exposed (pLDDT 65–80) = 0.4; exposed (pLDDT < 65) = 1.0.

pH activity factors: ALP conservatively 1.0 (outside active pH 6–12), NPr conservatively 1.0 (at edge of pH 5–9), acid protease 0.30 (Koaze et al. 1964 activity-vs-pH curve).

---

## Structural context

**Signal peptide (aa 1–19, MKLVFLVLLFLGALGLCLA):** pLDDT 35–54 throughout — fully disordered. This is the native mammalian secretory signal; it is co-translationally cleaved in the ER in the native context. In *A. oryzae*, heterologous signal peptide processing is common but not guaranteed for all foreign sequences.

**Inter-lobe linker (approx aa 432–445):** pLDDT 68–81 — partially exposed. Connects the N-lobe and C-lobe. Less constrained than either lobe core, giving some accessibility to recognition sites in this window.

**Lobe cores (majority of residues):** pLDDT 88–99 — well-folded, comparable to uricase. Protease risk in the lobe cores is low.

---

## Per-protease results

| Protease | Total sites | Exposed (full) | Exposed (mature) | Partly exposed | Max risk (full) | Max risk (mature) |
|---|---|---|---|---|---|---|
| ALP (alkaline subtilisin) | 492 | 21 | 3 | 4 | 0.188 | 0.188 |
| NPr (neutral metalloprotease) | 234 | 14 | 0 | 1 | 0.388 | 0.155 |
| acid_protease (aspergillopepsin) | 128 | 10 | 0 | 0 | 0.195 | 0.020 |

ALP's 3 mature-protein exposed sites (pLDDT < 65, outside signal peptide) drive the MODERATE verdict for mature lactoferrin. NPr has the highest full-sequence score (0.388) but zero exposed sites in the mature protein — its entire risk comes from signal peptide access.

---

## Comparison with uricase (comp-001)

| Feature | Uricase (comp-001) | Lactoferrin (comp-005) |
|---|---|---|
| Length | 301 aa | 710 aa (incl. signal peptide) |
| Mean pLDDT | 97.1 | 95.0 |
| Min pLDDT | 80.5 | 35.8 (signal peptide) |
| % residues pLDDT > 80 | 100% | 96.1% |
| Signal peptide | None (mature form only) | Present (uncertain processing) |
| Quaternary structure | Homotetramer (buries additional surface) | Bilobal monomer (exposed linker) |
| Full-sequence verdict | LOW | HIGH |
| Mature-protein verdict | LOW | MODERATE |

The key structural difference: uricase has no disordered regions and no signal peptide in the analyzed sequence — it is all compact, homotetramer-ready structure. Lactoferrin's soft spots are the signal peptide and the inter-lobe linker.

---

## Impact on §1.10 experimental framing

Unlike the uricase arm, the comp-005 result does **not** shift §1.10's lactoferrin arm from a feasibility gate to a confirmation experiment. The MODERATE mature-protein verdict (0.188 max, ALP) and the signal-peptide uncertainty together mean the wet-lab result is the primary determination.

If wet-lab §1.10 shows lactoferrin degradation while uricase survives:
- **Most likely cause:** ALP attack on 3 mature-protein exposed sites, and/or NPr attack if signal peptide is retained.
- **First diagnostic:** Western blot for characteristic ~40 kDa N-lobe + ~40 kDa C-lobe cleavage products (inter-lobe linker cleavage) vs. intact 80 kDa band.
- **Second diagnostic:** N-terminal sequencing to determine whether the 19 aa signal peptide was processed.

If wet-lab shows lactoferrin stability comparable to uricase:
- The mature-protein MODERATE verdict would be overstated — possibly because ALP's pH factor (conservatively 1.0) overcounts its activity at pH 4.5–5.0, where ALP is outside its active range.
- The correct update: revise ALP pH factor down (to ~0.1–0.3) and rerun comp-005; expect LOW mature-protein verdict.

---

## Key limitations

- **pLDDT ≠ SASA.** Signal peptide pLDDT 35–54 reliably predicts disorder; inter-lobe linker pLDDT 68–81 indicates partial exposure but solvent-accessible surface area (SASA) calculation would sharpen the accessibility score. A structure-based SASA analysis could refine the linker risk.
- **Signal peptide processing uncertain.** *A. oryzae* has signal peptidase activity, but cleavage efficiency for heterologous signal sequences varies. The two verdicts bracket the expected range.
- **Glycosylation not modelled.** Human lactoferrin has three characterized N-glycosylation sites (N137, N478, N623). N-glycans sterically shield backbone near Asn, and *A. oryzae* expression may hyperglycosylate the protein further — potentially shielding surface-accessible mature-protein sites. This biases the MODERATE verdict toward overestimating risk.
- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled; may over-count recognition sites.
- **ALP and NPr pH factors conservatively set to 1.0.** True activity at pH 4.5–5.0 is lower — likely ~0.1–0.2 for ALP (outside range 6–12) and ~0.5–0.7 for NPr (at lower edge 5–9). Risk is conservatively overstated for both.
- **Iron-binding state not modelled.** Apo-lactoferrin (iron-free) is more open than holo-lactoferrin; iron availability in shio-koji is uncertain. This analysis models the AlphaFold holo-like structure.

---

## Cross-references

- [lactoferrin.md](./lactoferrin.md) — parent wiki page; §7 covers Open Enzyme feasibility bet
- [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) — comp-001, the companion analysis
- [computational-experiments.md](./computational-experiments.md) — tracking index
- [validation-experiments.md §1.10](./validation-experiments.md) — wet-lab gate this informs
- [engineered-koji-protocol.md](./engineered-koji-protocol.md) — lactoferrin expression protocol context
- [koji-endgame-strain.md](./koji-endgame-strain.md) — dual-payload strain thesis
