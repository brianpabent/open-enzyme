---
type: maintenance
scope: comp-044-terminal-ileum-label
priority: last
---

# Correct COMP-044's compartment label

## Why action remains open

COMP-044's reviewed runnable artifact labels the 0.59 µM Miyazaki input as jejunal. The source measurement is from terminal-ileal fluid in a balloon-enteroscopy cohort and is not a healthy-population baseline. Current reader-facing pages have been corrected, but the historical COMP's inputs, code-facing keys, and generated outputs remain active and cannot be edited outside a new exact COMP lifecycle.

## Required action

Run a bounded COMP-044 Gate 1 → deterministic regeneration → Gate 2 correction that:

1. replaces jejunal labels with terminal-ileal clinical-cohort wording without changing the numeric input or upgrading its physiological scope;
2. updates every current COMP-044 input, code-facing identifier, generated output, and active interpretation that depends on the label;
3. preserves prior review receipts as immutable historical records; and
4. verifies that no active `0.59 µM` jejunal or healthy-baseline wording remains outside historical receipts.

Delete this queue file in the same commit after the corrected lifecycle passes.
