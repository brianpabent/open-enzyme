from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import synthesis_normalize as normalize  # noqa: E402


def load_hyphenated_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


state = load_hyphenated_module("sweep_state_test", SCRIPTS / "sweep-state.py")


class SynthesisNormalizationIncidentTests(unittest.TestCase):
    def test_failed_run_recovers_every_marked_item(self):
        path = Path("logs/v4-synthesis-2026-07-15-eeab5b5.md")
        manifest = normalize.normalize_text(path.read_text(), path)

        self.assertEqual("items", manifest["status"])
        self.assertEqual(10, len(manifest["items"]))
        self.assertEqual(10, manifest["normalization"]["marker_count"])
        self.assertEqual([], manifest["normalization"]["errors"])
        self.assertEqual(
            {"connection": 4, "contradiction": 2, "experiment": 3, "most-curious-thread": 1},
            {
                kind: sum(item["type_slug"] == kind for item in manifest["items"])
                for kind in {item["type_slug"] for item in manifest["items"]}
            },
        )

    def test_false_no_op_is_one_substantive_item(self):
        path = Path("logs/v4-synthesis-2026-07-15-08f10ad.md")
        manifest = normalize.normalize_text(path.read_text(), path)

        self.assertEqual("items", manifest["status"])
        self.assertEqual(1, len(manifest["items"]))
        self.assertEqual("most-curious-thread", manifest["items"][0]["type_slug"])
        self.assertEqual("bold", manifest["normalization"]["recognized_headings"][0]["style"])

    def test_explicit_no_op_is_the_only_zero_item_success(self):
        text = """---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
# Synthesis — test
**Status:** No new synthesis. The trigger was a spelling correction.
"""
        manifest = normalize.normalize_text(text, Path("logs/test-no-op.md"))
        self.assertEqual("no_new_synthesis", manifest["status"])
        self.assertEqual([], manifest["items"])

    def test_unstructured_content_fails_closed(self):
        text = """---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
# Synthesis — test
## Surprising Things
1. **A substantive finding.** It matters.

{{PEER-REVIEW}}
"""
        manifest = normalize.normalize_text(text, Path("logs/test-malformed.md"))
        self.assertEqual("normalization_failed", manifest["status"])
        self.assertTrue(manifest["normalization"]["errors"])

    def test_missing_cosmetic_markers_does_not_drop_structural_items(self):
        text = """---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
# Synthesis — test
## New Connections
1. **A substantive finding.** It matters.
"""
        manifest = normalize.normalize_text(text, Path("logs/test-markerless.md"))
        self.assertEqual("items", manifest["status"])
        self.assertEqual(1, len(manifest["items"]))

    def test_h3_items_and_internal_bold_labels_are_not_section_boundaries(self):
        text = """---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
## New Connections
### 1. First finding.
Body.

**Mechanism**
More body.
{{PEER-REVIEW}}

### 2. Second finding.
Body.
{{PEER-REVIEW}}

**Sources cited:**
- wiki/example.md
"""
        manifest = normalize.normalize_text(text, Path("logs/test-h3.md"))
        self.assertEqual("items", manifest["status"])
        self.assertEqual(2, len(manifest["items"]))
        self.assertIn("More body.", manifest["items"][0]["content"])

    def test_raw_or_canonical_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "v4-synthesis-test.md"
            raw.write_text("""---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
## New Connections
1. **A finding.** Body.
{{PEER-REVIEW}}
""")
            manifest, manifest_path = normalize.normalize_file(raw, root / "normalized.json")
            self.assertEqual("items", manifest["status"])
            normalize.verify_manifest(manifest_path)

            tampered = json.loads(manifest_path.read_text())
            tampered["items"][0]["content"] += " changed"
            manifest_path.write_text(json.dumps(tampered))
            with self.assertRaises(normalize.NormalizationError):
                normalize.verify_manifest(manifest_path)

            normalize.normalize_file(raw, manifest_path)

            metadata_tamper = json.loads(manifest_path.read_text())
            metadata_tamper["source"]["diff_base"] = "f" * 40
            manifest_path.write_text(json.dumps(metadata_tamper))
            with self.assertRaises(normalize.NormalizationError):
                normalize.verify_manifest(manifest_path)

            normalize.normalize_file(raw, manifest_path)

            raw.write_text(raw.read_text() + "\ntampered\n")
            with self.assertRaises(normalize.NormalizationError):
                normalize.verify_manifest(manifest_path)

    def test_served_model_and_corpus_snapshot_are_preserved(self):
        text = """---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
corpus_commit: cccccccccccccccccccccccccccccccccccccccc
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
reviewer_model: google/gemini-2.5-pro
reviewer_model_requested: x-ai/grok-4.20
---
## New Connections
1. **A finding.** Body.
{{PEER-REVIEW}}
"""
        manifest = normalize.normalize_text(text, Path("logs/test-fallback.md"))
        self.assertEqual("google/gemini-2.5-pro", manifest["source"]["synthesizer_model"])
        self.assertEqual(
            "cccccccccccccccccccccccccccccccccccccccc",
            manifest["source"]["corpus_commit_sha"],
        )


