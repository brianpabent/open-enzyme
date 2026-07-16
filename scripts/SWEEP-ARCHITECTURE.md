# Open Enzyme knowledge architecture

The system separates cheap, routine correctness from expensive, explicit discovery.

## Mission invariant

Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.

Every intervention is a falsifiable track. Koji is one track, not the project. A failed track should improve the exploit map and then stop consuming project identity.

## Event flow

```text
push to main
  ├─ publish current website (always)
  └─ knowledge-update coordinator
       ├─ identify changed COMP artifacts
       ├─ exact-snapshot COMP push review
       └─ bounded cross-page propagation if eligible

explicit manual request
  └─ full-corpus distributed synthesis
       ├─ require propagation backlog = 0
       ├─ require exact eligible COMP receipts
       ├─ read every corpus section twice
       ├─ compare every domain pair
       ├─ reopen cited raw sections and exact COMP outputs
       ├─ independent adversarial review
       └─ emit unresolved queue items only
```

## State

`logs/sweep-state.json` is compact operational state, not a narrative log.

- `last_successful_propagation`: the latest fully considered push batch;
- `last_successful_synthesis`: the latest completely covered corpus snapshot, including coverage digest and cost;
- `comp_reviews`: current exact-snapshot review eligibility by COMP;
- `unresolved_failures`: active failures only.

The two cursors are intentionally independent. A push may be fully published and propagated while remaining unsynthesized until Brian explicitly requests a sweep.

## Push-time propagation

`knowledge-update.yml` calls `comp-review.yml`, then `wiki-propagate.yml`.

Propagation:

- receives an explicit eligible path set;
- links to canonical evidence instead of copying exposition;
- updates direct dependents, hypotheses, dashboard/nav, and public surfaces as needed;
- refuses partial work beyond its path or cost cap;
- can advance on a verified no-op;
- never performs novelty synthesis.

A changed COMP blocks its derived claims until the current artifact has an exact push review. The structured review independently states propagation and synthesis eligibility.

## Three COMP reviews

1. Authoring pre-run review binds code, inputs, provenance, rules, and planned outputs before result-bearing execution.
2. Authoring post-run review binds code/input/output plus every proposed interpretation before completion or commit.
3. Push review independently inspects the exact changed COMP and every referencing wiki/hypothesis surface before propagation or later synthesis.

The reviews answer different questions and cannot substitute for one another. Current push receipts live under each COMP's `reviews/` directory and replace prior receipts. A stable `synthesis/queue/comp-review-NNN.md` exists only while action is required.

## Explicit full synthesis

`wiki-sweep.yml` runs `distributed-synthesis.py`. It preserves grounded creativity without loading one model with an ever-growing prompt:

1. deterministically split the full current corpus into section-addressable shards;
2. perform complete atomic extraction across all shards;
3. perform a second independent complete read focused on residue and missed details;
4. merge atoms without erasing disagreements;
5. examine every unordered domain pair;
6. rehydrate each candidate from exact source spans;
7. for COMP-backed candidates, reopen the exact generated outputs covered by a current receipt;
8. obtain an independent review;
9. emit only reviewed unresolved actions.

The run fails closed unless every section has both reads, every domain pair is examined, and every candidate is rehydrated and reviewed. Cost is tracked from provider usage where available and conservatively estimated otherwise; the workflow enforces an explicit cap.

Raw model output and review files are recovery artifacts with short CI retention. The repository keeps only active queue items and the compact coverage/cost receipt. Git preserves prior runs.

## Current-state content rules

- `wiki/`: current scientific understanding and active track state;
- `synthesis/queue/`: unresolved actions only;
- COMP directories: exact reproducible artifacts plus current reviews;
- `reference/`: immutable external source material;
- Git: all revision and completed-action history.

Do not create completed-item directories, immutable review logs, per-run synthesis narratives, inline changelogs, or “for posterity” copies.

## Failure behavior

- Publication is independent and should still run when knowledge automation fails.
- COMP review failure blocks only affected derived claims.
- Propagation failure leaves its cursor unchanged and records an active failure.
- Full-synthesis failure leaves its cursor unchanged and uploads recovery artifacts.
- The watchdog notifies; it never authorizes or automatically dispatches a full synthesis.

## Primary commands

```bash
python3 scripts/sweep-state.py read
python3 scripts/sweep-state.py pending-propagation-paths
python3 scripts/sweep-state.py pending-synthesis-paths
python3 scripts/comp-review.py --help
python3 scripts/distributed-synthesis.py --help
```
