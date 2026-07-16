---
title: Open-Source Research Platform
date: 2026-07-16
tags: [open source, reproducibility, research infrastructure, strains, protocols]
related: [open-enzyme-vision, track-template, computational-experiments, validation-experiments]
---

# Open-Source Research Platform

## Purpose

Open Enzyme applies open-source practice to a red-team research program for gout. The open artifact is not only a strain library. It is the current causal map, evidence corpus, intervention tracks, computational experiments, protocols, negative results, decision rules, and any reproducible biological designs that survive their gates.

The mission is defined in [open-enzyme-vision.md](./open-enzyme-vision.md). Koji and yeast designs are track outputs, not the platform definition.

## What “open” means

- Current research claims are readable and source-linked.
- Computational inputs, code, outputs, and exact review receipts are inspectable.
- Wet-lab protocols state controls, readouts, pass/revise/kill criteria, and safety constraints.
- Negative results remain when they are evidence needed to understand the current conclusion.
- Superseded prose and process history remain available through Git rather than duplicated archive pages.
- Contributors can challenge a real claim, reproduce an artifact, propose a better exploit, or improve a protocol.

Open does not mean that an experimental intervention is safe for unsupervised use. This is Phase 0 research, not a clinical or home-production protocol.

## Repository contract

| Software concept | Open Enzyme equivalent |
|---|---|
| Issue | Sourced open question, contradiction, or failure mode |
| Branch | Falsifiable intervention track |
| Source | Construct, formulation, model, protocol, and provenance |
| Test | Pre-registered assay or computational decision rule |
| CI | Link/privacy/integrity checks plus exact COMP review |
| Review | Independent adversarial inspection of claims and artifacts |
| Release | A configuration that passed its stated gate, with limitations |
| Deprecation | Track or configuration killed by evidence; prior version remains in Git |

Biology adds constraints software does not have: organisms evolve, batches vary, measurements have error, environments matter, and release can affect people or ecosystems. Reproducibility, containment, identity, activity, safety, and regulatory fit are part of the artifact—not optional documentation.

## Track portability

Each track uses the common [track template](./track-template.md). Detailed evidence should have one canonical home. A chassis page describes the chassis; a mechanism page describes the mechanism; a track page states why they are being combined and what would falsify the combination.

This prevents a favored implementation from becoming an implicit project requirement. If *A. oryzae* fails for a payload, the payload may move to yeast, a live biotherapeutic, cell-free production, a formulation, or be killed. If the payload fails, useful chassis evidence remains.

## Reproducible biological artifacts

A current strain, construct, or formulation artifact should include:

1. stable identifier and intended track;
2. host, payload, sequence or composition, and provenance;
3. build or preparation method;
4. exact inputs and dependencies;
5. identity, activity, purity, and stability assays;
6. safety and containment constraints;
7. operating conditions and known failure modes;
8. current evidence level and review status;
9. pass/revise/kill criteria;
10. license and contribution path.

Do not call a design “released” because its sequence is available. Release means it passed the gate stated by its track.

## Computational artifacts

The [COMP registry](../computational-experiments.md) contains reproducible computational experiments. New or materially revised COMPs require:

- a pre-run manifest and independent `GO` review bound to the exact design;
- a post-run manifest and independent clean review covering every output and proposed wiki update;
- an independent push review bound to the committed artifact, with separate propagation and synthesis eligibility.

Only the current executable design, outputs, and receipts remain in the live tree. Prior versions are available through Git.

## Distributed or community production

Community production is a hypothesis, not a consequence of open licensing. It must prove construct stability, operator-to-operator reproducibility, contamination detection, activity retention, release-assay fitness, and regulatory compatibility for the actual configuration.

The current threat model is [H09 — Community Fermentation Reliability](../hypotheses/H09-community-fermentation-reliability.md). Failure of H09 redirects that production option; it does not invalidate the project or require every track to be centrally or locally manufactured.

## Contribution workflow

1. Identify the canonical claim or track.
2. Add primary evidence, a reproducible result, or a clearly labeled mechanistic hypothesis.
3. State the local implication and blast radius.
4. Define the discriminating test or decision change.
5. Update dependent pages by link rather than copying the full argument.
6. Let bounded propagation check affected surfaces.
7. Use explicit full synthesis when a coherent research batch is ready for cross-domain analysis.

## Licensing and safety

Repository text and code use the project license. Third-party sequences, structures, datasets, and papers retain their own terms and provenance.

Nothing in the repository authorizes clinical use, environmental release, unsupervised genetic engineering, or distribution of regulated biological material. Each proposed artifact must satisfy the safety and legal constraints of its actual use.
