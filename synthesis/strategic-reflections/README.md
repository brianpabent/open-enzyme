# Strategic Reflections — content-triggered platform reflections

## What lives here?

Platform-level reframes that fire on **substance maturity**, not on walkthrough cadence. These are decisions about the project's direction (e.g., "should we expand the platform framing from koji-only to multi-track?"; "is the chaperone-orthogonal stacking framework actually predictive or sophisticated retrofit?") that need a critical mass of accumulated work before they can be sensibly answered.

Each file in this directory is one reflection. The file documents:
- **Reflection** — what the question is
- **Trigger** — what conditions need to be met before the reflection fires
- **Outcome** — what decision needs to be made when the reflection fires

## Why separate from `queue/`?

`queue/` holds daemon-emitted unit-of-work items that need walkthrough action. Reflections are different:

- They are **human-curated**, not daemon-emitted. The daemon does NOT write here.
- They are **content-triggered**, not walkthrough-triggered. The walkthrough lists them but does not action them.
- They are **decisions about the project's direction**, not unit-of-work tasks.

Mixing them with the queue would compound the project-management problem the migration is trying to solve.

## Resolution flow

When a reflection's trigger condition fires AND the user-decided outcome is documented, the file moves (via `git mv` to preserve path history) to `_resolved/<original-filename>.md`. The resolved file:

- Adds frontmatter field `resolved_date: YYYY-MM-DD`
- Adds appended section `## Resolution outcome` documenting what was decided
- Preserves the original Trigger / Outcome content above the resolution section

The `_resolved/` directory is created on first resolution; not present today.

Per [spec §5.7](../../operations/specs/2026-05-08-synthesis-filesystem-migration.md).

## Currently-open reflections

- **[Open Enzyme platform-framing reframe](./platform-framing-reframe.md)** — does the broader matrix-tracks portfolio justify expanding the project framing from "engineered enzymes in koji" to "solve gout, every avenue, fully open"?
- **[Chaperone framework predictive-power validation](./chaperone-framework-validation.md)** — is the chaperone-orthogonal stacking framework actually predictive, or sophisticated retrofit?
- **[Application-layer surface architecture](./application-layer-surface-architecture.md)** — does the sweep daemon need a propagation pass into the patient/practitioner-facing surfaces, or stays manual?
