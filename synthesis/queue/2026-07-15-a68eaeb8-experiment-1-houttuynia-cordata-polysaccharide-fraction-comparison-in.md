---
type: experiment
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 1
global_index: 7
pass3_verdict: Partial
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: NOVEL
---

# Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen

1. **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.** Three arms (HCPM 19.1 kDa purified RG-I fraction, crude HCP, commercial Houttuynia capsule extract) at three log-spaced doses (10, 100, 1000 μg/mL) in LPS-primed, MSU-challenged THP-1 macrophages. Primary readout IL-1β ELISA; secondary IL-6 (CP1b/TNFSF14 amplifier probe) + cell viability. **Cost:** $1,500–2,500. **Time:** 4–6 weeks. **Decides:** whether Houttuynia suppresses MSU-induced IL-1β in a gout-relevant cell model, and whether sourcing/purification matters. If positive on at least one arm, fire comp-040 next for CFH-independence mechanism confirmation. If all arms negative, deprioritize Houttuynia. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `complement-c5a-gout.md`, `nlrp3-exploit-map.md`, `upstream-complement-modulator-sweep-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `validation-experiments.md` §1.30, `medicinal-mushroom-extract-sops.md`  
   - *Page-pair linkage:* Weak — complement-c5a-gout.md and medicinal-mushroom-extract-sops.md do not cross-reference each other; both link to upstream-complement-modulator-sweep-computational.md but not to each other.  
   - *Why It Matters:* Houttuynia is the corpus's first dietary dual-CP0+CP1 candidate; the structure-dependent directionality (homogalacturonan → pro-inflammatory via TLR4; RG-I → anti-complement) means commercial capsules cannot be assumed equivalent to the Chen-group HCPM fraction. This screen is the cheapest discriminator of consumer-product viability before committing to the more expensive CFH-depleted serum assay (comp-040).  
   - *Suggested Action:* Run the 3-arm 3-dose THP-1/MSU IL-1β screen with the priming-only/extract-alone control arm (no MSU) to detect TLR4-priming signal. If positive on at least one arm, fire comp-040.

> **Pass 3 review — Partial.** `[OVERLAP: NOVEL]` `[GAP: tool-gap]` The Houttuynia experiment concept is strong and well-motivated — the structure-dependent directionality (homogalacturonan → pro-inflammatory via TLR4; RG-I → anti-complement) is documented in the upstream-complement corpus, and the 3-arm 3-dose THP-1/MSU IL-1β screen is a sensible discriminator before committing to the more expensive CFH-depleted serum assay. However, three of the five cited documents do not exist in the corpus: `complement-c5a-gout.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, and `validation-experiments.md` §1.30 (the validation-experiments page has no Houttuynia section). The cost estimate ($1,500–2,500) and timeline (4–6 weeks) are synthesis-generated, not corpus-anchored. The experiment is worth queuing; the citation chain needs correction before the walkthrough can rely on it.
