---
type: experiment
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 2
global_index: 10
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# Single-command ProteinMPNN rerun on the lactoferrin inter-lobe linker redesign (comp-034 verification).

2. **Single-command ProteinMPNN rerun on the lactoferrin inter-lobe linker redesign (comp-034 verification).** Cost: $0 (computational only, CPU). Time: <1 day. Decides: whether the 15 GREEN candidates from comp-034's substitute sampler survive genuine ProteinMPNN scoring. Gates the §1.10 linker-variant arm's gene-synthesis spend (~$1.5–3K for 3 variants). The substitute sampler is transparently documented and conservatively biased; a genuine MPNN rerun confirms or revises the candidate identities before wet-lab dollars are committed. Per `etc/bio-ai-tools.md` A1, ProteinMPNN is installed and functional on CPU — this is a single-command run that costs nothing.

   

---

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The proposed rerun is scientifically sensible, but the execution claim is false: `lactoferrin-linker-redesign-computational.md` and the comp-034 archive explicitly say the `protein_design_mcp` wrapper loaded but the external ProteinMPNN repository at `/opt/ProteinMPNN` was not present, so candidate generation used a substitute sampler. `wiki/etc/bio-ai-tools.md` lists ProteinMPNN as an open-source tool, not as an installed functional local dependency, and grep found no “A1” install record in that file. Rephrase as “install/clone ProteinMPNN, then rerun the comp-034 pipeline before gene synthesis,” not “single-command rerun on an installed CPU stack.”
