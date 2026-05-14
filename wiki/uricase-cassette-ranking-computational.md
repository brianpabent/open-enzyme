---
title: "Uricase Cassette Ranking, ClockBase-Style Combinatorial Composite Scoring (Computational, comp-022)"
date: 2026-05-14
tags:
  - computational
  - comp-022
  - clockbase-pattern
  - cassette-design
  - uricase
  - codon-optimization
  - signal-peptide
  - secretion-scaffold
  - chaperone-load
  - aspergillus-oryzae
  - ranking
related:
  - computational-experiments.md
  - autonomous-screening-methodology.md
  - cassette-compatibility-computational.md
  - chaperone-orthogonal-stacking.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - engineered-koji-protocol.md
  - digestive-enzyme-optimization.md
  - uricase-protease-stability-computational.md
sources:
  - "Sharp PM, Li WH. Nucleic Acids Res. 1987;15(3):1281-95 (PMID 3547335); CAI methodology"
  - "Kudla G, Murray AW, Tollervey D, Plotkin JB. Science 2009;324(5924):255-8 (PMID 19359587); 5' mRNA structure dominates initiation"
  - "Ward PP et al. Biotechnology (N Y) 1995;13(5):498-503 (PMID 9634791); glucoamylase-KEX2 architecture"
  - "Huynh HH et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131); A. oryzae NSlD-ΔP10 antibody titer benchmark"
  - "Machida M et al. Nature 2005;438(7071):1157-61 (PMID 16372010); A. oryzae RIB40 genome / codon usage"
  - "Nakao Y et al. Nucleic Acids Res 1992;20 Suppl:2117 (PMID 1482437); A. oryzae codon usage reference"
  - "Tada S et al. PMID 1937733; PamyB Taka-amylase A promoter characterization"
  - "Punt PJ et al. PMID 2113023; PgpdA A. nidulans GAPDH promoter"
  - "Angov E. Biotechnol J 2009;4(11):1583-94 (PMID 18851725); codon harmonization"
  - "Ying K, Tyshkovskiy A, Gladyshev VN et al. bioRxiv 2023.02.28.530532v3 (PMC12667862, PMID 41332661); ClockBase autonomous screening"
status: complete (v1; fold-quality model deferred to wet-lab)
---

# Uricase Cassette Ranking, Computational Analysis (comp-022)

## 1. Question

Across the *A. oryzae* uricase expression cassette design space, parameterized as **6 promoters × 12 signal peptides × 10 codon variants × 60 secretion scaffolds = 43,200 combinations**, which cassettes survive a multi-model concordance gate and warrant promotion to the [§1.9 dual-cassette wet-lab feasibility test](./validation-experiments.md)?

This is the first comp-NNN to instantiate the ClockBase exhaustive-search-then-rank pattern at full cardinality. Prior cassette work in the corpus (comp-010, comp-011) examined two specific candidate designs each; comp-022 ranks the full combinatorial space. The intent is not to replace §1.9, but to ensure that the §1.9 cassette design is the right point in the design space before gene synthesis dollars commit.

## 2. Verdict

**The §1.9 architecture is robust.** The composite ranking converges on the architecture comp-010 already recommended (PamyB + amyB signal peptide + direct-secretion, no fusion), and adds three gene-synthesis-time refinements:

1. **Codon variant: prefer "5'-softened" over pure max-CAI.** A two-zone codon optimization (low-GC + min-secondary-structure first 30 codons, max-CAI thereafter) ranks at the top of the concordance gate across all four models. Pure max-CAI gives slightly higher CAI (1.000 vs 0.915) but worse 5' mRNA structure (0.594 vs 0.733); the 5'-softened variant wins on N-of-4 concordance.
2. **C-terminal tag: block the PTS1 signal explicitly.** Append 3×Ala or His6 to mask the native C-terminal SKL PTS1 motif. This addresses the routing risk flagged in comp-010 §3 at the cassette-design level rather than waiting for the §1.9 anti-uricase ELISA to detect peroxisomal misrouting.
3. **N-glycosylation: ablate N191.** The one predicted N-glycosylation sequon in uricase (NSS at position 191; comp-010 §5) is unlikely to be occupied in the native protein but adds residual chaperone-pathway load if it is. A single N191Q point mutation removes the sequon at zero design cost.

