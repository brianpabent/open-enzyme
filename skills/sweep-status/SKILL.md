---
name: sweep-status
description: Report propagation, synthesis, COMP-review, evidence-radar, and queue state for Open Enzyme without changing anything.
---

# Sweep status

Use this read-only skill when Brian asks whether the knowledge system is current.

Read:

```bash
python3 scripts/sweep-state.py read
python3 scripts/sweep-state.py pending-propagation-paths
python3 scripts/sweep-state.py pending-synthesis-paths
python3 scripts/evidence-radar.py status
gh run list --workflow=knowledge-update.yml --limit 5 --json status,conclusion,databaseId,createdAt,displayTitle,url
gh run list --workflow=wiki-sweep.yml --limit 5 --json status,conclusion,databaseId,createdAt,displayTitle,url
gh run list --workflow=evidence-radar.yml --limit 5 --json status,conclusion,databaseId,createdAt,displayTitle,url
```

Report seven fields:

1. last successful propagation commit and time;
2. propagation backlog count and first five paths;
3. last successful explicit synthesis commit, time, coverage receipt, and cost;
4. synthesis backlog count and first five paths;
5. changed COMP paths whose exact current push review is missing or blocked, separated by propagation and synthesis eligibility;
6. active queue count plus the recommended next action.
7. each evidence-radar feed's last complete source snapshot, cursor where applicable, unresolved source faults, candidate/review counts, and review cost.

Recommendations:

- propagation backlog and no run active: run the propagation catch-up;
- COMP-blocked paths: review those COMPs before propagation or synthesis;
- synthesis backlog alone: report it; do not imply it is an error or auto-run synthesis;
- queue files: walk the queue;
- an incomplete radar source: report the failed source/query; do not describe the feed as current and do not advance its cursor manually;
- a complete zero-candidate radar run: report it as current without suggesting synthesis;
- no propagation backlog, no blocked COMP changes, empty queue: current for push-time duties.

Do not move a cursor, dispatch a workflow, or equate “propagated” with “fully synthesized.”
