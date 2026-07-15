---
type: experiment
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 3
global_index: 7
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.

3. **Houttuynia cordata polysaccharide fraction comparison in MSU-stimulated THP-1 macrophages — prioritization screen.** Cost: ~$1,500–2,500 (CRO macrophage assay). Time: 4–6 weeks. Decides: Whether Houttuynia suppresses MSU-induced IL-1β in a gout-relevant cell model, and whether sourcing (HCPM purified vs. crude vs. commercial capsule) matters. Houttuynia is the corpus's first dual-CP0+CP1 dietary candidate. comp-039 classified HCP/HCPM/CHCP as CFH-independent on mechanism-site grounds (C3 + C4 cleavage targets are mechanistically incompatible with CFH-dependence — CFH is AP-specific not C4), but cell-model translation is a separate question. Cheng 2014 (PMC7112369) documents structure-dependent directionality — purified 60 kDa HCP-2 is pro-inflammatory on naïve PBMCs while the anti-inflammatory phenotype appears in disease-context inflammation — so a generic "Houttuynia extract" capsule cannot be assumed equivalent to the Chen-group HCPM preparation without direct comparison. (source: complement-c5a-gout.md §9.7, nlrp3-exploit-map.md §CP1, upstream-complement-modulator-sweep-computational.md (comp-018 Phase 2), cfh-mechanism-dissociation-cp0-candidates-computational.md §3.3 (comp-039), supplements-stack.md (Houttuynia catalog entry))

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The Houttuynia cordata polysaccharide fraction comparison is well-scoped and correctly identifies the key caveat: Cheng 2014 (PMC7112369) documents structure-dependent directionality — purified 60 kDa HCP-2 is pro-inflammatory on naïve PBMCs while anti-inflammatory activity appears in disease-context inflammation — so a generic extract cannot be assumed equivalent to the Chen-group HCPM preparation. The upstream-complement-modulator-sweep-computational.md Phase 2 confirms the dual-CP0+CP1 classification and the multi-anchor status. The cost estimate ($1,500–2,500) is reasonable for a CRO macrophage assay with multiple fractions. The CFH-independence claim (comp-039 classified HCP/HCPM/CHCP as CFH-independent because C3 + C4 cleavage targets are mechanistically incompatible with CFH-dependence) is correctly relayed. One augmentation: the proposal could add a parallel IL-6 readout (TNFSF14-driven, per `tnfsf14-gout-target.md`) to test the CP1b amplifier loop on the same plate at marginal additional cost, since Houttuynia's NF-κB suppression should hit both NLRP3 priming and TNFSF14-driven amplification.

---

## ✓ Actioned 2026-07-14

**Experiment already registered (§1.30); closed with a dogfooded lit scan that resolved the fraction-directionality question + surfaced a mechanism-grounded safety caution.**

The §1.30 macrophage screen was already registered (added 2026-05-21). Rather than just close-as-actioned + queue the clarity work, we **ran the Houttuynia structure-activity lit scan** as the first dogfooded use of the new `lit-scan` skill (artifact: [`logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md`](../../logs/houttuynia-polysaccharide-structure-activity-lit-scan-2026-07-14.md), commit ecbcd21a).

**What the scan delivered + what propagated:**
- **Structure→directionality rule:** homogalacturonan (pure 1,4-α-GalA, ~60 kDa HCP-2) → TLR4/MD-2 agonist → **PRO**-inflammatory on naïve PBMCs (Cheng 2014, PMID 24528726); branched RG-I (HCPM 19.1 kDa, HC-PS1/3, HBHP-3) → anti-complement → **ANTI** in disease models. Same receptor, opposite outcomes; structure + naïve-vs-disease context axes confounded.
- **Arm A clarified:** purified **HCPM 19.1 kDa RG-I** is the mechanistically-cleanest anti-inflammatory candidate (the only fraction with a direct NLRP3/IL-1β/IL-18-suppression readout, Li 2025 PMID 40654358). **Citation corrected** in §1.30 + dependencies: HCPM 19.1 kDa is **Zhou 2022 (PMID 36252625)**, not Lu 2018 (that's the CHCP crude paper).
- **Mechanism-grounded safety caution + priming-only control arm added to §1.30:** purified HG / crude capsule could supply signal-1 (TLR4→NF-κB→pro-IL-1β priming) and **amplify** IL-1β in the MSU (signal-2) screen, inverting the readout. Added an extract-alone (no-MSU) priming-detection control arm; Xu 2015 bidirectionality is the empirical proof the sign flips.
- **IL-6 reframe (Pass 3 augmentation):** §1.30's existing IL-6 readout now serves triple duty — technical-fail safeguard + CP1b/TNFSF14 amplifier probe + TLR4-priming detector.
- **supplements-stack.md** Houttuynia consumer-caveat enriched with a pointer to the full fraction catalog + rule.
- **Biggest gap (comp-018 Phase-0 caveat honored):** no HC polysaccharide has EVER been tested in an MSU/gout model (confirmed EN + zh) — §1.30 would be the first; Houttuynia correctly stays Phase-0.

**Dogfood outcome (fed back into the skill):** `local_curl_fetch` reached **CQVIP** with genuine SSR full text (carried the zh scan incl. bilingual confirmation of the gout gap); WanFang = JS-shell, Baidu = CAPTCHA, CNKI/ChinaXiv = curl-layer fail — the skill's fetch guidance (step 4) updated to reflect real host reliability. Two-model DeepSeek cross-check on 2 zh sources → full agreement. One library bug surfaced: `OpenRouterClient` uses `urllib` which fails without a cert store — flagged as a follow-up.
