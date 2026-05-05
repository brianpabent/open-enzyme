---
title: "C. utilis Uricase Cassette Compatibility — Dual-Cassette Koji Endgame Strain (Computational, comp-011)"
date: 2026-05-05
tags:
  - computational
  - dual-cassette
  - uricase
  - candida-utilis
  - cyberlindnera-jadinii
  - lactoferrin
  - ward-1995
  - kex2
  - codon-usage
  - aspergillus-oryzae
  - cassette-design
  - endgame-strain
  - koji
  - alln-346
related:
  - cassette-compatibility-computational.md
  - uricase-variant-selection.md
  - computational-experiments.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - hypotheses/H01-ward-dual-cassette.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - lactoferrin.md
sources:
  - "Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791)"
  - "Huynh HH, Morita N, Sakamoto T, et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131)"
  - "Rockwell NC, Krysan DJ, Komiyama T, Fuller RS. Chem Rev 2002;102(12):4525-48 (PMID 12475198)"
  - "Brenner C, Fuller RS. Proc Natl Acad Sci 1992;89:922-6 (PMID 1371243)"
  - "US10815461B2 — Allena Pharmaceuticals ALLN-346 C. utilis uricase directed-evolution mutations"
  - "Sands BE et al. Nat Commun 2022 — SEL-212 / pegadricase phase 3 attribution (PMID 35022448)"
status: complete
---

# *C. utilis* Uricase Cassette Compatibility — Computational Analysis (comp-011)

## 1. Question

Does the *C. utilis* uricase (P78609) + lactoferrin (P02788) payload pair have any cassette-design-specific issues — codon collisions, KEX2 site geometry problems, or secretion-pathway burden — that the Ward 1995 glucoamylase-KEX2 fusion architecture will not handle out of the box in *A. oryzae*?

This is the follow-on to [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) (comp-010), which verified **LOW cassette-design risk** for *A. flavus* uricase (Q00511) + lactoferrin. The motivation: [uricase-variant-selection.md](./uricase-variant-selection.md) documents that the industry's revealed preference for oral uricase programs is *C. utilis*, not *A. flavus* — three independent programs (ALLN-346, SEL-212 pegadricase, SSS11) all chose *C. utilis*. If the project adopts *C. utilis* as the §1.9 payload, the comp-010 LOW verdict does not transfer automatically. *C. utilis* uricase has a different sequence, different codon-usage profile (AT-biased yeast vs. GC-biased filamentous fungus), 4 free cysteines (vs. 0 in *A. flavus*), and 2 internal KR sites vs. 1.

comp-011 resolves this in silico using the same seven-analysis pipeline as comp-010.

---

## 2. Verdict

**Overall cassette-design risk: MODERATE** (Mechanistic Extrapolation; in silico only)

No blocking cassette-design issues identified. The *C. utilis* uricase (P78609) + lactoferrin (P02788) pair is architecturally compatible with the Ward 1995 / Huynh 2020 design, but carries three design requirements that are absent from the comp-010 (*A. flavus*) baseline:

1. **Full codon optimization required** for *C. utilis* uricase — the AT-biased yeast codon preference (GC~42%) diverges substantially from the *A. oryzae* host (GC~54%). CAI proxy = 0.65 vs. 1.51 for *A. flavus*. This means both cassettes require gene synthesis optimization (vs. only lactoferrin in the *A. flavus* design). Not a blocker — standard gene synthesis resolves it.

2. **4 free cysteines** (positions 39, 168, 250, 293) vs. 0 in *A. flavus* uricase. No disulfide bonds are annotated, but free thiols in the oxidizing *A. oryzae* ER lumen during secretion can form aberrant intermolecular disulfides. Risk: aggregation bands in secreted fraction. Mitigation: non-reducing SDS-PAGE QC.

3. **2 internal KR sites** (positions 130 and 138, both HIGH risk in KEX2 scoring) vs. 1 in *A. flavus* (position 128). Non-load-bearing in the direct-secretion cassette design (KEX2 never encounters the payload), but both require mutation if *C. utilis* uricase is ever moved to a fusion architecture.

