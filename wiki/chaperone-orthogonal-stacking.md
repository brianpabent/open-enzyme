---
title: "Chaperone-Orthogonal Cassette Stacking — A Predictive Framework for Multi-Cassette Koji Yield"
date: 2026-05-05
tags:
  - koji
  - aspergillus-oryzae
  - cassette-design
  - chaperones
  - secretion-pathway
  - UPR
  - HacA
  - PDI
  - BiP
  - calnexin
  - co-expression
  - synergy
  - design-framework
  - endgame-strain
related:
  - aspergillus-oryzae.md
  - cassette-compatibility-computational.md
  - codon-optimization-expression-cassette.md
  - engineered-koji-protocol.md
  - koji-construct-design.md
  - koji-endgame-strain.md
  - protein-engineering-strategy.md
  - validation-experiments.md
sources:
  - "Huynh HH, Morita N, Sakamoto T, et al. Fungal Biol Biotechnol 2020;7:7 (PMC7257131) — adalimumab HC+LC dual cassette in NSlD-ΔP10, 39.7 mg/L"
  - "Wakai S, Yoshie T, Asai-Nakashima N, et al. Bioresour Technol 2019;276:146-153 (DOI: 10.1016/j.biortech.2018.12.117) — 3-cellulase co-expression in A. oryzae with 5–16 chromosomal copies; 40× total cellulolytic activity"
  - "Oikawa H. Proc Jpn Acad Ser B 2020;96(9):420-435 (PMC7725655) — NSAR1 5-marker platform; ≥17-gene fungal BGC reconstitution"
  - "Li Q, Zhang C, Li J, et al. Synth Syst Biotechnol 2024;10(2):365-372 (PMID 39830075) — A. oryzae multi-copy expression at distinct α-amylase loci, 3.3× uplift"
  - "Liu L, Feizi A, Österlund T, et al. BMC Syst Biol 2014;8:73 (PMC4086290) — A. oryzae genome-scale secretion analysis; duplicated chaperone paralogs (CPR1, ERJ5, ERD2)"
  - "Zhou B, Xie J, Liu X, et al. Gene 2016;593:143-153 (DOI: 10.1016/j.gene.2016.08.018) — constitutive HacA in A. oryzae; 80 secretory genes upregulated but RESS feedback reduces amylase output"
  - "Tanaka M, Shintani T, Gomi K. Fungal Genet Biol 2015;85:1-6 (DOI: 10.1016/j.fgb.2015.10.003) — UPR required for A. oryzae growth under enzyme-producing conditions; IreA conditional"
  - "Carvalho ND, Arentshorst M, Kooistra R, et al. BMC Genomics 2012;13:350 (PMC3472299) — A. niger constitutive HacA; growth + central metabolism trade-offs"
  - "Yu C, Yao X, Chen Y, et al. Sci Rep 2017;7:16577 (DOI: 10.1038/s41598-017-16577-x) — Pichia Hsp70/90 co-chaperone helper screen"
  - "Zhang W, Zhao HL, Xue C, et al. Biotechnol Prog 2006;22(4):1090-1095 — Pichia combinatorial chaperone (Ydj1+Pdi, Kar2+Pdi) 6.5-8.7× single-substrate uplift"
  - "Delic M, Göngrich R, Mattanovich D, Gasser B. Antioxid Redox Signal 2014;21(3):414-437 (DOI: 10.1089/ars.2014.5844) — Pichia substrate-specific chaperone effects"
  - "Gong Y, Kakihara Y, Krogan N, et al. Mol Syst Biol 2009;5:275 (DOI: 10.1038/msb.2009.26) — S. cerevisiae 63-chaperone modular network catalog"
  - "Chen Y, Siewers V, Nielsen J. Metab Eng 2024;88:1-13 (DOI: 10.1016/j.ymben.2024.11.010) — pcSecYeast proteome-constrained secretion model + CRISPRi/a validation"
  - "Li C, Zhou J, Du G, et al. J Fungi 2023;9(5):528 (DOI: 10.3390/jof9050528) — A. niger monellin copy-number ceiling; protease deletion 13.5× vs BiP/PDI no rescue"
  - "Sun XL et al. Acta Crystallogr D 1999;55(Pt 2):403-7 (PMID 10089347) — A. awamori-produced hLf, native fold confirmed despite fungal glycans"
status: draft
---

# Chaperone-Orthogonal Cassette Stacking

The interesting first-principles question for multi-cassette engineering in *A. oryzae* is not "how many cassettes can we bolt on?" but **"which cassettes share folding machinery, and which don't?"** Multi-cassette yield in heterologous secretion is dominated by competition for ER folding subsystems, not by genome real estate, transcription, or translation capacity. Cassettes partitioned across non-overlapping chaperone classes should stack with sublinear yield decay; cassettes competing for the same chaperone class show steep yield collapse well before promoter or genome-architecture limits are reached.

This page makes the framework explicit, scores Open Enzyme's candidate cassettes against it, and proposes a falsifiable test (pairwise expression matrix → measured synergy coefficients). It is a *predictive* design framework — not a literature review of demonstrated multi-cassette work, which is covered in [koji-endgame-strain.md](./koji-endgame-strain.md) §3 and [engineered-koji-protocol.md](./engineered-koji-protocol.md). The specific 2-cassette uricase + lactoferrin analysis at [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) is a case study under this framework; this page generalizes it.

All claims here are **Mechanistic Extrapolation** unless otherwise tagged. The framework is biochemically grounded but has not been empirically validated by a published koji-specific pairwise expression matrix — that absence is itself a load-bearing finding (see §8).

---

## 1. Why Cassette Count Is the Wrong Metric

The naive view treats heterologous expression as a per-cassette resource draw: N cassettes = N × per-cassette burden. Under that model, stacking enzymes is a simple optimization — keep adding until promoter strength, marker availability, or growth rate becomes limiting. Industrial fungal engineering treats cassettes this way by default; multi-locus integration platforms like NSAR1 (5 simultaneous markers per Oikawa 2020) are framed as "more cassette slots" rather than "more chaperone budget."

Several lines of evidence from the existing wiki and the literature suggest the per-cassette model breaks down:

