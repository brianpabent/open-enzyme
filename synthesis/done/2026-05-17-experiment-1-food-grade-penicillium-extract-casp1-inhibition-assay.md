---
type: experiment
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 1
global_index: 9
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Food-grade *Penicillium* extract CASP1 inhibition assay.

1. **Food-grade *Penicillium* extract CASP1 inhibition assay.** Cost: $500–1,000. Time: 2 weeks. Decides: whether food-fermentation-accessible *Penicillium* species (P. camemberti, P. roqueforti) produce the Berkeleyamide/Berkeleyone chemotype at detectable levels — opening a producer-organism class that bridges cultivation and fermentation tracks. Protocol: grow P. camemberti on standard cheese-ripening substrate, prepare aqueous + ethanolic extracts, test CASP1 inhibition in recombinant human caspase-1 fluorometric assay against Berkeleyamide A as positive control (Cayman Chemical or equivalent). If positive at IC50 < 10 μM → promote to a new "Food-grade ascomycete secondary metabolites" section in the medicinal-mushroom-complement-track. If negative → the Berkeleyamide chemotype is restricted to environmental *Penicillium* isolates; the finding remains a comp-014 curiosity rather than a platform candidate.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` This is the natural wet-lab follow-up to the strongest surprising comp-014 Phase 3 result: Berkeleyamides A/D are the only sub-µM fungal CASP1 hits named in the corpus, and the current medicinal-mushroom track does not cover food-grade ascomycete producers. The experiment is cheap and decisive for platform routing: positive CASP1 inhibition in food-grade *Penicillium* extracts opens a cultivation / fermentation-accessible producer class; negative activity confines the Berkeleyamide finding to environmental-isolate chemistry. Include mycotoxin screening and species-authentication as required QC, because *Penicillium* safety variance is not comparable to the basidiomycete mushroom track.

---

**WALKED 2026-05-19 — Closed (cheap lit-scan discriminator firing; wet-lab assay gated on lit-scan result + wet-lab budget).**

Actioned per the H2 reframing principle (investigate cheaply before committing wet-lab budget):
- 🔄 Lit-scan subagent firing in background. The daemon's own "cheapest possible move" framing: $0, ~30 min, scans whether the Berkeleyamide chemotype is plausibly present in food-grade *Penicillium* species (P. camemberti / P. roqueforti) before the $500-1,000 wet-lab assay commitment. Output → `logs/food-grade-penicillium-casp1-lit-scan-2026-05-19.md`.
- Wet-lab assay status: documented in `medicinal-mushroom-complement-track.md` §"Ascomycete secondary metabolites" as the discriminator that promotes the provisional subsection to a committed track. Gates on (a) lit-scan signal + (b) wet-lab budget allocation (~$500-1,000 with mycotoxin screening + species-authentication QC).
- This sequencing is intentional: a $0 lit scan that returns null on food-grade *Penicillium* materially affects whether the wet-lab budget commit makes sense.
