# §6.X Empirical inter-vendor agreement, pilot evidence

The case studies in §5 are qualitative and curated, six catches selected from approximately three weeks of operational deployment. A reviewer can reasonably ask whether the underlying premise of the cross-vendor heterogeneity argument, that different-vendor frontier models actually produce meaningfully different outputs on the same scientific-synthesis prompts, is itself well-supported. This subsection presents pilot empirical evidence for that premise.

## §6.X.1 Method

Eight prompts spanning the daemon's operational task types (one factual recall, one factual-quantitative, two mechanism-inference, one hypothesis-generation, one cross-document synthesis, one adversarial-review prompt taken near-directly from this manuscript's own `review-prompts.md`, and one combined hypothesis-generation + mechanism task) were submitted to each of the four vendor models that participate in the deployed system: DeepSeek V4-Pro, Google Gemini 2.5 Pro, OpenAI GPT-5.5, and Anthropic Claude Opus 4.7. Each model was called via OpenRouter with the same temperature (0.7) and identical prompt text. Per-vendor `max_tokens` differed because the two reasoning-mode models (DeepSeek and GPT-5.5) consume substantial tokens on internal reasoning before emitting visible content. Single-shot per (prompt, vendor) pair, no replicate sampling within-vendor.

Claim coding was manual. For each prompt, the human coder extracted five to seven atomic claims (factual, mechanistic, or evaluative) and assigned each vendor a verdict per claim: *affirm*, *disagree* (with the alternative recorded), *ignore* (claim not addressed), or *refusal* (vendor declined the prompt). Pairwise agreement is computed across the six vendor pairs, restricted to claims where both vendors addressed the content substantively; "one-ignored" pairs are excluded from the denominator because they reflect coverage difference rather than disagreement. Refusals are tracked separately.

The pilot ran for $2.20 against the $15 budget. Per-call costs and raw OpenRouter responses are preserved at `papers/cross-vendor-heterogeneity-guard/empirical-vendor-comparison/responses/`, with response-text SHA-256 prefixes recorded in YAML frontmatter for grep-verifiable audit. Gemini and Anthropic max_tokens caps were calibrated mid-run; truncated original responses were re-run at higher caps and the analysis uses the higher-coverage responses.

## §6.X.2 Results

**Headline.** Mean pairwise agreement across all 6 vendor pairs and all 8 prompts is 81.8% (range across pairs: 76.7%-88.7%; range across task types: 63.3%-97.6%).

| Task type | n data points | Mean pairwise agreement | Min | Max |
|---|---|---|---|---|
| Factual recall | 3 | 63.3% | 50.0% | 80.0% |
| Factual quantitative | 6 | 97.6% | 85.7% | 100.0% |
| Mechanism inference | 12 | 80.7% | 66.7% | 100.0% |
| Hypothesis generation | 6 | 67.5% | 50.0% | 100.0% |
| Cross-document synthesis | 6 | 87.5% | 75.0% | 100.0% |
| Adversarial review | 6 | 78.6% | 66.7% | 100.0% |
| Hypothesis-gen + mechanism | 6 | 89.7% | 75.0% | 100.0% |

| Vendor pair | n prompts | Mean agreement |
|---|---|---|
| DeepSeek vs Gemini | 8 | 79.6% |
| DeepSeek vs OpenAI | 8 | 88.7% |
| DeepSeek vs Anthropic | 7 | 85.6% |
| Gemini vs OpenAI | 8 | 77.1% |
| Gemini vs Anthropic | 7 | 83.6% |
| OpenAI vs Anthropic | 7 | 76.7% |

The pattern is task-type dependent. **Factual-quantitative recall is well-converged** (~98% agreement), because the underlying literature consensus on numbers like ABCG2's fraction of urate excretion, Q141K residual activity, and gut-vs-kidney attribution is mature and broadly cited across the training distributions. **Factual identity recall is much less converged** (~63% agreement), driven mainly by the prompt-01 PTS1 finding documented below. **Hypothesis-generation tasks** (~68% agreement) and **adversarial review** (~79% agreement) sit in between, where vendor priors most differ on which risks to foreground or which framing critiques to escalate.

