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

---

**WALKED 2026-05-19 — Closed (coding subagent firing to clone ProteinMPNN + rerun comp-034; Pass 3's "install first" framing reflected in the task brief).**

Actioned:
- 🔄 Coding subagent firing in background. Task: (Phase 1) clone ProteinMPNN to `/opt/ProteinMPNN` or writable location, install PyTorch + biopython, smoke-test; (Phase 2) reconstruct comp-034's input PDB + design positions for the inter-lobe linker (aa 353–363), run ProteinMPNN sampling at ~60 sequences, default temperature 0.1; (Phase 3) score candidates against comp-034's 5-metric framework (cleavage, fold quality, codon compatibility, loop flexibility, identity to WT) and compare ranking against the substitute-sampler's 15 GREEN candidates.
- Output → `logs/proteinmpnn-comp-034-rerun-2026-05-19.md` when complete. Brian propagates findings to the comp-034 archive + the bio-ai-tools.md install path documentation manually after review.
- Pass 3's reframing ("install/clone ProteinMPNN, then rerun") is reflected in the subagent task brief — Phase 1 explicitly does the install before any rerun attempt.
- Headline question the subagent will resolve: do the substitute-sampler's 15 GREEN candidates reproduce under genuine ProteinMPNN, or are they substitute-method artifacts? Resolves before any §1.10 wet-lab gene-synthesis commitment (~$1.5–3K for 3 variants).

Worth noting: this is the **first concrete coding-subagent task** in the walkthrough (vs the lit-scan subagents fired earlier for A2, CFH, serpin, J2, J3.2, H2). Engineering subagent tasks may have different failure modes than literature-scan subagents — Mac-specific compilation issues, missing dependencies, PyTorch installation pain are all plausible failure paths. The subagent brief explicitly asks for partial-install reporting if the install fails — so even a stalled-out attempt produces actionable next-step documentation for Brian.
