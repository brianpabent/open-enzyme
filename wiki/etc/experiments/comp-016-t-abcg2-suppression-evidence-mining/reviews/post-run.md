ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: c7b72e66e839a528590be34c6d9e31a0b35f691bd701ce89efe5e571a32b700b

# Independent comp review — comp-016

## Reviewed snapshot

Reviewer: Codex independent Gate-2 reviewer, 2026-07-29. I inspected all 14 entries in `reviews/post-run.manifest.json` completely. The manifest’s embedded canonical SHA-256 is `c7b72e66e839a528590be34c6d9e31a0b35f691bd701ce89efe5e571a32b700b`; every listed path was readable and matched its recorded byte count and content hash when inspected. The Gate-1 receipt records `PRE_RUN_GATE: GO` against canonical pre-run SHA-256 `260b5a07aa2f65b147b896e6cb8519c1a1c1caebff1999fafa25b315cb52fa3d`. All five pre-run design paths, byte counts, and SHA-256 values are exactly equal to their post-run design entries.

## Bottom-line verdict

Clean with limitations. The standard-library analyzer correctly answers the narrow preregistered question for the fixed 17-record inventory: the sole qualifying direct test is Slepnev 2023 (`in_vitro`, `increase`), no qualifying record has outcome `decrease`, and the computed result is therefore `NOT_DEMONSTRATED_IN_FIXED_INVENTORY`. The artifact consistently forbids a literature-wide absence claim, a healthy-human null, a physiological-human induction claim, a male export ceiling, rejection of the broader androgen–urate prior, or a clomiphene implication.

## Implementation and constraint closure

I traced all 17 input rows through strict validation, direct-test classification, aggregation, JSON construction, and Markdown rendering. A direct row must manipulate androgen, measure intestinal ABCG2, link the outcome to the same context, be citable, use a primary/full-text or official/primary-abstract tier, and record an outcome other than `not_tested`. Adjacent and unresolved rows are barred from carrying a target outcome. All count fields, IDs, corrected findings, boundaries, and forbidden inferences in both generated outputs derive from the fixed JSON; no load-bearing count is hard-coded.

The positive and negative branches are both implemented from `direct_suppression`: contrary `decrease` evidence would name the qualifying rows and change the result code, while the observed no-decrease branch stays explicitly bounded. This is an evidence-inventory validator, not a biological rate or exposure model, so substrate, mass-balance, localization, coproduct, and safety calculations are not applicable. Their analogues here—tissue/model context, manipulation/outcome linkage, nominal culture exposure, source tier, and human-translation limits—are explicit.

I executed the reviewed standard-library analyzer twice using the README command. Both runs reported `inventory_size=17`, `direct_in_vivo=0`, `direct_in_vitro=1`, `direct_suppression=0`, and `result_code=NOT_DEMONSTRATED_IN_FIXED_INVENTORY`. The two runs were byte-identical: `results.json` SHA-256 `e9e209a11864be6405f1e5b2f45c3b68cdcf3b2852dbbbe3fd09a56df8eec0b2`; `summary.md` SHA-256 `8dab7afa21d92ae08aa8bb0d5f7cac5c9415b2316c86c38af6834349dc0573bb`. The exact post-manifest check returned the reviewed canonical SHA, and `check-lifecycle` returned `authoring lifecycle valid`.

## Summary-fidelity audit

`results.json` and `summary.md` agree on 17 records, 16 citable records, 15 adjacent records, one unresolved row, one direct in-vitro row, zero direct in-vivo rows, and zero direct suppressions. They preserve the corrected Hoque 78% jejunal versus 44% renal Western comparison, Liu attribution and pharmacological Caco-2 boundary, Slepnev attribution and official-abstract boundary, and MacLean animal-model null.

All seven current interpretation surfaces keep the fixed-inventory result narrow. They remove the old 53%/88% Hoque values as evidence, correct Klyushova to Slepnev, avoid a serum-exposure multiplier, retain the healthy-human question as unresolved, preserve the broader androgen–urate prior, and route the next observation to total/apical ABCG2 plus polarized urate flux. Corpus searches found no operative COMP-014 dependency in COMP-016 or its seven bound surfaces. The independently sourced DAE lead remains on `wiki/medicinal-mushroom-complement-track.md` with DOI provenance, exact-material/exposure limits, and a discriminating test rather than COMP-014 authority.

## Reader-facing ownership audit

The focused COMP-016 page owns only the bounded historical scan and links to COMP-017 for corrected source detail. The ABCG2 and androgen pages own their respective mechanism boundaries; the computational registry remains an index; `open-questions.md` indexes unresolved work; and the methodology page uses COMP-016 only as a source-tier example. No COMP-016-derived cross-track rank, narrative foil, personalized treatment instruction, or duplicated long-form result was introduced.

## Conjecture preservation audit

