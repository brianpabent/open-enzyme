---
title: Autonomous AI Screening Methodology — Lessons from ClockBase Agent for Comp-NNN
date: 2026-05-07
tags: [methodology, ai-driven-discovery, comp-NNN, peer-track, prior-art, rigor-discipline]
related:
  - computational-experiments.md
  - manual-literature-mining.md
  - linter-design.md
  - ai-bio-tools-playbook.md
  - chaperone-orthogonal-stacking.md
  - open-source-platform.md
sources:
  - "Ying K, Tyshkovskiy A, Gladyshev VN et al. Autonomous AI Agents Discover Aging Interventions from Millions of Molecular Profiles. bioRxiv 2023.02.28.530532v3 (current version posted late 2025 / early 2026)"
  - "PMC ID PMC12667862; PubMed PMID 41332661"
  - "ClockBase platform: https://www.clockbase.org/"
  - "Lifespan.io coverage (paraphrased '43,529'; abstract reports 43,602)"
  - "Avinasi Labs co-founder thread: https://x.com/avinasilabs/status/1999509383068385504"
---

# Autonomous AI Screening Methodology

**Peer-track methodology page.** This is not a gout target. It documents external prior art on autonomous AI-driven biomedical screening that informs how Open Enzyme should design its own comp-NNN computational pipeline. Methodology mirror, not therapeutic candidate.

## Why this is on the wiki

A May 2026 social-media post claimed: *"AI tested 43,529 longevity interventions and validated the top candidate in aged mice without a single human researcher making the call."* On its face, this is exactly the comp-NNN pattern Open Enzyme is building toward: large search-space ranking → top candidate → wet-lab validation. If that pattern works at the scale + autonomy claimed, it's directly transferable to ranking strain-engineering candidates (codon optimization × signal peptide × promoter × secretion scaffold combinations).

But "transferable" requires identifying what the actual paper says vs. what the social-media compression claimed. This page does that work.

## Identification

- **Paper:** Ying K, Tyshkovskiy A, Gladyshev VN et al. *Autonomous AI Agents Discover Aging Interventions from Millions of Molecular Profiles.*
- **Venue:** bioRxiv 2023.02.28.530532 — v1 was a 2023 ClockBase platform paper; **v3 with the agentic-discovery + ouabain validation contribution was posted late 2025 / early 2026**.
- **PMC:** PMC12667862. **PubMed:** PMID 41332661.
- **Affiliations:** Brigham and Women's / Harvard Medical School; co-authors at Stanford Med, Broad Institute, Genentech; co-founder Kejun Ying also at Avinasi Labs.
- **System name:** ClockBase Agent (Avinasi Labs co-developed).

**Number-fingerprint reconciliation:** the social-media "43,529" is a paraphrase of the paper's abstract figure of **43,602 intervention–control comparisons** drawn from 13,211 mouse RNA-seq studies. Lay coverage (Lifespan.io, NAD.com) consistently reports "43,529" — almost certainly a journalistic paraphrase. **Cite 43,602 (paper abstract), not 43,529 (lay coverage).**

**Verification status (per [CLAUDE.md §4](../CLAUDE.md) pre-commit grep-verify gate):** the bioRxiv PDF returned 403 from the agent research environment, so cohort sizes, exact dosing, blinding protocol, and statistical correction methods have NOT been verified against primary supplementary methods. Numbers in this page are sourced from the paper abstract + lay coverage. **Treat as preliminary until full supplementary methods are retrieved locally.** Specific load-bearing items flagged inline below.

## Methodology essentials

### Search space
- **43,602 intervention–control comparisons** (paper abstract; verified) drawn from **13,211 public mouse RNA-seq studies** (plus methylation data); >2 million total human + mouse molecular profiles ingested.
- Interventions span genetic perturbations, diseases, pharmacological compounds, and environmental conditions — **not a curated compound library**, but everything experimentalists ever uploaded to GEO / SRA.
- **Insight:** the win came from being **exhaustive over existing data** rather than **generative over new chemical space**. They didn't generate new candidates; they ranked across existing data nobody else had aggregated.

