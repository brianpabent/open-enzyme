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

---

## ✓ Actioned 2026-05-15 (drafted AND implemented)

User direction was to implement, not just draft. Shipped:

**Pilot proposal** drafted as a top-level section in [`scripts/SWEEP-ARCHITECTURE.md`](../../scripts/SWEEP-ARCHITECTURE.md) §"Pilot — Tool-Gap vs. Science-Gap Disagreement Attribution":

- **`[GAP: <tag>]`** annotation emitted by Pass 3 reviewer immediately after the existing `[OVERLAP: <tag>]` annotation, **only on disagreement verdicts** (Partial / Push back / Rejected). Confirmed / Confirmed-prioritize / Augment / Defer get no GAP tag.
- Tag vocabulary: `tool-gap` (right topic, wrong execution) / `science-gap` (right plumbing, wrong biology) / `both` (specify dominant) / `unclear` (interpretive disagreement).
- Pilot framing: 2–3 sweep cycles. Promote/abandon gates encoded:
  - **Promote** if (a) ≥30% clean tool/science attribution (not "unclear"), (b) ≥1 model shows >2× gap-type skew, (c) walkthrough operator reports the tag changed at least one closure action.
  - **Abandon** on cargo-cult tagging, mode collapse (>80% unclear/both), or operational burden.
- BioDesignBench PRIMARY-SOURCE-PENDING gate honored — pilot draws on the *idea*, not the preprint's empirical claims; if PDF verification fails, pilot stands or falls on its own utility.

**Pass 3 prompts wired** (both variants, so the pilot fires whichever model the daemon uses):

- `scripts/sweep-prompt-3-review.md` (Opus variant) — added "Gap tag vocabulary (pilot — 2026-05-15)" section under §"Overlap tag vocabulary"; updated the format-of-each-blockquote spec; updated the strong-push-back example with a `[GAP: tool-gap]` demonstration.
- `scripts/sweep-prompt-3-review-gpt55.md` (GPT-5.5 variant, the active reviewer per the 2026-05-15 sweep history) — added "Decision rule — GAP tag (pilot, 2026-05-15)" section under §"Decision rule — OVERLAP tag"; updated the output format spec; included a worked example.

**Pointer added** at `wiki/bio-ai-tools.md` §BioDesignBench (line 766) so the methodology-upgrade-candidate mention now points to the concrete operational pilot section.

**Pass 4 (DeepSeek peer-reviewer)** has no prompt file yet — the architecture mentions it but the file doesn't exist in `scripts/`. When the Pass 4 prompt lands, the GAP tag instruction needs to be mirrored. Carries forward as a Phase 2 follow-up noted in the SWEEP-ARCHITECTURE pilot section's "Implementation surface" subsection.

**Evaluation cadence:** the next 2–3 daemon sweeps will emit GAP tags. Brian (or Claude on Brian's behalf) reviews the pilot against the promote/abandon gates after sweep 3 lands. The walkthrough that processes those sweep outputs will be the natural evaluation surface.

Pass 3's "pilot, not permanent" framing was honored. Closing.
