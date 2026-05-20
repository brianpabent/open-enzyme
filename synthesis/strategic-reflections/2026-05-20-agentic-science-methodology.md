---
title: "Agentic science methodology — Robin and Gemini-for-Science as platform unlock for OE's literature-bound chokepoints"
status: open
created: 2026-05-20
class: strategic-reflection
related:
  - ../../operations/agentic-science-adoption.md
  - ../queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md
  - ../queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md
  - ../queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md
  - ../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/
sources:
  - "Ghareeb et al. 2026 (Nature) — Robin: A multi-agent system for automating scientific discovery — doi:10.1038/s41586-026-10652-y"
  - "Google 2026-05 — Gemini for Science (I/O 2026) — blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/"
---

# Agentic science methodology — Robin and Gemini-for-Science as platform unlock for OE's literature-bound chokepoints

## Reflection

Two independent groups (FutureHouse / Robin in Nature 2026; Google DeepMind / Gemini for Science at I/O 2026) shipped converging multi-agent architectures for literature-grounded scientific discovery within a week of each other. The Robin paper demonstrated a closed-loop cycle that, given just the disease name "dry age-related macular degeneration," surfaced **ripasudil** (a clinically-approved ROCK inhibitor never proposed for dAMD) plus a genuinely novel ABCA1-lipid-efflux mechanism story. Cost per full cycle: $10.76. Time: ~30 min.

The operations-layer captures (methodology + tooling + comp-NNN extension) live at [`operations/agentic-science-adoption.md`](../../operations/agentic-science-adoption.md). This reflection is the *epistemic* companion — what changes about how OE evaluates its own "stuck" list.

**The reframe:** Many of OE's currently "wet-lab-gated" items are not actually wet-lab gated. They're *literature-synthesis bound* — the answer plausibly exists in the published literature (sometimes in non-English-indexed corpora; sometimes across silos that no human reader connects), waiting to be retrieved and ranked. Robin's whole thesis is exactly this — the dabrafenib / ketamine / leucovorin / KarXT delay-between-insight-and-application pattern in the intro.

The discipline question this reflection raises: **which items on OE's stuck list get re-classified from "wet-lab gated" to "agentic-search candidate"?** Each re-classification is a real decision — the wet-lab budget gets reallocated, the timeline gets re-projected, the chassis-pending-interventions analysis gets updated.

Getting the re-classification right is the entire point of this reflection. Re-classifying everything is wrong (the SGF survival of engineered proteins under actual shio-koji conditions genuinely needs wet lab). Re-classifying nothing is also wrong (Tier 2 butyrate assay discovery is pure literature synthesis with a structured-output ask).

## What this reflection does NOT argue

- **Not "agentic search replaces wet lab."** Robin's own paper is explicit: "semi-autonomous" is the honest abstract framing; "first AI system to autonomously discover" in the conclusion is overclaim. Humans selected 5 of 30 candidates to test, swapped reagents, picked the cell line, ran the cytotoxicity assay. The pattern shifts priors and triages. It doesn't run experiments.
- **Not "every stuck item is agentic-search-eligible."** Wet-lab work that requires actual cells, actual fermentation conditions, actual in-vivo response — those don't move. The shio-koji protease-stability question for engineered uricase / lactoferrin under genuine 7-14-day high-salt conditions is wet-lab. The SGF survival test is wet-lab. The ABCG2 Q141K trafficking assay in epithelial transwells is wet-lab.
- **Not "comp-NNN replaces all the above wet-lab work."** Computational priors before wet lab is the existing OE thesis ([`open-source-platform.md`](../../wiki/open-source-platform.md) Platform Principles). The reflection adds a *sub-type* of comp-NNN (agentic-literature-synthesis) for the items where the prior IS the literature itself, not a structural simulation. Both sub-types continue to inform — not replace — wet lab.
- **Not "adopt FutureHouse/Google's exact stack."** The methodology patterns (N-trajectory consensus, pairwise tournament, concise/deep tier split, full Robin-cycle) are independently adoptable. Aviary fork is conditional on comp-038 fit. Deep Think is conditional on the mechanism-reasoning bench. The stack is reviewed; the patterns are adopted.

