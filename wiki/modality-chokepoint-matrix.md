---
title: "Modality × Target Matrix — Exploration Surface"
date: 2026-04-28
tags:
  - modalities
  - chokepoints
  - exploration
  - platform-strategy
  - multi-modal
  - first-principles
related:
  - nlrp3-exploit-map.md
  - gut-lumen-sink.md
  - androgen-urate-axis.md
  - abcg2-modulators.md
  - open-questions.md
  - synthesis.md
  - open-source-platform.md
  - open-enzyme-vision.md
  - gout-pathophysiology.md
sources:
  - "Brian framing 2026-04-28: 'OE is the mission, not the koji chassis'"
  - "Synthesis derived from existing wiki pages (chokepoint map, transporter biology, exploit map)"
status: published
---

# Modality × Target Matrix — Exploration Surface

## Why this page exists

Open Enzyme is a living research output of an exploration mission, not a fixed koji-platform roadmap. The wiki has historically organized around mechanism (NLRP3 chokepoints CP0-CP6) and around chassis (engineered yeast / koji), and that mostly works — but it has a blind spot: **it doesn't make the orthogonal "what tools haven't we considered" search visible.** When a new modality lands in the broader scientific toolset (mRNA, base editing, engineered exosomes, kidney-tropic siRNA, etc.), there's no canonical place to ask "where in the gout / NLRP3 / urate-axis map could this open a door?"

This page is that place. **Rows are modalities** (small molecules, peptides, engineered organisms, RNA platforms, phages, etc.). **Columns are targets** — anatomical/cellular sites and pathway nodes where intervention is mechanistically relevant. Each cell answers one question: what's currently in OE here, what could plausibly go here from outside, and which cells are the genuine empty-space exploration vectors.

The matrix is **not** an attempt to commit OE to any particular new direction. It's a navigable map of the exploration surface — kept alive so the next sweep, the next paper, the next conversation can ask "which cell does this update?" rather than "does this fit the current chassis?"

The framing question per cell, per Brian (2026-04-28): **"What open questions might this modality answer at this target?"** — not "is this modality useful here?" The inversion is load-bearing.

## How to read this page

The matrix below uses a 5-symbol legend:

| Symbol | Meaning |
|:-:|---|
| ✅ | OE has live coverage at this cell — see linked wiki page |
| 🔬 | OE has partial / mechanism-relevant coverage; specific intervention not yet engineered |
| 🟡 | Open exploration vector — modality could plausibly answer a stuck question at this target; not currently in OE |
| ⚪ | Mechanistically possible but no realistic path / overkill / addressed by another modality |
| — | Not applicable / mechanism doesn't intersect target |

Cells marked 🟡 are where the most interesting nuggets live. Each one is a candidate "what gout-relevant problem could THIS open?" question. The "Open exploration questions" section below pulls the highest-leverage 🟡 cells into a queue.

---

## The matrix

Targets across the top, modalities down the side. Columns grouped by anatomical site / pathway access. Click into the per-modality and per-target sections below for the full per-cell prose.

### Row 1: Gut compartment targets

