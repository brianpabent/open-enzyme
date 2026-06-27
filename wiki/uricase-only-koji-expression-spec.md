---
title: "Uricase-Only Koji Expression Spec"
date: 2026-06-27
tags:
  - koji
  - aspergillus-oryzae
  - uricase
  - uaZ
  - expression-spec
  - validation-experiments
  - phase-0
  - measurement
related:
  - validation-experiments.md
  - engineered-koji-protocol.md
  - koji-construct-design.md
  - koji-endgame-strain.md
  - uricase.md
  - uricase-cassette-ranking-computational.md
  - uricase-protease-stability-computational.md
  - cassette-compatibility-computational.md
  - enzyme-quantification-protocol.md
  - quantification-ladder.md
  - hypotheses/H01-ward-dual-cassette.md
sources:
  - "Legoux R, Delpech B, Dumont X, et al. J Biol Chem 1992;267(12):8565-70 (PMID: 1339455) - A. flavus uaZ cloning"
  - "Machida M et al. Nature 2005;438(7071):1157-61 (PMID: 16372010) - A. oryzae RIB40 genome"
  - "Tada S et al. PMID 1937733 - amyB / Taka-amylase A promoter characterization"
  - "comp-001 - uricase shio-koji protease stability computational prior"
  - "comp-010 - dual-cassette cassette compatibility computational prior"
  - "comp-022 - uricase cassette ranking computational prior"
status: draft
---

# Uricase-Only Koji Expression Spec

