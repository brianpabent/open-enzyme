---
type: connection
sweep_date: 2026-05-15
sweep_sha: ebbce26
section_index: 4
global_index: 4
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# The RFdiffusion + ProteinMPNN tool gap closed by BioDesignBench directly enables lactoferrin variant engineering and future protein redesigns.

4. **The RFdiffusion + ProteinMPNN tool gap closed by BioDesignBench directly enables lactoferrin variant engineering and future protein redesigns.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `lactoferrin.md`, `bio-ai-tools.md`, `autonomous-screening-methodology.md`
   - *Page-pair linkage:* The BioDesignBench evaluation (`bio-ai-tools.md` §BioDesignBench) audited OE’s computational tool stack and identified RFdiffusion and ProteinMPNN as absent from the platform, despite being canonical for structure-conditioned sequence redesign. Simultaneously, the lactoferrin dossier (`lactoferrin.md` §12, open question #13) explicitly tags RFdiffusion + ProteinMPNN as needed for future variant design work (lactoferricin constructs, host-optimized glycosylation, apo-form stabilization). This is a **precise match between an identified tool gap and a queued engineering task**, and the protein-design-mcp package (Kim & Romero 2026) makes integration straightforward.
   - *Why It Matters:* Without these tools, lactoferrin optimization for the koji chassis would rely on trial-and-error mutagenesis or limited ESM2 scoring. With them, OE can perform true computational protein redesign — designing disulfide-stabilized or protease-resistant variants tailored to the *A. oryzae* secretory environment — directly addressing the stability concerns flagged in comp-005. This is the first concrete task that justifies deploying the protein-design-mcp server.
   - *Suggested Action:* Deploy the `protein-design-mcp` package locally (already done per `bio-ai-tools.md` §BioDesignBench) and run a pilot redesign of the lactoferrin inter-lobe linker region, targeting improved shio-koji protease resistance. Use comp-030’s multi-metric concordance gate (N-of-3 ≥ 2, combining ESM2, Rosetta, and interface-metrics) to rank candidate sequences before wet-lab testing.
   

---

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The central page-reading claim is wrong: the tool-verified `wiki/etc/bio-ai-tools.md` page already lists **RFdiffusion2** and **ProteinMPNN** under “Open Source Protein AI Tools,” so it does not identify them as absent from OE’s stack. A direct grep of `wiki/etc/*.md` also returned no matches for “BioDesignBench” or “protein-design-mcp,” contradicting the claim that `bio-ai-tools.md §BioDesignBench` closes this tool gap via that package. The lactoferrin page’s open question about RFdiffusion / ProteinMPNN for variant design is real, but Pass 2 mis-plumbed the source and inverted the tool-gap status; rewrite as “existing listed tools should now be applied to the lactoferrin redesign task,” not as “BioDesignBench closed an absent-tool gap.”

---

## ✓ Actioned 2026-05-16

**Pass 3's pushback was empirically wrong** — both "BioDesignBench" and "protein-design-mcp" terms ARE in `wiki/etc/bio-ai-tools.md` (lines 752, 810+ as of this commit), and the §BioDesignBench section + A1 install record were ADDED in the same trigger commit that fired this sweep. Pass 3's grep returned a false-negative because Pass 3 has no trigger-file awareness — it can't distinguish "Pass 2 hallucinated a section" from "Pass 2 saw a brand-new section added in the trigger commit." This is a structural Pass 3 architecture gap, not a content-level disagreement. The synthesizer's framing was substantively correct: BioDesignBench-driven content added in this commit DID identify the tools as a gap AND DID install them (A1, CPU-mode, 2026-05-15), AND the lactoferrin redesign task is the natural first use case.

Three actions shipped + one in-flight:

- [`wiki/lactoferrin.md` §12 #13](../../wiki/lactoferrin.md) — state-reconciliation edit. Updated to reflect post-install reality: ProteinMPNN installed (CPU-mode functional), RFdiffusion pending GPU (A4 task), PyRosetta blocked (UW license), Boltz-2 blocked (torch venv conflict). The CPU-functional ProteinMPNN subset is sufficient for sequence-design-only tasks where the structure is known. The "fires when" dormancy condition relaxed: tool-stack readiness no longer gates additional pilots.
- [`scripts/SWEEP-ARCHITECTURE.md` §"Pass 3 trigger-file awareness gap"](../../scripts/SWEEP-ARCHITECTURE.md) — new architecture section naming the failure mode, using this exact case (2026-05-16 walkthrough Item 5) as the canonical empirical example, proposing the orchestrator + prompt-engineering fix (compute trigger-commit diff, inject as Pass 3 context). Added "Open improvements" subsection tracking the implementation as a follow-up.
- **comp-034 lactoferrin inter-lobe linker redesign pilot** — spawned as a background Opus subagent following the `new-comp-experiment` skill discipline. First concrete use of the newly installed protein-design-mcp tools. Brief includes BioDesignBench multi-metric discipline (≥30 candidates, N-of-5 ≥ 3 concordance gate across ESM2 pLDDT / shio-koji protease cleavage / A. oryzae CAI / linker-loop pLDDT / sequence-similarity-to-WT), verification-agent pass per CLAUDE.md Rule 4, multilingual default (J-STAGE / CiNii for Japanese koji-Lf literature), and explicit non-touch list for the in-flight walkthrough files. Output will be reviewed at walkthrough Item 24 (auto-appended per skill Section 4 background-subagent rule).
- **Queued:** the Pass 3 trigger-aware prompt update (orchestrator script + sweep-prompt-3-review.md + GPT-5.5 variant). Tracked in SWEEP-ARCHITECTURE.md Open Improvements; not action it today.

**Walkthrough side-note (meta).** Brian's question — "would Pass 3 say something different if it knew the file was brand new?" — surfaced the trigger-awareness architecture gap. The gap is structural, not item-specific; once the prompt+orchestrator fix lands, every future sweep gets correct reviews on trigger-content connections. This case is the canonical empirical example for the eventual implementation PR description.