### Ranking
- **Multi-agent LLM system.** Specialized sub-agents for metadata parsing, hypothesis generation, statistical method selection, literature review, scientific report generation. Architecture not fully specified in the public materials. [VERIFY: which LLM(s); orchestration framework; prompt templates.]
- **Composite scoring across >40 aging clocks** (epigenetic + transcriptomic), not a single biomarker.
- **Hypothesis-then-verify loop.** LLM generates a hypothesis from data, second pass verifies it against raw data + literature before it enters the shortlist. Explicit two-step pattern, not single-shot generation.

### Validation
- **20-month-old C57BL/6 (Black 6) mice**, intermittent ouabain dosing for **~3 months**, replicating the protocol of the original GEO study the AI flagged. [VERIFY: cohort sizes per group; exact dosing schedule; blinding protocol.]
- **Endpoints:** frailty index progression, cognitive performance, fur condition, cardiac function, regional microglial neuroinflammation. **NOT lifespan.** Healthspan biomarkers only.
- **Top candidate:** ouabain (cardiac glycoside; previously known as a senolytic in some contexts). KMO inhibitor, fenofibrate, NF1 knockout also flagged in the top set.

### Autonomy boundary
- **AI autonomous over:** metadata parsing, hypothesis generation, composite-score ranking, report generation.
- **Human-disposed:** candidate selection from shortlist (humans picked ouabain), validation experimental design, mouse study execution, result interpretation.
- **The social-media framing is wrong.** This is *AI-proposes, human-disposes* — not closed-loop autonomous discovery (e.g., NOT a Coscientist-style autonomous lab). The tweet conflates "AI ranked 43k+ candidates without human curation" (true) with "AI validated in mice without humans" (not true).

## Transferable patterns for comp-NNN

### 1. Search-space sizing — exhaustive over existing data, not pre-pruned

ClockBase's win was being exhaustive over GEO / SRA, not curated. Analogous comp-NNN move: **enumerate the full combinatorial space upfront**, then rank — don't pre-prune to "reasonable" candidates.

For a single enzyme target (e.g., uricase) the combinatorial space is approximately:

> ~6 promoters × ~12 signal peptides × ~10 codon variants × ~60 secretion scaffolds ≈ **~43,200 combinations**

Tractable. Same order of magnitude as ClockBase's 43,602. Pre-pruning to the "obvious 50 candidates" is exactly the failure mode this methodology refutes.

### 2. Composite ranking across orthogonal predictors

The transferable pattern is **composite score across orthogonal models**, not any single model.

For comp-NNN: don't rank purely on AlphaFold confidence or purely on codon adaptation index. Combine ≥3 orthogonal scores:

