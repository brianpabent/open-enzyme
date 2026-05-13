# Cross-vendor review — claude-on-2

**Model requested:** `anthropic/claude-opus-4.5`
**Model returned:** `anthropic/claude-4.5-opus-20251124`
**Latency:** 43.6s
**Usage:** {'prompt_tokens': 2891, 'completion_tokens': 2421, 'total_tokens': 5312, 'cost': 0.07498, 'is_byok': False, 'prompt_tokens_details': {'cached_tokens': 0, 'cache_write_tokens': 0, 'audio_tokens': 0, 'video_tokens': 0}, 'cost_details': {'upstream_inference_cost': 0.07498, 'upstream_inference_prompt_cost': 0.014455, 'upstream_inference_completions_cost': 0.060525}, 'completion_tokens_details': {'reasoning_tokens': 0, 'image_tokens': 0, 'audio_tokens': 0}}

---

## Cross-Vendor Review of §2 (Related Work)

### Overall Assessment

The section is well-structured and the core argument—that cross-vendor heterogeneity operates at a different abstraction level than existing multi-agent/self-refinement patterns—is coherently presented. However, I have identified several catches requiring attention.

---

### Catch 1 — [§2.5]

**Claim under review:** "Song et al. (2026) introduced PaperOrchestra, an explicitly partial system that automates only the writing layer — five communicating agents (outline, plotting, literature review, section writing, content refinement) converting pre-writing materials into a submission-ready LaTeX manuscript with Semantic-Scholar-verified citations."

**Verdict:** Push-back

**Reasoning:** Song et al. 2026 is a future publication date (the current date appears to be 2025 or earlier based on context). Either this is a typo, a preprint with an incorrect date, or a fabricated citation. The S2-verification claim cannot be accurate for a paper dated in the future. Additionally, this paper was drafted *using* PaperOrchestra, creating a potential conflict-of-interest in how the system is described ("explicitly partial" and the favorable framing of S2-verification as "a partial defense" reads as promotional).

**Suggested correction:** Verify the actual publication date of Song et al. If this is a 2025 preprint, correct the date. Additionally, add a disclosure that this manuscript was drafted using PaperOrchestra, and consider whether the favorable framing ("explicitly partial" as a virtue, highlighting S2-verification as a defense) constitutes PaperOrchestra-favorable bias. A neutral rewrite: "Song et al. (202X) introduced PaperOrchestra, a system that automates manuscript drafting through five communicating agents, with citation verification against Semantic Scholar."

---

### Catch 2 — [§2.5]

**Claim under review:** "each is constructed within a single vendor's model family — Claude or GPT for AI Scientist, Gemini-based for PaperOrchestra"

**Verdict:** Partial

**Reasoning:** Lu et al. (2024) AI Scientist uses Claude (Anthropic) in its primary implementation, but the paper also reports experiments with other models. Describing it as "Claude or GPT" is accurate but potentially misleading—the system architecture doesn't *require* single-vendor construction; the authors simply evaluated it that way. The claim that PaperOrchestra is "Gemini-based" needs verification against the Song et al. source. The broader point (these systems don't architecturally commit to cross-vendor routing) appears valid, but the specific vendor attributions should be verified.

**Suggested correction:** Soften to: "each has been primarily demonstrated within a single vendor's model family in published evaluations" or verify the specific vendor claims against the source papers.

---

### Catch 3 — [§2.4]

**Claim under review:** The entire §2.4 on Constitutional AI and RLAIF (Bai et al. 2022, Lee et al. 2023).

**Verdict:** Push-back (Drafter-Vendor-Favorable Framing)

