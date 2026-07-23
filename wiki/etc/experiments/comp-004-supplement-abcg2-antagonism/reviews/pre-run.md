PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 91b72ed87af76bb7ccd8746cdc240d62c1e3292ec00dd419dd725f4104d0c236

# Adversarial pre-run review — comp-004

- Reviewer: `/root/comp004_pre_review_v5` (fresh, context-isolated)
- Method: static, read-only inspection; no result-bearing logic was executed.
- Manifest: four design files, zero prior outputs; every recorded byte count and SHA-256 matched.

## Verdict

This bounded correction may run. It audits exactly three cited primary records and does not present them as a literature census. The design cannot estimate intestinal urate inhibition from nominal concentration, transfer drug-substrate kinetics to urate, assign a clinical-risk tier, rank compounds, or recommend a dose or formulation.

## Findings

- Cooray (PMID 15047179) supports a quercetin/BCRP functional signal with drug substrates in non-intestinal cells, not intestinal urate transport.
- Karibe (PMID 29358184) supports an intestinal curcumin/BCRP interaction in cynomolgus monkeys with sulfasalazine and rosuvastatin, not direct urate flux.
- Farabegoli (PMID 20149610) supports reduced mitoxantrone-assayed BCRP activity after EGCG exposure in tamoxifen-resistant MCF-7 cells without changed BCRP mRNA or protein, not an intestinal urate effect.
- The input gate validates the exact compound set, normalized duplicates, evidence and urate-status vocabularies, Boolean fields, nonempty substrates, and structured source metadata.
- Direct intestinal urate evidence has a prespecified contrary branch and cannot silently receive the default assay-required disposition.
- Both branches prohibit quantitative risk ranking.
- The deterministic standard-library script writes only the declared UTF-8 JSON and Markdown outputs.
- The downstream map correctly assigns transporter evidence and the bounded Research Conjecture to `abcg2-modulators.md`, EGCG-specific evidence to `egcg.md`, and the context-matched exposure/protein/attribution/barrier/viability/urate-flux experiment to `validation-experiments.md`.
- The invalidation boundary is narrow: the nominal occupancy ratios, predicted inhibition percentages, VERY_HIGH labels, and derived clinical uses fail; the individual interaction signals and untested time/exposure/metabolite/context connection survive.

## Required actions before execution

None.

## Review limits

The review was limited to the manifest-bound design and the named primary abstracts. It did not conduct a literature census or inspect future outputs and downstream edits; those require the post-run gate.
