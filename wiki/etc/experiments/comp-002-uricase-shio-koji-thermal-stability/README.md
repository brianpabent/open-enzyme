> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** The retired model converted unvalidated thermal, pH, salt, and pLDDT/interface assumptions into numerical retention and decision labels. Repair would require a new model rather than a correction. The executable artifact is preserved by Git, not duplicated in the live corpus.

# comp-002 — Uricase Shio-Koji Thermal/pH Stability

**Status:** Invalidated for quantitative and physical-interface interpretation and retired from execution.

No retained-activity value or band, RAG/verdict label, dominant-driver ranking, pLDDT-derived physical-interface conclusion, modeled salt-bridge or pH-integrity conclusion, failure-mode ordering, or intervention priority survives.

## What survives

The useful scope is empirical:

- measure Q00511 specific activity and oligomeric state under the joint shio-koji ranges of temperature, pH, salt, and duration;
- separate thermal, pH, and salt effects with controlled measurements rather than inferred multipliers;
- track ferment pH over time and pair activity-per-total-protein with an orthogonal tetramer-state readout; and
- compare stabilization variants only if measurements identify a limiting failure mode.

The [current evidence and experiment page](../../../uricase-shio-koji-thermal-stability-computational.md) defines the direct measurements. The retired COMP-002 outputs are not evidence for their answers.

## Dependency disposition

No active runtime imports a file from the retired artifact. Exact-path references elsewhere are historical review or operational records; they do not require a legacy input to remain live. All executable, input, generated-output, and old review files were therefore retired.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) records the exact Git tree containing the last live executable artifact, the SHA-256 and byte count of every retired non-review file, the last push-review manifest digest, a canonical digest over the retirement scope, and the current evidence owner.

Historical files can be inspected with Git when needed:

```bash
git show 70e60ea9a7c84a92cec37164f38b456aaa6d6881:wiki/etc/experiments/comp-002-uricase-shio-koji-thermal-stability/analyze.py
```

There is no reproduction command. Old push-review receipts were retired with the executable artifact; `reviews/` contains only current tombstone review material.
