PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: b6d68757d7b9aca6ac97608f27497c2ec7672ba6365d1a5c23c714d67d48f6cf

# Adversarial pre-run review — comp-017

Reviewer: Claude Opus 4.8 via a fresh isolated CLI context with no tools, session persistence, prior review, or preferred verdict. The exact package contained the manifest, all six design files, and both historical outputs as prior-output baselines.

## Verdict

The corrective audit may execute unchanged. The design deterministically refuses the unanswerable direct-human question, fails closed on input/schema drift, keeps Animal Model and In Vitro evidence from substituting for healthy-human data, and removes the historical attribution, magnitude, exposure, and interpretation errors. No design, code, input, rule, sensitivity, or output-contract change is required.

## Load-bearing findings

- Missing sex-stratified GTEx and HPA intestinal values correctly force `DIRECT_HUMAN_BASELINE_UNRESOLVED`; the 1.5-fold threshold is not tested.
- The historical GTEx HTTP 403/`host_not_allowed` trace is preserved as an operational explanation, not biological evidence.
- Hoque's primary-verified like-for-like Western comparison is 78% jejunal versus 44% renal reduction in the Q140K mouse model.
- The old 53%/88% sentence is correctly excluded: the article-representation audit and publisher source-data workbook do not support it, and repository provenance shows that it entered COMP-016 at explicitly unverified search-summary tier before historical COMP-017 mislabeled it as verbatim.
- Slepnev, Liu, and MacLean records retain their declared verification tiers and do not support physiological hormone magnitude, clomiphene effects, a pan-male rule, or Q141K-conditioned gut-uricase response ordering.
- Planned downstream edits are limited to correction/status plus links to the single evidence home.

## Reviewer limitation and receipt correction

The reviewer performed static inspection and did not execute the code, recompute hashes, or retrieve sources. Its narrative incorrectly stated that `inputs/provenance.md` was absent from the manifest and counted five design files. The exact manifest contains six design entries and includes `inputs/provenance.md` at SHA-256 `25103445173b6a9d9c4d362a42328feaee0256f069dc7254de3aee8742787834`. This clerical review-text error does not alter the `GO` verdict or create a design gap.

## Required actions before execution

None.
