# COMP-038 corrective primary-source verification plan

**Approved:** 2026-07-24  
**Mode:** Static forensic repair; no result-bearing code execution  
**Canonical evidence home:** `wiki/tier-2-butyrate-assay-audit-computational.md`

## Decision to resolve

Repair the unsupported claim that a July 14, 2026 full-text pass verified both
leading COMP-038 candidates. Preserve only source-reconstructable method
details, distinguish source-study validation from Open Enzyme method
qualification, and leave the overall YELLOW verdict unchanged unless the two
named sources contradict it.

This plan does not rerun the 2026-05-20 assay-landscape search and does not
claim search completeness.

## Frozen source set

1. De Baere et al. 2013, PMID 23542733, DOI
   `10.1016/j.jpba.2013.02.032`.
   - Access: PubMed-indexed primary abstract reproduced by the U.S. EPA HERO
     record.
   - Allowed status: `primary_source_abstract_verified`.
   - Prohibited status: `full_text_verified`.
2. Gu et al. 2026, PMID 42041444, PMCID PMC13114974, DOI
   `10.3390/bios16040223`.
   - Access: NCBI PMC full text, including tables and supplement index.
   - Allowed status: `primary_source_full_text_verified`.
   - The 30-sample cohort may be described as an independent test cohort
     within the source study, not as independent external replication.

No secondary synthesis may supply a scientific claim. Agent-authored prior
text is a claim list to audit, not evidence.

## Required claim map

Create `outputs/primary-source-verification-2026-07-24.json`. For each retained
claim record:

- stable claim ID;
- source identity and access URL;
- access scope;
- exact method or result field;
- evidence level;
- article section, figure, or table where available;
- a bounded supporting excerpt or precise paraphrase;
- verification date and reviewer;
- disposition: retained, tightened, or retracted;
- Open Enzyme qualification boundary.

At minimum, audit:

- De Baere matrix, analytes, wavelength, extraction, acidification,
  calibration range, correlation/goodness-of-fit range, LOD/LOQ, and intended
  culture-supernatant use;
- whether “underivatized” is explicit;
- Gu hardware, electrode composition, butyrate pretreatment, acquisition mode,
  fresh-chip/triplicate handling, test-cohort size, GC-MS comparator,
  butyrate MAE/RMSE/R², ±5% count, bias/limits/p-values, data availability, and
  conflict-of-interest disclosure;
- the distinction between internal model-development test metrics and the
  independent fecal test-cohort metrics.

## Retraction rules

- Retract the claim that a July 14 full-text verification occurred.
- Retract “both candidates full-text verified.”
- Omit “underivatized” unless the accessible primary source states it
  explicitly.
- Do not translate an independent test cohort within one paper into external
  replication.
- Do not call HPLC-UV Tier 2.
- Keep SCFA/ELISA RED-provisional scoped to the bounded original search.
- Do not infer adoption, clinical validity, target-compartment exposure, gout
  efficacy, safety, or a universal matrix transfer.

## Outputs and propagation

COMP-owned outputs:

- add `outputs/primary-source-verification-2026-07-24.json`;
- revise `outputs/results.json` with explicit 2026-05-20 and 2026-07-24 layers;
- replace `outputs/summary.md` with a concise current summary;
- add the compact literature method receipt under `logs/lit-scans/`.

Proposed reader-facing and operational updates:

- `wiki/tier-2-butyrate-assay-audit-computational.md`;
- `wiki/computational-experiments.md`;
- `wiki/open-questions.md`;
- `wiki/validation-experiments.md`;
- `wiki/quantification-ladder.md` only if a stale classification remains;
- `operations/agentic-science-adoption.md`;
- `index.md`;
- `mkdocs.yml`.

No comparison ranking belongs on the focused evidence page. No creation-date,
sweep, review, or corpus-maintenance narration belongs in reader-facing prose.

## Acceptance criteria

The repair passes only if:

1. every retained quantitative or method claim maps to the verification
   artifact;
2. `results.json`, `summary.md`, and provenance distinguish the two dates and
   access scopes;
3. no active page says electrochemical stool profiling failed categorically;
4. culture-supernatant HPLC-UV and stool electrochemical/ANN remain separate
   validation tracks;
5. no active page calls De Baere full-text verified or calls the Gu cohort
   external independent replication;
6. exact-snapshot Gate 2 passes with no required action;
7. link, privacy, corpus-hygiene, and receipt checks pass.

If a claim cannot be reconstructed, retract it. The overall YELLOW result may
remain while its support becomes narrower and more accurate.
