---
type: experiment
sweep_date: 2026-07-01
sweep_sha: 18d3696
section_index: 1
global_index: 5
pass3_verdict: Confirmed
overlap_tag: NOVEL
---

# Validate GSDMD-pore delivery of KPV in MSU-stimulated macrophages.

1. **Validate GSDMD-pore delivery of KPV in MSU-stimulated macrophages.** `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Cost:* ~$2,000-5,000. *Time:* 4-6 weeks. *Decides:* Whether the novel synergistic delivery mechanism proposed in "New Connections #3" is biologically real.
   - *Protocol:* Stimulate THP-1 macrophages with LPS+MSU to induce GSDMD-mediated pyroptosis. Co-incubate with a fluorescently-labeled KPV peptide (e.g., FITC-KPV). Use confocal microscopy and/or flow cytometry to quantify intracellular fluorescence.
   - *Controls:* Unstimulated cells (no pores), cells treated with a GSDMD inhibitor like disulfiram (pores blocked), cells treated with a membrane-permeant fluorescent dye as a positive control for uptake.
   - *Success:* Significantly higher intracellular fluorescence in pyroptotic cells vs. controls, reversed by disulfiram. This would provide the first evidence for a novel, self-targeting drug delivery mechanism highly relevant to acute gout flares.

> **Pass 3 review — Confirmed.** `[OVERLAP: NOVEL]` The experiment is well-designed, tests the Connection #3 hypothesis directly, and the cost estimate ($2,000–5,000) is realistic for a THP-1 macrophage + confocal/flow experiment with fluorescently-labeled KPV. One strengthening note from `gsdmd-pore-delivery-paradox.md` §"Open questions" (Tier-1 delivery-readout precursor added 2026-06-01): consider a staged approach where a cheaper *delivery-only* experiment (fluorescent-KPV uptake with/without nigericin-induced pores, flow cytometry readout) gates the full IL-1β efficacy experiment. If KPV doesn't enter pore-forming cells faster than intact-membrane controls, the self-delivery thesis fails at the physical-transport step and the IL-1β readout is moot. The staged design isolates the delivery claim from the efficacy claim and saves ~$2,000 if the delivery mechanism doesn't survive the first gate. Controls are appropriate: unstimulated cells, disulfiram as GSDMD pore blocker, plus the suggested membrane-permeant positive control.