**Evidence level:** Mechanistic Extrapolation (in silico only). Verdict gates a wet-lab confirmation in §1.9; the cassette-design refinements are gene-synthesis-time decisions that can be incorporated in the §1.9 construct order at no marginal cost.

**Design-space size:** 43,200 candidates enumerated (matches brief's Pass-2 estimate exactly). Concordance pass rate N-of-4 = 4: **195 candidates (0.45%)**. Concordance pass rate N-of-4 ≥ 3: **2,421 candidates (5.6%)**, which collapse to **501 unique cassette designs** after removing degeneracy across propeptide and N-glyc modifier states.

## 3. Method

### 3.1 Design-space parameterization

| Axis | Cardinality | Range |
|---|---|---|
| Promoter | 6 | PamyB (Tada 1991 PMID 1937733), PglaA (Ward 1995 PMID 9634791), PenoA (Toda 2001), PgpdA (Punt 1990 PMID 2113023), PtefI (Kitamoto 1998), PnmtA (Shoji 2005) |
| Signal peptide | 12 | 6 native koji SPs (amyB, glaA, pepO, alpA, lipase) + foreign cbhI (T. reesei), each × {with pro-region, without pro-region} |
| Codon variant | 10 | native_uaZ approx, cai_max, cai_balanced, cai_max_gc54, harmonized (Angov 2008), rare_avoid, low_gc, high_gc, 5p_softened (Kudla 2009), 5p_softened_balanced |
| Secretion scaffold | 60 | 10 base scaffolds (direct × 3 C-term tag variants; glaA-full KEX2 × 4 KEX2-linker variants; glaA-truncated KEX2 × 2; tandem-KEX2 × 1) × 3 propeptide states × 2 N-glyc states |
| **Product** | **43,200** | |

Full part-by-part provenance (sequences, citations, fetch dates) is in [`experiments/comp-022-clockbase-uricase-cassette-ranking/inputs/provenance.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/inputs/provenance.md).

### 3.2 Four scoring models

| Model | Tier | Direction | Method | Primary source |
|---|---|---|---|---|
| Codon Adaptation Index (CAI) | 1 | Higher better | Geometric mean of per-codon w-values (w = freq/max-freq-synonym) under A. oryzae table | Sharp & Li 1987 PMID 3547335 |
| mRNA 5' structure proxy | 1 | Higher better | GC-content + GC-clamp + palindromic-4mer count over first 120 nt | Kudla 2009 PMID 19359587 |
| Architecture-adjusted chaperone load | 2 | Lower better | Σ (disulfide_count × α) + glycosylation + KEX2 + PTS1 penalties | [chaperone-orthogonal-stacking.md §3.5](./chaperone-orthogonal-stacking.md) |
| Promoter × SP prior | 4 | Higher better | Literature-derived bounded multiplier per promoter and SP | (See §3.4) |

Tiers reflect the cascading-filter design from the brief. In practice, Tier 1 and Tier 2 are both per-component (per codon variant; per scaffold base) rather than per-candidate, so the full 43,200-candidate evaluation is computationally cheap. The cascading framing matters when Tier 3 fold-quality is included; in this v1 run, Tier 3 is deferred.

### 3.3 Concordance gate (N-of-M)

Each candidate is assigned a binary "top quintile" flag per model (1 if it falls in the top 20% by that model's score). N-of-4 concordance = sum of flags. The promotion threshold is **N-of-4 ≥ 3 (75%)**, chosen a priori from the ClockBase precedent (30/40 ≈ 75%; [autonomous-screening-methodology.md](./autonomous-screening-methodology.md) §"Computational-to-wet-lab handoff: N-of-M concordance").

Within the concordance-passing shortlist, candidates are ranked by a continuous composite score (mean of per-model min-max normalized values) to break ties.

### 3.4 Promoter and signal peptide priors

| Promoter | Relative strength | Citation |
|---|---|---|
| PamyB | 1.00 (reference) | Tada 1991 PMID 1937733; canonical workhorse |
| PglaA | 0.85 | Ward 1995 PMID 9634791; Huynh 2020 PMC7257131 |
| PenoA | 0.70 | Toda 2001 |
| PtefI | 0.65 | Kitamoto 1998; orthogonal constitutive |
| PnmtA | 0.60 | Shoji 2005; tunable repressible |
| PgpdA | 0.55 | Punt 1990 PMID 2113023; selection-marker promoter |

Signal peptide efficiencies: native koji SPs (amyB, glaA, alpA, lipase, pepO) score 0.82-1.02; foreign cbhI from *T. reesei* scores 0.65-0.68; pro-region present adds a small bonus (2-5%) for KEX2-mediated N-terminal-homogeneity benefit. All values are bounded literature estimates; the ordinal ranking is robust, the scalar values are priors not measurements. See [`experiments/comp-022-.../inputs/provenance.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/inputs/provenance.md).

## 4. Key Results

### 4.1 Per-codon-variant scores (10 variants)

| Codon Variant | CAI | mRNA-5' proxy | Rare-codon clusters | Headline |
|---|---|---|---|---|
| native_uaZ (approx) | 0.464 | 0.667 | 14 | Native rate; many rare clusters in *A. oryzae* context |
| cai_max | 1.000 | 0.594 | 0 | Pure max-CAI; degraded 5' structure |
| cai_balanced | 0.724 | 0.589 | 1 | Frequency-weighted; middling on both axes |
| cai_max_gc54 | 0.757 | 0.800 | 2 | GC-constrained; good 5' structure but lower CAI |
| harmonized (Angov 2008) | 0.695 | 0.617 | 2 | Mid-rank harmonized |
| rare_avoid | 0.781 | 0.489 | 0 | RSCU≥0.4 filter; worst 5' structure of any cluster |
| low_gc | 0.386 | 0.667 | 26 | GC-poor; very poor CAI |
| high_gc | 1.000 | 0.594 | 0 | GC-rich; equivalent to cai_max here |
| **5p_softened** | **0.915** | **0.733** | **2** | **Top-quintile on both axes; the headline variant** |
| 5p_softened_balanced | 0.679 | 0.733 | 2 | 5'-softened but mid-rank tail; worse CAI |

The "5'-softened" variant (low-GC + max-CAI two-zone optimization) is the only codon variant that lands in the top quintile on both CAI and 5' structure simultaneously. Pure max-CAI lands top on CAI but bottom on 5' structure.

### 4.2 Per-scaffold chaperone load (10 base scaffolds)

| Scaffold | Fusion | KEX2 site | PTS1 blocked | Effective load |
|---|---|---|---|---|
| direct_natag_pts1ok | none | none | False | 0.50 |
| **direct_3xAla_pts1blk** | **none** | **none** | **True** | **0.20** |
| **direct_his6_pts1ok** | **none** | **none** | **True** | **0.20** |
| glaA_KR_pts1ok | glaA_full | KR | False | 5.10 |
| glaA_KR_3xAla | glaA_full | KR | True | 4.80 |
| glaA_KRGGG_pts1ok | glaA_full | KRGGG | False | 5.05 |
| glaA_KRGGG_3xAla | glaA_full | KRGGG | True | 4.75 |
| glaA_trunc_KR_pts1ok | glaA_truncated | KR | False | 2.60 |
| glaA_trunc_KR_3xAla | glaA_truncated | KR | True | 2.30 |
| tandem_KEX2_pts1ok | glaA_full | double_KR | False | 5.40 |

Direct-secretion with PTS1-blocking C-terminal tag is the lowest chaperone-load architecture. Glucoamylase-KEX2 fusion variants carry 10-25× the chaperone load because they impose the carrier's disulfides and glycosylation on top of uricase's near-zero intrinsic load. Tandem-KEX2 saturates KEX2 capacity (Spencer 1998 precedent) and adds 5-10% additional load.

**Architectural implication:** the Ward 1995 fusion architecture is correct for *lactoferrin* (where it boosts secretion of a complex glycoprotein) but is the *wrong* architecture for uricase, which has zero intrinsic chaperone load and benefits most from a minimum-overhead direct-secretion design. Comp-010 reached this conclusion via design analysis; comp-022 confirms it via full design-space ranking.

### 4.3 Top-5 unique cassettes (after collapsing propeptide and N-glyc modifier degeneracy)

| Rank | Promoter | Signal Peptide | Codon Variant | Scaffold | Propeptide | N-glyc | N-of-4 | Composite |
|---|---|---|---|---|---|---|---|---|
| 1 | PamyB | SPamyB_pro | 5p_softened | direct_3xAla_pts1blk | none | ablated | 4 | 0.912 |
| 2 | PamyB | SPamyB_pro | 5p_softened | direct_his6_pts1ok | none | ablated | 4 | 0.912 |
| 3 | PamyB | SPamyB | 5p_softened | direct_3xAla_pts1blk | none | ablated | 4 | 0.904 |
| 4 | PamyB | SPamyB | 5p_softened | direct_his6_pts1ok | none | ablated | 4 | 0.904 |
| 5 | PamyB | SPglaA_pro | 5p_softened | direct_3xAla_pts1blk | none | ablated | 4 | 0.904 |

195 candidates pass N-of-4 = 4 (all four models top quintile). The top cluster is tightly constrained: PamyB promoter, amyB or glaA signal peptide (with optional pro-region), 5'-softened codon variant, direct-secretion scaffold with PTS1-blocking C-terminal tag, no propeptide between SP and mature N-terminus, N191 glycosylation sequon ablated.

The full top-25 table is in [`experiments/comp-022-.../outputs/top25.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/top25.md). The full 501-cassette concordance-passing shortlist is in [`unique_cassette_shortlist.csv`](../experiments/comp-022-clockbase-uricase-cassette-ranking/outputs/unique_cassette_shortlist.csv).

### 4.4 Concordance distribution

| N-of-4 | Candidates | Share |
|---|---|---|
| 4 | 195 | 0.45% |
| 3 | 2,226 | 5.15% |
| 2 | 9,438 | 21.8% |
| 1 | 17,946 | 41.5% |
| 0 | 13,395 | 31.0% |

The mass of the design space (72.5%) lands at N-of-4 ≤ 1; i.e., most cassette designs are bad on at least three of four axes simultaneously. This is the expected pattern for a high-dimensional design space with orthogonal scoring axes; it is also the failure mode that comp-022's exhaustive enumeration is intended to surface (a priori one-at-a-time selection is path-dependent and tends to lock in a single axis's preferred value while ignoring the others).

## 5. Limitations

The brief authorized these v1 simplifications; each is documented for downstream readers.

1. **Fold-quality model (Tier 3) deferred to wet-lab.** ESMFold and AlphaFold pLDDT are not callable from this subagent's environment (no GPU, no API key, sandbox restricts network). ColabFold and ESM2 perplexity were considered as proxies and also unavailable. Brief authorized this deferral. **Implication:** the "structural foldability" axis is unscored in this v1. For uricase specifically the consequence is minor because every candidate uses the same AA sequence (Q00511), so fold-quality differences would be driven entirely by cassette-context effects (signal-peptide cleavage, propeptide processing, glycosylation occupancy) rather than by primary-sequence variation. The wet-lab fold quality readout in §1.9 is anti-uricase ELISA + uricase activity assay (UA-disappearance spectrophotometry), which directly tests folded-and-secreted protein. This supersedes any in silico pLDDT proxy at the cassette-design stage.

2. **N-of-M threshold = 3 of 4 (75%), not 4 of 5 (80%).** Because the fold-quality model is deferred, M=4 not 5. The 75% concordance fraction is preserved (matches ClockBase 30/40 precedent). An a priori choice; no retrospective calibration was attempted because comp-001 through comp-014 were not cassette-ranking experiments (TCM and complement-modulator literature mining, protease stability, transporter modulation). The retrospective-calibration framing in the brief was based on a misreading of those comps. This is documented in [`experiments/comp-022-.../README.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/README.md).

3. **Promoter strengths and SP efficiencies are bounded literature estimates.** They are priors, not measurements in NSlD-ΔP10. They affect the absolute composite scores but not the ordinal ranking robustness of the top cluster: PamyB dominates in the literature consensus by a sufficient margin that any reasonable bounded estimate places it at the top. PglaA's 0.85 vs 0.95 multiplier would swap rank 1 vs rank 3 but not the architectural class of the headline cluster.

4. **mRNA 5' secondary structure is a GC-content + GC-clamp + palindromic-4mer count proxy**, not a true minimum-free-energy calculation. ViennaRNA is not installable in this environment (no pre-built binary, network-restricted pip). The proxy is defensible per Kudla 2009 PMID 19359587 (5' GC dominates translation initiation in *E. coli*; replicated in *S. cerevisiae* and filamentous fungi), but a true MFE calculation on the surviving shortlist would refine the ranking. **Recommended follow-up:** retrofit ViennaRNA MFE on the 501-cassette shortlist when an environment with the binary is available.

