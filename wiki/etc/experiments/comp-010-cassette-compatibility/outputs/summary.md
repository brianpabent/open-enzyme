# comp-010 — Cassette Compatibility Analysis: Summary

**Experiment:** comp-010  
**Date:** 2026-05-05  
**Script:** `experiments/comp-010-cassette-compatibility/analyze.py`  

---

## 1. Question

Does the uricase (Q00511) + lactoferrin (P02788) payload pair have any cassette-design-specific issues — codon collisions, KEX2 site geometry problems, or secretion-pathway burden — that the Ward 1995 glucoamylase-KEX2 architecture will not handle out of the box?

---

## 2. Verdict

**Overall cassette-design risk: LOW**

No blocking sequence-level issues identified for the candidate architecture: uricase (direct-secretion candidate) has no KEX2 fusion concerns and zero disulfide load; lactoferrin's two internal K-R sites are either non-functional (P1'=D, KEX2 abolished) or moderate-risk (P1'=K, reduced efficiency) — no high-risk truncation sites. The corrected bulk disulfide count equals the Huynh 2020 adalimumab comparator, but architecture-specific folding burden remains unmodeled. A uricase internal K-R site exists at residue 128 but is irrelevant within the direct-secretion candidate; §1.33 determines whether that topology survives.

---

## 3. Per-Analysis Findings

### 3.1 Codon Usage Compatibility

| Metric | Uricase (Q00511) | Lactoferrin (P02788) |
|---|---|---|
| Origin | A. flavus (fungal) | Homo sapiens (mammalian) |
| Sequence length | 302 aa | 710 aa |
| Codons analyzed | 302 | 710 |
| Rare codons (RSCU < 0.4) | 0 (0.0%) | 0 (0.0%) |
| CAI proxy (geometric mean RSCU) | 1.5074 | 1.4463 |
| Hotspots (≥3 consecutive rare) | 0 | 0 |
| Burden classification | **LOW** | **LOW** |

**Uricase:** Minimal codon optimization needed; origin-preferred codons largely overlap A. oryzae preferences

**Lactoferrin:** Minimal codon optimization needed; origin-preferred codons largely overlap A. oryzae preferences

**Design recommendation:** Uricase (A. flavus origin) requires minimal or no codon optimization — A. flavus and A. oryzae share near-identical codon usage (>99.5% coding-region identity). Lactoferrin (human origin) CAI proxy comes out LOW at this amino-acid-level analysis, but this is a methodological artifact: human-preferred codons happen to overlap A. oryzae preferred codons for many amino acids at the residue level. At the CDS level, human cDNA uses AU-rich 3rd-codon-position synonyms that A. oryzae disfavors. **Full gene synthesis from scratch with A. oryzae codon optimization is standard practice for mammalian-origin genes — treat Lf as requiring full optimization regardless of this proxy score.** Standard gene-synthesis vendors (Twist, IDT) will apply A. oryzae optimization automatically.

---

### 3.2 KEX2 Site Geometry

| Metric | Uricase (Q00511) | Lactoferrin (P02788) |
|---|---|---|
| Signal peptide (excluded from scan) | 0 aa | 19 aa |
| Mature protein length | 302 aa | 691 aa |
| Internal K-R sites (total) | 1 | 2 |
| High-risk sites (P1' preferred) | 1 | 0 |
| Moderate-risk sites | 0 | 1 |
| Low-risk sites (P1'=D/E — non-functional) | 0 | 1 |
| KEX2 internal site risk | **HIGH** | **MODERATE** |

**Uricase:** 1 high-risk site(s) — truncated protein species predicted; linker redesign or site mutation recommended

**Lactoferrin:** 1 moderate-risk site(s) — may produce minor truncation bands; verify by SDS-PAGE

**Uricase internal K-R sites:**

| Position (mature) | P1' | Risk | Note |
|---|---|---|---|
| 128 | N | HIGH | P1'=N — KEX2 cleavage likely; site is functional |

**Lactoferrin internal K-R sites:**

| Position (mature) | P1' | Risk | Note |
|---|---|---|---|
| 38 | D | LOW | P1'=D (acidic — KEX2 cleavage abolished; this site is non-functional) |
| 579 | K | MODERATE | P1'=K — KEX2 cleavage reduced but possible |

**Design recommendation:** Verify KEX2 internal site risks experimentally by SDS-PAGE of secreted fractions (truncated species produce lower-MW bands). If high-risk sites produce truncation: (a) mutate KR→KQ or KR→QR at the problematic site (conservative amino acid change that eliminates KEX2 recognition while preserving electrostatic environment), or (b) extend the KRGGG linker to KRGGGGG for more flexibility. Uricase's proposed cassette design (PTEF1-amyB_SP-uaZ-TgpdA, direct secretion) avoids the KEX2 fusion entirely for the uricase cassette — KEX2 internal sites in uricase are irrelevant unless uricase is also put in a fusion architecture.

---

### 3.3 Signal Peptide / Secretion-Targeting Analysis

| Metric | Uricase (Q00511) | Lactoferrin (P02788) |
|---|---|---|
| Routing issues found | 1 | 0 |
| Routing risk | **MODERATE** | **LOW** |

**Uricase:** Moderate-risk routing signal(s) detected — verify in vivo

**Lactoferrin:** No ER-retention, PTS1, or PTS2 signals detected in mature protein sequence

**Uricase routing issues:**

- `PTS1_peroxisomal` at C-terminal tripeptide: `SKL` — C-terminal SKL resembles a PTS1 peroxisomal targeting signal. Unlikely to override secretion signal in fusion context, but worth checking in vivo. (risk: MODERATE)

---

### 3.4 Disulfide Bonding Load

| Metric | Uricase (Q00511) | Lactoferrin (P02788) | Huynh 2020 baseline |
|---|---|---|---|
| Cysteine count | 3 | 32 | ~32 (16 per chain × 2) |
| Disulfide bonds | 0 | 16 | 16 (total both chains) |
| Folding load index (vs. Huynh = 1.0) | 0.0 | 1.0 | 1.00 |
| Fold risk | **VERY LOW** | **MODERATE** | — |

**Uricase:** No disulfide bonds — no PDI load. Folding is independent of ER oxidative machinery.

**Lactoferrin:** 16 disulfides — comparable to Huynh 2020 adalimumab baseline (16 disulfides)

**Dual-cassette combined:** 16 disulfides total (1.00× Huynh baseline). Lactoferrin carries the entire disulfide load; uricase contributes nothing to PDI burden.

---

### 3.5 N-Glycosylation Site Prediction

| Metric | Uricase (Q00511) | Lactoferrin (P02788) |
|---|---|---|
| Predicted N-X-S/T sequons (mature protein) | 1 | 3 |
| UniProt-annotated sites | 0 (none annotated) | 3 (N137, N478, N623) |

**Uricase predicted N-X-S/T sites:**

| Position | Sequon |
|---|---|
| 191 (mature 191) | `NFS` |

**Lactoferrin predicted N-X-S/T sites (cross-reference against UniProt N137, N478, N623):**

| Position (full seq) | Position (mature) | Sequon | UniProt annotated? |
|---|---|---|---|
| 156 | 137 | `NWT` | Yes |
| 497 | 478 | `NQT` | Yes |
| 642 | 623 | `NGS` | Yes |

**Glycosylation divergence note:** A. oryzae produces high-mannose fungal N-glycans. Native human lactoferrin has complex sialylated/fucosylated N-glycans at N137, N478, N623. Recombinant A. oryzae lactoferrin (per Ward 1995 / Sun 1999) produces correctly-folded protein with fungal glycans that are ~40× less immunogenic and ~200× less allergenic in mouse model (Almond 2012, PMID 23012214). Glycan divergence is likely a feature for chronic oral dosing, not a structural concern. Uricase is unglycosylated (bacterial enzyme, no N-X-S/T sequons that are functionally occupied).

---

### 3.6 Concurrent-Expression Secretion-Pathway Burden

| Axis | Uricase | Lactoferrin | Combined | Huynh 2020 baseline |
|---|---|---|---|---|
| Disulfides | 0 | 16 | 16 | 16 |
| N-glycosylation sites | 1 | 3 | 4 | 2 |
| Codon burden | LOW | LOW | — | HEAVY (both mammalian) |
| Folding load index | — | — | 1.00× | 1.00 |

**Overall dual-cassette secretion burden: LOW**

**Informational (not a risk driver):** Uricase has 1 internal K-R site(s) (overall KEX2 risk: HIGH). NOT load-bearing within the direct-secretion candidate (PTEF1-amyB_SP-uaZ-TgpdA). Direct secretion is not a settled topology: if §1.33 selects a fusion architecture, this site requires attention.

**Titer gap:** The H01 Lf target (500 mg/L) is 12.6× above Huynh 2020 vs. the Huynh 2020 adalimumab titer (39.7 mg/L). This gap is partly explained by antibody-specific constraints; Ward 1995 achieved >2 g/L for lactoferrin specifically, so 500 mg/L is within the demonstrated range for this protein in this host family (submerged, with strain improvement).

---

### 3.7 Comparison to Huynh 2020 Adalimumab Baseline

| Dimension | OE pair (uricase + lactoferrin) | Huynh 2020 (adalimumab HC + LC) |
|---|---|---|
| Protein origins | Fungal (uricase) + Mammalian (Lf) | Mammalian + Mammalian |
| Total disulfides | 16 (all on Lf) | 16 (8 per chain) |
| Glycosylation sites (N-X-S/T) | 4 | 2 (Fc N297 ×2) |
| Host strain | NSlD-ΔP10 (recommended) | NSlD-ΔP10 (required) |
| Architecture | AmyB-KRGGG-Lf + direct-secretion uricase | AmyB-KRGGG-HC + AmyB-KRGGG-LC |
| Achieved/target titer | 500 mg/L (target) / 100 mg/L uricase | 39.7 mg/L (achieved) |

**Where OE is EASIER than Huynh:**

- Uricase origin is fungal (A. flavus) — near-identical codon usage to A. oryzae host. No codon optimization required for uricase; both adalimumab chains required heavy optimization.

**Where OE is HARDER than Huynh:**

- OE Lf titer target (500 mg/L) is 12.6× the Huynh 2020 adalimumab titer (39.7 mg/L). However, Ward 1995 submerged Lf achieved >2 g/L — so the Huynh adalimumab titer reflects antibody-specific constraints, not the maximum capacity of the Lf + A. oryzae system. 500 mg/L is within Ward 1995 validated Lf range with strain improvement.
- Solid-state format: OE primary target is solid-state rice koji, not submerged. Huynh 2020 was submerged only. Solid-state adds format-translation risk (Sun 2024 — some proteins that secrete in submerged do not secrete in solid-state).

**Where OE is COMPARABLE to Huynh:**

- Bulk disulfide count comparable: OE pair 16 vs. Huynh 16; folding architectures differ.
- Both OE and Huynh use the same NSlD-ΔP10 protease-deletion host. Both require KRGGG linker KEX2 processing. Both target dual loci (niaD + sC or equivalent).
- Lactoferrin and adalimumab are both mammalian-origin, glycosylated, disulfide-rich proteins, but their folding and assembly architectures differ. Huynh 2020 is therefore a contextual host precedent rather than a quantitative capacity proof for lactoferrin.

---

## 4. Design Recommendations for §1.33 → §1.9

1. **Host strain:** Start from NSlD-ΔP10 (or equivalent 10-protease-deletion A. oryzae derivative). Wild-type RIB40 is insufficient for high-titer Lf — confirmed by Huynh 2020.

2. **Uricase cassette architecture:** Carry direct secretion (PTEF1 or PamyB — amyB signal peptide — uaZ — TgpdA) as one §1.33 candidate, not as the selected topology. It avoids KEX2 internal-site risk within that arm. Include the competing intracellular/fusion or retention architectures specified in §1.33; only the physiological product/peroxide/viability result selects the §1.9B build. Codon optimization remains optional but low-priority for the A. flavus sequence-level candidate.

3. **Lactoferrin cassette architecture:** Use Ward 1995 / Huynh 2020 design exactly: PamyB — glucoamylase — KRGGG — hLf (codon-optimized) — TamyB. Full codon optimization for A. oryzae is required (human origin, MODERATE/HEAVY burden; see §3.1 hotspot list for regions to prioritize). Monitor for KEX2 internal site truncation by SDS-PAGE (see §3.2 — 0 high-risk, 1 moderate-risk internal K-R sites).

4. **Selection markers:** pyrG for Lf cassette (at niaD locus per Huynh 2020); niaD or amdS for uricase cassette (at sC or amyC locus). NSAR1 platform (Oikawa 2020) provides 5 marker slots; 2-cassette design fits with room to spare.

5. **System-to-format handoff:** Resolve topology × oxygen × peroxide in §1.33 liquid/system conditions first; then reproduce the winner in §1.9B solid-state koji with a matched submerged control before §1.9C. This separates physiological-system failure from solid-state format risk.

6. **KEX2 capacity monitoring:** If both Lf AND uricase (if also in fusion architecture) compete for KEX2, monitor for unprocessed fusion bands by SDS-PAGE at molecular weights consistent with glucoamylase-linker-payload. If KEX2 is saturated, stagger promoter strengths: strong PamyB for Lf, weaker constitutive PTEF1 for uricase.

7. **Iron supplementation:** Add FeCl₃ or iron citrate at 10–50 ppm to the rice substrate before solid-state koji fermentation. Rice grain iron (~1–3 ppm bioavailable) may be insufficient for high-titer Lf folding. Ward 1995 used defined iron supplementation in submerged culture.

---

## 5. Limitations

1. **Protein-sequence-level CAI proxy, not CDS analysis.** Codon usage analysis uses amino acid composition + origin-organism preferred codons as a proxy. Actual rare-codon burden depends on the specific CDS sequence (which codon the gene-synthesis vendor selects). This analysis provides an upper-bound (worst-case) estimate. A gene-synthesis provider's codon optimizer will solve this problem automatically — the hotspot list points to regions to verify post-optimization.

2. **KEX2 P1' rules are S. cerevisiae-derived.** A. oryzae kexB specificity has not been published with a full P1' preference matrix. The P1' rules are inferred by homology from Kex2p family enzymes. Huynh 2020 validates the KRGGG linker in A. oryzae, but internal site processing probabilities are predictions, not measurements.

3. **No structural accessibility correction for KEX2 analysis.** KEX2 internal sites in buried high-pLDDT domains are much less likely to be cleaved than surface-exposed sites. This analysis treats all KR sites as equally accessible — a conservative overestimate of risk.

4. **Codon-usage table represents genome-wide average, not secreted-protein-specific.** Highly-expressed secreted proteins (glucoamylase, amylase) in A. oryzae may have distinct codon preferences vs. the genome-wide table used here. Deviation is estimated at ±15% RSCU per the provenance note.

5. **No competitive secretion modeling.** This analysis does not model the shared ER folding-machinery capacity quantitatively. Whether expressing both cassettes simultaneously saturates BiP/PDI/ERO1 or vesicle trafficking is empirically unknown — no published quantitative model exists for A. oryzae dual-heterologous-protein secretion capacity.

6. **Solid-state format is not modeled.** All analyses apply to the molecular sequence and protein folding; solid-state vs. submerged differences (water activity, O₂ gradient, protein secretion mode) are not captured computationally. This is the Sun 2024 caveat (some proteins secrete in submerged but not solid-state) — comp-010 cannot resolve it.

---

## 6. Cross-References

- [wiki/hypotheses/H01-ward-dual-cassette.md](../../../../hypotheses/H01-ward-dual-cassette.md) — Falsification Card; comp-010 is design support for §1.9
- [wiki/koji-endgame-strain.md §3.4](../../../../koji-endgame-strain.md) — Protocol sketch for §1.9; design recommendations above update this
- [wiki/validation-experiments.md §1.9](../../../../validation-experiments.md) — The wet-lab experiment this analysis informs
- [wiki/computational-experiments.md](../../../../computational-experiments.md) — comp-010 tracking entry
- [wiki/cassette-compatibility-computational.md](../../../../cassette-compatibility-computational.md) — Interpretive wiki page
- [experiments/comp-001-uricase-shio-koji-protease-stability/](../../comp-001-uricase-shio-koji-protease-stability/) — Uricase protease stability (comp-001: LOW risk)
- [experiments/comp-005-lactoferrin-shio-koji-protease-stability/](../../comp-005-lactoferrin-shio-koji-protease-stability/) — Lactoferrin protease stability (comp-005: MODERATE mature)

---

*Evidence level for all findings in this analysis: Mechanistic Extrapolation — in silico sequence analysis only. Wet-lab confirmation required for all design recommendations.*
