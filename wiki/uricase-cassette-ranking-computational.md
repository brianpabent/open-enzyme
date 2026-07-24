---
title: "Retired Uricase Cassette Ranking (Computational, comp-022)"
date: 2026-05-14
tags:
  - computational
  - comp-022
  - cassette-design
  - uricase
  - aspergillus-oryzae
  - invalidated
related:
  - computational-experiments.md
  - koji-construct-design.md
  - validation-experiments.md
  - etc/autonomous-screening-methodology.md
sources:
  - "UniProt Q00511; reviewed Aspergillus flavus urate oxidase sequence"
status: invalidated; non-runnable
---

# Retired Uricase Cassette Ranking (Computational, comp-022)

An active UOX cassette must produce correctly processed, localized, folded, and
functional enzyme in the intended compartment. COMP-022 did not establish
which *A. oryzae* configuration can do that.

## Evidence boundary

COMP-022 is invalidated and non-runnable. Its CAI, RNA-structure,
chaperone-load, promoter–signal-peptide, and ESM2 axes were not calibrated to
one named biological outcome. No score, rank, shortlist, N-of-M tier, winner,
component preference, gene-synthesis refinement, expression claim, processing
claim, fold claim, secretion claim, activity claim, or safety inference
survives.

The historical program enumerated a declared **6 promoters × 12 signal
peptides × 10 codon variants × 60 scaffold labels = 43,200 rows**. That is an
inventory fact, not a validated parts universe or ranked build list.

## Corrections to the historical record

- All four v1 top-cluster rows entered the retired v2 N-of-five ≥4 artifact
  tier; only one of the four entered N-of-five =5. The strict tier contained
  both PTS1-blocked and unblocked routes, so it did not confirm PTS1 masking.
- The historical file named `esmfold_pLDDT.csv` contains single-pass ESM2 log
  probabilities rescaled to 50–90. It is not ESMFold pLDDT or a fold-quality
  measurement.
- The reviewed [UniProt Q00511](https://www.uniprot.org/uniprotkb/Q00511/entry)
  sequence contains `NFS` at residues 191–193, not the historical `NSS`
  annotation, and terminates in `SKL`. N191Q would disrupt the N-X-S sequon,
  but COMP-022 established neither glycan occupancy nor a mutation preference.

These are corrections to an invalidated artifact, not rescued ranking results.

## What remains worth testing

Direct secretion and GlaA-KEX2 processing remain distinct, unranked
configurations. Promoter, signal peptide, codon design, terminal handling,
propeptide, and glycosylation choices remain possible experimental factors;
COMP-022 selects none of them.

Use matched exact constructs to measure transcript, processing and termini,
localization, native or oligomeric state, fraction-specific intact active UOX,
oxygen and peroxide behavior, host viability, and process retention. The
[construct-design page](./koji-construct-design.md) owns that matrix;
[validation §1.5](./validation-experiments.md#15-koji-uricase-expression-and-activity)
owns cassette characterization, and
[§1.33](./validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial)
owns the physiological UOX gate.

No successor ranking COMP is warranted until an exact cassette choice will
drive near-term gene-synthesis spending.

**Artifact:** [invalidated, non-runnable tombstone](./etc/experiments/comp-022-clockbase-uricase-cassette-ranking/)
· [computational experiment registry](./computational-experiments.md)
