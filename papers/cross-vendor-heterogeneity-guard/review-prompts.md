# Cross-vendor review prompts

Ready-to-fire prompts for the independent cross-vendor review passes required by the paper's own methodology. Each prompt is self-contained, paste the relevant section of the draft into the indicated placeholder and fire.

The reviewers should produce findings in the `revisions.md` format: numbered catches, each with (a) the specific claim or sentence under review, (b) the verdict (*Confirmed* / *Partial* / *Push-back* / *Rejected*), (c) the reasoning, (d) the suggested correction if applicable. Catches land in the manuscript's `revisions.md` under "Session 3, cross-vendor review."

---

## Prompt 1, DeepSeek V4-Pro on §4 + §5 (heterogeneity argument + case-study factual claims)

```
You are running an independent cross-vendor review of a draft scientific paper titled
"Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted
scientific literature synthesis." You are DeepSeek V4-Pro. The primary drafter was
Anthropic Claude Opus 4.7. The paper's central methodology — which this review is part
of — is that any draft authored by one vendor's model must be independently reviewed
by a different vendor's model so that vendor-specific blind spots are surfaced.

Your role: review §4 (the heterogeneity-guard rationale) and §5 (four case-study
vignettes), and emit catches in the format below.

Sections under review are pasted at the bottom of this prompt. Primary sources are
all in the Open Enzyme GitHub repo (brianpabent/open-enzyme); read them via the
references in the draft to spot-check.

What to check:

1. PRIOR-DISTRIBUTION CLAIMS. §4 asserts that cross-vendor heterogeneity provides
   prior-distribution diversity that within-vendor heterogeneity does not. Stress-test
   this claim. Where is the argument weakest? Where would a skeptical ML reviewer
   push back? What evidence is missing or could be sharpened?

2. ANTHROPIC-FAVORABLE FRAMING. The primary drafter is an Anthropic model. Watch
   for over-claiming Anthropic's role, under-citing competing vendors, or framing
   that subtly elevates Claude's contribution to the daemon at the expense of
   DeepSeek's contribution. Flag any sentence where the framing skews toward the
   drafter's vendor.

3. FACTUAL CLAIMS IN §5. Each case study makes specific factual claims about an
   operational incident — dates, model versions, numerical magnitudes, primary
   source references. Cross-check against the primary sources cited in the draft.
   Flag any claim that does not survive primary-source verification.

4. THE HOMOGENIZATION DEFINITION. §4 defines epistemic homogenization as distinct
   from per-output hallucination. Is the definition tight? Are there counterexamples
   that would weaken it? Does it survive translation to non-AI contexts (e.g., human
   research groups dominated by a single intellectual school)?

5. THE SELF-DEMONSTRATING MOMENT (§4 closing paragraph, §5.4). This is the paper's
   strongest single argument. Is it presented as strongly as the evidence supports?
   Is it over-claimed? Look at the original peer-review log (logs/v4-peer-review-
   2026-04-25-deepseek.md) — does Connection 7 say what the draft claims it says?

6. ANY CLAIM THAT FEELS TOO CONFIDENT. The paper is a methodology argument with
   N=1 operational deployment. Flag any sentence that overstates what the operational
   record demonstrates.

Output format — one numbered entry per catch:

```
### Catch N, [section §X.Y]

**Claim under review:** [paste the specific sentence or passage]

**Verdict:** [Confirmed / Partial / Push-back / Rejected]

**Reasoning:** [1-3 sentences explaining the catch]

