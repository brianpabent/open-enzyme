from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
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


def synthesis_fixture() -> str:
    sections = [
        ("New Connections", 4),
        ("Contradictions", 2),
        ("Proposed Experiments", 3),
        ("Most Curious Thread", 1),
    ]
    body = ["---", f"commit: {'a' * 40}", f"diff_base: {'b' * 40}", "trigger_files: wiki/example.md", "---"]
    for heading, count in sections:
        body.append(f"## {heading}")
        for index in range(1, count + 1):
            body.extend([f"{index}. **{heading} fixture {index}.** Evidence-bearing body.", "{{PEER-REVIEW}}"])
    return "\n".join(body) + "\n"


class SynthesisNormalizationIncidentTests(unittest.TestCase):
    def test_failed_run_recovers_every_marked_item(self):
        path = Path("tests/fixtures/synthesis-ten-items.md")
        manifest = normalize.normalize_text(synthesis_fixture(), path)

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
        path = Path("tests/fixtures/synthesis-one-item.md")
        text = f"""---
commit: {'a' * 40}
diff_base: {'b' * 40}
trigger_files: wiki/example.md
---
## Most Curious Thread
**Most Curious Thread 1: A real finding.** Evidence-bearing body.
{{{{PEER-REVIEW}}}}
"""
        manifest = normalize.normalize_text(text, path)

        self.assertEqual("items", manifest["status"])
        self.assertEqual(1, len(manifest["items"]))
        self.assertEqual("most-curious-thread", manifest["items"][0]["type_slug"])
        self.assertEqual("atx", manifest["normalization"]["recognized_headings"][0]["style"])

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
            raw = root / "synthesis-ten-items.md"
            raw.write_text(synthesis_fixture())
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
                "--sweep-date", "2026-07-15",
            ]
            subprocess.run(command, cwd=REPO_ROOT, check=True, capture_output=True, text=True)
            self.assertEqual(10, len(list(queue.glob("*.md"))))
            self.assertFalse(history.exists())

            # The recovery rerun emitted the same Most Curious headline on the
            # same date. Before artifact IDs entered filenames, this 11th item
            # silently overwrote the first artifact's 10th queue file.
            second_raw = root / "synthesis-one-item.md"
            second_raw.write_text(f"""---
commit: {'c' * 40}
diff_base: {'b' * 40}
trigger_files: wiki/example.md
---
## Most Curious Thread
**Most Curious Thread 1: A real finding.** Second evidence-bearing body.
{{{{PEER-REVIEW}}}}
""")
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
            command = [
                sys.executable,
                "scripts/synthesis-emit-files.py",
                "--synthesis-log", str(raw),
                "--normalized-manifest", str(manifest_path),
                "--reviews-file", str(reviews),
                "--commit-sha", "a" * 40,
                "--trigger-files", "wiki/example.md",
                "--queue-dir", str(root / "queue"),
                "--sweep-date", "2026-07-15",
            ]
            subprocess.run(command, cwd=REPO_ROOT, check=True, capture_output=True, text=True)
            self.assertFalse((root / "history").exists())


