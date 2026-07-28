# Open Enzyme knowledge architecture

The system separates cheap, routine correctness from expensive, explicit discovery.

## Mission invariant

Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.

Every intervention is a falsifiable track. Koji is one track, not the project. A failed track should improve the exploit map and then stop consuming project identity.

## Event flow

```text
push to main
  ├─ publish current website (always)
  └─ knowledge-update coordinator
       ├─ identify changed COMP artifacts
       ├─ exact-snapshot COMP push review
       └─ bounded cross-page propagation if eligible

scheduled source surveillance
  └─ evidence radar
       ├─ deterministic ClinicalTrials.gov + WHO ICTRP delta monthly
       ├─ deterministic FAERS release-window delta quarterly
       ├─ spend zero model tokens when nothing relevant changed
       ├─ context-isolated review of exact changed records only
       └─ emit reviewed unresolved queue items only

explicit manual request
  └─ full-corpus distributed synthesis
       ├─ require propagation backlog = 0
       ├─ require exact eligible COMP receipts
       ├─ read every corpus section twice
       ├─ compare every domain pair
       ├─ reopen cited raw sections and exact COMP outputs
       ├─ independently audit premises and creative leaps
       └─ emit unresolved queue items only
```

## State

`logs/sweep-state.json` is compact operational state, not a narrative log. `logs/evidence-radar-state.json` is replaceable source state: the FAERS quarter cursor and exact-window backlog, retained monitor subjects, latest query faults, exact packet/review hashes, decision counts, and review cost. Clinical-trial comparison records live in deterministic compressed form at `logs/evidence-radar-clinical-records.json.gz`; an unchanged snapshot is byte-identical and does not create a monthly full-state diff. Compact literature-search method receipts live under `logs/lit-scans/*.json`; they preserve exact queries, coverage, and faults without duplicating the scientific synthesis. The full-corpus synthesizer deliberately excludes `logs/`.

- `last_successful_propagation`: the latest fully considered push batch;
- `last_successful_synthesis`: the latest completely covered corpus snapshot, including coverage digest and cost;
- `comp_reviews`: current exact-snapshot review eligibility by COMP;
- `unresolved_failures`: active failures only.

The two cursors are intentionally independent. A push may be fully published and propagated while remaining unsynthesized until Brian explicitly requests a sweep.

## Evidence radar

`evidence-radar.yml` runs two surveillance feeds without invoking propagation or full synthesis:

- monthly ClinicalTrials.gov API and WHO ICTRP searches discover new trials and compare current status, enrollment, dates, interventions, and posted-results flags against exact prior fingerprints;
- quarterly openFDA/FAERS searches scan the newly released receipt-date quarter for `GOUT`, `HYPERURICAEMIA`, `BLOOD URIC ACID INCREASED`, `GOUTY ARTHRITIS`, and `GOUTY TOPHUS`;
- report-level parsing keeps each FAERS drug's suspect/concomitant/interacting classification attached to that drug, rather than treating every drug and reaction in a report as a pair;
- deterministic collection happens before model review; zero-candidate runs cost zero model tokens;
- capped FAERS review batches retain an exact-window backlog and do not advance the quarter cursor until every eligible subject has a disposition;
- monitor decisions persist by subject with their rationale so later windows can accumulate or weaken the lead;
- a hash-bound, context-isolated review may dismiss, monitor, or emit one active action brief; raw packets and review output expire from CI after seven days.

Clinical-trial registrations are protocol/status evidence, not efficacy results. FAERS co-reports are unvalidated pharmacovigilance leads, not causality, incidence, or risk. A source fault remains visible in current state; the affected source is not called current. Neither feed triggers full synthesis. Reviewed radar actions enter `synthesis/queue/` only as verification tasks, and supported scientific claims still require their primary evidence and canonical wiki owner.

## Push-time propagation

`knowledge-update.yml` calls `comp-review.yml`, then `wiki-propagate.yml`.

Propagation:

- receives an explicit eligible path set;
- uses an explicit semantic-trigger batch cap (currently 10 in
  `wiki-propagate.yml`) and carries every unprocessed eligible path forward in
  compact state;
- ignores regenerable COMP code, binary intermediates, and machine outputs
  when a reviewed README, provenance page, or Markdown summary owns the
  propagatable scientific meaning;
- links to canonical evidence instead of copying exposition;
- updates direct dependents, hypotheses, dashboard/nav, and public surfaces as needed;
- refuses partial work beyond its path or cost cap;
- can advance on a verified no-op;
- never performs novelty synthesis.

A catch-up backlog may therefore require several bounded runs. Each run moves
the cursor to its own result commit, records the exact selected triggers, and
retains the deterministic remainder. No path is silently dropped and a
propagation-generated edit is not fed back into the next batch as a new
scientific trigger.

A changed completed COMP blocks its derived claims before any model call and remains blocked until the current artifact has an exact push review. Cost overflow defers the COMP rather than reusing a stale receipt. A deterministic quarantine retains the complete artifact and imported repository-local decision libraries, while excluding that COMP from execution, propagation, synthesis, and routine model review. Hash-bound non-runnable tombstones are removed from eligibility and verified deterministically against their retired Git trees; Gate-1-only COMPs do not enter result-bearing push review. The structured review independently states propagation and synthesis eligibility.

