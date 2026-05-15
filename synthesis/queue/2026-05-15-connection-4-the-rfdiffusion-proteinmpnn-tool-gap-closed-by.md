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