class SweepStateBindingTests(unittest.TestCase):
    def test_unverified_migrated_synthesis_cursor_forces_full_source_set(self):
        registry = {
            "schema_version": 2,
            "last_successful_propagation": None,
            "last_successful_synthesis": {
                "coverage_commit": "a" * 40,
                "integrity_status": "migrated_cursor_unverified",
            },
            "comp_reviews": {},
            "unresolved_failures": [],
        }
        with mock.patch.object(state, "read_registry", return_value=registry), mock.patch.object(
            state,
            "_all_synthesis_paths",
            return_value=[
                "wiki/a.md",
                "wiki/etc/experiments/comp-001-example/reviews/review.md",
                "wiki/hypotheses/H01.md",
            ],
        ):
            output = StringIO()
            with redirect_stdout(output):
                state.cmd_pending_synthesis_paths(argparse.Namespace())
        self.assertEqual(
            ["wiki/a.md", "wiki/hypotheses/H01.md"],
            output.getvalue().splitlines(),
        )

    def test_unverified_initial_synthesis_cursor_forces_full_source_set(self):
        registry = {
            "schema_version": 2,
            "last_successful_propagation": None,
            "last_successful_synthesis": {
                "coverage_commit": "a" * 40,
                "integrity_status": "initial_cursor_unverified",
            },
            "comp_reviews": {},
            "unresolved_failures": [],
        }
        with mock.patch.object(state, "read_registry", return_value=registry), mock.patch.object(
            state,
            "_all_synthesis_paths",
            return_value=["wiki/a.md", "wiki/hypotheses/H01.md"],
        ):
            output = StringIO()
            with redirect_stdout(output):
                state.cmd_pending_synthesis_paths(argparse.Namespace())
        self.assertEqual(
            ["wiki/a.md", "wiki/hypotheses/H01.md"],
            output.getvalue().splitlines(),
        )

    def test_unverified_initial_cursor_requires_synthesis_without_diff_probe(self):
        registry = {
            "schema_version": 2,
            "last_successful_synthesis": {
                "coverage_commit": "a" * 40,
                "integrity_status": "initial_cursor_unverified",
            },
        }
        with mock.patch.object(state, "read_registry", return_value=registry), mock.patch.object(
            state,
            "_git_changed_paths",
        ) as changed_paths:
            output = StringIO()
            with redirect_stdout(output):
                state.cmd_should_sweep(argparse.Namespace())
        self.assertEqual("run", output.getvalue().strip())
        changed_paths.assert_not_called()

    def test_comp_artifacts_collapse_to_one_semantic_propagation_trigger(self):
        registry = {
            "schema_version": 2,
            "last_successful_propagation": {
                "coverage_commit": "a" * 40,
                "deferred_paths": [],
                "blocked_paths": [],
            },
            "last_successful_synthesis": None,
            "comp_reviews": {},
            "unresolved_failures": [],
        }
        active_dir = Path("wiki/etc/experiments/comp-038-tier-2-butyrate-assay-audit")
        tombstone_dir = Path("wiki/etc/experiments/comp-029-combined-cp0-systems-model")
        changed = [
            str(active_dir / "README.md"),
            str(active_dir / "inputs/provenance.md"),
            str(active_dir / "outputs/summary.md"),
            str(tombstone_dir / "README.md"),
            str(tombstone_dir / "outputs/summary.md"),
            "wiki/urate-transport.md",
        ]
        with mock.patch.object(state, "_git_changed_paths", return_value=changed):
            paths = state._pending_propagation_paths(registry)
        self.assertEqual(
            [
                str(tombstone_dir / "invalidation.json"),
                str(active_dir / "README.md"),
                "wiki/urate-transport.md",
            ],
            paths,
        )

    def test_propagation_discovers_comp_artifacts_at_any_depth(self):
        registry = {
            "schema_version": 2,
            "last_successful_propagation": {
                "coverage_commit": "a" * 40,
                "deferred_paths": [],
                "blocked_paths": [],
            },
            "last_successful_synthesis": None,
            "comp_reviews": {},
            "unresolved_failures": [],
        }
        changed = [
            "wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/"
            "v2-env/source_docs/esm/README.md"
        ]
        with mock.patch.object(state, "_git_changed_paths", return_value=changed) as git_paths:
            paths = state._pending_propagation_paths(registry)
        self.assertIn(
            "wiki/etc/experiments/comp-022-clockbase-uricase-cassette-ranking/"
            "invalidation.json",
            paths,
        )
        self.assertIn(
            "wiki/etc/experiments/comp-*/**",
            git_paths.call_args.args[1],
        )

    def test_propagation_backlog_is_resumable_without_reprocessing_blocked_paths(self):
        registry = {
            "schema_version": 2,
            "last_successful_propagation": {
                "coverage_commit": "a" * 40,
                "deferred_paths": ["wiki/b.md", "wiki/c.md"],
                "blocked_paths": ["wiki/released.md"],
            },
            "last_successful_synthesis": None,
            "comp_reviews": {
                "comp-047": {
                    "comp_dir": "wiki/etc/experiments/comp-047-example",
                    "derived_paths": ["wiki/c.md"],
                    "propagation_eligibility": "blocked",
                }
            },
            "unresolved_failures": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            deferred_path = Path(tmp) / "deferred.txt"
            args = argparse.Namespace(
                max_paths=2,
                deferred_output=str(deferred_path),
            )
            with mock.patch.object(state, "read_registry", return_value=registry), mock.patch.object(
                state,
                "_git_changed_paths",
                return_value=["wiki/a.md", "wiki/released.md"],
            ):
                output = StringIO()
                with redirect_stdout(output):
                    state.cmd_pending_propagation_paths(args)

            self.assertEqual(
                ["wiki/a.md", "wiki/b.md"],
                output.getvalue().splitlines(),
            )
            self.assertEqual(
                ["wiki/released.md"],
                deferred_path.read_text().splitlines(),
            )

    def test_propagation_receipt_retains_source_and_deferred_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry_path = Path(tmp) / "sweep-state.json"
            registry_path.write_text(json.dumps({
                "schema_version": 2,
                "last_successful_propagation": {
                    "coverage_commit": "a" * 40,
                },
                "last_successful_synthesis": None,
                "comp_reviews": {},
                "unresolved_failures": [],
            }))
            args = argparse.Namespace(
                coverage_commit="c" * 40,
                source_commit="b" * 40,
                result_commit="c" * 40,
                expected_cursor="a" * 40,
                changed_paths="wiki/a.md,wiki/b.md",
                affected_paths="wiki/dependent.md",
                blocked_paths="wiki/blocked.md",
                deferred_paths="wiki/c.md,wiki/d.md",
                cost_usd=0.1,
            )
            with mock.patch.object(state, "REGISTRY_PATH", registry_path):
                state.cmd_update_propagation(args)
            saved = json.loads(registry_path.read_text())[
                "last_successful_propagation"
            ]
            self.assertEqual("b" * 40, saved["source_commit"])
            self.assertEqual("c" * 40, saved["coverage_commit"])
            self.assertEqual(
                ["wiki/c.md", "wiki/d.md"], saved["deferred_paths"]
            )

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
                    "coverage_commit": manifest["source"]["diff_base"],
                    "integrity_status": "migrated_cursor_unverified",
                },
                "comp_reviews": {},
                "unresolved_failures": [{
                    "id": state.LEGACY_SYNTHESIS_INTEGRITY_FAILURE,
                    "lane": "synthesis",
                }],
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
                self.assertEqual("verified", saved["last_successful_synthesis"]["integrity_status"])
                self.assertEqual([], saved["unresolved_failures"])

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
        self.assertEqual(
            ["bad", state.LEGACY_SYNTHESIS_INTEGRITY_FAILURE],
            [f["id"] for f in migrated["unresolved_failures"]],
        )
        self.assertEqual(
            "migrated_cursor_unverified",
            migrated["last_successful_synthesis"]["integrity_status"],
        )
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