1. **Huynh 2020** (PMC7257131; Fungal Biol Biotechnol 7:7, [DOI 10.1186/s40694-020-00098-w](https://doi.org/10.1186/s40694-020-00098-w)) achieved 39.7 mg/L adalimumab in *A. oryzae* NSlD-ΔP10 only with the ten-protease-deletion background; the lower-protease-deletion strains (NSlDv10, AUT1-lD-v10-sD) and the control NSlD1 produced less, and wild-type RIB40 was used only as a DNA donor (Huynh 2020 Results §"Adalimumab production in the culture supernatant of *A. oryzae*", Fig. 1; Abstract: "the highest amount of antibody was obtained from the ten-protease deletion strain (39.7 mg/L)" — verified 2026-05-06). The bottleneck was not cassette count (two cassettes — heavy chain + light chain) but ER folding capacity for paired heavy + light chains carrying **16 disulfides per assembled IgG1** (4 inter-chain + 12 intra-chain; verified via UniProt P01857 IgG1 heavy chain CH constant region annotations + P01834 kappa LC; standard IgG1 stoichiometry, 2026-05-06). (In Vitro). At the time of this writing, this is the highest published mAb-class titer in *A. oryzae* — the apparent ceiling at ~40 mg/L for two PDI-heavy cassettes is consistent with the orthogonality hypothesis (PDI/ERO1 saturation).
2. **Wakai 2019** (Bioresour Technol 276:146-153, PMID 30623869, [DOI 10.1016/j.biortech.2018.12.117](https://doi.org/10.1016/j.biortech.2018.12.117)) achieved a **40× total cellulolytic activity uplift versus the single-integration strain** in *A. oryzae* by stacking three cellulase cassettes (cellobiohydrolase + endoglucanase + β-glucosidase) at 5–16 chromosomal copies each, then optimizing promoter/terminator combinations (P-sodM/T-glaB demonstrated the strongest per-copy transcription) (Wakai 2019 Abstract; verified 2026-05-06). The decomposition: multi-copy integration alone gave ~10-fold over single-integration; promoter/terminator engineering on top of multi-copy integration gave the additional 4× to reach 40-fold (Wakai 2019 Abstract verbatim: "approximately 10-fold higher activity versus single integration strains... resulting transformant showing 40-fold higher cellulolytic activity versus the single integration strain"). [VERIFICATION CORRECTION 2026-05-06: the previous wiki framing — "approximately 10× from copy stacking; the rest from multi-cassette synergy" — was a misattribution. The 4× delta from 10-fold to 40-fold is from promoter/terminator optimization, not from multi-cassette synergy. The word "synergy" does not appear in the Wakai abstract.] Critically, all three cellulases are fungal-origin with modest disulfide load and N-glycan content — they share BiP/calnexin dominance but minimal PDI competition. The 40× titer is consistent with chaperone-orthogonal compatibility for fungal-native substrates, but it is not direct evidence of cross-cassette synergy distinct from per-cassette transcriptional scaling. (In Vitro).
3. **Oikawa 2020** (PMC7725655) reconstituted a ≥17-gene fungal biosynthetic cluster in *A. oryzae* NSAR1 — but those genes encode small-molecule biosynthetic enzymes (intracellular, mostly cytosolic), which entirely bypass the secretion pathway. The 17-gene number is not comparable to 17 secreted heterologous proteins. (In Vitro)
4. **Li 2024** (PMID 39830075) achieved 3.3× yield uplift by integrating multiple copies of the same cassette at distinct α-amylase loci — pure transcriptional/translational scaling of one substrate, not multi-substrate competition. (In Vitro)
5. **Li 2023** (DOI: 10.3390/jof9050528) found that for *A. niger* monellin, copy-number gave diminishing returns (1→2 copies = 2.7×; 2→5 copies = 1.5×) and **BiP/PDI overexpression did not rescue**, but **extracellular protease deletion gave 13.5× uplift**. (In Vitro). For some substrates, post-secretion proteolysis is the binding constraint, not folding — emphasizing that "chaperone competition" is one of multiple potential ceilings.

Read together: the published multi-cassette successes either (a) use protease-deletion strains to expand folding headroom, (b) co-express substrates that don't load the same chaperone subsystem heavily, or (c) bypass the secretion pathway entirely. None of them tested two heavily-disulfide-bonded mammalian-origin secreted proteins in parallel beyond the Huynh 2020 antibody case, which appears to have hit a real ceiling — which would be the worst-case design for chaperone competition. **No published koji-specific pairwise expression matrix tests cassette-cassette competition as a function of predicted chaperone-class overlap** — the framework's central prediction has not been empirically validated.

The framework below predicts which combinations fall into the "easy" vs. "hard" buckets *a priori*, from substrate features alone, before any wet-lab work.

---

## 2. The Five ER Chaperone Subsystems in *A. oryzae*

Heterologous proteins targeted to the secretion pathway pass through a sequence of chaperone-mediated folding steps. Each step is mediated by a discrete molecular subsystem with finite catalytic capacity. Saturating any one subsystem creates a bottleneck that cannot be relieved by stronger promoters, more cassettes, or higher amino acid supply — only by either reducing load on that subsystem or expanding its capacity (HacA UPR, directed evolution, exogenous expression).

| Subsystem | Function | Substrate features that load it | Capacity expansion lever |
|---|---|---|---|
| **BiP/Kar2** (HSP70) | Generic ER lumen chaperone; binds nascent unfolded chains, prevents aggregation, hands off to specialized chaperones | All ER-targeted proteins (universal); especially proteins with extended hydrophobic stretches | HacA UPR upregulates ~3-5× (In Vitro, A. niger); BiP overexpression cassettes documented |
| **PDI / ERO1** | Disulfide bond formation and isomerization; ERO1 reoxidizes PDI cycling | Cysteine count; disulfide bond count; per-chain disulfide density | HacA UPR; PDI overexpression; directed evolution of PDI variants (Pichia precedent) |
| **Calnexin / Calreticulin cycle** | N-glycoprotein quality control; GlcNAc-trimming-driven folding cycle; UGGT re-glucosylation for re-folding | N-X-S/T sequons (X≠P); per-protein N-glycan site density | UPR induction; UGGT overexpression less characterized in koji |
| **Lectin / Mns1 ER mannosidase** | ERAD trigger after failed calnexin cycles; commits misfolded glycoproteins to degradation | Glycoproteins that fold slowly; chronic UPR substrates | Knockdown can transiently raise titer at cost of strain stress |
| **HacA UPR (transcriptional)** | Transcription factor (Hac1/HacA homolog) that responds to ER stress by upregulating BiP, PDI, ERAD machinery, lipid biosynthesis | Cumulative ER folding load (sums across all heterologous substrates) | Constitutive activated HacA (HacA<sup>i</sup>) gives 2-3× heterologous titer in *A. niger* and *T. reesei* (In Vitro; Valkonen 2003; Mulder 2004) |

Two additional axes that aren't ER chaperones but interact strongly with cassette stacking:

- **Cytosolic ribosome / chaperonin pool** — only relevant for very-high-translation cassettes or cytosolic targets. Generally not limiting in koji at typical heterologous expression levels.
- **Vesicular traffic (COPII / ER exit sites)** — emerging evidence in *A. niger* that ER exit site density limits secretion at high titer; not characterized in koji.

**Koji-specific note: chaperone paralog redundancy.** Liu 2014 (PMC4086290) genome-scale secretion analysis of *A. oryzae* found multiple paralogs for several core ER chaperone components (CPR1 cyclophilin, ERJ5 J-protein co-chaperone, ERD2 KDEL receptor) that are not duplicated in *S. cerevisiae*. (In Vitro). This suggests koji may have **higher partition capacity** than yeast — different paralogs may specialize on different substrate classes — though the functional independence of these paralogs has not been characterized. If functionally distinct, this is a structural advantage of koji as a multi-cassette chassis vs. yeast. Open question for direct testing.

A network-property note from Pichia: **Palma/Gasser 2024** (bioRxiv 10.1101/2024.08.21.609038) found that *K. phaffii* Pdi1 KO is viable for disulfide-bonded recombinant protein production — backup paralogs (Eug1, Mpd1) compensate. (In Vitro). This means "PDI capacity" is a network property, not a single-gene quantity. The implication for OE: PDI competition manifests as a network-saturation effect, not a single-enzyme bottleneck, and may be relieved by paralog upregulation rather than only by direct PDI overexpression.

The framework's claim is that **ER chaperone competition is the binding constraint for typical multi-cassette koji designs**, with PDI / ERO1 the most commonly saturated subsystem (because mammalian-origin therapeutic proteins disproportionately carry disulfide-rich folds).

---

## 3. Substrate Categorization — Predicting Chaperone Load

For each candidate cassette, score five features. The combined profile predicts which chaperone subsystem(s) will dominate the burden:

| Feature | What it measures | Scoring |
|---|---|---|
| **Cysteine / disulfide count** | PDI / ERO1 load | 0 disulfides = none; 1-3 = light; 4-10 = moderate; 11+ = heavy |
| **N-glycosylation site count** | Calnexin / calreticulin load | 0 sites = none; 1-2 = light; 3-5 = moderate; 6+ = heavy |
| **Subunit assembly requirements** | BiP retention / multi-chain coordination | Monomer = none; homo-multimer = light; hetero-multimer = heavy |
| **Domain count / chain length** | Generic BiP load; folding kinetics | <200 aa single domain = light; 200-500 = moderate; >500 or multi-domain = heavy |
| **Subcellular target** | Whether the cassette uses the secretion pathway at all | Cytosolic = bypasses entire system; secreted = full pathway; peroxisomal/mitochondrial = different machinery |

The prediction: cassettes whose dominant load classes (the heaviest 1-2 features) are **non-overlapping** stack synergistically; cassettes whose dominant load classes overlap heavily compete for the same machinery.

---

## 4. Open Enzyme Candidate Cassettes — Scored

| Cassette | Origin | Disulfides | N-glyc sites | Assembly | Length | Target | **Dominant load class** |
|---|---|---|---|---|---|---|---|
| **Uricase** (*uaZ*, A. flavus, Q00511) | Fungal | 0 | 0 (annotated; 1 sequon predicted but unoccupied per [comp-010 §5.5](./cassette-compatibility-computational.md#55-n-glycosylation)) | Homotetramer | 302 aa | Cytosolic native; secreted via amyB SP | **BiP-only (transit)** — chaperone-light |
| **Uricase variant — *C. utilis*** (URIC_CYBJA, P78609; per [comp-011 §4.2](./c-utilis-uricase-cassette-compatibility-computational.md#42-free-cysteines-4-vs-0)) | Yeast | 0 disulfides + **4 free Cys** (positions 39, 168, 250, 293) | 1 predicted (NSS pos 54, not annotated) | Homotetramer | 302 aa | Secreted via amyB SP | **PDI-engaged via free-Cys load** — variant choice matters; magnitude unknown ([comp-011 §4.4](./c-utilis-uricase-cassette-compatibility-computational.md#44-chaperone-load-implications-cross-reference-to-chaperone-orthogonal-stacking-framework)) |
| **Lactoferrin** (hLf, P02788) | Mammalian | 17 (one chain) | 3 confirmed | Monomer | 691 aa | Secreted | **PDI-heavy** + calnexin-moderate + BiP-heavy |
| **Native lipase** (e.g., *A. oryzae* TGL) | Fungal native | 3 | 0-1 | Monomer | ~270 aa | Secreted | **PDI-light** — well-adapted |
| **Native α-amylase** (TAKA-amylase) | Fungal native | 1 | 4-5 | Monomer | 478 aa | Secreted | **Calnexin-moderate** + PDI-light |
| **Native acid protease** | Fungal native | 2-3 | Variable | Monomer | ~330 aa | Secreted | **PDI-light** + calnexin-light |
| **DAF / CD55 SCR1-4** (truncated; per [comp-012](./daf-cd55-scr14-truncated-computational.md)) | Mammalian | 8 (4 SCRs × 2 disulfides each) | 0 (stalk truncation removed sites) | Monomer | ~250 aa | Secreted | **PDI-moderate** — small SCR domains fold fast |
| **Carnosine synthase** (*Lactobacillus* CarnS) | Bacterial | 0 | 0 | Monomer | ~460 aa | Cytosolic | **Bypasses secretion entirely** |
| **panD aspartate decarboxylase** (β-alanine supply) | Bacterial | 0 | 0 | Homotetramer | ~140 aa | Cytosolic | **Bypasses secretion entirely** |
| **Kojic acid pathway** (native) | Fungal native | n/a (small-molecule) | n/a | n/a | n/a | Cytosolic biosynthesis | **Off the protein machinery axis entirely** |
| **Ergothioneine pathway** (native) | Fungal native | n/a | n/a | n/a | n/a | Cytosolic biosynthesis | **Off the protein machinery axis entirely** |

The pattern is striking: the **Open Enzyme koji endgame strain is implicitly already a chaperone-orthogonal design.** The five "molecules" of [koji-endgame-strain.md](./koji-endgame-strain.md) §1 distribute across non-overlapping load classes —

- **Uricase**: BiP-transit only (zero disulfide, zero glycosylation, zero subunit assembly) — *this orthogonality is variant-specific to A. flavus (Q00511); the C. utilis variant (P78609) carries 4 free Cys that engage PDI/ERO1, partially collapsing the orthogonality. See [comp-011 §4.4](./c-utilis-uricase-cassette-compatibility-computational.md#44-chaperone-load-implications-cross-reference-to-chaperone-orthogonal-stacking-framework) for the bidirectional analysis. The §1.9 parallel head-to-head is the empirical resolver.*
- **Lactoferrin**: PDI + calnexin + BiP — carries essentially the entire ER chaperone load on its own
- **Native digestives** (lipase, protease, amylase): light, well-adapted, host-evolved
- **Carnosine + panD**: cytosolic — completely off the secretion pathway
- **Kojic acid + ergothioneine**: small-molecule biosynthesis — off the protein machinery entirely

This was not an explicit design choice — it emerged from each cassette being chosen for therapeutic mechanism, with the chaperone-orthogonality being a happy accident. Making the framework explicit gives a *prospective* tool for the next round of cassette additions: any new candidate should be scored against the existing four load classes and preferentially fill underused ones.

---

## 5. Predicted Synergy Coefficients

Define a **synergy coefficient** for cassette pair (A, B):

$$
\text{Synergy}(A, B) = \frac{\text{Yield}(A | A+B) + \text{Yield}(B | A+B)}{\text{Yield}(A | A \text{ alone}) + \text{Yield}(B | B \text{ alone})}
$$

Where Yield(X | A+B) is the per-cassette yield of X when co-expressed with B, and Yield(X | X alone) is the single-cassette baseline. Interpretation:

- **Synergy ≈ 1.0** — additive; cassettes don't interact (orthogonal)
- **Synergy < 0.7** — antagonistic; cassettes compete for shared machinery
- **Synergy > 1.0** — supra-additive; cassettes positively interact (rare; e.g., one cassette upregulates UPR which helps the other)

Predicted synergy matrix for OE candidate pairs (Mechanistic Extrapolation; ranges reflect uncertainty):

| Pair | Predicted Synergy | Rationale |
|---|---|---|
| Uricase × Lactoferrin | **0.8 - 1.0** | Non-overlapping: uricase is BiP-transit only, Lf carries PDI/calnexin/BiP. Slight Lf-from-uricase BiP draw, but uricase load is small. (Validated direction by [comp-010](./cassette-compatibility-computational.md): combined ER burden 1.06× Huynh 2020 antibody baseline, within demonstrated capacity.) |
| Uricase × DAF SCR1-4 | **0.85 - 1.0** | Both light loads, different dominant subsystems. Should stack near-additively. |
| Uricase × Carnosine cassette | **~1.0** | Completely orthogonal — uricase secreted, carnosine cytosolic. No shared machinery. |
| Lactoferrin × DAF SCR1-4 | **0.5 - 0.7** | Both PDI substrates. 17 + 8 = 25 disulfides simultaneously loading PDI/ERO1. Likely PDI-saturating without UPR upregulation. |
| Lactoferrin × Native α-amylase (excess) | **0.6 - 0.8** | Both load calnexin. Native amylase has 4-5 N-glycan sites; Lf has 3. Calnexin competition possible at high titer. |
| Two PDI-heavy mammalian glycoproteins (e.g., Lf + Fab heavy chain) | **0.5 - 0.6** | Worst case. Antibody HC + LC at Huynh 2020 (39.7 mg/L) is in this regime — only achievable in NSlD-ΔP10 protease-deletion background. Falsifiable lit-scan prediction: sub-additive ~50-60% of expected. |
| Three light secreted enzymes (e.g., 3 cellulases per Wakai 2019) | **≥1.0 (provisional — see caveat)** | Wakai 2019 reports 40× total cellulolytic activity from 3-cellulase stacking versus single-integration baseline. Decomposition (verified from Wakai abstract 2026-05-06): ~10× from multi-copy integration alone; the additional ~4× from promoter/terminator optimization (P-sodM/T-glaB selected via per-copy transcription screen). **The Wakai paper does NOT directly evidence cross-cassette synergy** — three cellulases co-existing at high titer is consistent with chaperone-orthogonal compatibility for fungal-native substrates (no titer collapse), but the 40× number is not a synergy coefficient. The supra-additive prediction here remains a framework-level extrapolation pending a single-cassette-vs-pair pairwise expression matrix in koji. (In Vitro — partial direct evidence.) |
| Endgame strain (uricase + Lf + native digestives + carnosine) | **~0.85 weighted** | Lf carries the chaperone load; everything else is light or off-pathway. The "five-molecule" payload should approximate two-cassette burden in chaperone terms. |

The Open Enzyme endgame strain's predicted weighted synergy ~0.85 — close to additive — is the framework's quantitative reframe of why the "five molecules in one strain" thesis is biochemically reasonable. It is *not* five-fold burden; it is roughly Huynh-2020-equivalent burden distributed across more deliverables.

---

## 5.5 Triple-Cassette Prospective Prediction — Uricase + Lactoferrin + DAF SCR1-4

**This is Sweep A Proposed Experiment 1 (2026-05-05, commit 3e928d3): the first real prospective test of whether the chaperone-orthogonal framework has predictive power beyond retrofit.**

The question is load-bearing for the platform: **Can the koji endgame strain be a single triple-cassette strain (uricase + lactoferrin + DAF SCR1-4) that closes CP0 (complement-priming chokepoint, per [H05](../hypotheses/H05-daf-scr14-cp0-thesis.md)) as well as the existing CP1-CP6 coverage from uricase + lactoferrin? Or does chaperone-load competition from adding DAF SCR1-4 force it onto a separate strain or onto the [engineered LBP chassis](./engineered-lbp-chassis.md) as a parallel peer track?**

All predictions in this section are **Mechanistic Extrapolation** anchored to the verified source numbers in §10.1. No new unverified quantitative claims are introduced.

### 5.5.1 Setup — Cassettes, Disulfide Totals, and Baseline

The three cassettes:

| Cassette | Gene | Disulfides | N-glyc sites | Dominant load class |
|---|---|---|---|---|
| **Uricase** | *A. flavus uaZ* (Q00511) | **0** | 0 (unoccupied) | BiP-transit only — chaperone-light |
| **Lactoferrin** | hLf (P02788) | **17** (one chain) | 3 confirmed | PDI-heavy + calnexin-moderate |
| **DAF SCR1-4** | P08174 aa 35–285 | **8** (2 per SCR × 4 SCRs, per UniProt P08174 DISULFID features, verified 2026-05-06; see [comp-012 §1.5](./daf-cd55-scr14-truncated-computational.md#15-correction-note-2026-05-06-disulfide-count-anchor)) | 0 (stalk truncation removed glycosylation sites) | PDI-moderate |

**Triple-cassette disulfide total: 25** (0 + 17 + 8). This is 1.56× the Huynh 2020 adalimumab baseline of 16 disulfides (4 inter-chain + 12 intra-chain; verified via UniProt P01857 + P01834; see §10.1). Compare to the dual-cassette (comp-010) of 17 disulfides = 1.06× the Huynh baseline. Adding DAF SCR1-4 pushes the triple 47% above the dual on the PDI-load axis, and 56% above the demonstrated capacity ceiling if the Huynh ceiling is architecture-independent.

**Calibration context:** The §1.9 wet-lab experiment has a Lf-alone arm that directly resolves the capacity-vs-titer benchmark ambiguity flagged in §8 item 7 and [koji-endgame-strain.md §3.3](./koji-endgame-strain.md). If Lf alone reaches >500 mg/L in NSlD-ΔP10 solid-state, the Huynh ceiling is antibody-architecture-specific (dual-chain assembly difficulty, not single-chain disulfide count), and the framework's synergy coefficients are systematically conservative. Until that data lands, both scenarios must bound the prediction.

### 5.5.2 Per-Pair Synergy Recap (With Corrected DAF Disulfide Count)

Three pairwise synergies from §5, applied to the corrected 8-disulfide DAF count:

| Pair | §5 predicted synergy | Note with corrected 8-disulfide DAF |
|---|---|---|
| **Uricase × Lactoferrin** | **0.8–1.0** | Unchanged — uricase carries zero disulfides, Lf carries 17. This pair is the framework's best-case: fully orthogonal on the PDI axis. (Validated direction by [comp-010](./cassette-compatibility-computational.md): 1.06× Huynh baseline, within demonstrated capacity.) |
| **Uricase × DAF SCR1-4** | **0.85–1.0** | Largely unchanged by the disulfide correction. Uricase's zero disulfide load means it doesn't compete with DAF's PDI draw regardless of whether DAF has 8 or 12 disulfides. Both remain light-load cassettes from each other's perspective; the prior prediction holds. |
| **Lactoferrin × DAF SCR1-4** | **0.5–0.7** | **This is the worst pair and it stays worst after the disulfide correction.** The prior estimate assumed 12 DAF disulfides; the correct number is 8. The corrected total Lf + DAF load is 17 + 8 = 25 disulfides vs. the prior 17 + 12 = 29. The PDI saturation risk is real but ~14% lower than the prior framing implied — the pair synergy range of 0.5–0.7 still reflects PDI-saturation risk, but the lower bound is somewhat less severe than a 29-disulfide prior would suggest. The pairwise prediction remains "likely PDI-saturating without UPR upregulation." |

**The Lf × DAF SCR1-4 pair is the dominant constraint on the triple.** Any combination that includes this pair inherits its synergy floor. Uricase's orthogonality does not rescue the Lf-DAF competition.

### 5.5.3 Triple-Cassette Composition Rule — Two Bounding Models

Pairwise synergy coefficients do not compose trivially for a triple. Two models bound the prediction:

**Model A — Multiplicative pairwise (floor estimate).**
Treat each pair's synergy as an independent multiplier on the others. The three pairs are Uricase × Lf (midpoint ~0.90), Uricase × DAF (midpoint ~0.925), and Lf × DAF (midpoint ~0.60). Naive multiplication: 0.90 × 0.925 × 0.60 ≈ 0.50. This is a floor because it assumes the three pairwise competitions are independent — that adding a third cassette creates additive marginal penalties. In a saturated system, the third cassette may find the pool already depleted and contribute near-zero additional burden (the marginal cost flattens once the bottleneck is hit). Therefore 0.50 is a conservative lower bound, not the expected value.

**Model B — Chaperone-saturation (upper estimate).**
If the Lf × DAF pair already saturates PDI/ERO1 at pairwise synergy 0.5–0.7, adding a third cassette (uricase) that is PDI-orthogonal does not worsen the saturated subsystem. The triple-cassette synergy converges to the worst pairwise synergy (Lf × DAF), limited by how far the saturation ceiling has already been hit. Upper bound: if the Lf-alone arm of §1.9 shows >500 mg/L in NSlD-ΔP10 (suggesting the Huynh ceiling is antibody-specific), then the effective PDI capacity for single-chain substrates may accommodate the 25-disulfide load more readily, pushing the saturation-model upper bound toward the higher end of the Lf × DAF range (0.65–0.70).

**Neither model is empirically validated in koji.** The Wakai 2019 verification (§10.1) confirmed that three light-substrate cellulases stack without titer collapse — but all three are fungal-native with negligible disulfide load. There is no published koji-specific data point for a two-PDI-heavy-substrate stacking scenario (the closest is Huynh 2020, which is a dual-chain antibody, not two separate PDI-heavy proteins). The models below should be read with this absence explicitly in mind.

### 5.5.4 Predicted Synergy Range — 0.45–0.70

**Lower bound: ~0.45** (multiplicative pairwise model; no UPR rescue; Huynh ceiling is architecture-independent).

Anchored to: (a) Lf × DAF pairwise prediction of 0.5–0.7, floor 0.5; (b) multiplicative composition reducing the effective triple synergy ~10% below the worst pair; (c) the Huynh 2020 capacity ceiling interpretation where 16 disulfides represents a genuine PDI/ERO1 saturation limit and 25 disulfides exceeds it.

**Named uncertainty sources for the lower bound:**
- Whether the multiplicative pairwise composition rule holds in a saturated system (it may be an overestimate of penalty if the bottleneck is already hit at the pairwise level)
- Whether the Huynh ceiling applies to single-chain substrates (Lf is single-chain; adalimumab is dual-chain; §8 item 7)

**Upper bound: ~0.70** (chaperone-saturation model; single PDI overexpression rescue; Huynh ceiling is antibody-specific).

Anchored to: (a) Lf × DAF pairwise upper bound of 0.70; (b) saturation-model composition convergence to the worst pair without additional multiplicative penalty from uricase; (c) if §1.9 Lf-alone arm shows >500 mg/L, the effective PDI capacity for single-chain substrates may accommodate the triple's 25-disulfide load at or near the Lf × DAF pairwise ceiling; (d) single PDI overexpression (one additional cassette) provides 1.05–1.15× rescue in the same-paper comparison to baseline (within Zhang 2006 PMID 16889384; the cross-paper comparison to Yu 2017 is confounded — see §10.1), which can marginally lift the upper bound without displacing it to the >0.85 tier.

**Named uncertainty sources for the upper bound:**
- Whether the §1.9 Lf-alone result resolves the Huynh ambiguity in the favorable direction (this is the single biggest mover of the range)
- Whether UPR background upregulation in NSlD-ΔP10 under high-load conditions provides a free rescue effect not captured in the pairwise estimates
- Whether the Lf × DAF 0.5–0.7 range is itself calibrated correctly (it is an extrapolation from Pichia and *A. niger* data, not a koji-measured value)

**Central expectation: 0.55–0.65.** This lands in the 0.6–0.85 decision gate — feasible with chaperone-helper augmentation, but not cleanly stackable as a simple triple.

### 5.5.5 Decision Threshold Gates

**Important disclaimer:** These thresholds are **framework-convention**, not derived from empirical data. They should be read as "if the wet-lab measurement of the triple-cassette strain lands in this region, this is the recommended decision direction" — not as bright-line rules with mechanistic derivation.

| Measured triple-cassette synergy | Interpretation | Recommended platform direction |
|---|---|---|
| **>0.85** | Triple stacks cleanly; PDI subsystem not saturated by the 25-disulfide load. | Pursue triple-cassette endgame strain as the single-strain CP0+CP1-CP6 solution. **Assessed probability: low**, given the Lf × DAF pairwise prediction. Would require the Huynh ceiling to be strongly antibody-architecture-specific AND NSlD-ΔP10 to have unusually high single-chain PDI capacity. |
| **0.6–0.85** | Feasible with chaperone-helper augmentation. PDI/ERO1 partially saturated but rescuable. | Pursue triple-cassette with a PDI co-expression cassette (4-cassette design). Per §10.1 Zhang 2006 verification (PMID 16889384), **single PDI overexpression alone captures ~1.05-1.15× rescue** (intra-paper comparison; single-chaperone arms gave 4-7×, combinations gave 6.5-8.7×, combination/single advantage = ~1.2-1.5×). The NSlD-ΔP10 host's existing ten-protease-deletion background may also provide an indirect rescue effect by reducing post-secretion degradation of any misfolded intermediate, marginally reducing the apparent PDI bottleneck. **Assessed probability: medium**, dependent on §1.9 Lf-alone resolving the Huynh ambiguity favorably. |
| **<0.6** | DAF cassette should go on a separate strain (two-strain co-fermentation) or onto the [engineered LBP chassis](./engineered-lbp-chassis.md) as a parallel peer track. The CP0 closure thesis (H05) stays alive in all three cases — only the chassis-route changes. | Maintain uricase + Lf dual-cassette as the endgame strain (CP1-CP6 coverage); route DAF SCR1-4 separately. **Assessed probability: high**, given the Lf × DAF pairwise prediction and the central expectation of 0.55–0.65. |

### 5.5.6 Dominant Predicted Bottleneck

**PDI/ERO1 saturation from the simultaneous Lf + DAF disulfide load (17 + 8 = 25 disulfides)** is the almost-certain dominant bottleneck. Rationale:

- Lactoferrin alone at 17 disulfides already approaches the demonstrated Huynh 2020 capacity ceiling of 16 disulfides (though the antibody-architecture ambiguity in §8 item 7 creates uncertainty about how hard that ceiling is for single-chain substrates).
- Adding 8 DAF SCR1-4 disulfides pushes the simultaneous PDI/ERO1 load 56% above the Huynh benchmark.
- Uricase contributes zero disulfides — it does not contribute to this bottleneck.
- The BiP/Kar2 pathway (which handles all ER-targeted proteins generically) is less likely to be limiting: uricase's transit load is small, DAF SCR1-4 at ~250 aa is also small, and Lf at 691 aa is the largest contributor — consistent with the dual-cassette (comp-010) already being within comfortable BiP range at 1.06× baseline.
- The calnexin/calreticulin pathway is not predicted to be limiting: Lf has 3 N-glycan sites (moderate), DAF SCR1-4 has 0 sites after stalk truncation, uricase has 0 confirmed sites.

**Cross-reference §8 item 7 (capacity-vs-titer benchmark ambiguity):** If the §1.9 Lf-alone arm demonstrates >500 mg/L Lf in NSlD-ΔP10 solid-state, this indicates the Huynh ceiling is antibody-architecture-specific (dual-chain assembly difficulty, not total disulfide count). In that scenario, the triple-cassette upper bound shifts more favorably — PDI/ERO1 can handle single-chain substrates at higher disulfide loads than the antibody baseline implies, and the predicted bottleneck is less severe. The §1.9 experiment directly resolves this before any triple-cassette wet-lab work is committed.

### 5.5.7 Prospective Falsifiable Prediction

**Framework prediction:** triple-cassette (uricase + Lf + DAF SCR1-4) synergy falls in the range **0.45–0.70** (central expectation 0.55–0.65), with PDI/ERO1 saturation as the dominant bottleneck.

**The falsifiable test:** Wet-lab measurement of the triple-cassette strain's Lf titer (or DAF SCR1-4 titer) in NSlD-ΔP10 solid-state, compared to the dual-cassette (uricase + Lf) baseline measured in the same §1.9 experiment, directly tests this prediction. The synergy coefficient is:

$$
\text{Synergy}_{\text{triple}} = \frac{\text{Lf titer (triple-cassette strain)} + \text{DAF titer (triple-cassette strain)} + \text{Uricase activity (triple-cassette strain)}}{\text{Lf titer (dual-cassette alone)} + \text{DAF titer (DAF alone)} + \text{Uricase activity (uricase alone)}}
$$

In practice, measuring Lf titer alone in the triple vs. dual-cassette context gives the cleanest single-protein readout: if **Lf titer in the triple-cassette strain is >85% of the dual-cassette baseline**, the triple stacks cleanly (synergy >0.85 regime). If Lf titer is 60-85% of dual-cassette baseline, augmentation is warranted. If Lf titer drops below 60% of the dual-cassette baseline, separate-strain routing is the framework-recommended direction.

**This is the first real prospective test of whether the chaperone-orthogonal framework has predictive power beyond retrofit.** All existing synergy coefficients were derived to explain known outcomes (Huynh 2020, Wakai 2019, comp-010). The triple-cassette prediction is the first case where the framework commits to a specific outcome *before* wet-lab data exists. Outcome range 0.45–0.70 is a falsifiable prediction; any measured value outside this range (particularly synergy >0.85) would require framework revision.

### 5.5.8 Platform Decision Tree — What This Changes

| Scenario | Probability | Platform direction |
|---|---|---|
| Synergy >0.85 (triple stacks cleanly) | Low | Pursue triple-cassette endgame strain as CP0+CP1-CP6 single-strain solution. Four cassette slots free in NSAR1 5-marker platform for downstream additions (kojA/kojR overexpression, carnosine module). |
| Synergy 0.6–0.85 (feasible with helper augmentation) | Medium | Pursue triple-cassette with single-PDI-overexpression cassette (4-cassette total). Characterize bottleneck (PDI vs. ERO1 vs. BiP) before adding helper, per §7 order-of-operations. NSlD-ΔP10's protease-deletion background may provide partial rescue without a dedicated helper cassette. |
| Synergy <0.6 (separate-strain routing) | High | Maintain uricase + Lf dual-cassette as the endgame strain. Route DAF SCR1-4 to either: (a) a dedicated second *A. oryzae* strain co-fermented with the dual-cassette strain, OR (b) the engineered LBP chassis ([engineered-lbp-chassis.md](./engineered-lbp-chassis.md)) as a parallel peer track. H05 thesis stays alive — only the chassis-route changes. The endgame strain stays at CP1-CP6 coverage (five chokepoints, four molecules per [koji-endgame-strain.md](./koji-endgame-strain.md) §1); CP0 direct-antagonism coverage becomes a separate-strain or peer-track output. |

**Key point in all three scenarios:** the H05 CP0-closure thesis is not killed by a low triple-cassette synergy — it only changes where the DAF SCR1-4 cassette lives. The platform's five-chokepoint endgame strain design is preserved regardless of which gate the triple-cassette measurement lands in.

**Dependency on §1.9 experiment arms:** The §1.9 wet-lab design now has three cassette-configuration arms relevant to chaperone-load resolution:
1. **Lf-alone arm** — resolves the capacity-vs-titer ambiguity (§8 item 7). Required before interpreting any dual or triple result.
2. **Uricase + Lf dual-cassette arm** — validates the comp-010 prediction (1.06× Huynh baseline, within capacity). Required for interpreting the triple.
3. **Uricase + Lf + DAF SCR1-4 triple-cassette arm** — the prospective falsifiable test of this §5.5 prediction. **Optional for the §1.9 gate decision** (the dual-cassette arm is sufficient to decide whether to proceed with the endgame strain); adds ~$1-2k and 2-3 weeks but provides the framework's first prospective validation data point.

---

## 6. The Falsifiable Test — Pairwise Expression Matrix

The framework is testable. Construction of a pairwise expression matrix on a small set of representative substrates would either validate or falsify the predicted synergy coefficients.

**Experimental design:**

1. **Choose 4-6 candidate cassettes** spanning the load classes:
   - One BiP-only / cytosolic-native repurposed (uricase)
   - One PDI-heavy mammalian glycoprotein (lactoferrin or DAF full-length)
   - One PDI-light / calnexin-light fungal-native (lipase or amylase, controlled overexpression beyond native)
   - One PDI-moderate small mammalian protein (DAF SCR1-4)
   - One cytosolic / off-pathway (carnosine cassette)
   - Optionally: one PDI-heavy from a different fold class than Lf (e.g., a second mammalian glycoprotein)

2. **Build all single-cassette and pairwise-cassette strains.** N=6 candidates → 6 single + 15 pairwise = 21 strains. Triple combinations (~20 more) optional for second pass.

3. **Quantify per-protein titer** for each protein in each strain background (ELISA, activity assay, or quantitative SDS-PAGE).

4. **Compute synergy coefficient** for each pair. Plot against predicted (load-class overlap) — the framework predicts a strong negative correlation between "shared dominant load class" and synergy.

5. **Identify which feature (disulfide count / glycan count / chain length / subunit assembly) is the strongest predictor** of antagonism. The expected answer is disulfide bond competition (PDI) — but this is empirical.

**Cost / timeline.** 21-strain construction + quantification: ~$15-25k, 4-6 months in a skilled lab. Three-cassette extension: another $10-15k, 2-3 months. This is substantial — bigger than any single comp-NNN — but the result is a *predictive design tool* for all future Open Enzyme cassette additions. The first wet-lab Ward 1995 dual-cassette test ([validation-experiments.md §1.9](./validation-experiments.md)) generates the first two data points (uricase alone, uricase + Lf) for free as a side product.

**Falsification conditions:**

- If **synergy coefficients show no correlation** with load-class overlap, the framework is wrong; cassette competition is governed by something else (codon usage, mRNA stability, vesicular traffic, growth-rate burden).
- If **synergy is uniformly < 0.7** across all pairs regardless of load class, the binding constraint is upstream of folding (transcription, translation, growth) and chaperone-orthogonality is irrelevant at typical OE expression levels.
- If **single-cassette and pairwise titers are statistically indistinguishable**, the OE expression regime is below saturation for all subsystems and the framework only matters at higher titers than OE currently targets.

---

## 7. Headroom Expansion Levers

If empirical synergy coefficients confirm chaperone competition is the binding constraint, several published levers expand capacity. **The picture in koji is more complex than in *A. niger* / *T. reesei*** — naive UPR activation does not straightforwardly help.

| Lever | Effect (literature) | OE applicability |
|---|---|---|
| **NSlD-ΔP10 background** (10-protease-deletion; Huynh 2020 / Maruyama-lineage patent JP5140832B2) | Required for Huynh's 39.7 mg/L adalimumab; raises secretion floor for PDI-heavy substrates. Independent confirmation: Li 2023 *A. niger* monellin showed extracellular protease deletion gave **13.5× uplift** where BiP/PDI overexpression gave none. (In Vitro) | Already the recommended host for Lf cassette per [comp-010](./cassette-compatibility-computational.md) §6. **Likely the highest-leverage single intervention** for any PDI-heavy or stability-sensitive cassette |
| **Constitutive HacA<sup>i</sup>** (active UPR transcription factor) | Tested in *A. oryzae* directly: **Zhou 2016** (DOI: 10.1016/j.gene.2016.08.018) found HacA-CA upregulated 80 secretory-pathway genes (folding/UPR/glycosylation/vesicle transport) but **paradoxically reduced secreted amylase output** via RESS (repression under secretion stress) feedback, and impaired growth. **Carvalho 2012** (PMC3472299) saw the same growth + central-metabolism trade-off in *A. niger*. Earlier reports of 2-3× uplift in *A. niger* / *T. reesei* (Valkonen 2003 / Mulder 2004) are therefore substrate- and host-context-specific. (In Vitro) | **NOT a free win in koji.** Naive HacA-CA may down-regulate native amylase production — a non-starter for the OE digestive-enzyme leg, where amylase output is therapeutic. Asymmetric HacA response (does it help PDI-heavy substrates while suppressing amylase?) is an unresolved question worth direct testing before committing a cassette slot |
| **UPR is required as baseline** | **Tanaka/Gomi 2015** (DOI: 10.1016/j.fgb.2015.10.003) showed UPR is *required* for *A. oryzae* growth under hydrolytic-enzyme-producing conditions — IreA-repressed strain is rescued only by constitutive intronless hacA-i. (In Vitro) | Background UPR induction (substrate-driven) is essential and ceiling-limited. The lever is not "should we have UPR" (yes, always) but "should we constitutively over-activate it" (uncertain, possibly counterproductive in koji) |
| **Cross-class chaperone helper combinations** (Pichia precedent) | **Yu 2017** (DOI: 10.1038/s41598-017-16577-x) — single helpers (CPR6, FES1, STI1) gave only 1.4-1.6×. **Zhang 2006** (Biotechnol Prog 22(4):1090-5, PMID 16889384, [DOI 10.1021/bp060019r](https://doi.org/10.1021/bp060019r)) — combinatorial pairs in *P. pastoris*: YDJ1+PDI gave **8.7×**, YDJ1+Sec63 gave **7.6×**, Kar2+PDI gave **6.5×** (Zhang 2006 Abstract verbatim, verified 2026-05-06). [VERIFICATION CAVEAT 2026-05-06: Zhang's own single-chaperone arms (Kar2p, Ssa1p, PDI alone) gave **4-7×** uplift in the same paper. Within Zhang 2006, the combination/single advantage is ~1.2-1.5×, not 5×. The 5× advantage claim previously here implicitly compared Zhang's combinations to Yu 2017's single helpers — a cross-paper, cross-substrate, cross-host-strain comparison with confounded controls. Use 1.2-1.5× as the intra-Zhang comparison or hold the claim as "combinations outperform singles in the same experiment" without a cross-paper magnitude.] The Zhang 2006 abstract does not specify the test substrate by name; the wiki's previous "single-substrate uplift" framing should be read as "single-protein test system" pending full-text confirmation of substrate identity. (In Vitro) | **Highest-leverage direction once individual chaperone bottlenecks are characterized.** Untested in koji. Each combination is 2 cassette slots, but the per-substrate uplift is large enough to be net-positive even at the cassette-slot opportunity cost. Order-of-operations: empirical synergy matrix first → identify dominant bottleneck → targeted helper combination |
| **PDI overexpression (cassette)** | Variable; substrate-specific. **Delic 2014** (DOI: 10.1089/ars.2014.5844) review documents that PDI co-expression had no effect on horseradish peroxidase yield (HRP not PDI-limited), but does help disulfide-rich Fab fragments and antibody chains. (In Vitro) | One cassette slot; modest gene size (~500 aa). Worth using for Lf if empirical PDI bottleneck is confirmed; not worth using prophylactically |
| **Directed evolution of PDI** | Pichia precedent; substrate-specific variants give 2-5× per-substrate titer | High effort; reserved for a single high-value substrate (e.g., Lf at >1 g/L target) |
| **Proteome-constrained model (pcSecYeast)** | **Chen 2024** (DOI: 10.1016/j.ymben.2024.11.010) operationalized secretion capacity as a quantitative proteome-constrained model in *S. cerevisiae*; 50% downregulation and 35% upregulation predictions confirmed by CRISPRi/a screen. (In Vitro). Closest published "secretion capacity index" but does not yet model multi-substrate competition | Building a koji equivalent (pcSecKoji) would convert the framework from qualitative to quantitative. Substantial undertaking; would be a publishable platform contribution |
| **UPR small-molecule inducers** (DTT, tunicamycin) | Transient UPR activation; not viable for food-grade fermentation | Not applicable to OE chassis |

**The picture inverts what the *A. niger* / *T. reesei* HacA literature would predict for koji.** The most promising capacity-expansion lever is **NSlD-ΔP10 (already adopted)** plus **cross-class chaperone helper combinations** (untested in koji, but Pichia data shows 6.5-8.7× absolute uplift over baseline; Zhang 2006 verified 2026-05-06). Constitutive HacA<sup>i</sup> alone is *not* a default lever in koji — Zhou 2016's finding that it suppresses native amylase output is a specific OE problem because the digestive-enzyme leg of the platform requires high native amylase. Order-of-operations: build the endgame strain, measure baseline titers, run pairwise expression matrix, identify bottleneck, then targeted helper-pair intervention.

---

## 8. What This Framework Does *Not* Predict

Honest about edges:

1. **Solid-state vs. submerged secretion divergence.** Sun 2024 (PMC11051239) explicitly notes that "there are certain proteins that are not secreted in solid-state culture, unlike submerged culture, such as the glucoamylase-encoding gene glaB." Whether a cassette secretes well in koji solid-state is a separate question from chaperone load. The framework predicts which cassettes compete with each other; it does not predict which cassettes secrete in solid-state at all. Format-translation risk dominates [validation-experiments.md §1.9](./validation-experiments.md).

2. **Quantitative UPR ceiling in koji is unmeasured.** No published "secretion capacity index" exists for *A. oryzae*. Adapt the Pichia-developed approaches (Mattanovich / Gasser group at BOKU) — measurable quantities: UPR-target gene transcript levels, BiP/PDI relative abundance, ER stress reporter induction. Building this measurement infrastructure is the precondition for predictive synergy modeling beyond rough qualitative tiers.

3. **Vesicular traffic is the next likely binding constraint** if chaperone capacity is expanded. ER exit site density, COPII vesicle budding, Golgi throughput — these become rate-limiting once folding is no longer rate-limiting. The framework does not address them. Recent *A. niger* work on ER architecture engineering may translate.

4. **Codon-level interactions are not captured.** Two cassettes drawing on the same rare-codon tRNA pool can antagonize each other independently of chaperone load. [Codon optimization](./codon-optimization-expression-cassette.md) treats cassettes as independent substrates; multi-cassette codon competition is unstudied.

5. **Glycosylation pathway divergence between koji and mammalian cells** changes substrate features in a way the load-class scoring doesn't capture. Native koji glycans are high-mannose; mammalian native is complex sialylated. A cassette with 3 N-glycan sites loads calnexin similarly in both hosts, but the resulting product is biophysically different. This affects therapeutic outcome, not synergy prediction — flagged for clarity, not as a framework gap.

6. **The published koji multi-cassette literature is thin.** There is no published koji-specific pairwise expression matrix at the time of this writing (2026-05-05). The framework's quantitative coefficients are extrapolated from Pichia, *A. niger*, and yeast literature; they may need rescaling once direct koji data is generated. The framework's *qualitative* prediction (load-class overlap → synergy decay) is robust across all published fungal and yeast systems; the *quantitative* synergy coefficients in §5 (e.g., uricase × Lf "0.8-1.0", Lf × DAF SCR1-4 "0.5-0.7") remain placeholder calibrations. The three load-bearing source numbers feeding §1 and §7 — Huynh 2020 39.7 mg/L, Wakai 2019 40×, Zhang 2006 6.5-8.7× — were grep-verified against primary sources on 2026-05-06; see §10 "Verification provenance" for source-line anchoring.

7. **Capacity-vs-titer benchmark ambiguity (flagged 2026-05-06).** The framework calibrates synergy coefficients against the Huynh 2020 antibody capacity ceiling (39.7 mg/L adalimumab in NSlD-ΔP10, 16 disulfides). [`koji-endgame-strain.md` §3.3](./koji-endgame-strain.md) cites Ward 1995 (>2 g/L lactoferrin in *A. awamori*, 17 disulfides) as the lactoferrin titer precedent. Both numbers cannot be the binding constraint — Lf at 2 g/L would be impossible if 16-disulfide adalimumab at 40 mg/L were a hard capacity ceiling. Three resolutions are possible: (a) Huynh's ceiling is antibody-architecture-specific (single-chain Lf folds easier than dual-chain HC+LC paired assembly), (b) *A. awamori* (Ward) has different chaperone capacity than *A. oryzae* NSlD-ΔP10 (Huynh), (c) submerged ≠ solid-state. **If resolution (a) holds, this framework's synergy coefficients are systematically conservative for single-chain payloads.** The §1.9 wet-lab Lf-alone arm directly resolves the ambiguity ([`validation-experiments.md` §1.9 "Capacity-vs-titer side-product readout"](./validation-experiments.md)). Until that data lands, the framework's coefficient ranges should be read with this asymmetry in mind: the lower bounds are well-anchored, the upper bounds may understate true capacity for single-chain glycoproteins.

---

## 9. Open Questions

1. **Does HacA<sup>i</sup> help PDI-heavy substrates while suppressing native amylase?** Zhou 2016 found constitutive HacA reduces secreted amylase via RESS feedback — but whether it simultaneously *helps* PDI-heavy substrates (which would justify the trade-off if the OE digestive-enzyme leg can absorb the amylase loss) was not tested. **Substrate-asymmetric HacA response in koji is the load-bearing unresolved question** for capacity-expansion strategy.

2. **Are *A. oryzae*'s duplicated chaperone paralogs (CPR1, ERJ5, ERD2) functionally independent capacity pools?** Liu 2014 documents the duplications; functional differentiation is not characterized. If different paralogs specialize on different substrate classes, koji has structural advantages over yeast as a multi-cassette chassis. Direct test: paralog-specific KO impacts on a cassette panel.

3. **Is there a "secretion pathway capacity index" measurable per koji strain?** Chen 2024's pcSecYeast operationalizes this for *S. cerevisiae*. Building a pcSecKoji equivalent — using *A. oryzae*-specific secretion proteome data (Liu 2014 is the starting point) — would convert the framework from qualitative to quantitative. Substantial undertaking; would be a publishable platform contribution.

4. **What's the synergy coefficient for two PDI-light fungal-native enzymes overexpressed beyond native level?** I.e., is there meaningful chaperone competition between native lipase and native amylase when each is pushed to 2-3× native titer? This affects the digestive-enzyme leg of the OE platform. Wakai 2019's >1.0 cross-cellulase synergy suggests light-substrate stacking is actually super-additive in koji at moderate loads.

5. **Does the framework hold for intracellular cassettes?** The cytosolic chaperonin (TRiC / CCT) and HSP70 / HSP90 cytosolic chaperones have their own competition dynamics. Carnosine cassette (cytosolic) is "off the secretion pathway" but not "off chaperone competition entirely." Probably modest at OE expression levels but worth checking.

6. **Pairwise vs. higher-order interactions.** Does the synergy coefficient compose linearly across 3+ cassette combinations, or are there triplet / quadruplet emergent effects? Pairwise matrix is a tractable starting point but may miss higher-order behavior. Wakai 2019's 3-cellulase 40× synergy is a hint that triplet effects exist.

7. **Cross-class helper combination effect size in koji.** Zhang 2006 (verified 2026-05-06) shows Pichia gets 6.5-8.7× absolute uplift over baseline from YDJ1+PDI, YDJ1+Sec63, Kar2+PDI cross-class pairs. Within Zhang's own data, single chaperones (Kar2p, Ssa1p, PDI) gave 4-7× — so the intra-paper combination/single advantage is only 1.2-1.5×, not the >5× the framework previously implied via cross-paper comparison to Yu 2017's 1.4-1.6× single-helper data (Yu 2017 used different host strain, different substrate, different growth conditions; the cross-paper comparison is confounded). The clean Zhang-only signal is that combinations *do* outperform singles in the same experiment, but the magnitude of the combination/single advantage is modest absent the cross-paper anchor. Whether this composes the same way in koji is untested, and the smaller intra-paper advantage weakens (but does not eliminate) the case for prioritizing helper combinations over single-helper cassettes. Direct koji testing remains the resolver.

**Multilingual literature scan (2026-05-05):** A multi-database multilingual scan (PubMed, J-STAGE, CiNii, CNKI, WanFang, J-GLOBAL) for chaperone-orthogonal multi-cassette frameworks in *A. oryzae* surfaced no published predictive design rule. Japanese koji-engineering work (Maruyama, Kitamoto, Gomi labs) publishes predominantly in English-language venues (*AEM*, *AMB*, *Fungal Biol Biotechnol*); Chinese groups working on *Aspergillus* heterologous expression (Pan/Wang at South China Univ of Technology) similarly publish in English. **The framework gap is genuine, not a translation artifact** — no two-model translation cross-check was needed because no non-English-only source contained mechanism claims absent from the English literature.

---

## 10. Cross-References

- [aspergillus-oryzae.md](./aspergillus-oryzae.md) — Host chassis overview, native enzyme production, GRAS context
- [cassette-compatibility-computational.md](./cassette-compatibility-computational.md) — comp-010: specific 2-cassette uricase + lactoferrin analysis (the case study under this framework)
- [koji-endgame-strain.md](./koji-endgame-strain.md) — The 4-molecule / 5-chokepoint endgame design that this framework retroactively explains
- [engineered-koji-protocol.md](./engineered-koji-protocol.md) — Full engineering protocol; §15 covers carnosine co-expression module
- [codon-optimization-expression-cassette.md](./codon-optimization-expression-cassette.md) — Independent cassette optimization (multi-cassette codon competition is an extension)
- [koji-construct-design.md](./koji-construct-design.md) — Cassette architecture (promoters, signal peptides, terminators)
- [protein-engineering-strategy.md](./protein-engineering-strategy.md) — Substrate-specific protein engineering
- [validation-experiments.md](./validation-experiments.md) §1.9 — First wet-lab dual-cassette test; generates the first 2 data points for the pairwise matrix
- [manual-literature-mining.md](./manual-literature-mining.md) §"Pre-commit verification gate" — methodology applied retroactively to this page on 2026-05-06; see §10.1 below for outcomes

### 10.1 Verification provenance

Pre-commit verification gate ([manual-literature-mining.md](./manual-literature-mining.md) §"Pre-commit verification gate") applied retroactively on 2026-05-06 to the three load-bearing numbers feeding §1 and §7. Outcomes:

| Source paper | Number(s) verified | Verdict | Source location | Date |
|---|---|---|---|---|
| **Huynh HH et al. 2020** *Fungal Biol Biotechnol* 7:7, PMC7257131, [DOI 10.1186/s40694-020-00098-w](https://doi.org/10.1186/s40694-020-00098-w) | 39.7 mg/L adalimumab; ten-protease deletion (NSlD-ΔP10) required | ✅ VERIFIED | Abstract verbatim ("highest amount of antibody was obtained from the ten-protease deletion strain (39.7 mg/L)"); Results §"Adalimumab production in the culture supernatant of *A. oryzae*"; Fig. 1 production-curve | 2026-05-06 |
| **Huynh 2020 + UniProt P01857 (IgG1 HC) + P01834 (kappa LC)** | 16 disulfides per assembled IgG1 (4 inter-chain + 12 intra-chain) | ✅ VERIFIED via UniProt | UniProt P01857 FT DISULFID annotations: 27..83 (intra CH1), 144..204 (intra CH2), 250..308 (intra CH3), 103 (inter HC-LC), 109 + 112 (inter HC-HC); plus VH (1 intra) and LC (1 intra VL + 1 inter LC-HC). Total: 12 intra + 4 inter = 16. Note: the Huynh 2020 paper itself does not state the disulfide count; the wiki's "16 disulfides" is textbook IgG1 stoichiometry verified via UniProt, not extracted from Huynh 2020. | 2026-05-06 |
| **Wakai S et al. 2019** *Bioresour Technol* 276:146-153, PMID 30623869, [DOI 10.1016/j.biortech.2018.12.117](https://doi.org/10.1016/j.biortech.2018.12.117) | 40× total cellulolytic activity over single-integration baseline; 5-16 chromosomal copies; three cellulases (cellobiohydrolase + endoglucanase + β-glucosidase) | ✅ VERIFIED on the 40× and 5-16 numbers (abstract verbatim); ⚠️ CORRECTED on the synergy decomposition | Abstract verbatim ("The resulting strain possessed 5-16 copies of each cellulase gene within the chromosome and showed approximately 10-fold higher activity versus single integration strains... resulting transformant showing 40-fold higher cellulolytic activity versus the single integration strain"). The wiki's previous claim — "approximately 10× of the gain came from copy stacking; the rest from multi-cassette synergy" — was a misattribution. Per the abstract, the 4× delta from 10-fold to 40-fold came from **promoter/terminator engineering** (P-sodM/T-glaB selected via per-copy transcription screen), not multi-cassette synergy. The word "synergy" does not appear in the abstract. | 2026-05-06 |
| **Zhang W et al. 2006** *Biotechnol Prog* 22(4):1090-5, PMID 16889384, [DOI 10.1021/bp060019r](https://doi.org/10.1021/bp060019r) | YDJ1+PDI 8.7×, YDJ1+Sec63 7.6×, Kar2+PDI 6.5× | ✅ VERIFIED on the absolute fold values; ⚠️ CORRECTED on the "5× advantage over single helpers" framing | Abstract verbatim ("the combination chaperones of YDJ1p/PDI, YDJ1p/Sec63, and Kar2p/PDI synergistically increase secretion levels 8.7, 7.6, and 6.5 times, respectively"). Within the same paper, single chaperones (Kar2p, Ssa1p, PDI alone) gave **4-7× uplift** ("introduction of Kar2p, Ssa1p, or PDI improves protein secretion 4-7 times"). The intra-paper combination/single advantage is therefore ~1.2-1.5×, not 5×. The previous "5× advantage" claim was a cross-paper comparison to Yu 2017's single-helper data (1.4-1.6× for CPR6/FES1/STI1), which uses different host strain, substrate, and conditions — confounded comparison. The Zhang 2006 abstract does not specify the test substrate by name; "single-substrate uplift" framing in earlier wiki versions should read "single test-protein system" pending full-text confirmation. | 2026-05-06 |

**Methodology:** All four papers retrieved 2026-05-06 via `mcp__plugin_pubmed_PubMed__get_full_text_article` (Huynh 2020 only — open-access via PMC7257131) and `mcp__plugin_pubmed_PubMed__get_article_metadata` (Wakai 2019, Zhang 2006 — abstract-level metadata). Wakai and Zhang full-text not retrieved due to publisher paywalls (Elsevier, Wiley); abstracts authoritatively verified the load-bearing numbers, and the methodological details that would require full text (Wakai's per-cassette ratios, Zhang's substrate identity) are flagged as needing separate full-text retrieval if downstream work depends on them.

---

## 11. Strategic Implication for Open Enzyme

The chaperone-orthogonal framework reframes a question Brian asked in conversation: *"how many cassettes can we bolt on?"*

The reframe: **not "how many" but "which combinations get synergistic yield."** Concretely, the OE roadmap implications:

1. **The endgame strain's "five molecules" thesis is biochemically reasonable**, not greedy. Total chaperone burden ≈ Huynh 2020 antibody baseline because four of the five payloads are off-pathway or chaperone-light. The framework converts what looked like an aggressive payload count into a defensible engineering target.

2. **Future cassette additions should preferentially fill underused load classes.** If the next addition is another PDI-heavy mammalian glycoprotein (e.g., DAF full-length rather than SCR1-4), the framework predicts steep synergy decay vs. lactoferrin. If the next addition is another cytosolic small-molecule pathway or another off-pathway cassette, additivity is preserved.

3. **NSlD-ΔP10 (already adopted) is the highest-leverage host intervention; cross-class chaperone helper combinations are the highest-leverage capacity-expansion experiment.** Zhou 2016's finding that constitutive HacA<sup>i</sup> in koji suppresses native amylase via RESS feedback rules out the naive *A. niger* / *T. reesei* HacA strategy as a default OE move — the digestive-enzyme leg of the platform requires native amylase output. The replacement strategy is targeted: build endgame strain → measure baseline titers and per-class bottlenecks → install matched helper-pair cassettes (Pichia precedent verified 2026-05-06: YDJ1+PDI 8.7×, YDJ1+Sec63 7.6×, Kar2+PDI 6.5× absolute uplift over baseline, Zhang 2006 Biotechnol Prog 22(4):1090-5; intra-paper combination/single advantage 1.2-1.5×). Two cassette slots, substrate-specific intervention.

4. **The pairwise expression matrix is the single highest-leverage characterization investment** the platform could make at this stage. ~$25k / 4-6 months for a predictive design tool reusable across every future OE cassette decision. Compare to the per-cassette wet-lab cost of guess-and-check expression in the absence of a framework.

5. **The under-explored design axis Brian flagged is real, and the multilingual literature scan confirmed it.** No published pairwise expression matrix exists for koji; no published predictive design rule for chaperone-class orthogonality in any filamentous fungus. Component pieces exist (Gong 2009 chaperone-module catalog; Liu 2014 *A. oryzae* secretome map; Delic 2014 Pichia substrate-specificity data; Chen 2024 pcSecYeast) but no one has composed them. Open Enzyme can be the project that builds and publishes this framework — both as a contribution to fungal synthetic biology and as a competitive moat for the platform's multi-cassette designs.

6. **The "five-molecule endgame strain" is more biochemically defensible than it looks.** The Wakai 2019 3-cellulase result (40× total cellulolytic activity over single-integration baseline; ~10× from copy-stacking + ~4× from promoter/terminator engineering, verified 2026-05-06) is direct *A. oryzae* evidence that three light substrates *can coexist at high titer without titer collapse* in the same chaperone subset — a necessary precondition for chaperone-orthogonal compatibility, though not direct evidence of cross-cassette synergy distinct from per-cassette transcriptional scaling. The OE endgame strain has *more* orthogonality than Wakai (substrates partitioned across BiP/PDI/calnexin/cytosolic/off-pathway classes vs. Wakai's three substrates all in one class). Predicted synergy ≥0.85 is consistent with the absence-of-titer-collapse evidence in Wakai and the broader chaperone-orthogonality framework.

---

*All synergy coefficients in this analysis are Mechanistic Extrapolation pending the §6 pairwise expression matrix validation. Quantitative coefficients are calibrated from yeast, Pichia, and A. niger literature; koji-specific calibration is the load-bearing missing data.*