**comp-010 comparison: comp-010 (*A. flavus*) = LOW. comp-011 (*C. utilis*) = MODERATE.** The MODERATE verdict reflects more design work required, not a fundamental incompatibility. The differences are manageable with standard gene synthesis and SDS-PAGE QC.

---

## 3. Per-Analysis Summary

| Analysis | *C. utilis* uricase verdict | Lactoferrin verdict | comp-010 delta (*A. flavus*) |
|---|---|---|---|
| 1. Codon usage | **HEAVY** (full optimization required; CAI proxy 0.65) | LOW (proxy; full opt required in practice) | **Delta: A. flavus LOW (CAI proxy 1.51)** |
| 2. KEX2 geometry | HIGH (2 sites, positions 130 and 138, both HIGH) — not load-bearing (direct-secretion) | MODERATE (1 site, position 579, P1'=K; 1 abolished at 38, P1'=D) | Delta: A. flavus 1 site (128 HIGH) |
| 3. Routing/secretion | MODERATE (C-terminal TKL, UniProt-annotated microbody signal) | LOW (no routing issues) | Comparable (A. flavus SKL — same risk level) |
| 4. Disulfide load | VERY LOW (0 disulfides) + **4 free Cys new risk** | MODERATE (17 disulfides, 1.06× Huynh baseline) | **Delta: A. flavus 0 Cys (no free-Cys risk)** |
| 5. N-glycosylation | 1 predicted (NSS at pos 54; not UniProt-annotated) | 3 predicted, all UniProt-annotated (N137, N478, N623) | Comparable (A. flavus 1 predicted at pos 191) |
| 6. Dual-cassette burden | **MODERATE** | — | **Delta: comp-010 LOW (A. flavus codon burden LOW)** |
| 7. Comparison | Harder than comp-010 on codon + free-Cys axes; strategic advantage from ALLN-346 prior art | Identical to comp-010 | — |

---

## 4. Material Differences vs. comp-010 (*A. flavus*)

The platform decision (which uricase to use for §1.9) hinges on this comparison. Three differences are material:

### 4.1 Codon burden: HEAVY vs. LOW

*C. utilis* (*Cyberlindnera jadinii*) is a yeast with AT-biased codon usage (GC~42%). *A. oryzae* is a GC-biased filamentous ascomycete (~54% GC). The preferred codons for *C. utilis* (e.g., GCT for Ala, AGA for Arg, GAA for Glu) are systematically in the 0.40–0.80 RSCU range in *A. oryzae* — disfavored but not individually rare by the RSCU < 0.4 threshold. The aggregate effect is a CAI proxy of 0.65 (meaning the geometric mean of the RSCU values for *C. utilis* preferred codons in *A. oryzae* is 0.65 — substantially below 1.0 = neutral). In contrast, *A. flavus* has near-identical codon preferences to *A. oryzae* (both GC-biased, ~54% GC), giving a CAI proxy of ~1.51.

**Practical consequence:** full gene synthesis with *A. oryzae* codon optimization is mandatory for *C. utilis* uricase — the same requirement as for human lactoferrin. In the *A. flavus* design (comp-010), only lactoferrin required full optimization; the uricase cassette was optimization-free. With *C. utilis*, BOTH cassettes require gene synthesis optimization. Cost delta: ~$200–400 for one additional codon-optimized gene. Not a blocker. (Mechanistic Extrapolation)

### 4.2 Free cysteines: 4 vs. 0

*C. utilis* uricase (P78609) has 4 cysteine residues (positions 39, 168, 250, 293). None are annotated as disulfide-bonded in UniProt — consistent with uricase family biochemistry (Cu-independent, O2-dependent active site, no disulfide requirement). *A. flavus* uricase (Q00511) has 0 cysteines.

When *C. utilis* uricase is expressed via the secretory pathway in *A. oryzae* and transits the oxidizing ER lumen, these 4 free thiols are exposed to PDI/ERO1. The risk is aberrant intermolecular disulfide formation producing aggregated species. This is a new risk factor absent in the *A. flavus* design.

