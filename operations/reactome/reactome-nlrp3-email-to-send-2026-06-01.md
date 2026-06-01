---
title: Reactome NLRP3 Email To Send
date: 2026-06-01
status: ready-to-send
tags: [reactome, nlrp3, contribution, email]
---

# Reactome NLRP3 Email To Send

Send to: `help@reactome.org`

Subject: Proposed literature-supported regulatory annotations for Reactome NLRP3 inflammasome pathway

Do not attach the raw generated JSON files on first contact. They are internal provenance. If you want to include an attachment, attach [`reactome-nlrp3-supporting-detail-2026-06-01.md`](./reactome-nlrp3-supporting-detail-2026-06-01.md) or paste its contents below the email body.

## Body

Hello Reactome team,

I am writing from Open Enzyme, an open research project studying engineered food-grade microbial strains and inflammatory disease mechanisms. We have been using Reactome's NLRP3 inflammasome pathway (`R-HSA-844456`) as a structured reference for gout-relevant innate immune biology, and we would like to ask whether three literature-supported regulatory mechanisms would be appropriate additions or annotations.

Before writing, we checked the existing Reactome graph with the Content Service and confirmed that many mechanisms we first thought might be missing are already represented, including P2X7/pannexin-1 pore formation, SGT1:HSP90 binding, HMOX1 regulation, Pyrin-ASC binding, and disulfiram/GSDMD Cys191 modification. We therefore narrowed this note to three candidates:

1. **Oridonin as a covalent NLRP3 inhibitor.** He et al. report that oridonin covalently modifies NLRP3 Cys279 in the NACHT domain, blocks NLRP3-NEK7 interaction, and suppresses NLRP3 inflammasome assembly/activation, including in mouse gouty arthritis models. Candidate Reactome mapping: negative regulation of `R-HSA-1296421` ("NLRP3 oligomerizes via NACHT domains") or a curator-preferred upstream event representing NLRP3-NEK7-enabled activation.

2. **Tranilast as a direct NLRP3 NACHT-domain inhibitor.** Huang et al. report that tranilast directly binds NLRP3's NACHT domain and blocks NLRP3 oligomerization, with activity in mouse NLRP3-driven disease models including gouty arthritis and ex vivo activity in synovial fluid mononuclear cells from gout patients. Candidate Reactome mapping: negative regulation of `R-HSA-1296421`, with possible downstream annotation on `R-HSA-844610` ("NLRP3 recruits PYCARD (ASC) via a PYD-PYD interaction").

3. **Beta-hydroxybutyrate / 3-hydroxybutyrate as a metabolism-to-innate-immunity regulatory link.** Youm et al. report that beta-hydroxybutyrate suppresses NLRP3 activation in response to urate crystals, ATP, and lipotoxic fatty acids; mechanistically, it prevents K+ efflux and reduces ASC oligomerization/speck formation. Reactome already contains beta-hydroxybutyrate in ketone metabolism (`R-HSA-73920`), so the possible addition would be a cross-pathway regulatory annotation rather than a new molecule.

We would be grateful for guidance on whether these are appropriate Reactome additions and, if so, how your curators would prefer them represented: as negative regulators, black-box regulatory annotations, new small-molecule binding/modification events, or summation/reference updates.

Primary references and candidate event IDs are included in the supporting detail below. We are happy to reformat the evidence in whichever structure is most useful for your curation workflow.

Best,

Brian Abent

## Optional Supporting Detail

Attach or paste: [`reactome-nlrp3-supporting-detail-2026-06-01.md`](./reactome-nlrp3-supporting-detail-2026-06-01.md)
