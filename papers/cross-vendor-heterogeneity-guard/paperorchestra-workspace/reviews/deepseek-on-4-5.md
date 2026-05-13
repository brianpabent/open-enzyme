# Cross-vendor review — deepseek-on-4-5

**Model requested:** `deepseek/deepseek-v4-pro`
**Model returned:** `deepseek/deepseek-v4-pro-20260423`
**Latency:** 90.0s
**Usage:** {'prompt_tokens': 3666, 'completion_tokens': 6972, 'total_tokens': 10638, 'cost': 0.03031146, 'is_byok': False, 'prompt_tokens_details': {'cached_tokens': 0, 'cache_write_tokens': 0, 'audio_tokens': 0, 'video_tokens': 0}, 'cost_details': {'upstream_inference_cost': 0.03031146, 'upstream_inference_prompt_cost': 0.0060489, 'upstream_inference_completions_cost': 0.02426256}, 'completion_tokens_details': {'reasoning_tokens': 5872, 'image_tokens': 0, 'audio_tokens': 0}}

---

### Catch 1 — §4 (Why cross-vendor specifically)

**Claim under review:** “Running GPT-4o and GPT-4 in alternation does not guard against OpenAI-specific blind spots; both share the same training-distribution prior, the same alignment procedure, the same characteristic failure modes.”

**Verdict:** Push-back

**Reasoning:** The assertion that within-vendor models share *the same* training-distribution prior, alignment procedure, and failure modes is too strong. GPT-4 and GPT-4o differ in architecture, training data cut-off, and post-training; they can exhibit meaningfully different biases and failure profiles. A skeptical ML reviewer would ask for evidence that within-vendor diversity is negligible compared to cross-vendor diversity.

**Suggested correction:** Soften to “may share substantial overlap in training-distribution prior and alignment objectives, reducing the diversity relative to cross-vendor pairings” and acknowledge that within-vendor diversity is not zero.

---

### Catch 2 — §4 (Why cross-vendor specifically)

**Claim under review:** “Cross-*vendor* heterogeneity … is the level at which prior-distribution diversity actually appears.”

**Verdict:** Push-back

**Reasoning:** This is an absolute claim that prior-distribution diversity does not appear at any finer granularity. Within-vendor model families can exhibit non-trivial prior differences (e.g., different data mixtures, different fine-tuning). The paper provides no empirical comparison of within- vs. cross-vendor prior divergence, so the claim overstates the evidence.

**Suggested correction:** Replace with “is a level at which substantial prior-distribution diversity appears” or “is the most reliable level at which to obtain prior-distribution diversity in current practice.”

---

### Catch 3 — §4 (Why cross-vendor specifically)

**Claim under review:** “A blind spot in one vendor's training pipeline is unlikely to appear in the same form in another vendor's pipeline.”

**Verdict:** Push-back

**Reasoning:** Vendors often train on overlapping corpora (e.g., Common Crawl, Wikipedia) and use similar alignment techniques (RLHF, constitutional AI variants). Blind spots can correlate across vendors. The claim of unlikeliness is an untested independence assumption; the paper’s own N=1 deployment cannot establish it.

**Suggested correction:** “A blind spot in one vendor’s training pipeline may not appear in the same form in another vendor’s pipeline” or “is less likely to appear in identical form.”

---

### Catch 4 — §5.3 (External-tool reliability test)

**Claim under review:** “for the Najjari 2022 PASylated uricase paper (PMC9773812), the true Km is 52.61 µM; Paperclip's `map` returned 0.007 mM — off by approximately 7,500-fold.”

**Verdict:** Rejected (factual error)

**Reasoning:** 52.61 µM = 0.05261 mM. The returned value 0.007 mM is lower by a factor of ~7.5, not 7,500. The claimed 7,500-fold discrepancy is off by three orders of magnitude and appears to be a unit-conversion or arithmetic mistake.

**Suggested correction:** Recalculate the fold-error correctly (≈7.5-fold) and update the text. If the true Km was 52.61 mM rather than µM, clarify the unit and adjust the comparison accordingly.

---

### Catch 5 — §4 (The self-demonstrating moment, closing paragraph)

**Claim under review:** “The architecture's own motivation came from the architecture working.”

**Verdict:** Partial (overstated)

**Reasoning:** At the time of DeepSeek’s Connection 7, the cross-vendor daemon architecture did not yet exist; the observation came from a one-off peer-review pass. The phrasing implies the architecture was already operational and validated itself, which overstates the historical sequence.

**Suggested correction:** “The principle that later motivated the architecture was demonstrated by the cross-vendor review that inspired it.” or “The architecture’s motivation came from a cross-vendor review that prefigured the architecture’s core logic.”

---

### Catch 6 — §5.4 (Cross-vendor catches methodological risk)

**Claim under review:** “It is also the class that justifies the cost of the cross-vendor pass: cheaper architectures cannot catch it.”

**Verdict:** Push-back

**Reasoning:** The paper reports a single operational deployment (N=1). The claim that *no* cheaper architecture (e.g., within-vendor multi-model, human review, prompt-diversification) can catch methodological risks invisible to the dominant vendor is an absolute statement unsupported by the evidence. A skeptical reviewer would demand comparative ablation.

**Suggested correction:** “It is also the class that justifies the cost of the cross-vendor pass: cheaper architectures are less likely to catch it, and within-vendor review may systematically miss it.”

---

**No catches on Anthropic-favorable framing in §4–5.** The text credits DeepSeek explicitly for the motivating observation and does not under-cite competing vendors or over-claim Anthropic’s role.
