# §6.X Empirical inter-vendor agreement, pilot evidence

> **SUPERSEDED.** This file is the subagent's intermediate working draft of §6. The canonical, post-audit version lives in `../draft.md` §6, which incorporates: (1) the within-vendor replicate study integrated into the main interpretation, (2) the 2026-05-14 cross-vendor audit-trail catch of the PTS1 / Gemini-r1 / claim-coding mismatch (preserved as the §6 meta-catch box), and (3) corrected agreement numbers (cross-vendor 82.3%, within-vendor 90.8%, real-heterogeneity gap 8.5 pp; Gemini answered SKL correctly on r1, not SSH). Wherever this file's prose differs from `../draft.md` §6, the latter is canonical. Retained here for provenance.

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

## §6.X.4 Partitioning the disagreement: within-vendor replicate study

A reviewer of the pilot draft asked the obvious next question: how much of the 18.2% cross-vendor disagreement is real vendor-prior difference, versus within-vendor temperature stochasticity that would produce similar disagreement on consecutive calls to the same model? To partition the variance, each of the 32 (prompt, vendor) cells from the original pilot was called two additional times at the same prompt, same vendor, same temperature (0.7), same max_tokens cap. Each replicate response was coded against the same atomic-claim taxonomy from the original run. Within-vendor pairwise agreement is computed across the three replicates per cell (r1-r2, r1-r3, r2-r3 = three pairs), aggregated across the 32 cells.

**Headline within-vendor agreement rate: 90.6%, compared to the 81.8% cross-vendor headline.** The within-vendor rate is 8.7 percentage points higher than the cross-vendor rate. Interpreting the gap as a partition:

- Cross-vendor disagreement: 18.2%
- Within-vendor disagreement (temperature noise floor): 9.4%
- Residual cross-vendor heterogeneity signal: 8.7% (48% of total cross-vendor disagreement)

About half of the original 18.2% cross-vendor disagreement is real prior-distribution difference between vendors; the other half is within-vendor noise that any single-vendor pipeline running at the same temperature would also produce on a second call. The architectural-principle claim survives the partition but at roughly half the headline magnitude. The cross-vendor heterogeneity guard captures real prior diversity that within-vendor sampling does not reproduce, even though both contribute roughly equally to the headline disagreement number.

The per-vendor structure of within-vendor stability does *not* support the reasoning-mode hypothesis flagged in the original pilot draft. The earlier draft speculated that DeepSeek V4-Pro and OpenAI GPT-5.5 might be individually more stable across replicates than the non-reasoning Gemini and Anthropic models, which would explain why DeepSeek-vs-OpenAI was the highest-agreement cross-vendor pair (88.7%). The replicate data falsify that explanation:

| Vendor | Within-vendor agreement (this study) | Cross-vendor agreement (pilot) |
|---|---|---|
| Anthropic Claude Opus 4.7 | 94.0% | 81.9% |
| DeepSeek V4-Pro | 90.7% | 84.6% |
| Gemini 2.5 Pro | 89.2% | 79.9% |
| OpenAI GPT-5.5 | 88.3% | 81.0% |

Anthropic is the *most* stable vendor across replicates, not the least. The non-reasoning models (Anthropic 94.0%, Gemini 89.2%) bracket the reasoning models (DeepSeek 90.7%, OpenAI 88.3%) on both sides. The DeepSeek-vs-OpenAI cross-vendor agreement (88.7% in r1) is better explained as a real prior overlap between the two reasoning-mode pipelines than as artifact of within-vendor stability. Anthropic's high within-vendor rate is partly inflated by its refusal stability on prompt 01: the model refused all three replicates of the uricase PTS1 prompt, and "both refused" is coded as substantive agreement. Excluding that effect, the four vendors are within ~7 percentage points of each other in within-vendor stability, with Anthropic still modestly ahead.

The task-type structure is also informative. Factual-quantitative tasks have the highest within-vendor rate (95.2%) and the highest cross-vendor rate (97.6%), nearly identical: vendors converge on quantitative reference values and reproduce them on second calls. Hypothesis-generation and mechanism-inference tasks show the largest within-vendor swings, with the same vendor naming different mechanism trios across replicates. DeepSeek on the NLRP3 priming prompt 03 picked {gut-LPS, DAMPs, FFAs} in r1, {gut-LPS, C5a complement, mast-cell TNF} in r2, and {gut-LPS, FFAs, soluble urate} in r3: only one mechanism (gut-LPS) is consistent across all three replicates. This is exactly the form of within-vendor variation that the partition surfaces.

Two within-vendor findings worth flagging separately because they directly affect the pilot's three highlighted catches:

