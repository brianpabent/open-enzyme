# Open Enzyme

**Use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.**

Open Enzyme is an open-source Phase 0 research project. It maps gout across urate physiology, crystal formation, innate immunity, inflammatory amplification, resolution, delivery, and translation; turns promising weaknesses into falsifiable intervention tracks; and runs the cheapest experiments that can kill or redirect them.

Koji is one track. It will be valuable if it works. If it does not, the project will document why, preserve what the result teaches about gout, and move to a better exploit. No chassis, strain, payload, or production model is the project.

Start with:

- [Mission and operating principles](wiki/etc/open-enzyme-vision.md)
- [Research dashboard](index.md)
- [Adversarial method and track threat models](wiki/cross-validation.md)
- [Gout exploit map](wiki/nlrp3-exploit-map.md)
- [Validation experiments](wiki/validation-experiments.md)
- [Active synthesis queue](synthesis/queue/)

For the engineered-koji work specifically, use the [koji track](wiki/koji-track.md), [engineering protocol](wiki/engineered-koji-protocol.md), and [current threat model](wiki/cross-validation.md#koji-track-threat-model).

## Research model

Each active track states:

1. the gout weakness;
2. the exploit hypothesis;
3. the proposed engineering;
4. evidence by level;
5. assumptions and safety constraints;
6. the cheapest discriminating experiment;
7. pass, revise, and kill criteria;
8. what remains true if the track fails.

The reusable form is [track-template.md](wiki/etc/track-template.md).

## Evidence standard

Claims distinguish clinical trials, animal models, in-vitro evidence, computational results, and mechanistic extrapolation. Load-bearing numbers are verified against primary sources before commit. Computational experiments use hash-bound pre-run and post-run review gates plus an independent push review before their claims can propagate or enter synthesis.

This repository is research-stage and does not provide medical advice.

## Knowledge workflow

- Every push publishes the current site.
- Relevant research pushes receive bounded cross-page propagation.
- Changed computational experiments are independently reviewed before derived claims propagate.
- Full-corpus synthesis runs only by explicit request. It reads the complete current corpus twice, searches every domain pair, reopens raw sources and exact computational outputs, and independently reviews candidates.
- The live tree stores current scientific state and active actions. Git is the revision history.

See [AGENTS.md](AGENTS.md) for the complete authoring and review rules.

## Contributing

The research library is the codebase. Before opening an issue or pull request:

- check the [dashboard](index.md) and relevant concept page;
- source the real project claim before challenging it;
- add evidence levels and primary provenance;
- keep detailed evidence in one home and link from related pages;
- define how the new information changes a track or decision.

## Team and license

Open Enzyme is led by Brian Abent and is recruiting collaborators in microbiome/in-vivo validation, pharma translation/regulatory strategy, and innate-immune safety. See [team.md](wiki/etc/team.md).

The repository is released under the [MIT License](LICENSE).
