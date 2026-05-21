---
type: open-question
sweep_date: 2026-05-20
sweep_sha: 6437cb4
section_index: 3
global_index: 10
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Does the substrate-engineering lit scan's finding — that substrate composition shifts compound PROFILE, not just yield (Luo 2024: 13.5× ganosporelactone B difference between wood-log and substitute-substrate *G. lucidum*; Doar 2025: ~100× erinacine C↔Q ratio shift in *Hericium* even when *eri* transcript doesn't change) — imply that the medicinal-mushroom-extract-sops' SOP-7 protocol matrix needs a "profile-shift" column, not just a "yield-multiplier" column?

3. **Does the substrate-engineering lit scan's finding — that substrate composition shifts compound PROFILE, not just yield (Luo 2024: 13.5× ganosporelactone B difference between wood-log and substitute-substrate *G. lucidum*; Doar 2025: ~100× erinacine C↔Q ratio shift in *Hericium* even when *eri* transcript doesn't change) — imply that the medicinal-mushroom-extract-sops' SOP-7 protocol matrix needs a "profile-shift" column, not just a "yield-multiplier" column?** The current SOP-7 table (`medicinal-mushroom-extract-sops.md` §SOP-7) reports expected magnitude as a single fold-change number (e.g., "3× cordycepin," "+85.96% ganoderic acids"). But if substrate composition shifts the *ratio* of compounds within a class (not just the absolute yield), the SOP needs to document which compounds are *up* and which are *down* under each substrate condition — a single fold-change number is misleading if it hides a profile inversion. The most dramatic example is Doar 2025's *Hericium* finding: ~100× erinacine C↔Q ratio shift with no change in *eri* transcript — a post-transcriptional, substrate-driven compound-profile shift that a yield-only SOP would completely miss. For distributed contributors following SOP-7, a "profile-shift" column (documenting the direction and approximate magnitude of ratio changes for the top 2–4 compounds per species) would prevent the "I increased the yield but accidentally shifted to the wrong compound" failure mode. This is a documentation upgrade, not a new experiment — the primary literature already contains the profile-shift data; the SOP just needs to surface it.

   

---

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The profile-shift column is the right documentation upgrade. `medicinal-mushroom-extract-sops.md` SOP-7 already records some profile-shift language in single cells—e.g., *G. lucidum* wood-log vs substitute substrate lists “2.19× lucidenic acids (profile shift)” and *Hericium* complex vs minimal media lists ~100× erinacine C—but the table lacks a dedicated field that distinguishes yield increase from compound-ratio inversion. Making profile direction explicit prevents a real distributed-cultivation failure mode: increasing total yield while shifting away from the target molecule.
