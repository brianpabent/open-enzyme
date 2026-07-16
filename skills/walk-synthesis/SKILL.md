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
4. Propose a concrete action and name the canonical files that would change.
5. Wait for explicit approval before editing.
6. Make and verify the approved change. Follow load-bearing-number and COMP lifecycle gates.
7. Delete the queue file in the same commit. Do not append a closure essay or move it to a completed-items directory; Git preserves the decision.
8. Summarize what landed and any unresolved follow-up. Auto-advance only after a clean close; otherwise wait.

For a `comp-review-NNN.md` item, do not edit the receipt to make it pass. Fix the experiment or interpretation, then obtain a new exact-snapshot review. The reviewer replaces or deletes the stable queue item.

## Finish

Inbox zero means `synthesis/queue/` contains no unresolved item files. Commit eagerly, but ask before the single end-of-batch push. The push performs publication, COMP review, and propagation; it does not perform full synthesis.

Research belongs in canonical wiki pages, experiment artifacts, or explicit tracking surfaces—not in queue closure narratives.