| Modality | Gut lumen (urate degradation) | Gut epithelium ABCG2 (transcellular secretion) | Gut macrophages (NLRP3 priming) | Gut barrier (TNFα cycle / LPS leak) | Gut microbiome (community shape) |
|---|:-:|:-:|:-:|:-:|:-:|
| Small molecules / supplements | ⚪ | ✅ ([sulforaphane](./supplements-stack.md)) | ✅ ([BHB](./bhb-ketones.md), [oridonin](./oridonin.md)) | ✅ ([zinc-carnosine](./carnosine.md)) | 🔬 ([berberine](./supplements-stack.md)) |
| Peptides | ⚪ | ⚪ | 🔬 ([KPV](./kpv-peptide.md)) | ✅ ([BPC-157](./bpc-157.md), [KPV](./kpv-peptide.md)) | — |
| Engineered yeast | ✅ ([uricase](./engineered-yeast-uricase-proposal.md)) | ⚪ | 🟡 (yeast-cell-wall β-glucan local NLRP3?) | 🔬 (transit organism) | 🟡 |
| Engineered koji | ✅ ([uricase](./engineered-koji-protocol.md), [carnosine](./carnosine.md), [lactoferrin](./engineered-koji-protocol.md)) | 🟡 (glucoraphanin co-production — see [open-questions](./open-questions.md)) | 🔬 (kojic acid, ergothioneine local) | ✅ (lactoferrin TNFα suppression) | 🔬 |
| Engineered LBPs (obligate anaerobes — Bacteroides / Faecalibacterium / Akkermansia) | 🟡 (genuine colonization vs. yeast/koji transit) | 🟡 (engineered Faecalibacterium for local butyrate at crypt) | 🟡 | 🟡 (engineered Akkermansia for mucus-layer repair) | 🟡 (community-level by design) |
| Engineered E. coli Nissle | ✅ ([PULSE](./engineered-yeast-uricase-proposal.md)) | ⚪ | 🟡 | 🟡 (engineered IL-22 secretion) | 🟡 |
| Bacteriophages | — | ⚪ | ⚪ | 🟡 (selective suppression of LPS-producing gram-negatives) | 🟡 (selective rather than additive) |
| Microbiome consortia / FMT | — | ⚪ | ⚪ | 🔬 | 🟡 (community-level) |
| Engineered exosomes | ⚪ | 🟡 (oral-route exosomes carrying ABCG2-inducer) | 🟡 (macrophage-tropic NLRP3 silencer) | 🟡 (claudin / ZO-1 modulator delivery) | — |
| mRNA / saRNA / circRNA + LNP | ⚪ | ⚪ (oral mRNA still research-stage) | 🟡 (myeloid-tropic LNP NLRP3 silencer) | ⚪ | — |
| siRNA / ASOs | ⚪ | ⚪ | 🟡 (myeloid-tropic NLRP3 / NF-κB silencer) | 🟡 (TNFα siRNA local) | — |
| CRISPR / base editing in patient | — | 🟡 (Q141K → Q141 base edit in crypt stem cells; delivery unsolved) | ⚪ | ⚪ | — |
| Antibodies / biologics | — | ⚪ | ⚪ | ⚪ (anti-TNFα systemic; overkill) | — |
| Engineered soluble complement regulators (sCR1, Factor H, DAF/CD55) | — | — | 🟡 (gut-luminal sCR1 / Factor H fragment / DAF ectodomain heterologously expressed in GRAS host for mucosal CP0 coverage — closes the wiki's only "honest platform gap") | ⚪ | — |
| Pharmacological chaperones | — | 🟡 (Q141K folding rescue à la CFTR-corrector class) | ⚪ | ⚪ | — |
| SPM precursors (DHA → RvD1/MaR1) | — | 🔬 | ✅ ([SPM](./spm-resolution-pathway.md)) | 🔬 | — |
| Fermentable fiber / prebiotics | — | ✅ ([butyrate → PPARγ → ABCG2](./abcg2-modulators.md)) | 🔬 | 🔬 (mucus-layer support) | ✅ |

### Row 2: Renal compartment targets

| Modality | Kidney URAT1 / GLUT9 (renal reabsorption) | Kidney ABCG2 (renal secretion) | Kidney macrophages (urate nephropathy) |
|---|:-:|:-:|:-:|
| Small molecules / supplements | 🔬 ([carnosine](./carnosine.md) — animal model only) | 🔬 (fenofibrate adjacent) | 🔬 |
| Peptides | ⚪ | ⚪ | ⚪ |
| Engineered yeast | — | — | — |
| Engineered koji | — | — | — |
| Engineered LBPs | — | 🟡 (systemic SCFA from gut → renal PPARγ?) | — |
| Engineered E. coli Nissle | — | — | — |
| Bacteriophages | — | — | — |
| Microbiome consortia / FMT | ⚪ | ⚪ | ⚪ |
| Engineered exosomes | 🟡 (kidney-tropic exosomes carrying URAT1 inhibitor) | 🟡 | 🟡 |
| mRNA / saRNA / circRNA + LNP | 🟡 (kidney-tropic LNPs are research-active; mRNA encoding URAT1-blocker?) | 🟡 (mRNA encoding wild-type ABCG2 to renal tubule) | 🟡 (NLRP3-silencer mRNA) |
| **siRNA / ASOs** | **🟡 (kidney-tropic siRNA against URAT1 mRNA — the cleanest "elegant solution"; megalin-binding conjugates are an active class)** | 🟡 | 🟡 |
| CRISPR / base editing in patient | 🟡 (renal tubule editing — delivery hard) | 🟡 (Q141K rescue at renal expression — same problem) | ⚪ |
| Antibodies / biologics | ⚪ | ⚪ | ⚪ |
| Pharmacological chaperones | 🟡 (URAT1 destabilizer / GLUT9 destabilizer — research-class for renal transporters) | 🟡 (Q141K folding rescue at renal site) | — |
| SPM precursors | — | — | 🔬 |
| Fermentable fiber / prebiotics | — | 🔬 (systemic SCFA → modest renal effect) | — |

### Row 3: Tissue-resident NLRP3 sites + acute flare

| Modality | Synovial macrophages (joint flare site) | Vessel-wall macrophages (Lp-PLA2 / chronic vascular inflammation) | Acute flare termination (IL-1β block) |
|---|:-:|:-:|:-:|
| Small molecules / supplements | ✅ (systemic [BHB](./bhb-ketones.md), [oridonin](./oridonin.md), [EGCG](./egcg.md)) | 🔬 (same systemic compounds, low local concentration) | 🔬 ([colchicine](./colchicine.md), prednisone) |
| Peptides | ⚪ (systemic peptides poorly absorbed) | ⚪ | ⚪ |
| Engineered yeast / koji | — | — | ⚪ (chronic only — no fast onset) |
| Engineered LBPs | — | 🟡 (systemic SCFA → vessel-wall PPARγ?) | — |
| Bacteriophages | — | — | — |
| Engineered exosomes | 🟡 (intra-articular exosome carrying NLRP3 inhibitor) | 🟡 (CD163 / mannose-receptor-tropic exosomes for Lp-PLA2 source macrophages) | 🟡 (rapid IL-1RA delivery) |
| **mRNA / saRNA / circRNA + LNP** | 🟡 (intra-articular mRNA-IL-1RA at flare onset) | **🟡 (myeloid-tropic LNP delivering NLRP3-silencer mRNA — the genuinely novel angle for Lp-PLA2)** | **🟡 (mRNA-IL-1RA pulse therapy IV — fits because flare is short-window; transient expression IS the right shape)** |
| siRNA / ASOs | 🟡 (NLRP3 silencer in joint tissue) | 🟡 (NLRP3 / NF-κB silencer in vessel-wall macrophages) | ⚪ (too slow for acute) |
| CRISPR / base editing in patient | ⚪ | ⚪ | ⚪ |
| Antibodies / biologics | ✅ (canakinumab, anakinra — exist, expensive) | 🔬 (no current biologic for vessel-wall NLRP3 specifically) | ✅ ($300K/yr canakinumab — the existing high-cost option) |
| Pharmacological chaperones | ⚪ | ⚪ | ⚪ |
| SPM precursors | ✅ ([SPM](./spm-resolution-pathway.md) — RvD1/MaR1 in animal MSU model) | 🔬 (DHA-emphasis rationale per [tnfsf14](./tnfsf14-gout-target.md)) | 🔬 |
| Fermentable fiber | — | 🔬 (systemic anti-inflammatory) | ⚪ |

### Row 4: Monitoring / detection

| Modality | Real-time UA monitoring | Chokepoint biomarker readout | Microbiome state monitoring |
|---|:-:|:-:|:-:|
| Lab panel (Quest / clinical) | ✅ (intermittent) | 🔬 ([self-experiment-protocol](./self-experiment-protocol.md) — pending CP-biomarker map per [synthesis #4](./synthesis.md)) | ⚪ |
| Wearable sensors | 🟡 (sweat UA — UCSD / Stanford research; ~5 yr from clinical) | ⚪ | ⚪ |
| Microneedle patches | 🟡 (continuous interstitial UA — research-stage CGM-equivalent) | ⚪ | ⚪ |
| Implantable monitors | 🟡 (overkill for gout-only; unit economics flip if multi-marker) | 🟡 (multi-analyte) | ⚪ |
| Stool 16S / shotgun sequencing | ⚪ | ⚪ | 🔬 (Onegevity, Viome — getting cheaper) |
| At-home immune-cell profiling | ⚪ | 🟡 (citH3 / cfDNA / aggNET ratio per [synthesis #7](./synthesis.md)) | ⚪ |

---

## Per-modality details (rows)

### Engineered yeast / koji
- **Strengths:** GRAS, food-grade, home-fermentable, dual-enzyme (uricase + carnosine + lactoferrin co-expression), gut-lumen sink mechanism is the cleanest fit for these chassis.
- **Coverage gaps relative to platform mission:** anything that requires durable colonization, anything renal, anything systemic at high titer.
- **Live OE pages:** [`engineered-koji-protocol.md`](./engineered-koji-protocol.md), [`engineered-yeast-uricase-proposal.md`](./engineered-yeast-uricase-proposal.md), [`koji-home-fermentation.md`](./koji-home-fermentation.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md).

### Engineered LBPs (obligate anaerobes — Bacteroides / Faecalibacterium / Akkermansia)
- **Strengths:** genuine colonization vs. transit. *Faecalibacterium prausnitzii* engineering is the obvious play for sustained colonic butyrate (relevant to [`abcg2-modulators.md`](./abcg2-modulators.md) ABCG2 induction + Q141K rescue). *Akkermansia muciniphila* is mucus-layer-resident — the natural barrier-repair chassis. *Bacteroides* offers the broadest metabolic engineering toolkit (Sonnenburg lab, others).
- **Coverage gaps relative to current OE:** **the wiki has no dedicated page on this chassis class.** Brian-side Pendulum probiotic uses Akkermansia + butyrate-producers commercially; the engineering thesis for OE hasn't been developed.
- **Open exploration questions:** see [`open-questions.md` §"Co-engineered substrate-supply mechanisms"](./open-questions.md). Engineered Faecalibacterium for local butyrate is the highest-leverage candidate.
- **Regulatory class:** LBP framework (FDA 2018 guidance); same general lane as PULSE-style engineered E. coli Nissle, **distinct from yeast/koji food path.** Worth a dedicated wiki page.
- **Critical product-thesis limitation:** obligate anaerobes cannot be home-fermented. The Open Enzyme home-fermentation thesis (grow koji at home, make shio-koji or amazake condiment) does not transfer to *F. prausnitzii* or *Akkermansia* — these are strict anaerobes requiring anaerobic bioreactor culture, cold-chain stabilization, and regulatory handling as Live Biotherapeutic Products (LBPs). An engineered *F. prausnitzii* is a commercial pharmaceutical product, not a home recipe. This is a fundamental platform-type distinction: LBP vector = commercial manufacturing + distribution track, not the "democratized home access" track the koji chassis enables.
- **Dedicated scope page (committed 2026-05-05):** [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) formalizes this row as a peer track to the koji chassis under the broader Open Enzyme mission. Six in silico Phase 2 follow-ups are queued (engineering toolkit lit scan, commercial/clinical landscape lit scan, FDA LBP regulatory path lit scan, comp-008 *F. prausnitzii* expression feasibility, falsification card H02, comparative chassis matrix for gout). Phase 3 (content-triggered): platform-framing reflection on whether the LBP track justifies expanding Open Enzyme's framing from "engineered enzymes in koji" to "solve gout, every avenue, fully open."

### Bacteriophages
- **Strengths:** **selective suppression** rather than additive probiotic. Could selectively reduce LPS-producing gram-negatives (gut barrier / TNFα cycle relief), purine-fermenting Bacteroides species (luminal urate substrate reduction), or specific dysbiosis patterns identified by sequencing.
- **Current OE coverage:** zero. No wiki page.
- **Clinical context:** approved in several Eastern European jurisdictions; compassionate-use US; clinical programs at Adamas, Locus, Phaxiam, BiomX. AMR-associated infection is the lead indication; microbiome-modulation indications are next wave.
- **Open exploration questions:** does selective phage-mediated gut microbiome reshaping shift serum UA in hyperuricemia models? Does it reduce hs-CRP / Lp-PLA2 in chronic-inflammation gout patients? No clinical data, but mechanistically defensible — the Open Enzyme thesis would benefit from explicitly evaluating phages as a complementary modality to engineered organisms.

### mRNA / saRNA / circRNA platforms
- **Strengths:** transient expression (good for pulse therapy), sequence-specific (any encodable protein), lipid nanoparticle delivery (LNP) is a maturing platform.
- **Best-fit cells in the matrix:**
  1. **Acute flare termination via IV mRNA-IL-1RA pulse.** Transient expression IS the right shape — flare is short-window. mRNA-IL-1RA is a hypothetical canakinumab-equivalent at variable cost. Currently zero programs.
  2. **Myeloid-tropic LNP delivering NLRP3-silencing mRNA / siRNA to vessel-wall macrophages.** Brian's persistent Lp-PLA2 across panels is exactly the source — chronically activated vessel-wall macrophages. Acuitas, Moderna, others have myeloid-tropic LNP programs (mostly oncology-directed). For gout: nobody.
- **Worst-fit cells:** anything renal (kidney-tropic LNPs immature), anything in the gut (oral mRNA still research-stage), anything requiring durability (mRNA half-life is days at best).
- **Adjacent platforms worth tracking:** **self-amplifying mRNA (saRNA)** for lower dose / longer expression; **circular RNA (circRNA)** for resistance to exonucleases (Orna Therapeutics); these change the durability calculus.

### siRNA / ASOs
- **Strengths:** sequence-specific knockdown of any expressed gene; GalNAc conjugates already approved (inclisiran, patisiran) for liver targets; **kidney-tropic conjugate chemistry is an active research class** (megalin binding, kidney-cortex selectivity).
- **Best-fit cells in the matrix:**
  1. **Kidney URAT1 silencing.** This is **the cleanest "elegant solution"** in the entire matrix: sequence-specific knockdown of the renal-reabsorption transporter that drives Brian's hyperuricemia phenotype. Eliminates the dose-dependent off-target profile of small-molecule URAT1 inhibitors (benzbromarone hepatotoxicity). No clinical program for gout that I know of.
  2. **Macrophage NLRP3 silencing** — slower than mRNA-IL-1RA pulse but more durable.
  3. **Local TNFα siRNA in gut macrophages** — finer than systemic anti-TNFα biologic.
- **Worst-fit cells:** acute flare (too slow), anything that requires de novo protein expression rather than knockdown.

### CRISPR / base editing / prime editing in patient
- **Strengths:** durable correction, single-edit mechanism for Q141K-style point variants.
- **Best-fit cells:** Q141K → Q141 base edit in gut crypt stem cells. Mechanistically perfect; **delivery unsolved.**
- **Worst-fit cells:** everything else. Differentiated tissue editing wastes the durability advantage; nothing approved for non-hematopoietic somatic editing yet.
- **Status:** wait-and-see. Five-to-ten-year horizon for the delivery side. The OE thesis competes by sidestepping the editing problem entirely (gut-lumen sink + ABCG2 induction).

### Pharmacological chaperones
- **Strengths:** small molecules that bind misfolded protein variants (e.g., Q141K) and rescue trafficking. CFTR-corrector class (ivacaftor, tezacaftor, elexacaftor) is the precedent — multibillion-dollar therapeutic class for ΔF508 in CF.
- **Best-fit cells:** **Q141K folding rescue at the gut and renal sites simultaneously**, oral systemic delivery. Pharmacologically similar to the CFTR play.
- **Current research activity for ABCG2 Q141K specifically:** academic literature exists (Basseville 2012, others); **no clinical programs.** The market is small (gout has cheap alternatives), but mechanistically this is the cleanest non-genetic Q141K solution.
- **Open exploration question:** is the CFTR-corrector class chemistry transferable to ABCG2? Same ATP-binding cassette superfamily; the design problem is similar.

### Engineered exosomes
- **Strengths:** native cell-derived nanocarriers; bilayer + surface-marker engineering; can carry small molecules, peptides, RNA, or proteins; cell-tropic via surface marker selection.
- **Best-fit cells:**
  1. **Macrophage-tropic exosomes carrying NLRP3 inhibitors** (Lp-PLA2 source). CD163 or mannose-receptor display.
  2. **Kidney-tropic exosomes carrying URAT1 inhibitors or chaperones.**
  3. **Intra-articular exosomes for acute flare** carrying IL-1RA or NLRP3 silencer.
- **Status:** research-stage clinically; Codiak/Lonza alumni and several startups (Vesigen, Aegle, Ilias). For OE: a future complementary modality, not a near-term build.

### Engineered soluble complement regulators (sCR1, Factor H, DAF/CD55)
- **Strengths:** **closes the only "honest platform gap" in the OE corpus.** [`complement-c5a-gout.md`](./complement-c5a-gout.md) identifies CP0 (complement priming via C5a) as a dominant upstream chokepoint with no fermentable coverage — and `validation-experiments.md` §1.21 (executed 2026-04-27) confirmed via computational scan of ChEMBL / NPASS / LOTUS / Open Targets that **no validated natural-product C5aR1 antagonists exist.** This forced the platform to formally accept avacopan (a prescription pharma drug) as a permanent adjunct — awkward against the "your microbe makes the medicine" thesis. **The unexplored alternative** is to express endogenous human soluble complement regulators heterologously in the gut: sCR1 (soluble complement receptor 1), Factor H fragments, or DAF/CD55 ectodomain — proteins that already exist clinically as systemic IV biologics for autoimmune disease but have never been engineered for gut-luminal mucosal-complement coverage.
- **Best-fit cells in the matrix:** gut macrophages NLRP3 priming (the CP0 step); plausibly gut barrier (complement deposition contributes to barrier dysfunction).
- **Coverage gap relative to current OE:** **the wiki has no page on this.** All four candidate proteins (sCR1, Factor H, DAF/CD55, CD46) are in the human proteome — UniProt-fetchable, AlphaFold-modelled, MEROPS-screenable for shio-koji compatibility (the same comp-NNN protease-stability framework used for uricase and lactoferrin would apply directly).
- **Open exploration questions:**
  1. Can a soluble complement regulator be expressed in *A. oryzae* or *S. cerevisiae* at gut-luminal concentrations meaningful for mucosal C5a neutralization? sCR1 is ~190 kDa with 30 SCR domains — possibly too large for koji secretion. Factor H is ~150 kDa with 20 SCR domains. **DAF (CD55) ectodomain is ~70 kDa with 4 SCR domains — likely the most tractable engineering target.**
  2. Does mucosal C5a inhibition (luminal-side) meaningfully blunt CP0 priming? The macrophages doing the priming are submucosal — does luminal sCR1 / Factor H reach them, or does it require basolateral access?
  3. Same protease-stability question as uricase / lactoferrin: do the SCR (short consensus repeat) domains survive the koji fermentation environment? Run a comp-NNN analysis (e.g., comp-006) on the AlphaFold model of CD55 before any wet-lab engineering.
- **Status:** **zero programs.** All systemic complement-regulator biologics (TP10/sCR1 by Avant, mirococept by Univ. Oxford, ARC1905 anti-C5 aptamer) target IV / intravitreal delivery for autoimmune indications. **A gut-luminal mucosal-complement strategy is genuinely unexplored** and well-aligned with the OE chassis.
- **comp-006 protease-stability result (2026-05-05, Mechanistic Extrapolation):** AlphaFold pLDDT analysis of DAF/CD55 (P08174) under shio-koji conditions (17.5% NaCl, pH 4.5–5.0) returned **HIGH** for the soluble ectodomain (aa 35–353, max risk score 0.388, worst protease NPr). The verdict is **stalk-contingent**: the Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52) is fully disordered and drives all 9 NPr-exposed and 48 ALP-exposed ectodomain sites. The SCR1–4 domains (aa 35–285, pLDDT 85–98) contribute zero exposed sites. A stalk-truncated construct (aa 35–285, SCR1–4 only) would likely return a LOW verdict — comp-007 is the logical follow-up. See [`wiki/daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md).
- **Regulatory class:** if expressed in food-grade GRAS organism (koji, S. boulardii), this stays in the OE chassis lane — distinct from the systemic sCR1 biologic regulatory path. Same lane as engineered uricase / lactoferrin.

### Microbiome consortia / FMT
- **Strengths:** community-level intervention rather than single-strain. Vowst (Seres) FDA-approved 2023 for C. diff is the precedent.
- **Best-fit cells:** gut microbiome reshaping at community level; gut barrier; potentially distal effects via systemic SCFA.
- **Status:** zero programs for gout. Mechanistically defensible — adjacent indications (IBD, C. diff, metabolic syndrome) have positive signals.

### Antibodies / biologics
- **Existing in gout:** rasburicase, pegloticase (uricase variants — IV protein replacement, refractory gout). Canakinumab (IL-1β biologic, FDA-approved for gout 2023, very expensive). Anakinra (IL-1RA, off-label). All addressed in [`gout-clinical-pipeline.md`](./gout-clinical-pipeline.md).
- **Coverage gap:** the wiki tracks the existing biologics but doesn't catalog them as a modality class with their own row of cells where novel engineering could land (e.g., bispecifics, Fc-fusion uricases, CD163-targeted ADCs delivering NLRP3 inhibitors to Lp-PLA2-source macrophages).

### Wearable / implantable monitoring
- **Best-fit cells:** real-time UA monitoring; multi-analyte chokepoint biomarker readout.
- **Status:** sweat-based UA sensors are research-active (UCSD, Stanford); microneedle continuous monitoring is research-stage. Implantable multi-analyte is overkill for gout-only but flips when bundled with cardiometabolic indications.
- **Why this matters for OE:** any therapeutic intervention that's titrated against UA (carnosine dose, fiber load, clomid titration for the androgen-driven case) benefits from continuous data over discrete quarterly panels. The synthesis-queue chokepoint-biomarker map ([`synthesis.md`](./synthesis.md) #4) is partly bottlenecked by infrequent sampling.

---

## Per-target details (columns)

### Gut lumen
The most-developed target in the OE wiki — the gut-lumen sink is the platform's thesis. Multi-modal coverage is solid (yeast, koji, E. coli Nissle precedent). Gap: phages and microbiome-consortia don't appear; both are mechanistically relevant for shaping the microbial community whose metabolism produces the urate substrate.

### Gut epithelium ABCG2
Fairly well-covered via fiber → butyrate → PPARγ. Sulforaphane (Nrf2) supplements; glucoraphanin co-production in koji is open (per [`abcg2-modulators.md`](./abcg2-modulators.md) Engineering Implications #1). The Q141K rescue mechanism sits adjacent.

### Gut macrophages
Small molecules systemic absorption is the current lever. Local action via engineered organisms (β-glucan from yeast cell wall, kojic acid from koji metabolites, KPV via PepT1 absorption) is partial. RNA-platform delivery (LNP-targeted to gut myeloid cells) is open and unexplored.

### Gut barrier
Peptide layer (BPC-157, KPV, zinc-carnosine) + lactoferrin co-expression in koji + fermentable fiber. Engineered Akkermansia and engineered IL-22-secreting probiotics are the obvious novel additions.

### Gut microbiome (community shape)
Berberine (small molecule) + fermentable fiber. Phages and microbiome consortia are the modalities specifically built for community-level intervention; both absent from the wiki.

### Kidney URAT1 / GLUT9
**The biggest coverage gap in the matrix.** Carnosine is the only OE-relevant modality, and it's animal-model evidence only. siRNA against URAT1 mRNA via kidney-tropic conjugates is the cleanest novel angle in the entire matrix — sequence-specific, no off-target small-molecule profile, eliminates the historical benzbromarone hepatotoxicity concern.

### Kidney ABCG2
Indirect coverage via systemic SCFA from gut fiber. Direct kidney-targeted ABCG2 induction is open; pharmacological chaperones for Q141K at the renal site are open.

### Kidney macrophages (urate nephropathy)
Sparse coverage. SPM precursors have weak evidence for renal macrophage modulation. Systemic small molecules reach but at low local concentration.

### Synovial macrophages (joint flare site)
Existing biologics work (canakinumab, anakinra). Systemic small molecules. Intra-articular delivery (exosomes, mRNA-IL-1RA) is open and would compete with biologics on cost.

### Vessel-wall macrophages (Lp-PLA2)
**Brian-specific significance.** Persistent Lp-PLA2 elevation across his 2023-2025 panels while hs-CRP normalized. Systemic small-molecule reach is partial; **myeloid-tropic LNPs delivering NLRP3-silencing payloads is the genuinely novel exploration vector here.** Also: DHA-emphasis omega-3 (RvD1/MaR1) is the closest current OE-aligned tool — see [`spm-resolution-pathway.md`](./spm-resolution-pathway.md).

### Acute flare termination
OE has zero fast-acting tools. Existing options are pharma (colchicine, prednisone, anakinra, canakinumab). **mRNA-IL-1RA pulse therapy is the open exploration vector** — transient expression matches the short flare window.

### Real-time monitoring
No OE coverage. Wearable / microneedle / implantable are open vectors. For self-experiment purposes ([`self-experiment-protocol.md`](./self-experiment-protocol.md)), continuous UA data would change the kinetics of intervention titration.

---

## Open exploration questions surfaced by the matrix

The cells where 🟡 marks the genuinely novel exploration space, ordered by leverage:

1. **siRNA against URAT1 mRNA via kidney-tropic conjugate.** Sequence-specific renal-reabsorption knockdown. Cleaner than benzbromarone-class. Adjacent to inclisiran-style precedent. Zero clinical programs for gout. Mechanism: see [`androgen-urate-axis.md`](./androgen-urate-axis.md), [`gout-pathophysiology.md`](./gout-pathophysiology.md).

2. **Engineered Faecalibacterium prausnitzii for local butyrate at the gut crypt.** Hits both wild-type ABCG2 (PPARγ) and Q141K (HDAC trafficking rescue) per [`abcg2-modulators.md`](./abcg2-modulators.md). Genotype-agnostic; durable colonization avoids the "eat koji daily" adherence problem. Engineering precedent: Sonnenburg lab work on Bacteroides genome editing transfers conceptually.

3. **Myeloid-tropic LNP delivering NLRP3-silencing mRNA / siRNA to vessel-wall macrophages.** Brian-pattern Lp-PLA2 persistence is the n=1 case study. Acuitas / Moderna myeloid LNPs exist for oncology; gout repurposing is novel.

4. **Pharmacological chaperone for ABCG2 Q141K folding rescue.** CFTR-corrector class precedent (~$10B annual market for ΔF508 correction). Same ATP-binding cassette superfamily. Academic mechanism literature exists; no clinical programs. Could be a small-molecule discovery campaign with AI-era binder design.

4b. **Gut-luminal soluble complement regulator (sCR1 / Factor H / DAF/CD55 ectodomain) expressed in GRAS host for CP0 mucosal coverage.** Closes the only "honest platform gap" in the OE corpus — `complement-c5a-gout.md` flags CP0 as having no fermentable coverage; `validation-experiments.md` §1.21 confirmed zero natural-product C5aR1 antagonists exist. All four candidate proteins are human-endogenous, UniProt-fetchable, AlphaFold-modelled. **DAF/CD55 ectodomain (~70 kDa, 4 SCR domains) is the most tractable engineering target** (vs. sCR1 at 190 kDa / 30 SCR domains). Zero programs anywhere — all clinical complement regulators target systemic IV delivery. Mucosal-luminal expression is unexplored. **comp-006 (2026-05-05):** protease-stability analysis of the CD55 soluble ectodomain (aa 35–353) under shio-koji conditions returned HIGH (max risk 0.388, NPr worst protease). The verdict is **stalk-contingent** — the SCR1–4 domains are well-folded (zero exposed sites); the Ser/Thr-rich stalk (aa 286–353, pLDDT 30–52) drives all exposed-site risk. Next step: comp-007 on the SCR1-4-only truncation (aa 35–285), expected LOW verdict. See [`wiki/daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md).

5. **mRNA-IL-1RA pulse therapy for acute flare termination.** Transient expression matches flare window. Zero programs; mechanistically defensible; competes with canakinumab on cost (mRNA manufacturing scales; $300K/yr biologic doesn't).

6. **Engineered Akkermansia muciniphila for mucus-layer barrier repair.** Different chassis from yeast/koji. Mucus-resident colonization solves the transit-time problem. Adjacent to commercial Pendulum probiotic.

7. **Bacteriophage-mediated selective suppression of LPS-producing or purine-fermenting gut species.** Different from "add-an-organism" thesis. Mechanistically distinct from probiotic addition. No gout programs.

8. **Wearable sweat-based or microneedle continuous UA monitoring.** Changes intervention-titration kinetics. UCSD / Stanford research-stage.

9. **Glucoraphanin co-production in engineered koji.** Already flagged in [`abcg2-modulators.md`](./abcg2-modulators.md) Engineering Implications #1 and the just-added [`open-questions.md` §"Co-engineered substrate-supply mechanisms"](./open-questions.md). Same product, two mechanisms (substrate degradation + substrate supply).

10. **Engineered exosomes carrying NLRP3 inhibitors targeted to CD163+ macrophages.** Specifically for vessel-wall and synovial sites. Research-stage chassis; longer horizon than #1-3 above.

---

## Cross-references

- [`open-questions.md`](./open-questions.md) — meta-index where the leverage-bearing matrix cells should propagate as named open questions
- [`synthesis.md`](./synthesis.md) — action queue; expect new connections to surface here when the sweep daemon reads this page
- [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md) — the chokepoint map this matrix sits orthogonal to
- [`abcg2-modulators.md`](./abcg2-modulators.md), [`androgen-urate-axis.md`](./androgen-urate-axis.md), [`gut-lumen-sink.md`](./gut-lumen-sink.md) — the transporter-biology trio that grounds the renal and gut columns
- [`open-source-platform.md`](./open-source-platform.md) — platform-strategy positioning; this matrix supports its "we explore all angles" claim
- [`open-enzyme-vision.md`](./open-enzyme-vision.md) — top-level mission statement that the matrix operationalizes

## Maintenance

- **When a new modality lands in the broader scientific toolset:** add it as a row; ask the framing question per cell ("what gout-relevant problem could this open?"); flag the cells where it's genuinely novel.
- **When a new chokepoint, transporter, or biomarker surfaces:** add it as a column; re-evaluate which rows light up.
- **When OE makes a new build commitment:** mark the cell ✅ and link to the canonical wiki page; the matrix becomes the index.
- **The matrix is a meta-tool for exploration, not a roadmap.** Don't pretend a 🟡 cell is committed work; don't pretend a ⚪ cell is forever closed.