This page defines the first engineered-koji wet-lab gate: express functional *Aspergillus flavus* uricase in *A. oryzae* before adding lactoferrin. It consolidates the uricase-only branch already implied by [validation-experiments.md §1.5](./validation-experiments.md#15-koji-uricase-expression-and-activity), [koji-construct-design.md](./koji-construct-design.md), [uricase.md](./uricase.md), and [koji-endgame-strain.md](./koji-endgame-strain.md).

This is a design and measurement spec, not a transformation SOP. Live engineered *A. oryzae* work belongs in a reviewed lab or qualified partner workflow with organism handling, containment, verification, and disposal covered by institutional protocols. The home-distributed side of the Open Enzyme ladder remains wild-type koji, assay calibration, commercial enzyme controls, and nonviable or clarified material where appropriate.

## 1. What This Experiment Decides

**Primary question.** Can *A. flavus* `uaZ` / `uox` uricase be expressed in *A. oryzae* koji as an active enzyme at a level that justifies continuing the koji engineering track? Evidence level: **In Vitro target, Mechanistic Extrapolation until wet-lab readout**.

**Secondary question.** Does adding a single uricase cassette preserve the useful native koji phenotype: kojic acid production plus amylase, protease, and lipase activity? This matters because the koji chassis is not just a container for uricase; native metabolites and digestive enzymes are part of the platform value. Evidence level: **In Vitro target**.

**Strategic role.** A green uricase-only result does not prove the [Ward 1995 dual-cassette thesis](./hypotheses/H01-ward-dual-cassette.md). It earns the right to run that harder experiment. A red uricase-only result stops the dual-cassette spend before lactoferrin is added.

## 2. Design Constraints

| Constraint | Design implication | Source |
|---|---|---|
| Uricase-only is the Phase 0 / Year 1 starting strain | Start with the smallest useful engineered construct before lactoferrin | [koji-endgame-strain.md](./koji-endgame-strain.md) |
| *A. flavus* `uaZ` is the default koji-track payload | Use UniProt Q00511 / GenBank X61766.1 as the reference protein identity | [uricase.md](./uricase.md), [engineered-koji-protocol.md](./engineered-koji-protocol.md) |
| RIB40 remains acceptable for uricase-only | Do not spend the protease-deletion chassis on the first uricase question unless a partner already has it | [validation-experiments.md §1.9](./validation-experiments.md#19-ward-1995-dual-cassette-feasibility-test-koji-endgame-strain-gate-1-priority-gate) |
| Uricase is not lactoferrin | Prefer direct secretion; do not import the Ward glucoamylase-KEX2 lactoferrin architecture unless the direct design fails | [uricase-cassette-ranking-computational.md](./uricase-cassette-ranking-computational.md) |
| Native koji phenotype is part of the product thesis | Measure kojic acid, amylase, protease, and lipase in the same run | [enzyme-quantification-protocol.md](./enzyme-quantification-protocol.md), [quantification-ladder.md](./quantification-ladder.md) |
| Public OE artifacts must not depend on private health context | Keep personal symptom data, medication history, and household notes out of this page | umbrella privacy rule |

## 3. Candidate Construct Architecture

The uricase-only build should inherit the comp-022 design direction rather than the older one-candidate cassette from [koji-construct-design.md](./koji-construct-design.md):

- **Payload:** *A. flavus* uricase, `uaZ` / `uox`, UniProt Q00511. Evidence level: **In Vitro precedent + Clinical Trial parent enzyme through rasburicase, route differs**.
- **Expression logic:** starch-linked *A. oryzae* expression remains the default for solid-state koji because the substrate itself supplies the induction context. Evidence level: **Mechanistic Extrapolation from *A. oryzae* industrial expression literature**.
- **Secretion logic:** direct secretion is the preferred uricase architecture. comp-022 found the glucoamylase-KEX2 fusion scaffold unnecessary for uricase because uricase has no intrinsic disulfide/glycosylation problem that benefits from a carrier. Evidence level: **Mechanistic Extrapolation, in silico**.
- **Gene-synthesis refinements:** comp-022 promotes three zero-marginal-cost refinements for the uricase cassette: a 5-prime-softened codon variant, a C-terminal PTS1-blocking tag, and N191Q glycosylation-sequon ablation. These should be treated as design candidates to hand to a qualified build partner, not as a home transformation recipe. Evidence level: **Mechanistic Extrapolation, in silico**.

The spec should not proceed to a sequence-order or strain-release step until the build partner has produced a construct map, containment plan, analytical plan, and material-return plan.

## 4. Experimental Arms

Minimum comparison set:

| Arm | Purpose |
|---|---|
| Wild-type parental *A. oryzae* | Native phenotype baseline and assay-interference baseline |
| Uricase-only clone A | First independent expression datapoint |
| Uricase-only clone B | Reproducibility and clone-position-effect check |
| Uricase-only clone C, optional | Adds resilience if clone A or B is a positional outlier |
| Commercial purified uricase control | Activity assay positive control; not a food or dosing material |
| Matched inactive extract or heat-inactivated enzyme control | Controls for non-enzymatic urate loss and matrix interference |
| Buffer and substrate blanks | Spectral and HPLC/LC-MS baseline subtraction |

If a partner lab can only return nonviable material, prioritize clarified extracellular fraction, total extract, and raw analytical data. Live engineered strain transfer should be a separate deliberate decision, not the default output of this gate.

## 5. Readout Matrix

| Readout | Required output | Pass signal | Notes |
|---|---|---|---|
| Construct / strain identity | Partner-lab verification report | Insert identity and clone identity are unambiguous | Use the partner's validated QC workflow; OE needs raw files or signed summary |
| Uricase protein | Western, ELISA, targeted MS, or equivalent | Uricase detected in engineered arms and absent from WT | Protein detection alone is not success |
| Uricase activity | Urate depletion assay plus orthogonal urate/allantoin confirmation where possible | Activity above WT background and reproducible across independent clones | The existing §1.5 floor is >20 umol/h/OD; H01's later dual-cassette floor is >=50 umol/h/OD |
| Localization | Extracellular fraction vs. total extract | Secretion or recoverable total activity matches the intended delivery model | If activity is only intracellular, downstream GI-release design changes |
| Kojic acid | HPLC or LC-MS | Within 30% of WT for green; >50% loss is red | Mirrors H01 native-metabolite thresholds |
| Amylase | DNS or starch-iodine ladder method | No material collapse vs. WT under matched conditions | Absolute units require Tier 3 calibration |
| Protease | Azocasein, ninhydrin, gelatin, or skim-milk plate ladder method | No material collapse vs. WT under matched conditions | Protease is both phenotype and payload-risk context |
| Lipase | p-NPP, oil-emulsion, or outsourced activity assay | No material collapse vs. WT under matched conditions | Lipase is the EPI-relevant native-enzyme bottleneck |
| Aflatoxin screen | Outsourced or qualified analytical panel when material is food-adjacent | No detected elevation above applicable food limit | Any positive result is a stop condition |

For amylase, protease, and lipase, use the [quantification ladder](./quantification-ladder.md): Tier 3 or outsourced measurement anchors the first engineered-vs-WT comparison; Tier 1 or Tier 2 can track later batch consistency only after calibration.

## 6. Decision Gates

| Outcome | Interpretation | Next move |
|---|---|---|
| **Green**: uricase protein and activity reproducible in at least two independent clones; native kojic acid within 30% of WT; amylase/protease/lipase not materially collapsed; strain QC clean | Uricase-only koji is a real engineering node | Advance to [validation-experiments.md §1.6](./validation-experiments.md#16-koji-enzyme-stability-at-digestive-ph-and-temperature), [§1.10](./validation-experiments.md#110-heterologous-uricase-lactoferrin-stability-in-shio-koji-salt-protease-ferment), and then the §1.9 dual-cassette gate |
| **Yellow**: protein detected but activity weak; activity present only in the wrong fraction; one native phenotype axis drops 30-50%; clone-to-clone spread is large | The chassis can express the payload, but architecture or locus choice is not resolved | Iterate on localization, expression architecture, clone selection, or host background before lactoferrin |
| **Red**: no reproducible uricase activity; native phenotype collapse >50%; aflatoxin signal; unstable or ambiguous engineered material | Do not proceed to dual-cassette spend | Return to design: alternative cassette architecture, alternative host, alternative uricase parent, or non-koji chassis |

The green threshold is intentionally stricter than "one positive band on a gel." The platform needs functional enzyme plus preserved koji behavior. A one-dimensional expression win that breaks the food chassis is not a win.

## 7. Deliverables For A Build Partner

The minimum useful partner-lab package is:

- construct-level design rationale and non-sequence construct map;
- explicit arm list and replicate plan;
- strain identity / construct verification report;
- uricase protein and activity data with raw files;
- WT-vs-engineered kojic acid, amylase, protease, and lipase measurements;
- aflatoxin or food-safety analytical screen when material is food-adjacent;
- material-return statement specifying whether the returned material is live, inactivated, clarified extract, purified protein, or data-only.

For the Open Enzyme public corpus, the preferred return is data plus nonviable or clarified analytical material. Any live engineered strain distribution belongs to a later strain-release decision with its own biosafety, QC, and governance document.

## 8. Relationship To The Dual-Cassette Endgame

Uricase-only is the right first milestone because it isolates the easiest load-bearing question: does the koji chassis express functional uricase while retaining the useful native phenotype? Lactoferrin adds disulfide folding, glycosylation, iron-binding, KEX2 processing, and chaperone-load questions. Those are worth paying for only after the uricase arm is real.

If uricase-only is green, [H01](./hypotheses/H01-ward-dual-cassette.md) becomes a better-spend experiment because one half of the dual-cassette system is already de-risked. If uricase-only is yellow, H01 should pause until the uricase architecture is stabilized. If uricase-only is red, H01's single-strain endgame claim is not worth testing in its current form.
