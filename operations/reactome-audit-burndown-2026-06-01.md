---
title: Reactome Audit Burndown
date: 2026-06-01
status: active
tags: [reactome, pathway-audit, operations, today]
---

# Reactome Audit Burndown

Purpose: use the new repo-local Reactome tool to audit Open Enzyme's pathway-heavy wiki areas, find where Reactome can correct our maps, and identify narrow contribution opportunities back to Reactome.

This is an operational task list, not a research page. Mechanism claims belong in `wiki/` only after the pre-commit verification gate.

## Working Protocol

For each audit:

1. Search Reactome with 2-4 query phrasings.
2. Query the most relevant human stable IDs.
3. Pull contained events, ancestors, participants, and `regulatedBy` where useful.
4. Classify each finding as `already-modeled`, `under-modeled`, `absent`, `present-only-in-other-context`, or `not-Reactome-lane`.
5. Decide the action: no wiki change, wiki correction, new wiki note, validation-experiment update, or Reactome contribution candidate.
6. Verify any load-bearing PMID, DOI, residue, ChEBI, UniProt, kinetic constant, dose, or evidence-tier claim against primary sources before editing `wiki/`.

Scratch outputs go in `/tmp/reactome-audit/<slug>/`. Durable provenance, if worth committing, goes in `reference/generated/reactome/<slug>/`.

Core command pattern:

```bash
python3 tools/reactome/reactome_analysis.py search --query "QUERY" --output /tmp/reactome-audit/SLUG/search-QUERY.json
python3 tools/reactome/reactome_analysis.py query --id R-HSA-ID --output /tmp/reactome-audit/SLUG/query-R-HSA-ID.json
python3 tools/reactome/reactome_analysis.py contained-events --id R-HSA-ID --output /tmp/reactome-audit/SLUG/events-R-HSA-ID.json
python3 tools/reactome/reactome_analysis.py participants --id R-HSA-ID --output /tmp/reactome-audit/SLUG/participants-R-HSA-ID.json
```

## Today Queue

### P0-1 Complement CP0 / C5a Gout Axis

Wiki surfaces:

- `wiki/complement-c5a-gout.md`
- `wiki/medicinal-mushroom-complement-track.md`
- `wiki/upstream-complement-assay-format-mapping-computational.md`
- `wiki/upstream-complement-modulator-sweep-computational.md`
- `wiki/combined-cp0-systems-model-computational.md`
- `wiki/nlrp3-exploit-map.md`

Reactome starting queries:

- `complement C5`
- `C5a receptor`
- `classical complement pathway`
- `alternative complement pathway`

Done means:

- Map C5 cleavage, C5a/C5aR1 signaling, C3 convertase, C5 convertase, factor H, factor I, DAF/CD55, and C1-INH to Reactome IDs where present.
- Identify which CP0 claims are already modeled vs. Open Enzyme extrapolation.
- Flag any contribution candidates around gout/MSU-specific complement activation only if Reactome lacks the connection.

### P0-2 Gut Urate Transport / Lumen Sink

Wiki surfaces:

- `wiki/gut-lumen-sink.md`
- `wiki/abcg2-modulators.md`
- `wiki/androgen-urate-axis.md`
- `wiki/gout-genetic-variants.md`
- `wiki/uricase-abcg2-genotype-stratification-computational.md`
- `wiki/supplement-abcg2-antagonism-computational.md`

Reactome starting queries:

- `URAT1`
- `SLC22A12`
- `SLC2A9`
- `ABCG2`
- `urate transporter`

Done means:

- Map URAT1/SLC22A12, GLUT9/SLC2A9, ABCG2, and any urate transport reactions to Reactome IDs.
- Determine whether intestinal ABCG2 urate efflux is modeled or only ABCG2 protein/transporter context exists.
- Generate a short gap verdict for possible Reactome contribution: gut urate secretion / ABCG2-Q141K / intestinal sink.

### P0-3 Purine Catabolism / XO / Uricase Context

Wiki surfaces:

- `wiki/gout-pathophysiology.md`
- `wiki/fructose-connection.md`
- `wiki/prps-purine-biosynthesis-chokepoint.md`
- `wiki/uricase.md`
- `wiki/engineered-yeast-uricase-proposal.md`
- `wiki/uricase-variant-selection.md`

Reactome starting queries:

- `purine catabolism`
- `XDH`
- `hypoxanthine`
- `xanthine`
- `urate synthesis`

Done means:

- Map human purine degradation to urate and XDH/XO-related reactions.
- Identify where Reactome ends because humans lack uricase.
- Note whether engineered microbial uricase belongs only in Open Enzyme docs rather than Reactome human pathway curation.

### P0-4 IL-1 / Pyroptosis / GSDMD

Wiki surfaces:

- `wiki/nlrp3-inflammasome.md`
- `wiki/disulfiram.md`
- `wiki/gsdmd-pore-delivery-paradox.md`
- `wiki/chassis-pending-interventions.md`
- `wiki/gout-kill-chain-delivery-routes.md`
- `wiki/modality-chokepoint-matrix.md`

Reactome starting queries:

- `IL-1 family signaling`
- `interleukin-1 signaling`
- `pyroptosis`
- `gasdermin D`
- `caspase-1`

