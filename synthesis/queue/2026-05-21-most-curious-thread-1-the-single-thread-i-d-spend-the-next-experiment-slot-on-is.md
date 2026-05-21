---
type: most-curious-thread
sweep_date: 2026-05-21
sweep_sha: 3edb643
section_index: 1
global_index: 15
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The single thread I'd spend the next experiment slot on is the Houttuynia cordata polysaccharide (HCP/HCPM) prioritization screen in MSU-stimulated THP-1 macrophages — validation-experiments §1.

**The single thread I'd spend the next experiment slot on is the Houttuynia cordata polysaccharide (HCP/HCPM) prioritization screen in MSU-stimulated THP-1 macrophages — validation-experiments §1.30.**

*Corpus evidence supporting the hunch:* Houttuynia is the first dual-CP0+CP1 dietary candidate in the corpus (comp-018 Phase 2). It has multi-anchor primary literature from the Chen Daofeng / Fudan group showing complement C3+C4+C5 targeting at CH50 79–318 µg/mL (Lu 2018 PMC5925397) AND intestinal NLRP3/caspase-1/IL-1β suppression + tight-junction restoration in vivo (Li et al. 2025 PMC12254813) AND TLR4-MD2 direct binding with antagonist rescue (Yu et al. 2026 PMC12937656). It was discovered through a query-framing fix ("Houttuynia cordata anti-complementary" rather than "C3 convertase inhibitor") — meaning it was hiding in plain sight in the English-language literature, missed by mechanism-name search. It is widely consumed as a dietary herb across China, Japan, Korea, and Vietnam (魚腥草 / どくだみ / diếp cá). The structure-dependent directionality caveat (Cheng 2014 PMC7112369 — purified 60 kDa HCP-2 is pro-inflammatory on naïve PBMCs while the anti-inflammatory phenotype appears in disease-context inflammation) is exactly the kind of non-obvious pharmacology that makes this compound class either a breakthrough or a dead end.

*Evidence that would refute it:* If none of the three arms in §1.30 (purified HCPM, crude HCP, commercial capsule extract) suppress MSU-induced IL-1β at ≤100 µg/mL in THP-1 macrophages, the dual-chokepoint mechanism does not translate to the gout-relevant cell model. The in vivo murine data from the Chen group would stand, but the gap between murine disease models and human macrophage MSU response would be unresolved. If the commercial extract arm performs dramatically worse than the purified HCPM arm (≥10× dose difference), the "dietary accessibility" claim collapses — Houttuynia becomes a research-grade purified polysaccharide intervention, not a kitchen-accessible dietary herb.

*Cheapest discriminating experiment:* The §1.30 prioritization screen as specified — three arms (HCPM purified, crude HCP, commercial capsule extract) at three log-spaced doses (10, 100, 1000 µg/mL) in MSU-stimulated THP-1 macrophages with IL-1β ELISA as the primary readout — costs ~$1,500–2,500 at a CRO and takes 4–6 weeks. This is the cheapest experiment that discriminates between "Houttuynia is the platform's highest-leverage single dietary intervention" and "Houttuynia is an interesting pharmacology paper that doesn't translate to a macrophage model." The cell-viability control (CCK-8 or MTT) is load-bearing because of the structure-dependent directionality caveat — cytotoxicity at high doses could masquerade as anti-inflammatory effect.

*Multi-vendor signal:* I suspect another sweep model (Claude, GPT-5.5, or a future model) would converge on Houttuynia as the most curious thread, because the pattern is canonical Open Enzyme: a compound surfaced by query-framing fix rather than new biology, multi-anchor primary literature, dual-chokepoint mechanism, dietary accessibility, and a single cheap experiment that discriminates. The structure-dependent directionality caveat adds productive uncertainty — the outcome is genuinely non-obvious ex ante. If I'm idiosyncratic on this pick, it would be because another model weights the PK uncertainty (see Riskiest Assumption above) more heavily and would prefer a direct PK measurement on rosmarinic acid before committing to any dietary CP0 wet-lab work.



---

## Sources cited

- wiki/complement-c5a-gout.md
- wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md
- wiki/purine-degrading-bacteria.md
- wiki/abcg2-modulators.md
- wiki/nlrp3-exploit-map.md
- wiki/gout-genetic-variants.md
- wiki/spm-resolution-pathway.md
- wiki/self-experiment-protocol.md
- wiki/gout-action-guide.md
- wiki/cannabinoids-terpenes.md
- wiki/colchicine.md
- wiki/quantification-ladder.md
- wiki/tier-2-butyrate-assay-audit-computational.md
- wiki/genotype-informed-supplement-workflow.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/validation-experiments.md
- wiki/combined-cp0-systems-model-computational.md
- wiki/gout-pathophysiology.md

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` Houttuynia is a defensible “most curious” pick because it hits documented CP0 and CP1 nodes, has multi-anchor primary evidence in `complement-c5a-gout.md` §9.7 / `nlrp3-exploit-map.md` CP1, and has a cheap discriminating assay already specified in `validation-experiments.md` §1.30. The synthesizer correctly treats the structure-dependent directionality caveat as productive uncertainty rather than a reason to dismiss the candidate. The next action is execution of §1.30, with commercial-extract equivalence and viability controls treated as load-bearing.
