---
title: Autonomous AI Screening Methodology — Lessons from ClockBase Agent for Comp-NNN
date: 2026-05-07
tags: [methodology, ai-driven-discovery, comp-NNN, peer-track, prior-art, rigor-discipline]
related:
  - ../computational-experiments.md
  - manual-literature-mining.md
  - ../linter-design.md
  - ai-bio-tools-playbook.md
  - ../chaperone-orthogonal-stacking.md
  - ./open-source-platform.md
  - practitioner-toolkit.md
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

**Verification status (per [CLAUDE.md §4](../../CLAUDE.md) pre-commit grep-verify gate):** the bioRxiv PDF returned 403 from the agent research environment, so cohort sizes, exact dosing, blinding protocol, and statistical correction methods have NOT been verified against primary supplementary methods. Numbers in this page are sourced from the paper abstract + lay coverage. **Treat as preliminary until full supplementary methods are retrieved locally.** Specific load-bearing items flagged inline below.

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

### 2. Rank only with outcome-calibrated predictors

Multiple models are useful when each predicts a named quantity and its relationship to the decision outcome is calibrated. “Orthogonal” labels alone do not make heterogeneous proxies commensurable.

For comp-NNN, keep each model inside the quantity it actually represents:

- Structure-model confidence/context (AlphaFold + ESMFold + Boltz-2 outputs; not thermodynamic stability, folding kinetics, secretion capacity, or native-fold attainment)
- mRNA structure metrics (RNAfold accessibility, codon usage)
- Host-toxicity proxies (where applicable)
- Folding-route, disulfide, glycosylation, or trafficking annotations as separate hypothesis-generating fields until matched outcome data calibrate a predictor

Do not collapse these fields into a biological composite merely because they are different. A composite ranking is allowed only when the direction, scale, dependence, and relationship of each input to the same named outcome have been justified in advance. Otherwise report a property table and use disagreement to expose uncertainty.

### 3. Hypothesis-then-verify pattern (mirrors the pre-commit grep-verify gate)

ClockBase's two-pass pattern (hypothesis-generation agent → verification agent re-checking against raw data + literature) maps directly onto the pre-commit grep-verify discipline in [CLAUDE.md §4](../../CLAUDE.md). They've operationalized the same discipline at the agent level.

**Comp-NNN implementation:** an agent produces a provenance-bound property table and, only where calibrated, a ranked shortlist. An **independent verification agent** re-checks load-bearing numbers (residue indices, disulfide counts, predicted Tm, cleavage-site predictions) against primary databases before any candidate enters the wet-lab queue. Verification of an input does not calibrate a score built from it.

**COMP-022 caution:** The artifact enumerated 43,200 uricase cassette combinations, but its current shortlist is non-authoritative. Its N-of-5 vote includes an uncalibrated chaperone-load axis inherited from the retired folding-score framework, and the remaining axes do not share one measured outcome. Enumeration survives as a hypothesis inventory; the open corrective review must recompute or retire the rankings before candidate promotion. See the [current boundary](../uricase-cassette-ranking-computational.md) and [open actions](../../synthesis/queue/comp-review-022.md).

**Proxy-quality lesson from the COMP-022 retrofit.** Within the historical artifact, replacing a GC-content/clamp/palindrome proxy with ViennaRNA MFE produced a weak correlation and materially changed shortlist membership. That diagnostic shows proxy sensitivity; it does not validate the revised shortlist. A proxy must be calibrated against the quantity it stands in for before it can drive promotion. ViennaRNA models RNA secondary-structure energy; structure predictors generate structural hypotheses; Rosetta encodes energy functions; FBA tests declared metabolic constraints. None is empirical validation of expression, folding, secretion, or function.

