ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: 5ccb7440f0a9986048cfc19a1a739d453c7157f1ae93a0dce0c16e9f08c4519f

# Independent comp review — comp-004

## Reviewed snapshot

Independent static Gate-2 review of the exact 48-entry post-run manifest.

All entries match their recorded byte counts and SHA-256 hashes. The four post-run design files are byte-for-byte identical to the Gate-1-approved design bound by pre-run digest `4d1a41ff214e1e17c4d5fcc065078b7a6c4074f8c00ff4bab4b803daf94b5d26`.

Repository checks passed:

- COMP-004 manifest verification
- Corpus hygiene
- Relative-link validation
- Privacy validation
- Validation-dashboard consistency
- Whitespace/diff integrity
- COMP-013 invalidation-ledger verification

## Bottom-line verdict

Clean.

COMP-004 correctly withdraws its former quantitative gut-lumen occupancy model. The current artifact supports only a bounded conclusion: the three cited records contain compound-specific ABCG2/BCRP interaction signals, but none establishes quantitative intestinal urate transport.

The implementation, outputs, canonical interpretation, experiment plan, operational correction cascade, COMP-013 tombstone, COMP-014 scope correction, and reader-facing pages consistently prohibit:

- Nominal gut concentration divided by drug-substrate IC50 as a biological decision metric.
- Hill-equation estimates of intestinal urate-transport inhibition.
- Compound ranking or `VERY_HIGH`/`HIGH` risk labels.
- Dose, formulation, genotype, safety, or clinical-direction conclusions.
- An EGCG class effect, stacking effect, or invented acute-versus-chronic sign switch.
- Reuse of COMP-013 or COMP-014 rankings as current evidence.

No remaining action is required for this exact snapshot.

## Implementation and constraint closure

The deterministic implementation:

- Enforces the exact quercetin, curcumin, and EGCG record set.
- Validates evidence tier, assay context, substrate identity, intestinal-model status, urate-evidence status, and allowed disposition.
- Requires direct intestinal urate-flux testing whenever the cited record does not establish it.
- Fails if any record authorizes quantitative risk ranking.
- Emits no biological concentration estimate, occupancy ratio, percent inhibition, dose, ranking, or clinical inference.
- Produces a machine-readable audit and a faithful human summary.

The generated outputs agree exactly with the fixed inputs and decision rules.

## Summary-fidelity audit

The summary faithfully reports:

- **Quercetin — In Vitro:** drug-substrate BCRP assays in nonintestinal systems.
- **Curcumin — Animal Model:** intestinal BCRP interaction in cynomolgus monkeys using sulfasalazine and rosuvastatin, not urate.
- **EGCG — In Vitro:** mitoxantrone-assayed BCRP activity in MCF-7Tam cells, without an intestinal model or urate endpoint.

It explicitly identifies the audit as a three-record bounded evidence set rather than a literature census. Its direct-assay recommendation is supported by the model’s unresolved variables and does not become a treatment recommendation.

## Reader-facing ownership audit

The correction now lands on the proper surfaces:

- `supplement-abcg2-antagonism-computational.md` owns the COMP result.
- `abcg2-modulators.md` owns the transporter evidence and bounded conjecture.
- `egcg.md`, `theaflavins.md`, and `supplements-stack.md` own compound-specific boundaries.
- `validation-experiments.md` owns the discriminating wet-lab route.
- Portfolio and computational indexes contain only bounded status summaries.
- TCM and medicinal-mushroom pages no longer inherit invalid rankings.
- Duckweed’s separately primary-verified luteolin/XO result remains available without importing COMP-013’s unsupported URAT1 or viability conclusions.
- Cross-track and chassis comparisons remain on portfolio surfaces instead of dominating focused intervention pages.

The corrected luteolin operational artifacts now separate the independent complement hypothesis from the invalid COMP-013 urate-axis premise.

## Conjecture preservation audit

The useful ideas survive with explicit epistemic boundaries.

The ABCG2 conjecture preserves the possibility that free compound/metabolite exposure, time, intestinal context, and transporter attribution could produce a meaningful effect. It explicitly states that direct intestinal urate evidence is absent and identifies the observation that would discriminate the idea.

The COMP-013 correction preserves source-material and traditional-formula leads as an unranked inventory. COMP-049 can qualify those leads without resurrecting the invalid ranking.

The medicinal-mushroom track preserves its exact-material interaction idea as a Research Conjecture while withdrawing unsupported combination, sourcing, exposure, and portfolio conclusions.

## Generated-output and proposed-update inventory

