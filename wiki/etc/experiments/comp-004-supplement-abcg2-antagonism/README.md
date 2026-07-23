# comp-004: Supplement–ABCG2 Assay-Evidence Audit

**Question:** Do three primary ABCG2/BCRP interaction records already cited by Open Enzyme—one each for quercetin, curcumin, and EGCG—support a quantitative prediction of intestinal urate-transport inhibition?

**Planned verdict boundary:** The code may route a compound from this bounded evidence set to a direct intestinal urate-flux assay. It may not calculate percent urate-transport inhibition, assign a clinical-risk tier, or rank compounds from nominal bulk concentration divided by a drug-substrate IC50.

**Informs:** [`validation-experiments.md` §1.14](../../../validation-experiments.md) — compound controls and paired exposure/protein/urate-flux readouts

**Canonical evidence homes:** [`abcg2-modulators.md`](../../../abcg2-modulators.md) for transporter evidence and conjecture; [`egcg.md`](../../../egcg.md) for EGCG evidence, sourcing, delivery, and falsification

## Why the quantitative verdict is invalid

The model combined nominal dose-derived bulk gut concentration with ABCG2 IC50 values obtained using drug substrates in other systems. It then applied a one-site Hill equation and presented the result as percent inhibition of intestinal urate transport and as a patient-risk tier.

That substitutes four unmeasured quantities:

1. nominal total concentration for free compound at the relevant enterocyte surface;
2. a drug-substrate IC50 for an urate-transport parameter;
3. non-intestinal or cancer-cell assay context for intestinal epithelium;
4. model occupancy for clinical direction and magnitude.

Accordingly, the nominal ratios, percent-inhibition estimates, and VERY_HIGH labels are invalid for biological or clinical decision use. Git retains the historical implementation; the current artifact does not reproduce those calculations.

## Pre-registered method

`inputs/assay_evidence.json` contains one primary-source-bounded record for each compound. It is a bounded correction set, not a systematic or multilingual literature census. The code:

1. validates the schema, exact compound set, controlled vocabularies, Boolean fields, substrates, and structured source identifiers;
2. assigns `DIRECT_INTESTINAL_URATE_FLUX_ASSAY_REQUIRED` when the cited record does not establish intestinal urate flux;
3. assigns the contrary disposition `DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED` if an updated record reports direct intestinal urate-flux evidence;
4. emits explicit reasons and `quantitative_risk_rank_allowed: false`;
5. writes a machine-readable audit and a short human summary.

There is no numerical sensitivity analysis because no numerical biological verdict is produced. The dominant uncertainties—free exposure, metabolites, substrate dependence, tissue context, and time—are experimental variables rather than parameter ranges justified for this model.

## Decision and falsification rules

- **Allowed result:** qualitative routing from the three cited records to a direct intestinal urate-flux assay.
- **Contrary result:** a cited record reporting direct intestinal urate flux triggers `DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED`; it cannot silently pass through the default disposition.
- **Required failure:** malformed records, duplicate or missing compounds, unsupported controlled values, or invalid source metadata.
- **Forbidden inference:** dose, formulation, percent inhibition, clinical risk, genotype susceptibility, acute/chronic direction, or dietary/extract direction.
- **Conjecture boundary:** Exposure time, concentration, metabolites, and tissue context may change EGCG's net effect on intestinal ABCG2. Direct evidence for the direction of that relationship is absent. The idea survives only as a Research Conjecture on the mechanism-owning wiki page.

## Planned outputs

- `outputs/assay_evidence_audit.json`
- `outputs/summary.md`

The run is deterministic, uses Python's standard library only, has no randomness or external calls, reads and writes UTF-8 explicitly, and writes only those two output files. Supported runtime: CPython 3.11 or newer.

## Reproduce after Gate 1 approval

From the repository root:

```bash
python3 wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/analyze.py
```

Run twice and compare output hashes before creating the post-run manifest.

## Planned downstream claim map

- `wiki/abcg2-modulators.md` — own the cross-compound evidence boundaries; correct the EGCG/Yu attribution; preserve the exposure/time/context idea only as a Research Conjecture.
- `wiki/egcg.md` — state the verified Farabegoli functional result and Yu renal-transporter result; remove the invented ABCG2/Nrf2 sign switch; retain sourcing, delivery, and the direct falsification experiment.
- `wiki/supplements-stack.md` — replace the claimed conflicting transporter directions with a bounded assay-design warning.
- `wiki/theaflavins.md` — remove EGCG as a supposed second example of an acute-inhibition/chronic-upregulation class pattern.
- `wiki/validation-experiments.md` — own the compound, exposure-time, ABCG2-attribution, barrier-integrity, viability, protein, and urate-flux controls; remove the presumed EGCG mechanism and unsupported concentration rationale.
- `wiki/computational-experiments.md` and `wiki/supplement-abcg2-antagonism-computational.md` — report the invalid quantitative verdict and the surviving direct-assay routing only.
- `wiki/nlrp3-inhibitor-screen.md` — replace “reconcile acute function with chronic expression” with the direct intestinal urate-flux evidence gap.
- `wiki/hypotheses/H04-tcm-rigor-intersection.md` and `wiki/tcm-modern-rigor-intersection.md` — remove comp-004 as validation of nominal gut-concentration/IC50 occupancy; preserve the useful requirement to measure exposure in the compartment where the mechanism is proposed.
- `wiki/tcm-gout-compound-triage-computational.md` and its entry in `wiki/computational-experiments.md` — state that comp-013's inherited occupancy component cannot by itself support biological viability or non-viability; its primary-source evidence map remains separately reviewable.
- `wiki/open-questions.md` and `wiki/medicinal-mushroom-compound-mapping-computational.md` — replace planned reuse of the occupancy shortcut with measured free exposure plus context-matched functional assays.
- `wiki/androgen-natural-modulation.md` — remove the patient-facing “counterindication” description and link to the bounded evidence audit.
- `index.md` — replace the public comp-004 quantitative risk summary because it currently repeats the invalid verdict.
- `synthesis/queue/2026-07-15-a68eaeb8-contradiction-2-egcg-in-vitro-inhibition-vs-in-vivo-favorable-phenotype-is.md` — delete after all active surfaces above are corrected.

Reader-facing pages receive current evidence and experiments, not narration about old artifacts, sweeps, or page placement. No page receives a quantitative or clinical risk ranking from comp-004. A negative result for one compound, exposure time, or formulation does not erase untested neighboring conditions or the bounded Research Conjecture.
