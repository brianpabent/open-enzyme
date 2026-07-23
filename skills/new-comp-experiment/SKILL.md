---
name: new-comp-experiment
description: Create or materially revise a reproducible Open Enzyme computational experiment with exact-snapshot pre-run, post-run, and push review gates.
---

# New COMP experiment

A COMP is executable analysis, not a literature scan. Use `lit-scan` when the question is “what does the field say?”

## Artifact contract

Create `wiki/etc/experiments/comp-NNN-<slug>/`:

```text
analyze.py
inputs/                 fixed inputs and provenance.md
outputs/                deterministic machine and human outputs
reviews/
  pre-run.manifest.json
  pre-run.md
  post-run.manifest.json
  post-run.md
README.md
```

Also maintain the interpretive `wiki/<slug>-computational.md`, `wiki/computational-experiments.md`, and every affected hypothesis, validation, safety, or priority surface.

Reader-facing outputs follow the same ownership contract as the rest of the corpus: a focused page stands on its own evidence, sourcing, delivery, exposure constraints, and falsification gate. Cross-track rankings and comparison tables belong only in portfolio comparison surfaces. A COMP result is evidence for a decision, not permission to add editorial history, page-placement narration, personalized treatment instructions, or repeated exposition.

Audit claims and ideas separately. Correct an unsupported factual assertion, but preserve a grounded, useful untested connection as a compact **Research Conjecture** on its mechanism-owning page: sourced premises with evidence tags, the explicit unsupported leap, why it matters, and a discriminating observation. Research Conjecture is an epistemic status, not an evidence tier. A COMP kills only the exact claim and regime its preregistered rules test; do not erase adjacent ideas unless their required premise also fails.

## Method rules

- State the biological question, decision, model, assumptions, parameters, decision rules, sensitivity plan, planned outputs, and kill criteria before execution.
- Use the database that answers the question. Inhibition, transport/substrate status, pathway membership, sequence, and structure are different data problems. Follow `wiki/etc/chembl-cross-check.md` and `wiki/etc/ai-bio-tools-playbook.md`; document any new source in both provenance and the relevant tooling page.
- Fix inputs; record URL/accession/version/date and transformations.
- Prefer deterministic, reproducible code. Commit code, inputs, and outputs together.
- Treat computational results as priors, not substitutes for wet-lab validation.
- Grep-verify every load-bearing number against its primary source before writing it into a result-bearing page.
- Name the planned canonical evidence home and each downstream decision surface before execution. Plan only a local decision delta plus a link on dependents; route genuinely comparative outputs to portfolio comparison surfaces rather than inserting them into one track's page.
- Name which proposed claims the computation can decide and which adjacent connections remain conjectures regardless of outcome. Precommit narrow invalidation boundaries.
- For natural-product discovery, use mechanism, species/original-language, traditional-formula, and traditional-pathology query frames. That work is normally a lit scan unless an executable model follows.

## Gate 1: pre-run

Write code, inputs, provenance, decision rules, sensitivity plan, planned outputs, and reproduction instructions. Do not execute result-bearing logic.

From the COMP directory:

```bash
python3 ../../../../scripts/comp-review-manifest.py create --phase pre --comp-dir . --output reviews/pre-run.manifest.json
```

Give a fresh context-isolated reviewer the raw artifact, question, and decision—never predicted results or a preferred verdict—and require `scripts/comp-pre-run-review-prompt.md`.

Save reviewer identity, exact manifest SHA-256, verdict, findings, and resolutions in `reviews/pre-run.md`. Only `PRE_RUN_GATE: GO` with no required action passes. Any design change requires a new manifest and fresh review.

Immediately before execution:

```bash
python3 ../../../../scripts/comp-review-manifest.py check --manifest reviews/pre-run.manifest.json --review reviews/pre-run.md --required-line 'PRE_RUN_GATE: GO'
```

Then run the documented command twice and verify deterministic outputs.

## Gate 2: post-run

Draft every generated output and every proposed interpretation/propagation surface. Create the post manifest, repeating `--proposed-file` for every changed external surface:

```bash
python3 ../../../../scripts/comp-review-manifest.py create --phase post --comp-dir . --output reviews/post-run.manifest.json --proposed-file <path>
```

Use a different fresh context-isolated reviewer and `scripts/comp-review-prompt.md`. It must inspect all code, inputs, outputs, summaries, and proposed updates, including whether each reader-facing update has the correct owner and shape and whether unsupported claims were corrected without erasing useful conjectures outside the tested scope. Only `ACTION_REQUIRED: no` passes.

If a finding changes code, inputs, parameters, decision rules, model, or sensitivity plan, return to Gate 1 before rerunning. Narrative-only changes still require a new post manifest and review. Verify the exact post snapshot before commit.

## Gate 3: push review

The push coordinator independently reviews the exact changed COMP plus every referencing wiki/hypothesis page. It writes only current files under `reviews/push-review.*` and a stable `synthesis/queue/comp-review-NNN.md` when action is required.

The push review is a backstop, not a substitute for Gates 1 or 2. Its structured result independently controls:

- `PROPAGATION_ELIGIBILITY`
- `SYNTHESIS_ELIGIBILITY`

Any later COMP artifact change invalidates that exact-snapshot receipt until a new push review succeeds.

## Completion

A COMP is complete only when reproduction succeeds, both authoring gates pass on exact manifests, all interpretation surfaces match the outputs, evidence/limitations are explicit, claim-kill scope is narrow, surviving conjectures remain correctly bounded, focused pages remain track-local, comparative conclusions are routed to portfolio surfaces, and the push review does not block derived claims. Current receipts replace prior receipts; Git is the review history.
