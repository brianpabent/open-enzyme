---
type: experiment
sweep_date: 2026-07-15
sweep_sha: eeab5b5
section_index: 1
global_index: 7
pass3_verdict: Confirmed
sweep_id: a68eaeb8939b91ac9d0bf42c
source_synthesis_sha256: 53af1a8e881d713ef1848bffb135b54373df151770468ed91af430aa101dad9b
canonical_items_sha256: 20f08e5cdb1aee45b8ae8e210dba3c1233c597013d00f26e65f8ef5db30b390f
overlap_tag: EXTENSION
---

# Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen

1. **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.** Three arms (HCPM 19.1 kDa purified RG-I fraction, crude HCP, commercial Houttuynia capsule extract) at three log-spaced doses (10, 100, 1000 μg/mL) in LPS-primed, MSU-challenged THP-1 macrophages. Primary readout IL-1β ELISA; secondary IL-6 (CP1b/TNFSF14 amplifier probe) + cell viability. **Cost:** $1,500–2,500. **Time:** 4–6 weeks. **Decides:** whether Houttuynia suppresses MSU-induced IL-1β in a gout-relevant cell model, and whether sourcing/purification matters. If positive on at least one arm, fire comp-040 next for CFH-independence mechanism confirmation. If all arms negative, deprioritize Houttuynia. **[CHAIN-DEPTH: 3+]** **[PHASE-A-MATCH: no]**  
   - *Documents Connected:* `complement-c5a-gout.md`, `nlrp3-exploit-map.md`, `upstream-complement-modulator-sweep-computational.md`, `cfh-mechanism-dissociation-cp0-candidates-computational.md`, `validation-experiments.md` §1.30, `medicinal-mushroom-extract-sops.md`  
   - *Page-pair linkage:* Weak — complement-c5a-gout.md and medicinal-mushroom-extract-sops.md do not cross-reference each other; both link to upstream-complement-modulator-sweep-computational.md but not to each other.  
   - *Why It Matters:* Houttuynia is the corpus's first dietary dual-CP0+CP1 candidate; the structure-dependent directionality (homogalacturonan → pro-inflammatory via TLR4; RG-I → anti-complement) means commercial capsules cannot be assumed equivalent to the Chen-group HCPM fraction. This screen is the cheapest discriminator of consumer-product viability before committing to the more expensive CFH-depleted serum assay (comp-040).  
   - *Suggested Action:* Run the 3-arm 3-dose THP-1/MSU IL-1β screen with the priming-only/extract-alone control arm (no MSU) to detect TLR4-priming signal. If positive on at least one arm, fire comp-040.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The Houttuynia cordata polysaccharide fraction comparison is a well-designed prioritization experiment. The corpus evidence supporting Houttuynia as a dietary dual-CP0+CP1 candidate is documented in `upstream-complement-modulator-sweep-computational.md` and `complement-c5a-gout.md`. The structure-dependent directionality caveat (homogalacturonan → pro-inflammatory via TLR4; RG-I → anti-complement) is correctly identified as the reason commercial capsules cannot be assumed equivalent. The 3-arm (HCPM, crude HCP, commercial capsule extract) × 3-dose design with the priming-only control arm is the right discriminator before committing to the more expensive CFH-depleted serum assay. **Caveat:** the reference to `validation-experiments.md` §1.30 is aspirational — §1.30 does not exist in the current experiment registry (grep confirmed zero matches for `§1\.30` or `1\.30` anywhere in the corpus). The experiment should be assigned the next available §1.XX slot rather than cited as if it already exists. The cost estimate ($1,500–2,500) and timeline (4–6 weeks) are reasonable for a CRO-executed THP-1 ELISA screen.
