---
title: Reactome NLRP3 Curator Packet
date: 2026-06-01
status: ready-for-review
tags: [reactome, nlrp3, contribution, curation, open-source]
---

# Reactome NLRP3 Curator Packet

Purpose: provide a curator-facing, conservative submission packet for possible updates to Reactome's NLRP3 inflammasome pathway (`R-HSA-844456`). This is the version to review before emailing Reactome. It is deliberately narrow: only propose mechanisms that survived the 2026-06-01 Reactome audit and have primary-source support.

## What To Send

Send the email in [`reactome-nlrp3-email-to-send-2026-06-01.md`](./reactome-nlrp3-email-to-send-2026-06-01.md) to `help@reactome.org`.

Do **not** attach the raw files in `../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/` on first contact. Those files are internal provenance: Reactome query outputs and PubChem registry pulls that let us reproduce the audit.

If you want to include an attachment, attach or paste [`reactome-nlrp3-supporting-detail-2026-06-01.md`](./reactome-nlrp3-supporting-detail-2026-06-01.md). That file is external-facing and contains no local file references.

Recommended route: Reactome's public contribution page asks prospective contributors to contact Reactome for pathways not already listed as active calls for review; the EBI Reactome training page gives `help@reactome.org` for informal contribution discussions.

External verification links:

