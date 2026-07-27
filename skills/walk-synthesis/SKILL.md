---
name: walk-synthesis
description: Walk unresolved synthesis/queue items with Brian one at a time, action approved work, delete resolved items, and finish at inbox zero.
---

# Walk synthesis

## Preflight

Read every file in `synthesis/queue/`, group by producer/date/type, and report the count. Wait for Brian to start.

## One-item loop

For one item only:

1. Explain the finding in plain English, including its evidence and uncertainty.
2. Verify that any challenged project claim is real and source-anchored. Corpus absence is not refutation of a world claim; propose the appropriate literature or data check.
3. Ask: which gout weakness does this hit, and is the delivery/production chassis known? Koji is one possible track, never a scope filter.
4. Treat the queue item as an action brief, not reader-facing copy. Reconstruct the update from its cited evidence instead of pasting its framing into the corpus.
5. Audit factual support and idea value separately. If the item's premises are grounded but the connection itself is untested, propose a compact Research Conjecture on the mechanism-owning page rather than rejecting it for lack of direct evidence. The block must separate grounded premises, the unsupported leap, why it matters, and the cheapest discriminating observation. Research Conjecture is not an evidence level.
6. Propose a concrete action and name the canonical files that would change. A focused intervention or chassis page owns that track's evidence, sourcing, delivery, exposure constraints, and falsification gate. Put cross-track rankings or comparison tables only in portfolio surfaces such as `wiki/modality-chokepoint-matrix.md` or `wiki/chassis-pending-interventions.md`; never use another track as the focused page's narrative foil.
7. Keep full evidence or the complete conjecture block in its canonical home. `open-questions.md` and other affected pages receive only a one-line link or local decision delta. Do not add editorial history, corpus-placement narration, personalized treatment instructions, or duplicated exposition.
8. Wait for explicit approval before editing.
9. Make and verify the approved change. Follow load-bearing-number and COMP lifecycle gates. A negative result kills only the exact tested claim; retain adjacent conjectures unless one of their required premises failed.
10. Delete the queue file in the same commit. Do not append a closure essay or move it to a completed-items directory; Git preserves the decision.
11. Summarize what landed and any unresolved follow-up. Auto-advance only after a clean close; otherwise wait.

For a `comp-review-NNN.md` item, do not edit the receipt to make it pass. Fix the experiment or interpretation, then obtain a new exact-snapshot review. The reviewer replaces or deletes the stable queue item.

Do not use tombstoning to optimize walk speed. When repairability or retirement scope is uncertain, stop that COMP’s walk item, place the complete artifact and imported decision libraries in deterministic quarantine, and continue only with unrelated non-destructive items. Final retirement requires a bound independent disposition review, complete surviving-detail and dependency-cascade mapping, and Brian’s explicit decision. Present retirement decisions in batches of at most three.

## Finish

Inbox zero means `synthesis/queue/` contains no unresolved item files. Commit eagerly, but ask before the single end-of-batch push. The push performs publication, COMP review, and propagation; it does not perform full synthesis.

Research belongs in canonical wiki pages, experiment artifacts, or explicit tracking surfaces—not in queue closure narratives.