Done means:

- Map IL-1 family signaling, caspase-1 substrate cleavage, GSDMD pore formation, and pyroptosis to Reactome IDs.
- Check whether disulfiram/GSDMD is absent, modeled elsewhere, or contribution-worthy.
- Update the NLRP3 downstream chokepoint map only if Reactome exposes a real mismatch.

### P1-5 Autophagy / Mitophagy / Nrf2 Stress Response

Wiki surfaces:

- `wiki/lactoferrin.md`
- `wiki/carnosine.md`
- `wiki/medicinal-mushroom-compound-mapping-computational.md`
- `wiki/food-grade-hdaci-screen-computational.md`
- `wiki/chaperone-orthogonal-stacking.md`

Reactome starting queries:

- `autophagy`
- `mitophagy`
- `NFE2L2`
- `KEAP1`
- `glutathione`

Done means:

- Separate direct NLRP3 inhibition from upstream stress-response modulation in stack logic.
- Identify whether Nrf2/autophagy claims in wiki should link to Reactome anchors.
- Flag any over-broad "NLRP3 inhibitor" labels that are really upstream pathway modulation.

### P1-6 Barrier / Tight Junction / Gut Inflammation

Wiki surfaces:

- `wiki/blood-barrier.md`
- `wiki/blood-barrier-exploits.md`
- `wiki/sibo.md`
- `wiki/lactoferrin.md`
- `wiki/engineered-lbp-chassis.md`

Reactome starting queries:

- `tight junction`
- `epithelial barrier`
- `TGF beta tight junction`
- `intestinal inflammation`
- `TLR4`

Done means:

- Map tight-junction and TLR4/barrier-relevant human pathways.
- Decide whether Reactome is useful for this area or whether most evidence is microbiome / tissue-physiology literature outside Reactome's lane.

### P1-7 Digestive Enzyme / EPI Biology

Wiki surfaces:

- `wiki/digestive-enzymes.md`
- `wiki/digestive-enzyme-optimization.md`
- `wiki/enzyme-deficit-deep-dive.md`
- `wiki/enzyme-quantification-protocol.md`

Reactome starting queries:

- `amylase`
- `lipase`
- `protease digestion`
- `pancreatic secretion`
- `digestive enzyme secretion`

Done means:

- Map human digestion reactions for amylase, lipase, and protease context.
- Decide whether this helps EPI mechanism pages or is too generic for microbial enzyme engineering.
- Capture any useful enzyme substrate/product vocabulary for assay design.

### P1-8 Bile Acid / Chaperone / ABCG2-Q141K Adjacency

Wiki surfaces:

- `wiki/abcg2-q141k-chaperone-screen-computational.md`
- `wiki/abcg2-modulators.md`
- `wiki/chassis-pending-interventions.md`
- `wiki/genotype-informed-supplement-workflow.md`

Reactome starting queries:

- `bile acid metabolism`
- `TUDCA`
- `ursodeoxycholic acid`
- `protein folding`
- `ER stress`

Done means:

- Determine whether Reactome can anchor UDCA/TUDCA/bile-acid context for Q141K chaperone hypotheses.
- Avoid overclaiming: this is likely adjacency mapping, not direct ABCG2-Q141K evidence.

## Cross-Cutting Contribution Gap Sweep

After the pathway audits, run no-hit or context-only searches for candidate molecules already important in the wiki:

- `oridonin`
- `tranilast`
- `beta-hydroxybutyrate`
- `disulfiram`
- `echinatin`
- `dapansutrile`
- `MCC950`
- `avacopan`
- `anakinra`
- `colchicine`

Done means:

- For each candidate, classify Reactome status.
- Add true candidates to `operations/reactome-contribution-nlrp3.md` or create a new contribution dossier for non-NLRP3 pathways.
- Do not create Reactome contribution claims from no-hit search alone; inspect target event regulation first.

## Tracking Table

| Audit | Status | Reactome anchors | Wiki action | Contribution candidate | Notes |
|---|---|---|---|---|---|
| Complement CP0 / C5a | not started | TBD | TBD | TBD | P0 |
| Gut urate transport / lumen sink | not started | TBD | TBD | TBD | P0 |
| Purine catabolism / XO / uricase | not started | TBD | TBD | TBD | P0 |
| IL-1 / pyroptosis / GSDMD | not started | TBD | TBD | TBD | P0 |
| Autophagy / mitophagy / Nrf2 | not started | TBD | TBD | TBD | P1 |
| Barrier / tight junction / gut inflammation | not started | TBD | TBD | TBD | P1 |
| Digestive enzyme / EPI biology | not started | TBD | TBD | TBD | P1 |
| Bile acid / chaperone / ABCG2-Q141K | not started | TBD | TBD | TBD | P1 |
| Cross-cutting molecule gap sweep | not started | TBD | TBD | TBD | after pathway audits |

## End-of-Day Closeout

- Update this tracking table with completed audits.
- Move durable Reactome outputs worth keeping into `reference/generated/reactome/`.
- Update affected wiki pages with only verified claims.
- Update or create contribution dossiers in `operations/`.
- Run `git diff --check`.
- Commit the batch locally.
- Do not push until the batch is coherent and Brian says to ship it.
