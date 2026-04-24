---
title: "Linter Design — Document Lint + Falsification Lint (Two-Linter Architecture)"
date: 2026-04-24
tags:
  - linter
  - falsification
  - document-lint
  - hypothesis-commit
  - rigor
  - methodology
  - infrastructure
  - design-doc
  - severity-levels
  - failure-mode-ontology
  - calibration
  - n-of-1
related:
  - hypotheses/README.md
  - hypotheses/H01-ward-dual-cassette.md
  - koji-endgame-strain.md
  - chembl-cross-check.md
  - self-experiment-protocol.md
  - synthesis.md
  - open-questions.md
  - validation-experiments.md
sources:
  - "Brian Abent / ChatGPT-generated brief: falsification-lint-brief.md (2026-04-24, not in repo — personal Downloads)"
  - "Refinement conversation 2026-04-24 (preserved in git history)"
status: design
---

# Linter Design — Two-Linter Architecture

## Intro — The Core Insight

Generation and rigor are different modes of thought. Fusing them into a single pipeline strangles both: generation becomes cautious, rigor becomes dilute, and the entire apparatus becomes the 500-rule ESLint nobody actually runs. The trap most ML-bio platforms fall into is exactly this fusion — a "scientific discipline" layer bolted upstream of ideation, which filters out the non-obvious four-hop speculative connections that are the point of generation in the first place.

The framing from the original brief is load-bearing:

> *Generator stays free. Linter catches what we'd regret later.*

The refinement landed in the 2026-04-24 conversation: **this is actually two linters, not one.** One runs always, non-blocking, on every document change, and checks that documents are well-formed *as documents*. The other runs on demand, per committed hypothesis, and generates a Falsification Card probing whether the hypothesis is well-formed *as a scientific claim*. They share a philosophical stance (opt-in rigor, severity levels, honesty about confounding) but have different triggers, scopes, rule sets, and output surfaces.

Splitting into two gives each one a single job and prevents the instinct to merge everything into one super-pass. This page is the design document for both.

---

## §1 — Two Linters, Not One

### Document Lint

- **Trigger.** Always-on; runs per file change, per commit, or per PR.
- **Scope.** Every `wiki/*.md` file, plus `index.md`, `mkdocs.yml`, top-level README.
- **Job.** Check that documents are *correct as documents*. Evidence-level tags are present. Inline provenance is cited. Cross-refs resolve. CP labels conform to the v1.2 exploit map (no orphan "CP5" without the a/b sub-branch). Rodent IC50 citations carry a species-gap caveat. New pages appear in `mkdocs.yml` nav. YAML frontmatter is complete. No inline revision-history sections.
- **Output surface.** Non-blocking reports / PR annotations. Never breaks a build. Findings are advisory — the author decides what to address.
- **Rule types.** Mix of regex-level (cheap, deterministic, free) and Claude-semantic (token-priced, fuzzy). v0 starts with regex; semantic rules layer in as needed.

### Falsification Lint

- **Trigger.** On-demand, user-invoked. The user has committed to a hypothesis — written it down in `wiki/hypotheses/H0N-*.md` — and explicitly asks the linter to scrutinize it.
- **Scope.** One hypothesis artifact at a time. Reads the committed hypothesis file plus the wiki pages it cross-references.
- **Job.** Generate a Falsification Card: assumption stack + killshot menu + pre-committed thresholds + failure-mode tags. Surface the *cheapest upstream killshot that would collapse the branch* — the hero interaction per the brief.
- **Output surface.** The Falsification Card itself (rendered into the hypothesis file, or into a companion artifact). Advisory — does not gate hypothesis creation. Does not determine "truth," only surfaces tests that would update belief.
- **Scoring.** Ranks killshots by approximately `(kill_probability × information_weight) / (cost × time_penalty)`. Tracks survival score over time with decay and retraction.

### They Are Complementary, Not Redundant

