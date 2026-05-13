# Glossary

Running list of precise terms used in the paper, with plain-English glosses. **How to use this:** read the gloss alongside the term in the draft. If a sentence in the draft uses one of these terms and the gloss here doesn't help you understand what the sentence means, the sentence is wrong — flag it for rewrite. Conversely, if the draft uses a technical term that is not in this glossary, it needs to either be added here or replaced in the prose.

Terms grouped by topic, not by section.

---

## Conceptual terms — the paper's argument

**Epistemic homogenization.** The drift of a knowledge corpus — a wiki, a research graph, an AI-assisted literature synthesis — toward the blind spots and biases of whichever AI model is doing the synthesis. Distinct from per-output hallucination, which is a single wrong answer. Homogenization is the corpus *as a whole* starting to reflect one model's prior rather than the underlying reality. The paper's central concept.

**Heterogeneity guard.** A procedural defense against epistemic homogenization. Forces synthesis or review to pass through models with different training pipelines, so a blind spot in one is likely caught by another.

**Cross-vendor vs. multi-model.** "Multi-model" means using more than one model — but those models can all be from the same company (e.g., GPT-4o + GPT-4 + GPT-3.5 are multi-model but single-vendor). "Cross-vendor" means models trained by different companies on different data with different alignment procedures. The paper argues that cross-vendor is the heterogeneity level that matters, not multi-model alone.

**Adversarial collaboration.** A pattern from social science where two researchers with opposing predictions design an experiment together. Used in this paper as an analogy for what cross-vendor review produces — different models with different priors are forced to converge on the same evidence, with disagreement highlighted as data.

**Training-distribution prior.** The implicit "default opinions" a model picks up from the data it was trained on. Two models trained on substantially different data have different priors; two models from the same vendor trained on overlapping data have largely the same prior, even if the models themselves are different sizes.

**RLHF (Reinforcement Learning from Human Feedback).** The procedure by which frontier model vendors fine-tune raw language models to be more helpful, harmless, and honest. Each vendor's RLHF pipeline reflects that vendor's choices about which behaviors to reward — which is why two models from different vendors have characteristically different verbal patterns and failure modes even when their base capability is similar.

**RLAIF (Reinforcement Learning from AI Feedback).** Extension of RLHF in which the preference labels driving reward-model training come from an off-the-shelf LLM rather than from human annotators. Originated as part of Anthropic's Constitutional AI work and was later scaled and benchmarked against RLHF on summarization and dialogue tasks. Same-vendor AI feedback by construction in the standard formulation.

**PoLL (Panel of LLM evaluators).** Term coined by Verga et al. (2024). An ensemble of LLM judges (rather than a single large judge) used to evaluate the quality of LLM outputs. The original PoLL construction is cross-vendor (Cohere, OpenAI, Anthropic) and is the closest antecedent in the existing literature to this paper's cross-vendor heterogeneity guard, applied to per-output evaluation rather than corpus-level synthesis.

**Model collapse.** The training-time failure mode in which a generative model trained recursively on its own outputs progressively loses the tails of its output distribution and degrades irreversibly. Documented by Shumailov et al. (2023, 2024). Related to but distinct from epistemic homogenization: model collapse manifests in the model's parameters; homogenization manifests in a corpus the model maintains, with the model itself unchanged.

**Ensemble methods / variance reduction.** A classical machine-learning pattern where multiple models' outputs are combined to produce a more reliable answer than any single model could give. Works because random errors in different models are uncorrelated and tend to cancel. The cross-vendor heterogeneity guard is a special case of ensemble logic applied at the vendor level — the heterogeneity is at the level of training-distribution prior, not at the level of inference-time stochasticity.

---

## Architectural terms — what the daemon is

**Sweep daemon.** The automated three-pass review pipeline described in this paper. Fires on every wiki edit; runs the three passes; commits results back to the repository.

**Pass 1 — Propagate.** First model (currently Anthropic Claude Sonnet 4.6) reads the edited file and propagates the new findings to any other wiki pages that cross-reference the affected concepts. Inline updates only; no synthesis.