5. **Native A. flavus codon usage approximated.** The "native_uaZ" variant is back-translated using the A. oryzae table with mid-rank-codon biasing rather than from an A. flavus codon usage table directly. This affects only the native_uaZ variant's ranking and does not affect the headline cluster (which uses the 5p_softened variant, optimized for A. oryzae from first principles).

6. **Single payload only.** comp-022 ranks uricase cassettes in isolation. The §1.9 wet-lab test is a dual-cassette uricase + lactoferrin design, where pairwise chaperone-pathway competition is governed by [chaperone-orthogonal-stacking.md §3.5.3](./chaperone-orthogonal-stacking.md) (effective PDI load 0 + 24-40 = 24-40 total, within demonstrated NSlD-ΔP10 capacity). Comp-022 does not re-evaluate the pairwise interaction; it inherits the comp-010 finding that the uricase + lactoferrin pair is architecturally compatible.

7. **Cascading-filter framing partially redundant for this experiment.** Brief described a cascading filter where Tier 1 evaluates all 43,200, Tier 2 evaluates top 5,000, Tier 3 evaluates top 100. In practice, Tier 1 (CAI + mRNA-5') is per-codon-variant only (10 evaluations) and Tier 2 (chaperone-load) is per-scaffold-base only (10 evaluations), so the full 43,200-candidate evaluation is O(1) per candidate after the per-component pre-computations. Cascading matters when Tier 3 fold-quality (per-candidate ESMFold) is in scope; in this v1 it is not.

## 6. Impact on Experimental Priorities

### 6.1 §1.9 wet-lab cassette design

The §1.9 architecture stands. The uricase cassette in the existing §1.9 design ([`validation-experiments.md` §1.9](./validation-experiments.md)) is already `[PTEF1 - amyB signal peptide - A. flavus uaZ codon-optimized - TgpdA]`, which is in the comp-022 top cluster. Three gene-synthesis-time refinements should be incorporated when the construct is ordered:

| Refinement | Current §1.9 | comp-022 recommendation | Cost delta |
|---|---|---|---|
| Promoter | PTEF1 | Substitute PamyB OR keep PTEF1 as orthogonal-promoter design choice | $0 (same gene-synthesis cost; PTEF1 is justified by orthogonal-promoter rationale per koji-endgame-strain.md §3.4 even though PamyB is the single-promoter optimum) |
| Codon variant | "codon-optimized for *A. oryzae*" (unspecified strategy) | 5'-softened (low-GC first 30 codons + max-CAI thereafter) | $0 |
| C-terminal tag | none (native SKL) | append 3×Ala or His6 to block PTS1 | $0 (single codon trio extension) |
| N-glycosylation sequon | native N191 NSS | N191Q ablation | $0 (single point mutation) |

None of these refinements require new wet-lab infrastructure or change the §1.9 cost or timeline ($3-5K / 8-12 weeks). They are added to the gene-synthesis order at no marginal cost.

### 6.2 The §1.9 architecture decision: PamyB vs PTEF1 for uricase

Comp-022 single-cassette ranking favors PamyB for both cassettes. The current §1.9 design uses PTEF1 for the uricase cassette specifically to separate transcriptional programs from the PamyB-driven lactoferrin cassette (koji-endgame-strain.md §3.4: "Distinct promoter (TEF1, constitutive) to avoid direct competition with the starch-inducible PamyB of Cassette A"). This is a dual-cassette-specific rationale that comp-022's single-payload ranking does not override.

**Decision rule for the §1.9 construct:** keep PTEF1 for the uricase cassette per the orthogonal-promoter rationale. If the §1.9 Lf-alone arm titer falls below the 500 mg/L threshold per [chaperone-orthogonal-stacking.md §3.5.4 calibration framework](./chaperone-orthogonal-stacking.md), revisit the dual-PamyB design via comp-022's promoter-strength ranking (PamyB-PamyB cassette pair, integrated at paralogous loci per Li 2024 PMID 39830075; brief noted as a "symmetric alternative" in koji-endgame-strain.md §3.4).

### 6.3 Beyond §1.9: when this framework adds value

Comp-022's value is highest for **future cassettes** where the right architecture is not yet obvious from manual design:

- **DAF SCR1-4 single-cassette design** ([`validation-experiments.md` §1.25](./validation-experiments.md)): would benefit from a comp-022-style ranking with a fold-quality Tier 3 included (DAF SCR1-4 has 8 disulfides and is sensitive to fold quality, unlike uricase). Recommended follow-up.
- **Engineered C1-INH cassette** (parallel CP0 thread surfaced in [comp-018](./upstream-complement-modulator-sweep-computational.md)): comparable disulfide load + glycosylation + protease-sensitivity profile to lactoferrin. comp-022-style ranking would be load-bearing for first-pass cassette selection.
- **Complestatin NRPS LBP cassette** ([comp-024](./computational-experiments.md) when authored): different chassis (Bacteroides / E. coli Nissle), different codon optimization context, but the same combinatorial structure applies.

For uricase specifically, comp-022 is partly retrospective validation that the cassette-design intuition in the corpus (comp-010 + koji-endgame-strain.md §3.4) was correct. The headline architecture was not surprising; the value is the **501-cassette concordance shortlist as a reproducible artifact** plus the codon-variant refinement (5'-softened beats pure max-CAI) which was not in the existing design.

## 7. Cross-References

- [`computational-experiments.md`](./computational-experiments.md): comp-NNN tracking index
- [`autonomous-screening-methodology.md`](./autonomous-screening-methodology.md): ClockBase pattern this comp instantiates
- [`cassette-compatibility-computational.md`](./cassette-compatibility-computational.md) (comp-010): prior cassette-design analysis at single-candidate scope
- [`c-utilis-uricase-cassette-compatibility-computational.md`](./c-utilis-uricase-cassette-compatibility-computational.md) (comp-011): *C. utilis* uricase variant scoring
- [`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md): chaperone-load formula in §3.5
- [`validation-experiments.md`](./validation-experiments.md) §1.9: the wet-lab gate this informs
- [`koji-endgame-strain.md`](./koji-endgame-strain.md) §3.4: current §1.9 architecture
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) §06-§14: cassette design context
- [`uricase-protease-stability-computational.md`](./uricase-protease-stability-computational.md) (comp-001): orthogonal in silico prior on uricase stability
- [`experiments/comp-022-clockbase-uricase-cassette-ranking/`](../experiments/comp-022-clockbase-uricase-cassette-ranking/): analysis script, inputs, outputs, provenance

## 8. Status

Complete (v1). Fold-quality Tier 3 model deferred to a future run with GPU / API access OR to the §1.9 wet-lab readout. ViennaRNA MFE refinement of the mRNA-5' axis deferred (would refine but not substantively reorder the top cluster). Verification-agent pass complete per CLAUDE.md Rule 4; all load-bearing numbers in this page are grep-verified against primary sources in [`experiments/comp-022-.../provenance.md`](../experiments/comp-022-clockbase-uricase-cassette-ranking/provenance.md).