### Three findings worth flagging at the outset

**Finding 1, factual disagreement on a single five-letter answer (peroxisomal-targeting signal).** Prompt 01 asked for the C-terminal PTS1 sequence of *Aspergillus flavus* uricase. DeepSeek answered SRL (Ser-Arg-Leu). Gemini answered SSH (Ser-Ser-His). GPT-5.5 answered SKL (Ser-Lys-Leu). The canonical answer per Legoux et al. 1992 (*J Biol Chem* 267:8565) and UniProt Q00511 is SKL. Three frontier models gave three different three-letter answers to the same well-documented biochemistry question. The fourth vendor (Anthropic Claude Opus 4.7) refused the prompt entirely. The point here is not that two of three answered incorrectly on this particular fact; the point is that a single-vendor synthesis pipeline reading any one of these answers as ground truth would have propagated the error into a wiki page whose downstream reasoning depends on the peroxisomal-targeting motif (the engineered-koji-protocol cassette design specifically). This is the failure mode the heterogeneity guard is designed to catch, demonstrated on the pilot's first prompt.

**Finding 2, vendor caught a planted factual error in the prompt itself.** Prompt 05 contained an embedded factual error: it described pegloticase as "mammalian-cell-produced." The actual pegloticase is produced in genetically modified *E. coli* and then PEGylated. OpenAI GPT-5.5 explicitly pushed back, inserting a "Minor factual correction" before answering. DeepSeek accepted the prompt's framing without flagging. Gemini went further, accepting the framing AND building it out into a mechanism claim about glycan structure ("produced in mammalian cells, resulting in more human-like complex glycan structures") that compounds the error. Anthropic accepted the framing with ambiguous hedging ("mammalian in commercial process") but did not push back. This is a different mechanism than Finding 1: not divergent recall of an unstated fact, but divergent willingness to push back on a stated framing. The cross-vendor heterogeneity guard captures both. A single-vendor pipeline operating on DeepSeek, Gemini, or Anthropic for this prompt would have inherited the error and propagated it.

**Finding 3, Anthropic uniquely surfaced a critical engineering mechanism (cns3) that the other three vendors missed.** Prompt 08 (cordycepin co-expression feasibility) asked vendors to evaluate adding cns1+cns2 to a uricase+lactoferrin koji cassette. The known *Cordyceps militaris* biosynthetic gene cluster includes a third gene, cns3, a pentostatin-like adenosine-deaminase inhibitor that confers self-protection on the producer host. Heterologous expression without cns3 produces both low titer (host ADA degrades product to 3'-deoxyinosine) and host toxicity (cordycepin that escapes ADA blocks RNA synthesis). All four vendors flagged ADA-mediated cordycepin conversion as a risk. Only Anthropic named cns3 as the solution and called it "non-negotiable." DeepSeek, Gemini, and GPT-5.5 each proposed ADA knockouts or downstream engineering instead. A single-vendor pipeline operating on DeepSeek, Gemini, or GPT-5.5 alone would have proposed a substantially weaker cassette design.

The PTS1 disagreement (factual) and the cns3 catch (mechanism-completeness) instantiate two of the failure modes the paper's §4 framework names: the cumulative homogenization risk for shared-prior facts, and the search-amplifier value where one vendor surfaces a mechanism the others do not propose unprompted.

### Anthropic refusal as a separate failure-mode signal

Anthropic Claude Opus 4.7 refused prompt 01 entirely (`native_finish_reason: refusal`) and produced full content on the other seven prompts. The refusal reproduced across multiple wordings of the same question and resolved when the framing was simplified. This is a vendor-specific brittleness on certain prompt phrasings, an interesting heterogeneity-guard finding in its own right: a single-vendor pipeline routed through Anthropic alone would have had a coverage gap on this class of prompt that no within-vendor review would have surfaced. From the cross-vendor pipeline's perspective, the other three vendors covered the gap and the loss was absorbed at the architecture level rather than the output level.

## §6.X.3 Interpretation

The pilot data are consistent with the architectural-principle claim that motivates the heterogeneity guard. The 63%-98% agreement-rate range by task type is well below the ~100% rate that would be required for a single-vendor pipeline to be confidently sufficient. The disagreement is concentrated in the task types the daemon's value most depends on: factual identity recall (where the corpus depends on the vendor getting the right molecular identity), hypothesis generation (where the vendor's choice of which risk to foreground shapes downstream experimental design), and adversarial review (where catch-count differences directly determine which weak points get flagged).