**Pass 2 — Synthesize.** Second model (currently DeepSeek V4-Pro primary, Google Gemini 2.5 Pro fallback) reads the entire corpus and emits cross-document synthesis: new connections, contradictions, open questions, proposed experiments. Each finding ends with a `{{PEER-REVIEW}}` marker so Pass 3 knows where to insert a review.

**Pass 3 — Review.** Third model (currently Anthropic Claude Opus 4.7, or OpenAI GPT-5.5 in an alternative configuration) critiques each Pass 2 finding with a fixed verdict vocabulary (*Confirmed* / *Confirmed-prioritize* / *Partial* / *Push-back* / *Rejected*). Has read-only tool access for primary-source spot-checks.

**Episodic peer-review pass.** A separate, formalized fourth pattern: an independent vendor's model receives the substrate (the wiki at a given commit) and produces a parallel synthesis plus a differential analysis against the daemon's output. Run when a major architectural change lands, when a class of synthesis output is suspect, or when the cost of a missed connection is high. The seminal instance is DeepSeek V4-Pro reviewing Claude Opus 4.7 on 2026-04-25 — the catch that motivated formalizing the cross-vendor daemon itself.

**OpenRouter.** A third-party API gateway that exposes multiple vendors' models behind one HTTP interface. The sweep uses it to avoid per-vendor rate limits and to make the cross-vendor pattern operationally simple. Cost dashboards and routing logs are OpenRouter's, not the underlying vendor's.

**`[skip-wiki-sweep]` commit marker.** A literal string in a commit message that tells the GitHub Action to skip the sweep for that commit. Prevents the sweep from infinitely re-triggering on its own output commits. Enforced by hooks so an operator typo cannot suppress sweeps silently.

**`sweep-N-` commit prefix.** Daemon-authored commits start their subject with `sweep-1-propagate:`, `sweep-2-synthesize:`, or `sweep-3-review:`. Hooks enforce that this prefix is only usable by the daemon (author email = `github-actions[bot]`), so a hand-edit cannot accidentally hide work from the diff-base computation.

---

## Inter-pass handoff terms

**Trigger files.** The wiki page(s) edited in the commit that fired the sweep. Pass 1 receives these as input.

**Propagated files.** Wiki pages that Pass 1 modified beyond the original triggers. Pass 1 emits this list so Pass 2 can weight its attention toward the union of triggers and propagated files (where new cross-document connections are most likely to emerge).

**Cited files.** Wiki pages Pass 2 referenced in any of its emitted findings. Pass 2 emits this list as a `Sources cited:` manifest so Pass 3 can read those pages as a "warm cache" without tool round-trips.

**Warm cache.** The set of files inlined into a pass's initial prompt as context, so the pass doesn't have to spend tool calls fetching them. Used in Pass 3 to give the reviewer immediate access to triggers + cited files; tool fetches are reserved for the cache misses.

**Failure ledger.** A Markdown file (`logs/failed-sweep-<sha>.md`) written when a pass fails non-recoverably. Captures pass number, model, prompt path, error message, and cost-so-far. Uploaded as a GitHub Actions workflow artifact so the trace survives runner teardown even when the failing commit doesn't.

**State registry.** `logs/sweep-state.json`, the atomic-write source of truth for "what has been swept and what hasn't." Replaces a brittle regex over commit messages. Includes `last_full_sweep_commit`, `pending_paths`, and a `recent_failures` ledger.

---

## Discipline terms

**Pre-commit grep-verify gate.** A rule that every load-bearing quantitative claim in newly-authored wiki content must be checked against its primary source *before* the commit lands. Catches hallucinated numbers before they propagate.

**Subagent.** An AI model invoked by the main agent to perform a focused sub-task (e.g., one wiki page authoring run). The subagent has no memory of the main conversation and works only from a brief.

**Subagent brief.** The prompt given to a subagent. Contains scope, method, source pointers.

