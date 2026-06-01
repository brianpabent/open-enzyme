---
title: Reactome NLRP3 Contribution Dossier (Corrected)
date: 2026-06-01
tags: [reactome, nlrp3, contribution, curation, pathway-audit]
---

# Reactome NLRP3 Contribution Dossier (Corrected)

## Status

Do not send the Antigravity scratch dossier as written. It overstates what Reactome lacks and contains incorrect PMIDs/DOIs. This corrected working note narrows the contribution to plausible gaps that should be verified against the live Reactome graph before contacting curators.

Live search check (2026-06-01, `tools/reactome`): `oridonin` and `tranilast` return structured `notFound: true`; `hydroxybutyrate` returns metabolic reactions, led by `R-HSA-73920`, not an immune/NLRP3 regulatory link.

## Reactome Baseline

Pathway: `R-HSA-844456` — The NLRP3 inflammasome, Reactome Release 96.

Reactome already models or documents these mechanisms, so they are not clean "missing reaction" contributions:

| Mechanism | Reactome status | Notes |
|---|---|---|
| P2X7 / pannexin-1 pore formation | Already modeled | `R-HSA-877178`, `R-HSA-877187`, `R-HSA-877198` cover ATP-P2X7 activation, potassium loss, and pore formation. |
| SGT1:HSP90 binding inactive NLRP3 | Already modeled | `R-HSA-874087`, `R-HSA-873951`; primary paper PMID: 17435760. |
| HMOX1 negative regulation of NLRP3/TXNIP axis | Already present as regulation | `R-HSA-1250272` includes negative regulation by cytosolic HMOX1. Correct HMOX1 PubMed record appears to be PMID: 30333233. |
| Pyrin binding ASC | Already modeled | `R-HSA-877361`; Reactome summation already states interference with NLRP3-ASC association. |

## Candidate Contributions

| Candidate | Proposed Reactome curation angle | Evidence | Caveat |
|---|---|---|---|
| Oridonin | Add oridonin as a negative regulator of NLRP3 activation/oligomerization or NLRP3-NEK7 interaction, likely upstream of `R-HSA-1296421` after curator mapping. | He et al. 2018, *Nature Communications*, PMID: 29959312, DOI: 10.1038/s41467-018-04947-6. Oridonin covalently modifies NLRP3 Cys279 and blocks NLRP3-NEK7 interaction; mouse gouty arthritis evidence. | Verify Reactome search under `oridonin`, `Ori`, and the correct ChEBI ID before submission. Do not use ChEBI:7780 unless independently verified. |
| Tranilast | Add tranilast as a negative regulator of NLRP3 NACHT-domain oligomerization, likely around `R-HSA-1296421`. | Huang et al. 2018, *EMBO Molecular Medicine*, PMID: 29531021, DOI: 10.15252/emmm.201708689. Tranilast directly binds NLRP3 NACHT and blocks oligomerization; mouse gouty arthritis and ex vivo gout synovial cell evidence. | Reactome may classify small-molecule regulation differently from explicit binding reactions; ask curators for preferred representation. |
| BHB / 3-hydroxybutyrate | Add immune-regulatory link from 3-hydroxybutyrate to NLRP3 activation, potassium efflux, and ASC oligomerization context. | Youm et al. 2015, *Nature Medicine*, PMID: 25686106, DOI: 10.1038/nm.3804. BHB suppresses NLRP3 activation in response to urate crystals, ATP, and lipotoxic fatty acids; mechanism includes prevention of potassium efflux and reduction of ASC oligomerization/speck formation. | Reactome already has 3-hydroxybutyrate in ketone metabolism; contribution is cross-pathway immune regulation, not a new molecule. |

## Draft Curator Email

Subject: Proposed updates to Reactome NLRP3 inflammasome pathway curation

Hello Reactome team,

I am working on Open Enzyme, an open research project focused on engineered food-grade microbial strains and inflammatory disease mechanisms. While using Reactome's NLRP3 inflammasome pathway (`R-HSA-844456`), we noticed several primary-literature-supported regulatory mechanisms that may be useful additions or annotations to the pathway.

We first checked the existing Reactome graph and recognize that P2X7/pannexin-1 pore formation, SGT1:HSP90 binding, HMOX1 regulation, and Pyrin-ASC binding are already represented or described. The narrower candidate additions we would like to ask about are:

1. Oridonin as a covalent NLRP3 inhibitor that modifies Cys279 and blocks NLRP3-NEK7 interaction (He et al. 2018, *Nature Communications*, PMID: 29959312, DOI: 10.1038/s41467-018-04947-6).
2. Tranilast as a direct NLRP3 NACHT-domain inhibitor that blocks oligomerization (Huang et al. 2018, *EMBO Molecular Medicine*, PMID: 29531021, DOI: 10.15252/emmm.201708689).
3. 3-hydroxybutyrate / BHB as an immune-regulatory ketone body that suppresses NLRP3 activation by preventing potassium efflux and reducing ASC oligomerization/speck formation (Youm et al. 2015, *Nature Medicine*, PMID: 25686106, DOI: 10.1038/nm.3804).

Would these be appropriate to submit as negative regulators or pathway annotations for the NLRP3 inflammasome pathway? If so, I would be glad to prepare the mechanism details in the format preferred by your curators.

Best,
Brian Abent

## Pre-Submission Checklist

- Re-run Reactome search for each candidate and synonym.
- Verify ChEBI identifiers for oridonin, tranilast, and BHB.
- Query target events (`R-HSA-1296421`, `R-HSA-844610`, `R-HSA-877187`) and inspect existing `regulatedBy` edges.
- Confirm every PMID/DOI from primary sources.
- Do not promise authorship, DOI publication credit, or ORCID integration unless Reactome confirms the contribution pathway.
