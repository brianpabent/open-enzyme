---
type: connection
sweep_date: 2026-05-16
sweep_sha: 91acf49
section_index: 4
global_index: 4
pass3_verdict: Push back
overlap_tag: EXTENSION
---

# The lactoferrin inter-lobe linker redesign (comp-034) and the DAF SCR1-4 CCP/SCR fold share a structural vulnerability pattern — exposed inter-domain linkers are the dominant protease-liability feature for both proteins in shio-koji, and the same proline-substitution design logic applies to both.

4. **The lactoferrin inter-lobe linker redesign (comp-034) and the DAF SCR1-4 CCP/SCR fold share a structural vulnerability pattern — exposed inter-domain linkers are the dominant protease-liability feature for both proteins in shio-koji, and the same proline-substitution design logic applies to both.** *Speculative.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `lactoferrin-linker-redesign-computational.md`, `daf-cd55-scr14-truncated-computational.md`, `lactoferrin-protease-stability-computational.md`, `daf-cd55-protease-stability-computational.md`, `validation-experiments.md`
   - *Page-pair linkage:* `lactoferrin-linker-redesign-computational.md` (comp-034) and `daf-cd55-scr14-truncated-computational.md` (comp-012) are not cross-referenced to each other. Both are computational analyses of shio-koji protease stability for secreted OE payloads. Both identify inter-domain linker regions as the dominant vulnerability: comp-005 flagged the lactoferrin inter-lobe linker (aa 353–363) as the most plausible secondary vulnerability; comp-006 identified the DAF Ser/Thr-rich stalk (aa 286–353) as the driver of the HIGH verdict, and comp-012 confirmed that stalk truncation eliminated all exposed sites. The structural pattern is identical: **well-folded domains connected by protease-accessible linkers.** The design logic is transferable: comp-034's proline-substitution strategy for the Lf linker could, in principle, be applied to any inter-domain linker in any secreted OE payload.
   - *Why It Matters:* This is a platform-level design pattern, not a single-protein finding. The shio-koji format is the platform's preferred delivery vehicle, and protease stability of secreted payloads is the gating constraint. If the "rigidify inter-domain linkers with proline substitutions" strategy generalizes beyond lactoferrin, it becomes a standard design step for any new secreted payload — run a comp-034-style linker scan before committing to gene synthesis. This would be the first generalized design rule to emerge from the comp-NNN computational pipeline, and it would accelerate future payload addition by making the protease-stability question answerable in silico rather than requiring per-protein wet-lab validation.
   - *Suggested Action:* After comp-034's ProteinMPNN rerun (queued as `synthesis/queue/2026-05-16-experiment-2`), if the proline-substitution strategy validates against the WT linker, codify the pattern as a design rule in `chaperone-orthogonal-stacking.md` or a new `payload-design-rules.md` page: "For any secreted payload with inter-domain linkers, run a comp-034-style linker scan before gene synthesis. Proline substitution at ALP-hot positions in the linker is the default first-pass strategy." Track as a platform-level methodology contribution.

> **Pass 3 review — Push back.** `[OVERLAP: EXTENSION]` `[GAP: science-gap]` The platform-level “exposed regions drive protease liability” pattern is valid, but the DAF analogy is biologically overextended: comp-006 identifies the DAF Ser/Thr-rich stalk aa 286–353 as the protease-liability driver, and comp-012 says truncating to SCR1–4 aa 35–285 removes 100% of exposed sites. That is not the same problem as lactoferrin’s inter-lobe linker `SEEEVAARRAR`, and proline-substituting DAF inter-SCR linkers is not supported by the DAF pages; for DAF, the validated design logic is stalk truncation, not linker rigidification.

---

**WALKED 2026-05-19 — Closed (DAF analogy dropped per Pass 3 + Brian's call; generalization question reframed in comp-034 stub; failure-mode pattern documented in bio-ai-tools.md).**

**Brian's 2026-05-19 walkthrough call (Option A):** drop the DAF analogy entirely. Pass 3's correction is correct — DAF SCR1-4's protease-vulnerability question is solved by stalk truncation (comp-012), not by linker rigidification. The DAF analogy was a Pass 2 daemon failure mode: surface-level pattern-matching ("both proteins have exposed protease-accessible regions") generalized without checking whether the structural-functional details support the same intervention strategy.

Actioned:
- ✓ Added new "Open follow-up — does the proline-rigidification strategy generalize?" section to `lactoferrin-linker-redesign-computational.md` (the comp-034 stub). Defines the right candidate class — short structured linker, mandatory connector, protease-vulnerable, koji production format — and explicitly excludes DAF SCR1-4 as the wrong exemplar with a brief explanation of WHY (truncatable spacer, opposite design strategy).
- ✓ Documented the failure-mode pattern in `etc/bio-ai-tools.md` §"Protease-vulnerability-to-redesign workflow" step 2 — names the "structural-mandatory vs structural-removable" classification as a required discipline step that catches this Pass 2 error class. Future redesign work routes through this check.
- ✓ Cross-referenced from `lactoferrin.md` §12 item 13 with explicit "NOT to be confused with the DAF SCR1-4 strategy (which is truncation per comp-012)" framing.

**Cluster E surfaced a broader Pass 2 daemon failure-mode pattern** — the same shape as the CFH allele-frequency catch (gnomAD-actual vs daemon-stated population priors), the Berkeleyamide/Talaromyces taxonomy catch (daemon used 2008 taxonomy without checking reclassification), the cortisol "not documented" circular dismissal (Pass 3 failure mode that Brian overruled), and the MPA-direction-of-effect catch (daemon assumed "food-grade Penicillium = anti-inflammatory" without checking). Five distinct catches in this single walkthrough. **Brian queued a Pass 3 failure-mode retrospective for end-of-walk** — a subagent task to grep `synthesis/done/` across this + prior walkthroughs for closure annotations naming Pass 3 errors, produce a typology of Pass 3 failure modes with frequency counts. The Pass 2 failure modes are caught by Pass 3 + Brian; the Pass 3 failure modes are caught only by Brian — that single-point-of-failure asymmetry is the systemic gap the retrospective will quantify.

Also closes:
- 2026-05-16 open-question-1 (same generalization question framed as open question; Pass 3 also corrected the DAF exemplar in that item).
