> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** The retired artifact encoded an unsupported metabolic scenario and then interpreted its solver outputs as biological burden and feasibility.

# comp-023 — *cns1+cns2* Cordycepin-Burden FBA

**Status:** Invalidated for burden, flux, yield, breakpoint, feasibility, compatibility, and roadmap decisions.

No growth-change result, flux value, capacity maximum, native-product headroom, burden breakpoint, GREEN/YELLOW/RED label, “effectively free” conclusion, ATP-substitution mechanism, proteome-gap conclusion, or multi-cassette recommendation survives.

## What survives

Jeennor et al. directly demonstrated heterologous cordycepin production in *A. oryzae* in their tested configuration (PMID 38071331). That primary result does not validate this model.

One unranked research conjecture also survives: if the functional *cns1+cns2* route is cytosolic in the intended configuration, it might avoid direct competition for ER folding with a secreted-protein cassette. The [current evidence page](../../../cordycepin-cassette-burden-computational.md) states the exact isogenic product-and-cell-state experiment required to test that leap. The track is currently deprioritized.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds every retired non-review file to Git commit `70e60ea9a7c84a92cec37164f38b456aaa6d6881` by byte count and SHA-256 and defines the exact invalidated and surviving scopes.

There is no reproduction command. Git retains the retired code, inputs, outputs, and reviews.