Document Lint keeps the surface clean: every wiki page is a well-formed research artifact, evidence levels tagged, cross-refs resolve, nav is coherent. Its rules are *broad* (many rules, light checks) and *cheap* (mostly regex).

Falsification Lint digs deep on one specific claim: assumption stack, killshot menu, failure-mode independence, pre-committed thresholds, survival tally. Its rules are *narrow* (one hypothesis at a time) and *expensive* (semantic reasoning, user-invoked).

Neither linter pre-filters ideation. Pass 2 sweep synthesis stays promiscuous. New wiki page creation stays promiscuous. Brian's riffs stay promiscuous. The linters run where they pay — clean documents always, hypothesis scrutiny on demand — and nowhere else.

---

## §2 — Design Principles

Directly from the brief, adapted to the Open Enzyme context:

1. **Generator stays promiscuous.** Pass 2 sweep synthesis (the second daemon pass that prepends new dot-connections to `wiki/synthesis.md`), new wiki page creation, Brian's 3 a.m. speculation riffs — untouched by either linter. The generator's failure mode is *not generating*; a lint that discourages dot-connecting is a lint that kills the product.

2. **Rigor is opt-in.** Document Lint findings are non-blocking reports/annotations. Falsification Lint is user-invoked per hypothesis. Neither gates a commit, blocks a build, or pre-filters upstream. The user decides when rigor is worth the cost.

3. **Severity levels matter.** Hard / soft / style. Without severity, everything becomes an equal-priority warning and the lint loses signal. Severity maps onto the evidence-level tags already in use across the wiki (Clinical > Animal > In Vitro > Mechanistic Extrapolation): a *hard* failure is a claim tagged at a higher evidence level than the cited source supports; a *soft* warning is missing or ambiguous provenance; a *style* note is formatting preference.

4. **Honesty about confounding is a feature, not a failure.** Especially for n=1 self-experiments where Brian is stacking koji + supplements + clomid + diet changes simultaneously by necessity. The linter logs concurrent interventions, flags that attribution is weak, and proposes single-variable follow-ups once the combined stack shows signal. Pretending a messy real-world experiment is clean is the worse outcome; tracking the mess honestly is the better one. See §7.

5. **The hero moment is the redirect.** The product's killer demo is when Falsification Lint says *don't run the expensive assay — here's a cheap upstream killshot that could collapse the whole branch*. User runs the cheap test. Branch dies. Expensive assay never happens. Every other feature of the linter justifies this moment. For H01 (see `hypotheses/H01-ward-dual-cassette.md`), that cheap upstream killshot is the literature/patent landscape deep-dive — $0 cost, 1 week, kill probability 0.3 on a root assumption — which is why it scores highest in the menu despite being the least "experimental" option.

---

## §3 — Document Lint Rule Catalog (v0)

Rules are tagged with severity (hard / soft / style) and detection method (regex vs. Claude-semantic). Regex rules are free and deterministic; Claude-semantic rules cost tokens and are fuzzy. v0 starts with the regex set; semantic rules layer in incrementally.

