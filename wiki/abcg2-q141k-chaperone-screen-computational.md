---
title: "ABCG2 Q141K Pharmacological-Chaperone Screen (comp-032)"
date: 2026-05-16
updated: 2026-07-16
tags: [computational, abcg2, q141k, superseded]
related:
  - ./abcg2-q141k-chaperone-rescreen-computational.md
---

# ABCG2 Q141K Pharmacological-Chaperone Screen (comp-032)

**Current status: superseded; do not use its ranking.** The comp-032 heuristic embedded drug-class priors in its score, making its apparent separation of the CFTR cross-protein comparators tautological. It did not establish chaperone binding or rescue.

The current result is [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md): the static docking configuration is **inconclusive**. Rosuvastatin is excluded by ABCG2 evidence; vorinostat is the sole marginal executable row but is not a docking-backed priority. The CFTR comparators do not validate sensitivity for ABCG2 chaperones. The earlier candidate set remains an unranked hypothesis inventory and must not guide a compound or compounding decision.

The reproducible comp-032 artifact remains under `wiki/etc/experiments/`; Git preserves the former interpretation.
