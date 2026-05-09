---
type: connection
sweep_date: 2026-05-09
sweep_sha: 259a8e8
section_index: 4
global_index: 4
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# The tiered quantification ladder (kitchen → smartphone → bench → outsource) generalises as a cross-track quality framework for Open Enzyme.

4. **The tiered quantification ladder (kitchen → smartphone → bench → outsource) generalises as a cross-track quality framework for Open Enzyme.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `enzyme-quantification-protocol.md`, `medicinal-mushroom-extract-sops.md`
   - *Page-pair linkage:* Weak. `enzyme-quantification-protocol` explicitly describes the four-tier ladder for koji digestive enzymes. `medicinal-mushroom-extract-sops` (SOP-6) independently adapts the same ladder for cordycepin, ergothioneine, and GLPP. No wiki page names this as a **general Open Enzyme quality methodology** — the two implementations exist as local solutions rather than a unified platform-level discipline.
   - *Why It Matters:* The “calibrate once at Tier 3, track batches at Tier 1/2” pattern is what makes both the koji track and the mushroom track feasible at distributed, open-source scale. Elevating it from two separate SOP sets into a named platform principle (`quantification-ladder.md`) would make it reusable for the TCM track, the siRNA/URAT1 track, and any future compound class the discovery engine surfaces. This is a meta-level infrastructure observation — it improves the platform’s efficiency without changing any scientific hypothesis.
   - *Suggested Action:* Draft a short principle page (`open-source-platform.md` section or standalone) documenting the quantification ladder as a cross-track quality methodology, with explicit references to both the enzyme and mushroom instantiations. This is a documentation synthesis, not a new experiment.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` The “no wiki page names this as a general methodology” premise is too strong: `medicinal-mushroom-extract-sops.md` SOP-6 already says the four-tier framework from `enzyme-quantification-protocol.md` “transfers cleanly to mushroom extract characterization” and states the “calibrate-once-at-Tier-3, track-batches-at-Tier-1/2” discipline. A standalone platform-principle page may still be useful, but the finding should be framed as elevating an already named cross-track SOP pattern, not discovering two isolated local solutions.
