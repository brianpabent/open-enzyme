---
title: Reactome Audit Results
date: 2026-06-01
status: completed
tags: [reactome, pathway-audit, operations, contribution]
---

# Reactome Audit Results

Purpose: close the 2026-06-01 Reactome burndown by recording what the repo-local Reactome tool adds to the Open Enzyme corpus, where the wiki should use Reactome as a pathway backbone, and which contribution ideas are real enough to pursue.

Durable generated provenance: [`reference/generated/reactome/2026-06-01-open-enzyme-audit/`](../../reference/generated/reactome/2026-06-01-open-enzyme-audit/).

## Executive Verdict

Reactome is high-value for Open Enzyme as a stable pathway ID layer: complement, purine catabolism, URAT1, pyroptosis, TLR4, NFE2L2, digestion, and bile-acid metabolism all have usable human pathway anchors. It should be treated as structured pathway infrastructure, not as primary evidence for Open Enzyme's therapeutic claims.

The contribution surface is narrower than the first Antigravity pass implied. The plausible NLRP3 contribution candidates remain oridonin, tranilast, and beta-hydroxybutyrate / 3-hydroxybutyrate immune regulation. Several tempting "missing" items are already modeled by Reactome: disulfiram/GSDMD, avacopan/C5AR1, anakinra/IL1R1, colchicine/tubulin, complement activation, IL-1 signaling, and pyroptosis.

## Audit Results

| Area | Classification | Reactome anchors | Open Enzyme action |
|---|---|---|---|
| Complement CP0 / C5a | Already modeled as core complement; gout/MSU context remains primary-lit/OE synthesis | `R-HSA-166658` Complement cascade; `R-HSA-173623` classical activation; `R-HSA-173736` alternative activation; `R-HSA-166665` terminal pathway; `R-HSA-375395` C5a receptor binds C5a; `R-HSA-9957423` C5AR1 antagonist binding; `R-HSA-977371` Factor I inactivates Factor H-bound C3b; `R-HSA-982830` CD55; `R-HSA-981657` CD55:C3 convertase complexes | Add wiki anchor note only. Do not claim Reactome itself models MSU-gout CP0 priming. C1-INH/SERPING1 is present in Reactome, but this audit surfaced it mainly in secretion, kallikrein, and hereditary-angioedema/contact-system contexts rather than a clean gout-CP0 anchor. |
| Gut urate transport / lumen sink | Partly modeled; intestinal ABCG2 urate efflux appears under-modeled | `R-HSA-561253` SLC22A12 urate/lactate exchange; `R-HSA-561048` SLC22 organic anion transport; ABCG2 entities `R-HSA-917929` / `R-HSA-9794401`; `R-HSA-9796076` NFE2L2-dependent ABCG2 expression | Add wiki note that URAT1 is modeled but gut ABCG2 urate secretion is not cleanly represented. Treat as a possible future contribution only after primary-source packaging. |
| Purine catabolism / XO / uricase | Well modeled through human urate endpoint; human uricase absent for biological reasons | `R-HSA-74259` Purine catabolism; `R-HSA-74247` and `R-HSA-9727347` hypoxanthine to xanthine; `R-HSA-74258` and `R-HSA-9727349` xanthine to urate | Add wiki anchor to gout pathophysiology. Engineered microbial uricase remains Open Enzyme design context, not a missing human Reactome step. |
| IL-1 / pyroptosis / GSDMD | Already modeled | `R-HSA-446652` IL-1 family signaling; `R-HSA-9020702` interleukin-1 signaling; `R-HSA-5620971` pyroptosis; `R-HSA-9647680` CASP1 cleaves GSDMD; `R-HSA-9693324` disulfiram modifies Cys191 in GSDMD; `R-HSA-9716258` dimethyl fumarate modifies Cys191 in GSDMD | Update disulfiram page and contribution dossier: disulfiram is not a contribution gap. |
| Autophagy / mitophagy / NFE2L2 | Useful pathway anchors, not direct NLRP3 inhibitor evidence | `R-HSA-9612973` autophagy; `R-HSA-5205647` mitophagy; `R-HSA-9755511` KEAP1-NFE2L2 pathway; `R-HSA-9818749` NFE2L2 gene expression | Use as graph anchors for lactoferrin/carnosine/stress-response stack logic. Keep mechanism claims anchored to primary literature. |
| Barrier / tight junction / gut inflammation | Useful anchors for human pathway vocabulary; microbiome/tissue physiology remains mostly outside Reactome's lane | `R-HSA-420029` tight junction interactions; `R-HSA-166016` TLR4 cascade; `R-HSA-166166` MyD88-independent TLR4 cascade | Add a small lactoferrin TLR4 anchor note. No broad rewrite. |
| Digestive enzyme / EPI biology | Useful substrate/product vocabulary; not enough for fungal supplement standardization | `R-HSA-8935690` digestion; `R-HSA-189085` dietary carbohydrate digestion; `R-HSA-192456` dietary lipid digestion; `R-HSA-188979` amylose digestion; `R-HSA-191114` amylopectin digestion; `R-HSA-192422` triacylglycerol digestion by PTL:colipase; `R-HSA-192417` cholesterol ester digestion by CEL | Add wiki anchor note for human digestion context. |
| Bile acid / chaperone / ABCG2-Q141K | Adjacency only | `R-HSA-194068` bile acid and bile salt metabolism; `R-HSA-192105` synthesis; `R-HSA-159418` recycling; `R-HSA-381119` unfolded protein response; `R-HSA-391251` protein folding | No wiki claim change needed now. TUDCA/UDCA chaperone claims remain primary-lit/computational, not Reactome-derived. |