**Known proxy failure — pLDDT is not accessibility.** The retired shared protease-stability helper used AlphaFold pLDDT as a solvent-accessibility proxy. pLDDT is prediction confidence, not burial, secondary-structure compatibility with cleavage, protease survival, or retained activity. The live helper was removed so a future COMP cannot silently reuse the invalid mapping; Git preserves it for audit. COMP-001 therefore supplies only adjacent-pair matches to three unverified legacy preference filters plus a structural-confidence inventory for *A. flavus* UOX. The arrays are not established exhaustive protease-specificity rules. COMP-001 cannot support a LOW-risk, survival, or fermentation-performance conclusion. Any UOX shio-koji survival claim requires the direct [§1.10 assay](../validation-experiments.md#110-heterologous-uricase--lactoferrin-stability-in-shio-koji-salt-protease-ferment); a structure/SASA analysis may refine candidate selection but cannot replace that gate. The same boundary applies to other COMPs that inherited the proxy.

### 4. Autonomy boundary = structured hypothesis generation, not validation

Useful prior: keep the AI on the **property table + provenance + explicit uncertainty** side of the boundary. A ranked shortlist is acceptable only when its predictors and decision rule are calibrated to the named outcome. Humans or an explicit gate still make the wet-lab commit.

This connects to the comp-NNN gating ritual: computation should emit property-specific quantities, provenance, uncertainty, and explicit non-claims. Configuration-level experiments then measure the biological outcomes the models cannot establish. Composite LOW/MODERATE/HIGH labels are appropriate only when calibrated to the named outcome; otherwise retain the underlying proxy values without a biological verdict.

**Physical-execution counterpart surfaced 2026-05-19: Picolab.** ClockBase is prior art for autonomous ranking over existing data; [Picolab v2](https://github.com/OmkarKovvali/picolab_v2) is early open-source prior art for the other half of the loop: cheap, tube-scale physical execution. The repo wraps a repurposed 3D-printer gantry with a G-code motion planner, calibration layer, camera-assisted agent workspace, and operator-approved execution. For OE methodology, the lesson is not "closed-loop validation is solved"; it is narrower and useful: a lower-cost automation layer could make serial dilution, colorimetric assay setup, and post-step camera verification less operator-variable. The autonomy boundary should remain explicit: AI may propose and preview actions; hardware execution stays gated; biological interpretation and wet-lab commit decisions stay human-reviewed until the assay itself is validated. (Engineering prior art; source: Picolab v2 repository; see [`practitioner-toolkit.md`](./practitioner-toolkit.md) DIY Capability Builds)

### 5. Computational-to-wet-lab handoff: conditional N-of-M concordance

N-of-M agreement can inform promotion only when the axes are sufficiently independent and each has been calibrated to the same named outcome in a relevant domain. Without those conditions, voting counts unlike proxies as if they were interchangeable evidence.

For Open Enzyme, use a property table when folding, secretion, codon, scaffold, or other models target different quantities. Promote from that table only through a prespecified rule tied to the actual experiment, or after outcome data calibrate a composite or vote. There is no generic 4-of-5 threshold.

## BioDesignBench evaluation-depth audit (added 2026-05-15)

Kim & Romero's BioDesignBench paper (bioRxiv 10.64898/2026.05.06.723381, verified 2026-05-15 — see [`bio-ai-tools.md` §BioDesignBench](./bio-ai-tools.md)) empirically validates the "deeper multi-metric evaluation" methodology this page advocates. The paper's central finding across 836 task–condition observations on 76 protein-design tasks: top LLM agents (DeepSeek V3, GPT-5) select appropriate tools but **evaluate candidate designs at only ~14% of expert intensity** and **never discard a generated candidate** across the entire benchmark. Forcing multi-metric evaluation (≥3 metric categories per candidate, compute-matched against shallow control) recovers DeepSeek V3 by +9.3 points (p = 0.002) and GPT-5 by +15.9 points (p < 0.001). The deterministic hardcoded pipeline (which already has multi-metric evaluation built into its workflow) gains nothing from the intervention — confirming the deficit is **specifically behavioral**, not generic compute.

This supports deeper, genuinely multi-metric evaluation. It does not validate an N-of-M vote whose axes are uncalibrated, correlated, or aimed at different outcomes; COMP-022 remains the current cautionary example.

**Audit of OE's existing comp-NNN stack** against BioDesignBench's three failure-mode axes — (A) multiple candidates generated? (B) multi-metric evaluation across orthogonal scoring axes? (C) head-to-head comparison + filtering before termination?

| comp-NNN | Topic | (A) Multiple candidates? | (B) Multi-metric eval? | (C) Head-to-head + filter? | Audit verdict |
|---|---|---|---|---|---|
| comp-019 | Gut-lumen uricase × ABCG2 flux model | **Historical invalidated implementation only—not decision-grade evidence** (Monte Carlo n=5000 across genotype × sex × dose) | **No—unconditional classification not robust** (multiple reported metrics inherited one Vmax-only capacity assumption) | Implicit grid; no empirical calibration | **Invalidated tombstone.** None of the Monte Carlo outputs survive for decision use. COMP-044 supplies no replacement physiology, dose, efficacy, genotype order, production target, topology/chassis, or safety conclusion. |
| comp-022 | Uricase cassette ranking (v1 + v2) | Yes; 43,200 combinations enumerated | Heterogeneous proxies; chaperone-load axis uses uncalibrated inherited coefficients | N-of-5 gate exists but is not calibrated to one named biological outcome | **Corrective review open.** Enumeration survives as a hypothesis inventory; current shortlist and winners are non-authoritative. |
| comp-023 | *cns1+cns2* cordycepin-burden FBA | Historical scenario set only; boundaries were not implemented consistently | No; one uncalibrated static-FBA model with unverified reaction and unit assumptions | No valid head-to-head comparison | **Invalidated tombstone.** No burden, flux, yield, breakpoint, feasibility, or compatibility result survives. Jeennor's direct production evidence and the ER-orthogonality conjecture are independent of the model. |
| comp-024 | Complestatin-family BGC heterologous expression | Historical pair: *Bacteroides* versus *E. coli* Nissle | Multiple hand-assigned factors with no calibration | Arbitrary geometric mean and incomparable C1-INH comparator | **Invalidated tombstone.** Preserve the oxygen-regime conjecture; use direct active-product measurements, not a rescored candidate set. |
| comp-025 | ADA × cns1 substrate competition | Yes (kinetic + FBA + strain-background comparison) | **Yes** (kinetic Km + FBA stratified pool + literature strain-background check; 3 orthogonal approaches per the brief) | Yes (3-approach concordance gates the verdict) | **Clean** — methodology-fit |
| comp-026 | Multi-cassette induction interference | Historical multi-cassette enumeration | Included a COMP-022 top-cluster comparison whose authority is now open | Historical orthogonal-promoter filter | **Not current decision authority.** Re-review independently before reuse; no COMP-022-derived candidate survives by inheritance. |
| comp-027 | Disulfiram dose modeling (GSDMD vs. AUD ceiling) | Methodology TBD (queued 2026-05-15) | **TBD** — brief covers 4 axes (PK, EC50, plasma-vs-deterrent ratio, sub-AUD window) but the methodology isn't yet specified | **TBD** | **Audit flag** — when comp-027 brief is finalized, ensure multi-method evaluation (PK modeling + literature meta-analysis + Brian-specific dose-response priors) rather than single-axis dose calculation |

**Action items from the audit:**

1. **Complestatin route test.** If the thread resumes, define an exact host × oxygen-regime matrix and require analytical recovery of active crosslinked product before comparing routes.
2. **comp-027 methodology spec.** When comp-027 brief is finalized, explicitly require multi-method evaluation per BioDesignBench's "≥3 evaluation-metric categories" finding. Don't ship comp-027 as a single-axis PK model.
3. **General rule for new comp-NNN authoring.** Subagent briefs for new comp-NNNs must explicitly require multi-method evaluation + candidate filtering + termination only after head-to-head comparison. The walk-synthesis SKILL.md §4 briefing-rules now carries this guidance. The Pass 3 review prompt also emphasizes evaluation-depth-over-tool-coverage.

The audit supports using prespecified multi-metric comparison to reduce shallow candidate promotion. It does not show that an N-of-M rule is a general solution: the metrics may share assumptions, and empirical validation remains required.

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
- **Not** a recommendation to adopt ClockBase Agent's specific architecture. The transferable lessons are exhaustive search where appropriate, provenance-bound property evaluation, hypothesis-then-verify, and conditional use of calibrated multi-model agreement.

## Open follow-ups

- **Retrieve full bioRxiv supplementary methods** when local PDF access is available; verify cohort sizes, blinding, statistical correction, decorrelation of the 40-clock set. Update the [VERIFY] flags inline.
- **Map ClockBase's verification-agent pattern onto comp-NNN.** Concrete proposal: every comp-NNN run produces a primary-output report + a verification-pass report (independent agent re-checks load-bearing numbers vs. UniProt / ChEMBL / AlphaFold). The DAF SCR1-4 incident (2026-05-06) is the canonical case showing why this is needed.
- **Outcome-specific calibration.** Identify a future COMP with enough matched computational and experimental outcomes to test whether any predictor set supports a promotion rule. Do not infer a threshold by pooling unrelated COMPs or unlike biological outcomes.
- **Multi-vendor LLM agent orchestration.** ClockBase appears to use a single LLM across sub-agents. Per OE's multi-model heterogeneity discipline, comp-NNN should consider using different LLMs for hypothesis-generation vs. verification (e.g., Claude generates hypotheses, DeepSeek verifies; or Gemini ranks, Claude reviews).
- **Map Picolab-style physical execution onto OE assay loops.** Concrete proposal: identify the first non-sterile, tube-scale protocol where low-cost liquid handling would reduce operator variance without introducing safety risk. Leading candidates: serial dilution practice, smartphone colorimetry standard curves, p-NPP lipase setup, DNS amylase setup, or benign dye controls before any biological sample handling.
- **Surface ouabain as a senolytic-class entry on the modality matrix?** Tangential to gout-NLRP3 directly, but the ouabain-as-senolytic mechanism intersects with NLRP3 priming (cellular senescence → SASP → IL-1β). Decision: not a chase target for Open Enzyme, but worth a one-line note on the modality-chokepoint matrix for completeness.

## See also

- [`computational-experiments.md`](../computational-experiments.md) — comp-NNN tracking index
- [`manual-literature-mining.md`](./manual-literature-mining.md) — five-rule discipline for safe LLM literature use
- [`linter-design.md`](../linter-design.md) — falsification-card + document-lint architecture
- [`ai-bio-tools-playbook.md`](./ai-bio-tools-playbook.md) — computational stack
- [`open-source-platform.md`](./open-source-platform.md) — multi-vendor heterogeneity guard discipline
- [`practitioner-toolkit.md`](./practitioner-toolkit.md) — section umbrella (self-experiments + DIY-bio + rigor disciplines)
