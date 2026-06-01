---
title: Reactome NLRP3 Supporting Detail
date: 2026-06-01
status: sendable
tags: [reactome, nlrp3, contribution, supporting-detail]
---

# Supporting Detail: Proposed NLRP3 Regulatory Annotations

This note supports a proposed Reactome curation discussion for `R-HSA-844456` ("The NLRP3 inflammasome"). The request is intentionally narrow: three literature-supported regulatory mechanisms that do not appear to be represented in the current Reactome NLRP3 graph.

## Candidate 1: Oridonin -> NLRP3

**Candidate entity identifiers**

- Name: Oridonin
- PubChem CID: `5321010`
- CAS: `28957-04-2`
- ChEBI: `CHEBI:138236`
- ChEMBL: `CHEMBL1164920`

**Primary source**

- He H, Jiang H, Chen Y, et al. "Oridonin is a covalent NLRP3 inhibitor with strong anti-inflammasome activity." *Nature Communications* 2018;9:2550. PMID: 29959312. DOI: `10.1038/s41467-018-04947-6`.
- DOI: https://doi.org/10.1038/s41467-018-04947-6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/29959312/

**Evidence summary**

- Evidence level: In Vitro + Animal Model.
- Mechanism: oridonin covalently binds NLRP3 Cys279 in the NACHT domain and blocks NLRP3-NEK7 interaction.
- Pathway consequence: prevents NLRP3 inflammasome assembly/activation, including NLRP3-ASC complex formation.
- Disease relevance in source: mouse peritonitis, gouty arthritis, and type 2 diabetes models; human PBMC inflammasome readouts.

**Possible Reactome mapping**

- Primary candidate target: `R-HSA-1296421` — "NLRP3 oligomerizes via NACHT domains".
- Possible representation: new small-molecule covalent modification/binding event ("oridonin covalently modifies NLRP3 Cys279") that negatively regulates NLRP3 oligomerization, or a curator-preferred negative regulator annotation on an upstream NLRP3 activation event.
- Curation caveat: if Reactome prefers to explicitly represent the NLRP3-NEK7 licensing step, oridonin may fit more cleanly there than directly on `R-HSA-1296421`.

## Candidate 2: Tranilast -> NLRP3

**Candidate entity identifiers**

- Name: Tranilast
- PubChem CID: `5282230`
- CAS: `53902-12-8`
- ChEBI: `CHEBI:77572`
- ChEMBL: `CHEMBL415324`

**Primary source**

- Huang Y, Jiang H, Chen Y, et al. "Tranilast directly targets NLRP3 to treat inflammasome-driven diseases." *EMBO Molecular Medicine* 2018;10:e8689. PMID: 29531021. DOI: `10.15252/emmm.201708689`.
- DOI: https://doi.org/10.15252/emmm.201708689
- PubMed: https://pubmed.ncbi.nlm.nih.gov/29531021/

**Evidence summary**

- Evidence level: In Vitro + Animal Model + ex vivo human gout synovial cell evidence.
- Mechanism: tranilast directly binds the NLRP3 NACHT domain.
- Pathway consequence: blocks NLRP3 oligomerization and suppresses NLRP3 inflammasome assembly; reported as selective versus AIM2 and NLRC4 in the source paper.
- Disease relevance in source: mouse gouty arthritis, CAPS, and type 2 diabetes models; ex vivo synovial fluid mononuclear cells from patients with gout.

**Possible Reactome mapping**

- Primary candidate target: `R-HSA-1296421` — "NLRP3 oligomerizes via NACHT domains".
- Secondary affected event: `R-HSA-844610` — "NLRP3 recruits PYCARD (ASC) via a PYD-PYD interaction".
- Possible representation: negative regulator of NLRP3 NACHT-domain oligomerization, or an annotation to the event summation if a drug-regulation edge is not appropriate.
- Curation caveat: the source paper's mechanism is upstream of ASC recruitment, so `R-HSA-844610` is best treated as a downstream consequence rather than the primary target event.

