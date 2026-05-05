# comp-011 — Cassette Compatibility Analysis: C. utilis Uricase + Lactoferrin

**Experiment:** comp-011  
**Date:** 2026-05-05  
**Script:** `experiments/comp-011-c-utilis-uricase-cassette-compatibility/analyze.py`  
**Follow-on to:** comp-010 (A. flavus uricase Q00511 + lactoferrin P02788)  

---

## 1. Question

Does the *C. utilis* uricase (P78609) + lactoferrin (P02788) payload pair have any cassette-design-specific issues — codon collisions, KEX2 site geometry problems, secretion-pathway burden, or ER-routing conflicts — that the Ward 1995 glucoamylase-KEX2 architecture will not handle out of the box in *A. oryzae*?

This is the industry-preferred uricase backbone (ALLN-346, SEL-212 pegadricase, SSS11 — all three recent oral/non-IV programs chose *C. utilis*). comp-010 verified LOW risk for *A. flavus* (Q00511). comp-011 asks whether the *C. utilis* cassette inherits that LOW verdict or carries additional risks.

---

## 2. Verdict

**Overall cassette-design risk: MODERATE** (Mechanistic Extrapolation; in silico only)

The C. utilis uricase (P78609) + lactoferrin (P02788) payload pair in the Ward 1995 glucoamylase-KEX2 / direct-secretion architecture has no blocking cassette-design issues but carries three manageable design requirements absent in the comp-010 (A. flavus) baseline: (1) full codon optimization required for C. utilis (AT-biased yeast origin, GC~42% vs. A. oryzae ~54%); (2) 4 free cysteines in C. utilis uricase create a theoretical ER aggregation risk during secretion; (3) 2 internal KR sites (positions 130 and 138) vs. 1 in A. flavus — non-load-bearing in direct-secretion design but noted for completeness. The MODERATE verdict is design-driven, not a fundamental incompatibility. Lactoferrin findings are numerically identical to comp-010.

**comp-010 comparison:** comp-010 (*A. flavus* Q00511 + lactoferrin) = **LOW**. comp-011 (*C. utilis* P78609 + lactoferrin) = **MODERATE**. The delta is not a fundamental incompatibility — it reflects three manageable design requirements that gene synthesis and SDS-PAGE QC resolve.

---

## 3. Per-Analysis Findings

### 3.1 Codon Usage Compatibility

| Metric | C. utilis uricase (P78609) | Lactoferrin (P02788) |
|---|---|---|
| Origin | C. utilis / Cyberlindnera jadinii (yeast) | Homo sapiens (mammalian) |
| Sequence length | 303 aa | 710 aa |
| Codons analyzed | 303 | 710 |
| Rare codons (RSCU < 0.4) | 0 (0.0%) | 0 (0.0%) |
| CAI proxy (geometric mean RSCU) | 0.6525 | 1.4463 |
| Hotspots (≥3 consecutive rare) | 0 | 0 |
| Burden classification | **HEAVY** | **LOW** |

**C. utilis uricase:** Full codon optimization required: CAI proxy (0.6525) indicates systematic codon mismatch between origin organism and A. oryzae host — all preferred codons are in the disfavored-but-not-rare range (RSCU 0.40–0.80). This is characteristic of an AT-biased yeast origin in a GC-biased filamentous fungus host. Full gene synthesis with A. oryzae codon optimization is required. Compare: A. flavus CAI proxy ~1.50 (near-matching host); C. utilis CAI proxy 0.6525 (systematic mismatch).

**Lactoferrin:** Minimal codon optimization needed; origin-preferred codons largely overlap A. oryzae preferences

**Design recommendation:** *C. utilis* uricase (yeast, AT-biased, GC~42%) has substantially different codon preferences from *A. oryzae* (filamentous ascomycete, GC-biased, ~54% GC). This is fundamentally different from *A. flavus* (comp-010), which shares the GC-biased codon preference with *A. oryzae* and required minimal/no codon optimization. **Full gene synthesis with A. oryzae codon optimization is mandatory for C. utilis uricase** — the same requirement applies to lactoferrin. This is standard practice and is not a design blocker, but it means both cassettes require optimization (vs. only lactoferrin in the A. flavus design). Cost impact: one additional codon-optimized gene synthesis order (~$200–400 USD for a 303-aa gene).