**Suggested correction:** [proposed rewrite, or "drop the claim," or "needs additional
evidence: <what>"]
```

If the section is clean and you have no catches, say so explicitly — "No catches on
§X.Y" — rather than producing low-confidence findings to fill the format. False
positives are worse than missed catches for this review pass.

---

[PASTE §4 AND §5 HERE]
```

---

## Prompt 2, Google Gemini 2.5 Pro on §3 + §6 + §7 (architecture + operational data + limitations)

```
You are running an independent cross-vendor review of a draft scientific paper titled
"Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted
scientific literature synthesis." You are Google Gemini 2.5 Pro. The primary drafter
was Anthropic Claude Opus 4.7. The paper's central methodology — which this review
is part of — is that any draft authored by one vendor's model must be independently
reviewed by a different vendor's model so that vendor-specific blind spots are
surfaced.

Your role: review §3 (architecture), §6 (operational data), and §7 (limitations and
failure modes), and emit catches in the format below.

Sections under review are pasted at the bottom of this prompt. Primary sources are
all in the Open Enzyme GitHub repo (brianpabent/open-enzyme); read them via the
references in the draft to spot-check.

What to check:

1. ARCHITECTURAL ACCURACY. §3 describes the daemon as three operational passes plus
   an episodic peer-review pattern. Cross-check against the actual files:
   scripts/sweep-prompt-1-propagate.md, scripts/sweep-prompt-2-synthesize.md,
   scripts/sweep-prompt-3-review.md, .github/workflows/wiki-sweep.yml,
   scripts/SWEEP-ARCHITECTURE.md. Flag any architectural claim that does not match
   the actual code.

2. MODEL ASSIGNMENT CLAIMS. §3 names specific models for each pass (Sonnet 4.6,
   DeepSeek V4-Pro primary with Gemini 2.5 Pro fallback, Opus 4.7 or GPT-5.5). Verify
   these against the actual prompts and workflow YAML. Flag mismatches.

3. OPERATIONAL DATA. §6 cites specific cost and latency numbers (Pass 2 $0.7288 on
   2026-04-28; DeepSeek peer-review $0.2070 on 2026-04-25). Verify against
   scripts/SWEEP-ARCHITECTURE.md (Pass 2 cost) and logs/v4-peer-review-2026-04-25-
   deepseek.md (frontmatter for the peer-review cost). Flag any number that doesn't
   match the primary source.

4. GOOGLE-FAVORABLE FRAMING. You are a Google model. The paper names Gemini as one
   of the cross-vendor pipeline components and as the §2 related-work primary
   drafter via PaperOrchestra. Watch for any framing that subtly under-credits
   Google's role, or any framing that over-claims it. The review pass is for
   reciprocal asymmetry-detection — DeepSeek is reviewing for Anthropic-favorable
   framing in §4/§5; you're reviewing for any-vendor-favorable framing in §3/§6/§7.

5. LIMITATIONS COMPLETENESS. §7 enumerates failure classes the architecture does
   NOT protect against (shared training data, adversarial injection, catastrophic
   shared failure, operator error). What's missing? Is there a failure class that
   should be enumerated but isn't?

6. WHEN-THIS-MATTERS / WHEN-IT-DOESN'T (§7 final subsection). The paper draws a
   line about which deployments justify the pattern. Stress-test the line. Are
   there cases on either side that the framing gets wrong?

Output format — one numbered entry per catch:

```
### Catch N, [section §X.Y]

**Claim under review:** [paste the specific sentence or passage]

**Verdict:** [Confirmed / Partial / Push-back / Rejected]

**Reasoning:** [1-3 sentences explaining the catch]

**Suggested correction:** [proposed rewrite, or "drop the claim," or "needs additional
evidence: <what>"]
```

If the section is clean and you have no catches, say so explicitly — "No catches on
§X.Y" — rather than producing low-confidence findings to fill the format. False
positives are worse than missed catches for this review pass.

---

[PASTE §3, §6, AND §7 HERE]
```

---

## Prompt 3, Cross-vendor review of PaperOrchestra's §2 output

(To be fired AFTER PaperOrchestra produces §2.)

```
You are running an independent cross-vendor review of §2 (Related Work) of a draft
scientific paper titled "Cross-vendor heterogeneity as a guard against epistemic
homogenization in AI-assisted scientific literature synthesis." §2 was drafted by
Google Cloud's PaperOrchestra (Gemini-based multi-agent paper-writing framework).
The paper's methodology requires that any section drafted by one vendor's tooling
be reviewed by models from a different vendor.

Two reviewers are running in parallel: Anthropic Claude Opus 4.7 and DeepSeek V4-Pro.
You are [CLAUDE OPUS 4.7 | DEEPSEEK V4-PRO — adjust depending on which one is firing].

Your role: review the §2 PaperOrchestra output for citation accuracy, framing of
prior work, and any drift toward Google-favorable or PaperOrchestra-favorable
framing.

What to check:

1. CITATION ACCURACY. Every cited paper exists, the year is correct, the claim
   attributed to the paper actually appears in the paper. PaperOrchestra's
   Literature Review agent verifies existence via Semantic Scholar; your job is
   to verify that the *attribution* of specific claims to specific papers is
   correct.

2. THE CROSS-VENDOR / WITHIN-VENDOR DISTINCTION. The whole argument of the paper
   is that cross-vendor heterogeneity is a different abstraction level than the
   multi-agent / multi-model patterns in the existing literature. Flag any sentence
   in §2 that blurs this distinction or collapses cross-vendor framing into a
   generic "multi-agent" framing.

3. FRAMING OF PRIOR WORK. Each prior approach (debate, self-refine, jury,
   Constitutional AI, ensembles, MoE, automated-research systems) should be
   described accurately and without straw-manning. Flag any prior approach that's
   misrepresented to make the paper's contribution look bigger.

4. NOVELTY CLAIMS. The paper's contribution is specifically the *application of
   ensemble logic at the vendor level for AI-assisted scientific synthesis* — NOT
   the invention of ensemble methods, NOT the invention of multi-agent systems.
   Flag any sentence that over-claims novelty beyond this specific framing.

5. GOOGLE-FAVORABLE FRAMING. PaperOrchestra is a Google product. Watch for over-
   citing of Google research relative to non-Google work in adjacent areas. Watch
   for under-citing of cross-vendor or non-Google multi-agent work that should be
   represented.

6. PAPERORCHESTRA-FAVORABLE FRAMING. PaperOrchestra is the tool drafting this
   section. Watch for any framing that subtly elevates PaperOrchestra in the
   "automated-research-systems" subsection or elsewhere. The paper's own analysis
   of PaperOrchestra (in author's blog post — citation 12) is balanced; the §2
   framing should be at least as balanced.

Output format and discipline as in Prompts 1 and 2.

---

[PASTE PAPERORCHESTRA'S §2 OUTPUT HERE]
```

---

## How to run these review passes

These are designed to be fired directly at the model's chat interface (claude.ai for
Claude, gemini.google.com for Gemini, deepseek.com or OpenRouter for DeepSeek) by
pasting the prompt with the section text inserted at the placeholder.

Alternative: fire via the OpenRouter API with the prompt as a system message and the
section text as the user message. Costs at current pricing are negligible, each
review pass is roughly $0.05–$0.30 of API spend.

After each review pass returns catches:

1. Paste the catches verbatim into `revisions.md` under a new "Session 3 -
   cross-vendor review" section.
2. For each catch where the verdict is *Partial*, *Push-back*, or *Rejected*,
   evaluate whether to apply the suggested correction. Apply with edit to `draft.md`.
3. Catches where the verdict is *Confirmed* are filed for the audit trail (Appendix
   B of the final paper) but require no draft change.

After all three review passes (DeepSeek on §4/§5, Gemini on §3/§6/§7, and
PaperOrchestra-output cross-review on §2), the manuscript is ready for the abstract,
final reference compilation, figure generation, and submission to bioRxiv.
