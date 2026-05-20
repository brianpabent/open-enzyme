---
title: "Agentic-Science Adoption — Process Changes and Tooling from Robin (Nature 2026) and Gemini for Science (I/O 2026)"
date: 2026-05-20
status: active
tags: [operational, methodology, agentic-search, comp-nnn, tooling, platform]
related:
  - ../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md
  - ./README.md
  - ../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/
  - ../.claude/skills/new-comp-experiment/SKILL.md
sources:
  - "Ghareeb et al. 2026 (Nature) — Robin: A multi-agent system for automating scientific discovery — doi:10.1038/s41586-026-10652-y"
  - "Google 2026-05 — Gemini for Science: AI experiments and tools for a new era of discovery — blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/"
  - "Google DeepMind 2025 — Towards an AI co-scientist — arXiv:2502.18864"
  - "FutureHouse 2024 — PaperQA2 / Aviary — arXiv:2409.13740, arXiv:2412.21154"
---

# Agentic-Science Adoption — Process Changes and Tooling from Robin (Nature 2026) and Gemini for Science (I/O 2026)

## TL;DR

Two independent groups (FutureHouse / Robin and Google DeepMind / Gemini for Science) shipped converging multi-agent architectures for literature-grounded scientific discovery within weeks of each other (Robin: Nature 2026-05-13 accepted; Gemini for Science: Google I/O 2026-05-19). The patterns they document — N-trajectory consensus, LLM-judged pairwise tournament, concise/deep lit-search tier split, full disease→mechanism→assay→candidate cycle — are all directly applicable to OE's existing comp-NNN workflow and to the literature-bound chokepoints currently classed as "wet-lab gated."

This document captures the methodology changes worth adopting, the tooling decisions worth making (or deferring), and the first validation instance — **comp-038 tier-2-butyrate-assay-audit** — which tests whether an agentic literature-synthesis cycle can resolve a documented OE assay-infrastructure gap without defaulting to extra API spend when Codex can perform the GPT-5.5 synthesis role in-session.