| Rule | Severity | Detection | Fix hint |
|---|---|---|---|
| `evidence-tag-required` | hard | regex (claim-pattern grep + nearby-tag check); Claude for ambiguity | Every substantive claim carries one of: Clinical / Animal Model / In Vitro / Mechanistic Extrapolation. If a claim has a citation but no tag, flag. |
| `inline-provenance` | soft | regex (`(source: <name>)` or PMID format) | New claims should cite provenance inline. Accept `(source: filename.md)`, `PMID: nnnnnnnn`, `[DOI](...)`. |
| `cross-ref-resolves` | hard | regex + filesystem existence check | `[text](./path.md)` targets must exist. Dangling refs flagged with the target path. |
| `mkdocs-nav-coverage` | hard | regex (scan `mkdocs.yml` nav + `wiki/*.md` filesystem) | Every `wiki/*.md` must appear in `mkdocs.yml` nav, or in an explicit `nav-excluded.txt` allowlist. |
| `chokepoint-label-v1.2` | soft | regex | References to "CP5" without `a`/`b`, or "Chokepoint 6" without `a`/`b`, are ambiguous post-v1.2 exploit map. Flag for disambiguation. |
| `species-gap-caveat` | soft | Claude-semantic | Rodent IC50 citations (`mouse`, `rat`, `murine`, `rodent` near `IC50`, `EC50`, `Ki`) require nearby species-gap caveat or link to `chembl-cross-check.md`. Examples: dapansutrile 1000× mouse→human ratio; BCP rat 100–400 mg/kg → human 50–200 mg/day 20–50× under-dose. |
| `no-inline-revision-history` | hard | regex | Forbidden section headers: `## Changelog`, `## Revision History`, `## Change Log`, `## History`. Git is the revision history per project convention. |
| `frontmatter-complete` | hard | regex (YAML block parse) | Required keys: `title`, `date`, `tags`. Strongly recommended: `related`, `sources`, `status`. |
| `standard-markdown-links` | style | regex | Prefer `[text](./path.md)` over `[[wiki-links]]` for GitHub rendering. `[[wiki-links]]` are Obsidian-only. |
| `claim-calibration` | soft | Claude-semantic | (Optional, v0.5+.) Does the claim's linguistic strength match the cited evidence level? "Lactoferrin *crushes* NLRP3" cited to in vitro is a mismatch; "*may suppress* NLRP3 (in vitro)" is calibrated. Flag strength-mismatches for author review. |
| `orphan-page` | soft | regex + filesystem | A wiki page not referenced by any other wiki page, `index.md`, or `mkdocs.yml` is probably discoverability-broken. |
| `duplicate-frontmatter-date` | style | regex | `date:` frontmatter values that match another page's exactly might indicate copy-paste errors. Low-priority sanity check. |

**v0 scope decision.** Implement the regex-level rules first: `evidence-tag-required` (regex heuristic only, not semantic), `cross-ref-resolves`, `mkdocs-nav-coverage`, `no-inline-revision-history`, `frontmatter-complete`, `standard-markdown-links`. These are free, deterministic, and cover ~80% of the consistency wins. Claude-semantic rules (`species-gap-caveat`, `claim-calibration`) layer in once the regex set is stable and we have calibration on token cost.

**Existing infrastructure.** `chembl-cross-check.md` is effectively an already-deployed linter for one dimension (rodent-IC50 cross-check against ChEMBL human-target data). It's user-invoked, quarterly. Document Lint formalizes this pattern: existing tools stay, new lint rules slot in alongside.

---

## §4 — Falsification Card Schema

Each hypothesis lives at `wiki/hypotheses/H0N-slug.md` and conforms to this schema.

### Frontmatter

```yaml
---
id: H0N
title: <one-line claim>
committed: YYYY-MM-DD
status: Alive | Killed | Pending | Retracted
survival_count: N
---
```

- `id` — zero-padded two-digit (H01, H02, …, H99). Three digits when needed.
- `title` — single sentence, mechanistic, precise. This is the public one-liner.
- `committed` — the date the hypothesis was first written to the file. Subsequent edits log in git.
- `status` — one of:
  - **Pending** — committed, not yet tested.
  - **Alive** — at least one killshot executed, claim survived.
  - **Killed** — at least one killshot executed, claim falsified per its pre-committed threshold.
  - **Retracted** — a killshot result was later invalidated (bad control, wrong substrate batch, assay artifact); status reverts based on remaining valid killshots.
- `survival_count` — running tally of valid (non-retracted) killshots survived.

### Body Sections

**Claim.** One sentence. Mechanistic. Precise. No hedge words unless they carry information. The claim is load-bearing for every downstream section.

