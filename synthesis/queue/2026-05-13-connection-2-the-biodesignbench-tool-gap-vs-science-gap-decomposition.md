---
type: connection
sweep_date: 2026-05-13
sweep_sha: 69103ce
section_index: 2
global_index: 2
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# The BioDesignBench tool-gap vs. science-gap decomposition provides a diagnostic framework that could make the sweep daemon’s multi-model disagreement resolution actionable rather than merely adjudicatory.

2. **The BioDesignBench tool-gap vs. science-gap decomposition provides a diagnostic framework that could make the sweep daemon’s multi-model disagreement resolution actionable rather than merely adjudicatory.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: partial]`
   - *Documents Connected:* `wiki/bio-ai-tools.md`, `wiki/open-source-platform.md`, `wiki/autonomous-screening-methodology.md`
   - *Page-pair linkage:* `bio-ai-tools.md` already cross-references `open-source-platform.md` via the multi-model synthesis section, but the specific tool-gap/science-gap decomposition is not yet applied to the sweep daemon’s Pass 3/Pass 4 disagreement resolution.
   - *Why It Matters:* The sweep daemon currently uses four models from three vendors (Sonnet propagate → Gemini synthesize → Opus critique → DeepSeek peer-review) as a guard against epistemic homogenization. When models disagree, Pass 3 emits a fixed-verdict tag but does not attribute the disagreement to mechanism. BioDesignBench’s decomposition — *tool gap* (correct plan, failed execution) vs. *science gap* (wrong plan, didn’t understand the biology) — would let the daemon say: “Opus and DeepSeek disagree on this connection; Opus appears to have a science gap (misinterpreting the mechanism), DeepSeek a tool gap (correct mechanism but wrong magnitude).” This converts disagreement from a binary “reviewer disagrees” signal into a **diagnostic** that tells the human *where to look*. It also provides a calibration surface: if one model consistently shows science-gap failures on complement biology, that’s a known weakness to route around.
   - *Suggested Action:* Draft a `sweep-architecture.md` extension (or a subsection of `open-source-platform.md`) that defines tool-gap and science-gap categories for Pass 3/Pass 4, with examples from past sweeps. Pilot on the next 2–3 sweep cycles before committing to a permanent pass.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` The diagnostic idea is valid, but the evidence gate matters: `bio-ai-tools.md` marks BioDesignBench as **PRIMARY-SOURCE-PENDING** and explicitly says not to cite it from `open-source-platform.md` as architectural validation until the PDF is verified. `open-source-platform.md` already names the tool-gap vs. science-gap decomposition as a Pass 3/4 methodological-upgrade candidate, so the new value here is the concrete proposal to turn disagreement tags into routed diagnostic examples; keep it as a pilot proposal, not a permanent architecture change yet.