The repaired artifact rejects only direct androgen suppression of intestinal ABCG2 as an established premise from this fixed scan. It does not reject the androgen–urate prior, genotype × hormone × inflammation stratification, an intestinal response question, or independently sourced fungal-material leads. The context-stratified ABCG2 Research Conjecture retains source-tagged animal and in-vitro premises, states that direct evidence for the connection is absent, and names a discriminating donor-derived intestinal-model experiment. No conjecture depends on COMP-014.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/README.md` | design | Yes | Narrow question, rules, forbidden scope, reproduction, and downstream set agree. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/analyze.py` | design | Yes | Strict validation; derived counts and polarity; both result branches closed. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/maintenance-repair-plan-2026-07-29.md` | design | Yes | Defects and authorized repair match the implementation. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/provenance.md` | design | Yes | Exact queries, access limits, correction sources, multilingual limit, and source tiers explicit. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/inputs/studies.json` | design | Yes | Seventeen complete rows; one direct increase; no direct decrease. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/results.json` | generated_output | Yes | Machine output exactly reflects the fixed table. |
| `wiki/etc/experiments/comp-016-t-abcg2-suppression-evidence-mining/outputs/summary.md` | generated_output | Yes | Human output matches JSON and preserves all forbidden inferences. |
| `wiki/abcg2-modulators.md` | proposed_update | Yes | Mechanism, exposure, genotype, and functional-flux boundaries are consistent. |
| `wiki/androgen-urate-axis.md` | proposed_update | Yes | Broader prior preserved; intestinal suppression and male-ceiling claims remain unconfirmed. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Registry reports a historical bounded scan and corrected COMP-017 ownership. |
| `wiki/etc/manual-literature-mining.md` | proposed_update | Yes | Uses COMP-016 as bounded overclaim correction, not literature absence. |
| `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` | proposed_update | Yes | Human baseline unresolved; corrected contexts and conjecture remain separate. |
| `wiki/open-questions.md` | proposed_update | Yes | Direct measurement remains open; COMP-014 contributes no evidence. |
| `wiki/t-abcg2-suppression-evidence-mining-computational.md` | proposed_update | Yes | Historical scope and surviving bounded result agree with the repaired artifact. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Fixed inventory size = 17 | `studies.json`; validator | Required length and rendered count | Directly inspectable fixed input | Pass |
| Citable = 16; unresolved = S15 | Input Booleans and tiers | Derived counts/list | Directly inspectable fixed input | Pass |
| Direct in-vivo = 0; direct in-vitro = S04 | Row classifications and strict validation | Determines direct-test set | S04 official publisher abstract tier | Pass |
| Direct suppression = 0 | S04 outcome `increase` | Determines result code and negative branch | Directly inspectable classification; source boundary explicit | Pass |
| Hoque 78% jejunal vs 44% renal | S01/provenance | Corrected source anchor only; not direct-test verdict | Recorded as COMP-017 primary-full-text verification | Pass within inherited verification boundary |
| Liu 100 µM, 48 h; LY294002 50 µM | S03/provenance | Corrected adjacent anchor | Recorded as COMP-017 primary-full-text verification | Pass; no physiological transfer |
| Slepnev 1/10/100 µM, 24 h, increase | S04/provenance | Sole direct-test polarity | Official publisher English abstract only | Pass at abstract tier |
| MacLean qualitative rat null | S10/provenance | Adjacent context only | Primary database abstract | Pass; no human-null transfer |
| No universal absence or male ceiling | `forbidden_inferences` | Rendered verbatim into both outputs | Preregistered scope control | Pass |
| DAE fungal lead is independent of COMP-014 | `wiki/medicinal-mushroom-complement-track.md` | Adjacent correction-cascade check only | Named DOI 10.1016/j.biopha.2022.113303; full-text rehydration remains a gate | Pass as bounded lead |

## Affected wiki pages

- `wiki/t-abcg2-suppression-evidence-mining-computational.md` — already consistent — historical bounded result only.
- `wiki/intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md` — already consistent — owns corrected sources, unresolved human baseline, and context-stratified conjecture.
- `wiki/computational-experiments.md` — already consistent — registry scope and supersession are explicit.
- `wiki/abcg2-modulators.md` — already consistent — no direct-suppression, physiological-induction, or male-ceiling upgrade.
- `wiki/androgen-urate-axis.md` — already consistent — renal/hormone prior survives while intestinal direction remains measured, not assumed.
- `wiki/open-questions.md` — already consistent — unresolved direct-human and functional-flux questions remain open; retired COMP-014 supplies no evidence.
- `wiki/etc/manual-literature-mining.md` — already consistent — bounded non-retrieval is used only to reject an overclaim at the reviewed-source tier.
- `wiki/medicinal-mushroom-complement-track.md` — already consistent — DAE is independently DOI-sourced and exact-material bounded.

## New connections or implications

The sole direct test in this inventory points upward in a pharmacological Caco-2 context, while healthy-rat baseline is qualitatively null and Q140K mice show a genotype-stressed intestinal defect. These discordant contexts support the existing Research Conjecture that genotype, hormone state, and inflammatory context may stratify intestinal ABCG2 response more usefully than a binary sex rule. Direct evidence for that composed connection is absent; the donor-derived apical-protein and polarized-flux experiment remains the discriminator.

## Required actions

1. None.

## Review limits

I did not perform a new literature search or independently re-fetch the four corrected primary/official source records; the review therefore preserves their explicit verification tiers and COMP-017 provenance rather than claiming new primary verification. I executed only the reviewed standard-library analyzer and exact manifest/lifecycle checks authorized by the review brief. The ordinary Gate-1 manifest check now reports the two expected `prior_output_baseline` changes because execution replaced the historical outputs; the lifecycle validator is the controlling post-execution check and confirmed exact pre/post design equality plus current post-snapshot binding. No binary artifacts were present.