**Assumption stack.** Three to seven priors the claim rests on. Each tagged with severity:
- **load-bearing** — if wrong, the claim collapses.
- **supporting** — if wrong, the claim is weaker but recoverable.
- **stylistic** — if wrong, the claim is unaffected; included for completeness.

Each assumption carries a brief justification (1–3 sentences) and ideally a citation or pointer to the wiki page where it's defended in depth.

**Killshot menu.** Table with columns:
- `#` — killshot identifier (1, 2, 3, …).
- `killshot` — the observation or test that would falsify the claim (or a specific assumption).
- `cost` — dollars or compute budget.
- `weeks` — time to run.
- `kill_pr` — estimated kill probability, 0–1. User-entered; calibrated over time per §6.
- `info_weight` — how much of the hypothesis tree collapses if this kills. Root assumption = 1.0; leaf = 0.1.
- `failure_modes` — tags from the §5 ontology.
- `score` — computed as `(kill_pr × info_weight) / (cost × time_penalty)`. Sorted descending.

The scoring math is intentionally un-baroque. The goal is *ordering better than intuition*, not Bayesian purity. v0 uses a simple multiplicative form; refinements layer in later.

**Failure-mode ontology reference.** Link to §5 of this page. Each killshot is tagged with 1–3 failure modes it probes.

**Pre-committed thresholds.** Declared *before execution*. What counts as **Alive** vs. **Killed** vs. **Pending** (intermediate). Quantitative where possible: "killed if X < threshold"; "survived if Y > threshold"; "pending if X–Y intermediate, plan follow-up."

**Kill switches.** Safety/sanity stops. Example: abort if aflatoxin detected above regulatory limit during koji engineering; abort if n=1 self-experiment triggers a red-flag halt criterion per `self-experiment-protocol.md`.

**Log.** Table recording actual executions: date, killshot run, outcome, notes. Append-only.

**Survival score.** Current value. Computed per §6: `Σ(weight × time_decay)` over valid survivals. Recorded as a number plus qualitative tag.

**Retraction history.** If any killshot result was later invalidated, document it here. This is what distinguishes a hypothesis that survived four fresh independent attacks from one that survived four redundant attacks that were later found to share a confound.

---

## §5 — Failure-Mode Ontology

Independence between killshots is defined as *non-overlapping failure modes*, not non-overlapping methods. Two tests that share a failure mode (e.g., both assume the same training distribution) are not independent even if the methods look different. The ontology is the vocabulary for that independence check.

### v0 Ontology — Extended from the Brief

1. **Species-gap translation.** Mouse/rat data extrapolated to human. Rodent IC50, dosing, receptor affinity, metabolic fate. Examples from this wiki: dapansutrile 1000× mouse→human efficacy ratio (NLRP3 inhibitor screen); GPR32 is a pseudogene in rodents but a functional resolution receptor in humans (SPM pathway); BCP rat 100–400 mg/kg → human 50–200 mg/day under-dose by ~20–50× (cannabinoids/terpenes).

2. **Chokepoint collapse.** Targeting CP2 when the actual bottleneck is CP0. The upstream trigger dominates and downstream interventions are low-leverage. Example: blocking NLRP3 assembly (CP2) matters less if C5a priming (CP0) is still driving the cascade; uricase trigger-elimination is a CP0-adjacent move that resolves the collapse (koji-endgame-strain.md §2.1).

3. **Assay specificity.** NLRP3 vs. NLRC4 vs. AIM2 readout confusion. A compound flagged as "NLRP3 inhibitor" based on IL-1β reduction might be hitting NLRC4 or AIM2 or an upstream shared component. Assay specificity failures manifest as false-positives in mechanism.

4. **Substrate availability / compartment mismatch.** Uricase needs luminal uric acid to act on; luminal UA depends on ABCG2; ABCG2 is androgen-suppressed in men with high T. A mechanism that works in principle fails when the substrate isn't actually present in the compartment where the enzyme lives. (See `gut-lumen-sink.md`, `androgen-urate-axis.md`.)

