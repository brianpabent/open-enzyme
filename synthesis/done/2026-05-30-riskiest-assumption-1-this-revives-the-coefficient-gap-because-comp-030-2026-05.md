---
type: riskiest-assumption
sweep_date: 2026-05-30
sweep_sha: 0317c56
section_index: 1
global_index: 21
pass3_verdict: unknown
overlap_tag: EXTENSION
---

# This revives the α-coefficient gap because comp-030 (2026-05-15) introduced ESM2 pseudo-pLDDT as a Tier 3 fold-quality proxy for the CCP/SCR architecture, materially shifting the calibration confidence of the standing belief from "in vitro folding kinetics only" to "in vitro + in silico structural robustness.

This revives the α-coefficient gap because comp-030 (2026-05-15) introduced ESM2 pseudo-pLDDT as a Tier 3 fold-quality proxy for the CCP/SCR architecture, materially shifting the calibration confidence of the standing belief from "in vitro folding kinetics only" to "in vitro + in silico structural robustness." The canonical chaperone-orthogonal α-coefficient calibration gap (transferrin-lobe α 1.5–2.5 / CCP-SCR α 0.3–0.6 from chaperone-orthogonal-stacking.md) is now supported by a second independent computational method (ESM2) that corroborates the low-α prediction for SCR1-4 (mean pseudo-pLDDT 88.8, 100% above 80). The §1.25 wet-lab gate (DAF SCR1-4 expression + activity in NSlD-ΔP10 solid-state) remains the resolution experiment, but the new ESM2 evidence narrows the uncertainty band and justifies keeping the section rather than omitting it per the dedup discipline. (source: chaperone-orthogonal-stacking.md §3.5.2 + §8 item 6; daf-cd55-scr14-cassette-ranking-computational.md)

> **Claude review — Augment.** `[OVERLAP: EXTENSION]` The comp-030 numbers are accurate — the archive reports mean ESM2 pseudo-pLDDT 88.8, range 87.6–89.8, and 100% above 80 across 720 DAF SCR1-4 protein-distinct candidates — and they do corroborate the low-α CCP/SCR prior. The augmentation is methodological: pseudo-pLDDT supports fold robustness, not direct PDI residence time, and the comp-034 pLDDT-as-accessibility failure reinforces that structural-confidence proxies must stay labeled as proxies until §1.25 wet-lab calibration measures secretion/activity.

---

## ✓ Already actioned 2026-06-01 (closure note) — pre-resolved on three fronts

This is an instance of the **Riskiest Assumption section, which was retired this walk** (Item 8 / commit 46080c9b) — the forced rank kept regurgitating the α-coefficient gap, and Grok ignored the dedup/omit discipline. So this item will not recur in future sweeps.

The one nugget Pass 3 flagged (Augment) is **already fully documented**:
- The comp-030 ESM2 pseudo-pLDDT corroboration (mean 88.8, 100% above 80 across 720 DAF SCR1-4 candidates → sequence-robust, fast-folding) is recorded at [`chaperone-orthogonal-stacking.md` §3.5.4](../../wiki/chaperone-orthogonal-stacking.md) line 165, tagged `[NUMBER PARTIALLY UNVERIFIED]`.
- Pass 3's methodological caveat — pseudo-pLDDT supports *fold robustness*, NOT direct *PDI residence time* (the actual α), and structural-confidence proxies must stay labeled as proxies until the §1.25 wet-lab calibration — is pervasive in that page (§3.5.2, §3.5.4, §8 item 6, §10.2; line 586 explicitly calls the CCP/SCR α "the largest unverified assumption in the architecture model"). The comp-034 pLDDT-as-accessibility failure (Item 12) reinforces exactly this discipline.

No new wiki work: retired section + comp-030 corroboration documented + proxy caveat already thorough. Genuinely open + gated on §1.9 + §1.25 wet-lab (access-blocked, Phase 0).