Mitigation strategy: (1) run non-reducing SDS-PAGE on secreted fractions to detect high-MW aggregation bands; (2) if aggregation is observed, use AlphaFold2 to identify solvent-exposed Cys residues and engineer Cys→Ser substitutions at surface positions. Buried cysteines are less accessible to PDI and lower risk. (Mechanistic Extrapolation; no quantitative model available for magnitude)

### 4.3 KEX2 internal sites: 2 vs. 1

*C. utilis* uricase has 2 internal KR dipeptides (positions 130–131: KRIT, P1'=I; positions 138–139: KRSG, P1'=S). Both I and S are in the "preferred" P1' category for KEX2 cleavage — both are scored HIGH by the canonical Rockwell 2002 / Brenner 1992 rules. The two sites are 8 residues apart in context GGEKRITDLYYKRSGD.

*A. flavus* has 1 internal KR site (position 128, P1'=N, HIGH).

In the proposed direct-secretion cassette design (PTEF1 or PamyB – amyB SP – uricase – TgpdA), KEX2 is not involved in uricase processing. Both sites are non-load-bearing. If *C. utilis* uricase is ever moved to a glucoamylase-KEX2 fusion architecture, a double KR→KQ mutation at positions 130 and 138 would be required (vs. single mutation at 128 for *A. flavus*). (Mechanistic Extrapolation; P1' rules from S. cerevisiae Kex2p homology)

---

## 5. Strategic Advantage of *C. utilis* (Non-Cassette Axis)

The comp-010 vs. comp-011 comparison is purely a cassette-design comparison. There is one strategic advantage of *C. utilis* that is not captured by the cassette-design analysis but is directly relevant to the oral/gut-lumen track:

**ALLN-346 ProteinGPS prior art (US10815461B2):** Allena Pharmaceuticals disclosed seven point mutations on a *C. utilis* uricase backbone (I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) that improve protease resistance and thermostability in the gut-lumen context. These mutations were identified by directed-evolution (ProteinGPS platform) and validated in Phase 1 / Phase 2a clinical studies (ALLN-346). They are publicly disclosed — freedom-to-operate for research use.

*A. flavus* uricase has no equivalent publicly-disclosed protease-resistance mutation panel. The ALLN-346 mutations convert *C. utilis* from "less-characterized alternative" to "alternative with millions of dollars of directed-evolution engineering already available to adopt."

This strategic asymmetry is noted here but does not change the cassette-design risk verdict. See [uricase-variant-selection.md](./uricase-variant-selection.md) for the full analysis.

---

## 6. Design Recommendations for §1.9

1. **If adopting *C. utilis* uricase (industry-preferred oral track):**
   - Order codon-optimized *C. utilis* uricase CDS from gene synthesis vendor (*A. oryzae* codon table). This is mandatory — unlike *A. flavus*, the native *C. utilis* codon preferences will suppress expression without optimization.
   - Add ALLN-346 ProteinGPS mutations (US10815461B2: I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) into the codon-optimized synthesis. Order as a single variant construct.
   - Cassette architecture: direct-secretion (PTEF1 or PamyB – amyB SP – codon-optimized C. utilis uricase – TgpdA). Do NOT use glucoamylase-KEX2 fusion for uricase — avoids the 2 internal KR site issue entirely.
   - Add non-reducing SDS-PAGE to the secreted fraction QC panel to detect free-Cys aggregation.

2. **If keeping *A. flavus* uricase (comp-010-verified LOW risk track):**
   - comp-010 verdict stands: LOW risk, no additional design requirements. Codon optimization optional but low-priority.
   - Recommended if speed-to-first-clone is the priority or rasburicase-derivative IP strategy is preferred.

3. **Recommended approach for §1.9: empirical head-to-head:**
   - Order both *A. flavus* (Q00511, codon-optimized) and *C. utilis* (P78609, codon-optimized + ALLN-346 mutations) as direct-secretion cassettes. The §1.9 fermentation experiment resolves the platform decision empirically at $0 additional fermentation cost (same experiment, two strains). Total gene synthesis cost delta: ~$200–400 for the second codon-optimized gene.

4. **Lactoferrin cassette (unchanged from comp-010):** PamyB – glucoamylase – KRGGG – hLf (codon-optimized) – TamyB. Monitor internal KR site at position 579 (P1'=K, MODERATE risk) by SDS-PAGE.

5. **Host strain:** NSlD-ΔP10 (10-protease-deletion *A. oryzae*) — required, same as comp-010.

---

## 7. Limitations

1. **CAI proxy, not CDS analysis.** Codon burden analysis uses protein sequence + origin-organism preferred codons as a proxy. The HEAVY verdict for *C. utilis* reflects the CAI proxy (0.65) capturing the systematic AT/GC mismatch. A gene synthesis vendor's codon optimizer resolves this — the burden analysis informs whether optimization is required, not its magnitude after optimization.

2. ***C. utilis* codon table is a genome-wide estimate.** A *C. utilis*-specific highly-expressed secreted-gene codon table is not publicly available. The AT-bias is well-established; specific RSCU values carry ±15–20% error.

3. **Free-Cys ER aggregation risk: no quantitative model.** The magnitude of aggregation from 4 free cysteines in the *A. oryzae* ER is empirically unknown. Flagged as a design consideration requiring SDS-PAGE monitoring, not a predicted outcome.

4. **P78609 is PE=3 (Inferred from homology).** The *C. utilis* uricase entry has not been directly characterized biochemically under this UniProt accession. The ALLN-346 work provides indirect evidence of biochemical activity on this backbone, but the exact parent sequence Allena used is not disclosed.

5. **KEX2 P1' rules from *S. cerevisiae* Kex2p homology.** *A. oryzae* kexB specificity has not been published with a full P1' preference matrix. This is the same caveat as comp-010.

6. **Solid-state format not modeled.** Solid-state vs. submerged differences (water activity, O2 gradient, secretion dynamics) are not captured computationally (Sun 2024 caveat).

---

## 8. Accession Note

UniProt P15296 was cited in early project planning as the likely *C. utilis* uricase accession. On retrieval (2026-05-05), P15296 returns sp|P16320|NOF_DROME (a Drosophila transposable element protein) — indicating this accession has been reassigned or merged. The correct reviewed Swiss-Prot entry for *Candida utilis* / *Cyberlindnera jadinii* uricase is **P78609 (URIC_CYBJA)**, confirmed by taxon search (OX=4903). comp-011 uses P78609.

---

## 9. Cross-References

- [experiments/comp-011-c-utilis-uricase-cassette-compatibility/](../experiments/comp-011-c-utilis-uricase-cassette-compatibility/) — Analysis code, inputs, outputs (machine-readable JSON + human-readable summary)
- [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) — comp-010 page (*A. flavus* baseline, LOW risk)
- [uricase-variant-selection.md](./uricase-variant-selection.md) — Industry-revealed preference analysis; comp-011 verdict and platform implications noted there
- [hypotheses/H01-ward-dual-cassette.md](./hypotheses/H01-ward-dual-cassette.md) — Falsification Card; comp-011 is design support for §1.9
- [validation-experiments.md](./validation-experiments.md) — §1.9 wet-lab experiment this analysis informs
- [koji-endgame-strain.md](./koji-endgame-strain.md) — Protocol sketch for §1.9
- [experiments/comp-001-uricase-shio-koji-protease-stability/](../experiments/comp-001-uricase-shio-koji-protease-stability/) — *A. flavus* uricase protease stability (comp-001, LOW)
- [experiments/comp-005-lactoferrin-shio-koji-protease-stability/](../experiments/comp-005-lactoferrin-shio-koji-protease-stability/) — Lactoferrin protease stability (comp-005, MODERATE)

---

*Evidence level for all findings: Mechanistic Extrapolation — in silico sequence analysis only. Wet-lab confirmation required for all design recommendations.*