The parallel strategic reflection ([`../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md)) names six OE stuck items that may be eligible for re-classification from "wet-lab gated" to "agentic-search candidate." This operations doc handles the *methodology and tooling*. The reflection handles the *what gets re-classed*.

## Why this lands now

Three things converged at the same moment:

1. **Robin demonstrated a closed-loop semi-autonomous discovery cycle in Nature.** Given just the disease name "dry age-related macular degeneration," Robin proposed enhancing RPE phagocytosis, screened 30 candidates, ran two wet-lab iterations, and surfaced **ripasudil** (a Japan-approved ROCK inhibitor never proposed for dAMD) and **KL001** (a circadian modulator, genuinely novel hit). Mechanism story: ROCK inhibition → ABCA1 upregulation → lipid efflux → ties cleanly into APOE-driven AMD genetics. Cost per full cycle: $10.76. Time: ~30 min compute + human-in-the-loop wet lab. The architecture is published; Aviary is open-sourced.

2. **Gemini for Science formalized the same architecture as a platform.** Co-Scientist's "idea tournament" is literally Robin's LLM-judged pairwise ranking. AlphaEvolve + ERA is the code-generating discovery agent. Science Skills bundle 30+ life-science databases as Antigravity skills. Deep Think hits gold on the 2025 Physics/Chem Olympiad written sections.

3. **OE's stuck list has a specific shape.** Per the diagnostic walkthrough on 2026-05-20: three clusters dominate — assay infrastructure gaps (Tier 2 butyrate quantification blocks the whole microbiome track), East Asian cohort RCTs that haven't been designed, and the engineered-koji validation gauntlet (SGF survival, protease stability, native kojic-acid NLRP3 activity, gut persistence). Of these, the items most plausibly resolvable via aggressive literature synthesis — not wet lab — are the items Robin-style cycles are best at.

The convergence isn't an accident: the architecture has matured enough that two well-resourced groups arrived at the same shape within weeks. OE doesn't need to invent the pattern. It needs to adopt the pieces that fit and decide what to wait on.

## Pattern library — four reusable patterns

These are the methodological units worth incorporating into OE's workflow. Each is small. Each is independently adoptable. None of them are research content; they're process discipline.

### Pattern 1 — N-trajectory consensus for noisy analyses

**What:** Run the same analysis N times (Robin used N=8) with independent LLM trajectories, then consensus-vote across the outputs. Report only the findings that survive the vote.

**Why:** LLM-driven analyses make subjective methodological choices (gating thresholds in flow cytometry, filter cutoffs in RNA-seq, MSA depth in structural prediction, scoring rubrics in chaperone-orthogonal stacking). A single trajectory's choice may not generalize. Eight trajectories with a consensus step lets the methodology variance show itself — and gives a quantitative confidence signal ("identified in 7/8 trajectories" beats "identified once").

**Where it applies in OE:**

- **comp-022 / comp-032 chaperone-orthogonal stacking** — the framework's coefficients (per [synthesis queue riskiest-assumption-1](../synthesis/queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md)) rest on expert-estimate values, not large-scale empirical datasets. Multi-trajectory analysis with different starting prompts and consensus selection would surface which coefficients are robust to phrasing and which are artifact.
- **Any future comp-NNN protease/stability analysis** — pLDDT-vs-SASA, monomer-vs-tetramer, point-estimate-vs-distribution. Run 8 trajectories with different defensible methodology choices, report consensus.
- **Subagent peer review pass** in the existing `new-comp-experiment` workflow — currently single subagent run; the Robin pattern argues for N parallel reviewers with consensus on "which limitations are real."

**Cost:** Roughly Nx the single-trajectory cost. For LLM-driven analyses this is cheap (8 × $1-2 = $8-16). For structural simulations it depends on the underlying compute.

**Engineering footprint:** A `for i in 1..8` wrapper and a consensus-reducer script. One-day add to the new-comp-experiment skill.

### Pattern 2 — LLM-judged pairwise tournament for ranking

**What:** Instead of asking one model to score N candidates with numeric ratings, do all-pairs (or Swiss-style) pairwise comparisons judged by an LLM, then derive an Elo-style ranking. Robin uses this for both disease-mechanism ranking and drug-candidate ranking. Co-Scientist's "idea tournament" is the same pattern.

**Why:** Numeric scoring from LLMs is unreliable across candidates (the same model rates the same item differently depending on context). Pairwise comparison is a much more stable judgment task. Tournament ranking aggregates the comparisons into a defensible ordering.

**Where it applies in OE:**

- **comp-032 (and follow-ups) pharmacological-chaperone candidate ranking** — currently the comp-032 output ranks candidates by composite score. Re-ranking with pairwise tournament would tighten the top-3 vs top-10 boundary that drives wet-lab spend on the ABCG2 Q141K trafficking assay.
- **Synthesis-queue triage** — `walk-synthesis` currently walks items in arrival order. A pre-pass that pairwise-ranks queue items by leverage (defined: blocks-most-downstream-work × tractability × cost) would let the walk happen in leverage order.
- **Any future multi-candidate evaluation step** in comp-NNN experiments where the analysis surfaces a ranked list (drug candidates, strain variants, formulation conditions, etc.).

**Cost:** O(N²) pairwise calls, or O(N log N) for Swiss-style. For N=30 candidates and ~$0.10/comparison, full pairwise is $90 — acceptable for items that drive wet-lab spend, overkill for a 5-item triage.

**Engineering footprint:** A pairwise-judge prompt template and an Elo aggregator. Two-day build.

### Pattern 3 — Concise / deep lit-search tier split

**What:** Robin uses two literature-search agents: Crow (concise reports, ~$4.33/call) for triage and Falcon (deep reports, ~$6.43/call) for committed candidates. The split is just budget discipline made architectural.

**Why:** Without an explicit tier split, every literature query gets either over-served (deep search on triage items) or under-served (concise search on committed items). Making the tier explicit lets you put per-call cost ceilings on each.

**Where it applies in OE:**

- **Phase 2 subagent runs across the four peer-track scope pages** (per [operations/todos.md](./todos.md) standing item) — these are currently a single "go research X" prompt class. Splitting into Crow-tier (triage scan, 10-20 papers, half-page summary) and Falcon-tier (deep evaluation, 50+ papers, full mechanism + limitations report) lets the triage runs happen at sweep cadence and the deep runs happen on committed items only.
- **Subagent calls in `new-comp-experiment` workflow** — currently the skill describes "subagent peer review" as a single class. The Crow/Falcon split argues for a triage subagent (catches obvious gaps) feeding a deep subagent (full critique on items that pass triage).
- **Already-implicit in `walk-synthesis`** — the CTO-not-PhD framing in the skill is functionally a Crow-tier triage. Making it explicit in the doc would let it be tuned.

**Cost:** Same total budget, smarter allocation. The discipline saves money on items that don't need deep search and gives more budget to items that do.

**Engineering footprint:** A prompt-template split and a routing rule. Half-day build.

### Pattern 4 — Full Robin-cycle methodology (the disease→mechanism→assay→candidate funnel)

**What:** A four-stage closed-loop cycle:

1. **General questions about the problem** → Crow-tier literature reports
2. **Causal mechanisms** ranked via pairwise tournament → top mechanism + suggested assay
3. **Drug/intervention candidates** for the chosen assay, ranked via pairwise tournament → top N for testing
4. **Iteration** — wet-lab results fed back as analysis input; round 2 hypothesis generation

Robin demonstrated this end-to-end on dry AMD: "dry age-related macular degeneration" → enhance RPE phagocytosis → 30 candidates → ripasudil + KL001 → ABCA1 mechanism story.

**Why:** This is the full agentic-discovery pattern. The other three patterns are units that compose into it.

**Where it applies in OE:**

- **Any peer-track scope page reaching Phase 2 maturity** — TCM × rigor track, engineered LBP track, siRNA URAT1 track, medicinal-mushroom-complement track. Each is currently a hand-curated landscape map. Running a Robin-cycle on each would surface (or fail to surface) candidates that the human curation missed.
- **comp-038 (this PR's first instance)** — a single-purpose Robin-cycle focused on assay-method discovery rather than therapeutic candidates. Same architecture, different output type.
- **Future chassis-pending interventions** — the [`chassis-pending-interventions.md`](../wiki/chassis-pending-interventions.md) page exists; a Robin-cycle on each entry would surface candidate chassis the human curation missed.

**Cost:** ~$10-20/cycle at Robin's published configuration. Cheap enough to run as a default first step on any committed track.

**Engineering footprint:** For comp-038, start with a lightweight OE-native runner rather than adopting Aviary up front. When Codex runs it locally, Codex performs the GPT-5.5 synthesis / judge role from a committed source packet; OpenRouter is reserved for explicit external-vendor roles such as DeepSeek query critique, Opus review, or two-model translation. Revisit Aviary only if repeated agentic-search comps create enough orchestration burden to justify a framework.

## Tooling adoption decisions

Four explicit decisions. Each names go / no-go / wait + revisit-trigger.

### 1. Fork Aviary for OE's first Robin-cycle? **No for comp-038; revisit after validation.**

- **What:** FutureHouse open-sourced the Aviary framework that Robin uses. Forking-and-modifying is faster than rebuilding the multi-agent orchestration from scratch.
- **Decision:** Do **not** use Aviary for comp-038. Use a small OE-native runner that preserves the methodological primitives without framework adoption. Default local path: fetch source snapshots, write a Codex packet, and have the current Codex/GPT-5.5 session perform N=5 synthesis trajectories and source-evidence gating. Optional paid path: use OpenRouter only when a second vendor is intentionally needed.
- **Risk:** A custom runner may underbuild retrieval ergonomics compared with PaperQA2 / Aviary, especially for full-text acquisition and citation-graph traversal.
- **Revisit trigger:** comp-038 completion. If the OE-native runner spends too much effort on generic orchestration or retrieval plumbing, revisit Aviary / PaperQA2 for the next agentic-literature-synthesis comp.

### 2. Benchmark Gemini 3 Deep Think on enzyme/mechanism reasoning? **Yes, scheduled as separate eval.**

- **What:** Google's claim is gold-medal performance on the 2025 Physics and Chemistry Olympiad written sections. If true for the *kinds of reasoning OE uses* — enzyme transition states, cofactor geometry, mechanism inference from structural and biochemical priors — Deep Think becomes the right model for the mechanism-interpretation step in any comp-NNN.
- **Decision:** Run a blind comparison on 3-5 mechanism-reasoning questions where we already have strong priors. Candidates: lactoferrin apo-vs-holo iron-saturation effects, kojic acid × NLRP3 binding mode plausibility, Houttuynia polysaccharide complement-modulation mechanism. Models: Claude Opus 4.7, Claude Sonnet 4.6, OpenAI o4-mini, Gemini Deep Think. Score blind by Brian (and ideally one outside reviewer).
- **Cost:** ~$50-100 in API spend + a half-day human review.
- **Decision criterion:** If Deep Think wins or ties on >=3 of 5, swap it into the comp-NNN mechanism-interpretation step. If it loses badly, document the result and stay with the current stack.
- **Revisit trigger:** Whenever a new frontier model lands (Claude/OpenAI/Google) on a reasoning-benchmark claim; re-run the same 5 prompts.

### 3. Adopt Science Skills / Antigravity for biological-data plumbing? **No, wait and revisit Q3 2026.**

- **What:** Google is bundling 30+ life-sci databases (UniProt, PDB, BRENDA, Reactome, etc.) as Antigravity skills. If this ships with broad coverage and reasonable query semantics, it removes the need for OE to build bespoke database integrations.
- **Decision:** **Don't build** OE-specific UniProt / PDB / ChEMBL plumbing in the meantime. The OE thesis depends on integration of these data sources, but the integration layer is not a structural advantage — it's commodity infrastructure that Google is about to ship.
- **Exception:** OE-specific data sources NOT in those 30 databases (CNKI / J-STAGE / KISS Korean literature corpora, ChiCTR trial registry, NBRC strain catalog, specific Aspergillus oryzae genomics resources) DO remain build-targets. Those are the structural data advantage; build them now.
- **Revisit trigger:** Q3 2026 (Antigravity Science Skills GA release), OR earlier if a specific OE comp-NNN is blocked on a missing database integration.

### 4. Adopt AlphaEvolve-style code-variant generation in comp-NNN? **No, defer indefinitely.**

- **What:** AlphaEvolve generates and scores thousands of code variations in parallel. Useful for combinatorial optimization, less obviously useful for OE's comp-NNN scope (where analyses are mostly single-script structural/sequence work).
- **Decision:** Defer. No current OE comp-NNN is the right shape for AlphaEvolve's approach. If a future analysis becomes one (e.g., systematic strain-engineering combinatorics, large-scale formulation-condition search), revisit.
- **Revisit trigger:** Any future comp-NNN proposal that explicitly involves combinatorial search over scripts or parameter spaces.

## Process changes to comp-NNN methodology

Three proposed extensions to [`.claude/skills/new-comp-experiment/SKILL.md`](../.claude/skills/new-comp-experiment/SKILL.md). Each is small.

### Extension 1 — Add agentic-literature-synthesis as a comp-NNN sub-type

The current skill explicitly EXCLUDES literary synthesis: *"Question is purely literary synthesis (writing a wiki page) | No"*. This rule pre-dates the Robin pattern.

A Robin-style literature synthesis is NOT "purely literary" in the original sense — it's:

- **Reproducible** (query strategy + sources + model + temperature documented per the existing comp-NNN provenance discipline)
- **Parameterized** (search depth, candidate pool size, tournament rounds are all explicit knobs)
- **Consensus-ranked** (N-trajectory consensus is part of the artifact, not a one-shot LLM judgment)
- **Structured-output** (the artifact is a ranked candidate list with per-candidate justification, not a narrative wiki page)

Proposed extension: add a sub-type to the skill's "When to use" table:

| Situation | Use? | Sub-type |
|---|---|---|
| Brian asks "could we model this computationally?" | Yes | structural / sequence |
| Wet-lab experiment has open structural/sequence question | Yes | structural / sequence |
| New protein target needs initial protease/stability assessment | Yes | structural / sequence |
| Question is **agentic literature synthesis** with structured ranked output | Yes | **agentic-literature-synthesis** |
| Question requires live cells, fermentation dynamics, in vivo readouts | No — needs wet-lab | — |
| Question is **purely narrative** literary synthesis (writing a wiki page) | No | — |

The distinction between agentic-literature-synthesis and "purely narrative" lit synthesis is: does the output have structured ranked candidates with reproducible methodology? If yes, comp-NNN. If no, it's a wiki page.

### Extension 2 — Add N-trajectory consensus as an optional methodology knob

Add to skill Step 3 ("Write the analysis"): for any LLM-driven analysis step where the methodology choice is subjective, run N trajectories with consensus selection. Default N=5 for lit synthesis, N=8 for analysis runs that drive wet-lab spend.

Document the consensus methodology in the experiment's README. Report consensus statistics in `outputs/summary.md` ("identified in K of N trajectories").

### Extension 3 — Replace single-pass numeric scoring with pairwise-tournament ranking

Add to skill Step 3: where the analysis produces a ranked list of candidates (drugs, mechanisms, strains, conditions), prefer pairwise-tournament ranking over single-pass numeric scoring. Document the tournament structure (full pairwise vs Swiss) and the judge model used.

For N <= 6 candidates: full pairwise (15 comparisons). For N > 6: Swiss-style (each candidate gets log₂(N) comparisons), or sample-and-tournament hybrid.

## First validation instance: comp-038

**Question:** Is there a Tier 2 butyrate quantification assay (colorimetric, enzymatic, or breath-hydrogen proxy) that can be validated against Tier 3 GC-MS to close the microbiome-metabolite quantification gap?

**Why this question:** Already named in [synthesis queue open-question-2](../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md) and [synthesis queue connection-5](../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md) — both Pass-3 confirmed as "prioritize, $0 desk audit before wet-lab investment." The gap blocks every microbiome-derived intervention downstream (engineered LBP butyrate-boost, bile-acid modulators, indole-based AhR agonists). It's pure literature synthesis. It's the cleanest possible test of the Robin-cycle methodology against OE's actual stuck list.

**Sub-type:** agentic-literature-synthesis (proposed comp-NNN extension above)

**Scaffold:** [`wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/)

**Status:** Runner scaffolded and run in this PR (`analyze.py`, shared `agentic_lit_synthesis.py`, inputs/ + committed outputs). The completed comp-038 pass used Codex synthesis from `outputs/codex-synthesis-packet.md` and made no OpenRouter model calls.

**Methodology questions to resolve before running:**

1. Does `analyze.py` for an agentic-search experiment fit the existing comp-NNN stdlib-only constraint? Yes at the dependency layer: the comp-038 runner uses only Python stdlib plus shared OE helpers. The default live path fetches source snapshots and writes a Codex synthesis packet with no model API calls. The explicit `--run-openrouter` path can call external models over HTTPS, so reproducibility for that path is achieved via committed query-strategy.json + model-config.json + response IDs + dated snapshots rather than deterministic local computation.

2. What's the consensus methodology? Implemented: N=5 Codex/GPT-5.5 in-session synthesis trajectories over the committed PubMed snapshot and query plan; consensus-style collapse on Tier 2 candidate assays; source-evidence gating prevents GREEN verdicts from PubMed abstracts alone. DeepSeek / Opus roles remain optional external checks when the cost is justified.

3. What's the budget ceiling? Default Codex-run path: $0 incremental OpenRouter spend. Optional `--run-openrouter` path: $25 ceiling. Robin's published per-cycle cost ($10.76) is the precedent for paid external runs, not a reason to spend when the local Codex subscription can do the synthesis seat.

**Decision criterion for the methodology test:** If comp-038 produces a defensible Tier 2 assay recommendation without unnecessary model spend, in under 90 minutes wall clock, with source snapshots and consensus-style reasoning that any reader can audit — the agentic-literature-synthesis sub-type is adopted as a candidate OE comp-NNN pattern. If it fails any of those, document the failure mode and decide whether to iterate or abandon the sub-type.

## Open evaluation experiments

Two evals that aren't comp-NNN instances but inform OE platform decisions. Park in [`operations/todos.md`](./todos.md) on PR merge.

### Eval 1 — Gemini Deep Think mechanism-reasoning bench

Described in Tooling Decision #2 above. Concrete steps:

1. Pick 5 OE mechanism-reasoning questions where we have strong prior beliefs (suggested: lactoferrin apo-vs-holo, kojic acid × NLRP3, Houttuynia polysaccharide complement modulation, koji-acid ABCG2 interaction, Y402H CFH × dietary polyphenol mechanism).
2. Run each through Claude Opus 4.7, Claude Sonnet 4.6, o4-mini, Gemini 3 Deep Think, with identical prompts.
3. Blind-score each response on (a) mechanistic accuracy, (b) limitation honesty, (c) novel-link surfacing.
4. Threshold: Deep Think wins/ties on >=3 of 5 → adopt as comp-NNN mechanism-interpretation default.

Estimated cost: $50-100 + half-day Brian time (+ optional external reviewer).

### Eval 2 — OE-native runner vs Aviary fit

During comp-038 run, log:

- Did the OE-native runner spend too much code on generic orchestration / retrieval plumbing that Aviary or PaperQA2 would already solve?
- Did the cost-aware role split work as config: Codex/GPT-5.5 in-session by default, OpenRouter only for explicit external-vendor checks?
- Where did the orchestration friction show up? (full-text retrieval, consensus aggregation, pairwise ranking, output formatting)

Deliverable: a comp-038 retrospective section in the README documenting whether to keep the OE-native runner or adopt Aviary / PaperQA2 for the next agentic-literature-synthesis comp.

## What this is NOT

Honest delineation, in the spirit of operations/README.md's "caveats are the recruiting angle" rule:

- **Not a claim that Robin/Gemini-for-Science replace wet lab.** Robin's own paper is honest: humans selected 5 of 30 candidates to test, swapped pHrodo beads for ROS, used ARPE-19 instead of suggested primary cells, ran the LDH cytotoxicity assay. "Semi-autonomous" is the right framing. The pattern shifts priors and triages. It doesn't run experiments.
- **Not a claim that OE's stuck list dissolves under agentic search.** Some items genuinely need wet lab (SGF protein stability under actual shio-koji conditions; ABCG2 Q141K trafficking assay in real cells). The reflection at [`../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md) names which items are eligible for re-classification and which aren't.
- **Not a blanket methodology victory from one run.** The proposed comp-NNN sub-type extension remains provisional after comp-038. If follow-up review finds the recommendation weak, or if future instances burn budget without converging, the extension does not land as standard practice.
- **Not a claim that any one of these models is "better."** The Deep Think bench is the empirical question. Until that runs, no model claim in this document is load-bearing.
- **Not a commitment to fork Aviary.** comp-038 deliberately starts with an OE-native runner. If that runner proves brittle or spends too much effort on generic retrieval/orchestration, Aviary / PaperQA2 gets revisited for the next cycle.

## Cross-references

- [`../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md`](../synthesis/strategic-reflections/2026-05-20-agentic-science-methodology.md) — sister strategic reflection; names the six OE stuck items eligible for re-classification
- [`../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/) — first validation instance scaffold
- [`./README.md`](./README.md) — operations folder framing
- [`./operational-search-template.md`](./operational-search-template.md) — sister operations doc class (resource-acquisition bottlenecks). This doc is the methodology-adoption analog.
- [`../.claude/skills/new-comp-experiment/SKILL.md`](../.claude/skills/new-comp-experiment/SKILL.md) — the skill this doc proposes extending
- [`../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md`](../synthesis/queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md) — the queue item that comp-038 addresses
- [`../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md`](../synthesis/queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md) — the platform-level framing of the same gap
- [`../synthesis/queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md`](../synthesis/queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md) — N-trajectory consensus pattern target

## Provenance

Drafted 2026-05-20 in response to Brian's review of the Robin paper (Ghareeb et al., Nature 2026, accepted 2026-05-12) and the Gemini for Science announcement (Google I/O 2026-05-19). The full conversation surfaced (a) the methodology patterns worth adopting and (b) the OE-specific stuck items potentially eligible for re-classification. This doc captures (a); the strategic reflection captures (b). comp-038 is the first instance.