5. **Expression / localization mismatch.** Protein produced but not secreted. Secreted but not folded correctly. Folded but mis-glycosylated. The gene is there, the transcript is there, the polypeptide is there, but the functional protein in the right compartment isn't. The §3.3 concerns for Ward 1995 dual-cassette (KEX-2 capacity, shared secretion machinery, solid-state glycosylation) live here.

6. **Kinetics / concentration mismatch.** In vitro IC50 is achievable in a test tube but not at any pharmacologically feasible in vivo concentration. Oral bioavailability gates it; tissue partitioning gates it; metabolic clearance gates it. The IC50 number is right but the story around it is wrong.

7. **Dose-translation scaling.** Body-surface-area / mg-per-kg extrapolation from rodent to human gives a dose that's not actually what was tested. A rat 100 mg/kg × human BSA-scale ≠ human 100 mg/kg. BCP is the canonical example (see §5.1 of ontology — species-gap overlaps here but the scaling math is separable).

8. **Compound purity / formulation.** Curcumin bioavailability pre-nanocarrier. Quercetin aglycone vs. glycoside. Resveratrol trans vs. cis. "Curcumin doesn't work" conclusions often reflect formulation failures, not molecular failures.

9. **Published-literature-gap / training-distribution.** The claim rests on a published precedent that doesn't actually cover the specific case. Ward 1995 is *A. awamori* single-protein — layering a second cassette in *A. oryzae* on rice koji is outside the training distribution. Killshot: literature/patent landscape deep-dive before wet-lab work. This mode is usually the cheapest upstream killshot and the highest-leverage one.

### Extensibility

The ontology is a living list. New modes land when a novel failure pattern shows up in practice. Editing this list is a sweep-triggering event (update `linter-design.md`, update any hypothesis cards that should now be tagged with the new mode). The v0 rule: don't invent modes prematurely; let failure patterns demand the vocabulary.

### Independence Calculation

```
independence(K1, K2) ≈ 1 − |fail_modes(K1) ∩ fail_modes(K2)| / |fail_modes(K1) ∪ fail_modes(K2)|
```

Jaccard distance on failure-mode sets. Two killshots that share all failure modes are dependent (independence = 0). Two killshots that share none are fully independent (independence = 1). The survival-score weight §6 uses this to avoid double-counting when the same failure-mode vector has been probed twice.

---

## §6 — Survival Score, Calibration, Retraction

Adapted from the brief; concise treatment here.

### Survival Score

```
Survival_Score = Σ (weight_i × time_decay_i)   over valid (non-retracted) killshots survived
weight_i = info_weight_i × independence_i
time_decay_i = exp(-λ × (t_now − t_i))   with λ tuned so a 2-year-old survival halves
```

Three properties the formula enforces:

1. **Accumulation.** Surviving more attacks adds weight. A hypothesis that has survived five independent killshots scores higher than one that survived one.
2. **Decay.** Old survivals weaken. Models get stale, data gets stale, assumptions drift. A killshot run in 2022 with 2022 assumptions is not equivalent to one run today.
3. **Retraction.** A killshot result later invalidated is removed from the sum. The retraction is logged; the hypothesis status is recomputed.

Distinguishes: four fresh independent attacks survived vs. four redundant attacks two years ago.

### Calibration

User-entered `kill_pr` values are scored over time. For each executed killshot: record predicted `kill_pr` and actual outcome (killed / survived). Bucket predictions, compute calibration curve (predicted vs. actual kill rate per bucket).

Visible, not hidden. Trains the user into a better forecaster. Corrects systematic over- or under-confidence. For the n=1 Brian-only regime, the curve is noisy (few data points), but the *direction* of bias becomes visible quickly. Team-scale calibration is Phase 2+.

### Retraction

