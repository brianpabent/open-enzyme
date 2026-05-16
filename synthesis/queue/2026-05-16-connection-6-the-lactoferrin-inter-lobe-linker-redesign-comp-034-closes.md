---
type: connection
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 6
global_index: 6
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# The Lactoferrin inter-lobe linker redesign (comp-034) closes the loop between computational protease-stability prediction (comp-005) and protein-design intervention for the shio-koji production gate — the first concrete use of the protein-design-mcp tool stack on a load-bearing OE engineering problem.

6. **The Lactoferrin inter-lobe linker redesign (comp-034) closes the loop between computational protease-stability prediction (comp-005) and protein-design intervention for the shio-koji production gate — the first concrete use of the protein-design-mcp tool stack on a load-bearing OE engineering problem.** *Supported*. `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `lactoferrin-linker-redesign-computational.md`, `lactoferrin-protease-stability-computational.md`, `lactoferrin.md`, `validation-experiments.md`, `etc/bio-ai-tools.md`

   - *Page-pair linkage:* **Weak.** comp-034 is brand new (2026-05-16) and has no existing cross-references from `lactoferrin.md` or `lactoferrin-protease-stability-computational.md`. The connection between the computational protease-stability analysis (comp-005, which identified the inter-lobe linker as the most plausible secondary vulnerability) and the computational redesign (comp-034, which produced 15 GREEN candidates reducing predicted cleavage by 24–43%) has not been named in the corpus.

   - *Why It Matters:* comp-005 (lactoferrin shio-koji protease stability) flagged the inter-lobe linker as the most plausible secondary vulnerability in the mature protein — a high-pLDDT structured α-helix (AF mean 95.6) with 16 predicted cleavage sites across the three koji proteases. comp-034 took that finding and ran a systematic redesign: 60 candidate linker sequences generated via a structure-conditioned biased sampler (substituting for ProteinMPNN, which wasn't installed), scored against 5 orthogonal metrics (cleavage, fold quality, codon compatibility, loop flexibility, ESM2 pLDDT). 15 of 60 pass N-of-5 ≥ 3; zero pass strict 5-of-5. The primary wet-lab candidate (S353E + V357P, 82% WT identity) reduces predicted cleavage by ~29%.

     This is the first time the OE corpus has taken a computational prediction of a specific protease vulnerability and produced a concrete, ranked set of redesign candidates targeting that vulnerability for wet-lab testing. The loop is: **comp-005 identifies the problem → comp-034 designs solutions → §1.10 linker-variant arm tests them**. The pattern is generalizable to any future shio-koji protease-vulnerability finding (DAF SCR1-4 exposed loops, future peptide payloads, etc.).

     The comp-034 caveat about the substitute sampler (ProteinMPNN not installed at run time) is important but not blocking: a single-command genuine ProteinMPNN rerun costs ~$0 and would confirm or revise the candidate identities before gene-synthesis spend. The protein-design-mcp tool stack is installed and functional on CPU for sequence-design tasks per `etc/bio-ai-tools.md` A1.

   - *Suggested Action:* (1) Run the single-command genuine ProteinMPNN rerun on the linker redesign before committing gene-synthesis dollars to the §1.10 linker-variant arm. (2) Document the comp-005 → comp-034 → §1.10 loop as a worked example of the computational-prediction-to-wet-lab-design pipeline in `lactoferrin.md` §12 (Open Research Questions, item 13 — the tool-stack integration question). (3) The pattern is generalizable — consider naming it as a "protease-vulnerability-to-redesign" workflow in `etc/bio-ai-tools.md` for future cassettes.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The comp-005 → comp-034 → §1.10 design loop is real: comp-005 flags mature lactoferrin as MODERATE risk and identifies linker/signal-peptide vulnerability, while comp-034 produces 15/60 GREEN linker candidates and recommends WT + conservative + aggressive wet-lab arms. The synthesis misstates the cleavage-improvement range: comp-034’s archive shows WT itself is GREEN, the conservative `EEEEPAARRAR` drops cleavage 0.407→0.290 (~29%), the single V357P drops ~24%, and aggressive candidates such as `DEEDPANPQAH` / `EEEQPQEQRHR` drop much more than 43% relative to WT. The strategic workflow is valid, but the candidate-performance summary needs correction and the ProteinMPNN-substitution caveat must stay prominent.
