---
type: most-curious-thread
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 1
global_index: 8
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# The single thread I'd spend the next experiment slot on is the Tier 2 butyrate assay validation (HPLC-UV vs.

The single thread I'd spend the next experiment slot on is the **Tier 2 butyrate assay validation (HPLC-UV vs. GC-MS spike/recovery on culture supernatant)** from comp-038. Corpus evidence supporting the hunch: the genotype-informed supplement workflow's Q141K butyrate-emphasis example (genotype-informed-supplement-workflow.md) and the butyrate dose-response arm in §1.14 (additive ABCG2 suppression by androgens + TNFα + butyrate rescue + lactoferrin synergy) both explicitly depend on a validated Tier 2 butyrate ruler; without it, butyrate-emphasis interventions cannot be cheaply verified, and unverified metabolite dose is indistinguishable from mechanism-failure noise (the exact "silent underdosing" failure mode the workflow was designed to block). The 2026-05-20 comp-038 audit returned YELLOW with a clear next-step: focused full-text/protocol verification on PMID 23542733 (De Baere 2013 HPLC-UV, validated on bacterial culture supernatant, linear 0.5–50 mM, no derivatization, butyrate resolved) and PMID 42041444 (electrochemical fecal SCFA, failed the gate due to vendor-locked hardware and unreleased ANN). The full-text verification step is complete (2026-06-01); the empirical spike/recovery remains the wet-lab gate at [`validation-experiments.md` §1.31](./validation-experiments.md). Evidence that would refute it: recovery <70% or GC-MS disagreement >30% in OE-relevant medium matrix (yeast/koji spent medium) would confirm HPLC-UV does not transfer, leaving GC-MS as the only Tier 3 anchor and the Tier 2 gap as unclosed for culture supernatant. Cheapest discriminating experiment: $500 spike/recovery study on sodium-butyrate standards in sterile and spent medium, measured in parallel by HPLC-UV and GC-MS (contract lab or community-biolab with both instruments). I suspect another sweep model would converge on this pick (it's the obvious next step from comp-038's YELLOW verdict and the workflow's explicit butyrate-specific limitation), so this is likely convergent rather than idiosyncratic.



**Sources cited:**
- wiki/abcg2-modulators.md
- wiki/abcg2-q141k-chaperone-screen-computational.md
- wiki/androgen-urate-axis.md
- wiki/aspergillus-oryzae.md
- wiki/blood-barrier-exploits.md
- wiki/cannabinoids-terpenes.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/chassis-pending-interventions.md
- wiki/computational-experiments.md
- wiki/cross-validation.md
- wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md
- wiki/delivery-route-matrix.md
- wiki/disulfiram.md
- wiki/dual-chassis-ecn-pdb-uricase-computational.md
- wiki/engineered-koji-protocol.md
- wiki/engineered-lbp-chassis.md
- wiki/etc/GRAPH.md
- wiki/etc/README.md
- wiki/etc/autonomous-screening-methodology.md
- wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/wiki-archive.md
- wiki/etc/experiments/comp-007-food-grade-hdaci-screen/inputs/provenance.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/inputs/provenance.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/outputs/summary.md
- wiki/etc/experiments/comp-008-f-prausnitzii-heterologous-expression/wiki-archive.md
- wiki/etc/experiments/comp-010-cassette-compatibility/README.md
- wiki/etc/experiments/comp-010-cassette-compatibility/inputs/provenance.md
- wiki/etc/experiments/comp-010-cassette-compatibility/outputs/summary.md
- wiki/etc/experiments/comp-010-cassette-compatibility/wiki-archive.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/README.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/inputs/provenance.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/outputs/summary.md
- wiki/etc/experiments/comp-011-c-utilis-uricase-cassette-compatibility/wiki-archive.md
- wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/README.md
- wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/wiki-archive.md
- wiki/etc/experiments/comp-032-abcg2-q141k-chaperone-screen/README.md
- wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/README.md
- wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/inputs/provenance.md
- wiki/etc/experiments/comp-042-kpv-gsdmd-pore-influx/outputs/summary.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/README.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/provenance.md
- wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/summary.md
- wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/README.md
- wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/inputs/provenance.md
- wiki/etc/experiments/comp-044-gut-lumen-uricase-physiologic-regime/outputs/summary.md
- wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/README.md
- wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/inputs/provenance.md
- wiki/etc/experiments/comp-045-uricase-topology-oxygen-peroxide-design/outputs/summary.md
- wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/README.md
- wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/inputs/provenance.md
- wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/summary.md
- wiki/etc/open-source-platform.md
- wiki/f-prausnitzii-heterologous-expression-computational.md
- wiki/fructose-connection.md
- wiki/genotype-informed-supplement-workflow.md
- wiki/gi-survival-prediction.md
- wiki/ginkgo-cloud-lab-evaluation.md
- wiki/gout-action-guide.md
- wiki/gout-genetic-variants.md
- wiki/gout-kill-chain-delivery-routes.md
- wiki/gout-multihop-research-program.md
- wiki/gout-pathophysiology.md
- wiki/gsdmd-pore-delivery-paradox.md
- wiki/gut-lumen-sink.md
- wiki/gut-lumen-uricase-physiologic-regime-computational.md
- wiki/hypotheses/H01-ward-dual-cassette.md
- wiki/hypotheses/H02-engineered-lbp-thesis.md
- wiki/hypotheses/H05-daf-scr14-cp0-thesis.md
- wiki/hypotheses/H08-gut-lumen-sink-platform-thesis.md
- wiki/hypotheses/H09-community-fermentation-reliability.md
- wiki/hypotheses/README.md
- wiki/koji-endgame-strain.md
- wiki/kpv-gsdmd-pore-influx-computational.md
- wiki/kpv-peptide.md
- wiki/nlrp3-exploit-map.md
- wiki/nlrp3-inhibitor-screen.md
- wiki/open-questions.md
- wiki/purine-degrading-bacteria.md
- wiki/purine-load-koji-vs-yeast.md
- wiki/staged-purine-sink-mass-balance-computational.md
- wiki/supplements-stack.md
- wiki/theaflavins.md
- wiki/tier-2-butyrate-assay-audit-computational.md
- wiki/tnfsf14-gout-target.md
- wiki/upstream-complement-assay-format-mapping-computational.md
- wiki/upstream-complement-modulator-sweep-computational.md
- wiki/upstream-complement-verification-rerun-computational.md
- wiki/urat1-sirna-target-site-selection-computational.md
- wiki/uricase-abcg2-genotype-stratification-computational.md
- wiki/uricase-cassette-ranking-computational.md
- wiki/uricase-topology-oxygen-peroxide-design-computational.md
- wiki/uricase.md
- wiki/validation-experiments.md

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The Most Curious Thread pick is the same Tier 2 butyrate assay validation as Proposed Experiment #1, which is correct — the convergence is acknowledged in the thread's own text ("I suspect another sweep model would converge on this pick"). The reasoning is well-supported: the genotype-informed supplement workflow's Q141K butyrate-emphasis example and the butyrate dose-response arm in §1.14 both depend on a validated Tier 2 butyrate ruler, and without it, unverified metabolite dose is indistinguishable from mechanism-failure noise. The full-text verification pass (completed 2026-06-01 per `tier-2-butyrate-assay-audit-computational.md`) correctly narrowed the candidates to one survivor (HPLC-UV, De Baere 2013). The refutation criteria (recovery <70% or GC-MS disagreement >30% in OE-relevant medium) are appropriately specific. The $500 cost and community-biolab accessibility make this the highest-insight-per-dollar experiment in the current queue. The convergence claim is honest — this is not an idiosyncratic pick but the obvious next step from comp-038's YELLOW verdict.