## Candidate 3: Beta-Hydroxybutyrate / 3-Hydroxybutyrate -> NLRP3 Immune Regulation

**Candidate entity identifiers**

- Names: beta-hydroxybutyrate; 3-hydroxybutyrate; D-beta-hydroxybutyrate, depending on curator entity choice.
- Existing Reactome metabolism event: `R-HSA-73920` — "D-beta hydroxybutyrate+NAD+ <=> acetoacetate+NADH+H+".
- Identifier note: PubChem name resolution returns related but not identical records for "3-hydroxybutyrate" (`CID 3541112`, `CHEBI:37054`) and "beta-hydroxybutyrate" (`CID 441`, `CHEBI:20067`). Reactome curators should choose the entity consistent with existing Reactome ketone-body modeling.

**Primary source**

- Youm YH, Nguyen KY, Grant RW, et al. "The ketone metabolite beta-hydroxybutyrate blocks NLRP3 inflammasome-mediated inflammatory disease." *Nature Medicine* 2015;21:263-269. PMID: 25686106. DOI: `10.1038/nm.3804`.
- DOI: https://doi.org/10.1038/nm.3804
- PubMed: https://pubmed.ncbi.nlm.nih.gov/25686106/

**Evidence summary**

- Evidence level: In Vitro + Animal Model.
- Mechanism: beta-hydroxybutyrate suppresses NLRP3 inflammasome activation in response to urate crystals, ATP, and lipotoxic fatty acids.
- Reported pathway effects: prevents K+ efflux and reduces ASC oligomerization/speck formation.
- Disease relevance in source: human monocyte IL-1beta/IL-18 readouts; mouse models including urate crystal-induced peritonitis and NLRP3-mutant autoinflammatory disease models.

**Possible Reactome mapping**

- Possible upstream target: `R-HSA-877187` — "P2X7 mediates loss of intracellular K+".
- Possible downstream target: `R-HSA-844610` — "NLRP3 recruits PYCARD (ASC) via a PYD-PYD interaction".
- Possible representation: cross-pathway negative regulation linking ketone-body metabolism to NLRP3 activation, or a summation annotation if Reactome curators prefer not to model the K+ efflux mechanism as direct regulation of P2X7.
- Curation caveat: the source paper frames BHB's effect as NLRP3-specific, but the exact molecular binding target is not equivalent to the oridonin/tranilast cases. This candidate is therefore best presented as a regulatory annotation rather than a direct binding event unless curators have a preferred model.

## Existing Reactome Baseline Checked

Pathway audited: `R-HSA-844456` — "The NLRP3 inflammasome".

Events already represented in Reactome:

| Event | Status |
|---|---|
| `R-HSA-877178` ATP binds to P2X7 | Already modeled |
| `R-HSA-877187` P2X7 mediates loss of intracellular K+ | Already modeled |
| `R-HSA-877198` P2X7 mediates membrane pores that include pannexin-1 | Already modeled |
| `R-HSA-873951` SGT1:HSP90 binds inactive NLRP3 | Already modeled |
| `R-HSA-1250272` TXNIP binds NLRP3, including HMOX1 negative regulation context | Already modeled |
| `R-HSA-1296421` NLRP3 oligomerizes via NACHT domains | Already modeled |
| `R-HSA-844610` NLRP3 recruits PYCARD (ASC) | Already modeled |
| `R-HSA-877361` Pyrin binds ASC | Already modeled |
| `R-HSA-9693324` Disulfiram covalently modifies Cys191 in GSDMD | Already modeled |

Not included in this first request: ABCG2-mediated intestinal urate efflux. That looks like a plausible separate Reactome contribution candidate from the broader Open Enzyme audit, but it needs a focused primary-source packet around intestinal ABCG2 urate secretion, Q141K disease relevance, and the exact transport reaction Reactome would model.