## Six unstick candidates — proposed re-classifications

For each: the current OE classification, the proposed re-classification, the rationale, the proposed methodology, the estimated cost, and the prerequisite ("what needs to be true before this gets run").

These are **proposals**, not decisions. Brian reviews and signs off per item, or sends back to the queue.

### 1. Tier 2 butyrate assay discovery — **re-class: agentic-search**

- **Currently:** Listed as $0 desk audit in [synthesis queue open-question-2](../queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md); Pass 3 confirmed prioritize. Blocks every microbiome-derived intervention downstream.
- **Proposed:** comp-038, agentic-literature-synthesis sub-type, Aviary-fork OR Claude+PaperQA2 stack, N=5 trajectories, pairwise-tournament ranking of candidate assays against Tier 3 GC-MS validation criteria.
- **Rationale:** Pure literature task. Cleanest possible test of the Robin-cycle methodology. Already named as $0 desk audit; we're just making the audit reproducible and structured.
- **Cost:** $25 ceiling per `operations/agentic-science-adoption.md` #comp-038 scaffold. Wall clock <90 min.
- **Prerequisite:** Methodology review of the comp-038 scaffold in this PR; analyze.py written after Aviary-fit decision. (This PR.)

### 2. East Asian Q141K × dietary-fiber RCT gap — **re-class: agentic-search**

- **Currently:** [synthesis queue connection-1](../queue/2026-05-20-connection-1-cfh-y402h-rs1061170-the-most-common-complement.md) and adjacent items. Q141K is ~30% allele frequency in East Asian general population, ~50% in gout patients. The obvious population-stratified fiber/butyrate RCT has not been designed.
- **Proposed:** A Crow/Falcon-tier split agentic-search across CNKI + J-STAGE + KISS (NOT just PubMed), classical formula corpora (per the [comp-NNN query-framing discipline](../../.claude/skills/new-comp-experiment/SKILL.md) for natural-product scans), and ChiCTR / J-RCT trial registries. Goal: does the RCT exist already in non-English-indexed sources, OR does the gap genuinely exist?
- **Rationale:** This is the dabrafenib-pattern par excellence — published insight may already exist, indexed in corpora OE has not yet scanned.
- **Cost:** ~$20-30 (Crow-tier triage scan + Falcon-tier deep on the most promising 3-5 papers). Wall clock ~2 hours.
- **Prerequisite:** comp-038 methodology validated. Decision on whether agentic-literature-synthesis sub-type lands as standard.

### 3. Kojic acid × NLRP3 binding-mode plausibility — **re-class: agentic-search → docking prior**

- **Currently:** [`wiki/aspergillus-oryzae.md`](../../wiki/aspergillus-oryzae.md) + `wiki/nlrp3-inhibitor-screen.md`. *A. oryzae* natively produces 3-5 g/L kojic acid; documented NF-κB suppression; direct NLRP3 inflammasome activity unpublished.
- **Proposed:** Two-stage. Stage 1: agentic literature search for any direct NLRP3 evidence (positive OR null result) for kojic acid OR structurally adjacent γ-pyranones. Stage 2 (if Stage 1 returns no clear result): structural comp-NNN — dock kojic acid + reference NLRP3 ligands against NACHT domain + downstream conformational consequences. Pairwise-tournament ranking of binding-mode plausibility across N trajectories.
- **Rationale:** If kojic acid shows credible NLRP3 binding, koji reframes from "single-enzyme chassis" to "multi-compound platform" — and OE's strategic narrative gets stronger without wet-lab spend. **This is the highest strategic-narrative leverage move on the list.**
- **Cost:** Stage 1 ~$15. Stage 2 (if needed) ~$30 (structural comp-NNN with N=8 trajectory consensus).
- **Prerequisite:** comp-038 methodology validated; Stage 1 results inform whether Stage 2 runs.