- Reactome contribution page: [Contribute Pathway Knowledge](https://reactome.org/community/collaboration)
- EBI Reactome training: [Contributing to Reactome](https://www.ebi.ac.uk/training/online/courses/reactome-quick-tour/contributing-to-reactome/)
- Oridonin source: [Nature Communications DOI](https://doi.org/10.1038/s41467-018-04947-6), [PubMed PMID 29959312](https://pubmed.ncbi.nlm.nih.gov/29959312/)
- Tranilast source: [EMBO Molecular Medicine DOI](https://doi.org/10.15252/emmm.201708689), [PubMed PMID 29531021](https://pubmed.ncbi.nlm.nih.gov/29531021/)
- Beta-hydroxybutyrate source: [Nature Medicine DOI](https://doi.org/10.1038/nm.3804), [PubMed PMID 25686106](https://pubmed.ncbi.nlm.nih.gov/25686106/)

Durable local provenance:

- Reactome audit: [`reactome-audit-results-2026-06-01.md`](./reactome-audit-results-2026-06-01.md)
- Existing corrected working note: [`reactome-contribution-nlrp3.md`](./reactome-contribution-nlrp3.md)
- Generated Reactome target-event pulls: [`reference/generated/reactome/2026-06-01-nlrp3-curator-packet/`](../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/)

## Sendable Email Draft

Subject: Proposed literature-supported regulatory annotations for Reactome NLRP3 inflammasome pathway

Hello Reactome team,

I am writing from Open Enzyme, an open research project studying engineered food-grade microbial strains and inflammatory disease mechanisms. We have been using Reactome's NLRP3 inflammasome pathway (`R-HSA-844456`) as a structured reference for gout-relevant innate immune biology, and we would like to ask whether three literature-supported regulatory mechanisms would be appropriate additions or annotations.

Before writing, we checked the existing Reactome graph with the Content Service and confirmed that many mechanisms we first thought might be missing are already represented, including P2X7/pannexin-1 pore formation, SGT1:HSP90 binding, HMOX1 regulation, Pyrin-ASC binding, and disulfiram/GSDMD Cys191 modification. We therefore narrowed this note to three candidates:

1. **Oridonin as a covalent NLRP3 inhibitor.** He et al. report that oridonin covalently modifies NLRP3 Cys279 in the NACHT domain, blocks NLRP3-NEK7 interaction, and suppresses NLRP3 inflammasome assembly/activation, including in mouse gouty arthritis models. Candidate Reactome mapping: negative regulation of `R-HSA-1296421` ("NLRP3 oligomerizes via NACHT domains") or a curator-preferred upstream event representing NLRP3-NEK7-enabled activation.

2. **Tranilast as a direct NLRP3 NACHT-domain inhibitor.** Huang et al. report that tranilast directly binds NLRP3's NACHT domain and blocks NLRP3 oligomerization, with activity in mouse NLRP3-driven disease models including gouty arthritis and ex vivo activity in synovial fluid mononuclear cells from gout patients. Candidate Reactome mapping: negative regulation of `R-HSA-1296421`, with possible downstream annotation on `R-HSA-844610` ("NLRP3 recruits PYCARD (ASC) via a PYD-PYD interaction").

3. **Beta-hydroxybutyrate / 3-hydroxybutyrate as a metabolism-to-innate-immunity regulatory link.** Youm et al. report that beta-hydroxybutyrate suppresses NLRP3 activation in response to urate crystals, ATP, and lipotoxic fatty acids; mechanistically, it prevents K+ efflux and reduces ASC oligomerization/speck formation. Reactome already contains beta-hydroxybutyrate in ketone metabolism (`R-HSA-73920`), so the possible addition would be a cross-pathway regulatory annotation rather than a new molecule.

We would be grateful for guidance on whether these are appropriate Reactome additions and, if so, how your curators would prefer them represented: as negative regulators, black-box regulatory annotations, new small-molecule binding/modification events, or summation/reference updates.

Primary references and candidate event IDs are included below. We are happy to reformat the evidence in whichever structure is most useful for your curation workflow.

Best,
Brian Abent

## Proposed Additions

### 1. Oridonin -> NLRP3

**Candidate entity identifiers**

- Name: Oridonin
- PubChem CID: `5321010`
- CAS: `28957-04-2`
- ChEBI: `CHEBI:138236`
- ChEMBL: `CHEMBL1164920`
- PubChem registry pull: `../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/pubchem-oridonin-registry.json`

**Primary source**

- He H, Jiang H, Chen Y, et al. "Oridonin is a covalent NLRP3 inhibitor with strong anti-inflammasome activity." *Nature Communications* 2018;9:2550. PMID: 29959312. DOI: `10.1038/s41467-018-04947-6`.

**Evidence summary**

- Evidence level: In Vitro + Animal Model.
- Mechanism: oridonin covalently binds NLRP3 Cys279 in the NACHT domain and blocks NLRP3-NEK7 interaction.
- Pathway consequence: prevents NLRP3 inflammasome assembly/activation, including NLRP3-ASC complex formation.
- Disease relevance in source: mouse peritonitis, gouty arthritis, and type 2 diabetes models; human PBMC inflammasome readouts.

**Reactome mapping proposal**

- Primary candidate target: `R-HSA-1296421` — "NLRP3 oligomerizes via NACHT domains". Local query showed no `regulatedBy` edge on 2026-06-01.
- Possible representation: new small-molecule covalent modification/binding event ("oridonin covalently modifies NLRP3 Cys279") that negatively regulates NLRP3 oligomerization, or a curator-preferred negative regulator annotation on an upstream NLRP3 activation event.
- Curation caveat: if Reactome prefers to explicitly represent the NLRP3-NEK7 licensing step, oridonin may fit more cleanly there than directly on `R-HSA-1296421`.

### 2. Tranilast -> NLRP3

**Candidate entity identifiers**

- Name: Tranilast
- PubChem CID: `5282230`
- CAS: `53902-12-8`
- ChEBI: `CHEBI:77572`
- ChEMBL: `CHEMBL415324`
- PubChem registry pull: `../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/pubchem-tranilast-registry.json`

**Primary source**

- Huang Y, Jiang H, Chen Y, et al. "Tranilast directly targets NLRP3 to treat inflammasome-driven diseases." *EMBO Molecular Medicine* 2018;10:e8689. PMID: 29531021. DOI: `10.15252/emmm.201708689`.

**Evidence summary**

- Evidence level: In Vitro + Animal Model + ex vivo human gout synovial cell evidence.
- Mechanism: tranilast directly binds the NLRP3 NACHT domain.
- Pathway consequence: blocks NLRP3 oligomerization and suppresses NLRP3 inflammasome assembly; reported as selective versus AIM2 and NLRC4 in the source paper.
- Disease relevance in source: mouse gouty arthritis, CAPS, and type 2 diabetes models; ex vivo synovial fluid mononuclear cells from patients with gout.

**Reactome mapping proposal**

- Primary candidate target: `R-HSA-1296421` — "NLRP3 oligomerizes via NACHT domains". Local query showed no `regulatedBy` edge on 2026-06-01.
- Secondary affected event: `R-HSA-844610` — "NLRP3 recruits PYCARD (ASC) via a PYD-PYD interaction". The source paper's mechanism is upstream of ASC recruitment, so this is best treated as a downstream consequence rather than the primary target event.
- Possible representation: negative regulator of NLRP3 NACHT-domain oligomerization, or an annotation to the event summation if a drug-regulation edge is not appropriate.

### 3. Beta-Hydroxybutyrate / 3-Hydroxybutyrate -> NLRP3 Immune Regulation

**Candidate entity identifiers**

- Names: beta-hydroxybutyrate; 3-hydroxybutyrate; D-beta-hydroxybutyrate, depending on curator entity choice.
- Existing Reactome metabolism event: `R-HSA-73920` — "D-beta hydroxybutyrate+NAD+ <=> acetoacetate+NADH+H+".
- PubChem registry pulls:
  - `../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/pubchem-3-hydroxybutyrate-registry.json`
  - `../../reference/generated/reactome/2026-06-01-nlrp3-curator-packet/pubchem-beta-hydroxybutyrate-registry.json`
- Identifier note: PubChem name resolution returned related but not identical records for "3-hydroxybutyrate" (`CID 3541112`, `CHEBI:37054`) and "beta-hydroxybutyrate" (`CID 441`, `CHEBI:20067`). Reactome curators should choose the entity consistent with existing Reactome ketone-body modeling.

**Primary source**

- Youm YH, Nguyen KY, Grant RW, et al. "The ketone metabolite beta-hydroxybutyrate blocks NLRP3 inflammasome-mediated inflammatory disease." *Nature Medicine* 2015;21:263-269. PMID: 25686106. DOI: `10.1038/nm.3804`.

**Evidence summary**

- Evidence level: In Vitro + Animal Model.
- Mechanism: beta-hydroxybutyrate suppresses NLRP3 inflammasome activation in response to urate crystals, ATP, and lipotoxic fatty acids.
- Reported pathway effects: prevents K+ efflux and reduces ASC oligomerization/speck formation.
- Disease relevance in source: human monocyte IL-1beta/IL-18 readouts; mouse models including urate crystal-induced peritonitis and NLRP3-mutant autoinflammatory disease models.

**Reactome mapping proposal**

- Possible upstream target: `R-HSA-877187` — "P2X7 mediates loss of intracellular K+". Local query showed no `regulatedBy` edge on 2026-06-01.
- Possible downstream target: `R-HSA-844610` — NLRP3 recruits PYCARD/ASC, because the source paper reports reduced ASC oligomerization/speck formation.
- Possible representation: cross-pathway negative regulation linking ketone-body metabolism to NLRP3 activation, or a summation annotation if Reactome curators prefer not to model the K+ efflux mechanism as direct regulation of P2X7.
- Curation caveat: the source paper frames BHB's effect as NLRP3-specific and independent of several starvation-regulated mechanisms, but the exact molecular binding target is not equivalent to the oridonin/tranilast cases. This candidate is therefore best presented as a regulatory annotation rather than a direct binding event unless curators have a preferred model.

## Reactome Baseline Checked

Pathway audited: `R-HSA-844456` — "The NLRP3 inflammasome".

Important existing Reactome events in the audited pathway:

| Event | Status |
|---|---|
| `R-HSA-877178` ATP binds to P2X7 | Already modeled |
| `R-HSA-877187` P2X7 mediates loss of intracellular K+ | Already modeled |
| `R-HSA-877198` P2X7 mediates membrane pores that include pannexin-1 | Already modeled |
| `R-HSA-873951` SGT1:HSP90 binds inactive NLRP3 | Already modeled |
| `R-HSA-1250272` TXNIP binds NLRP3, including HMOX1 negative regulation context | Already modeled |
| `R-HSA-1296421` NLRP3 oligomerizes via NACHT domains | Already modeled; no local `regulatedBy` edge found |
| `R-HSA-844610` NLRP3 recruits PYCARD (ASC) | Already modeled; no local `regulatedBy` edge found |
| `R-HSA-877361` Pyrin binds ASC | Already modeled |

Cross-cutting molecule sweep:

| Candidate | Reactome status from 2026-06-01 audit |
|---|---|
| Oridonin | No structured Reactome hit found |
| Tranilast | No structured Reactome hit found |
| Beta-hydroxybutyrate / 3-hydroxybutyrate | Present in ketone metabolism, not found as immune/NLRP3 regulation |
| Disulfiram | Already modeled as `R-HSA-9693324` GSDMD Cys191 covalent modification |
| Avacopan | Already modeled as `R-HSA-9957423` C5AR1 antagonist binding |
| Anakinra | Already modeled as `R-HSA-9681763` IL1R1 inhibitor binding |
| Colchicine | Already modeled as `R-HSA-9685830` tubulin binding |

## Not Included In This First Submission

ABCG2-mediated intestinal urate efflux looks like a plausible separate Reactome contribution candidate from the broader audit, but it should not be bundled into this NLRP3 submission. It needs a focused primary-source packet around intestinal ABCG2 urate secretion, Q141K disease relevance, and the exact transport reaction Reactome would model.

## Pre-Send Checklist

- Re-run the four Reactome target-event queries immediately before sending if more than a few days have passed.
- Confirm whether Reactome's current release has added any of oridonin, tranilast, or BHB/NLRP3 regulation.
- Optionally ask curators whether PubChem/ChEBI identifiers are sufficient or whether they prefer a different reference entity source.
- Do not ask for authorship, DOI credit, or ORCID handling in the first email; let Reactome explain their contribution workflow.
- Keep the first email short and attach/link this packet as supporting detail.
