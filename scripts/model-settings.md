# Model and role settings

[`model-settings.json`](model-settings.json) is the versioned registry for active automation and manual CLI model settings. [`model_settings.py`](model_settings.py) validates it offline and supplies model choices, budgets, output limits, capability checks and cost calculations. Changing a role's model selects that model's verified entry; it cannot retain another model's prices.

| Role | Selected model(s) | Existing budget |
|---|---|---|
| Evidence-radar review | GPT-5.5 | $0.75 per feed |
| Bounded propagation | DeepSeek V4 Pro | $5 per run |
| Distributed synthesis | Gemini 2.5 Flash extraction A; DeepSeek V4 Pro extraction B and bridge; GPT-5.5 review | $5 per run |
| COMP review | GPT-5.5 | $2.50 per COMP; $5 aggregate |
| Quarterly ChEMBL refresh | Native Claude Sonnet 4.6 CLI | No configured monetary cap |
| Manual fresh synthesis | DeepSeek V4 Pro | No configured monetary cap |
| Manual propagation evaluation | Explicit `--model` required | No configured monetary cap |
| Synthesis emission | Attribution labels only | No model request |

Output and iteration allowances are preserved in the role entries, including radar's candidate-count allowance and the different CLI/workflow propagation iteration limits. Sonnet 5.5 is a verified override, not a production default. A model being listed does not authorize running it or increasing a budget.

## Verification and routing

The registry records verification dates, primary URLs and SHA-256 fingerprints of the OpenRouter endpoint responses used to verify prices, context/input/output bounds and supported parameters. Rates are USD per million tokens. Endpoint metadata is available through the public [model catalog](https://openrouter.ai/api/v1/models) and each entry's `/endpoints` URL. Native Claude CLI settings use [Anthropic's model overview](https://platform.claude.com/docs/en/models/overview) and [pricing](https://platform.claude.com/docs/en/about-claude/pricing). Refresh metadata deliberately before adding or changing a model; runtime does not discover models or guess prices.

Chat requests retain the exact selected model ID, permit only recorded provider endpoint tags, require parameter support, disable provider fallbacks and enforce the selected model's unit-price ceiling. Long-context tiers use the same rates for planning and routing. The [OpenRouter routing contract](https://openrouter.ai/docs/guides/routing/provider-selection) defines these filters. Required tools, reasoning and response formats fail closed when unsupported. Unsupported sampling defaults are omitted; strict radar JSON schema and existing review/hash gates remain required. Provider drift or endpoint unavailability can cause a request to fail; no alternative model is substituted.

Provider-reported usage cost takes precedence when supplied. Missing cost uses the selected model's registered rates and applicable long-context tier. Cache savings are not assumed; propagation's cache-enabled fallback accounts conservatively for cache-write rates. Receipts record the registry hash where the consumer produces review or coverage metadata.

Budget checks remain planning/runaway guards. Character/4 input estimates are not native token counts, and unit-price filters are not prepaid total-spend limits. Existing retry behavior and failed-attempt accounting are unchanged. The previously uncapped manual/CLI roles remain uncapped; this change does not add an authorization to spend.

## Overrides and compatibility

- Existing `--model` overrides remain available for verified chat IDs and their required capabilities. Unknown IDs, retired models and native CLI IDs sent to chat transport fail before a request. In particular, OpenRouter's `anthropic/claude-sonnet-4.6` and native CLI's `claude-sonnet-4-6` are distinct IDs; old hyphenated OpenRouter spellings are not silently aliased.
- GitHub workflow budget inputs remain explicit overrides. Blank inputs use the role registry rather than duplicated workflow literals. Overrides must be finite and positive; a per-COMP cap cannot exceed the aggregate cap.
- COMP's old independent price flags are retained as consistency checks. They must match the selected model's base rates. Legacy radar review configs may specify matching rates; selecting a different model derives its own rates. New radar configs reference the role directly.
- `fresh-synthesis.py --prepare-only` validates the full request and prints its estimate without reading credentials or calling a model.
- Synthesis-emission defaults are attribution labels, not request IDs. The full-synthesis workflow derives its reviewer attribution from the run's coverage receipt.
- The literature client [`agentic_lit_synthesis.py`](../wiki/etc/experiments/lib/agentic_lit_synthesis.py) and historical caller-owned research configurations remain frozen. That library is bound into COMP038's authoring manifests. Migrating it requires the separate [COMP lifecycle gates](../AGENTS.md); editing it here would invalidate the existing scientific artifact. The registry identifies its exact hash and manifest, and an offline regression checks it remains unchanged.
- Only the existing OpenRouter chat and native Anthropic CLI transports are supported. A new transport or unverified model requires a separately verified registry entry and caller support; no provider-specific migration is implied.

## Offline checks

```sh
python3 scripts/model_settings.py check
python3 scripts/model_settings.py role evidence_radar_review
python3 scripts/model_settings.py env comp_review --override PER_COMP_CAP=2.5
python3 -m unittest tests.test_model_settings tests.test_model_consumers tests.test_evidence_radar
```

Corpus-integrity CI runs the registry and consumer regressions without credentials, network calls or paid model evaluation.
