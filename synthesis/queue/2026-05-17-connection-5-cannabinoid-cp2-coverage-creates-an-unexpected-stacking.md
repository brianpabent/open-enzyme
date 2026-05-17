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