**Reasoning:** Constitutional AI (Bai et al. 2022) and RLAIF (Lee et al. 2023) are both Anthropic papers. This section cites two Anthropic papers as a dedicated methodology cluster, while no comparable cluster exists for OpenAI's or Google's alignment research (e.g., InstructGPT, RLHF from OpenAI is not cited; Google's alignment work is absent). The distinction drawn ("training time vs. synthesis time") is valid, but the selection of *which* training-time alignment work to discuss appears Anthropic-skewed. The drafter is an Anthropic model; this is exactly the pattern the review was asked to flag.

**Suggested correction:** Either (a) broaden §2.4 to include non-Anthropic alignment work (e.g., Ouyang et al. 2022 for InstructGPT/RLHF from OpenAI) to make the cluster representative rather than Anthropic-specific, or (b) justify why Constitutional AI/RLAIF specifically are the relevant antecedents (if there's a principled reason), or (c) reduce the prominence of this cluster if it's not actually central to the paper's contribution.

---

### Catch 4 — [§2.1]

**Claim under review:** "Du et al. (2023) introduced multi-agent debate as a mechanism for improving the factuality and reasoning of language-model outputs: multiple instances of the same model propose and critique one another's answers"

**Verdict:** Partial

**Reasoning:** Du et al. (2023) "Improving Factuality and Reasoning in Language Models through Multiagent Debate" does use multiple instances, but the paper also explores heterogeneous model configurations (e.g., mixing ChatGPT and Bard in some experiments). The claim that multi-agent debate is definitionally "same model" slightly misrepresents the original work to sharpen the contrast with this paper's contribution. The core point (debate operates at inference-time argumentation, not training-distribution heterogeneity) remains valid, but the "same model" framing is too strong.

**Suggested correction:** Revise to: "multiple instances — often of the same model, though Du et al. also explored mixed-model configurations — propose and critique one another's answers across several rounds." Then adjust the subsequent paragraph to acknowledge that Du et al. touched on model heterogeneity but did not frame it as a vendor-level architectural commitment for corpus-level synthesis.

---

### Catch 5 — [§2.3]

**Claim under review:** "The distinction this paper draws is in the *abstraction level of application*. The jury pattern operates on per-output evaluation: each query gets an independent panel review, and there is no temporal accumulation of bias across queries to guard against."

**Verdict:** Confirmed (but flag for transparency)

**Reasoning:** The framing is accurate and the distinction is credible. PoLL is indeed cross-vendor, and the paper correctly acknowledges this ("the closest antecedent in the existing literature"). The relocation of the novelty claim to "abstraction level of application" (per-output evaluation vs. corpus-level synthesis over time) is a legitimate distinction. However, the section should be commended for *not* obscuring PoLL's cross-vendor nature—this is an honest handling of a close antecedent.

**Suggested correction:** None required. The handling is appropriate.

---

### Catch 6 — [§2.6]

**Claim under review:** "model collapse as studied by Shumailov et al. (2024) and Shumailov et al. (2023)"

**Verdict:** Partial

**Reasoning:** The Shumailov et al. model collapse work is typically cited as a 2023 arXiv preprint and a 2024 Nature publication (same core team, same line of work). Citing both years as separate works is technically accurate if referring to the preprint and the journal version, but this should be clarified. The description of model collapse itself appears accurate.

**Suggested correction:** Clarify whether these are two distinct papers or the preprint and published versions of the same work. If the latter, cite as "Shumailov et al. (2023; 2024)" or similar to indicate the relationship.

---

### Catch 7 — [§2.5]

**Claim under review:** "A parallel system, FARS (Fully Automated Research System), deployed publicly for 228 hours in March 2026 and produced 100 short machine-learning papers, optimizing for throughput rather than per-paper rigor."

**Verdict:** Push-back

**Reasoning:** March 2026 is in the future. This citation cannot be S2-verified as claimed in the header. Either the date is wrong, or this is a fabricated or hallucinated reference. The specific details (228 hours, 100 papers) require verification.

**Suggested correction:** Verify the actual date and source for FARS. If this is a 2025 system, correct the date. If the reference cannot be verified, drop the claim or mark it as requiring additional evidence.

---

### Catch 8 — [§2, introduction]

**Claim under review:** "The pattern this paper develops — heterogeneity at the level of training-distribution prior, achieved by routing successive synthesis passes through different vendors' frontier models — is, to our knowledge, the first explicit treatment of the cross-vendor regime as an architectural commitment for AI-assisted scientific literature synthesis."

**Verdict:** Confirmed (appropriately scoped)

**Reasoning:** The novelty claim is appropriately hedged ("to our knowledge") and specifically scoped ("for AI-assisted scientific literature synthesis"). It does not claim to be the first cross-vendor ensemble (PoLL is acknowledged), only the first to apply this as an architectural commitment for the specific use case of corpus-level scientific synthesis. This is an acceptable novelty claim.

**Suggested correction:** None required.

---

## Summary

| Catch | Section | Verdict | Severity |
|-------|---------|---------|----------|
| 1 | §2.5 | Push-back | High (future date, PaperOrchestra-favorable) |
| 2 | §2.5 | Partial | Medium (verify vendor claims) |
| 3 | §2.4 | Push-back | Medium (Anthropic-favorable citation selection) |
| 4 | §2.1 | Partial | Low (slight misrepresentation of Du et al.) |
| 5 | §2.3 | Confirmed | N/A (clean) |
| 6 | §2.6 | Partial | Low (clarify citation relationship) |
| 7 | §2.5 | Push-back | High (future date) |
| 8 | §2 intro | Confirmed | N/A (appropriately scoped) |

**Priority issues:** Catches 1, 3, and 7 require immediate attention before submission. The future dates (2026) are either errors or fabrications and must be resolved. The Anthropic-skewed citation selection in §2.4 should be addressed to avoid the appearance of drafter-vendor bias.
