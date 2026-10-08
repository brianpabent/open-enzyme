"""Offline integration contracts: no credentials, network, or paid evaluation."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import math
import os
import re
import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import model_settings as settings

ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    name = "settings_test_" + filename.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{filename}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


radar = load("evidence-radar")
propagation = load("sweep-1-propagate")
distributed = load("distributed-synthesis")
comp = load("comp-review")
evaluation = load("eval-propagation")


def response(usage=None):
    return {"choices": [{"finish_reason": "stop", "message": {"content": "{}"}}],
            "usage": usage if usage is not None else {"prompt_tokens": 1000, "completion_tokens": 100, "cost": 0.0123}}


def capture_curl(captured):
    def run(command, **kwargs):
        # Only the actual request transport is mocked; request construction,
        # feature/context checks and cost accounting still execute.
        assert command[0] == "curl", command
        path = command[command.index("-d") + 1].removeprefix("@")
        captured.append(json.loads(Path(path).read_text()))
        return subprocess.CompletedProcess(command, 0, json.dumps(response()), "")
    return run


class ConsumerTests(unittest.TestCase):
    def test_completed_propagation_cli_reports_the_same_billed_cost_as_workflow_receipt(self):
        loop = {"cached_input_tokens": 1000, "input_tokens": 2000, "output_tokens": 100,
                "cost_usd": 0.0123, "cost_is_estimated": False, "iterations": 1,
                "completed": True, "hit_iter_cap": False, "done_summary": "No changes", "last_text": ""}
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "github-output"
            arguments = ["propagate", "--commit-sha", "HEAD", "--trigger-files", "wiki/gout-pathophysiology.md", "--dry-run"]
            error = io.StringIO()
            with patch.object(sys, "argv", arguments), patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}), patch.object(propagation, "read_api_key", return_value="offline-placeholder"), patch.object(propagation, "run_agentic_loop", return_value=loop), patch.object(propagation, "stage_and_commit", return_value=(False, [])) as write, contextlib.redirect_stderr(error):
                propagation.main()
            self.assertIn("cost=$0.0123", error.getvalue())
            self.assertIn("cost_usd=0.012300", output.read_text())
            self.assertIn("cost_is_estimated=false", output.read_text())
            self.assertTrue(write.call_args.args[-1])

    def test_propagation_and_evaluation_validate_real_request_before_transport(self):
        for module in (propagation, evaluation):
            captured = []
            with self.subTest(module=module.__name__), patch.object(module.subprocess, "run", side_effect=capture_curl(captured)):
                module.call_openrouter("offline-placeholder", "openai/gpt-5.5", [{"role": "user", "content": "test"}])
            body = captured[0]
            self.assertEqual(module.ROLE["output_tokens"], body["max_tokens"])
            self.assertIn("tools", body)
            self.assertNotIn("temperature", body)
            self.assertEqual({"prompt": 5, "completion": 30}, body["provider"]["max_price"])

    def test_distributed_transport_and_ledger_share_selected_model(self):
        captured = []
        ledger = distributed.CostLedger(5)
        client = distributed.OpenRouter("offline-placeholder", ledger)
        with patch.object(distributed.subprocess, "run", side_effect=capture_curl(captured)):
            self.assertEqual({}, client.json_call(stage="review", model="openai/gpt-5.5", prompt="test", max_tokens=2500))
        self.assertNotIn("temperature", captured[0])
        self.assertEqual("json_object", captured[0]["response_format"]["type"])
        self.assertEqual("openai/gpt-5.5", ledger.calls[0]["model"])
        self.assertEqual(0.0123, ledger.actual)
        self.assertFalse(ledger.calls[0]["cost_estimated"])

    def test_comp_review_preserves_reasoning_and_accounts_for_missing_provider_cost(self):
        captured = []
        def transport(key, body):
            captured.append(body)
            return response({"prompt_tokens": 1000, "completion_tokens": 100})
        with patch.object(comp, "call_openrouter", side_effect=transport):
            _, usage = comp.review("offline-placeholder", "openai/gpt-5.5", "test", tools=True, max_tokens=16000)
        self.assertNotIn("temperature", captured[0])
        self.assertEqual("medium", captured[0]["reasoning"]["effort"])
        self.assertIn("tools", captured[0])
        self.assertAlmostEqual(0.008, usage["cost_usd"])

    def test_radar_preserves_strict_schema_and_receipt_cost(self):
        captured = []
        def open_request(request, **kwargs):
            captured.append(json.loads(request.data))
            return io.BytesIO(json.dumps(response()).encode())
        with patch.object(radar, "openrouter_key", return_value="offline-placeholder"), patch.object(radar, "build_opener") as opener:
            opener.return_value.open.side_effect = open_request
            _, usage = radar.openrouter_review({"candidates": []}, "test", model="openai/gpt-5.5", maximum_output_tokens=8000)
        self.assertTrue(captured[0]["response_format"]["json_schema"]["strict"])
        self.assertNotIn("temperature", captured[0])
        self.assertEqual(0.0123, usage["cost_usd"])
        self.assertFalse(usage["cost_is_estimated"])

    def test_unknown_native_and_incompatible_models_never_reach_transport(self):
        messages = [{"role": "user", "content": "test"}]
        for name in ("unverified/cheap", "claude-sonnet-4-6"):
            for module in (propagation, evaluation):
                with self.subTest(model=name, module=module.__name__), patch.object(module.subprocess, "run") as transport:
                    with self.assertRaises(settings.ModelSettingsError):
                        module.call_openrouter("offline-placeholder", name, messages)
                    transport.assert_not_called()
            with patch.object(distributed.subprocess, "run") as transport:
                with self.assertRaises(settings.ModelSettingsError):
                    distributed.OpenRouter("offline-placeholder", distributed.CostLedger(5)).json_call(stage="test", model=name, prompt="test", max_tokens=100)
                transport.assert_not_called()
            with patch.object(comp, "call_openrouter") as transport:
                with self.assertRaises(settings.ModelSettingsError):
                    comp.review("offline-placeholder", name, "test", tools=True, max_tokens=100)
                transport.assert_not_called()
            with patch.object(radar, "openrouter_key") as key, patch.object(radar, "build_opener") as transport:
                with self.assertRaises(radar.RadarError):
                    radar.openrouter_review({"candidates": []}, "test", model=name, maximum_output_tokens=100)
                key.assert_not_called()
                transport.assert_not_called()
        with patch.object(comp, "call_openrouter") as transport:
            with self.assertRaisesRegex(settings.ModelSettingsError, "reasoning"):
                comp.review("offline-placeholder", "qwen/qwen3-coder", "test", tools=True, max_tokens=100)
            transport.assert_not_called()

    def test_unknown_cli_models_and_invalid_budgets_fail_before_credentials_or_writes(self):
        cases = [
            (comp, ["--comp-dir", "missing", "--model", "unknown/model"], "resolve_comp"),
            (comp, ["--comp-dir", "missing", "--estimated-output-usd-per-million", "20"], "resolve_comp"),
            (comp, ["--comp-dir", "missing", "--max-cost-usd", "nan"], "resolve_comp"),
            (evaluation, ["--scenario", "missing", "--model", "unknown/model"], "read_api_key"),
            (evaluation, ["--scenario", "missing", "--model", "openai/gpt-5.5", "--max-iterations", "0"], "read_api_key"),
            (propagation, ["--commit-sha", "HEAD", "--trigger-files", "wiki/missing.md", "--model", "unknown/model"], "read_api_key"),
            (propagation, ["--commit-sha", "HEAD", "--trigger-files", "wiki/missing.md", "--max-cost-usd", "nan"], "read_api_key"),
        ]
        for module, arguments, gate in cases:
            with self.subTest(module=module.__name__, args=arguments), patch.object(sys, "argv", [module.__name__, *arguments]), patch.object(module, gate) as later:
                with self.assertRaises((settings.ModelSettingsError, SystemExit)):
                    module.main()
                later.assert_not_called()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "not-created"
            for arguments in (["--reviewer-model", "unknown/model"], ["--max-cost-usd", "nan"], ["--review-max-tokens", "0"]):
                args = distributed.parser().parse_args(["--work-dir", str(output), "--diff-base", "HEAD", *arguments])
                with patch.object(distributed, "api_key") as key:
                    with self.assertRaises(settings.ModelSettingsError):
                        distributed.run_pipeline(args)
                    key.assert_not_called()
                self.assertFalse(output.exists())

    def test_each_cost_consumer_uses_same_exact_model_rates_and_long_context_tiers(self):
        for model in ("openai/gpt-5.5", "deepseek/deepseek-v4-pro", "anthropic/claude-sonnet-5.5"):
            for input_tokens in (1000, 272001):
                with self.subTest(model=model, tokens=input_tokens):
                    expected = settings.estimate_cost(model, input_tokens, 8000)
                    self.assertAlmostEqual(expected, comp.estimate_cost(input_tokens * 4, 8000, model=model))
                    self.assertAlmostEqual(expected, distributed.CostLedger(100).project(model, input_tokens * 4, 8000))
                    packet = {"candidates": [{}]}
                    # Include the exact serialized packet contribution in the
                    # existing radar input proxy, without changing its contract.
                    prompt = "x" * (input_tokens * 4 - len(json.dumps(packet, ensure_ascii=False)))
                    self.assertAlmostEqual(expected, radar.estimated_review_cost(packet, prompt, {"model": model}))
        old_rates = {"model": "openai/gpt-5.5", "estimated_input_usd_per_million_tokens": 5, "estimated_output_usd_per_million_tokens": 30}
        selected = radar.review_settings(old_rates, "anthropic/claude-sonnet-5.5")
        self.assertEqual((2, 10), radar.review_token_rates(selected))
        with self.assertRaises(radar.RadarError):
            radar.review_settings({"model": "openai/gpt-5.5", "estimated_output_usd_per_million_tokens": 20})

    def test_cost_ledger_rejects_nan_and_unknown_prices_before_authorization(self):
        for cap in (math.nan, math.inf, -1, 0):
            with self.assertRaises(settings.ModelSettingsError):
                distributed.CostLedger(cap)
        ledger = distributed.CostLedger(0.001)
        with self.assertRaisesRegex(RuntimeError, "above hard cap"):
            ledger.authorize("openai/gpt-5.5", 4000, 8000)
        with self.assertRaises(settings.ModelSettingsError):
            ledger.project("unknown/cheap", 1000, 100)

    def test_fresh_synthesis_prepare_only_is_credentials_free_and_model_bound(self):
        env = {key: value for key, value in os.environ.items() if "API_KEY" not in key}
        result = subprocess.run([sys.executable, "scripts/fresh-synthesis.py", "--prepare-only"], cwd=ROOT, env=env, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        prepared = json.loads(result.stdout)
        self.assertEqual(settings.role("manual_fresh_synthesis")["model"], prepared["model"])
        self.assertIsNone(prepared["max_cost_usd"])
        self.assertEqual(settings.registry_sha256(), prepared["model_settings_sha256"])
        self.assertAlmostEqual(settings.estimate_cost(prepared["model"], prepared["input_token_estimate"], prepared["max_output_tokens"]), prepared["projected_cost_usd"])
        for arguments in (["--model", "unknown/cheap"], ["--max-tokens", "0"], ["--model", "meta-llama/llama-4-scout", "--max-tokens", "16385"]):
            failed = subprocess.run([sys.executable, "scripts/fresh-synthesis.py", "--prepare-only", *arguments], cwd=ROOT, env=env, capture_output=True, text=True)
            self.assertNotEqual(0, failed.returncode)
            self.assertNotIn("API_KEY", failed.stderr)

    def test_fresh_synthesis_override_request_and_report_use_verified_model_and_provider_cost(self):
        captured = []
        curl = capture_curl(captured)
        def transport(command, **kwargs):
            if command[0] == "git":
                return subprocess.CompletedProcess(command, 0, "offline-substrate\n", "")
            return curl(command, **kwargs)
        with tempfile.TemporaryDirectory() as tmp, patch.object(sys, "argv", ["fresh-synthesis", "--model", "openai/gpt-5.5"]), patch.dict(os.environ, {"OPENROUTER_API_KEY": "offline-placeholder"}), patch.object(subprocess, "run", side_effect=transport), patch.object(tempfile, "gettempdir", return_value=tmp), contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(str(ROOT / "scripts/fresh-synthesis.py"), run_name="__main__")
            files = list((Path(tmp) / "open-enzyme-fresh-synthesis").glob("*.md"))
            self.assertEqual(1, len(files))
            self.assertIn("cost_usd: 0.0123", files[0].read_text())
            self.assertIn("cost_is_estimated: false", files[0].read_text())
        self.assertEqual("openai/gpt-5.5", captured[0]["model"])
        self.assertNotIn("temperature", captured[0])
        self.assertEqual({"prompt": 10, "completion": 45}, captured[0]["provider"]["max_price"])

    def test_emission_defaults_are_labels_and_workflow_uses_actual_selected_reviewer(self):
        # Labels can describe a pipeline; they are not request model IDs.
        with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
            emitter = load("synthesis-emit-files")
        role = settings.role("synthesis_emission")
        self.assertEqual(role, emitter.ROLE)
        workflow = (ROOT / ".github/workflows/wiki-sweep.yml").read_text()
        self.assertIn('["models"]["reviewer"]', workflow)
        self.assertIn('--reviewer "$reviewer"', workflow)
        self.assertNotIn('--reviewer "openai/gpt-5.5"', workflow)


class WorkflowSettingsTests(unittest.TestCase):
    def test_actual_workflow_loader_commands_preserve_defaults_and_reject_invalid_overrides(self):
        roles = {"wiki-propagate.yml": "bounded_propagation", "wiki-sweep.yml": "distributed_synthesis", "evidence-radar.yml": "evidence_radar_review", "comp-review.yml": "comp_review", "chembl-refresh.yml": "quarterly_chembl_refresh"}
        for filename, role in roles.items():
            text = (ROOT / ".github/workflows" / filename).read_text()
            step = re.search(r"      - name: Load verified[^\n]*\n(.*?)(?=\n      - |\Z)", text, re.S).group(1)
            if "run: |" in step:
                script = "\n".join(line[10:] for line in step.split("run: |\n", 1)[1].splitlines() if line.startswith("          "))
            else:
                script = step.split("run: ", 1)[1].strip()
            overrides = re.findall(r"^          ([A-Z_]+_OVERRIDE):", step, re.M)
            with self.subTest(workflow=filename), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / "github-env"
                env = dict(os.environ, GITHUB_ENV=str(path), **{name: "" for name in overrides})
                result = subprocess.run(["bash", "-euo", "pipefail", "-c", script], cwd=ROOT, env=env, capture_output=True, text=True)
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertEqual(settings.workflow_environment(role), dict(line.split("=", 1) for line in path.read_text().splitlines()))
                if overrides:
                    path.write_text("")
                    env[overrides[0]] = "nan"
                    invalid = subprocess.run(["bash", "-euo", "pipefail", "-c", script], cwd=ROOT, env=env, capture_output=True, text=True)
                    self.assertNotEqual(0, invalid.returncode)
                    self.assertEqual("", path.read_text())
        native = (ROOT / ".github/workflows/chembl-refresh.yml").read_text()
        self.assertIn('claude --model "$ANTHROPIC_MODEL"', native)
        propagation_workflow = (ROOT / ".github/workflows/wiki-propagate.yml").read_text()
        self.assertIn('--max-iterations "$MAX_ITERATIONS"', propagation_workflow)


if __name__ == "__main__":
    unittest.main()
