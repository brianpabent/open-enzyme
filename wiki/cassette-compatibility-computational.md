---
title: "Cassette Compatibility — Dual-Cassette Koji Endgame Strain (Computational, comp-010)"
date: 2026-05-05
tags:
  - computational
  - dual-cassette
  - uricase
  - lactoferrin
  - ward-1995
  - kex2
  - codon-usage
  - aspergillus-oryzae
  - cassette-design
  - endgame-strain
  - koji
related:
  - computational-experiments.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - hypotheses/H01-ward-dual-cassette.md
  - uricase-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - lactoferrin.md
  - uricase-variant-selection.md
sources:
  - "Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791)"
  - "Huynh HH, Morita N, Sakamoto T, et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131)"
  - "Rockwell NC, Krysan DJ, Komiyama T, Fuller RS. Chem Rev 2002;102(12):4525-48 (PMID 12475198)"
  - "Brenner C, Fuller RS. Proc Natl Acad Sci 1992;89:922-6 (PMID 1371243)"
  - "Almond MH et al. (2012) PMID 23012214 — fungal-glycan Lf immunogenicity"
  - "Sun XL, Baker HM, Shewry SC, Jameson GB, Baker EN. Acta Crystallogr D Biol Crystallogr 1999;55(Pt 2):403-7 (PMID 10089347)"
status: complete
---

# Cassette Compatibility — Computational Analysis (comp-010)

## 1. Question

Does the uricase (Q00511) + lactoferrin (P02788) payload pair have any cassette-design-specific issues — codon collisions, KEX2 site geometry problems, or secretion-pathway burden — that the Ward 1995 glucoamylase-KEX2 fusion architecture will not handle out of the box in *A. oryzae*?

