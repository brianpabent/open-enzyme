---
type: connection
sweep_date: 2026-05-17
sweep_sha: 768d99c
section_index: 5
global_index: 5
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Cannabinoid CP2 coverage creates an unexpected stacking completeness check — the platform now has at least one intervention at every NLRP3 chokepoint from CP0 through CP6b, but CP0 and CP5a remain pharma-only.

5. **Cannabinoid CP2 coverage creates an unexpected stacking completeness check — the platform now has at least one intervention at every NLRP3 chokepoint from CP0 through CP6b, but CP0 and CP5a remain pharma-only.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`

   - *Documents Connected:* `cannabinoids-terpenes.md`, `nlrp3-exploit-map.md`, `colchicine.md`, `supplements-stack.md`, `gout-action-guide.md`, `chassis-pending-interventions.md`, `complement-c5a-gout.md`
   - *Page-pair linkage:* `cannabinoids-terpenes.md` and `colchicine.md` are **not cross-referenced** (the Connection #2 finding above is the first time they've been connected). `cannabinoids-terpenes.md` and `nlrp3-exploit-map.md` are linked (cannabinoids are in the exploit map). The others are well-linked across the CP0-CP6b framework.
   - *Why It Matters:* A full-chokepoint audit across the current corpus reveals an emergent completeness pattern that no single page captures: **Every NLRP3 chokepoint from CP0 through CP6b now has at least one named intervention in the platform corpus.** The coverage isn't uniformly fermentable — CP0 (avacopan, pharma-only) and CP5a (anakinra/canakinumab, pharma-only) remain gaps on the fermentable side — but the *named-intervention coverage* is complete. The cannabinoid page's §4a protocol (CBD:THC topical for acute flare, hitting CP2 via CB2) fills what was previously a gap at the acute-CP2 intersection — colchicine covers CP2 systemically, but the topical route provides local CP2 coverage without the colchicine drug-interaction surface. The anakinra SC protocol in `gout-action-guide.md` (100 mg/day × 3 days, off-label for acute flare) fills what was previously a gap at the acute-CP5a intersection below the canakinumab cost barrier. The result is a chokepoint-completeness landscape that is more mature than the wiki's own framing suggests.
   - *Suggested Action:* Add a "Chokepoint coverage completeness audit" subsection to `nlrp3-exploit-map.md` (or as a standalone one-table section in `index.md`) that maps every chokepoint × intervention pair, with fermentable vs. pharma-only status explicitly tagged. This converts what is currently implicit (and only visible to a reader who has read all seven pages) into an explicit platform-architecture statement.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The chokepoint-completeness audit is useful, but the "CP0 and CP5a remain pharma-only" wording is too coarse for the current corpus. CP0 is no longer only avacopan: `nlrp3-exploit-map.md` and `complement-c5a-gout.md` now track DAF/CD55 SCR1-4 as an active engineering candidate with wet-lab unknowns, while CP5a has anakinra/canakinumab clinically and inhaled mRNA-IL-1RA as chassis-pending in `chassis-pending-interventions.md`; the better table should distinguish "clinically available today," "pharma-only today," and "engineering/chassis-pending candidate," not collapse those categories.

---

**WALKED 2026-05-19 — Closed (Chokepoint Coverage Completeness Audit added to nlrp3-exploit-map.md with Pass 3's three-tier status categorization).**

Actioned:
- ✓ Added new "## Chokepoint Coverage Completeness Audit (added 2026-05-19)" section to `nlrp3-exploit-map.md` (between the chokepoint walk and the AI Analysis Updates section). Maps every chokepoint × intervention pair across CP0 through CP6b — ~30 rows.
- ✓ Pass 3's three-tier status categorization explicitly encoded (corrects the original "pharma-only" coarse framing):
  - **Clinical (today)** — FDA-approved in standard or off-label use
  - **Pharma-only (no gout indication)** — pharma exists for other indications
  - **OE engineering-pending** — in OE development pipeline
  - **OE fermentable (today)** — accessible via cultivation / fermentation / dietary intake
- ✓ Per Brian's 2026-05-19 walkthrough direction, audit added to `nlrp3-exploit-map.md` only, NOT to `index.md`.
- ✓ Two actual coverage gaps surfaced by the audit:
  - **CP4 (caspase-1)** — no OE-fermentable today; only VX-765 pharma-only + Berkeleyamides OE engineering-pending (J1 walkthrough — Talaromyces-corrected, see also `medicinal-mushroom-complement-track.md` §"Ascomycete secondary metabolites").
  - **CP5a (IL-1β receptor)** — clinical-pharma coverage robust (anakinra/canakinumab/rilonacept) but no OE-fermentable possible architecturally; IL-1β receptor blockade requires protein antagonist or high-affinity antibody, neither plausible at consumer-scale fermentation without engineered-LBP delivery (which is the inhaled-mRNA-IL-1RA path).
- The audit is the same architectural-surfacing pattern as B3 (closed-loop pharmacogenomics pipeline naming) and J3.3 (substrate engineering elevation to Platform Principle 9) — making visible what the platform already operates but hasn't named.
