---
type: most-curious-thread
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 1
global_index: 19
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The single thread I'd spend the next experiment slot on is the Berkeleyamide / Penicillium food-grade ascomycete secondary-metabolite connection.

The single thread I'd spend the next experiment slot on is the **Berkeleyamide / Penicillium food-grade ascomycete secondary-metabolite connection.** The corpus evidence supporting the hunch: comp-014 Phase 3 found Berkeleyamides A/D with direct CASP1 IC50 = 330/610 nM (pChEMBL 6.48/6.21, ChEMBL466565/ChEMBL466747, 2008) from *Penicillium* — the first fungal natural products in the OE corpus with sub-μM direct caspase-1 inhibition. Berkeleyones A/B/C from the same genus hit IL-1β at 2.7–37.8 μM. The evidence that would refute it: a CASP1 inhibition assay on extracts from food-grade *Penicillium* species (*P. camemberti*, *P. roqueforti*) grown under standard cheese-ripening conditions returns no activity at IC50 < 100 μM — meaning the Berkeleyamide chemotype is restricted to environmental *Penicillium* isolates and not present in food-fermentation-accessible species. The cheapest discriminating experiment: grow *P. camemberti* on standard cheese-ripening substrate (readily available as a commercial cheese-making culture, ~$15), prepare aqueous + ethanolic extracts, run recombinant human caspase-1 fluorometric inhibition assay with Berkeleyamide A as the positive control. Total cost ~$500–1,000; 2 weeks; fully benchable in a community-college biology lab. A positive result opens an entirely new producer-organism class that bridges cultivation and fermentation tracks; a negative result closes the question cleanly and saves downstream exploration effort. I suspect another sweep model (Claude or otherwise) would converge on this pick because the comp-014 Phase 3 Berkeleyamide finding is the single most surprising new-compound-class result in the trigger files and the Penicillium-ascomycete logic is the natural next question it raises.



---

## Sources cited

- wiki/medicinal-mushroom-compound-mapping-computational.md
- wiki/nlrp3-exploit-map.md
- wiki/medicinal-mushroom-complement-track.md
- wiki/aspergillus-oryzae.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/complement-c5a-gout.md
- wiki/supplements-stack.md
- wiki/gout-action-guide.md
- wiki/gout-genetic-variants.md
- wiki/abcg2-modulators.md
- wiki/c1-inh-protease-stability-ecn-computational.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/engineered-lbp-chassis.md
- wiki/tcm-modern-rigor-intersection.md
- wiki/medicinal-mushroom-extract-sops.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/koji-endgame-strain.md
- wiki/modality-chokepoint-matrix.md
- wiki/validation-experiments.md
- wiki/uricase-abcg2-genotype-stratification-computational.md
- wiki/cross-validation.md
- wiki/gout-pathophysiology.md

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The curiosity pick is justified by the evidence density and surprise value: comp-014 Phase 3 identifies Berkeleyamides A/D as direct CASP1 fungal natural-product hits at 330/610 nM, a qualitatively different mechanism class from the indirect β-glucan / redox / NF-κB mushroom literature. The proposed food-grade-*Penicillium* extract assay is the cheapest discriminating experiment between “platform-relevant producer class” and “environmental-isolate curiosity.” Add species authentication and mycotoxin screening to the protocol, but otherwise this deserves elevation.

---

**WALKED 2026-05-19 — Closed (already actioned in Cluster J with material correction — Berkeleyamide chemistry redirected from "Penicillium" to *Talaromyces amestolkiae*; wet-lab budget redirected to antiSMASH computational first).**

This curious-thread pick was already engaged during the 2026-05-19 walkthrough as Cluster J1 + J2. The execution surfaced THREE substantive corrections to the original framing:

1. **Identity correction:** Stierle 2008 "P. rubrum" Berkeley Pit isolate has been **reclassified to *Talaromyces amestolkiae*** — different genus from cheese-ripening *Penicillium*. Berkeleyamide chemistry is *Talaromyces* chemistry, not *Penicillium* chemistry (Cluster J1 walkthrough closure documents the full Pass 2 daemon failure-mode trace — surface-level "Penicillium" attribution without checking 2014+ taxonomic literature).

2. **Wrong direction of effect for food-grade *Penicillium*:** mycophenolic acid (closest food-grade *Penicillium* "anti-inflammatory" candidate) is **PRO-NLRP3**, not anti (Huang 2018 PMC6032679 — MPA synergizes with LPS to activate the inflammasome at 5–75 μM). Wet-lab assay would have risked reading MPA as positive when it's the opposite direction.

3. **Wrong genome for cheese strains:** P. roqueforti has actively-degraded toxin BGCs (Crequer 2024 PMC11605963 — frameshift in PR-toxin ORF, deletion in mpaC). Substrate-induction can't unlock what's been mutated out. The 2023 canonical BGC review (Chávez PMC10144355) enumerates the entire P. roqueforti chemotype — **Berkeleyamide / Berkeleyone are absent from the genome**, not just unexpressed.

**Wet-lab budget redirected** ($500-1,000 → $0 antiSMASH first; $5-15K only if computational signal warrants). If antiSMASH returns plausible homologs in cheese strains → wet-lab. If T. amestolkiae has a clean BGC but cheese strains don't → engineer the Berkeleyamide BGC into the koji chassis (A. oryzae heterologous host already supports andrastin-type meroterpenoid assembly per Matsuda 2013).

Already in the wiki via:
- [`medicinal-mushroom-complement-track.md`](../../wiki/medicinal-mushroom-complement-track.md) §"Ascomycete secondary metabolites" — full Talaromyces correction + 3-reason food-grade Penicillium misdirection documentation + corrected computational-first path
- [`logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md`](../../logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md) — J2 lit scan source report
- Cluster J1 closure annotation — Pass 2 failure-mode trace (surface-level taxonomy pattern-matching without 2014+ reclassification check)

**Multi-vendor heterogeneity guard worked as designed:** the J2 lit-scan subagent caught the *Talaromyces* reclassification within minutes of the daemon's "Penicillium"-framed curious-thread, and the J1 wiki edit was corrected accordingly. Same pattern as the CFH allele-frequency catch (Cluster A2 follow-up) earlier in this walkthrough.
