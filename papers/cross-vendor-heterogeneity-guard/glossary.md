# Glossary

Running list of precise terms used in the paper, with plain-English glosses. Brian's review pass: if a term in the draft does not appear here with a gloss he understands, the term is wrong (either it's mis-defined, or it shouldn't be in the paper, or it needs a different word).

## Conceptual terms

**Epistemic homogenization.** The drift of a knowledge corpus — a wiki, a research graph, an AI-assisted literature synthesis — toward the blind spots and biases of whichever AI model is doing the synthesis. Distinct from per-output hallucination, which is a single wrong answer. Homogenization is the corpus *as a whole* starting to reflect one model's prior rather than the underlying reality.

**Heterogeneity guard.** A procedural defense against epistemic homogenization. Forces synthesis or review to pass through models with different training pipelines, so a blind spot in one is likely caught by another.

**Cross-vendor vs. multi-model.** "Multi-model" means using more than one model — but those models can all be from the same company (e.g., GPT-4o + GPT-4 + GPT-3.5 are multi-model but single-vendor). "Cross-vendor" means models trained by different companies on different data with different alignment procedures. The paper argues that cross-vendor is the heterogeneity level that matters, not multi-model alone.

**Adversarial collaboration.** A pattern from social science where two researchers with opposing predictions design an experiment together. Used in this paper as an analogy for what cross-vendor review produces — different models with different priors are forced to converge on the same evidence.

## Architectural terms

**Sweep daemon.** The automated four-pass review pipeline described in this paper. Fires on every wiki edit; runs the four passes; commits results back to the repository.

**Pass 1 — Propagate.** First model (Sonnet) reads the edited file and propagates the new findings to any other wiki pages that cross-reference the affected concepts.

**Pass 2 — Synthesize.** Second model (Gemini) reads the entire corpus and emits cross-document synthesis: new connections, contradictions, open questions.

**Pass 3 — Review.** Third model (Opus) critiques Pass 2's synthesis with a fixed verdict vocabulary (Confirmed / Push-back / Rejected).

**Pass 4 — Cross-vendor peer review.** Fourth model (DeepSeek V4-Pro) runs an independent review of the Claude-Opus output, surfacing findings the Claude pipeline missed. The cross-vendor pass is the explicit heterogeneity guard.

**OpenRouter.** A third-party API gateway that exposes multiple vendors' models behind one HTTP interface. The sweep uses it to avoid per-vendor rate limits and to make the cross-vendor pattern operationally simple.

**`[skip-wiki-sweep]` commit marker.** A literal string in a commit message that tells the GitHub Action to skip the sweep for that commit. Prevents the sweep from infinitely re-triggering on its own output commits.

## Discipline terms

**Pre-commit grep-verify gate.** A rule that every load-bearing quantitative claim in newly-authored wiki content must be checked against its primary source *before* the commit lands. Catches hallucinated numbers before they propagate.

**Subagent.** An AI model invoked by the main agent to perform a focused sub-task (e.g., one wiki page authoring run). The subagent has no memory of the main conversation and works only from a brief.

**Subagent brief.** The prompt given to a subagent. Contains scope, method, source pointers.

**Subagent brief hygiene.** The discipline of keeping the subagent's brief uncontaminated by the user's contrived examples, predictions, or framings — because those propagate verbatim into the subagent's output and bias its findings.

**Comp-NNN.** Open Enzyme's numbering for computational experiments. Each comp-NNN has its own folder (`experiments/comp-NNN-name/`) with method, data, results, and a wiki page summarizing the findings.

## Biology terms (used only in case studies)

**DAF / CD55.** Decay-accelerating factor, a human complement regulator protein. UniProt accession P08174.

**SCR domain (sushi / CCP fold).** Short Consensus Repeat domain — the canonical building block of complement regulators. Each SCR has two intra-domain disulfide bonds (cysteine pairs that hold the fold together).

**UniProt.** The international canonical database of protein sequences and annotations. UniProt feature annotations are the authoritative source for things like disulfide-bond positions.

**pLDDT.** AlphaFold's per-residue confidence score (0-100). High pLDDT (>80) means AlphaFold is confident in the local structure; low pLDDT (<50) usually means the region is disordered or poorly predicted.

**MEROPS.** A database of proteases (enzymes that cut other proteins) and their cleavage-site preferences. Used in OE to predict which proteases will cut a designed construct.

**Paperclip MCP.** An external tool that exposes ~11M full-text scientific papers via an API. Tested for integration with the sweep daemon; failed the verification probe.

**`map` operator.** A specific synthesis primitive in the Paperclip tool. Promised to extract structured data across multiple papers; in testing, returned hallucinated quantitative values and misattributed organism identities.
