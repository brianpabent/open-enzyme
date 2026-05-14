---
prompt_id: 07-self-demonstrating-review
task_type: adversarial-review
provenance: adapted from papers/cross-vendor-heterogeneity-guard/review-prompts.md (Prompt 1, DeepSeek V4-Pro role)
target_output_tokens: 800
notes: |
  Cross-vendor review prompt taken near-directly from the paper's own
  methodology. Tests whether different vendors catch the same things
  or different things when given the same review task. THIS IS THE
  PROMPT TYPE THE PAPER'S CLAIM RESTS ON.
---

# Prompt

You are running an independent cross-vendor review of a passage from a draft scientific paper titled "Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis." The primary drafter was Anthropic Claude Opus 4.7. The paper's central methodology — which this review is part of — is that any draft authored by one vendor's model must be independently reviewed by a different vendor's model so that vendor-specific blind spots are surfaced.

Your role: review the passage below and emit catches in the format specified.

What to check:

1. PRIOR-DISTRIBUTION CLAIMS. The passage asserts that cross-vendor heterogeneity provides prior-distribution diversity that within-vendor heterogeneity does not. Stress-test this claim. Where is the argument weakest? Where would a skeptical ML reviewer push back? What evidence is missing or could be sharpened?

2. ANTHROPIC-FAVORABLE FRAMING. The primary drafter is an Anthropic model. Watch for over-claiming Anthropic's role, under-citing competing vendors, or framing that subtly elevates Claude's contribution to the daemon at the expense of DeepSeek's contribution. Flag any sentence where the framing skews toward the drafter's vendor.

3. ANY CLAIM THAT FEELS TOO CONFIDENT. The paper is a methodology argument with N=1 operational deployment. Flag any sentence that overstates what an N=1 case study can demonstrate.

Output format — one numbered entry per catch:

```
### Catch N

Claim under review: [paste the specific sentence or passage]

Verdict: [Confirmed / Partial / Push-back / Rejected]

Reasoning: [1-3 sentences explaining the catch]

Suggested correction: [proposed rewrite, or "drop the claim," or "needs additional evidence: <what>"]
```

If the passage is clean and you have no catches, say so explicitly rather than producing low-confidence findings to fill the format. False positives are worse than missed catches for this review pass.

---

## Passage under review

> A blind spot in one vendor's training pipeline is less likely to appear in the same form in another vendor's, though correlated blind spots from shared upstream data exist and are discussed as a limitation in §7. The cross-vendor pattern exploits the partial independence that does exist, in the same way classical ensemble methods exploit cross-architecture independence, but at a vendor abstraction level that the existing multi-agent literature has not explicitly developed. We frame the contribution as a methodology case study with N=1 operational deployment and qualitative catches; controlled ablations comparing cross-vendor against alternative review architectures remain future work. The manuscript is drafted using its own methodology; a logged self-catch during drafting is preserved as the cleanest available reflexive evidence that the guard applies to its own production.
