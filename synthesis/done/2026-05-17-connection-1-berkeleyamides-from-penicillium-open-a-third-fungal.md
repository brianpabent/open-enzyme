---
type: connection
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 1
global_index: 1
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Berkeleyamides from *Penicillium* open a third fungal producer class — food-grade ascomycete secondary metabolites, phylogenetically adjacent to koji — that the platform's medicinal-mushroom-complement track doesn't cover.

1. **Berkeleyamides from *Penicillium* open a third fungal producer class — food-grade ascomycete secondary metabolites, phylogenetically adjacent to koji — that the platform's medicinal-mushroom-complement track doesn't cover.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `medicinal-mushroom-compound-mapping-computational.md`, `nlrp3-exploit-map.md`, `medicinal-mushroom-complement-track.md`, `aspergillus-oryzae.md`
   - *Page-pair linkage:* Penicillium is NOT mentioned in the medicinal-mushroom-complement-track candidate species table (which covers only basidiomycetes). Berkeleyamides are NOT in the NLRP3 exploit map's CP4 or CP2 entries. This is a weakly-connected pair across three pages.
   - *Why It Matters:* The comp-014 Phase 3 target mapping found Berkeleyamides A/D from *Penicillium* with direct CASP1 IC50 = 330/610 nM (pChEMBL 6.48/6.21) and Berkeleyones A/B/C with IL-1β IC50 = 2.7–37.8 μM — the first fungal natural products with sub-μM caspase-1 hits in the OE corpus. *Penicillium* is an ascomycete (same phylum as *A. oryzae* koji), unlike the basidiomycete medicinal mushrooms (*Ganoderma*, *Cordyceps*, *Pleurotus*). Some *Penicillium* species are already food-grade (*P. camemberti*, *P. roqueforti* for cheese ripening). This opens a producer-organism class that bridges cultivation (like the mushroom track), food fermentation (like the koji track), and BGC heterologous expression (phylum-internal transfer to *A. oryzae* is easier than basidiomycete→ascomycete). No page in the corpus has named *Penicillium* as a platform-relevant organism. The Berkeleyamides hit CASP1 at the effector-caspase level — a mechanism class the NLRP3 exploit map currently covers only via the pharma caspase-1 inhibitor VX-765 and indirect plant-derived compounds, not via any fungal natural product.
   - *Suggested Action:* Add *Penicillium* to a new "Ascomycete secondary-metabolite candidates" section in the medicinal-mushroom-complement-track scope page. A $500–1,000 in vitro CASP1 inhibition assay on extracts from food-grade *P. camemberti* or *P. roqueforti* (grown on standard cheese-ripening substrate) would determine whether the Berkeleyamide chemotype is present in food-fermentation-accessible species or restricted to the environmental *Penicillium* isolates used in the original 2008/2011 papers. Cheapest possible move: lit scan for "Penicillium camemberti secondary metabolite CASP1 OR inflammasome" — $0, subagent, ~30 min.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The Berkeleyamide/Berkeleyone facts are directly supported by comp-014 Phase 3: Berkeleyamides A/D are *Penicillium* CASP1 hits at 330/610 nM and Berkeleyones A/B/C are IL-1β hits at 2.7/3.7/37.8 µM. The medicinal-mushroom-complement track’s candidate table is basidiomycete-centered and does not name *Penicillium* or an ascomycete secondary-metabolite section, so this is a real platform-scope expansion rather than a restatement. The proposed food-grade-*Penicillium* extract assay is the right cheap discriminator, with the explicit caveat that activity in environmental *Penicillium* isolates does not imply *P. camemberti* / *P. roqueforti* produce the same chemotype under cheese-fermentation conditions.

---

**WALKED 2026-05-19 — Closed (Ascomycete subsection added to medicinal-mushroom-complement-track.md; lit scan firing for food-grade Penicillium discriminator).**

Actioned:
- ✓ Added new "Ascomycete secondary metabolites (provisional, mycotoxin-screening required)" subsection to `medicinal-mushroom-complement-track.md`. Documents the Berkeleyamide A/D / Berkeleyone A/B/C findings with CASP1 IC50 anchors, food-grade species (P. camemberti / P. roqueforti) candidates, phylogenetic adjacency to koji, BGC heterologous-transfer opportunity, and mycotoxin-screening prerequisite. Explicitly scoped as chassis-pending discovery note, not a committed track — promotion gated on lit scan + wet-lab assay results.
- 🔄 Food-grade Penicillium lit scan firing in background. Targets: direct CASP1 evidence for P. camemberti / P. roqueforti, BGC architecture comparison with environmental isolates, substrate-induction angle, mycotoxin overlap with the CASP1 chemotype. Output → `logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md`. This is the cheap discriminator before the $500–1,000 wet-lab assay commitment.

Also closes:
- 2026-05-17 open-question-3 (Should the medicinal-mushroom-complement track's candidate species table include ascomycete producers?)
- 2026-05-17 priority-action-1 (Add Penicillium as Ascomycete subsection).
