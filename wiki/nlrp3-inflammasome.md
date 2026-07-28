---
title: NLRP3 Inflammasome
date: 2026-07-27
tags:
  - nlrp3
  - gout
  - inflammasome
  - chokepoints
related:
  - gout-pathophysiology.md
  - nlrp3-exploit-map.md
  - complement-c5a-gout.md
  - spm-resolution-pathway.md
  - nlrp3-inhibitor-screen.md
sources:
  - "An et al. Human-cell C5a/MSU study. PMID: 25229885"
  - "Youm et al. Nature Medicine 2015. PMID: 25686106"
  - "Oridonin mechanism. PMID: 29959312"
  - "Tranilast mechanism. PMID: 29531021"
  - "../reference/papers/R-HSA-844456_.pdf"
status: evidence-map
---

# NLRP3 Inflammasome

## Why it matters in gout

NLRP3, ASC, and pro-caspase-1 form an intracellular inflammasome complex. In gout-relevant systems, MSU crystals provide activation inputs that lead to caspase-1 activity, IL-1β maturation, GSDMD cleavage, pyroptosis, and neutrophil-rich inflammation. The pathway is causal enough to supply several intervention nodes, but a downstream cytokine change alone does not identify which node moved.

## Open Enzyme chokepoint map

The CP labels are an experimental decomposition, not a claim that every candidate acts cleanly at one node.

| Chokepoint | Experimental question | Qualified examples and boundaries |
|---|---|---|
| **CP0 — complement-associated priming** | Does C5a/C5aR1 or another complement input change the MSU response? | C5a potentiated MSU-associated IL-1β production in human whole blood and primary monocytes in the defined An et al. system (**In Vitro**; PMID 25229885); related murine work supplies **Animal Model** evidence. Comparative causal contribution in human flares remains open. |
| **CP1a — transcriptional priming** | Does the intervention change NF-κB-associated NLRP3 or pro-IL-1β preparation? | Sulforaphane, EGCG, and other exact-material probes have source-specific preclinical evidence; KPV is only a PepT1/priming conjecture without direct MSU evidence |
| **CP1b — non-transcriptional priming** | Does complement-associated ROS change activation competence without the same transcriptional route? | C5a/ROS work supplies a defined mechanistic branch; tissue and timing must be matched |
| **CP2 — NLRP3 activation** | Does the intervention change potassium flux, NLRP3 conformation, or NLRP3–NEK7-associated activity? | Oridonin and tranilast have source-specific direct-mechanism evidence; BHB changes potassium-efflux and later assembly readouts but is not a defined direct binder |
| **CP3 — ASC assembly** | Does ASC oligomerization or speck formation change? | BHB and other exact probes have source-specific preclinical readouts; colchicine affects microtubule-dependent assembly and has clinical gout evidence |
| **CP4 — caspase-1** | Is caspase-1 activity or substrate cleavage changed directly? | VX-765 is a direct caspase-1 comparator; downstream caspase readouts do not by themselves establish a direct CP4 mechanism |
| **CP5a — IL-1 signaling** | Does blocking IL-1 or IL-1R change the gout phenotype? | Product-specific human gout trials establish clinical tractability; exact status and indications require current primary records |
| **CP5b — active resolution** | Does an exact mediator change termination of MSU inflammation? | Exact RvD1 and MaR1 have distinct MSU mouse evidence; RvD2 is adjacent; EPA/DHA precursors require measured conversion |
| **CP6a — neutrophil amplification** | Does 5-LOX/LTB4 or another chemotactic input sustain recruitment? | Zileuton and exact natural compounds are separate pharmacology questions; adjacent approval does not establish gout activity |
| **CP6b — GSDMD execution** | Does the intervention change GSDMD cleavage, pore formation, or pyroptotic release? | Disulfiram and DMF supply exact-mechanism precedents in preclinical systems; gout exposure and efficacy remain separate |

See the [NLRP3 exploit map](./nlrp3-exploit-map.md) for candidate-level evidence and falsification gates.

## Claim discipline

- “Direct NLRP3 inhibitor” requires source-verified target-level evidence. Functional IL-1β suppression is not enough.
- A candidate can change several readouts because the cascade is sequential; node count does not rank efficacy.
- Different species, cells, stimuli, assays, and exposure schedules cannot be collapsed into a universal potency ratio.
- A route, dose, combination, or clinical status must come from the exact product and a current primary record.
- Activity in intestinal inflammation does not establish MSU activity or synovial exposure.

## Selected exact anchors

- **BHB:** suppressed urate-crystal, ATP, and lipotoxic NLRP3 activation; prevented potassium efflux; reduced ASC oligomerization/specks; and attenuated urate-crystal peritonitis in mice. **In Vitro + Animal Model** (PMID 25686106). This is pathway regulation, not a defined BHB–NLRP3 binding event.
- **Oridonin:** exact source-specific covalent NLRP3/NEK7-associated mechanism. **In Vitro + Animal Model** (PMID 29959312); see [oridonin](./oridonin.md).
- **Tranilast:** exact source-specific NACHT-domain NLRP3 mechanism. **In Vitro** (PMID 29531021).
- **Dapansutrile:** published Phase 2a gout evidence is compound- and protocol-specific. **Clinical Trial** (PMID 33005902); it does not validate an NLRP3-inhibitor class effect.
- **KPV:** PepT1-related uptake and an NF-κB reporter result in named non-MSU cell systems. **In Vitro** (PMID 18061177); direct gout and NLRP3 activity are absent from that experiment.

## Reactome boundary

The stored Reactome report for `R-HSA-844456` is at [reference/papers/R-HSA-844456_.pdf](../reference/papers/R-HSA-844456_.pdf). Reactome is curated pathway infrastructure, not primary evidence. The stored report includes P2X7/potassium-efflux, SGT1:HSP90, TXNIP/HMOX1, and pyrin/ASC-associated events. Before proposing a curation addition for BHB, oridonin, tranilast, or another candidate, query the current graph and then verify the load-bearing event against its primary paper.

## Cheapest decisive experiment

For any new candidate, use one qualified MSU-stimulated human-cell system and measure:

1. Exact material identity, free exposure, stability, and viability.
2. Priming markers before activation.
3. Potassium flux or another candidate-specific upstream event.
4. NLRP3/NEK7 or other claimed target engagement.
5. ASC oligomerization or specks.
6. Caspase-1, GSDMD, IL-1β, and orthogonal inflammasome controls.

Assign the narrowest supported node. If only the final cytokine changes, keep the mechanism unresolved.

## Clinical evidence boundary

The [clinical evidence surface](./gout-clinical-pipeline.md) holds selected exact trials and the refresh protocol. It is intentionally not reproduced here. “Approved,” “active,” “terminated,” “first,” “only,” and universal absence claims require a dated primary registry or regulator check.

This is Phase 0 research, not treatment, route, or dosing guidance.