- Folding stability (AlphaFold + ESMFold + Boltz-2 consensus)
- Secretion-pathway compatibility ([`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md))
- mRNA structure metrics (RNAfold accessibility, codon usage)
- Host-toxicity proxies (where applicable)

**Disagreement across orthogonal models = uncertainty signal.** This connects to the multi-vendor / multi-model heterogeneity discipline established in [CLAUDE.md §"Multi-model synthesis as guard against epistemic homogenization"](../CLAUDE.md) and [`open-source-platform.md`](./open-source-platform.md). ClockBase's >40 aging clocks is the same idea at scale.

### 3. Hypothesis-then-verify pattern (mirrors the pre-commit grep-verify gate)

ClockBase's two-pass pattern (hypothesis-generation agent → verification agent re-checking against raw data + literature) maps directly onto the pre-commit grep-verify discipline in [CLAUDE.md §4](../CLAUDE.md). They've operationalized the same discipline at the agent level.

**Comp-NNN implementation:** candidate-scoring agent produces a ranked shortlist; **independent verification agent** re-checks load-bearing numbers (residue indices, disulfide counts, predicted Tm, cleavage-site predictions) against primary databases (UniProt, ChEMBL, AlphaFold) before the candidate enters the wet-lab queue. The DAF SCR1-4 disulfide-count incident (2026-05-06) is the canonical case showing why this is needed — exactly what a verification-pass would have caught.

**Operational instantiation (comp-022, 2026-05-14):** The ClockBase exhaustive-search-then-rank pattern was instantiated at full cardinality for the first time in the OE corpus — 43,200 uricase cassette candidates enumerated, scored across 5 orthogonal models (CAI, ViennaRNA MFE, chaperone load, promoter×SP prior, ESM2 pseudo-pLDDT), with N-of-5 ≥ 4 concordance gate producing 71 promoted cassettes. The v1→v2 retrofit (adding real ViennaRNA MFE + ESM2 fold-quality proxy) confirmed the v1 top cluster at 100% survival. See [`uricase-cassette-ranking-computational.md`](./uricase-cassette-ranking-computational.md). (Mechanistic Extrapolation; source: uricase-cassette-ranking-computational.md)

### 4. Autonomy boundary = ranking, not validation

Useful prior: keep the AI on the **"produce ranked shortlist + provenance + composite score"** side of the boundary; humans (or an explicit gating ritual) make the wet-lab commit. Don't oversell autonomy.

This connects to the existing comp-NNN gating ritual: comp-NNN produces a verdict (LOW / MODERATE / HIGH / VERY HIGH risk + composite score + explicit limitations), and the human-driven §1.9 / §1.10 gating tests are the autonomy boundary. The shape is right; the discipline of explicitly naming the boundary is what's worth importing.

### 5. Computational-to-wet-lab handoff: N-of-M concordance

ClockBase's confidence calibration was **cohort-level concordance across many aging clocks** — if 30+ of 40 clocks agree, green light.

Translates to comp-NNN as: **require N-of-M concordance across orthogonal scoring models before promoting to wet lab.** For Open Enzyme: don't promote a strain-engineering candidate to wet-lab spend on a single high-confidence model output; require concordance across folding + secretion + codon + scaffold models. Concordance threshold is calibration-dependent (ClockBase ~30/40 = 75%; OE's smaller orthogonal-model set likely needs ~4/5 = 80% or higher).

## BioDesignBench evaluation-depth audit (added 2026-05-15)

Kim & Romero's BioDesignBench paper (bioRxiv 10.64898/2026.05.06.723381, verified 2026-05-15 — see [`bio-ai-tools.md` §BioDesignBench](./bio-ai-tools.md)) empirically validates the "deeper multi-metric evaluation" methodology this page advocates. The paper's central finding across 836 task–condition observations on 76 protein-design tasks: top LLM agents (DeepSeek V3, GPT-5) select appropriate tools but **evaluate candidate designs at only ~14% of expert intensity** and **never discard a generated candidate** across the entire benchmark. Forcing multi-metric evaluation (≥3 metric categories per candidate, compute-matched against shallow control) recovers DeepSeek V3 by +9.3 points (p = 0.002) and GPT-5 by +15.9 points (p < 0.001). The deterministic hardcoded pipeline (which already has multi-metric evaluation built into its workflow) gains nothing from the intervention — confirming the deficit is **specifically behavioral**, not generic compute.

This validates the N-of-M concordance methodology this page recommends (§5 above) and operationally instantiated in comp-022 (43,200 cassettes, 5 orthogonal scoring models, N-of-5 ≥ 4 gate, 71 promoted cassettes).

**Audit of OE's existing comp-NNN stack** against BioDesignBench's three failure-mode axes — (A) multiple candidates generated? (B) multi-metric evaluation across orthogonal scoring axes? (C) head-to-head comparison + filtering before termination?

| comp-NNN | Topic | (A) Multiple candidates? | (B) Multi-metric eval? | (C) Head-to-head + filter? | Audit verdict |
|---|---|---|---|---|---|
| comp-019 | Gut-lumen uricase × ABCG2 flux model | Yes (Monte Carlo n=5000 across genotype × sex × dose) | **Yes** (5-metric flux + capacity ratio + renal compensation + substrate-limit + dose-response) | Implicit (full grid stratified, no candidate-vs-candidate filtering — model is a continuous prediction surface, not a discrete-candidate selection problem) | **Clean** — methodology-fit for the question shape |
| comp-022 | Uricase cassette ranking (v1 + v2) | Yes (43,200 enumerated; 195 pass v1; 71 pass v2 N-of-5 ≥ 4) | **Yes** (CAI + ViennaRNA MFE + chaperone-load + promoter×SP prior + ESM2 pseudo-pLDDT) | **Yes** (N-of-5 ≥ 4 gate; v1→v2 retrofit confirms top cluster at 100% survival) | **Canonical exemplar** — exactly the BioDesignBench-recommended cure |
| comp-023 | cns1+cns2 cordycepin cassette burden FBA | Yes (5 scenarios: WT, dual cassette, +cns1-cns2, +carnS+panD, +panD only) | **Partial** (FBA alone — single-method evaluation; v1 verdict GREEN under static FBA) | Implicit (5-scenario comparison, but no orthogonal-method head-to-head; comp-023 v2 dynamic FBA was queued specifically to address this) | **Pending v2** — single-method risk acknowledged; v2 dFBA + CNKI cofactor refinement is the corrective queued in Planned Analyses |
| comp-024 | Complestatin-family BGC heterologous expression | One chassis pair primary (Bacteroides vs. *E. coli* Nissle) | Multi-axis (BGC cluster size + NRPS module count + precursor supply + codon usage + toxicity + regulatory architecture) | **Limited** — no explicit head-to-head between chassis candidates beyond comparator; would benefit from broader candidate set | **Audit flag** — consider expanding candidate chassis set when comp-024 fires |
| comp-025 | ADA × cns1 substrate competition | Yes (kinetic + FBA + strain-background comparison) | **Yes** (kinetic Km + FBA stratified pool + literature strain-background check; 3 orthogonal approaches per the brief) | Yes (3-approach concordance gates the verdict) | **Clean** — methodology-fit |
| comp-026 | Multi-cassette induction interference | Multi-cassette enumeration (uricase + lactoferrin + cns1+cns2) | Multi-axis (regulatory promoter crosstalk + comparative comp-022 top-cluster regulation + orthogonal-promoter recommendation) | Yes (orthogonal-promoter analysis is the head-to-head filter) | **Clean** — methodology-fit |
| comp-027 | Disulfiram dose modeling (GSDMD vs. AUD ceiling) | Methodology TBD (queued 2026-05-15) | **TBD** — brief covers 4 axes (PK, EC50, plasma-vs-deterrent ratio, sub-AUD window) but the methodology isn't yet specified | **TBD** | **Audit flag** — when comp-027 brief is finalized, ensure multi-method evaluation (PK modeling + literature meta-analysis + Brian-specific dose-response priors) rather than single-axis dose calculation |

**Action items from the audit:**

1. **comp-024 candidate-set expansion.** When comp-024 fires, expand beyond Bacteroides vs. *E. coli* Nissle to include the broader engineered-LBP chassis set (*Akkermansia*, *Faecalibacterium prausnitzii*) for proper head-to-head. Add to scope-page Phase 2.
2. **comp-027 methodology spec.** When comp-027 brief is finalized, explicitly require multi-method evaluation per BioDesignBench's "≥3 evaluation-metric categories" finding. Don't ship comp-027 as a single-axis PK model.
3. **General rule for new comp-NNN authoring.** Subagent briefs for new comp-NNNs must explicitly require multi-method evaluation + candidate filtering + termination only after head-to-head comparison. The walk-synthesis SKILL.md §4 briefing-rules now carries this guidance. The Pass 3 review prompt also emphasizes evaluation-depth-over-tool-coverage.

The audit reaffirms that the N-of-M concordance pattern this page advocates IS the BioDesignBench cure; the gap is consistency of application across all comp-NNNs, not the methodology itself.

## Honest critiques

- **Reproducibility:** Preprint, not peer-reviewed. Mouse cohort sizes, dosing schedule, blinding protocol, and statistical correction for multiple comparisons across 40 clocks are not pinned down in lay coverage. Need to read supplementary methods before citing specific numbers downstream.
- **Post-hoc-flexible "top candidate":** "Top-scoring AI candidate" is selection-on-the-dependent-variable unless they pre-registered which N candidates would be validated. Ouabain may have been picked because it was tractable (already FDA-approved for heart failure, easy to dose), not because it was rank #1.
- **Biomarker validation ≠ lifespan validation.** Frailty + cardiac + microglia at 3 months is **healthspan**, not survival. The social-media framing implies "validated longevity"; what was validated is "decelerated aging biomarkers in old wild-type mice." Big distinction. ITP-style lifespan trials are years away.
- **Composite score across 40 clocks risks circularity.** Many aging clocks are trained on overlapping datasets; "consensus across 40 clocks" may be less independent than it sounds. Worth checking whether they decorrelated the clock set in supplementary methods.
- **Ouabain therapeutic window.** Cardiac glycoside, narrow therapeutic index (used for atrial fibrillation; toxic at modest overdoses). The AI didn't discover ouabain de novo; it surfaced an existing drug whose senolytic properties were already in the literature. Translation framing should not conflate "AI-flagged" with "AI-discovered."
- **Underspecified in public version:** exact LLM(s), agent orchestration framework, prompt templates, composite-clock weighting, mouse cohort sizes, blinding, pre-registration status of validation experiment.

## What this page is not

- **Not** an endorsement of ouabain for any Open Enzyme target. Ouabain is a longevity-screen finding for aged WT mice on healthspan biomarkers; gout / EPI are not the indication.
- **Not** a claim that fully autonomous AI biomedical discovery is here. The autonomy boundary is "AI-ranks-candidates-from-existing-data, human-validates," not "AI-discovers-and-validates-end-to-end."
- **Not** a recommendation to adopt ClockBase Agent's specific architecture. The lessons are pattern-level (composite scoring, hypothesis-then-verify, N-of-M concordance), not implementation-level.

## Open follow-ups

- **Retrieve full bioRxiv supplementary methods** when local PDF access is available; verify cohort sizes, blinding, statistical correction, decorrelation of the 40-clock set. Update the [VERIFY] flags inline.
- **Map ClockBase's verification-agent pattern onto comp-NNN.** Concrete proposal: every comp-NNN run produces a primary-output report + a verification-pass report (independent agent re-checks load-bearing numbers vs. UniProt / ChEMBL / AlphaFold). The DAF SCR1-4 incident (2026-05-06) is the canonical case showing why this is needed.
- **N-of-M concordance threshold calibration.** What's the right threshold for promoting comp-NNN candidates to wet lab? ClockBase uses ~30/40 (75%); we likely need 4/5 (80%) or higher for our smaller orthogonal-model set. Pin via retrospective analysis of comp-001 through comp-014 verdicts.
- **Multi-vendor LLM agent orchestration.** ClockBase appears to use a single LLM across sub-agents. Per OE's multi-model heterogeneity discipline, comp-NNN should consider using different LLMs for hypothesis-generation vs. verification (e.g., Claude generates hypotheses, DeepSeek verifies; or Gemini ranks, Claude reviews).
- **Surface ouabain as a senolytic-class entry on the modality matrix?** Tangential to gout-NLRP3 directly, but the ouabain-as-senolytic mechanism intersects with NLRP3 priming (cellular senescence → SASP → IL-1β). Decision: not a chase target for Open Enzyme, but worth a one-line note on the modality-chokepoint matrix for completeness.

## See also

- [`computational-experiments.md`](./computational-experiments.md) — comp-NNN tracking index
- [`manual-literature-mining.md`](./manual-literature-mining.md) — five-rule discipline for safe LLM literature use
- [`linter-design.md`](./linter-design.md) — falsification-card + document-lint architecture
- [`ai-bio-tools-playbook.md`](./ai-bio-tools-playbook.md) — computational stack
- [`open-source-platform.md`](./open-source-platform.md) — multi-vendor heterogeneity guard discipline
- [`practitioner-toolkit.md`](./practitioner-toolkit.md) — section umbrella (self-experiments + DIY-bio + rigor disciplines)
