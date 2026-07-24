ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: e01a25c678d9c8802f4bc627e2b898df017d45934955191e26a86615b5c9f95a

# Independent comp review — COMP-015 retirement

**Reviewer:** `/root/comp015_gate2_final4` (fresh context-isolated Gate 2)

## Verdict

Clean with limitations. The manifest, all 30 bound files, and the retired
ten-file artifact were inspected. The retired files match Git commit
`b6ca51a4`, and the retirement-set digest recomputes to
`949f3d93a6b1a57fc677939bfe9a9b33080409dd0e1b93cee7096ff432bb06d1`.

COMP-015 is correctly non-runnable. Its rankings, categorical gout-direction
verdicts, evidence counts, heuristic exposure calculations, H-AN-02
adjudication, and cross-material substitutions are prohibited from predictive
or decision use.

## Findings and resolutions

- The original model collapsed distinct materials, assays, compartments,
  evidence tiers, negative screens, expression changes, clinical safety data,
  and heuristic exposure calculations into a single comparison. Retirement,
  rather than recomputation, is the correct scope.
- Purified cordycepin remains an unranked mouse-model lead. The 2019
  *Eurycoma* ethanol extract, its compounds 4–7, pure eurycomanone, the 2022
  purified-eurycomanol study, and Physta remain separate materials and
  evidence records.
- No source supports a pure-eurycomanone cross-target verdict, a Physta urate
  mechanism, or a cross-material ranking. Physta's week-12 urate comparisons
  were null.
- The focused COMP page, computational index, validation plan, papers, and
  dependent wiki pages consistently enforce those boundaries.
- `wiki/gout-pathophysiology.md` no longer uses SLC2A9 as the causal bridge for
  fructose sensitivity, contains no contradictory strongest/second-strongest
  transporter ranking, and no longer points to a removed §1 section.
- The androgen–urate dual-axis idea survives as an exact-material Research
  Conjecture with explicit absence of direct dual-axis evidence and a
  discriminating experiment.
- The eurycomanol/PRPS idea survives separately as an isotope-resolved flux
  conjecture. A negative result kills only the tested material, lot, exposure,
  schedule, model, and decision rule.
- COMP-017 completed its separate exact-snapshot lifecycle; this retirement
  does not alter its core result or use it to select an intervention.
- No active stale COMP-015 verdict or personalized treatment instruction was
  found.

## Evidence checks

Primary-source checks support the surviving boundaries for cordycepin
(PMID 29422889), the 2019 *Eurycoma* extract and isolated compounds
(PMID 31920654), purified eurycomanol (PMID 34785103), and the Physta trial
(PMC8254464). Full text for PMID 34785103 was not directly available to this
reviewer; its exact values and material identity were already bound to the
Gate 1 primary-source review, while metadata and abstract were independently
confirmed here.

No COMP-015 result-bearing code was executed. The PDF and PNG correction figure
artifacts were visually inspected; the rendering script was not rerun.

## Required actions

None. Deletion of `synthesis/queue/comp-review-015.md` is authorized in the
same commit as this reviewed retirement.
