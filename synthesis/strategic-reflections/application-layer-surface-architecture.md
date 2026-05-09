---
title: "Application-layer surface architecture"
status: open
created: 2026-05-08
class: strategic-reflection
related:
  - ../../wiki/gout-action-guide.md
  - ../../wiki/supplements-stack.md
  - ../../wiki/medicinal-mushroom-complement-track.md
  - ../../wiki/upstream-complement-modulator-sweep-computational.md
---

# Application-layer surface architecture

**Sub-question:** does the sweep daemon need a propagation pass into the patient/practitioner-facing surfaces?

## Reflection

The wiki has a **research-facing layer** (`wiki/*.md`) that the sweep daemon propagates findings between. As of 2026-05-08 it also has a **patient/practitioner-facing layer**:

- [`gout-action-guide.md`](../../wiki/gout-action-guide.md) — situation-first decision tree
- [`supplements-stack.md`](../../wiki/supplements-stack.md) — compound-first catalog

The sweep daemon does **not** currently propagate findings into these surfaces — promotion is manual.

The 2026-05-08 walkthrough (Item 1, cordycepin × pentostatin × GLPP synergy) was the canonical case: the synergy lived in `medicinal-mushroom-complement-track.md` for 2 days before being promoted to the action guide, and Cordyceps/GLPP/ergothioneine still aren't in the supplements catalog despite the medicinal-mushroom-complement track being live.

Brian's framing: **build the manual version first.** A `fresh-stack.py` script (sibling to `fresh-synthesis.py`) that scans the research wiki for findings that should be reflected in the action guide / catalog but aren't, surfaces them as a promotion-candidate report, and lets a human review and accept the propagation. Run it manually for a while; if the workflow proves stable, automate as a Pass 4 / Pass 5 in the daemon.

### Known caveat-with-the-compound entries (added 2026-05-08, Item 6)

When **reishi / GLPP** enters the application surface, the structure-dependent β-glucan NLRP3 directionality warning ([medicinal-mushroom-complement-track.md §"Consumer-product caveat"](../../wiki/medicinal-mushroom-complement-track.md)) must travel with it — *G. lucidum* EPS activate NLRP3 (wrong direction), spore-powder/GLP fractions inhibit (right direction).

When **rosmarinic acid** (per [comp-018](../../wiki/upstream-complement-modulator-sweep-computational.md)) enters the application surface, the dose-grounding caveat (typical culinary rosemary delivers sub-therapeutic RMA; a standardized extract or dose-aware preparation is needed) travels with it.

## Trigger

When the manual `fresh-stack.py` script has been run enough times (≥3?) to have a clear pattern of what kinds of findings need promotion, AND the promotion-candidate reports are converging (most candidates are already reflected, low-noise output) — that's the signal that the manual discipline is stable enough to automate.

Conversely, if the manual reports keep surfacing the same kind of finding (e.g., "this new compound entry needs a catalog row"), that's evidence for codifying a propagation rule rather than reviewing each one manually.

## Outcome

Decide whether to:

a. Keep the propagation manual indefinitely (low-friction, human-in-the-loop)
b. Add a Pass 4 (propagate-to-application) to the sweep daemon with the same multi-vendor cross-check discipline
c. Build a separate scheduled job (weekly?) that runs `fresh-stack.py` and emails Brian a promotion-candidate report

The decision depends on how the manual workflow goes. Brian's preference 2026-05-08: "manual first, automate only when we have evidence the workflow is stable."
