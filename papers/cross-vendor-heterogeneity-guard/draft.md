# Cross-vendor heterogeneity as a guard against epistemic homogenization in AI-assisted scientific literature synthesis

**Brian Abent**
Open Enzyme · brian@headsupresults.com

**Status:** Working draft. Sections §4 and §5 drafted in session 1 (2026-05-13). Remaining sections in progress per `outline.md`.

---

## §4 The heterogeneity-guard rationale

### Definition

A knowledge corpus maintained by a single AI synthesizer over time accumulates that synthesizer's blind spots and biases. New entries are written, reviewed, and cross-referenced through the same model, so consistent errors in the model's prior — preferences for certain framings, recurrent misreadings of specific terminology, characteristic numerical hallucinations — propagate uncorrected. The corpus stops being a faithful synthesis of the underlying literature and starts being a synthesis of the literature *as that model sees it*. We call this drift **epistemic homogenization** of the corpus.

Epistemic homogenization is structurally distinct from per-output hallucination. A hallucinated answer is a single wrong claim; it may be caught by any reader who looks at it. Homogenization is a property of the *corpus as a whole*: consistent biases compounding over hundreds of edits, each individually plausible, with no single output obviously wrong. A reader querying the homogenized corpus receives confident, internally consistent answers that drift from the underlying reality in a direction the reader cannot easily perceive without an outside reference.

### Why cross-vendor specifically

The natural response to epistemic homogenization is to introduce diversity into the synthesis pipeline — run multiple models in review, or alternate which model writes which sections. But the granularity of that diversity matters. Running GPT-4o and GPT-4 in alternation does not guard against OpenAI-specific blind spots; both share the same training-distribution prior, the same alignment procedure, the same characteristic failure modes. Running Sonnet and Opus in alternation does not guard against Anthropic-specific blind spots. Multi-model within a single vendor is multi-instance, not multi-perspective.

Cross-*vendor* heterogeneity — models trained by different companies, on different (though overlapping) data corpora, with different reinforcement-learning-from-human-feedback (RLHF) pipelines and different alignment objectives — is the level at which prior-distribution diversity actually appears. Anthropic-trained models have characteristic verbal patterns and characteristic failure modes that differ from OpenAI-trained models, which differ from Google-trained models, which differ from DeepSeek-trained models. A blind spot in one vendor's training pipeline is unlikely to appear in the same form in another vendor's pipeline. The cross-vendor pattern exploits this independence.

The pattern is not novel as a *concept* — it is a special case of ensemble methods, where the heterogeneity of the ensemble members is what produces the variance-reduction benefit. What is novel here is the application of ensemble logic at the *vendor* level for AI-assisted scientific synthesis, where the relevant variance is in the synthesizer's training-distribution prior, not in inference-time stochasticity. Existing multi-agent literature (debate, self-refine, jury-of-LLMs) operates almost exclusively within a single vendor; this paper argues that for load-bearing scientific corpora, the within-vendor regime is insufficient.

### The self-demonstrating moment

The motivation for the architecture described in this paper did not originate from Claude (Anthropic), the model that drives much of the Open Enzyme sweep pipeline. It originated from DeepSeek V4-Pro, in a peer-review pass on Claude-Opus synthesis output dated 2026-04-25. DeepSeek's Connection 7 (a numbered finding in the peer-review log) flagged that the proposal to run cheap full-corpus sweeps on a single model — at the time, an attractive cost-optimization — would erode exactly the diversity that makes the corpus trustworthy ([1](../../logs/v4-peer-review-2026-04-25-deepseek.md)).

That a model from a different vendor caught a methodological risk Claude had not surfaced unprompted is the cleanest available demonstration of the heterogeneity-guard principle. The architecture's own motivation came from the architecture working. This is the foundational observation the paper extends: cross-vendor review surfaces methodological risks that within-vendor review systematically misses, because the missed risks are precisely the ones that align with the within-vendor model's prior.

---

## §5 Case studies

This section presents four catches from the Open Enzyme sweep pipeline. Each illustrates a different class of failure that the four-pass cross-vendor architecture is designed to catch. The catches are drawn from the operational record of 2026-04-25 to 2026-05-08 — a 13-day window during which the pipeline ran continuously across approximately 60 wiki edits.

### §5.1 Within-vendor cascade: the DAF SCR1-4 disulfide-count hallucination (2026-05-06)

