---
type: most-curious-thread
sweep_date: 2026-05-16
sweep_sha: 3c1ca4b
section_index: 1
global_index: 15
pass3_verdict: Confirmed, prioritize
overlap_tag: EXTENSION
---

# Of everything in this corpus, the single thread I'd spend the next experiment slot on is the C1-INH (SERPING1) protease-stability + glycosylation feasibility analysis in EcN-luminal-secreted format — a $0, ~1-week computational prior that gates whether the two-chassis two-node CP0 coverage architecture (C1-INH LBP-luminal + DAF SCR1-4 koji-secreted) is mechanically viable.

Of everything in this corpus, the single thread I'd spend the next experiment slot on is **the C1-INH (SERPING1) protease-stability + glycosylation feasibility analysis in EcN-luminal-secreted format** — a $0, ~1-week computational prior that gates whether the two-chassis two-node CP0 coverage architecture (C1-INH LBP-luminal + DAF SCR1-4 koji-secreted) is mechanically viable.

**Corpus evidence supporting the hunch:** comp-024 scored C1-INH as GREEN-provisional 0.774 on EcN, specifically because C1-INH's dominant feasibility question (luminal-protease stability + glycosylation) is a *single-axis* problem testable with the comp-006/comp-012 pipeline. The comp-006/comp-012 pipeline has already been validated three times (uricase LOW, full DAF/CD55 HIGH stalk-driven, DAF SCR1-4 LOW after truncation) — it works. C1-INH (UniProt P05155) is a ~500-aa serpin with a single reactive-center loop and ~6 N-glycosylation sites — a different fold architecture than DAF's CCP/SCR β-sandwich, which makes it a genuinely independent test of the pipeline's applicability to a new fold class. DAF SCR1-4 (H05) is already in the koji pipeline as a single-cassette wet-lab candidate (§1.25). C1-INH would be the LBP pipeline's sister CP0 candidate, hitting a different node (classical/lectin pathway entry vs MSU-surface convertase decay) on a different chassis. The two complement each other cleanly — no mechanism overlap, no chassis overlap.

**Evidence that would refute it:** If the comp-006-style analysis returns HIGH protease risk for mature SERPING1 in EcN-secreted luminal conditions (max risk > 0.3, driven by exposed cleavage sites in the reactive-center loop or the serpin fold's metastable conformation), the single-axis problem becomes a multi-axis problem and C1-INH drops from the LBP CP0 candidate list. Alternatively, if the analysis returns LOW but the N-glycosylation profile of EcN-produced C1-INH is incompatible with complement-regulatory activity (EcN glycosylates differently than human hepatocytes), the functional question gates the engineering decision regardless of protease stability.

**Cheapest discriminating experiment:** A comp-006-style computational analysis — fetch SERPING1 from UniProt, run AlphaFold pLDDT-based cleavage-site prediction against the canonical gut-luminal protease panel (trypsin, chymotrypsin, elastase, plus EcN-native proteases where characterized), score the reactive-center loop's solvent exposure (the serpin fold's metastable conformational switch makes this the load-bearing vulnerability), and assess N-glycosylation site occupancy and complexity in an *E. coli* expression context. Cost: $0. Time: ~1 week. Output: a LOW/MODERATE/HIGH verdict with explicit caveats on glycosylation-dependent activity. If LOW → C1-INH becomes the next LBP-chassis computational gate; if HIGH → drops from the candidate list with clear documentation of why.

**Multi-vendor signal:** I suspect this is convergent across sweep models — the pattern (computational protease-stability pipeline applied to a new complement-regulator candidate in the LBP chassis) is a direct extension of already-validated methodology, and the strategic framing (two-chassis two-node CP0 architecture) is a natural composition of two active peer tracks. Gemini 2.5 Pro's comp-024 output already pointed at C1-INH; Claude and GPT would likely converge on the same thread if asked to rank CP0 exploration vectors by leverage-per-dollar. But the specific recommendation — run the comp-006-style analysis as the immediate next move — may be idiosyncratic to my read of the corpus's emphasis on cheap computational priors before wet-lab spend. If other models would recommend jumping directly to a wet-lab C1-INH expression test (skipping the computational prior), that divergence would itself be informative about how different models weight computational vs wet-lab risk in early-stage platform decisions.