Post-execution invalidation paths:
- Bad control (killshot's negative control was contaminated).
- Wrong substrate batch (enzyme was degraded before the assay ran).
- Assay artifact (readout was a false signal from buffer, plastic, autofluorescence).
- Model bug (in silico killshot used wrong parameter set).

Retraction is a visible log entry, not a silent edit. Git-native — the retraction commit carries the rationale.

### Pre-Commit Hashing — Addressed by Git

The brief calls for hashing the `{claim, killshot_menu, thresholds}` at commit time to prevent silent post-hoc editing. For markdown-backed hypotheses in git, **the git SHA of the commit that first wrote `wiki/hypotheses/H0N-*.md` is the hash.** Any edit creates a new commit with a visible diff. A separate hash layer would be redundant.

Convention: the hypothesis file's first commit establishes the pre-committed state. Subsequent commits log edits with commit messages like `H01: adjust threshold for lactoferrin titer (rationale: Ward 1995 was mg/L submerged, rice koji is pore-fluid equivalent)`. The git log is the audit trail.

---

## §7 — n=1 / Confounded-Run Honesty

Real experiments — especially personal-health n=1 where the subject is Brian — stack interventions by necessity. Brian adds koji, supplements, clomid titration, diet changes, training changes, all on overlapping timelines. Pretending any single intervention can be cleanly attributed is a lie; the honest framing is: *multiple interventions ran concurrently, attribution is weak, here's what we'll do about it*.

Falsification Lint supports this explicitly:

1. **Log all concurrent interventions.** Each hypothesis's execution log records *everything active at the time*, not just the variable being tested. Date ranges, dose ranges, and any deviations from baseline. This is a liability if read as "proof" and an asset if read as "context for signal interpretation."

2. **Flag attribution weakness.** If signal appears in a n=1 run where three interventions overlapped, the Falsification Card flags attribution as weak and declines to call the hypothesis Alive or Killed. Status stays Pending; the signal is logged as "interesting" but not dispositive.

3. **Propose single-variable follow-ups.** Once the combined stack shows signal, propose a subtractive A/B: remove one intervention for 2–4 weeks, observe whether the signal persists. If yes, that intervention wasn't load-bearing; if no, it was. This is the n=1 equivalent of a dropout experiment.

Cross-reference: `self-experiment-protocol.md` §7 (Logging and version control — the operational mechanics for intervention logging) and §6 (Red-flag halt criteria — the kill switches for n=1). The protocol already anticipates intervention stacking; Falsification Lint is the scientific-rigor counterpart to the protocol's operational rigor.

---

## §8 — What Document Lint Won't Check

- **Creative generation quality.** Pass 2 synthesis is a generation task. It produces new dot-connections, which are often speculative-by-design. Lint does not grade them.
- **Taste / prose quality.** "Is this well-written?" is not a lint rule. Voice, rhythm, clarity at the sentence level are author judgment.
- **Whether a hypothesis is "good."** That's Falsification Lint's domain, and even there the output is advisory. "Good" is not a lint category.
- **Anything that discourages document production.** If a lint rule makes authors write less, the rule is wrong. The bias is always toward *more documents, lint catches later*, not *fewer documents, lint catches upfront*.

---

## §9 — What Falsification Lint Won't Do

- **Gate hypothesis generation.** A user can write as many half-formed hypotheses as they want. Falsification Lint runs only on committed ones, only on request.
- **Block commits.** Writing a bad hypothesis file doesn't fail CI. The linter annotates; it doesn't reject.
- **Determine "truth."** It surfaces tests that would update belief. It does not certify correctness. A hypothesis with survival_count = 10 is well-attacked, not proven.
- **Replace peer review.** External expert review is a separate process. Falsification Lint is one author's tool for scrutinizing their own claims; it is not a substitute for a collaborator reading the wiki.

---

## §10 — Phase Boundary

**Current scope (v0, this commit).** Design docs + `wiki/hypotheses/` directory scaffold + H01 seed (Ward 1995 dual-cassette feasibility gate). No CI automation, no linter script, no GitHub Actions workflow. Everything here is a *specification* for the infrastructure, plus one worked example.

**Next phase (future).** Implement the regex-level Document Lint rules as a GitHub Actions workflow that runs on PR and posts annotations as PR comments. Build Falsification Lint as a `claude` CLI invocation that reads the committed hypothesis file + the wiki pages it cross-references + this design doc, and emits/updates the Falsification Card. Neither blocks merge. Both are advisory.

**Phase boundary discipline.** The specification has to be clear enough that implementation is a translation job, not a re-design. This page plus `hypotheses/README.md` plus `hypotheses/H01-ward-dual-cassette.md` together should be a complete spec. If implementation later reveals gaps, update this page and commit — git preserves the design history.

---

## §11 — Open Questions

1. **Where does Falsification Lint UX live?** *Answer:* the `wiki/hypotheses/` directory *is* the artifact. Invocation is a `claude` agent call reading the hypothesis file + context. No new UI surface. The rendered Falsification Card can be appended to the hypothesis file or kept as a side-car; either works.

2. **Pre-commit hashing — needed, or is git SHA sufficient?** *Answer:* git SHA of the hypothesis file's first commit + commit-message discipline is sufficient for markdown-backed hypotheses. A separate hash layer would be redundant. Noted explicitly in §6.

3. **Calibration: single-researcher vs. team?** *Answer:* n=1 for now (Brian only). Calibration curve is still useful but noisy — few data points, wide CIs. The direction of systematic bias becomes visible quickly; the magnitude is less reliable. Team-scale calibration waits on team-scale activity; it's a Phase 2+ feature. Document this limitation in the rendered curve.

4. **Claude-semantic rules vs. regex rules — token-cost ceiling for v0?** *Open.* Regex rules are free; semantic rules cost per PR / per sweep. A reasonable v0 budget: 100–500 input tokens and 50–200 output tokens per semantic rule, per document, per sweep pass. At current Open Enzyme sweep volume (a few sweeps per day), this is ~$0.05–0.50/day. Acceptable. If it becomes a cost bottleneck, sampling (run semantic rules only on changed files, or only on promoted hypotheses) is the first knob.

5. **Integration with existing infrastructure.** *Partially resolved.* `chembl-cross-check.md` is an existing user-invoked quarterly linter for one dimension (rodent-IC50 cross-check). Sweep-prompt Pass 1 does some lint-like work during propagation (enforces cross-refs, updates CP labels). Document Lint formalizes and extends these patterns without replacing them.

6. **Who is Falsification Lint *for* in the current regime?** *Answer:* Brian. When Brian commits to a hypothesis — when money, time, or collaborator attention is about to be spent — Falsification Lint is the scrutinize-yourself tool. If three PhD collaborators join, the calibration-curve question (§11.3) reopens; for now the answer is "single-researcher instrument."

7. **Interaction between the two linters.** Document Lint catches formatting / provenance / coverage at the document level. Falsification Lint catches assumption / killshot / threshold at the hypothesis level. In practice, the hypothesis file itself is a document and will also be run through Document Lint: the YAML frontmatter, the cross-refs, the evidence tags in assumption justifications. The linters cascade cleanly — Document Lint first (cheap, always), Falsification Lint second (expensive, on demand).

8. **Retraction log visibility.** Should retractions be visible on the main hypothesis page or moved to a separate `retractions/` directory? *Tentative answer:* in-line in the hypothesis file. The retraction is *part of the epistemic history of the claim* and belongs where the claim lives. A separate directory would hide it; visibility is the point.

---

*Design emerged from Brian's ChatGPT-generated brief (`falsification-lint-brief.md`, personal download 2026-04-24) + Claude refinement conversation 2026-04-24, preserved in git history.*
