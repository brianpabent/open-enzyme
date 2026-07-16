---
name: sweep-status
description: Report propagation, synthesis, COMP-review, and queue state for Open Enzyme without changing anything.
---

# Sweep status

Use this read-only skill when Brian asks whether the knowledge system is current.

Read:

```bash
python3 scripts/sweep-state.py read
python3 scripts/sweep-state.py pending-propagation-paths
python3 scripts/sweep-state.py pending-synthesis-paths
gh run list --workflow=knowledge-update.yml --limit 5 --json status,conclusion,databaseId,createdAt,displayTitle,url
gh run list --workflow=wiki-sweep.yml --limit 5 --json status,conclusion,databaseId,createdAt,displayTitle,url
```

Report six fields:

1. last successful propagation commit and time;
2. propagation backlog count and first five paths;
3. last successful explicit synthesis commit, time, coverage receipt, and cost;
4. synthesis backlog count and first five paths;
5. changed COMP paths whose exact current push review is missing or blocked, separated by propagation and synthesis eligibility;
6. active queue count plus the recommended next action.

Recommendations:

- propagation backlog and no run active: run the propagation catch-up;
- COMP-blocked paths: review those COMPs before propagation or synthesis;
- synthesis backlog alone: report it; do not imply it is an error or auto-run synthesis;
- queue files: walk the queue;
- no propagation backlog, no blocked COMP changes, empty queue: current for push-time duties.

Do not move a cursor, dispatch a workflow, or equate “propagated” with “fully synthesized.”
