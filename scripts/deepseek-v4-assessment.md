---
title: "DeepSeek V4 Assessment: What It Means for Open Enzyme"
date: 2026-04-25
tags: ["AI", "infrastructure", "doc-sweep", "protein-engineering", "cost-analysis", "DeepSeek"]
related: ["ai-bio-tools-playbook.md", "synthesis.md", "protein-engineering-strategy.md"]
sources: ["DeepSeek V4 technical paper (HuggingFace)", "DeepSeek API docs", "VentureBeat V4 review", "WCCFTech V4 long-context analysis", "NxCode benchmark comparison"]
status: draft
---

# DeepSeek V4 Assessment: What It Means for Open Enzyme

**April 25, 2026**

> **2026-04-25 update — validated**: A test peer-review pass was run via OpenRouter. Actual cost was **$0.21** for a 467,964-input + 4,005-output token full-corpus pass (60 wiki files minus three peripherals to fit under OpenRouter's 512K-token cap on V4-Pro). That's roughly **4× cheaper than this document estimated** — the assessment quoted DeepSeek's direct API pricing, but OpenRouter prices V4-Pro at $0.435/$0.87 per Mtok input/output (vs $1.74/$3.48 below). See `scripts/v4-peer-review.py` for the test harness and `logs/v4-peer-review-2026-04-25.md` for output. The 1M context advertised by the model itself is capped at 512K on the OpenRouter endpoint — a platform-side policy, not a model limitation. Hybrid CI architecture (Claude for Pass 1 propagation, V4 for Pass 2 synthesis) is feasible at the validated cost but not yet implemented.

> **Location note**: this file lives in `scripts/` rather than `wiki/` because it documents AI-tooling decisions (which LLM to invoke for which workflow), not biology research. The principle: `wiki/` is the substrate AI agents read for biology peer review; documents about *which AI* shouldn't pollute that substrate.

DeepSeek V4 dropped April 24. Two models: V4-Pro (1.6T params, 49B activated) and V4-Flash (284B params, 13B activated). Both have 1M token context windows, open weights under MIT license, and pricing that undercuts Claude and GPT by 6-7x. This document evaluates what V4 actually changes for this project, with a specific focus on the automated doc sweep workflow.

---

## 1. The Doc Sweep Use Case: Context Window Math

This is the headline question. The sweep daemon currently triggers a two-pass process: Pass 1 propagates findings from a changed file across all affected wiki pages, then Pass 2 reads the full corpus and synthesizes new connections. The quality of Pass 2 depends directly on how much of the knowledge base the model can hold in context simultaneously.

### Current corpus size

| Scope | Files | Characters | Estimated Tokens |
|-------|-------|------------|------------------|
| Wiki (living docs) | 59 | 1.95M | ~490K |
| Reference (read-only) | ~15 | 47K | ~12K |
| Total project markdown | ~85 | 2.1M | ~525K |

Token estimates use the ~4 chars/token ratio typical of English technical prose. Actual tokenizer counts will vary by model.

### What fits in context

**V4's 1M context window can hold the entire Open Enzyme wiki (~490K tokens) with room to spare for the reference library, the sweep prompt, and a substantial output.** That is roughly 2x the current corpus size, leaving headroom for the project to grow.

For comparison, Claude Sonnet 4.5 and Opus 4.6 offer 200K context windows. The current sweep workflow cannot load the full wiki into a single call. It relies on the daemon building an impact list per trigger file and selectively reading affected pages, which works for propagation (Pass 1) but limits synthesis (Pass 2) to whatever subset the daemon decides is relevant. The model never sees the full picture at once, so it can only find connections between documents it was told to read.

**With V4, Pass 2 could load all 59 wiki files plus all reference docs plus the sweep prompt in a single context.** No impact-list filtering, no missed connections because a seemingly unrelated doc was excluded. The model sees everything, every time.

### But: quality degrades at long context

This is the catch. DeepSeek's own MRCR 8-needle benchmark shows stable retrieval through 128K tokens, with meaningful degradation beyond that. At 1M tokens, the V4-Pro-Max scores 0.59 average MMR (V4-Flash-Max scores 0.49). That is a 10% KV cache architecture paying its tax: the compression that makes 1M tokens affordable also makes the model fuzzier about details buried deep in long inputs.

For the doc sweep, this matters in a specific way. Pass 1 (propagation) is mechanical: find where concept X is mentioned, update those paragraphs. Retrieval accuracy matters here. Pass 2 (synthesis) is creative: read everything and notice patterns. This is more forgiving of imperfect retrieval because the model is generating hypotheses, not answering factual queries about specific sentences.

**Practical recommendation:** Use V4 for Pass 2 (synthesis across the full corpus) where the 1M window is transformative and the task is tolerant of fuzzy retrieval. Keep Claude Opus or Sonnet for Pass 1 (propagation) where precision matters more than breadth. This is a hybrid approach: each model does what it is best at.

---

## 2. Cost Per Sweep

This is where V4 changes the calculus dramatically.

### V4-Pro pricing (the sweep candidate)

V4-Pro is the right choice here. At under $1 per full-corpus sweep, there is no reason to drop to Flash and accept worse reasoning quality. You pay 13x more than Flash but you get a 1.6T-parameter model with 49B activated per token instead of 13B. For scientific cross-referencing, that spread matters.

| | Cache Miss | Cache Hit |
|---|---|---|
| Input | $1.74 / Mtok | $0.145 / Mtok |
| Output | $3.48 / Mtok | $3.48 / Mtok |

For reference, V4-Flash is $0.14/$0.28 per Mtok (input/output, cache miss). It exists, but the Pro pricing is low enough that Flash only makes sense for high-volume batch jobs where you are running hundreds of calls per day.

### Cost estimate: full-corpus sweep pass

Assumptions: 490K input tokens (full wiki), 15K output tokens (synthesis section), cache miss (first call with new content).

| Model | Input Cost | Output Cost | Total |
|-------|-----------|-------------|-------|
| V4-Pro | $0.853 | $0.052 | **$0.91** |
| V4-Flash (for reference) | $0.069 | $0.004 | $0.07 |
| Claude Opus 4.6 (200K cap) | ~$7.35 (at $15/Mtok) | ~$1.13 (at $75/Mtok) | **~$8.48** |
| Claude Sonnet 4.5 (200K cap) | ~$1.47 (at $3/Mtok) | ~$0.23 (at $15/Mtok) | **~$1.70** |

**V4-Pro is roughly 2x cheaper than Sonnet and 9x cheaper than Opus, while fitting 5x more context.** The cost-per-insight ratio is where this gets interesting: Sonnet and Opus can only see a subset of the wiki per call (200K context), while V4-Pro sees everything. You are paying less and getting a more complete synthesis pass.

At $0.91 per full-corpus sweep, you could run V4-Pro on every push and a heavy research day (10 pushes) costs $9. A normal week might be $5-15 total. Compare that to Opus at ~$8.48 per partial-corpus sweep.

With cache hits (the wiki corpus is mostly unchanged between consecutive sweeps), the input cost drops to $0.145/Mtok, putting a full sweep at roughly $0.12. Consecutive sweeps during a sprint are nearly free.

### CI integration cost model

If you wired V4-Pro into the GitHub Actions sweep (the `ci=github-actions` path in `wiki-watch.sh`), every push to `wiki/` would trigger a full-corpus synthesis pass. At current project velocity (a few pushes per day), that is under $5/month. Even at aggressive daily rates during a research sprint, you are looking at $20-40/month for continuous full-corpus AI synthesis with the larger model. That is a rounding error in a research budget.

---

## 3. Science Benchmarks: Is V4 Good Enough for This Work?

### GPQA Diamond (graduate-level science reasoning)

| Model | Score |
|-------|-------|
| Claude Opus 4.7 | 94.2% |
| GPT-5.5 | 93.6% |
| DeepSeek V4-Pro-Max | 90.1% |

V4 trails the frontier closed models by 3-4 points on hard science questions. DeepSeek's own technical report acknowledges a "3 to 6 month gap" with frontier closed-source systems on knowledge and reasoning tasks.

### What this means for Open Enzyme

The doc sweep workflow asks the model to do two things: (a) accurately propagate factual claims with evidence levels, and (b) creatively synthesize connections across documents. These are different cognitive demands.

For (a), the 4-point GPQA gap matters. When the model is updating a claim about NLRP3 inflammasome chokepoints or correcting an evidence level from "in vitro" to "animal model," precision is non-negotiable. A model that is 4% less reliable on hard science means more errors per sweep that Brian has to catch and correct. The cost savings evaporate if you are spending time fixing hallucinated mechanisms.

For (b), the gap matters less. Synthesis is generative: "what if lactoferrin's GSDMD suppression via the Shan 2026 mitophagy axis means it covers CP6b, not just CP1a?" This kind of cross-referencing is about creative pattern-matching, not factual recall. V4's reasoning is likely adequate here, especially with the full corpus in context providing all the raw material.

**Bottom line:** V4-Flash is strong enough for synthesis passes where you are mining for connections. It is probably not the model you want for precision propagation of biochemical claims. V4-Pro closes some of that gap but not all of it.

---

## 4. Protein Engineering: Specific Capabilities

Open Enzyme's protein engineering track (the uricase mutation tiers for GI stability, the koji construct design) requires models to reason about protein structure, predict stability effects of mutations, and design experimental validation. This is specialized work.

### What V4 can do

V4 is a general-purpose language model. It has read the protein engineering literature and can discuss disulfide bond engineering, salt bridge design, surface charge redistribution, and codon optimization competently. It can reason about the mutation tiers in `protein-engineering-strategy.md` and suggest additional candidates.

### What V4 cannot do

V4 does not have a protein structure model. It cannot run molecular dynamics simulations, predict ddG values for mutations, dock substrates, or fold sequences. It is not AlphaFold, Rosetta, or ESMFold. The `ai-bio-tools-playbook.md` already covers the right tools for this: GPT-Rosalind (if access is granted), Amazon Bio Discovery (40+ specialized bio models), and dedicated protein structure tools like AlphaFold3 and ProteinMPNN.

### Where V4 adds value for protein engineering

V4's value is in the reasoning layer above the structure prediction tools. It can:

- Read the output of AlphaFold or FoldX runs and interpret them in the context of the uricase variant tiers (SB-1, BAL-1, OPT-1)
- Cross-reference mutation effects with published literature on homologous enzymes
- Draft experimental protocols for variant testing
- Synthesize results across multiple computational and experimental runs

This is the same kind of work Claude and GPT do today. V4 would be a cost-effective alternative for the bulk reasoning, especially for repetitive tasks like analyzing a batch of variant predictions, but it would not replace the specialized bio-AI tools.

---

## 5. Open Weights: Does Self-Hosting Matter?

V4 is MIT-licensed on Hugging Face. Both Pro and Flash weights are available for download, fine-tuning, and commercial deployment.

### Hardware requirements

| Model | VRAM (FP8) | Minimum Hardware |
|-------|-----------|------------------|
| V4-Flash (284B total, 13B active) | ~158 GB | 1x H200 or 2x A100 80GB |
| V4-Pro (1.6T total, 49B active) | ~500 GB | 8+ H100s with tensor + expert parallelism |

### Is self-hosting worth it for Open Enzyme?

Almost certainly not, at least right now. The API pricing is already low ($0.91/sweep for Pro), and the hardware costs for self-hosting V4-Pro (8+ H100s, ~$15-25K/month on cloud) would exceed API costs unless you were running hundreds of sweeps per day. Self-hosting makes sense for organizations with data sovereignty requirements, custom fine-tuning needs, or massive throughput demands. Open Enzyme has none of these today.

### Fine-tuning potential

This is the more interesting angle. LoRA fine-tuning on V4-Pro requires serious hardware (8+ H100s), but LoRA on V4-Flash-Base is feasible with modest GPU resources (a pair of A100s) and could serve as a stepping stone. A fine-tuned model trained on:

- The Open Enzyme wiki corpus (writing style, evidence-level conventions, cross-referencing patterns)
- Curated biology literature on uricase engineering, NLRP3 biology, and koji fermentation
- Examples of good synthesis passes (the existing `synthesis.md` entries as training data)

...could produce a model that is specifically calibrated for the doc sweep task. It would know the project conventions, understand the chokepoint numbering system, and recognize which compounds and mechanisms are already documented vs. novel.

This is a Phase 1-2 consideration, not Phase 0. The project needs to be further along and generating enough sweep volume to justify the fine-tuning investment. But the option is there, and it is real because the weights are open. You cannot fine-tune Claude or GPT-5 on your proprietary research corpus.

**Mark this as a future option, not a current action item.** The API is the right approach until sweep volume or quality requirements justify the additional complexity.

---

## 6. Comparison to Current Stack

| Dimension | Claude (Opus/Sonnet) | GPT-5.4/Rosalind | DeepSeek V4-Pro |
|-----------|---------------------|-------------------|-----------------|
| Context window | 200K | 128K-256K | **1M** |
| Science reasoning (GPQA) | **94.2%** (Opus 4.7) | ~93% | 90.1% |
| Cost per full sweep | ~$1.70 (Sonnet) / ~$8.48 (Opus) | ~$2-3 | **$0.91** |
| Biology specialization | General | **Rosalind: domain-trained** | General |
| Open weights | No | No | **Yes (MIT)** |
| Fine-tuning | No | No | **Yes (LoRA)** |
| Long-context retrieval | Strong to 200K | Strong to 128K | Good to 128K, degrades beyond |

---

## 7. Practical Recommendations

### Immediate (this week)

1. **Run a test sweep with V4-Pro via the DeepSeek API.** Load the full wiki corpus into a single V4-Pro call with the Pass 2 synthesis prompt. Compare the output quality to the most recent Claude-generated synthesis pass. This is a $0.91 experiment. You will know within one call whether the reasoning quality meets the bar.

2. **Benchmark retrieval accuracy.** Seed a known fact deep in the corpus (e.g., a specific mutation effect buried in `protein-engineering-strategy.md`) and ask the model to find it. Test at various corpus positions. This tells you whether the long-context degradation is tolerable for your specific content at 490K tokens (well under the 1M ceiling, which helps).

### Short-term (next 2-4 weeks)

3. **Implement hybrid sweep architecture.** Wire V4-Pro into the CI sweep for Pass 2 (synthesis across the full corpus). Keep Claude Sonnet or Opus for Pass 1 (propagation of specific pages) where factual precision matters. The combined cost per sweep: ~$0.91 (V4-Pro synthesis, full corpus) + $0.50-1.50 (Claude propagation of affected pages only) = under $2.50 total. Better synthesis quality than today because V4-Pro sees everything, plus better propagation quality because Claude handles the precision work.

4. **Increase sweep frequency.** At under $1/pass, there is no reason to batch saves. Sweep on every push. The sweep log becomes a continuous stream of synthesis rather than periodic snapshots.

### Medium-term (if the project grows)

5. **Evaluate fine-tuning V4-Pro** on the Open Enzyme corpus and synthesis conventions once you have 20+ synthesis entries as training examples. This would produce a sweep specialist that knows the project vocabulary and evidence standards natively. Self-hosting for fine-tuning requires 8+ H100s, so the economics only make sense if sweep volume or data sensitivity increases significantly.

6. **Use V4-Pro for bulk variant analysis** in the protein engineering track. When running batches of mutation candidates through computational tools, V4-Pro can handle the interpretation and cross-referencing at low cost while the specialized tools (AlphaFold, FoldX, Rosalind) handle the structural predictions.

---

## 8. What V4 Does Not Change

A few things stay the same regardless of V4:

- **GPT-Rosalind and Amazon Bio Discovery are still the right tools for protein structure work.** V4 is a language model, not a structure prediction system. The `ai-bio-tools-playbook.md` recommendations stand.

- **Claude is still the better model for high-stakes scientific reasoning.** When you need a model to correctly identify that quercetin and zileuton bind the same catalytic iron site on 5-LOX and are therefore redundant (not additive) at CP6a, you want the model with the highest GPQA score. The 4-point gap on science benchmarks is real and shows up in exactly these kinds of mechanistic subtleties.

- **The sweep architecture still needs a human in the loop.** V4 makes sweeps cheaper and broader, but Brian still reads `synthesis.md` and prunes. No model, regardless of context window or reasoning quality, replaces the judgment call of whether a proposed connection is worth pursuing.

- **Data security posture is unchanged for API use.** DeepSeek's API terms and data handling policies should be reviewed before sending the full research corpus through their endpoints. Open Enzyme is an open-source project, so this is lower-stakes than it would be for proprietary research, but it is worth a read of their privacy policy. Self-hosting eliminates this concern entirely if it ever becomes relevant.

---

## Summary

V4's value to Open Enzyme is concentrated in one specific capability: running full-corpus synthesis passes at a fraction of current cost with the entire knowledge base in context. The 1M context window means every wiki page can be loaded simultaneously for the first time. V4-Pro pricing ($0.91/sweep, dropping to ~$0.12 with cache hits) means you can sweep on every push instead of batching judiciously. The quality gap on science reasoning (4 points below Claude on GPQA) means V4-Pro is better suited for creative synthesis than for precision propagation, which suggests a hybrid architecture where each model handles its strength.

The open weights are a future option for fine-tuning, not an immediate action item. The protein engineering value is in the reasoning layer (interpreting results, cross-referencing literature), not in replacing specialized structure prediction tools.

The cheapest next experiment: a single $0.91 V4-Pro API call loading the full wiki with the Pass 2 synthesis prompt. Compare it to the last Claude synthesis pass. That tells you everything you need to know about whether the quality meets the bar.
