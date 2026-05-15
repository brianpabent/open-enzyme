---
type: connection
sweep_date: 2026-05-14
sweep_sha: 81e6264
section_index: 1
global_index: 1
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# ClockBase-style cassette ranking + cordycepin burden analysis converge on a tractable triple-cassette endgame strain (uricase + lactoferrin + cordycepin) that bypasses the chaperone bottleneck by exploiting cytosolic orthogonality.

1. **ClockBase-style cassette ranking + cordycepin burden analysis converge on a tractable triple-cassette endgame strain (uricase + lactoferrin + cordycepin) that bypasses the chaperone bottleneck by exploiting cytosolic orthogonality.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `uricase-cassette-ranking-computational.md`, `cordycepin-cassette-burden-computational.md`, `chaperone-orthogonal-stacking.md`, `koji-endgame-strain.md`, `computational-experiments.md`
   - *Page-pair linkage:* `uricase-cassette-ranking-computational.md` ↔ `cordycepin-cassette-burden-computational.md` are weakly connected — both are new comp-NNN pages, linked only through `computational-experiments.md` and `koji-endgame-strain.md`. Neither cites the other directly.
   - *Why It Matters:* The chaperone-orthogonal-stacking framework (§5.5) predicted that adding a third secreted cassette (DAF SCR1-4) to the dual uricase + lactoferrin strain would push PDI/ERO1 load into the sub-0.6 synergy regime, forcing separate-strain routing. comp-022 (cassette ranking) now provides a refined uricase cassette design (5′-softened codon variant, PTS1-blocking tag, N191Q glycosylation ablation), and comp-023 (cordycepin burden) demonstrates that the cns1+cns2 cordycepin pathway is **cytosolic** — imposing zero PDI load and <1% metabolic burden at the Jeennor 2023 titer. The three analyses compose into a design escape: the third cassette does not need to be secreted. A triple-cassette strain carrying uricase (secreted, PDI-light), lactoferrin (secreted, PDI-heavy), and cordycepin (cytosolic, PDI-null) is predicted to retain the dual-cassette synergy of ≥0.85 while adding URAT1-modulating cordycepin at negligible additional burden. This is a **three-document composition** — none of the individual pages names this specific triple, and the chaperone framework’s triple-cassette discussion focused exclusively on secreted payloads.
   - *Suggested Action:* Run a combined in silico feasibility pass: take comp-022’s top uricase cassette, comp-010’s lactoferrin cassette, and comp-023’s cns1+cns2 cassette parameters; model the triple-cassette strain under the chaperone-orthogonal-stacking framework (PDI load = 0 + 24–40 + 0 = 24–40, within demonstrated NSlD-ΔP10 capacity) and the iWV1314 FBA (cordycepin demand at 564 mg/L/d). If both axes are green, add a cordycepin arm to the §1.9 wet-lab design at marginal cost (~$1,500–2,500, 2–3 weeks).

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The composition is real: `chaperone-orthogonal-stacking.md` scores cns1+cns2 cordycepin as cytosolic with PDI load 0, and `cordycepin-cassette-burden-computational.md` gives a GREEN FBA verdict at the Jeennor 564 mg/L/day titer. But the suggested calculation overstates the source: `chaperone-orthogonal-stacking.md` treats lactoferrin’s architecture-adjusted effective PDI load as 24–40 and explicitly frames the Lf-alone capacity question as unresolved against the Huynh 16-disulfide reference, so “within demonstrated NSlD-ΔP10 capacity” and a clean ≥0.85 triple-synergy claim are not source-supported. Keep the design-escape insight, but soften the synergy/capacity language and route it through the §1.9 Lf-alone/dual-cassette readout.

---

## ✓ Actioned 2026-05-15

The design-escape insight is real and worth documenting; Pass 3's softening on the synergy/capacity overclaims is honored throughout.

**Files shipped:**

- **`wiki/computational-experiments.md` Planned Analyses** — queued **comp-028** (Triple-cassette endgame strain feasibility — does the cytosolic third cassette bypass the chaperone bottleneck?). Brief requires two orthogonal models (chaperone framework with explicit confidence bounds + iWV1314 FBA with dual-cassette baseline overlay), explicit GREEN/YELLOW/RED decision rule, and the Pass 3 softening discipline baked in: synergy is an *outcome* of comp-028, not an *input*; "within demonstrated capacity" is replaced with "PDI load budget the design must fit within"; ≥0.85 triple-synergy framing is explicitly NOT a load-bearing claim. The brief cites the BioDesignBench evaluation-depth discipline in `autonomous-screening-methodology.md` §"BioDesignBench evaluation-depth audit" as the methodology rationale.
- **`wiki/chaperone-orthogonal-stacking.md` §5.6 (new)** — "Design escape — cytosolic third cassette bypasses the secreted-stacking bottleneck." Names the structural insight (cytosolic cassettes are PDI-null and don't compete for chaperone capacity), preserves the Pass 3 softening (Lf-alone capacity question still unresolved; synergy framework was derived for secreted-only payloads; comp-028 is the gate), and adds a generalization paragraph for future OE design decisions: the practical stacking limit is the count of *secreted* cassettes, not total cassette count. A four-cassette strain of uricase + Lf + cordycepin + ergothioneine biosynthesis is, in principle, no harder on chaperone capacity than the dual-cassette baseline.

**Pass 3 softening discipline applied throughout:**
- Replaced "within demonstrated NSlD-ΔP10 capacity" with "PDI load 24–40 as the *budget* the design must fit within, not as a *demonstrated-capacity* assertion"
- Replaced "≥0.85 triple-synergy" with "synergy question is an outcome of comp-028, not an input"
- §3.5.4 calibration-data dependency (Lf-alone in §1.9) explicitly cross-linked from the §5.6 design-escape framing

**No new wet-lab commitment.** The cordycepin arm of §1.9 is gated on comp-028's GREEN/YELLOW/RED verdict, not on the §5.6 framework-level argument alone.

**Six-surface tracking:**
1. `wiki/chaperone-orthogonal-stacking.md` §5.6 (canonical design-escape framing)
2. `wiki/computational-experiments.md` Planned Analyses — comp-028 row
3. `wiki/validation-experiments.md` §1.9 — already references the cordycepin arm; comp-028's GREEN verdict would unblock it
4. `wiki/koji-endgame-strain.md` — already discusses the multi-cassette endgame; no edit needed (cross-referenced from §5.6)
5. `wiki/cordycepin-cassette-burden-computational.md` (comp-023) — already documents the cytosolic / PDI-null finding; no edit needed
6. This closure annotation + the queue→done move

Pass 3's "Partial" verdict was correct on both counts (keep insight, soften language). Closing.