### 4. comp-032 chaperone-orthogonal stacking re-rank — **re-class: pattern-application within existing comp-NNN**

- **Currently:** [synthesis queue riskiest-assumption-1](../queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md). Framework's coefficients rest on expert-estimate values; not large-scale empirical datasets.
- **Proposed:** Re-rank comp-032's pharmacological-chaperone candidates with (a) N=8 trajectory consensus to surface coefficient-robust vs coefficient-fragile rankings, (b) pairwise-tournament ranking replacing the existing composite-score approach. Output: tighter top-3 boundary that justifies the wet-lab ABCG2 Q141K trafficking assay spend.
- **Rationale:** Sharpens existing comp-NNN output without methodology innovation; cheap to run; saves wet-lab dollars by reducing top-N from 10 to 3.
- **Cost:** ~$50 (pairwise tournament for ~10 candidates × 8 trajectories at ~$0.10/comparison).
- **Prerequisite:** N-trajectory consensus pattern adopted (operations doc Pattern 1).

### 5. Shio-koji protease-stability MD consensus — **re-class: structural comp-NNN with N-trajectory consensus**

- **Currently:** [`wiki/koji-construct-design.md`](../../wiki/koji-construct-design.md) §6. Critical open question: does the 7-14 day high-salt room-temperature fermentation of shio-koji degrade engineered uricase and lactoferrin? Currently flagged for wet-lab SGF survival test (comp-001 + comp-005 provide structural priors).
- **Proposed:** Extend the existing comp-001 / comp-005 protease-stability work with N=8 trajectory MD consensus across the protease ensemble (KEX2, ALP, neutral protease I, neutral protease II, etc.) and the high-salt + low-temperature condition factors. Output: per-payload (uricase, lactoferrin, future cassette additions) "secrete vs intracellular-protected" recommendation with consensus confidence.
- **Rationale:** Doesn't replace the wet-lab SGF assay, but sharpens the prior before wet-lab spend. The construct-design decision (Koji-S secreted default vs Koji-I intracellular protected) currently has high consequence and low confidence; consensus tightens that.
- **Cost:** Roughly N× the existing comp-001 / comp-005 cost (depends on MD setup; if structural-MD this is compute-bound, if pLDDT-and-accessibility this is cheap).
- **Prerequisite:** N-trajectory consensus pattern adopted; comp-001 / comp-005 methodology readout that confirms the trajectory-consensus pattern fits structural analyses (not just LLM analyses).

### 6. Houttuynia cordata polysaccharide mechanism — **re-class: agentic-search → THP-1 wet-lab confirmation**

