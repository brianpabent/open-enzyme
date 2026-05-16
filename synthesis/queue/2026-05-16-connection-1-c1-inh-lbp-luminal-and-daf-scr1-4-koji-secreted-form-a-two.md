---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 1
global_index: 1
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# C1-INH (LBP-luminal) and DAF SCR1-4 (koji-secreted) form a two-chassis, two-node CP0 coverage architecture that the corpus has not yet named as a unified strategy.

1. **C1-INH (LBP-luminal) and DAF SCR1-4 (koji-secreted) form a two-chassis, two-node CP0 coverage architecture that the corpus has not yet named as a unified strategy.** *Supported*. `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `complestatin-bgc-lbp-feasibility-computational.md`, `engineered-lbp-chassis.md`, `daf-cd55-scr14-truncated-computational.md`, `chaperone-orthogonal-stacking.md`, `complement-c5a-gout.md`, `hypotheses/H05-daf-scr14-cp0-thesis.md`

   - *Page-pair linkage:* **Weak.** The DAF SCR1-4 track (H05) and the LBP-chassis track (H02) are sibling peer-track scope pages that cross-reference each other, but the *specific* C1-INH thread surfaced by comp-024's GREEN-provisional verdict has not been connected to the DAF SCR1-4 thesis as a complementary arm. `complement-c5a-gout.md` mentions C1-INH in the CP0 status update block but treats it as a "near-twin engineering thesis" rather than a second node in a two-chassis CP0 architecture. `chassis-pending-interventions.md` §"Pending entries to triage" mentions C1-INH but not the DAF+C1-INH two-node composition.

   - *Why It Matters:* comp-024 (complestatin BGC LBP feasibility) returned RED for complestatin and GREEN-provisional (0.774) for C1-INH in the LBP-luminal chassis. DAF SCR1-4 (H05) routes through koji secretion; its single-cassette wet-lab gate is §1.25. These two engineered soluble complement regulators hit **different nodes** of the CP0 cascade: C1-INH inactivates C1r/C1s and MASP-2 at the classical/lectin pathway *entry point* (preventing C4b2a convertase formation); DAF accelerates decay of *already-assembled* C4b2a and C3bBb convertases at the MSU crystal *surface*. Together they'd cover convertase-formation (C1-INH, upstream) + convertase-disassembly (DAF, downstream) — two independent mechanisms at two different cascade points, delivered via two completely independent chassis (engineered EcN LBP vs engineered koji). Neither chassis competes for the other's production infrastructure; neither mechanism is redundant with the other.

     The composition also distributes CP0 coverage across two chassis *that already exist as active OE peer tracks* — it doesn't require building a new track. DAF SCR1-4 is already in the koji pipeline (§1.25); C1-INH routes through the LBP pipeline that `engineered-lbp-chassis.md` already defines. The marginal engineering cost is one new cassette (SERPING1 in EcN) on an existing chassis, not a new chassis build-out.

     The cheapest computational prior — a comp-006-style protease-stability + glycosylation feasibility analysis on SERPING1 (C1-INH, UniProt P05155) in EcN-secreted format — is $0 and ~1 week. This directly gates whether C1-INH survives the luminal protease environment of the gut and retains complement-regulatory activity, the same pattern comp-006/comp-012 established for DAF/CD55.

   - *Suggested Action:* Queue a comp-NNN for C1-INH (SERPING1) protease-stability + glycosylation feasibility in EcN-luminal-secreted format, with the comp-006/comp-012 pipeline as template. If GREEN → promote C1-INH (LBP-luminal) as the sister CP0 candidate to H05 (DAF SCR1-4, koji-secreted) and document the two-chassis two-node CP0 architecture in `complement-c5a-gout.md` §9.7 alongside the existing combined-CP0-coverage hypothesis. Cross-reference `chassis-pending-interventions.md` §"Pending entries to triage" where C1-INH is already named as an unscoped entry.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The two-node CP0 composition is sound: `complestatin-bgc-lbp-feasibility-computational.md` explicitly drops complestatin for LBP and promotes C1-INH-on-EcN as GREEN-provisional 0.774, while `hypotheses/H05-daf-scr14-cp0-thesis.md` already frames DAF SCR1-4 as a koji-secreted CP0 candidate and calls C1-INH a sister hypothesis. The novelty is the architecture-level composition — C1-INH at classical/lectin entry plus DAF at convertase decay, across independent chassis — not either regulator alone. Queueing a SERPING1 protease/glycosylation feasibility comp is the right cheap gate before wet-lab commitment.
