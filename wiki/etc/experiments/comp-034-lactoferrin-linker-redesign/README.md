> **INVALIDATED TOMBSTONE — NOT RUNNABLE.** The retired model used an unverified legacy protease-preference table as a biological cleavage axis, then combined that axis with uncalibrated sequence, structure, and language-model scores to rank linker variants. Later ProteinMPNN and Rosetta calculations did not validate the biological target. Git retains the historical artifact.

# comp-034 — Lactoferrin Inter-Lobe Linker Redesign

**Status:** Invalidated for cleavage, protease-resistance, candidate-ranking, and wet-lab-selection use.

No cleavage count, cleavage-score reduction, GREEN/STRICT tier, cross-model concordance claim, “winner,” or preferred linker variant survives. The calculations do not establish that the native linker is a cleavage site or that any proposed sequence improves process survival.

## What survives

The exact inter-lobe connector remains an engineerable region if direct experiments identify a reproducible linker-associated failure. A new design lifecycle would need:

- an observed WT fragment or retained-function failure under the intended process;
- verified specificity inputs or a learned model validated against matched cleavage data;
- explicit structural and functional constraints; and
- a prespecified diversity panel tested without treating proxy rank as biological evidence.

No historical candidate inherits priority, panel membership, or any other design status from the retired artifact.

The current evidence boundary and direct-test conjecture are on the [lactoferrin linker page](../../../lactoferrin-linker-redesign-computational.md). Section [§1.10](../../../validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment) first tests WT integrity, fragment formation, and retained function.

## Hash-bound retirement record

[`invalidation.json`](./invalidation.json) binds the last live Git tree, every retired non-review file, the prior push-review manifest, the invalidated scope, and the narrow surviving research question.

There is no reproduction command. Historical files can be inspected with Git when needed.