- **Currently:** [synthesis queue connection-6](../queue/2026-05-20-connection-6-the-houttuynia-cordata-polysaccharide-hcp-hcpm-represents.md) and [synthesis queue experiment-2](../queue/2026-05-20-experiment-2-msustimulated-thp1-macrophage-assay-of-houttuynia-cordata.md). Strong in-vivo complement C5a correlation (survey data); molecular mechanism unvalidated. Proposed THP-1 macrophage assay queued.
- **Proposed:** Run an agentic-search pre-step before the THP-1 assay. Goal: surface any documented direct-binding partner or signaling pathway for Houttuynia cordata polysaccharide (HCP) or HCPm, especially in non-English literature. If a binding partner is documented, the THP-1 assay gets a directed hypothesis (test IL-1β + the specific candidate pathway). If not, the THP-1 assay stays as the discovery vehicle.
- **Rationale:** The wet-lab assay still runs; the agentic search sharpens what to look for. "Did anyone publish a mechanism in CNKI / J-STAGE that PubMed didn't index?" is exactly the dabrafenib-pattern.
- **Cost:** ~$15 (Crow-tier scan plus Falcon-tier deep on 2-3 candidate mechanisms).
- **Prerequisite:** comp-038 methodology validated; CNKI/J-STAGE search-capability proven (per #2 above).

## What's still open — Brian decisions needed

This reflection surfaces six re-classification proposals. The reflection does not decide any of them. Each item needs Brian's review against:

1. **Is the proposed re-classification right?** Or does the item genuinely need wet-lab as its first move, not agentic search?
2. **Is the proposed methodology right?** Or is there a sharper way to ask the question?
3. **Is the cost ceiling right?** Or should the budget be tighter / looser?
4. **What order do they run in?** Item 1 (comp-038) is the methodology test and must go first. Items 2-6 are conditional on comp-038 succeeding. Order within 2-6 is open — by leverage? by tractability? by readiness?

Reflection stays *open* until comp-038 returns its readout AND Brian decides which of items 2-6 to commit to. On commit, this reflection moves to `_resolved/` per the synthesis/strategic-reflections/README.md flow, with a `## Resolution outcome` appended documenting the decisions made.

## Trigger

Already triggered. Two announcements (Robin Nature paper + Gemini for Science I/O announcement) landed within a week of each other and were brought into OE conversation 2026-05-20. The methodology gap and the eligibility of OE's literature-bound items for re-classification are both immediate.

No accumulation needed before acting; the first instance (comp-038) is scaffolded in the same commit batch as this reflection.

## Outcome

Four artifacts land in the same commit batch as this reflection:

1. **This file** — the strategic reflection capturing the six unstick proposals.
2. **[`../../operations/agentic-science-adoption.md`](../../operations/agentic-science-adoption.md)** — the operations-layer methodology and tooling captures.
3. **[`../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/)** — first validation instance scaffold (analyze.py + run deferred).
4. **(deferred to follow-up PR after methodology review)** — updates to `operations/README.md` index, `operations/todos.md` action items, `wiki/computational-experiments.md` Planned Analyses table, and `.claude/skills/new-comp-experiment/SKILL.md` sub-type extension.

Resolution requires:

- comp-038 runs and produces a readout (success or failure mode documented).
- Brian reviews the six unstick proposals (this file's main content) and signs off / sends back / re-orders per item.
- The methodology decisions in operations doc are committed (Aviary fork yes/no; Deep Think bench scheduled; Science Skills wait/no-wait; AlphaEvolve defer/adopt) or revised.

## Cross-reference

- Origin conversation: 2026-05-20. Brian shared the Robin paper PDF (`s4158602610652y_reference.pdf`) and the Gemini for Science I/O 2026 blog post; the conversation surfaced the methodology patterns + OE-specific unstick eligibility. Specific framing: *"in OE, any of the open questions and anything gated by wet lab is stuck"* → the diagnostic walkthrough → the six unstick proposals.
- Sister operations doc: [`../../operations/agentic-science-adoption.md`](../../operations/agentic-science-adoption.md). This reflection captures the *what* (which items get re-classed); the operations doc captures the *how* (methodology, tooling, comp-NNN extension).
- First validation instance: [`../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/`](../../wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit/).
- Open-question source items (daemon-emitted, Pass-3 confirmed): [open-question-2](../queue/2026-05-20-open-question-2-is-there-a-tier2-butyrate-assay-colorimetric-enzymatic-or.md), [connection-5](../queue/2026-05-20-connection-5-the-tier2-butyrate-assay-gap-identified-in-the.md), [riskiest-assumption-1](../queue/2026-05-20-riskiest-assumption-1-the-chaperoneorthogonal-stacking-frameworks-coefficients.md), [connection-6](../queue/2026-05-20-connection-6-the-houttuynia-cordata-polysaccharide-hcp-hcpm-represents.md), [experiment-2](../queue/2026-05-20-experiment-2-msustimulated-thp1-macrophage-assay-of-houttuynia-cordata.md).
- Sister strategic reflection on workflow discipline: [`2026-05-15-chassis-is-downstream-of-chokepoint.md`](./2026-05-15-chassis-is-downstream-of-chokepoint.md). That reflection introduced the chassis-pending re-classification framework; this one introduces the agentic-search re-classification framework. Both are discipline reflections (operationalize an existing platform stance) rather than content reflections (require substance accumulation).