---

Sources cited:
- wiki/complestatin-bgc-lbp-feasibility-computational.md
- wiki/engineered-lbp-chassis.md
- wiki/daf-cd55-scr14-truncated-computational.md
- wiki/chaperone-orthogonal-stacking.md
- wiki/complement-c5a-gout.md
- wiki/hypotheses/H05-daf-scr14-cp0-thesis.md
- wiki/chassis-pending-interventions.md
- wiki/purine-degrading-bacteria.md
- wiki/abcg2-modulators.md
- wiki/validation-experiments.md
- wiki/intra-articular-uricase-h2o2-reaction-diffusion-computational.md
- wiki/gout-kill-chain-delivery-routes.md
- wiki/delivery-route-matrix.md
- wiki/engineered-koji-protocol.md
- wiki/koji-endgame-strain.md
- wiki/cordycepin-cassette-burden-computational.md
- wiki/carnosine.md
- wiki/androgen-urate-axis.md
- wiki/repeat-dose-inhaled-mrna-il1ra-pkpd-computational.md
- wiki/inhaled-mrna-il1ra-pulse-computational.md
- wiki/gout-action-guide.md
- wiki/nlrp3-inflammasome.md
- wiki/lactoferrin-linker-redesign-computational.md
- wiki/lactoferrin-protease-stability-computational.md
- wiki/lactoferrin.md
- wiki/etc/bio-ai-tools.md
- wiki/f-prausnitzii-heterologous-expression-computational.md
- wiki/uricase.md
- wiki/hypotheses/H02-engineered-lbp-thesis.md

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: EXTENSION]` The C1-INH curious-thread choice is well supported by the corpus. comp-024 explicitly demotes complestatin for LBP, promotes C1-INH-on-EcN as GREEN-provisional 0.774, and identifies protease stability plus glycosylation as the dominant unresolved axis; `complement-c5a-gout.md` also lists C1-INH as a protective fluid-phase complement regulator at the relevant upstream node. This is exactly the kind of chokepoint-first, chassis-pending intervention that should survive review: CP0 fit is strong, chassis remains open, and the next gate is a cheap computational falsification step before wet-lab spend.

---

**WALKED 2026-05-19 — Closed (already actioned — comp-037 ran 2026-05-17 → MODERATE verdict).**

The daemon's "next experiment slot" pick was already executed between this curious-thread (2026-05-16) and the 2026-05-19 walkthrough. **comp-037 ran 2026-05-17** and returned **MODERATE (kinetic-competition gated)**:
- Strictly-degradative serpin-body protease risk: **LOW (0.1)** after mucin truncation (aa 123-500 construct)
- Reactive-center loop (RCL R466-T467): **RED (0.8)** — reflects inhibitor mechanism (suicide-substrate), not body degradation
- Glycosylation feasibility: **GREEN** for luminal topology

The two-chassis CP0 architecture (C1-INH on EcN-LBP + DAF SCR1-4 on koji) is now substantiated at the computational-gate level. Remaining wet-lab gate: RCL kinetic-competition assay (does C1s/C1r/MASP-2 productively engage RCL before DegP/elastase cleaves it unproductively?).

Already in the wiki via:
- [`chassis-pending-interventions.md` §6.5 / §9.8](../../wiki/chassis-pending-interventions.md) — two-chassis architecture documentation
- [`c1-inh-protease-stability-ecn-computational.md`](../../wiki/c1-inh-protease-stability-ecn-computational.md) — comp-037 page
- [`complement-c5a-gout.md` §9.8](../../wiki/complement-c5a-gout.md) — two-chassis two-node CP0 coverage architecture
- Cluster C-serpin walkthrough (2026-05-19) — added provisional serpin α coefficient (0.5–1.5) to `chaperone-orthogonal-stacking.md` §3.5.2 + §3.5.3

This is a clean instance of the daemon's "most-curious-thread" actually being the next-step recommendation that the platform executed on schedule.