class EmitterRegressionTests(unittest.TestCase):
    def test_emitter_keeps_same_day_similar_artifacts_distinct(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "normalized.json"
            raw = Path("logs/v4-synthesis-2026-07-15-eeab5b5.md")
            normalize.normalize_file(raw, manifest_path)
            reviews = root / "reviews.txt"
            reviews.write_text("\n<<<NEXT>>>\n".join(
                "> **Pass 3 review — Restatement.** Regression fixture."
                for _ in range(10)
            ))
            queue = root / "queue"
            history = root / "history"
            command = [
                sys.executable,
                "scripts/synthesis-emit-files.py",
                "--synthesis-log", str(raw),
                "--normalized-manifest", str(manifest_path),
                "--reviews-file", str(reviews),
                "--commit-sha", "eeab5b53054b93544c428a476dad06a8f8fe2621",
                "--diff-base", "b52b9a893b6256d7d34eeb74e9a7748950bd7410",
                "--trigger-files", "wiki/example.md",
                "--synthesizer", "x-ai/grok-4.20",
                "--reviewer", "deepseek/deepseek-v4-pro",
                "--queue-dir", str(queue),
                "--history-dir", str(history),
                "--sweep-date", "2026-07-15",
            ]
            subprocess.run(command, cwd=REPO_ROOT, check=True, capture_output=True, text=True)
            self.assertEqual(10, len(list(queue.glob("*.md"))))
            history_text = (history / "2026-07-15-eeab5b5.md").read_text()
            self.assertIn("items_emitted: 10", history_text)
            self.assertIn("canonical_items_sha256:", history_text)

            # The recovery rerun emitted the same Most Curious headline on the
            # same date. Before artifact IDs entered filenames, this 11th item
            # silently overwrote the first artifact's 10th queue file.
            second_raw = Path("logs/v4-synthesis-2026-07-15-08f10ad.md")
            second_manifest_path = root / "normalized-second.json"
            first_manifest = json.loads(manifest_path.read_text())
            second_manifest, _ = normalize.normalize_file(
                second_raw, second_manifest_path
            )
            second_reviews = root / "reviews-second.txt"
            second_reviews.write_text(
                "> **Pass 3 review — Partial.** Second regression fixture.\n"
            )
            second_command = [
                sys.executable,
                "scripts/synthesis-emit-files.py",
                "--synthesis-log", str(second_raw),
                "--normalized-manifest", str(second_manifest_path),
                "--reviews-file", str(second_reviews),
                "--commit-sha", "08f10ad7adc83d9b373815ed42fa0663dafe1779",
                "--trigger-files", "wiki/example.md",
                "--queue-dir", str(queue),
                "--history-dir", str(history),
                "--sweep-date", "2026-07-15",
            ]
            subprocess.run(
                second_command, cwd=REPO_ROOT, check=True, capture_output=True, text=True
            )
            queue_files = list(queue.glob("*.md"))
            self.assertEqual(11, len(queue_files))
            queue_text = "\n".join(path.read_text() for path in queue_files)
            self.assertIn(first_manifest["sweep_id"], queue_text)
            self.assertIn(second_manifest["sweep_id"], queue_text)

    def test_no_op_requires_explicit_normalized_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "v4-synthesis-no-op.md"
            raw.write_text("""---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
**Status:** No new synthesis. Typo-only trigger.
""")
            _manifest, manifest_path = normalize.normalize_file(raw, root / "normalized.json")
            reviews = root / "reviews.txt"
            reviews.write_text("EXPLICIT_NO_OP\n")
            history = root / "history"
            command = [
                sys.executable,
                "scripts/synthesis-emit-files.py",
                "--synthesis-log", str(raw),
                "--normalized-manifest", str(manifest_path),
                "--reviews-file", str(reviews),
                "--commit-sha", "a" * 40,
                "--trigger-files", "wiki/example.md",
                "--history-dir", str(history),
                "--queue-dir", str(root / "queue"),
                "--sweep-date", "2026-07-15",
            ]
            subprocess.run(command, cwd=REPO_ROOT, check=True, capture_output=True, text=True)
            history_text = (history / "2026-07-15-aaaaaaa.md").read_text()
            self.assertIn("items_emitted: 0", history_text)
            self.assertIn("explicit normalized no-new-synthesis", history_text)


class ForcedFinalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = load_hyphenated_module("sweep_3_review_test", SCRIPTS / "sweep-3-review.py")

    def test_forced_final_request_physically_omits_tools(self):
        bodies = []

        def fake_call(_api_key, body):
            bodies.append(body)
            return {
                "choices": [{
                    "message": {"content": "> **Pass 3 review — Confirmed.** Done."},
                    "finish_reason": "stop",
                }],
                "usage": {},
            }

        with mock.patch.object(self.review, "call_openrouter_raw", side_effect=fake_call):
            content, *_ = self.review.run_agentic_review(
                "key", "deepseek/deepseek-v4-pro", "prompt", max_iterations=0, max_tokens=100
            )

        self.assertIn("Confirmed", content)
        self.assertEqual(1, len(bodies))
        self.assertNotIn("tools", bodies[0])
        self.assertNotIn("tool_choice", bodies[0])

    def test_large_file_reads_are_range_bounded_and_exact_slice_deduped(self):
        self.review._READ_CACHE.clear()
        first = self.review.tool_read_file({
            "path": "wiki/validation-experiments.md",
            "start_line": 1259,
            "end_line": 1265,
        })
        self.assertIn("[lines 1259-1265", first)
        self.assertIn("Houttuynia", first)

        repeated = self.review.tool_read_file({
            "path": "wiki/validation-experiments.md",
            "start_line": 1259,
            "end_line": 1265,
        })
        self.assertIn("ALREADY READ", repeated)

        another_range = self.review.tool_read_file({
            "path": "wiki/validation-experiments.md",
            "start_line": 1356,
            "end_line": 1362,
        })
        self.assertIn("[lines 1356-1362", another_range)


class SweepStateBindingTests(unittest.TestCase):
    def test_cursor_advance_records_hash_binding_and_rejects_cursor_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "v4-synthesis-test.md"
            raw.write_text("""---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
## New Connections
1. **A finding.** Body.
{{PEER-REVIEW}}
""")
            manifest, manifest_path = normalize.normalize_file(raw, root / "normalized.json")
            registry_path = root / "sweep-state.json"
            registry_path.write_text(json.dumps({
                "schema_version": 2,
                "last_successful_propagation": None,
                "last_successful_synthesis": {
                    "coverage_commit": manifest["source"]["diff_base"]
                },
                "comp_reviews": {},
                "unresolved_failures": [],
            }))
            args = argparse.Namespace(
                commit="cccccccccccccccccccccccccccccccccccccccc",
                synthesis_log=str(raw),
                normalized_manifest=str(manifest_path),
                expected_diff_base=manifest["source"]["diff_base"],
                trigger_files="wiki/example.md",
                run_id="test-run",
                trigger="workflow_dispatch",
            )
            completed = subprocess.CompletedProcess([], 0)
            with mock.patch.object(state, "REGISTRY_PATH", registry_path), mock.patch.object(
                state.subprocess, "run", return_value=completed
            ):
                state.cmd_update_success(args)
                saved = json.loads(registry_path.read_text())
                self.assertEqual(manifest["sweep_id"], saved["last_successful_synthesis"]["sweep_id"])
                self.assertEqual(
                    manifest["canonical_items_sha256"],
                    saved["last_successful_synthesis"]["coverage_receipt_sha256"],
                )
                self.assertEqual(
                    manifest["source"]["corpus_commit_sha"],
                    saved["last_successful_synthesis"]["coverage_commit"],
                )
                self.assertEqual(args.commit, saved["last_successful_synthesis"]["result_commit"])

                saved["last_successful_synthesis"]["coverage_commit"] = "dddddddddddddddddddddddddddddddddddddddd"
                registry_path.write_text(json.dumps(saved))
                with self.assertRaises(SystemExit):
                    state.cmd_update_success(args)

    def test_supplemental_recovery_and_rebind_preserve_cursor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / "v4-synthesis-test.md"
            raw.write_text("""---
commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
corpus_commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
diff_base: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
trigger_files: wiki/example.md
---
## New Connections
1. **A finding.** Body.
{{PEER-REVIEW}}
""")
            _manifest, manifest_path = normalize.normalize_file(raw, root / "normalized.json")
            registry_path = root / "sweep-state.json"
            cursor = "dddddddddddddddddddddddddddddddddddddddd"
            registry_path.write_text(json.dumps({
                "schema_version": 2,
                "last_successful_propagation": None,
                "last_successful_synthesis": {
                    "coverage_commit": cursor,
                    "result_commit": cursor,
                },
                "comp_reviews": {},
                "unresolved_failures": [],
            }))
            recovery = argparse.Namespace(
                review_commit="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
                synthesis_log=str(raw),
                normalized_manifest=str(manifest_path),
                run_id="recovery-run",
                trigger="workflow_dispatch",
            )
            completed = subprocess.CompletedProcess([], 0)
            with mock.patch.object(state, "REGISTRY_PATH", registry_path), mock.patch.object(
                state.subprocess, "run", return_value=completed
            ):
                state.cmd_record_recovery(recovery)
                saved = json.loads(registry_path.read_text())
                self.assertEqual(cursor, saved["last_successful_synthesis"]["coverage_commit"])

                rebind = argparse.Namespace(
                    old_commit=cursor,
                    new_commit="ffffffffffffffffffffffffffffffffffffffff",
                )
                state.cmd_rebind_review_commit(rebind)
                rebound = json.loads(registry_path.read_text())
                self.assertEqual(cursor, rebound["last_successful_synthesis"]["coverage_commit"])
                self.assertEqual(rebind.new_commit, rebound["last_successful_synthesis"]["result_commit"])

    def test_v1_migration_splits_cursors_without_carrying_success_history(self):
        legacy = {
            "schema_version": 1,
            "last_successful_sweep": {
                "commit": "a" * 40,
                "review_commit": "b" * 40,
                "timestamp": "2026-07-15T00:00:00Z",
                "trigger_files": ["wiki/example.md"],
                "normalized_item_count": 3,
            },
            "recent_runs": [
                {"run_id": "ok", "outcome": "success"},
                {"run_id": "bad", "outcome": "failure", "failed_phase": "pass-2-synthesize"},
            ],
        }
        migrated = state.migrate_v1_to_v2(legacy)
        self.assertEqual(2, migrated["schema_version"])
        self.assertEqual("a" * 40, migrated["last_successful_propagation"]["coverage_commit"])
        self.assertEqual("a" * 40, migrated["last_successful_synthesis"]["coverage_commit"])
        self.assertEqual(["bad"], [f["id"] for f in migrated["unresolved_failures"]])
        self.assertNotIn("recent_runs", migrated)

    def test_comp_review_records_separate_lane_eligibility(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry_path = Path(tmp) / "sweep-state.json"
            registry_path.write_text(json.dumps(state._empty_registry()))
            args = argparse.Namespace(
                comp_id="comp-047",
                comp_dir="wiki/etc/experiments/comp-047-example",
                artifact_manifest_sha256="1" * 64,
                source_commit="a" * 40,
                review_receipt="wiki/etc/experiments/comp-047-example/reviews/push-review.md",
                comp_verdict="clean_with_limitations",
                propagation_eligibility="eligible_with_warning",
                synthesis_eligibility="blocked",
                derived_paths="wiki/example.md",
                cost_usd=0.12,
            )
            with mock.patch.object(state, "REGISTRY_PATH", registry_path):
                state.cmd_record_comp_review(args)
            saved = json.loads(registry_path.read_text())["comp_reviews"]["comp-047"]
            self.assertEqual("eligible_with_warning", saved["propagation_eligibility"])
            self.assertEqual("blocked", saved["synthesis_eligibility"])


if __name__ == "__main__":
    unittest.main()