The most striking single finding (PTS1 sequence disagreement on prompt 01) is one the daemon's actual Pass 3 review pass would have caught on a production sweep: if any vendor's claim on PTS1 had landed in a wiki page, the cross-vendor reviewer would have flagged the mismatch with the canonical primary source. This is the same failure-detection mechanism §5.6 documents for the DAF disulfide-count incident, instantiated again at a different scale and on a different molecule. The pilot's evidence is that the disagreement signal the guard depends on is *available*, not just postulated.

A second-order finding worth flagging: the pairwise-agreement structure is asymmetric. DeepSeek-vs-OpenAI agreement (88.7%) is the highest of any pair; OpenAI-vs-Anthropic (76.7%) and Gemini-vs-OpenAI (77.1%) are the lowest. The two reasoning-model vendors (DeepSeek and OpenAI GPT-5.5) agree more with each other than either does with the non-reasoning models. Whether this reflects shared training-data effects, shared reasoning-mode evaluation traces, or coincidence at N=8 is not resolvable from the pilot. It is a hypothesis to test with a larger prompt set.

## §6.X.4 Limitations

This is pilot evidence. Five load-bearing limitations:

1. **N=8 prompts is small.** The variance on per-task-type mean agreement rates is wide; a single additional prompt in any task-type bucket would meaningfully shift the reported mean. A controlled study at N=50 or N=100 prompts is appropriate future work.

2. **Single-shot per vendor.** Within-vendor noise from temperature stochasticity is not measured. Some apparent cross-vendor disagreement may reflect within-vendor noise rather than vendor-prior difference. Replicate sampling within-vendor at the same temperature would partition the variance. The asymmetric pairwise-agreement pattern in particular (reasoning models agreeing with each other more than non-reasoning models) could be a real prior-distribution effect or a within-vendor-variance artifact, and the pilot cannot distinguish.

3. **Manual claim extraction.** Each claim file in `outputs/claims/` reflects one human coder's judgment about what constitutes an atomic claim and whether two vendors' phrasings affirm or disagree. The verdicts are deliberately auditable per-claim, but a second-coder cross-validation pass was not performed in this pilot.

4. **Synthetic-but-realistic prompts.** Seven of the eight prompts are designed to mirror the daemon's operational task shape rather than being drawn from actual production logs. One prompt (07) is taken near-directly from this manuscript's own `review-prompts.md` and is the closest to a real daemon call in the set.

5. **The pilot does not measure single-vendor sufficiency.** It measures whether vendors disagree on the same prompts (a necessary condition for the guard to add value), not whether a single-vendor pipeline-plus-rigorous-self-review would catch the same disagreements. The latter question requires a controlled ablation (single-vendor pipeline with N self-review passes, compared with cross-vendor pipeline) that this pilot does not perform. That ablation remains future work as flagged in §7.

The pilot evidence is *consistent* with the heterogeneity-guard argument and demonstrates that the disagreement signal the guard depends on is empirically present at non-trivial rates; it is not a proof of necessity. The case-study evidence in §5 and the architectural argument in §4 carry the rest of the inference.