**The PTS1 disagreement (§6.X.2 Finding 1) is partly within-vendor noise.** In the original pilot the three non-refusing vendors gave three different three-letter answers (DeepSeek SRL, Gemini SSH per the original codification against an earlier truncated response, OpenAI SKL); Anthropic refused. The replicate study shows that the same vendors produce *different* answers on the same prompt across replicates. DeepSeek's PTS1 answer flipped from SRL (r1) to SKL (r2); r3 was truncated at the 8000-token cap before PTS1 was emitted. Gemini answered SKL (r2) and AKL (r3). OpenAI answered AKL (r2) and returned to SKL (r3). Anthropic refused all three replicates of the prompt (a separately interesting stability signal documented in §6.X.2). Three of three non-refusing vendors changed their PTS1 answer at least once across the three replicates. The within-vendor instability is itself the failure mode: a single-vendor pipeline running at the same temperature would produce a different PTS1 answer on subsequent calls, sometimes the canonical SKL and sometimes a near-neighbor wrong answer (SRL, SSH, AKL all appear in this short data). The cross-vendor guard's value here is not only that vendors disagree with each other but that they disagree with themselves; the guard surfaces the underlying uncertainty regardless of which vendor produced the seed answer.

**The cns3 catch (§6.X.2 Finding 3) is stable across replicates.** Anthropic uniquely named cns3 as the non-negotiable resistance gene for cordycepin co-expression on the original pilot. On replicate 2 of prompt 08, Anthropic again named cns3 explicitly ("this is the showstopper... you must co-express the resistance gene cns3"). On replicate 3, Anthropic again named cns3 as required ("You must include cns3 (or a functional equivalent) in the cassette. This is non-negotiable"). DeepSeek, Gemini, and OpenAI again did not name cns3 as a kill-criterion-level requirement in any of r1/r2/r3, matching their original behavior. The cross-vendor catch is reproducible across three replicates of the same prompt to the same vendor: it is a stable vendor-prior difference, not a within-vendor coincidence. This finding is one of the cases the partition cleanly preserves: it is real cross-vendor heterogeneity, not temperature noise.

**The pegloticase factual-error catch (§6.X.2 Finding 2) is partly within-vendor noise on the catching side and stable on the missing side.** The prompt embedded "mammalian-cell-produced" as a factual error about pegloticase (correct: bacterial expression + PEGylation). On r1, OpenAI pushed back, DeepSeek accepted silently, Gemini accepted and amplified the error into a mechanistic glycan claim, and Anthropic accepted with ambiguous hedging. On r2, OpenAI again pushed back (stable), Gemini again accepted and amplified the same error (stable), DeepSeek again accepted silently (stable), and Anthropic caught and corrected the error ("Pegloticase is produced in *E. coli* (no N-glycosylation)" stated explicitly, contradicting the prompt). On r3, OpenAI and Anthropic again caught the error explicitly, DeepSeek now caught it as well ("The prompt describes pegloticase as mammalian-cell-produced; the currently marketed pegloticase (Krystexxa) is actually produced in *E. coli*"), while Gemini for the third time doubled down on the wrong mammalian-cell framing and extended it into the same human-like-glycan mechanistic claim. The catching-side stability is mixed (OpenAI catches all three times; Anthropic catches r2+r3; DeepSeek catches r3 only; Gemini misses all three times AND extends the error each time). Gemini's pattern of accepting AND extending the error is replicate-stable across three replicates, which is more concerning than a one-off error because it suggests the failure mode is structural to the vendor's response prior, not a random sample.

## §6.X.5 Limitations

This is pilot evidence. Five load-bearing limitations:

1. **N=8 prompts is small.** The variance on per-task-type mean agreement rates is wide; a single additional prompt in any task-type bucket would meaningfully shift the reported mean. A controlled study at N=50 or N=100 prompts is appropriate future work.

2. ~~**Single-shot per vendor.**~~ **Addressed by the replicate study reported in §6.X.4.** The original pilot called each cell once; the replicate study added two more calls per cell at the same temperature, producing three replicates per cell and 64 additional API calls. The partition (within-vendor 90.6%, cross-vendor 81.8%) splits the headline cross-vendor disagreement roughly evenly between real cross-vendor heterogeneity and within-vendor noise. N=3 replicates per cell captures modal behavior; N=10+ per cell would tighten the per-vendor stability estimates and is appropriate v2 work.

3. **Manual claim extraction.** Each claim file in `outputs/claims/` reflects one human coder's judgment about what constitutes an atomic claim and whether two vendors' phrasings affirm or disagree. The verdicts are deliberately auditable per-claim, but a second-coder cross-validation pass was not performed in this pilot.

4. **Synthetic-but-realistic prompts.** Seven of the eight prompts are designed to mirror the daemon's operational task shape rather than being drawn from actual production logs. One prompt (07) is taken near-directly from this manuscript's own `review-prompts.md` and is the closest to a real daemon call in the set.

5. **The pilot does not measure single-vendor sufficiency.** It measures whether vendors disagree on the same prompts (a necessary condition for the guard to add value), not whether a single-vendor pipeline-plus-rigorous-self-review would catch the same disagreements. The latter question requires a controlled ablation (single-vendor pipeline with N self-review passes, compared with cross-vendor pipeline) that this pilot does not perform. That ablation remains future work as flagged in §7.

The pilot evidence is *consistent* with the heterogeneity-guard argument and demonstrates that the disagreement signal the guard depends on is empirically present at non-trivial rates; it is not a proof of necessity. The case-study evidence in §5 and the architectural argument in §4 carry the rest of the inference.
