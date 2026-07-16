# comp-031 — Invalidated dual-chassis prior

**Status: INVALIDATED. No result or engineering recommendation survives.**

comp-031 attempted to predict whether PDB-EcN plus luminal uricase would produce additive serum-urate reduction and whether a PDB-derived butyrate axis would rescue ABCG2/Q141K. The model cannot answer those questions because it:

1. inherited comp-019's invalid uricase saturation regime;
2. transferred a *C. sporogenes* butyrate assumption into CBT2.0/EcN without product measurement;
3. misattributed direct butyrate rescue to Basseville 2012;
4. used unmatched background butyrate; and
5. treated spatially distinct oxidative and anaerobic processes as well-mixed competitors.

The former YELLOW verdict, all ΔSUA values, substrate-competition result, butyrate and Q141K effects, and separate-strain recommendation are retracted. Separate strains, one strain, and temporal staging remain unranked experimental options.

The obsolete executable model, parameter file, and raw outputs have been removed from the live tree. Git preserves the exact historical run. Do not rerun or patch that model. Any renewed analysis must be a new COMP using physiologic UOX kinetics, measured CBT2.0 carbon fate, matched comparators, explicit compartments and staging, and independently validated serum-urate mapping.

Current replacements:

- [comp-044](../../../gut-lumen-uricase-physiologic-regime-computational.md) reopens the UOX regime.
- [comp-046](../../../staged-purine-sink-mass-balance-computational.md) conserves dietary fate, treats the endogenous side as a capture-fraction comparison, and defines conditional architecture boundaries.
- [Validation §1.34](../../../validation-experiments.md#134-isotope-resolved-dietary-precursor--uox--pdb-sequential-flux) tests sequential flux.
- [Validation §1.37](../../../validation-experiments.md#137-cbt20-carbon-fate-and-pdb-self-niche-test) measures CBT2.0 carbon fate.

See the [canonical interpretive page](../../../dual-chassis-ecn-pdb-uricase-computational.md).
