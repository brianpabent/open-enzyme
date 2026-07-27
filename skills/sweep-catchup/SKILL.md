---
name: sweep-catchup
description: Catch up bounded cross-page propagation after push-time automation missed eligible wiki changes. Does not run full-corpus synthesis.
---

# Propagation catch-up

Use only after checking `sweep-status`.

1. Read eligible backlog:

```bash
python3 scripts/sweep-state.py pending-propagation-paths
```

2. If changed COMP artifacts lack a clean exact-snapshot push review, run the COMP review workflow for those experiments first. Do not bypass the gate.

3. Dispatch the bounded propagation workflow:

```bash
gh workflow run wiki-propagate.yml
```

4. Watch the run and verify that `last_successful_propagation` advanced. A
   legitimate no-op may still advance the cursor because the reviewed paths
   were fully considered.
5. Re-read `pending-propagation-paths`. When a backlog exceeded the 25-trigger
   bound, the workflow retains the exact deterministic remainder in
   `deferred_paths`. Dispatch and verify another bounded run until the eligible
   backlog reaches zero. Never replace this with silent truncation or a
   full-corpus synthesis.

Full synthesis is a separate, explicit decision. If Brian asks for it, first require zero eligible propagation backlog and clean synthesis eligibility for every referenced COMP, then dispatch `wiki-sweep.yml` with an explicit cost cap.

Never infer a synthesis request from “catch up,” a push, a propagation failure, or a nonempty synthesis backlog.