---

### 3.2 KEX2 Site Geometry

| Metric | C. utilis uricase (P78609) | Lactoferrin (P02788) |
|---|---|---|
| Signal peptide (excluded from scan) | 0 aa | 19 aa |
| Mature protein length | 303 aa | 691 aa |
| Internal K-R sites (total) | 2 | 2 |
| High-risk sites (P1' preferred) | 2 | 0 |
| Moderate-risk sites | 0 | 1 |
| Low-risk sites (P1'=D/E — non-functional) | 0 | 1 |
| KEX2 internal site risk | **HIGH** | **MODERATE** |

**C. utilis uricase:** 2 high-risk site(s) — truncated protein species predicted; linker redesign or site mutation recommended

**Lactoferrin:** 1 moderate-risk site(s) — may produce minor truncation bands; verify by SDS-PAGE

**C. utilis uricase internal K-R sites:**

| Position (mature) | P1' | Risk | Context | Note |
|---|---|---|---|---|
| 130 | I | HIGH | `GGEKRITDL` | P1'=I — KEX2 cleavage likely; site is functional |
| 138 | S | HIGH | `LYYKRSGDY` | P1'=S — KEX2 cleavage likely; site is functional |

**Lactoferrin internal K-R sites:**

| Position (mature) | P1' | Risk | Note |
|---|---|---|---|
| 38 | D | LOW | P1'=D (acidic — KEX2 cleavage abolished; this site is non-functional) |
| 579 | K | MODERATE | P1'=K — KEX2 cleavage reduced but possible |

**Design recommendation:** The proposed cassette design places *C. utilis* uricase on a DIRECT-SECRETION cassette (PTEF1-amyB_SP-P78609-TgpdA), not a glucoamylase-KEX2 fusion. In this design, the two internal KR sites (positions 130 and 138) are irrelevant — KEX2 does not encounter the payload. IMPORTANT COMP-010 DELTA: *C. utilis* has 2 internal KR sites (positions 130 and 138, both HIGH risk: P1'=I and P1'=S) vs. *A. flavus* 1 site (128 HIGH). Both are non-load-bearing in direct-secretion, but if *C. utilis* uricase is ever moved to a fusion architecture, KR→KQ mutations at BOTH positions 130 and 138 are required (vs. only position 128 for A. flavus). The two sites are 8 residues apart (context: GEKRITD...YYKRSGD) — a double KR→KQ mutation is a straightforward synthesis modification.

---

### 3.3 Signal Peptide / Secretion-Targeting Analysis

| Metric | C. utilis uricase (P78609) | Lactoferrin (P02788) |
|---|---|---|
| Routing issues found | 1 | 0 |
| Routing risk | **MODERATE** | **LOW** |

**C. utilis uricase:** Moderate-risk routing signal(s) detected — verify in vivo

**Lactoferrin:** No ER-retention, PTS1, or PTS2 signals detected in mature protein sequence

**C. utilis uricase routing issues:**

- `PTS1_peroxisomal` at C-terminal tripeptide: `TKL` — C-terminal TKL is annotated by UniProt as a microbody targeting signal (residues 301–303 of full sequence). TKL is a weak PTS1 variant (non-canonical T at position -3). In the native C. utilis context this signal routes the protein to peroxisomes. In an A. oryzae expression context with an N-terminal secretion signal (amyB SP), the ER-targeting signal should outcompete the weak C-terminal PTS1. However: if expressed without a secretion signal (e.g., intracellular), TKL may route the protein to peroxisomes rather than cytoplasm. Verify that the secretion signal is intact in the final construct. In vivo immunofluorescence recommended if unexpected localization is observed. (risk: MODERATE)
  - UniProt note: Microbody targeting signal annotated at residues 301-303 (TKL) in UniProt P78609

**Context:** The *C. utilis* TKL signal and the *A. flavus* SKL signal (comp-010) are equivalent in risk — both are weak C-terminal PTS1 variants that will be outcompeted by an N-terminal ER-targeting signal in the secretory pathway. The routing risk is MODERATE for both variants, with the same in vivo verification recommendation. No delta vs. comp-010 for this axis.

---

### 3.4 Disulfide Bonding Load

| Metric | C. utilis uricase (P78609) | Lactoferrin (P02788) | Huynh 2020 baseline |
|---|---|---|---|
| Cysteine count | 4 | 33 | ~32 (16 per chain × 2) |
| Disulfide bonds | 0 | 17 | 16 (total both chains) |
| Free cysteines (estimated) | 4 | 0 | 0 |
| Folding load index (vs. Huynh = 1.0) | 0.000 | 1.062 | 1.00 |
| Fold risk | **VERY LOW** | **MODERATE** | — |

**C. utilis uricase:** No disulfide bonds annotated (UniProt) — no PDI load from disulfide formation. However, 4 free cysteine(s) present: risk of aberrant intermolecular disulfide formation in the oxidizing ER environment during secretion. Monitor for aggregation bands in non-reducing SDS-PAGE. A. oryzae ER is oxidizing (PDI/ERO1 system active); free cysteines in secreted proteins can form unintended disulfide bonds during transit. Folding is otherwise independent of the PDI oxidative pathway.

**Lactoferrin:** 17 disulfides — comparable to Huynh 2020 adalimumab baseline (16 disulfides)

**Dual-cassette combined:** 17 disulfides total (1.06× Huynh baseline). Lactoferrin carries the entire disulfide load; C. utilis uricase contributes nothing to PDI burden.

**IMPORTANT COMP-010 DELTA:** *C. utilis* uricase has 4 free cysteines (positions 39, 168, 250, 293) vs. *A. flavus* uricase which has 0 cysteines. These 4 cysteines are not annotated as disulfide-bonded (UniProt P78609 — consistent with uricase family biochemistry: the active site uses Cu-independent O2-dependent mechanism without disulfide bonds). However, during secretion through the *A. oryzae* ER lumen (which is oxidizing, with active PDI/ERO1), free thiols may form aberrant intermolecular disulfides leading to aggregation. This risk is absent in *A. flavus* (0 Cys) and is a new consideration for C. utilis. Mitigation: run non-reducing SDS-PAGE on secreted fractions to detect aggregation bands. If aggregation is observed, consider Cys→Ser mutation of solvent-exposed cysteines (use AlphaFold2 pLDDT to identify surface-exposed vs. buried positions before mutagenesis).

---

### 3.5 N-Glycosylation Site Prediction

| Metric | C. utilis uricase (P78609) | Lactoferrin (P02788) |
|---|---|---|
| Predicted N-X-S/T sequons (mature protein) | 1 | 3 |
| UniProt-annotated sites | 0 (none annotated) | 3 (N137, N478, N623) |

**C. utilis uricase predicted N-X-S/T sites:**

| Position (mature) | Sequon |
|---|---|
| 54 | `NSS` |

**Lactoferrin predicted N-X-S/T sites (cross-reference against UniProt N137, N478, N623):**

| Position (full seq) | Position (mature) | Sequon | UniProt annotated? |
|---|---|---|---|
| 156 | 137 | `NWT` | Yes |
| 497 | 478 | `NQT` | Yes |
| 642 | 623 | `NGS` | Yes |

**Glycosylation note:** *C. utilis* uricase is intracellular (peroxisomal) in its native context and is not glycosylated. The single predicted N-X-S/T sequon (NSS at position 54) is unlikely to be occupied in the native context. In *A. oryzae* expression via the secretory pathway, if OST can access this sequon during ER transit, partial glycosylation at N54 is possible. Fungal N-glycans (high-mannose) would alter the protein's size and potentially its activity. This is the same situation as *A. flavus* uricase (comp-010: 1 predicted N-X-S/T sequon, NFS at position 191; not UniProt-annotated). Risk: LOW for both variants — unoccupied in native context, unlikely to be significantly glycosylated in the secretory pathway given structural constraints.

---

### 3.6 Concurrent-Expression Secretion-Pathway Burden

| Axis | C. utilis uricase | Lactoferrin | Combined | Huynh 2020 baseline |
|---|---|---|---|---|
| Disulfides | 0 | 17 | 17 | 16 |
| N-glycosylation sites | 1 | 3 | 4 | 2 |
| Codon burden | HEAVY | LOW | — | HEAVY (both mammalian) |
| Folding load index | — | — | 1.06× | 1.00 |
| Free cysteines (uricase) | 4 | 0 | — | 0 |

**Overall dual-cassette secretion burden: MODERATE**

**Concurrent risk flags:**

- C. utilis uricase codon burden is HEAVY — AT-biased codons are rare in A. oryzae (GC-biased host). Full gene synthesis with A. oryzae codon optimization is required. Without optimization, expected expression will be substantially reduced (estimated 2-5x titer penalty based on codon harmonization studies in Aspergillus; Mechanistic Extrapolation).
- C. utilis uricase has 4 free cysteine(s): risk of aberrant disulfide formation in the oxidizing ER lumen during secretion. Monitor for aggregation bands by non-reducing SDS-PAGE. This risk is ABSENT in A. flavus uricase (0 cysteines).

**Informational (not a risk driver):** C. utilis uricase has 2 internal K-R site(s) (overall KEX2 risk: HIGH). NOT load-bearing: the proposed protocol places uricase on a direct-secretion cassette (PTEF1-amyB_SP-C_utilis_uricase-TgpdA), not a glucoamylase-KEX2 fusion. If C. utilis uricase is later moved to a fusion architecture, both sites require attention — notably position 130 (P1'=I, HIGH) and position 138 (P1'=S, HIGH). These two sites are in close proximity (8 residues apart, GEKRITD...YYKRSGD) — if uricase is ever placed in a KEX2 fusion, a KR->KQ double mutation at both sites would be required.

**Titer gap:** The H01 Lf target (500 mg/L) is 12.6× above Huynh 2020 vs. the Huynh 2020 adalimumab titer (39.7 mg/L). Ward 1995 achieved >2 g/L for lactoferrin specifically — 500 mg/L is within the demonstrated range for this protein in this host family.

---

### 3.7 Comparison: comp-011 (*C. utilis*) vs. comp-010 (*A. flavus*) vs. Huynh 2020

#### comp-011 vs. comp-010 (platform decision axis)

| Dimension | *C. utilis* uricase (comp-011) | *A. flavus* uricase (comp-010) |
|---|---|---|
| Accession | P78609 (URIC_CYBJA) | Q00511 (URIC_ASPFL) |
| Origin | Yeast (AT-biased, GC~42%) | Filamentous fungus (GC-biased, ~54% GC) |
| Codon burden in A. oryzae | **HEAVY** (full optimization required) | **LOW** (minimal optimization) |
| Cysteine count | 4 (0 disulfides) | 0 (0 disulfides) |
| Free-Cys ER aggregation risk | **Present** (4 free Cys) | **Absent** (0 Cys) |
| KEX2 internal sites | 2 (130 HIGH, 138 HIGH) | 1 (128 HIGH) |
| C-terminal peroxisomal signal | TKL (UniProt-annotated microbody signal) | SKL (PTS1 variant) |
| N-X-S/T sequons | 1 (NSS at pos 54) | 1 (NFS at pos 191) |
| Overall cassette-design risk | **MODERATE** | **LOW** |
| ALLN-346 mutation library | Available (US10815461B2) | Not available (no equivalent IP) |
| Industry oral-program preference | 3-of-3 recent programs | 0-of-3 recent programs |

**Where C. utilis is HARDER than A. flavus (cassette-design):**

- Codon burden: HEAVY (C. utilis, AT-biased ~42% GC) vs. LOW (A. flavus, GC-biased ~54% GC). A. flavus codon preferences closely match A. oryzae (both GC-biased filamentous ascomycetes); C. utilis codon preferences diverge substantially (yeast AT-bias). Full gene synthesis from scratch with A. oryzae codon optimization is required for C. utilis — the same requirement as for human lactoferrin. This adds cost and lead time but does not block the architecture.
- KEX2 internal sites: C. utilis has 2 sites (130 HIGH, 138 HIGH) vs. A. flavus 1 site (128 HIGH). Both are non-load-bearing in the direct-secretion architecture. If either uricase variant is moved to a KEX2 fusion, C. utilis requires mutation of 2 sites vs. 1 — a modest but real additional engineering step.
- Free cysteines: C. utilis has 4 Cys (0 disulfides) vs. A. flavus 0 Cys. The 4 free cysteines in C. utilis uricase are a new risk factor: aberrant disulfide bond formation in the oxidizing A. oryzae ER lumen during secretion. This is specific to C. utilis and absent in A. flavus. Risk mitigation: monitor by non-reducing SDS-PAGE; if aggregation bands appear, consider Cys→Ser mutation of solvent-exposed free cysteines.

**Where C. utilis is EASIER / BETTER than A. flavus (strategic):**

- ALLN-346 prior art: C. utilis backbone carries publicly disclosed directed-evolution improvements (US10815461B2: I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) from Allena's ProteinGPS program. These mutations improve protease resistance and stability in the gut lumen — directly relevant to oral delivery. A. flavus has no equivalent publicly disclosed protease-resistance mutation panel. This advantage is in the engineering/IP domain, not the cassette-design domain, but it is a material consideration for the oral/gut-lumen track.

**Where C. utilis is COMPARABLE to A. flavus:**

- Disulfide load: both A. flavus and C. utilis uricase have 0 annotated disulfide bonds — neither adds PDI burden. The full 17-disulfide load of the dual-cassette system comes from lactoferrin only.
- Routing signals: both have C-terminal PTS1-like motifs (A. flavus: SKL; C. utilis: TKL). Both are annotated by UniProt as microbody targeting signals. In a secretion-signal context (amyB SP), both are outcompeted by the N-terminal ER-targeting signal. Same risk level (MODERATE, verify in vivo) for both variants.

#### comp-011 vs. Huynh 2020 adalimumab (engineering feasibility axis)

| Dimension | OE pair (*C. utilis* uricase + lactoferrin) | Huynh 2020 (adalimumab HC + LC) |
|---|---|---|
| Protein origins | Yeast (uricase) + Mammalian (Lf) | Mammalian + Mammalian |
| Total disulfides | 17 (all on Lf) | 16 (8 per chain) |
| Free cysteines | 4 (from C. utilis uricase) | 0 |
| Glycosylation sites (N-X-S/T) | 4 | 2 (Fc N297 ×2) |
| Codon burden | HEAVY (uricase) + LOW (Lf) | HEAVY + HEAVY |
| Host strain | NSlD-ΔP10 (recommended) | NSlD-ΔP10 (required) |
| Architecture | AmyB-KRGGG-Lf + direct-secretion uricase | AmyB-KRGGG-HC + AmyB-KRGGG-LC |
| Achieved/target titer | 500 mg/L (Lf target) / 100 mg/L (uricase target) | 39.7 mg/L (achieved) |

**Where OE (*C. utilis*) is EASIER than Huynh:**

- C. utilis uricase has 0 annotated disulfide bonds — no PDI load from the uricase cassette. Adalimumab both chains are disulfide-rich. C. utilis uricase cassette is structurally simpler for folding.

**Where OE (*C. utilis*) is HARDER than Huynh:**

- Codon burden: C. utilis uricase is AT-biased (GC~42%) in an A. oryzae host (GC~54%). Full codon optimization is required — same as human lactoferrin and both adalimumab chains. In comp-010 (A. flavus), the uricase cassette had LOW codon burden, making one of the two cassettes effectively optimization-free. With C. utilis, BOTH cassettes require full optimization.
- OE Lf titer target (500 mg/L) is 12.6x the Huynh 2020 adalimumab titer (39.7 mg/L). However, Ward 1995 submerged Lf achieved >2 g/L — so the Huynh adalimumab titer reflects antibody-specific constraints, not the maximum capacity of the Lf + A. oryzae system. 500 mg/L is within Ward 1995 validated Lf range with strain improvement.
- Solid-state format: OE primary target is solid-state rice koji, not submerged. Huynh 2020 was submerged only. Solid-state adds format-translation risk (Sun 2024 caveat).
- Free cysteines: C. utilis uricase has 4 free Cys (0 annotated disulfides). Adalimumab has all cysteines paired in disulfides. Free cysteines in the oxidizing ER lumen pose an aggregation risk not present in the Huynh 2020 system.

**Where OE (*C. utilis*) is COMPARABLE to Huynh:**

- Both OE and Huynh use the same NSlD-ΔP10 protease-deletion host. Both require KRGGG linker KEX2 processing for lactoferrin. Both target dual loci (niaD + sC or equivalent).
- Lactoferrin (human, glycosylated, high disulfide) is mechanistically similar to adalimumab heavy chain. Huynh 2020 demonstrated A. oryzae ER can handle mammalian-origin heavily-disulfided proteins.

---

## 4. Platform Decision Implication

comp-010 (A. flavus): LOW cassette-design risk. comp-011 (C. utilis): MODERATE cassette-design risk. The delta is driven by (a) codon burden (HEAVY for C. utilis vs. LOW for A. flavus — codon optimization required, resolves with gene synthesis), (b) free cysteine risk (4 Cys in C. utilis vs. 0 in A. flavus — new risk factor requiring SDS-PAGE monitoring), and (c) 2 vs. 1 KEX2 internal sites (non-load-bearing in direct-secretion design). None of these differences are BLOCKING for the architecture — they are all manageable with standard gene synthesis and SDS-PAGE QC. The MODERATE vs. LOW risk difference reflects more design work required for C. utilis, not a fundamental incompatibility. If adopting C. utilis: (1) full codon optimization is mandatory (same as lactoferrin), (2) add non-reducing SDS-PAGE to the QC panel to catch free-Cys aggregation, (3) note that the ALLN-346 ProteinGPS mutations (US10815461B2) are available to layer on top of the P78609 backbone for protease-resistance improvement.

---

## 5. Design Recommendations for §1.9

1. **If adopting *C. utilis* uricase (industry-preferred track):**
   - Full codon optimization for *A. oryzae* is MANDATORY — same as lactoferrin. Order from gene synthesis vendor (Twist, IDT) with *A. oryzae* codon optimization.
   - Add non-reducing SDS-PAGE to the QC panel to detect free-Cys-driven aggregation. If aggregation bands appear, identify solvent-exposed Cys residues by AlphaFold2 pLDDT and engineer Cys→Ser mutations.
   - Layer ALLN-346 ProteinGPS mutations (US10815461B2: I180V, V190G, Y165F, E51K, Q244K, I132R, A87G) on top of P78609 to improve protease resistance in the gut lumen. These are publicly disclosed — freedom-to-operate for research use.
   - Cassette architecture: direct-secretion (PTEF1-amyB_SP-P78609-TgpdA), NOT a glucoamylase-KEX2 fusion. This avoids the 2 internal KR site risk entirely.

2. **If keeping *A. flavus* uricase (comp-010-verified track):**
   - comp-010 verdict stands: LOW cassette-design risk. No additional design requirements.
   - Codon optimization: optional but low-priority for gene synthesis.
   - Recommended if: (a) speed-to-first-clone is the priority, (b) rasburicase-derivative IP strategy is preferred, (c) no budget for second codon-optimized gene synthesis.

3. **Recommended §1.9 approach — empirical head-to-head:**
   - Order BOTH A. flavus (Q00511, codon-optimized) AND C. utilis (P78609, codon-optimized + ALLN-346 mutations) as direct-secretion cassettes. Run them in parallel in the same §1.9 solid-state koji experiment. Total cost delta: ~$200–400 for the second codon-optimized gene. The empirical comparison resolves the A. flavus vs. C. utilis platform decision at $0 additional fermentation cost (same experiment, two strains).

4. **Lactoferrin cassette architecture (unchanged from comp-010):** PamyB — glucoamylase — KRGGG — hLf (codon-optimized) — TamyB. Monitor for KEX2 internal site truncation by SDS-PAGE (1 moderate-risk site at position 579, P1'=K).

5. **Host strain:** NSlD-ΔP10 (10-protease-deletion *A. oryzae* derivative) — same as comp-010. Required.

6. **Selection markers:** pyrG for Lf cassette (niaD locus per Huynh 2020); niaD or amdS for uricase cassette (sC or amyC locus). NSAR1 platform (Oikawa 2020) provides 5 marker slots; 2-cassette design fits with room to spare.

---

## 6. Limitations

1. **Protein-sequence-level CAI proxy, not CDS analysis.** Codon usage analysis uses amino acid composition + origin-organism preferred codons as a proxy. Actual rare-codon burden depends on the specific CDS sequence. This analysis provides an upper-bound (worst-case) estimate. A gene-synthesis provider's codon optimizer will solve this problem automatically.

2. **C. utilis codon preferences estimated from Kazusa database (genome-wide average, Ascomycete).** A C. utilis-specific highly-expressed secreted-gene table is not available in the public literature. The AT-bias of C. utilis coding sequences is documented and well-established; the specific RSCU values used are approximate (±15-20% error on individual codons).

3. **KEX2 P1' rules are S. cerevisiae-derived.** A. oryzae kexB specificity has not been published with a full P1' preference matrix. The P1' rules are inferred by homology from Kex2p family enzymes. Huynh 2020 validates the KRGGG linker in A. oryzae, but internal site processing probabilities are predictions, not measurements.

4. **Free-cysteine ER aggregation risk: no quantitative model.** Whether 4 free cysteines in C. utilis uricase produce detectable aggregation during A. oryzae ER secretion transit is empirically open. The risk is flagged based on the principle that the A. oryzae ER is oxidizing (PDI/ERO1 active) and free thiols can form intermolecular disulfides. Magnitude is unknown without wet-lab data.

5. **P78609 is PE=3 (Inferred from homology).** The protein has not been directly characterized biochemically in C. utilis under this accession. The active-site annotation (T12, C60, W263) is inferred from homology to A. flavus uricase and other characterized uricases. The ALLN-346 engineering work (US10815461B2) provides independent evidence of C. utilis uricase biochemical characterization, but the specific parent sequence used by Allena is not disclosed.

6. **No structural accessibility correction for KEX2 or glycosylation analysis.** Buried KR sites and buried N-X-S/T sequons have lower functional probability than surface-exposed ones. This analysis treats all sites as equally accessible — a conservative overestimate of risk.

7. **Solid-state format is not modeled.** All analyses apply to the molecular sequence and protein folding; solid-state vs. submerged differences are not captured computationally (Sun 2024 caveat).

---

## 7. Cross-References

- [wiki/c-utilis-uricase-cassette-compatibility-computational.md](../../wiki/c-utilis-uricase-cassette-compatibility-computational.md) — Interpretive wiki page for this experiment
- [wiki/uricase-variant-selection.md](../../wiki/uricase-variant-selection.md) — Industry-revealed preference analysis; comp-011 verdict added as subsection
- [wiki/cassette-compatibility-computational.md](../../wiki/cassette-compatibility-computational.md) — comp-010 page (A. flavus baseline)
- [wiki/hypotheses/H01-ward-dual-cassette.md](../../wiki/hypotheses/H01-ward-dual-cassette.md) — Falsification Card; comp-011 is design support for §1.9
- [wiki/koji-endgame-strain.md](../../wiki/koji-endgame-strain.md) — Protocol sketch for §1.9
- [wiki/validation-experiments.md](../../wiki/validation-experiments.md) — §1.9 wet-lab experiment this analysis informs
- [experiments/comp-010-cassette-compatibility/](../comp-010-cassette-compatibility/) — A. flavus uricase baseline (comp-010: LOW risk)
- [experiments/comp-001-uricase-shio-koji-protease-stability/](../comp-001-uricase-shio-koji-protease-stability/) — A. flavus uricase protease stability (LOW risk)
- [experiments/comp-005-lactoferrin-shio-koji-protease-stability/](../comp-005-lactoferrin-shio-koji-protease-stability/) — Lactoferrin protease stability (MODERATE mature)

---

*Evidence level for all findings in this analysis: Mechanistic Extrapolation — in silico sequence analysis only. Wet-lab confirmation required for all design recommendations.*