**Subagent brief hygiene.** The discipline of keeping the subagent's brief uncontaminated by the user's contrived examples, predictions, or framings — because those propagate verbatim into the subagent's output and bias its findings. Scope and method propagate; predictions and contrived examples scrub.

**Rhetorical-callback tell.** When a subagent's report-back uses the user's exact phrasing back at the user ("your X framing landed empirically," "as you suspected"), that is a signal the user's phrasing influenced not just the search but the framing of the result. A smoking gun for narrative-cohesion bias.

**Verification re-run.** When a subagent brief contains contamination-class content (compound names, contrived examples, motivational framing), the cheapest corrective is an independent re-run with a scrubbed brief. The comparison happens after both reports land; convergence raises confidence, divergence surfaces a confounder.

**Comp-NNN.** Open Enzyme's numbering for computational experiments. Each comp-NNN has its own folder (`experiments/comp-NNN-name/`) with method, data, results, and a wiki page summarizing the findings.

---

## Biology terms (used in case studies)

**DAF / CD55.** Decay-accelerating factor, a human complement regulator protein. UniProt accession P08174.

**Complement (in immunology).** A cascade of plasma proteins that, when activated, marks pathogens for destruction. DAF/CD55 is one of the human regulators that prevents the complement cascade from activating against the body's own cells. Engineering a soluble version of DAF SCR1-4 for delivery via fungal fermentation is one of the Open Enzyme platform's active engineering candidates.

**SCR domain (sushi / CCP fold).** Short Consensus Repeat domain — the canonical building block of complement regulators. Each SCR has two intra-domain disulfide bonds (cysteine pairs that hold the fold together). The 2026-05-06 hallucination incident in §5.1 was about the disulfide count in this specific fold class.

**UniProt.** The international canonical database of protein sequences and annotations. UniProt feature annotations are the authoritative source for things like disulfide-bond positions; the §5.1 catch came from grepping UniProt P08174 directly.

**pLDDT.** AlphaFold's per-residue confidence score (0-100). High pLDDT (>80) means AlphaFold is confident in the local structure; low pLDDT (<50) usually means the region is disordered or poorly predicted. Used in the comp-012 pipeline to decide which protein regions are surface-exposed enough to be protease-accessible.

**MEROPS.** A database of proteases (enzymes that cut other proteins) and their cleavage-site preferences. Used in OE to predict which proteases will cut a designed construct.

**Km (Michaelis-Menten substrate-affinity constant).** The substrate concentration at which an enzyme operates at half its maximum velocity. A core kinetic parameter for any enzyme; the §5.3 Paperclip probe surfaced a ~7,500-fold error on Km specifically.

**Paperclip MCP.** An external tool that exposes ~11 million full-text scientific papers via an API. Tested for integration with the sweep daemon; failed the verification probe.

**`map` operator.** A specific synthesis primitive in the Paperclip tool. Promised to extract structured data across multiple papers; in testing, returned hallucinated quantitative values and misattributed organism identities.

**Common Crawl.** A large public web-crawl dataset that most frontier model vendors include as part of their pre-training corpus. The shared-training-data limitation discussed in §7 is rooted in the fact that all major vendors train on substantially overlapping versions of Common Crawl.

---

## Production-process terms (Methods Appendix)

**Primary drafter.** The model that produced the initial draft of a section. Recorded per-section in Appendix A.

**Independent reviewer.** A model from a different vendor than the primary drafter, run on the section after the initial draft. Catches that surface are logged in `revisions.md`.

**PaperOrchestra.** Google Cloud's multi-agent framework for automated AI research paper writing (Outline / Plotting / Literature Review / Section Writing / Content Refinement, with Semantic Scholar citation verification). Designed to compress writing-up of work after the science is done. Used in this paper specifically for §2 related work, the section where outside literature is pulled in.

**Self-verification pass.** The drafter applying the project's own pre-commit grep-verify gate to load-bearing quantitative and identity claims in its own output before commit. Distinct from cross-vendor review (which is an independent vendor's pass). Captures the catches in `revisions.md`.