On 2026-05-05, a Sonnet 4.6 subagent was tasked with authoring the wiki page `daf-cd55-scr14-truncated-computational.md` — the computational write-up for comp-012, a stalk-truncation analysis of human DAF/CD55 (a complement regulator, UniProt P08174). The subagent's brief specified the analysis pipeline (AlphaFold-pLDDT-thresholded exposed-site mapping × MEROPS protease cleavage prediction) but did not require disulfide-bond modeling — and indeed, the comp-012 pipeline does not compute disulfide bonds. The Limitations section of the analysis explicitly states "Disulfide bonds not modelled."

The subagent's output asserted, in four separate places of prose narrative, "3 conserved disulfide bonds per SCR domain → 12 total for SCR1-4." The number was not computed by the pipeline; it was generated as plausible-sounding context. The error propagated overnight: the next-morning sweep's Pass 1 incorporated the "12 disulfide" figure into the H05 hypothesis card (`wiki/hypotheses/H05-daf-scr14-cp0-thesis.md`), and downstream synthesis used it as an input to a chaperone-orthogonal stacking calculation, producing a panic over a fabricated total of 29 disulfides across a triple-cassette design.

The catch came from Pass 2 of the next-day sweep, which cross-referenced the new figure against the canonical UniProt P08174 record. UniProt has exactly 8 DISULFID feature annotations across SCR1-4 — the canonical sushi/CCP fold of 2 disulfides per domain, well established in complement biology. The discrepancy surfaced as a contradiction in the Pass 2 synthesis output; the Pass 3 review pass confirmed the error and traced it to the original Sonnet hallucination.

This catch motivated the addition of a "pre-commit grep-verify gate" to the wiki authoring discipline ([2](../../CLAUDE.md)), which requires every load-bearing quantitative claim to be checked against its primary source *before* the commit lands. Pass 2 / Pass 3 remain the backstop; the pre-commit gate is the front line.

**Class of failure caught:** within-vendor cascade — a single-model hallucination propagated through multiple downstream pages, plausible enough to evade casual review, caught by primary-source cross-checking in the next sweep.

### §5.2 Upstream-of-subagent contamination: the comp-018 framing bias (2026-05-08)

On 2026-05-08, a comp-018 subagent was launched to perform a literature scan of upstream complement-cascade modulators. The brief composed for the subagent included a contrived example, originally from a casual user message: "if it's rosemary I'll grow rosemary." The framing was meant to illustrate the kind of finding that would be useful — a specific, growable, dietary modulator — but it landed verbatim in the subagent's instructions.

The subagent's output prioritized rosmarinic acid (a polyphenol abundant in rosemary) as a Tier-1 finding. On review, the evidence supporting Tier-1 placement was thinner than the subagent's narrative suggested — the IC50 values were in vitro only, the in vivo data was sparse, and at least one cited paper had been retracted. The headline finding tracked the framing in the brief more than the underlying evidence.

The catch came from comp-020, a verification rerun specified without the contaminated framing. comp-020's brief was deliberately stripped of contrived examples and asked the same literature scan as an open question. The rerun did not surface rosmarinic acid as a Tier-1 finding; it placed it appropriately in Tier 2 with the evidence caveats. The discrepancy between comp-018 and comp-020 outputs was logged in `operations/comp-018-vs-comp-020-retrospective.md` ([3](../../operations/comp-018-vs-comp-020-retrospective.md)).

This catch motivated the "subagent brief hygiene" discipline now documented in the project's working instructions: scope and method propagate from user direction into the brief, but predictions and contrived examples must be stripped. The full discipline is at `scripts/SWEEP-ARCHITECTURE.md` ([4](../../scripts/SWEEP-ARCHITECTURE.md)).

**Class of failure caught:** upstream-of-subagent contamination — user-supplied framing biases the subagent's output before any model-internal reasoning happens, caught only by independent rerun under a cleaner brief. This class is invisible to within-pass review of the contaminated subagent's own output, because the output is internally coherent.

### §5.3 External-tool reliability test: the Paperclip MCP probe (2026-05-05)

The Paperclip MCP (a Model Context Protocol server exposing ~11 million full-text scientific papers across PMC, arXiv, and bioRxiv/medRxiv via a unified query interface) was evaluated as a potential augmentation to the sweep daemon — specifically as a "literature delta" surface that would let the pipeline detect when a wiki page had fallen behind recent publications. The candidate integration point was the Paperclip `map` operator, a synthesis primitive that promised structured extraction across multiple papers.

