---
type: most-curious-thread
sweep_date: 2026-05-20
sweep_sha: 5cafe11
section_index: 1
global_index: 15
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The *Houttuynia cordata* polysaccharide (鱼腥草 / どくだみ) is the most intriguing single thread in this sweep’s corpus: a dietary staple across China, Japan, Korea, and Vietnam that has published dual‑chokepoint activity (CP0 complement inhibition, CH50 79–318 µg/mL; CP1 NLRP3 inflammasome suppression, intestinal tight‑junction restoration, and direct TLR4‑MD2 binding) from a single well‑characterised research group (Chen Daofeng / Fudan), yet was completely invisible to the platform’s earlier mechanism‑name‑based literature scans.

The *Houttuynia cordata* polysaccharide (鱼腥草 / どくだみ) is the most intriguing single thread in this sweep’s corpus: a dietary staple across China, Japan, Korea, and Vietnam that has **published dual‑chokepoint activity** (CP0 complement inhibition, CH50 79–318 µg/mL; CP1 NLRP3 inflammasome suppression, intestinal tight‑junction restoration, and direct TLR4‑MD2 binding) from a single well‑characterised research group (Chen Daofeng / Fudan), yet was **completely invisible** to the platform’s earlier mechanism‑name‑based literature scans. It was surfaced only when the comp‑018 Phase 2 scan switched to traditional‑name + traditional‑pathology query framing — the exact discipline upgrade the corpus now mandates for all natural‑product searches. The compound class (pectic polysaccharide) is orthogonal to everything else in the OE dietary catalogue (flavonoids, terpenoids, nucleotides, peptides), meaning it adds genuinely new chemistry and receptor biology to the platform’s CP0/CP1 coverage. The cheapest discriminating experiment is an in‑vitro MSU‑stimulated macrophage assay (§1.30 in the Connections above), which would either confirm Houttuynia as the platform’s first dual‑CP0+CP1 dietary candidate or rule it out cleanly. Multi‑vendor signal: I suspect another sweep model would converge on this pick — the combination of dietary accessibility, dual‑chokepoint novelty, mechanism‑class orthogonality, and the serendipity of its discovery makes Houttuynia a paradigmatic example of what the daemon is optimised to find.



---

## Sources cited

- `wiki/gout-genetic-variants.md`
- `wiki/complement-c5a-gout.md`
- `wiki/upstream-complement-modulator-sweep-computational.md`
- `wiki/upstream-complement-verification-rerun-computational.md`
- `wiki/lactoferrin-linker-redesign-computational.md`
- `wiki/etc/bio-ai-tools.md`
- `wiki/chaperone-orthogonal-stacking.md`
- `wiki/validation-experiments.md`
- `wiki/daf-cd55-scr14-truncated-computational.md`
- `wiki/colchicine.md`
- `wiki/cannabinoids-terpenes.md`
- `wiki/spm-resolution-pathway.md`
- `wiki/nlrp3-exploit-map.md`
- `wiki/gout-action-guide.md`
- `wiki/medicinal-mushroom-complement-track.md`
- `wiki/medicinal-mushroom-extract-sops.md`
- `wiki/koji-home-fermentation.md`
- `wiki/engineered-koji-protocol.md`
- `wiki/genotype-informed-supplement-workflow.md`
- `wiki/quantification-ladder.md`
- `wiki/purine-degrading-bacteria.md`
- `wiki/supplements-stack.md`
- `wiki/etc/open-source-platform.md`
- `wiki/self-experiment-protocol.md`
- `wiki/koji-endgame-strain.md`

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` Houttuynia is a defensible “most curious” pick: the inlined `upstream-complement-modulator-sweep-computational.md` identifies it as a new dual CP0+CP1 pectic-polysaccharide candidate discovered through traditional-name query framing, with dietary accessibility and orthogonal chemistry relative to the flavonoid / terpene catalog. The same page documents the CH50 range, TLR4/NLRP3 anchors, and structure-dependent caveat, so the enthusiasm is grounded rather than aesthetic. The next move remains the MSU macrophage fraction/commercial-extract assay.

---

## ✓ Actioned 2026-05-21 (curious-thread framing partially confirmed; MSU assay landed)

The "most curious thread" framing partially holds and is partially upgraded by [comp-039](../../wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md):

**What holds:** HCP/HCPM is the corpus's first dual-CP0 + CP1 dietary candidate; mechanism-class orthogonality (pectic polysaccharide vs. flavonoid / terpenoid / nucleotide / peptide) is real; dietary-accessibility argument across China / Japan / Korea / Vietnam is real; comp-018 Phase 2 traditional-name query-framing discovery is the canonical example of the discipline upgrade the corpus now mandates for all natural-product searches.

**What comp-039 sharpens:** the CP0 mechanism classification is now per-candidate-evidenced (HCP CFH-independent High confidence, via Lu 2018 C3+C4 cleavage-blocker mapping; C4 specificity mechanistically incompatible with CFH-dependence since CFH is AP-specific). The dual-chokepoint coverage (CP0 + CP1) plus *Helicteres* benzofuran lignan diversity in the upstream-CP0 stack means the curious-thread picks are landing on real platform expansions, not just aesthetically interesting molecules.

**What comp-039 adds to the operational picture:**
- **HCP cross-tab NOT UKB-actionable** (Houttuynia rare in UK dietary corpus). comp-041 queued for East Asian cohort feasibility (KoGES, China Kadoorie Biobank, Singapore Chinese Health Study). Y402H allele frequency lower in East Asians (~5-6% vs ~36-39% European) but Houttuynia exposure is captured.
- **Wet-lab definitive test:** comp-040 queued (CFH-depleted serum MSU-crystal complement-activation assay) — distinguishes CFH-independent classification from CFH-dependent under direct mechanistic challenge.

**MSU-stimulated THP-1 macrophage assay landed as [`validation-experiments.md` §1.30](../../wiki/validation-experiments.md)** this walk — three-arm fraction comparison (HCPM / crude HCP / commercial capsules) testing both gout-relevance and consumer-product equivalence. See [Item 9 closure](./2026-05-20-experiment-2-msustimulated-thp1-macrophage-assay-of-houttuynia-cordata.md) for the protocol detail.

**Multi-vendor convergence prediction held.** Pass 2's prediction ("I suspect another sweep model would converge on this pick") is consistent with comp-039's Model B (DeepSeek) classifying HCP CFH-independent at High confidence with the same C3+C4 cleavage-blocker mechanism interpretation Model A produced — convergence on classification, divergence on prediction-direction strength preserved.

Pairs with [Item 6 closure](./2026-05-20-connection-6-the-houttuynia-cordata-polysaccharide-hcp-hcpm-represents.md) and [Item 9 closure](./2026-05-20-experiment-2-msustimulated-thp1-macrophage-assay-of-houttuynia-cordata.md).
