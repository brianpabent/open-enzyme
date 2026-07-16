---
id: H09
title: Community fermentation can be a reproducible production option for an engineered-koji configuration
status: active-stub
tags: [hypothesis, koji-track, community-fermentation, production-reliability, strain-stability, contamination]
related:
  - ../koji-track.md
  - ../cross-validation.md
  - ../engineered-koji-protocol.md
  - ../validation-experiments.md
  - ../etc/open-source-platform.md
---

# H09 — Community Fermentation Reliability

## Scope

H09 tests one possible production and distribution model within the [engineered-koji track](../koji-track.md). It is not a project claim and is not required for other gout tracks. The project has not made a sourdough-equivalence claim about therapeutic production.

If H09 fails, the koji track may use centralized manufacture, licensed community facilities, a non-viable preparation, or another chassis. The red-team mission and unrelated interventions remain intact.

## Provisional hypothesis

**Mechanistic and operational extrapolation:** a defined engineered *A. oryzae* configuration may be produced across more than one operator or facility with reproducible identity and activity if the process includes controlled starter stock, bounded propagation, contamination controls, and release testing.

The acceptable variation, construct-retention, contamination, activity-retention, and assay-performance thresholds must be justified by the intended product and measurement system before a pilot is run. Earlier unsourced numerical thresholds are not retained as evidence.

## Current evidence boundary

- Industrial koji production shows that controlled *A. oryzae* fermentation can be standardized, but it does not establish distributed production of an engineered therapeutic configuration.
- Chromosomal integration and master-stock discipline are plausible stability controls; the actual construct and process require direct testing.
- Community laboratories may provide environmental control and analytical release testing that home settings cannot.
- No current result establishes cross-operator reproducibility, therapeutic dose consistency, or a regulatory path for distributed engineered starter cultures.

## Assumptions under attack

1. The current construct remains genetically and phenotypically stable across the allowed propagation window.
2. Operator, substrate, temperature, humidity, and process variation do not push activity outside the release specification.
3. Contamination and strain-identity failures are detected before use.
4. Drying, storage, and final preparation preserve the payloads required by the selected configuration.
5. The release assay measures the load-bearing activity with sufficient accuracy and is practical at the chosen production site.
6. The legal and regulatory model matches the actual organism state, claims, and distribution path.

## Cheapest discriminating sequence

Do not test community production before a viable single-site configuration exists.

1. Establish construct identity, activity, and stability in controlled production.
2. Pre-register product-specific release criteria and assay performance.
3. Run controlled process-variation and serial-propagation studies.
4. Compare a small number of trained operators or sites using blinded central release testing.
5. Expand only if the observed failure modes are measurable and correctable.

Current protocol candidates belong in [validation-experiments.md](../validation-experiments.md); detailed production design belongs in [engineered-koji-protocol.md](../engineered-koji-protocol.md).

## Decision criteria

- **Pass:** multiple sites meet a justified release specification with detectable, correctable deviations.
- **Revise:** the biological configuration works, but production must move to a community laboratory, centralized facility, shorter propagation window, different preservation method, or stronger release assay.
- **Kill this production option:** reproducibility or safety failures remain frequent, silent, or economically unmeasurable under the intended operating model.

## What remains true if H09 fails

Results still inform strain stability, assay design, preservation, contamination control, and manufacturing requirements. They do not invalidate the payload, the koji chassis under centralized manufacture, the gut-lumen mechanism, or any non-koji track.
