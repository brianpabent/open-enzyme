---
type: connection
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 4
global_index: 4
pass3_verdict: Confirmed
overlap_tag: RESTATEMENT
---

# The chaperone framework's §5.6 "cytosolic third cassette" design escape generalizes to a platform-level design rule: the practical stacking limit for the koji endgame strain is the count of *secreted* cassettes, not total cassette count.

4. **The chaperone framework's §5.6 "cytosolic third cassette" design escape generalizes to a platform-level design rule: the practical stacking limit for the koji endgame strain is the count of *secreted* cassettes, not total cassette count.** *Supported.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* [`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`cordycepin-cassette-burden-computational.md`](./cordycepin-cassette-burden-computational.md), [`computational-experiments.md`](./computational-experiments.md)
   - *Page-pair linkage:* `chaperone-orthogonal-stacking.md` §5.6 (newly added 2026-05-15) and `koji-endgame-strain.md` §3 (third-cassette slot design rule, also new) both state the rule, but the generalization to a named platform-level design principle — "the stacking limit is secreted-cassette count, not total cassette count" — is not yet codified as a standalone design heuristic that future payload decisions can reference. The connection composes: (1) the chaperone framework's §5.5 triple-cassette pessimism (0.35–0.65 synergy for secreted-only triples) derived from PDI/ERO1 competition; (2) the §5.6 observation that cytosolic payloads (cns1+cns2 cordycepin, carnosine/panD, native ergothioneine biosynthesis) impose zero PDI/ERO1 load and therefore don't compete for the binding constraint; (3) comp-023's independent FBA confirmation that the cns1+cns2 pathway is metabolically tractable at <1% of carbon flux; and (4) the implication that a four-cassette strain of uricase + lactoferrin (secreted) + cordycepin + ergothioneine biosynthesis (cytosolic) is, in principle, no harder on chaperone capacity than the dual-cassette baseline.
   - *Why It Matters:* This rule changes how the platform evaluates new payload candidates. Previously, the implicit question was "can we add another cassette?" — a count-based framing that treated all cassettes as fungible. The new rule reframes the question as "is the new payload secreted or cytosolic?" — a mechanism-based framing that distinguishes between cassettes that consume the binding constraint (PDI/ERO1 for secreted disulfide-rich proteins) and those that don't. This is operationally load-bearing: when a new therapeutic target is identified (e.g., a C1-INH serpin for the parallel CP0 track, a terpenoid pathway for a novel anti-inflammatory), the first design question is "secreted or cytosolic?" — not "do we have a free cassette slot?" The rule also provides a clean decision heuristic for the §1.9-extended endgame design: the third cassette slot goes to a cytosolic payload (cordycepin, carnosine, or native metabolite enhancement); secreted payloads beyond uricase + lactoferrin route to separate strains or peer-track chassis.
   - *Suggested Action:* Codify the rule as a named design principle in `koji-endgame-strain.md` §3 (the third-cassette slot design rule is already there; elevate it to a standalone callout box) and cross-reference from `chaperone-orthogonal-stacking.md` §5.6. Add a "Payload class decision tree" to `engineered-koji-protocol.md` that asks "secreted or cytosolic?" as the first branching question for any new cassette candidate. The comp-028 triple-cassette feasibility gate (queued in `computational-experiments.md` Planned Analyses) will provide the formal three-axis validation (chaperone + FBA + regulatory architecture) that either confirms or qualifies the rule.

> **Pass 3 review — Confirmed.** `[OVERLAP: RESTATEMENT]` The design rule is correct and already first-class in the corpus: `chaperone-orthogonal-stacking.md` §5.6 states that cytosolic third cassettes bypass the secreted-stacking bottleneck, and `koji-endgame-strain.md` §3 names the third-cassette slot rule for cytosolic payloads. The requested “secreted-cassette count, not total cassette count” callout is sensible, but the scientific content is already present.

---

## ✓ Actioned 2026-05-16

Closed as already-actioned. The "secreted-cassette count, not total cassette count" platform-level design rule is stated in two places in the corpus:

- [`chaperone-orthogonal-stacking.md` §5.6 "Generalization — cytosolic payloads as a strategic design lever"](../../wiki/chaperone-orthogonal-stacking.md) — framework-level statement of the rule with cytosolic / secreted payload classification
- [`koji-endgame-strain.md` §3 "Third-cassette slot design rule"](../../wiki/koji-endgame-strain.md) — strain-design application of the rule (post-Item-7 candidate list = carnosine + ergothioneine biosynthesis; cordycepin removed as active candidate but the rule itself unchanged)

Single edit: added cross-reference from §5.6 → koji-endgame-strain.md §3, with explicit framing that the framework's rule is independent of which specific payloads are currently active (payload selection = strategy decision; cytosolic-vs-secreted framing = structural design rule). This is the right boundary — the framework page carries framework, the strain-design page carries strategy.

**Skipped per the "don't recommend creating what already exists" discipline (SWEEP-ARCHITECTURE.md):**
- Standalone callout box upgrade in koji-endgame-strain.md §3 — the rule is stated clearly enough in the existing paragraph; promoting to a callout is documentation-shape-tweaking with no information gain
- "Payload class decision tree" in engineered-koji-protocol.md — a new decision tool that re-derives the secreted-vs-cytosolic decision already named in §5.6 + §3
- New platform-positioning section — nothing to position that isn't already positioned
