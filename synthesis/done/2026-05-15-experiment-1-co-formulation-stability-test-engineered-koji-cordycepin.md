---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 1
global_index: 7
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Co-formulation stability test: engineered-koji cordycepin + dried *C. militaris* extract under ADA challenge.

1. **Co-formulation stability test: engineered-koji cordycepin + dried *C. militaris* extract under ADA challenge.** *Cost: $1,500–3,000. Time: 3–4 weeks. Decides:* Whether the cross-chassis ADA-protection strategy (Connection 1 above) is viable, avoiding pentostatin co-engineering. Protocol: spike engineered-koji cordycepin fermentate with *C. militaris* extract calibrated for pentostatin content, challenge with bovine ADA, measure cordycepin half-life vs. whole-fermentate *Cordyceps* alone. If ≥50% protection, this route bypasses comp-025/comp-026 gates. Specified in `validation-experiments.md` §2.7 (to be added per Connection 1's Suggested Action).

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: science-gap]` The ADA-challenge co-formulation assay is useful, but the conclusion that success “bypasses comp-025/comp-026 gates” overstates what the assay decides. It tests post-production cordycepin protection under ADA challenge; it does not test native *A. oryzae* ADA competition during cns1+cns2 biosynthesis or regulatory crowding among the uricase/lactoferrin/cordycepin cassette architecture, both of which remain queued in `computational-experiments.md`. Promote the assay as an ADA-protection gate, not as a full cordycepin-track gate bypass.

---

## ✓ Closed via strategic deprioritization 2026-05-16

**Walkthrough Item 13 — moot via koji-cordycepin engineering deprioritization.** The proposed §2.7 co-formulation stability test was designed to gate the koji-cordycepin engineering decision. With koji-cordycepin removed from the active cassette stack via the walkthrough Item 7 strategic call (full reasoning at [`koji-endgame-strain.md` §3.5](../../wiki/koji-endgame-strain.md) and the closure annotation on Connection 1), the gating question is no longer load-bearing. §2.7 is NOT added to the wet-lab queue. The cultivation route already delivers cordycepin + pentostatin together at the natural co-evolved ratio; no co-formulation stability test needed for a product that doesn't exist as an engineered output. Cluster-closure: closes with Items 7, 16, 17, 18 via the same strategic call.