| # | Manifest entry | Kind | Verdict |
|---:|---|---|---|
| 1 | `COMP-004/README.md` | Design | Consistent |
| 2 | `COMP-004/analyze.py` | Design | Consistent |
| 3 | `COMP-004/inputs/assay_evidence.json` | Design | Consistent |
| 4 | `COMP-004/inputs/provenance.md` | Design | Consistent |
| 5 | `COMP-004/outputs/assay_evidence_audit.json` | Generated | Faithful |
| 6 | `COMP-004/outputs/summary.md` | Generated | Faithful |
| 7 | `index.md` | Update | Consistent |
| 8 | `operations/cfh-mechanism-dissociation-2026-05-21/README.md` | Update | Corrected |
| 9 | `operations/.../inputs/run_deepseek_counterread.py` | Update | Corrected |
| 10 | `operations/.../luteolin-source-read-2026-05-21.md` | Update | Corrected |
| 11 | `operations/.../luteolin-two-model-annotated-2026-05-21.md` | Update | Corrected |
| 12 | `operations/global-lit-scan-gap-audit-2026-05-20.md` | Update | Consistent |
| 13 | `operations/.../p0-3-cnki-rerun-summary-2026-05-20.md` | Update | Consistent |
| 14 | `operations/notable-moments.md` | Update | Consistent |
| 15 | `operations/operational-search-template.md` | Update | Consistent |
| 16 | `operations/todos.md` | Update | Consistent |
| 17 | `wiki/abcg2-modulators.md` | Update | Consistent |
| 18 | `wiki/androgen-natural-modulation.md` | Update | Consistent |
| 19 | `wiki/androgen-urate-axis.md` | Update | Consistent |
| 20 | `wiki/cfh-mechanism-dissociation-cp0-candidates-computational.md` | Update | Corrected |
| 21 | `wiki/complement-c5a-gout.md` | Update | Bounded |
| 22 | `wiki/computational-experiments.md` | Update | Consistent |
| 23 | `wiki/cross-validation.md` | Update | Mission-aligned |
| 24 | `wiki/duckweed-aquatic-chassis.md` | Update | Track-focused |
| 25 | `wiki/egcg.md` | Update | Evidence-bounded |
| 26 | `COMP-013/README.md` | Update | Valid tombstone |
| 27 | `COMP-013/invalidation.json` | Update | Ledger verified |
| 28 | `COMP-014/README.md` | Update | Scope bounded |
| 29 | `COMP-014/outputs/scope-summary.md` | Update | Scope bounded |
| 30 | `wiki/etc/manual-literature-mining.md` | Update | Consistent |
| 31 | `wiki/gout-genetic-variants.md` | Update | Consistent |
| 32 | `wiki/gout-kill-chain-delivery-routes.md` | Update | Bounded |
| 33 | `wiki/gout-pathophysiology.md` | Update | Bounded |
| 34 | `wiki/hypotheses/H04-tcm-rigor-intersection.md` | Update | Properly scoped |
| 35 | `wiki/hypotheses/README.md` | Update | Consistent |
| 36 | `wiki/medicinal-mushroom-complement-track.md` | Update | Conjecture preserved |
| 37 | `wiki/medicinal-mushroom-compound-mapping-computational.md` | Update | Partial inventory only |
| 38 | `wiki/medicinal-mushroom-extract-sops.md` | Update | Draft status explicit |
| 39 | `wiki/modality-chokepoint-matrix.md` | Update | Correct comparison owner |
| 40 | `wiki/nlrp3-exploit-map.md` | Update | Consistent |
| 41 | `wiki/nlrp3-inhibitor-screen.md` | Update | Exposure/additivity corrected |
| 42 | `wiki/open-questions.md` | Update | Leads and gates preserved |
| 43 | `wiki/supplement-abcg2-antagonism-computational.md` | Update | Canonical result faithful |
| 44 | `wiki/supplements-stack.md` | Update | No personalized dosing rule |
| 45 | `wiki/tcm-gout-compound-triage-computational.md` | Update | Invalidation propagated |
| 46 | `wiki/tcm-modern-rigor-intersection.md` | Update | Unranked leads preserved |
| 47 | `wiki/theaflavins.md` | Update | No unsupported class effect |
| 48 | `wiki/validation-experiments.md` | Update | Discriminating tests bounded |

## Load-bearing verification table

| Claim or boundary | Verification | Verdict |
|---|---|---|
| Approved design equals post-run design | Four design hashes compared | Pass |
| Manifest binds every current file | Byte and SHA-256 verification | Pass |
| Generated summary matches JSON audit | Record-by-record static trace | Pass |
| Quercetin record establishes intestinal urate flux | It does not | Properly rejected |
| Curcumin drug-probe result establishes urate transport | It does not | Properly rejected |
| EGCG MCF-7Tam result establishes intestinal urate transport | It does not | Properly rejected |
| Yu 2024 establishes ABCG2 | Primary abstract does not | Properly excluded |
| Nominal concentration/IC50 estimates intestinal urate inhibition | Unsupported | Invalidated |
| COMP-013 rankings remain decision-usable | No | Tombstoned |
| COMP-013 retired artifacts match the historical tree | Invalidation checker passed | Pass |
| COMP-014 supplies a valid ranked portfolio | No | Correctly bounded |
| Luteolin COMP-013 XO/URAT1 premise remains active in CFH work | No | Corrected |
| Validation experiment measures the missing variables | Free exposure, attribution, barrier, viability, time, and urate flux specified | Pass |

## Affected wiki pages

The main COMP-004 correction is fully propagated through the ABCG2, EGCG, theaflavin, supplement, validation, computational-index, and portfolio surfaces.

The broader dependency correction also reaches the TCM, COMP-013, COMP-014, medicinal-mushroom, complement, NLRP3, gout-pathophysiology, open-question, hypothesis, and mission-facing pages included in the manifest.

## New connections or implications

The corrected corpus points to a stronger experiment than compound ranking:

1. Measure free parent compound and metabolites in the relevant intestinal system.
2. Measure total and surface ABCG2.
3. Establish ABCG2 attribution with a matched perturbation.
4. Measure basolateral-to-apical urate flux directly.
5. Include barrier integrity, viability, and prespecified exposure times.
6. Evaluate compounds independently unless direct data justify a class or interaction model.

This retains the potentially valuable ABCG2 lead while making the unsupported shortcut impossible to reuse.

## Required actions

None.

## Review limits

This was a static, read-only review. No result-bearing COMP analysis was executed.

The primary-record verification boundary remains the cited abstracts or publisher records rather than a systematic full-text literature census. COMP-014’s complete historical artifact has its own separate Gate-2 review; this review assessed the COMP-014 surfaces included in the COMP-004 correction cascade.
