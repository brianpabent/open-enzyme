# Synthesis queue

`synthesis/queue/` contains unresolved actions from explicit full-corpus synthesis, COMP push reviews, and other current detectors. It is project-management state, not scientific evidence.

## Current-state rule

- One file per unresolved item.
- Action the item in its canonical wiki, experiment, or operations file.
- Delete the queue file when the action is resolved or deliberately rejected.
- An empty queue is inbox zero.
- Do not move completed items into another live directory. Git records the finding, decision, and deletion.
- Do not store successful run narratives here. A full-synthesis run retains only its coverage/cost receipt in `logs/sweep-state.json`; raw recovery artifacts expire from CI.

COMP review findings use a stable filename, `comp-review-NNN.md`. A later exact-snapshot review replaces that file or deletes it when clean, so there is never an accumulating review archive in the live tree.

## Producers

- `scripts/distributed-synthesis.py` produces candidate findings only during an explicit full synthesis.
- `scripts/synthesis-emit-files.py --no-history` emits reviewed findings into the queue.
- `scripts/comp-review.py` maintains the stable COMP action item.
- Quarterly or manual detectors may add another unresolved item, but must follow the same delete-on-resolution rule.

Scientific claims belong in `wiki/`; reproducible computational artifacts belong in their `comp-NNN` directories; Git is the revision history.
