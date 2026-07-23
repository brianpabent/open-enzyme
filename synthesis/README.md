# Synthesis queue

`synthesis/queue/` contains unresolved actions from explicit full-corpus synthesis, COMP push reviews, and other current detectors. It is project-management state, not scientific evidence.

## Current-state rule

- One file per unresolved item.
- Action the item in its canonical wiki, experiment, or operations file.
- Delete the queue file when the action is resolved or deliberately rejected.
- An empty queue is inbox zero.
- Do not move completed items into another live directory. Git records the finding, decision, and deletion.
- Do not store successful run narratives here. A full-synthesis run retains only its coverage/cost receipt in `logs/sweep-state.json`; raw recovery artifacts expire from CI.

A queue file is a reviewed action brief, never ready-to-paste reader prose. Reopen its cited evidence, identify the canonical owner, and write the current scientific state there. Focused pages receive their own evidence/source/delivery/exposure/falsification update; comparative findings go to portfolio comparison surfaces. Other dependents receive only a local decision delta and a link.

When the useful output is a novel but untested connection, close the queue action by writing a compact **Research Conjecture** on the mechanism-owning wiki page. Its grounded premises retain their evidence tags; its novel leap is stated separately as unsupported; it names why the lead matters and the cheapest discriminating observation. Do not reject a useful lead merely because direct evidence is absent, and do not leave it only in the deletable queue. `wiki/open-questions.md` may receive a one-line link. Promote it to `wiki/hypotheses/` only when it is ready for a committed falsification card.

COMP review findings use a stable filename, `comp-review-NNN.md`. A later exact-snapshot review replaces that file or deletes it when clean, so there is never an accumulating review archive in the live tree.

## Producers

- `scripts/distributed-synthesis.py` produces candidate findings only during an explicit full synthesis.
- `scripts/synthesis-emit-files.py --no-history` emits reviewed findings into the queue.
- `scripts/comp-review.py` maintains the stable COMP action item.
- `scripts/evidence-radar.py` may add a hash-bound, independently reviewed source-delta action. Registry entries remain protocol/status evidence and FAERS entries remain non-causal leads.
- Other quarterly or manual detectors may add another unresolved item only after independent review and must follow the same delete-on-resolution rule.

Scientific claims belong in `wiki/`; reproducible computational artifacts belong in their `comp-NNN` directories; Git is the revision history.