## Three COMP reviews

1. Authoring pre-run review binds code, inputs, provenance, rules, and planned outputs before result-bearing execution.
2. Authoring post-run review binds code/input/output plus every proposed interpretation before completion or commit.
3. Push review independently inspects the exact changed COMP and every referencing wiki/hypothesis surface before propagation or later synthesis.

The completed authoring lifecycle requires unchanged executable design between the pre-run and post-run snapshots and a current COMP artifact that still matches the post-run snapshot. A non-runnable tombstone may receive a Gate-2-only README correction while its hash-bound invalidation ledger remains unchanged. A legacy artifact that honestly predates Gate 1 may instead carry an exact independent post-run binding. Later canonical-page edits do not retroactively invalidate those historical gates; the current push review binds and audits the evolved pages. The reviews answer different questions and cannot substitute for one another. Current push receipts live under each active completed COMP's `reviews/` directory and replace prior receipts. A stable `synthesis/queue/comp-review-NNN.md` exists only while action is required.

Quarantine is reversible; final retirement is not. A new retirement requires a complete quarantined artifact, a context-isolated disposition review bound to its manifest, a unique-detail audit with current homes for every survivor, a closed dependency cascade, and Brian’s explicit decision. The deterministic checker caps a retirement batch at three and refuses a new tombstone while a retirement-cascade action remains open.

## Explicit full synthesis

`wiki-sweep.yml` runs `distributed-synthesis.py`. It preserves grounded creativity without loading one model with an ever-growing prompt:

1. deterministically split the full current corpus into section-addressable shards;
2. perform complete atomic extraction across all shards;
3. perform a second independent complete read focused on residue and missed details;
4. merge atoms without erasing disagreements;
5. examine every unordered domain pair;
6. require each candidate to separate grounded premises from any novel leap;
7. rehydrate each candidate from exact source spans;
8. for COMP-backed candidates, reopen the exact generated outputs covered by a current receipt;
9. independently review premise fidelity, novelty, upside, and the discriminating observation;
10. emit only reviewed unresolved actions.

The run fails closed unless every section has both reads, every domain pair is examined, and every candidate is rehydrated and reviewed. It is conservative about claims and deliberately aggressive about generating connections: a useful unsupported leap survives as a Research Conjecture when its premises are grounded and it has a discriminating observation. Direct evidence is not required for the leap; it is required before the leap can be restated as fact. Cost is tracked from provider usage where available and conservatively estimated otherwise; the workflow enforces an explicit cap.

Raw model output and review files are recovery artifacts with short CI retention. The repository keeps only active queue items and the compact coverage/cost receipt. Git preserves prior runs.

## Current-state content rules

- `wiki/`: current scientific understanding and active track state;
- `synthesis/queue/`: unresolved actions only;
- `logs/lit-scans/`: compact reproducibility receipts, never a second scientific narrative;
- `logs/evidence-radar-state.json` plus its deterministic compressed trial store: replaceable source cursors/fingerprints, retained monitors/backlogs, and latest review receipt, excluded from synthesis;
- COMP directories: exact reproducible artifacts plus current reviews;
- `reference/`: immutable external source material;
- Git: all revision and completed-action history.

Do not create completed-item directories, immutable review logs, per-run synthesis narratives, inline changelogs, or “for posterity” copies.

Reader-facing intervention pages follow one current-state sequence: exploitable gout weakness, evidence, source, delivery, exposure constraints, and falsification. A compact Research Conjecture may preserve a grounded but untested connection on the mechanism-owning page; it separates sourced premises, the unsupported leap, upside, and the cheapest discriminating observation. `open-questions.md` may link to it without copying it. Each focused intervention or chassis page stands on that track's own case; it does not use another track as a narrative foil. Cross-track rankings and comparison tables live only on portfolio surfaces such as `wiki/modality-chokepoint-matrix.md` and `wiki/chassis-pending-interventions.md`. Chassis analysis is local to an active production or delivery decision; it is never the default filter for whether an intervention belongs in the project. Editorial provenance and page-creation history live in Git, not prose. Research pages do not prescribe personalized dosing.

## Failure behavior

- Publication is independent and should still run when knowledge automation fails.
- COMP review failure blocks only affected derived claims.
- Propagation failure leaves its cursor unchanged and records an active failure.
- Full-synthesis failure leaves its cursor unchanged and uploads recovery artifacts.
- A migrated synthesis cursor without corpus and coverage hashes is marked unverified. `pending-synthesis-paths` then returns the complete tracked scientific source set, explicit path narrowing is ignored, and the next successful manual synthesis records fresh integrity hashes and clears the warning.
- A failed FAERS query or undisposed capped batch does not advance the quarter cursor. A failed trial-registry profile preserves that source's prior complete baseline; another fully successful registry may still advance independently.
- The watchdog notifies; it never authorizes or automatically dispatches a full synthesis.

## Primary commands

```bash
python3 scripts/sweep-state.py read
python3 scripts/sweep-state.py pending-propagation-paths
python3 scripts/sweep-state.py pending-synthesis-paths
python3 scripts/comp-review.py --help
python3 scripts/distributed-synthesis.py --help
python3 scripts/evidence-radar.py status
python3 scripts/evidence-radar.py check
```
