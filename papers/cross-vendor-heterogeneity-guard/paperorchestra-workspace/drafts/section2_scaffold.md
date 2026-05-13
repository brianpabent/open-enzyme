# §2 Related Work — drafting scaffold

This is a working scaffold for §2. Once `citation_pool.json` is complete and `refs.bib` is generated, fill in the `\cite{KEY}` placeholders with the actual BibTeX keys from `build_bib.py` output.

---

## §2 Related Work

The cross-vendor heterogeneity guard described in this paper sits in a literature already rich with multi-agent and self-reflective patterns for improving language-model outputs. This section positions the contribution against five methodology clusters in that literature, plus a sixth body of work on the underlying corpus-collapse phenomenon that motivates the guard.

The clusters share a structural property the paper's contribution does not share: they all operate *within* a single model-vendor's training pipeline, or at an abstraction level orthogonal to vendor identity altogether. The pattern this paper develops — heterogeneity at the level of training-distribution prior, achieved by routing successive synthesis passes through different vendors' frontier models — is, to our knowledge, the first explicit treatment of the cross-vendor regime as an architectural commitment for AI-assisted scientific literature synthesis.

### 2.1 Multi-Agent Debate and Consensus Approaches

[CITE_MULTIAGENT_DEBATE] introduced multi-agent debate as a mechanism for improving the factuality and reasoning of language-model outputs: multiple instances of the same model propose and critique one another's answers across several rounds before converging on a final response. The paper demonstrated gains on reasoning benchmarks and reductions in characteristic hallucination patterns, and the framing was adopted and extended by follow-on work on adversarial argumentation and consensus mechanisms.

The structural commitment of multi-agent debate is at the *inference-time argumentation* layer. The heterogeneity in the system is in how the instances interact — proposing, critiquing, defending — not in their underlying training-distribution priors. When the instances all derive from a single vendor's model family, the system improves robustness to inference-time stochasticity but does not guard against blind spots that are characteristic of the vendor's training pipeline as a whole. The cross-vendor pattern in this paper operates at a different abstraction level: heterogeneity is in the prior itself, with the synthesis passes routed across vendors as an architectural commitment rather than as inference-time agent behavior.

### 2.2 Self-Refinement and Iterative Reflection

[CITE_SELF_REFINE] proposed Self-Refine, in which a single language model produces an initial output and then critiques and revises that output in an iterative loop. [CITE_REFLEXION] proposed Reflexion, which extends the same pattern by maintaining verbal reflective text in an episodic memory buffer so that an agent can learn from prior trials without weight updates. Both patterns are influential and have spawned a substantial body of follow-on work on self-critique loops.

These approaches are, by construction, **same-vendor and typically same-model**: the critic is the generator. They improve local output quality and per-task accuracy, but they cannot surface blind spots that are characteristic of the model's training pipeline — the critic shares the generator's prior. A self-refinement loop catches consistency errors and surface-level mistakes; it cannot catch corpus-level drift toward the model's prior across many independent outputs maintained in a long-lived knowledge graph. The cross-vendor heterogeneity guard described here is complementary to self-refinement rather than a substitute: self-refinement improves individual outputs; the cross-vendor guard prevents the corpus they accumulate into from converging on any one model's blind spots.

### 2.3 LLM-as-Jury and Panel-of-Evaluators

[CITE_LLM_JURY] proposed evaluating LLM generations using a panel of diverse models (PoLL) — an ensemble of LLM evaluators rather than a single large judge — and showed that smaller-model panels can outperform a single large judge on standard evaluation benchmarks while exhibiting less intra-model bias. The work motivates panel diversity by appeal to the same intuition the present paper formalizes for synthesis: a single judge's biases propagate into the evaluation signal; a panel of diverse judges reduces that effect.

Two differences separate the jury pattern from the cross-vendor heterogeneity guard. First, the jury pattern operates on *per-output evaluation*, not on the construction of a long-lived corpus — there is no temporal accumulation of bias to guard against; each evaluation is independent. Second, the diversity in PoLL is across model sizes and families but, in the original construction, predominantly within a single vendor's lineup; the paper's commitment to vendor diversity is implicit at best. The present paper extends the jury-of-LLMs intuition to (a) corpus-level synthesis rather than per-output evaluation and (b) explicit cross-vendor commitment as the architectural pattern.

### 2.4 Constitutional AI and AI-Feedback Alignment

[CITE_CONSTITUTIONAL_AI] introduced Constitutional AI, a technique for training a harmless AI assistant through self-supervision against an explicit list of constitutional principles, without per-output human labels. The technique was extended by [CITE_RLAIF] as Reinforcement Learning from AI Feedback (RLAIF), which uses an off-the-shelf LLM rather than a human annotator to generate the preferences that drive reward-model training. Both approaches have been broadly adopted by frontier labs.