This question sits between the [Killshot #1 literature audit](./hypotheses/H01-ward-dual-cassette.md) (which confirmed the dual-cassette Ward architecture is precedented in *A. oryzae* submerged culture) and [§1.9 of validation-experiments.md](./validation-experiments.md) (the first wet-lab feasibility test). comp-010 is design support — not a killshot, not a replacement for §1.9. It asks whether there are any sequence-level landmines in the proposed payload pair that should be designed around *before* gene synthesis begins.

---

## 2. Verdict

**Overall cassette-design risk: LOW** (Mechanistic Extrapolation; in silico only)

No blocking cassette-design issues identified for the proposed asymmetric architecture — direct-secretion for uricase, glucoamylase-KEX2 fusion for lactoferrin. The payload pair is architecturally compatible with the Ward 1995 / Huynh 2020 design as-is, with two actionable design notes and one informational finding.

**Design notes (not blocking, but act before gene synthesis):**

1. **Lactoferrin KEX2 internal sites:** One moderate-risk internal K-R dipeptide at mature position 579 (P1'=K — cleavage reduced but possible). One non-functional site at mature position 38 (P1'=D — cleavage abolished). Monitor by SDS-PAGE in §1.9.
2. **Uricase C-terminal SKL motif:** Resembles a peroxisomal PTS1 signal. Unlikely to override the amyB secretion signal in the fusion context, but verify by ELISA fractionation vs. subcellular localization in §1.9.

**Informational finding (not load-bearing for proposed architecture):**

- Uricase contains one high-risk internal K-R site at residue 128 (P1'=N). This is irrelevant for the proposed direct-secretion cassette design but would require attention if uricase is later moved to a glucoamylase-KEX2 fusion.

---

## 3. Why This Matters

The [koji endgame strain](./koji-endgame-strain.md) thesis requires two heterologous expression cassettes co-integrated in *A. oryzae*. Both payloads are validated independently:

- **Uricase:** *A. flavus uaZ* expressed in *S. cerevisiae* = rasburicase (FDA 2001); parent gene well-characterized.
- **Lactoferrin:** Human hLf expressed in *A. awamori* at >2 g/L (Ward 1995); correct fold confirmed at 2.2 Å (Sun 1999).

But combining them in the same strain introduces payload-pair-specific risks that the individual precedents don't resolve: Will a KEX2 site in one payload cause aberrant cleavage of the other's fusion? Does the combined disulfide load saturate ER folding? Does the human-origin lactoferrin require extensive codon optimization that blocks expression?

comp-010 computes these risks from sequence alone before committing ~$600–1,000 to gene synthesis. If a blocking design issue had been found, it would restructure §1.9 before the first dollar is spent on gene synthesis. No blocking issue was found — the experiment proceeds as designed.

---

## 4. Method Summary

Seven analyses run on the protein sequences (Python stdlib only; reproducible):

| Analysis | Method | Inputs |
|---|---|---|
| Codon usage | CAI proxy (geometric mean RSCU of origin-preferred codons vs. A. oryzae table); rare-codon hotspot scan (≥3 consecutive RSCU < 0.4) | Q00511.fasta, P02788.fasta, a_oryzae_codon_usage.json |
| KEX2 geometry | Internal K-R dipeptide census; P1' residue scoring vs. canonical Kex2p preference rules | Q00511.fasta, P02788.fasta, kex2_site_specs.json |
| Secretion targeting | C-terminal KDEL/HDEL scan (ER retention); C-terminal SKL family (PTS1); N-terminal R/K-L-x5-H/Q (PTS2) | Q00511.fasta, P02788.fasta |
| Disulfide load | Cysteine count + UniProt-annotated disulfide bonds; folding load index = N_SS / 16 (Huynh 2020 baseline) | Sequence + UniProt annotations |
| N-glycosylation | N-X-S/T sequon scan (X ≠ P); cross-reference to UniProt annotations | Q00511.fasta, P02788.fasta |
| Combined burden | Synthesis of analyses 1–5; concurrent-load risk for the dual-cassette scenario | All above |
| Huynh 2020 comparison | Dimension-by-dimension comparison vs. adalimumab HC + LC (PMC7257131) | Literature; above outputs |

All evidence level: **Mechanistic Extrapolation** (in silico).

---

## 5. Key Results

### 5.1 Codon Usage

| Protein | Origin | Burden label | CAI proxy | Rare-codon hotspots |
|---|---|---|---|---|
| Uricase Q00511 | *A. flavus* (fungal) | **LOW** | 1.51 | 0 |
| Lactoferrin P02788 | *Homo sapiens* (mammalian) | **LOW** (proxy) | 1.45 | 0 |

The amino-acid-level proxy scores both LOW because human and *A. flavus* preferred codons broadly overlap *A. oryzae* preferences at this resolution. This is a known methodological artifact — at the actual CDS level, human cDNA uses AU-rich 3rd-position synonyms that *A. oryzae* disfavors. **Standard practice for mammalian-origin genes in *Aspergillus*: full gene synthesis with *A. oryzae* codon optimization.** This is not optional for lactoferrin; it is the expected gene-synthesis workflow regardless of this proxy result. Uricase (fungal origin) requires minimal or no codon optimization.

### 5.2 KEX2 Site Geometry

| Protein | Internal K-R sites | High-risk (P1' preferred) | Moderate-risk | Low-risk (P1'=D/E) | Overall |
|---|---|---|---|---|---|
| Uricase Q00511 | 1 | 1 (pos 128, P1'=N) | 0 | 0 | HIGH — but not load-bearing (direct-secretion design) |
| Lactoferrin P02788 | 2 | 0 | 1 (pos 579, P1'=K) | 1 (pos 38, P1'=D) | **MODERATE** |

**Uricase K-R site note.** Residue 128 (K128-R129-N130) is a canonical KEX2 recognition sequence with preferred P1' context. If uricase were in a glucoamylase-KEX2 fusion, this site would be cleaved — producing a 128-aa truncated fragment (N-lobe) and a 174-aa C-terminal fragment. However, the §1.9 design puts uricase on a **direct-secretion cassette** (PTEF1-amyB_SP-uaZ-TgpdA) — no glucoamylase fusion, no KEX2 processing step, no internal-site risk. This finding is actionable only if uricase is ever moved to a fusion architecture.

**Lactoferrin K-R site note.** Two sites in the mature protein (post-signal-peptide):
- Position 38 (K56-R57-D58 in full sequence): P1'=D — KEX2 cleavage **abolished** by acidic residue. Non-functional site.
- Position 579 (K597-R598-K599 in full sequence): P1'=K — KEX2 cleavage **reduced** (~2–3× below baseline rate). Monitor by SDS-PAGE for minor truncated species (~67 kDa). If truncation is visible, mutate K597→Q597 (conservative, preserves charge environment without introducing K-R dipeptide).

### 5.3 Secretion Targeting

| Protein | Issues | Routing risk |
|---|---|---|
| Uricase Q00511 | C-terminal SKL (resembles PTS1 peroxisomal signal) | MODERATE — verify in vivo |
| Lactoferrin P02788 | None | **LOW** |

Uricase (*A. flavus uaZ*) ends in ...SKL — a canonical PTS1 peroxisomal targeting signal in fungi. However, PTS1 targeting requires the protein to lack an N-terminal secretion signal; in the §1.9 design, uricase is expressed with the amyB signal peptide, which should route it into the ER secretory pathway and override PTS1 routing. Verify by anti-uricase ELISA on secreted fraction vs. cell lysate in §1.9. If peroxisomal misrouting is confirmed (uricase in cell lysate only, absent from culture supernatant), append a short C-terminal tag (3× Ala or Gly) to mask the PTS1 signal.

### 5.4 Disulfide Load

| Protein | Cysteines | Disulfides (UniProt) | Folding load (vs. Huynh = 1.00) | Fold risk |
|---|---|---|---|---|
| Uricase Q00511 | 3 | **0** | 0.00× | VERY LOW |
| Lactoferrin P02788 | 33 | **17** | 1.06× | MODERATE |
| Combined | 36 | **17** | **1.06×** | — |

Uricase is a disulfide-free enzyme — all three cysteine residues in the *A. flavus* sequence are free thiols, consistent with the intracellular homotetramer biology (no ER oxidative machinery required). This means the ER PDI/ERO1 burden of the dual-cassette strain is entirely attributable to lactoferrin.

Lactoferrin's 17 disulfides (1.06× Huynh 2020 adalimumab baseline) fall within the demonstrated capacity of the *A. oryzae* NSlD-ΔP10 ER folding machinery. Huynh 2020 achieved 39.7 mg/L functional full-length adalimumab (16 disulfides, two chains) — confirming that this host's ER can correctly fold ~16–17 disulfide bonds simultaneously in a secreted mammalian-origin glycoprotein. Lactoferrin's 17 disulfides are concentrated in a single chain rather than split across two, which slightly increases the per-chain folding complexity but does not change the total oxidative load.

### 5.5 N-Glycosylation

| Protein | N-X-S/T sites predicted | UniProt-annotated | Comments |
|---|---|---|---|
| Uricase Q00511 | 1 (NFS at pos 191) | 0 | NFS likely unoccupied (fungal intracellular enzyme; no glycosylation documented) |
| Lactoferrin P02788 | 3 (NWT at pos 137, NQT at pos 478, NGS at pos 623) | 3 (N137, N478, N623) | All three predicted sites confirmed by UniProt; match Sun 1999 crystal structure |

All three lactoferrin glycosylation sites are correctly predicted by the N-X-S/T scanner and confirmed by UniProt annotation. *A. oryzae* will produce high-mannose fungal N-glycans at these sites rather than the complex sialylated/fucosylated glycans of native milk lactoferrin. This difference has been characterized: recombinant *Aspergillus*-produced hLf with fungal glycans is ~40× less immunogenic and ~200× less allergenic than native milk hLf in BALB/c mice (Almond 2012, PMID 23012214) — and the Sun 1999 2.2 Å crystal structure confirmed the native fold is preserved with fungal glycans in *A. awamori*-produced Lf. Glycan divergence is likely a **feature** for the chronic oral dosing use case, not a concern.

### 5.6 Combined Secretion-Pathway Burden

| Axis | Uricase | Lactoferrin | Combined | Huynh 2020 baseline |
|---|---|---|---|---|
| Disulfides | 0 | 17 | **17** | 16 |
| N-glycosylation | ~0 (unoccupied) | 3 | **3** | 2 |
| Codon burden | LOW (fungal) | LOW (proxy) / full-opt in practice | — | HEAVY (both mammalian) |
| Folding load index | 0.00 | 1.06 | **1.06×** | 1.00 |

**OE dual-cassette burden is essentially equal to or slightly below the Huynh 2020 adalimumab precedent.** Uricase contributes zero disulfide load (unlike adalimumab light chain which contributed 4–6 of the 16 disulfides). The combined glycosylation is 3 sites (slightly above Huynh's 2 Fc sites). Overall: the ER processing machinery faces a comparable or lighter folding load than it handled for adalimumab at 39.7 mg/L.

### 5.7 Huynh 2020 Baseline Comparison

| Dimension | OE pair | Huynh 2020 adalimumab |
|---|---|---|
| Protein origins | Fungal + Mammalian | Mammalian + Mammalian |
| Total disulfides | 17 (all on Lf) | 16 (8 per chain) |
| Glycosylation sites | 3 (Lf only) | 2 (Fc N297 ×2) |
| Host strain | NSlD-ΔP10 (recommended) | NSlD-ΔP10 (required) |
| Architecture | AmyB-KRGGG-Lf + direct uricase | AmyB-KRGGG-HC + AmyB-KRGGG-LC |
| Titer (achieved / target) | Target: 500 mg/L Lf + 100 mg/L uricase | Achieved: 39.7 mg/L |

**Easier than Huynh:**
- Uricase (fungal origin) requires no codon optimization. Both adalimumab chains were human-origin and required full optimization.
- Uricase contributes zero disulfide load. Adalimumab light chain added ~4–6 disulfides to the combined ER load.

**Harder than Huynh:**
- The H01 Lf target (500 mg/L) is 12.6× the Huynh 2020 adalimumab titer (39.7 mg/L). However, the correct benchmark for lactoferrin is Ward 1995 (>2 g/L, *A. awamori* submerged with strain improvement) — not the Huynh antibody titer, which reflects antibody-specific dual-chain assembly constraints. 500 mg/L is well within the Ward 1995 demonstrated range for this exact protein class.
- Solid-state format (primary OE target) adds format-translation risk. Huynh 2020 was submerged only. This is the dominant unresolved risk — not addressed by comp-010 (in silico) and remains load-bearing for §1.9.

**Comparable to Huynh:**
- Same NSlD-ΔP10 host, same KRGGG linker KEX2 architecture, same dual-locus integration strategy.
- Lactoferrin's per-chain disulfide complexity (~17 SS bonds in one chain) is analogous to adalimumab heavy chain's disulfide density in the Huynh 2020 system.

---

## 6. Design Recommendations for §1.9

1. **Host strain:** NSlD-ΔP10 (default, per H01 Killshot #1 findings). Wild-type RIB40 is insufficient.

2. **Uricase cassette:** Direct-secretion design (PTEF1 or PamyB :: amyB signal peptide :: *uaZ* :: TgpdA). Do NOT use glucoamylase-KEX2 fusion for uricase (internal KR128 site would cause truncation). Codon optimization optional but not required.

3. **Lactoferrin cassette:** Ward 1995 / Huynh 2020 exact design (PamyB :: glucoamylase :: KRGGG :: hLf (A. oryzae codon-optimized) :: TamyB). **Full codon optimization mandatory** — order as codon-optimized synthetic gene from Twist or IDT, specifying *A. oryzae* or high-GC fungal optimization.

4. **Monitor Lf KEX2 site (pos 579):** Run SDS-PAGE on secreted fraction; a ~67 kDa band indicates truncation at K579-R580. If seen: mutate K597→Q (full-sequence position) in the codon-optimized gene design.

5. **Monitor uricase routing (C-terminal SKL):** Confirm uricase is in the secreted fraction (anti-uricase ELISA on culture supernatant). If primarily intracellular, add C-terminal 3×Ala linker to mask PTS1.

6. **Iron supplementation:** FeCl₃ or iron citrate at 10–50 ppm added to rice substrate. Rice grain bioavailable iron (~1–3 ppm) may be insufficient for high-titer Lf folding; Ward 1995 used defined iron supplementation in submerged culture.

7. **Submerged parallel control:** Run solid-state koji and submerged DPY in parallel. Solid-state format risk is the load-bearing unresolved question; the parallel control isolates format-specific failure modes from architecture-specific ones.

---

## 7. Limitations

1. **Amino-acid-level CAI proxy, not CDS analysis.** Codon burden scores reflect residue-level analysis only. At CDS level, human cDNA uses synonymous codons that *A. oryzae* disfavors — lactoferrin requires full gene synthesis with codon optimization regardless of the LOW proxy score. This is a methodological floor, not a green light.

2. **KEX2 P1' rules are S. cerevisiae-derived.** *A. oryzae* kexB specificity is not independently published with a full P1' matrix. Rules are inferred from Kex2p family homology. The KRGGG linker validation in *A. oryzae* (Huynh 2020) is the strongest available evidence for internal-site risk estimation.

3. **No structural accessibility correction for KEX2 sites.** Internal KR sites buried in high-pLDDT domains have lower cleavage probability. This analysis assumes all KR sites are equally accessible — a conservative (worst-case) estimate. The lactoferrin moderate-risk site (pos 579) is in the C-lobe; if it is buried (high pLDDT in AF model), actual cleavage risk is lower than scored here.

4. **No quantitative ER capacity model.** Whether simultaneous expression of both cassettes at target titers (500 mg/L Lf + 100 mg/L uricase) saturates *A. oryzae* ER folding machinery (BiP, PDI, ERO1) is empirically unknown. No published quantitative model exists for dual-heterologous-protein secretion in *A. oryzae*.

5. **Solid-state format not modeled.** All sequence-level findings apply equally to submerged and solid-state formats. The Sun 2024 caveat (some proteins fail to secrete in solid-state despite secreting in submerged) is a format risk, not a sequence risk — comp-010 cannot resolve it.

6. **Codon table represents genome-wide average, not secreted-protein-specific preferences.** RSCU estimates carry ~±15% error relative to highly-expressed secreted gene preferences.

---

## 8. Impact on §1.9 Priority

comp-010 does **not** reframe §1.9 as a confirmation experiment. §1.9 remains a **feasibility gate** — the primary open question is the solid-state format translation, which is a wet-lab question that no sequence-level analysis can answer. What comp-010 does:

- **Removes cassette architecture as a pre-experiment concern.** No blocking sequence-level issues mean the §1.9 design (direct secretion uricase + glucoamylase-KEX2 lactoferrin in NSlD-ΔP10) can proceed as specified without redesign.
- **Provides two actionable design notes** (KEX2 site 579 monitoring; C-terminal SKL verification) that should be built into the §1.9 readout plan before wet-lab starts.
- **Anchors the Huynh 2020 titer comparison.** The 12.6× titer gap vs. Huynh adalimumab is not the correct benchmark for Lf — Ward 1995 >2 g/L Lf is. The Huynh baseline is relevant for confirming ER folding capacity; it is not a ceiling for Lf titer.

---

## 9. Cross-References

- [hypotheses/H01-ward-dual-cassette.md](./hypotheses/H01-ward-dual-cassette.md) — Falsification Card; comp-010 adds a cross-reference note in the Killshot #1 Findings section
- [koji-endgame-strain.md §3.4](./koji-endgame-strain.md) — Protocol sketch for §1.9; design recommendations above are consistent with and elaborated from this section
- [validation-experiments.md §1.9](./validation-experiments.md) — The wet-lab experiment this analysis informs
- [computational-experiments.md](./computational-experiments.md) — comp-010 tracking entry
- [uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md) — comp-001: uricase shio-koji protease stability (LOW risk)
- [lactoferrin-protease-stability-computational.md](./lactoferrin-protease-stability-computational.md) — comp-005: lactoferrin shio-koji protease stability (MODERATE mature)
- [experiments/comp-010-cassette-compatibility/](../experiments/comp-010-cassette-compatibility/) — Reproducible experiment folder

---

*All findings in this analysis are Mechanistic Extrapolation — in silico sequence analysis. Wet-lab confirmation required for all design recommendations.*
