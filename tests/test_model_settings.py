from __future__ import annotations

import copy
import json
import math
import unittest
from pathlib import Path

from scripts import model_settings as settings

ROOT = Path(__file__).resolve().parents[1]


class RegistryTests(unittest.TestCase):
    def test_production_selections_and_budgets_are_preserved(self):
        expected = {
            "evidence_radar_review": ("openai/gpt-5.5", 0.75),
            "bounded_propagation": ("deepseek/deepseek-v4-pro", 5.0),
            "comp_review": ("openai/gpt-5.5", 2.5),
            "quarterly_chembl_refresh": ("claude-sonnet-4-6", None),
            "manual_fresh_synthesis": ("deepseek/deepseek-v4-pro", None),
            "manual_propagation_eval": (None, None),
        }
        for name, (model, cap) in expected.items():
            with self.subTest(role=name):
                self.assertEqual(model, settings.role(name)["model"])
                self.assertEqual(cap, settings.role(name)["max_cost_usd"])
        synthesis = settings.role("distributed_synthesis")
        self.assertEqual({"extractor_a": "google/gemini-2.5-flash", "extractor_b": "deepseek/deepseek-v4-pro", "bridge": "deepseek/deepseek-v4-pro", "reviewer": "openai/gpt-5.5"}, synthesis["models"])
        self.assertEqual(5.0, synthesis["max_cost_usd"])
        self.assertEqual(5.0, settings.role("comp_review")["aggregate_max_cost_usd"])

    def test_unknown_models_and_native_transport_cannot_use_chat_fallback(self):
        for name in ("unknown/cheap", "anthropic/claude-sonnet-4-6", "openai/gpt-6.1-sol", ""):
            with self.subTest(model=name), self.assertRaises(settings.ModelSettingsError):
                settings.estimate_cost(name, 100, 100)
        with self.assertRaises(settings.ModelSettingsError):
            settings.chat_body({"model": "claude-sonnet-4-6", "messages": [{"role": "user", "content": "x"}], "max_tokens": 100})

    def test_gpt_standard_and_long_context_prices_are_bound_to_model(self):
        self.assertAlmostEqual(0.245, settings.estimate_cost("openai/gpt-5.5", 1000, 8000))
        self.assertEqual(30.0, settings.token_rates("openai/gpt-5.5", 272000)["output"])
        self.assertEqual(45.0, settings.token_rates("openai/gpt-5.5", 272001)["output"])
        self.assertAlmostEqual(2.76501, settings.estimate_cost("openai/gpt-5.5", 272001, 1000))
        self.assertNotEqual(settings.estimate_cost("openai/gpt-5.5", 1000, 1000), settings.estimate_cost("deepseek/deepseek-v4-pro", 1000, 1000))

    def test_provider_receipt_is_used_and_missing_receipt_has_no_cache_discount(self):
        self.assertEqual((0.7, False), settings.usage_cost("openai/gpt-5.5", {"cost": 0.7}))
        cost, estimated = settings.usage_cost("anthropic/claude-sonnet-4.6", {"prompt_tokens": 1000, "completion_tokens": 100, "prompt_tokens_details": {"cached_tokens": 1000}}, prompt_cache=True)
        self.assertTrue(estimated)
        self.assertAlmostEqual(0.0075, cost)
        for invalid in (math.nan, math.inf, -1, True, "0.1"):
            with self.subTest(cost=invalid), self.assertRaises(settings.ModelSettingsError):
                settings.usage_cost("openai/gpt-5.5", {"cost": invalid})

    def test_requests_keep_required_features_and_omit_unsupported_sampling(self):
        body = settings.chat_body({"model": "openai/gpt-5.5", "messages": [{"role": "user", "content": "x"}], "max_tokens": 100, "temperature": 0.1, "reasoning": {"effort": "low"}, "tools": [{"type": "function", "function": {"name": "done", "parameters": {"type": "object"}}}], "response_format": {"type": "json_schema", "json_schema": {"strict": True}}})
        self.assertNotIn("temperature", body)
        self.assertIn("reasoning", body)
        self.assertIn("tools", body)
        self.assertEqual({"prompt": 5.0, "completion": 30.0}, body["provider"]["max_price"])
        self.assertTrue(body["provider"]["require_parameters"])
        self.assertFalse(body["provider"]["allow_fallbacks"])
        with self.assertRaises(settings.ModelSettingsError):
            settings.chat_body({"model": "qwen/qwen3-coder", "messages": [{"role": "user", "content": "x"}], "max_tokens": 100, "reasoning": {"effort": "medium"}})

    def test_context_output_and_nonfinite_tokens_fail_closed(self):
        limit = settings.model("openai/gpt-5.5")["maximum_output_tokens"]
        for tokens in (limit + 1, 0, -1, math.inf, math.nan, True, 1.5):
            with self.subTest(tokens=tokens), self.assertRaises(settings.ModelSettingsError):
                settings.validate_context("openai/gpt-5.5", 10, tokens)
        with self.assertRaises(settings.ModelSettingsError):
            settings.validate_context("anthropic/claude-haiku-4.5", 199999, 100)

    def test_registry_rejects_detached_rates_unknown_selections_and_bad_budgets(self):
        registry = settings.load_registry()
        mutations = [
            lambda d: d.update(schema_version=2),
            lambda d: d["roles"]["comp_review"].update(model="unverified/model"),
            lambda d: d["roles"]["comp_review"].update(max_cost_usd=math.inf),
            lambda d: d["roles"]["comp_review"].update(aggregate_max_cost_usd=1),
            lambda d: d["models"]["openai/gpt-5.5"]["provider_rate_limits"].update(completion=20),
            lambda d: d["models"]["openai/gpt-5.5"].update(maximum_output_tokens=-1),
        ]
        for mutate in mutations:
            data = copy.deepcopy(registry)
            mutate(data)
            with self.assertRaises(settings.ModelSettingsError):
                settings.validate_registry(data)

    def test_workflow_defaults_and_explicit_budget_overrides_are_consistent(self):
        for name in ("bounded_propagation", "evidence_radar_review", "distributed_synthesis", "comp_review", "quarterly_chembl_refresh"):
            config = settings.role(name)
            for key, field in config["workflow_env"].items():
                self.assertEqual(str(config[field]), settings.workflow_environment(name)[key])
        self.assertEqual("1.0", settings.workflow_environment("bounded_propagation", {"MAX_COST_USD": "1"})["MAX_COST_USD"])
        for overrides in ({"MAX_COST_USD": "nan"}, {"MAX_COST_USD": "-1"}, {"PROPAGATION_MODEL": "other/model"}, {"UNKNOWN": "1"}):
            with self.assertRaises(settings.ModelSettingsError):
                settings.workflow_environment("bounded_propagation", overrides)
        with self.assertRaises(settings.ModelSettingsError):
            settings.workflow_environment("comp_review", {"PER_COMP_CAP": "6", "AGGREGATE_CAP": "5"})

    def test_role_copies_cannot_mutate_global_defaults(self):
        config = settings.role("evidence_radar_review")
        config["model"] = "anything"
        self.assertEqual("openai/gpt-5.5", settings.role("evidence_radar_review")["model"])

    def test_manifest_bound_library_is_identified_and_unmodified(self):
        import hashlib
        frozen = settings.load_registry()["frozen_consumers"]
        self.assertEqual(1, len(frozen))
        self.assertTrue((ROOT / frozen[0]["manifest"]).is_file())
        self.assertEqual(frozen[0]["sha256"], hashlib.sha256((ROOT / frozen[0]["path"]).read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