## Cross-Cutting Molecule Sweep

| Molecule | Reactome status | Contribution verdict |
|---|---|---|
| Oridonin | No structured hit in the 2026-06-01 search | Plausible NLRP3 contribution candidate after ChEBI/synonym and target-event `regulatedBy` checks. |
| Tranilast | No structured hit in the 2026-06-01 search | Plausible NLRP3 contribution candidate after ChEBI/synonym and target-event `regulatedBy` checks. |
| Beta-hydroxybutyrate / 3-hydroxybutyrate | Present in ketone metabolism, led by `R-HSA-73920`; no immune/NLRP3 regulatory edge found in this audit | Plausible cross-pathway regulatory contribution candidate, not a new-molecule contribution. |
| Disulfiram | Already modeled as drug plus `R-HSA-9693324` GSDMD Cys191 covalent modification | Not a contribution gap. |
| Avacopan | Already modeled as C5AR1 antagonist context, `R-HSA-9957423` | Not a contribution gap. |
| Anakinra | Already modeled as IL1R1 inhibitor context, `R-HSA-9681763` | Not a contribution gap. |
| Colchicine | Already modeled as tubulin-binding reaction, `R-HSA-9685830` | Not a contribution gap. |
| Echinatin | No structured hit in the 2026-06-01 search | Possible future candidate only if a primary-source mechanism is packaged against a specific Reactome event. |
| Dapansutrile | No structured hit in the 2026-06-01 search | Possible future candidate; needs target-event mapping and primary-source packaging. |
| MCC950 | No structured hit in the 2026-06-01 search | Possible future candidate; needs target-event mapping and primary-source packaging. |

## Contribution Queue

1. Keep [`reactome-contribution-nlrp3.md`](./reactome-contribution-nlrp3.md) focused on oridonin, tranilast, and BHB/3-hydroxybutyrate.
2. Open a separate ABCG2-intestinal-urate contribution dossier only after collecting the primary sources that establish ABCG2-mediated intestinal urate efflux and Q141K disease relevance.
3. Do not submit no-hit molecules from search alone. For each candidate, package the target Reactome event, primary citation, exact molecule identifier, and the proposed regulation relation.

## Usage Pattern Going Forward

For any new wiki mechanism with a pathway-heavy claim:

1. Search Reactome for the mechanism, gene/protein, and molecule name.
2. Pull the target event and contained events.
3. Classify the claim as already-modeled, present-only-in-other-context, under-modeled, absent, or not-Reactome-lane.
4. Add Reactome IDs only as pathway anchors.
5. Run the normal Open Enzyme primary-source verification gate before adding any load-bearing mechanism, residue, dose, or evidence-tier claim.
