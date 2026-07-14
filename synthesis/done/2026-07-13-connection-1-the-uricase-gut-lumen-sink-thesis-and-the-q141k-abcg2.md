---
type: connection
sweep_date: 2026-07-13
sweep_sha: fae0e36
section_index: 1
global_index: 1
pass3_verdict: Confirmed, prioritize
overlap_tag: NOVEL
---

# The uricase gut-lumen-sink thesis and the Q141K ABCG2 rescue mechanism are now linked through a common, testable substrate-supply chokepoint.

1. **The uricase gut-lumen-sink thesis and the Q141K ABCG2 rescue mechanism are now linked through a common, testable substrate-supply chokepoint.** *Supported.* `[CHAIN-DEPTH: 3+]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `gut-lumen-sink.md`, `abcg2-modulators.md`, `gout-pathophysiology.md`, `comp-044-gut-lumen-uricase-physiologic-regime-computational.md`, `validation-experiments.md`, `hypotheses/H08-gut-lumen-sink-platform-thesis.md`
   - *Page-pair linkage:* Weakly-connected pair. `gut-lumen-sink.md` and `abcg2-modulators.md` cite each other at a high level, but the explicit synthesis that the gut-lumen-sink mechanism is gated on ABCG2 *substrate supply*, that Q141K is the single largest common genetic vulnerability for both the transporter and the sink, and that the two threads now share a common wet-lab gate (§1.14 in validation-experiments.md) is named nowhere.
   - *Why It Matters:* The platform's core therapeutic claim (gut-lumen uricase → clinically-meaningful SUA reduction) is only true if sufficient urate reaches the lumen. The Q141K variant reduces ABCG2 trafficking and surface expression. The two mechanisms are not independent — they share a common, testable bottleneck (substrate supply to the sink). This synthesis reframes what had been two parallel research threads into a single, load-bearing platform question: does the engineered strain's uricase output exceed the Q141K-limited ABCG2 flux, or is the transporter the rate-limiter? The wet-lab gate (§1.14) now tests both the butyrate rescue of Q141K and the lactoferrin rescue of TNFα-suppressed ABCG2 in the same Caco-2 transwell experiment. This is the first multi-level chain that directly informs whether the gut-lumen-sink thesis survives in the dominant male/Q141K gout population.
   - *Suggested Action:* Run the §1.14 Caco-2 experiment with the Q141K-transfected line as a parallel arm (already scoped in the current protocol). The result directly gates whether the platform's primary demographic benefits from the gut-lumen-sink mechanism or requires an ABCG2-rescue adjunct layer. If the transporter is rate-limiting, the Q141K-specific rescue stack (butyrate + pharmacological chaperone) becomes load-bearing for the endgame strain. Pass 3 reviewer will annotate with critique.

> **Pass 3 review — Confirmed, prioritize.** `[OVERLAP: NOVEL]` The synthesis that the gut-lumen-sink thesis and Q141K ABCG2 rescue share a common substrate-supply chokepoint is genuinely new to the corpus. The claim that `gut-lumen-sink.md` and `abcg2-modulators.md` "cite each other at a high level" but the explicit "substrate-supply is the shared bottleneck" synthesis is named nowhere is accurate: `gut-lumen-sink.md` discusses ABCG2 as the urate efflux transporter and `abcg2-modulators.md` discusses Q141K trafficking rescue, but neither page names the other as a load-bearing dependency. The §1.14 wet-lab gate (DHT + TNFα additive ABCG2 suppression + butyrate/lactoferrin rescue + Q141K arm) does appear in the `validation-experiments.md` dashboard table, confirming the shared experimental gate exists. The reframing of two parallel threads into a single "does uricase output exceed Q141K-limited ABCG2 flux?" question is the kind of compositional synthesis the daemon is designed to surface. This should route to `gut-lumen-sink.md` and `abcg2-modulators.md` as an explicit cross-page linkage.

---

## ✓ Actioned 2026-07-14

Made the shared substrate-supply chokepoint an explicit cross-page linkage. Added a synthesis subsection to both canonical pages:

- `wiki/gut-lumen-sink.md` — new §"The substrate-supply chokepoint — the sink and the Q141K rescue axis are one question" (under The Concentration Sink Mechanism, after the Sink Principle). Names the sink's substrate supply = ABCG2 output; Q141K throttles the pump that fuels the sink; the two theses share one bottleneck; the platform question collapses to "does uricase output exceed Q141K-limited ABCG2 flux?"; shared §1.14 gate with the Q141K arm.
- `wiki/abcg2-modulators.md` — new §"The substrate-supply chokepoint — the sink and the Q141K rescue are one question" (after the Q141K rescue / pharmacological-chaperone block). Mirror framing, cross-linked to gut-lumen-sink.md.

**Hedging applied (deliberate, per walk):** rescue layer written as *proposed, not established* on both pages — butyrate's direct Q141K rescue flagged untested (Basseville 2012 = chaperones, not butyrate), chaperone candidates flagged hypothesis-stage. **comp-032 was NOT cited as empirical support** in the new text, anticipating its GREEN→hypothesis-generation downgrade later in this same walk (comp-review Item, conclusion-at-risk tier).

Verified the §1.14 Q141K parallel arm is scoped in `validation-experiments.md` (dashboard row + the "Butyrate dose-response arm — direct Q141K attribution test (corrected 2026-07-13)" block, which already hedges butyrate). No change needed there — the existing correction matches the framing used here.

No follow-ups queued. Evidence tag: Mechanistic Extrapolation over established In Vitro ABCG2 biology.