Constitutional AI and RLAIF operate at *training time* — they shape a single model's behavior by adjusting its parameters through same-vendor AI feedback. The cross-vendor heterogeneity guard described here operates at *synthesis time*, using different-vendor frontier models as the sources of independent critique on a corpus that none of them owns or controls. The two are adjacent but address disjoint failure modes: Constitutional AI affects a single model's prior; the cross-vendor guard prevents that prior from dominating a corpus the model contributes to over time.

### 2.5 Automated AI-Scientist Systems

A class of recent end-to-end automated-research systems aspires to compress the full scientific lifecycle — hypothesis generation, experiment design, analysis, and manuscript drafting — into a single agentic pipeline. [CITE_AI_SCIENTIST] introduced Sakana's AI Scientist, the first system aimed at end-to-end open-ended scientific discovery in machine learning. [CITE_AI_SCIENTIST_V2] extended the system with agentic tree search and reported the first fully AI-generated paper to pass a rigorous human peer-review process. [CITE_PAPER_ORCHESTRA] introduced PaperOrchestra, an explicitly partial system that automates only the writing layer — five communicating agents (outline, plotting, literature review, section writing, content refinement) converting pre-writing materials into a submission-ready LaTeX manuscript with Semantic-Scholar-verified citations. A parallel system, FARS (Fully Automated Research System), deployed publicly for 228 hours and produced 100 short machine-learning papers, optimizing for throughput rather than per-paper rigor.

Two structural features unite these systems and motivate the relevance of cross-vendor heterogeneity to autonomous-research deployments specifically. First, each is constructed within a single vendor's model family — Claude or GPT for AI Scientist, Gemini-based for PaperOrchestra, a single-vendor pipeline for FARS. Second, they iterate AI synthesis as a load-bearing component: each step builds on the prior step's AI output, so any blind spot in the system's prior compounds across loop iterations before a human can intervene. The cross-vendor heterogeneity guard is the structural defense against this compounding. None of the systems above currently deploys it as an architectural commitment, though PaperOrchestra's Semantic Scholar citation-verification step is a partial defense against one failure mode (fabricated citations). The pattern this paper develops can be adopted by such systems with modest engineering effort and provides a defense the within-vendor architectures cannot.

### 2.6 Epistemic Homogenization and Model Collapse

The underlying phenomenon the cross-vendor heterogeneity guard defends against is closely related to, but distinct from, **model collapse** as studied by [CITE_MODEL_COLLAPSE] and [CITE_CURSE_RECURSION]. Model collapse describes a training-time failure: when a generative model is trained on data produced by previous generations of the same model, the distribution of generated outputs progressively loses its tails and degenerates over time. The driver is the same — recursive consumption of model-produced content — but the surface is different. Model collapse manifests as a degradation of the model's parameters; epistemic homogenization manifests as a drift in a corpus the model is maintaining, with the model itself unchanged.

The cross-vendor heterogeneity guard does not address training-time model collapse directly; it addresses the corpus-level analogue. The two are complementary defenses for related failure modes in the broader AI-content-feedback-loop literature. We treat epistemic homogenization as a distinct construct from model collapse in this paper, while acknowledging the shared structural intuition: any system that consumes its own outputs as load-bearing input over time develops a degradation that requires an outside reference to detect.

---

## Drafter notes (not for inclusion in paper)

- Citation keys to replace once `build_bib.py` runs: `[CITE_MULTIAGENT_DEBATE]`, `[CITE_SELF_REFINE]`, `[CITE_REFLEXION]`, `[CITE_LLM_JURY]`, `[CITE_CONSTITUTIONAL_AI]`, `[CITE_RLAIF]`, `[CITE_AI_SCIENTIST]`, `[CITE_AI_SCIENTIST_V2]`, `[CITE_PAPER_ORCHESTRA]`, `[CITE_MODEL_COLLAPSE]`, `[CITE_CURSE_RECURSION]`.
- FARS is referenced in §2.5 but is currently not in the S2-verified pool — it has no arXiv preprint we could locate, only blog posts and a tweet thread from Analemma. Either (a) cite the project blog directly via a non-paper citation, or (b) remove the FARS reference. Recommend (a) for accuracy, noting that the citation is to the public deployment record rather than a peer-reviewed paper.
- This scaffold deliberately does NOT cite Bai-Kadavath 2022 beyond the Constitutional AI cluster — the original paper is the canonical reference; sub-citations on specific alignment subtopics are deferred to avoid bloat.
- Word count target: ~1,000 words for §2 total per the outline. Current scaffold prose runs ~1,100 words; tighten if needed during the cross-vendor review pass.
