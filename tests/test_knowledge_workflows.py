from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


comp_review = load("comp_review_test", ROOT / "scripts" / "comp-review.py")
manifest = load("comp_manifest_test", ROOT / "scripts" / "comp-review-manifest.py")
distributed = load("distributed_synthesis_test", ROOT / "scripts" / "distributed-synthesis.py")
normalize = load("distributed_normalize_test", ROOT / "scripts" / "synthesis_normalize.py")
hygiene = load("corpus_hygiene_test", ROOT / "scripts" / "check-corpus-hygiene.py")
lit_receipt = load("lit_scan_receipt_test", ROOT / "scripts" / "check-lit-scan-receipt.py")
invalidation = load(
    "comp_invalidation_test", ROOT / "scripts" / "check-comp-invalidation.py"
)
disposition = load(
    "comp_disposition_test", ROOT / "scripts" / "check-comp-disposition.py"
)
propagation = load(
    "sweep_propagation_test", ROOT / "scripts" / "sweep-1-propagate.py"
)


class CompReviewContractTests(unittest.TestCase):
    def test_structured_verdict_keeps_lane_eligibility_separate(self):
        parsed = comp_review.parse_final(
            """COMP_VERDICT: clean_with_limitations
REVIEWED_SNAPSHOT: abc
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: Correct stale claims only.
SYNTHESIS_ALLOWED_SCOPE: Use the bounded negative result.
FORBIDDEN_INFERENCES: efficacy; clinical readiness

# Independent comp review — comp-047
"""
        )
        self.assertEqual("eligible_with_warning", parsed["PROPAGATION_ELIGIBILITY"])
        self.assertEqual("blocked", parsed["SYNTHESIS_ELIGIBILITY"])

    def test_queue_excerpt_keeps_actions_not_full_review(self):
        review = """## Bottom-line verdict

The artifact has one blocking mismatch.

More review detail that belongs in the receipt.

## Required actions

1. Fix the mismatch.
2. Re-run the exact manifest.

## Review limits

Long review-history material.
"""
        excerpt = comp_review.queue_action_excerpt(review)
        self.assertIn("Why action remains open", excerpt)
        self.assertIn("The artifact has one blocking mismatch.", excerpt)
        self.assertIn("1. Fix the mismatch.", excerpt)
        self.assertNotIn("More review detail", excerpt)
        self.assertNotIn("Long review-history material", excerpt)

    def test_oversized_text_is_sharded_without_dropping_a_span(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            path = Path(tmp) / "large.json"
            text = "x" * (comp_review.SHARD_CHARS * 2 + 17)
            path.write_text(text)
            segments = comp_review._segments(path, "generated_output")
        self.assertEqual(3, len(segments))
        self.assertEqual(text, "".join(str(segment["content"]) for segment in segments))
        self.assertEqual((0, len(text)), (segments[0]["start"], segments[-1]["end"]))

    def test_coordinate_artifact_gets_hash_bound_deterministic_representation(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            path = Path(tmp) / "model.pdb"
            path.write_text("HEADER TEST\nATOM      1  CA  ALA A   1      1.0  2.0  3.0\n")
            segment = comp_review._segments(path, "comp_artifact")[0]
        self.assertEqual("deterministic_molecular_structure_summary", segment["representation"])
        self.assertIn("ATOM/HETATM records: 1", segment["content"])
        self.assertEqual(64, len(segment["file_sha256"]))

    def test_review_receipts_do_not_enter_authoring_or_push_manifest(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            comp = Path(tmp) / "comp-999-test"
            (comp / "outputs").mkdir(parents=True)
            (comp / "reviews").mkdir()
            (comp / "run.py").write_text("print('ok')\n")
            (comp / "outputs" / "summary.json").write_text("{}\n")
            (comp / "reviews" / "push-review.md").write_text("old receipt\n")
            design, outputs = manifest.comp_files(comp)
        self.assertEqual(["run.py"], [path.name for path in design])
        self.assertEqual(["summary.json"], [path.name for path in outputs])

    def test_authoring_manifest_binds_transitive_shared_decision_code(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            base = Path(tmp)
            comp = base / "comp-999-test"
            shared = base / "lib"
            comp.mkdir()
            shared.mkdir()
            (comp / "analyze.py").write_text(
                "from scoring_model import score\nprint(score())\n"
            )
            (shared / "scoring_model.py").write_text(
                "from scoring_helper import value\n"
                "def score():\n"
                "    return value()\n"
            )
            (shared / "scoring_helper.py").write_text(
                "def value():\n"
                "    return 1\n"
            )
            dependencies = manifest.shared_dependencies(comp)
        self.assertEqual(
            ["scoring_helper.py", "scoring_model.py"],
            [path.name for path in dependencies],
        )

    def test_git_snapshot_dependency_closure_finds_current_shared_importer(self):
        comp_path = (
            "wiki/etc/experiments/"
            "comp-038-tier-2-butyrate-assay-audit"
        )
        dependencies = manifest.shared_dependency_paths_at_revision(
            comp_path,
            "HEAD",
        )
        self.assertIn(
            "wiki/etc/experiments/lib/agentic_lit_synthesis.py",
            dependencies,
        )

    def test_push_review_shards_inspect_manifest_bound_shared_dependency(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            base = Path(tmp)
            comp = base / "comp-999-test"
            comp.mkdir()
            dependency = base / "shared_model.py"
            dependency.write_text("def score():\n    return 1\n")
            manifest_path = base / "push-manifest.json"
            manifest_path.write_text(json.dumps({
                "files": [
                    {
                        "path": dependency.relative_to(ROOT).as_posix(),
                        "kind": "shared_dependency",
                    }
                ]
            }))
            shards, binary = comp_review.build_shards(
                comp.relative_to(ROOT).as_posix(),
                "comp-999",
                manifest_path,
            )
        roles = [
            segment["role"]
            for shard in shards
            for segment in shard["segments"]
        ]
        self.assertEqual([], binary)
        self.assertEqual(["shared_dependency"], roles)

    def test_authoring_manifest_excludes_gitignored_local_cache(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            comp = Path(tmp) / "comp-999-test"
            (comp / "outputs").mkdir(parents=True)
            (comp / ".gitignore").write_text("outputs/local-cache.json\n")
            (comp / "run.py").write_text("print('ok')\n")
            (comp / "outputs" / "summary.json").write_text("{}\n")
            (comp / "outputs" / "local-cache.json").write_text('{"local": true}\n')
            design, outputs = manifest.comp_files(comp)
        self.assertEqual([".gitignore", "run.py"], [path.name for path in design])
        self.assertEqual(["summary.json"], [path.name for path in outputs])

    def test_quarantine_supersedes_historical_authoring_binding(self):
        comp = (
            ROOT
            / "wiki/etc/experiments/comp-020-upstream-complement-verification-rerun"
        )
        result = comp_review.verify_authoring_gates(comp)
        self.assertEqual("quarantined", result["status"])
        self.assertTrue(result["valid"])
        self.assertIn("historical authoring receipts", result["details"][0])

    def test_push_manifest_is_limited_to_git_tracked_artifacts(self):
        source = (ROOT / "scripts/comp-review-manifest.py").read_text()
        self.assertIn('tracked_only = args.phase == "push"', source)
        self.assertIn('["git", "ls-files", "--", relative(comp_dir)]', source)
        self.assertIn('and "reviews" not in rel.parts', source)
        self.assertIn('"shared_dependency"', source)

    def test_reader_contract_has_deterministic_residue_guards(self):
        patterns = hygiene.READER_RESIDUE_PATTERNS
        self.assertRegex("Why this page exists", patterns["wiki-discovery narration"])
        self.assertRegex(
            "Not producible in engineered yeast or koji",
            patterns["default chassis disqualification"],
        )
        self.assertRegex(
            "For Brian as of 2026-05-08",
            patterns["personalized stack protocol"],
        )
        self.assertRegex("like sourdough", patterns["invented sourdough premise"])
        self.assertRegex("the canonical protocol", patterns["wiki-discovery narration"])
        self.assertRegex(
            "the wiki currently attributes",
            patterns["wiki-discovery narration"],
        )
        self.assertRegex(
            "## Limitations of this page",
            patterns["wiki-discovery narration"],
        )
        self.assertRegex(
            "(added 2026-05-08)",
            patterns["editorial timestamp"],
        )
        self.assertRegex(
            "Where duckweed beats koji",
            patterns["track framed as another track's foil"],
        )
        self.assertRegex(
            "Duckweed aquatic-sibling chassis to koji",
            patterns["track framed as another track's foil"],
        )
        self.assertRegex(
            "## What goes on this track vs. the koji track",
            patterns["track framed as another track's foil"],
        )
        self.assertRegex(
            "## Comparison with the koji chassis",
            patterns["track framed as another track's foil"],
        )
        self.assertRegex(
            "## Comparison with sister exploration vectors",
            patterns["track framed as another track's foil"],
        )
        self.assertRegex(
            "| Use case | Winner | Why |",
            patterns["winner table on a focused page"],
        )

    def test_synthesis_ignores_editorial_history_and_chassis_defaulting(self):
        source = (ROOT / "scripts/distributed-synthesis.py").read_text()
        self.assertIn("Do not emit authoring history", source)
        self.assertIn("Do not rank an intervention by fit", source)

    def test_index_catalog_has_a_concise_entry_budget(self):
        self.assertLessEqual(hygiene.INDEX_ENTRY_MAX_CHARS, 420)

    def test_every_authoring_path_carries_page_ownership(self):
        files_and_phrases = {
            "skills/walk-synthesis/SKILL.md": "the queue item as an action brief",
            "skills/new-comp-experiment/SKILL.md": "Reader-facing outputs follow the same ownership contract",
            "scripts/sweep-prompt-1-propagate.md": "Preserve page ownership",
            "scripts/comp-pre-run-review-prompt.md": "Downstream authoring plan",
            "scripts/comp-review-prompt.md": "Reader-facing ownership",
            "synthesis/README.md": "never ready-to-paste reader prose",
        }
        for relative, phrase in files_and_phrases.items():
            with self.subTest(path=relative):
                self.assertIn(phrase, (ROOT / relative).read_text())

    def test_lit_scan_keeps_method_receipt_outside_scientific_corpus(self):
        skill = (ROOT / "skills/lit-scan/SKILL.md").read_text()
        synthesis = (ROOT / "scripts/distributed-synthesis.py").read_text()
        self.assertIn("logs/lit-scans/<scope>-<date>.json", skill)
        self.assertIn("must not duplicate the findings narrative", skill)
        self.assertNotIn('(ROOT / "logs").glob', synthesis)

    def test_lit_scan_receipt_validates_method_and_rejects_narrative(self):
        receipt = {
            "schema_version": 1,
            "scan_id": "test-2026-07-17",
            "question": "What does the evidence show?",
            "started_at": "2026-07-17T12:00:00Z",
            "completed_at": "2026-07-17T13:00:00Z",
            "canonical_updates": ["wiki/example.md"],
            "query_attempts": [{
                "source": "PubMed", "language": "en", "frame": "mechanism",
                "query": "gout mechanism", "status": "success",
                "result_count": 3, "error": None,
            }],
            "source_ids_considered": ["PMID:123"],
            "translation_checks": [],
            "load_bearing_verifications": [],
            "limitations": [],
            "errors": [],
            "workspace": {"path": "operations/test-2026-07-17", "cleaned": True},
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "receipt.json"
            path.write_text(json.dumps(receipt))
            self.assertEqual([], lit_receipt.validate(path))
            receipt["findings"] = "Duplicated scientific conclusion."
            receipt["workspace"]["cleaned"] = False
            path.write_text(json.dumps(receipt))
            errors = lit_receipt.validate(path)
        self.assertTrue(any("scientific narrative belongs in wiki" in error for error in errors))
        self.assertTrue(any("workspace.cleaned must be true" in error for error in errors))

    def test_lit_scan_receipt_allows_no_wiki_update_for_closed_lead(self):
        receipt = {
            "schema_version": 1,
            "scan_id": "closed-lead-2026-07-26",
            "question": "Does the candidate signal survive controlled evidence?",
            "started_at": "2026-07-26T12:00:00Z",
            "completed_at": "2026-07-26T13:00:00Z",
            "canonical_updates": [],
            "query_attempts": [{
                "source": "PubMed", "language": "en", "frame": "safety signal",
                "query": "candidate AND safety", "status": "success",
                "result_count": 0, "error": None,
            }],
            "source_ids_considered": [],
            "translation_checks": [],
            "load_bearing_verifications": [],
            "limitations": [],
            "errors": [],
            "workspace": {"path": "operations/closed-lead-2026-07-26", "cleaned": True},
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "receipt.json"
            path.write_text(json.dumps(receipt))
            self.assertEqual([], lit_receipt.validate(path))
            receipt["canonical_updates"] = ["synthesis/queue/example.md"]
            path.write_text(json.dumps(receipt))
            errors = lit_receipt.validate(path)
        self.assertTrue(any("must be a list of wiki/ paths" in error for error in errors))


class WorkflowTriggerTests(unittest.TestCase):
    def test_propagation_nudges_truncated_no_tool_turn_to_explicit_done(self):
        responses = iter([
            {
                "choices": [{
                    "finish_reason": "length",
                    "message": {"content": "Incomplete internal analysis"},
                }],
                "usage": {
                    "prompt_tokens": 100,
                    "completion_tokens": 4000,
                    "cost": 0.01,
                },
            },
            {
                "choices": [{
                    "finish_reason": "tool_calls",
                    "message": {
                        "content": None,
                        "tool_calls": [{
                            "id": "done-1",
                            "function": {
                                "name": "done",
                                "arguments": json.dumps({"summary": "No propagation needed."}),
                            },
                        }],
                    },
                }],
                "usage": {
                    "prompt_tokens": 200,
                    "completion_tokens": 20,
                    "cost": 0.01,
                },
            },
        ])
        original = propagation.call_openrouter
        propagation.call_openrouter = lambda *_args, **_kwargs: next(responses)
        try:
            result = propagation.run_agentic_loop(
                "key",
                "deepseek/deepseek-v4-pro",
                "system",
                "user",
                max_iterations=3,
                max_cost_usd=1.50,
            )
        finally:
            propagation.call_openrouter = original
        self.assertTrue(result["completed"])
        self.assertEqual(2, result["iterations"])
        self.assertEqual("No propagation needed.", result["done_summary"])

    def test_full_synthesis_has_no_push_trigger(self):
        text = (ROOT / ".github/workflows/wiki-sweep.yml").read_text()
        on_block = text.split("on:\n", 1)[1].split("\n# Never run", 1)[0]
        self.assertIn("workflow_dispatch:", on_block)
        self.assertNotIn("push:", on_block)

    def test_push_coordinator_orders_review_before_propagation(self):
        text = (ROOT / ".github/workflows/knowledge-update.yml").read_text()
        propagate = text.split("  propagate:\n", 1)[1]
        self.assertIn("needs: [gate, comp-review]", propagate)
        self.assertIn("uses: ./.github/workflows/wiki-propagate.yml", propagate)

    def test_propagation_cost_limit_is_a_runaway_guardrail(self):
        workflow = (ROOT / ".github/workflows/wiki-propagate.yml").read_text()
        self.assertIn("Emergency runaway cap", workflow)
        self.assertIn("default: '5.00'", workflow)
        self.assertIn("inputs.max_cost_usd || '5.00'", workflow)

    def test_comp_review_fails_closed_before_model_calls(self):
        workflow = (ROOT / ".github/workflows/comp-review.yml").read_text()
        classify = workflow.index(
            "Fail closed and remove non-result artifacts from review scope"
        )
        commit = workflow.index(
            "Commit fail-closed eligibility before any model call"
        )
        preflight = workflow.index("Complete-review cost preflight")
        review = workflow.index(
            "Review every selected artifact and update current eligibility"
        )
        self.assertLess(classify, commit)
        self.assertLess(commit, preflight)
        self.assertLess(preflight, review)
        self.assertIn("comp-review-deferred.txt", workflow)
        self.assertIn('git add -A -- "$comp_dir"', workflow[commit:preflight])

    def test_local_and_generated_updates_fail_closed_on_reader_contract(self):
        hook = (ROOT / ".githooks/pre-push").read_text()
        propagation = (ROOT / ".github/workflows/wiki-propagate.yml").read_text()
        propagation_driver = (ROOT / "scripts/sweep-1-propagate.py").read_text()
        integrity = (ROOT / ".github/workflows/corpus-integrity.yml").read_text()
        self.assertIn("check-corpus-hygiene.py", hook)
        self.assertIn("check-lit-scan-receipt.py", hook)
        self.assertIn("Verify propagated reader contract", propagation)
        self.assertIn("check-corpus-hygiene.py", propagation)
        self.assertLess(
            propagation.index('git config user.name "github-actions[bot]"'),
            propagation.index("python3 scripts/sweep-1-propagate.py"),
        )
        self.assertIn(
            "Propagation model did not call done(); refusing to commit partial",
            propagation_driver,
        )
        self.assertIn('"wiki/etc/experiments/**"', propagation_driver)
        self.assertIn(
            "COMP artifacts are immutable propagation inputs",
            (ROOT / "scripts/sweep-prompt-1-propagate.md").read_text(),
        )
        self.assertIn("check-lit-scan-receipt.py", integrity)

    def test_warning_lanes_carry_binding_scope(self):
        propagation = (ROOT / "scripts/sweep-prompt-1-propagate.md").read_text()
        synthesis = (ROOT / "scripts/distributed-synthesis.py").read_text()
        self.assertIn("propagation_allowed_scope", propagation)
        self.assertIn("forbidden_inferences", propagation)
        self.assertIn("synthesis_allowed_scope", synthesis)
        self.assertIn("forbidden_inferences", synthesis)

    def test_comp_workflow_replaces_receipts_not_immutable_logs(self):
        text = (ROOT / ".github/workflows/comp-review.yml").read_text()
        self.assertIn("push-review.manifest", (ROOT / "scripts/comp-review.py").read_text())
        self.assertNotIn("logs/comp-reviews", text)

    def test_disposition_governance_runs_locally_and_in_ci(self):
        hook = (ROOT / ".githooks/pre-push").read_text()
        integrity = (ROOT / ".github/workflows/corpus-integrity.yml").read_text()
        self.assertIn("check-comp-disposition.py --all --base", hook)
        self.assertIn("Check COMP quarantine and retirement governance", integrity)

    def test_completed_review_baseline_preserves_real_provenance(self):
        state = json.loads((ROOT / "logs/sweep-state.json").read_text())
        records = state["comp_reviews"]
        comp_root = ROOT / "wiki" / "etc" / "experiments"
        completed_active: set[str] = set()
        pre_run_only: set[str] = set()
        tombstones: set[str] = set()
        quarantines: set[str] = set()
        for comp_dir in comp_root.glob("comp-*"):
            identifier = comp_dir.name[:8]
            reviews = comp_dir / "reviews"
            if (comp_dir / "quarantine.json").is_file():
                quarantines.add(identifier)
                self.assertEqual([], disposition.validate_quarantine(comp_dir))
                self.assertFalse(any(reviews.glob("push-review*")))
                continue
            if (comp_dir / "invalidation.json").is_file():
                tombstones.add(identifier)
                self.assertEqual([], invalidation.validate(comp_dir))
                self.assertFalse(any(reviews.glob("push-review*")))
                continue
            if (
                (reviews / "pre-run.manifest.json").is_file()
                and (reviews / "pre-run.md").is_file()
                and not (reviews / "post-run.manifest.json").exists()
                and not (reviews / "post-run.md").exists()
            ):
                pre_run_only.add(identifier)
                self.assertFalse(any(reviews.glob("push-review*")))
                continue
            completed_active.add(identifier)

        self.assertEqual(completed_active, set(records))
        self.assertTrue(tombstones or quarantines)
        self.assertEqual({"comp-048", "comp-049"}, pre_run_only)
        pending = []
        for identifier, record in records.items():
            if record["comp_verdict"] == "review_pending_exact_push":
                pending.append(identifier)
                self.assertEqual("blocked", record["propagation_eligibility"])
                self.assertEqual("blocked", record["synthesis_eligibility"])
                self.assertIsNone(record["artifact_manifest_sha256"])
                self.assertIsNone(record["review_receipt"])
                continue
            receipt = json.loads(
                (ROOT / record["comp_dir"] / "reviews" / "push-review.json").read_text()
            )
            self.assertEqual(
                record["artifact_manifest_sha256"],
                receipt["artifact_manifest_sha256"],
            )
            binding_mode = receipt.get("binding_mode")
            if binding_mode == "completed_review_migration":
                provenance = receipt["independent_review"]
                self.assertTrue(provenance["completed"])
                self.assertTrue(
                    provenance["review_log_git_path"].startswith("logs/comp-reviews/")
                )
                self.assertEqual(40, len(provenance["review_log_commit"]))
            elif binding_mode == "fresh_authoring_review":
                self.assertEqual("fresh_authoring_review", receipt["binding_mode"])
                authoring = receipt["authoring_review"]
                self.assertTrue(authoring["completed"])
                self.assertFalse(authoring["action_required"])
            else:
                self.assertIsNone(binding_mode)
                self.assertTrue(receipt["authoring_gates"]["valid"])
                lane = receipt["lane_adjudication"]
                self.assertEqual("exact push review", lane["method"])
                self.assertTrue(lane["new_artifact_review_performed"])
            self.assertNotEqual("legacy_review_pending", receipt["comp_verdict"])
            if receipt["action_required"]:
                self.assertIn("lane_adjudication", receipt)
        self.assertEqual([], pending)


class DistributedSynthesisContractTests(unittest.TestCase):
    def test_domain_pair_plan_is_exhaustive(self):
        import itertools

        pairs = list(itertools.combinations(distributed.DOMAINS, 2))
        self.assertEqual(28, len(pairs))
        self.assertEqual(len(pairs), len(set(pairs)))

    def test_domain_pair_preserves_up_to_three_orthogonal_candidates(self):
        prompt = distributed.bridge_prompt("urate-physiology", "strategy-methods", [], [], [])
        self.assertEqual(3, distributed.MAX_PAIR_CANDIDATES)
        self.assertIn("up to 3 non-redundant", prompt)

    def test_same_run_duplicate_headlines_are_suppressed(self):
        items = [
            {"candidate_id": "a", "type": "connection", "headline": "Substrate engineering: shared lever"},
            {"candidate_id": "b", "type": "connection", "headline": "Substrate engineering — shared lever"},
            {"candidate_id": "c", "type": "experiment", "headline": "Substrate engineering — shared lever"},
        ]
        kept, removed = distributed.deduplicate_promoted(items)
        self.assertEqual(["a", "c"], [item["candidate_id"] for item in kept])
        self.assertEqual(["b"], removed)

    def test_blocked_comp_does_not_stop_unrelated_full_corpus_synthesis(self):
        state = json.loads((ROOT / "logs/sweep-state.json").read_text())
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", dir=ROOT / "wiki", delete=False
        ) as handle:
            handle.write("comp-031 is invalidated.\n")
            trigger = Path(handle.name)
        try:
            distributed.validate_trigger_comp_eligibility(
                [trigger.relative_to(ROOT).as_posix()], state
            )
        finally:
            trigger.unlink(missing_ok=True)

    def test_proposed_comp_label_does_not_require_an_artifact_receipt(self):
        state = json.loads((ROOT / "logs/sweep-state.json").read_text())
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", dir=ROOT / "wiki", delete=False
        ) as handle:
            handle.write("comp-040 is proposed and has no artifact yet.\n")
            trigger = Path(handle.name)
        try:
            distributed.validate_trigger_comp_eligibility(
                [trigger.relative_to(ROOT).as_posix()], state
            )
        finally:
            trigger.unlink(missing_ok=True)

    def test_section_inventory_and_sharding_preserve_every_section(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            path = Path(tmp) / "source.md"
            path.write_text("# One\nalpha\n\n## Two\nbeta\n")
            sections = distributed.sections(path, max_chars=8)
            shards = distributed.pack_sections(sections, max_chars=10)
        self.assertEqual(
            {section["section_id"] for section in sections},
            {section["section_id"] for shard in shards for section in shard},
        )
        self.assertTrue(all(section["sha256"] for section in sections))

    def test_ledger_merge_preserves_dispute_and_pass_heterogeneity(self):
        base = {
            "atom_id": "a", "section_id": "s", "type": "constraint",
            "statement": "Only luminal exposure was modeled.", "excerpt": "luminal exposure",
            "domain": "delivery-chassis", "path": "wiki/x.md", "start_line": 1,
        }
        atoms = [dict(base, extraction_pass="A"), dict(base, extraction_pass="B", dispute="May also constrain systemic use")]
        merged = distributed.merge_atoms(atoms)
        self.assertEqual(1, len(merged))
        self.assertEqual(["A", "B"], merged[0]["extraction_passes"])
        self.assertEqual(["May also constrain systemic use"], merged[0]["disputes"])

    def test_coverage_receipt_fails_closed_on_missing_second_read(self):
        receipt = {
            "status": "complete", "section_count": 2,
            "pass_a_covered_sections": 2, "pass_b_covered_sections": 1,
            "domain_pairs_expected": 28, "domain_pairs_completed": 28,
            "candidate_count": 0, "rehydrated_candidate_ids": [],
            "reviewed_candidate_ids": [], "promoted_candidate_ids": [],
            "cost": {"actual_usd": 1.0, "hard_cap_usd": 5.0},
        }
        receipt["coverage_receipt_sha256"] = distributed.canonical_hash(receipt)
        with self.assertRaises(RuntimeError):
            distributed.validate_coverage_receipt(receipt)

    def test_coverage_receipt_accepts_deterministically_excluded_candidate(self):
        receipt = {
            "status": "complete",
            "section_count": 1,
            "pass_a_covered_sections": 1,
            "pass_b_covered_sections": 1,
            "domain_pairs_expected": 28,
            "domain_pairs_completed": 28,
            "candidate_count": 2,
            "rehydrated_candidate_ids": ["active"],
            "reviewed_candidate_ids": ["active"],
            "excluded_candidate_ids": ["quarantined"],
            "promoted_candidate_ids": [],
            "cost": {"actual_usd": 1.0, "hard_cap_usd": 5.0},
        }
        receipt["coverage_receipt_sha256"] = distributed.canonical_hash(receipt)
        distributed.validate_coverage_receipt(receipt)

    def test_quarantined_comp_excludes_only_its_candidate(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", dir=ROOT / "wiki", delete=False
        ) as handle:
            handle.write("comp-999 supplied the retired quantitative prior.\n")
            source = Path(handle.name)
        atom = {
            "atom_id": "a",
            "path": source.relative_to(ROOT).as_posix(),
            "start_line": 1,
            "end_line": 1,
            "excerpt": "comp-999 supplied",
            "type": "claim",
            "statement": "The artifact supplied a prior.",
        }
        original = distributed.comp_dispositions
        original_homes = distributed.comp_evidence_homes
        distributed.comp_dispositions = lambda: {"comp-999": "quarantined"}
        distributed.comp_evidence_homes = lambda: {
            "comp-999": "wiki/current-evidence.md"
        }
        try:
            with self.assertRaises(distributed.CandidateExcluded):
                distributed.exact_source_packet(
                    {"atom_ids": ["a"], "hypothesis": "artifact prior"},
                    {"a": atom},
                    {},
                )
        finally:
            distributed.comp_dispositions = original
            distributed.comp_evidence_homes = original_homes
            source.unlink(missing_ok=True)

    def test_nonactive_comp_current_evidence_home_remains_synthesizable(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", dir=ROOT / "wiki", delete=False
        ) as handle:
            handle.write(
                "comp-999 is invalid; the matched experiment remains a conjecture.\n"
            )
            source = Path(handle.name)
        relative_source = source.relative_to(ROOT).as_posix()
        atom = {
            "atom_id": "a",
            "path": relative_source,
            "start_line": 1,
            "end_line": 1,
            "excerpt": "comp-999 is invalid",
            "type": "constraint",
            "statement": "The model is invalid; the matched experiment remains.",
        }
        original = distributed.comp_dispositions
        original_homes = distributed.comp_evidence_homes
        distributed.comp_dispositions = lambda: {"comp-999": "quarantined"}
        distributed.comp_evidence_homes = lambda: {
            "comp-999": relative_source
        }
        try:
            packet = distributed.exact_source_packet(
                {"atom_ids": ["a"], "hypothesis": "matched experiment conjecture"},
                {"a": atom},
                {},
            )
            self.assertEqual("a", packet["rehydrated_sources"][0]["atom"]["atom_id"])
            self.assertEqual({}, packet["comp_support"])
        finally:
            distributed.comp_dispositions = original
            distributed.comp_evidence_homes = original_homes
            source.unlink(missing_ok=True)

    def test_contrary_evidence_is_not_silently_truncated(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", dir=ROOT / "wiki", delete=False
        ) as handle:
            handle.write("shared mechanism premise\n")
            source = Path(handle.name)
        base = {
            "path": source.relative_to(ROOT).as_posix(),
            "start_line": 1,
            "end_line": 1,
            "excerpt": "shared mechanism premise",
        }
        atoms = {
            "selected": {
                **base,
                "atom_id": "selected",
                "type": "claim",
                "statement": "shared mechanism premise",
            }
        }
        for index in range(40):
            atoms[f"c{index}"] = {
                **base,
                "atom_id": f"c{index}",
                "type": "constraint",
                "statement": f"shared mechanism constraint {index}",
            }
        try:
            packet = distributed.exact_source_packet(
                {
                    "atom_ids": ["selected"],
                    "hypothesis": "shared mechanism could connect",
                },
                atoms,
                {},
            )
        finally:
            source.unlink(missing_ok=True)
        self.assertEqual(40, packet["contrary_constraint_count"])
        self.assertEqual(40, len(packet["contrary_constraint_atoms"]))
        self.assertFalse(packet["contrary_constraint_overflow"])


class CompDispositionContractTests(unittest.TestCase):
    def test_quarantine_binds_complete_artifact_and_expires(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            comp = Path(tmp) / "comp-999-test"
            (comp / "inputs").mkdir(parents=True)
            (comp / "README.md").write_text("# Test\n")
            (comp / "analyze.py").write_text("print('historical')\n")
            (comp / "inputs" / "provenance.md").write_text("source\n")
            manifest_entries = disposition.artifact_manifest(comp)
            dependency_entries = disposition.artifact_dependencies(comp)
            document = {
                "schema_version": 1,
                "comp": "comp-999",
                "status": "quarantined",
                "runnable": False,
                "owner": "brian",
                "entered_on": "2026-07-27",
                "expires_on": "2026-08-27",
                "decision_status": "pending_re_review",
                "reason": "Bounded disposition review is pending.",
                "blocked_scope": ["all derived claims"],
                "current_evidence_home": "wiki/index.md",
                "artifact_manifest": manifest_entries,
                "artifact_dependencies": dependency_entries,
                "artifact_manifest_sha256": disposition.canonical_quarantine_sha256(
                    manifest_entries,
                    dependency_entries,
                ),
            }
            (comp / "quarantine.json").write_text(json.dumps(document))
            self.assertEqual(
                [],
                disposition.validate_quarantine(
                    comp,
                    today=disposition.dt.date(2026, 7, 28),
                ),
            )
            (comp / "analyze.py").write_text("print('changed')\n")
            errors = disposition.validate_quarantine(
                comp,
                today=disposition.dt.date(2026, 7, 28),
            )
            self.assertTrue(any("artifact_manifest" in error for error in errors))
            expiry_errors = disposition.validate_quarantine(
                comp,
                today=disposition.dt.date(2026, 8, 28),
            )
            self.assertTrue(any("expired" in error for error in expiry_errors))

    def test_quarantine_binds_imported_shared_library(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            base = Path(tmp)
            comp = base / "comp-999-test"
            shared = base / "lib"
            comp.mkdir()
            shared.mkdir()
            (comp / "README.md").write_text("# Test\n")
            (comp / "analyze.py").write_text(
                "from scoring_model import score\nprint(score())\n"
            )
            (shared / "scoring_model.py").write_text(
                "from scoring_helper import value\n"
                "def score():\n"
                "    return value()\n"
            )
            (shared / "scoring_helper.py").write_text(
                "def value():\n    return 1\n"
            )
            manifest_entries = disposition.artifact_manifest(comp)
            dependency_entries = disposition.artifact_dependencies(comp)
            self.assertEqual(
                [
                    (shared / "scoring_helper.py").relative_to(ROOT).as_posix(),
                    (shared / "scoring_model.py").relative_to(ROOT).as_posix(),
                ],
                [entry["path"] for entry in dependency_entries],
            )
            document = {
                "schema_version": 1,
                "comp": "comp-999",
                "status": "quarantined",
                "runnable": False,
                "owner": "brian",
                "entered_on": "2026-07-27",
                "expires_on": "2026-08-27",
                "decision_status": "pending_re_review",
                "reason": "Bounded disposition review is pending.",
                "blocked_scope": ["all derived claims"],
                "current_evidence_home": "wiki/index.md",
                "artifact_manifest": manifest_entries,
                "artifact_dependencies": dependency_entries,
                "artifact_manifest_sha256": disposition.canonical_quarantine_sha256(
                    manifest_entries,
                    dependency_entries,
                ),
            }
            (comp / "quarantine.json").write_text(json.dumps(document))
            self.assertEqual(
                [],
                disposition.validate_quarantine(
                    comp,
                    today=disposition.dt.date(2026, 7, 28),
                ),
            )
            (shared / "scoring_model.py").write_text(
                "def score():\n    return 2\n"
            )
            errors = disposition.validate_quarantine(
                comp,
                today=disposition.dt.date(2026, 7, 28),
            )
            self.assertTrue(any("artifact_dependencies" in error for error in errors))

    def test_final_disposition_pending_requires_bound_review(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            comp = Path(tmp) / "comp-999-test"
            reviews = comp / "reviews"
            reviews.mkdir(parents=True)
            (comp / "README.md").write_text("# Test\n")
            (comp / "analyze.py").write_text("print('historical')\n")
            manifest_entries = disposition.artifact_manifest(comp)
            dependency_entries = disposition.artifact_dependencies(comp)
            manifest_sha = disposition.canonical_quarantine_sha256(
                manifest_entries,
                dependency_entries,
            )
            review = reviews / "disposition-review.md"
            review.write_text(
                f"ARTIFACT_MANIFEST_SHA256: {manifest_sha}\n"
                "DISPOSITION_REVIEW: RETIREMENT_JUSTIFIED\n"
            )
            document = {
                "schema_version": 1,
                "comp": "comp-999",
                "status": "quarantined",
                "runnable": False,
                "owner": "brian",
                "entered_on": "2026-07-27",
                "expires_on": "2026-08-27",
                "decision_status": "final_disposition_pending",
                "reason": "Independent review completed; final decision pending.",
                "blocked_scope": ["all derived claims"],
                "current_evidence_home": "wiki/index.md",
                "artifact_manifest": manifest_entries,
                "artifact_dependencies": dependency_entries,
                "artifact_manifest_sha256": manifest_sha,
            }
            marker = comp / "quarantine.json"
            marker.write_text(json.dumps(document))
            errors = disposition.validate_quarantine(
                comp,
                today=disposition.dt.date(2026, 7, 28),
            )
            self.assertTrue(any("requires a bound" in error for error in errors))
            document["disposition_review"] = {
                "path": review.relative_to(ROOT).as_posix(),
                "sha256": disposition.sha256(review),
            }
            marker.write_text(json.dumps(document))
            self.assertEqual(
                [],
                disposition.validate_quarantine(
                    comp,
                    today=disposition.dt.date(2026, 7, 28),
                ),
            )

    def test_new_retirement_requires_schema_two_governance(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            comp = Path(tmp) / "comp-999-test"
            comp.mkdir()
            (comp / "invalidation.json").write_text(json.dumps({
                "schema_version": 2,
                "comp": "comp-999",
                "status": "invalidated_tombstone",
                "runnable": False,
                "invalidated_scope": ["all categorical rankings"],
                "surviving_scope": {
                    "kind": "bounded_question",
                    "questions": ["Does the direct assay support the mechanism?"],
                },
                "current_evidence_home": "wiki/index.md",
            }))
            errors = disposition.validate_invalidation_governance(comp)
        self.assertTrue(any("decision_owner" in error for error in errors))
        self.assertTrue(any("disposition_review" in error for error in errors))
        self.assertTrue(any("unique_detail_audit" in error for error in errors))
        self.assertTrue(any("closed dependency cascade" in error for error in errors))

    def test_retirement_batch_is_capped_and_cascade_blocked(self):
        paths = [ROOT / f"comp-{index:03d}/invalidation.json" for index in range(4)]
        errors = disposition.validate_retirement_batch_paths(paths, [])
        self.assertTrue(any("maximum is 3" in error for error in errors))
        errors = disposition.validate_retirement_batch_paths(
            paths[:1],
            [ROOT / "synthesis/queue/comp-retirement-cascade-001.md"],
        )
        self.assertTrue(any("open cascade" in error for error in errors))

    def test_promoted_markdown_normalizes_without_narrative_history(self):
        manifest = {"coverage_commit": "a" * 40}
        raw, reviews = distributed.raw_markdown(
            [{
                "candidate_id": "c1", "type": "connection", "headline": "A grounded bridge",
                "body": "Mechanistic extrapolation grounded in `wiki/example.md`.",
                "status": "partial", "review": "Source support is bounded.",
                "cheapest_next_step": "Run the discriminating assay.",
            }],
            manifest, "b" * 40, ["wiki/example.md"], "deepseek/deepseek-v4-pro",
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "distributed.md"
            path.write_text(raw)
            normalized = normalize.normalize_text(raw, path)
        self.assertEqual("items", normalized["status"])
        self.assertEqual(1, len(normalized["items"]))
        self.assertIn("Pass 3 review", reviews)


if __name__ == "__main__":
    unittest.main()