The evaluation took the form of a ground-truth probe: 12 papers from the uricase variant landscape (a domain where Open Enzyme already has hand-curated ground truths for organism, kinetic parameters, and experimental modality). The Paperclip `map` operator was queried for the same fields across these papers, and its outputs were compared against the curated ground truths ([5](../../wiki/paperclip-deep-dive.md)).

The probe surfaced three failure classes. (a) Wrong organism identity: papers on *A. flavus* uricase were repeatedly attributed to *A. globiformis*. (b) Fabricated kinetic parameters: specific activity values were returned that were off the true values by approximately 7,500-fold — not within experimental variance, but qualitatively wrong. (c) Invented wet-lab data for purely computational papers: papers that contained no experimental work were summarized as having produced expression yields and activity measurements.

The decision: do not integrate Paperclip into the sweep pipeline. Wiring the `map` operator into Pass 1 or Pass 2 would inject a structured external hallucination source into a corpus designed for rigor — exactly the failure mode the heterogeneity guard is meant to prevent. Paperclip remains available as a manual research tool used with verification discipline; `map` outputs are never propagated without grep-verification.

**Class of failure caught:** external-tool reliability test before integration. The catch happened because the tool was probed against known-correct ground truths *before* being wired into the pipeline. Without the probe, Paperclip's plausible-sounding outputs would have entered the corpus through Pass 2 synthesis and contaminated downstream pages.

### §5.4 Cross-vendor catches methodological risk: DeepSeek Connection 7 (2026-04-25)

The four-pass architecture described in this paper was not the original sweep design. The original design used three passes, all routed to Claude models (Sonnet propagate → Opus synthesize → Opus review). The proposal that motivated the four-pass redesign came from a peer-review pass run on a different vendor — DeepSeek V4-Pro reviewing a Claude-Opus synthesis output on 2026-04-25 ([1](../../logs/v4-peer-review-2026-04-25-deepseek.md)).

DeepSeek's Connection 7 in that review observed: "The 'DeepSeek V4 Assessment' inadvertently highlights a risk of epistemic homogenization in the sweep process. […] If a single model (even a frontier one) becomes the sole source of synthesis, the project's knowledge graph could converge on that model's blind spots and biases. […] The value of this corpus is that it can be interrogated by multiple AI systems with different reasoning architectures, creating a form of 'adversarial collaboration.'"

This was, at the time, a routine peer-review finding among several Connections in the same log. It was not flagged with special urgency. But the observation was load-bearing: it named a structural risk that Claude-driven reviews had not surfaced across previous sweeps, despite the same Claude models having authored the synthesis outputs being reviewed. The within-vendor pipeline could not see the within-vendor blind spot. A different vendor named it on the first pass.

The architectural response was to formalize DeepSeek V4-Pro as a permanent fourth pass — independent peer review of Claude-Opus output, with the explicit role of catching methodological risks that the Claude-driven passes systematically miss. The pattern is documented in `wiki/open-source-platform.md` ([6](../../wiki/open-source-platform.md)) and implemented in `.github/workflows/wiki-sweep.yml`.

**Class of failure caught:** methodological risks invisible from within the dominant vendor's pipeline. This is the highest-value catch class because it is, by construction, the class that within-vendor review cannot surface — the missed risks are precisely the ones that align with the within-vendor model's prior. It is also the class that justifies the cost of the cross-vendor pass: cheaper architectures cannot catch it.

---

## §1 Introduction *(to be drafted next session)*

## §2 Related work *(to be drafted next session)*

## §3 Architecture *(compress from `scripts/SWEEP-ARCHITECTURE.md` next session)*

## §6 Operational data *(extract from logs next session)*

## §7 Limitations and failure modes *(next session)*

## §8 Discussion *(next session)*

## §9 Conclusion *(last)*

## Abstract *(last)*

---

## References *(provisional; full bibliography to follow)*

1. Open Enzyme operational logs. `logs/v4-peer-review-2026-04-25-deepseek.md`. 2026-04-25.
2. Open Enzyme working instructions. `CLAUDE.md`, §"Pre-commit grep-verify gate for load-bearing numbers." 2026-05-06.
3. Open Enzyme retrospective. `operations/comp-018-vs-comp-020-retrospective.md`. 2026-05-08.
4. Open Enzyme sweep architecture. `scripts/SWEEP-ARCHITECTURE.md`. 2026-04-28 onward.
5. Open Enzyme tool evaluation. `wiki/paperclip-deep-dive.md`. 2026-05-05.
6. Open Enzyme platform thesis. `wiki/open-source-platform.md`, §"Multi-model synthesis as guard against epistemic homogenization." 2026-04-25 onward.
