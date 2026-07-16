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

    def test_push_manifest_is_limited_to_git_tracked_artifacts(self):
        source = (ROOT / "scripts/comp-review-manifest.py").read_text()
        self.assertIn('tracked_only=args.phase == "push"', source)
        self.assertIn('["git", "ls-files", "--", relative(comp_dir)]', source)


class WorkflowTriggerTests(unittest.TestCase):
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

    def test_completed_review_baseline_preserves_real_provenance(self):
        state = json.loads((ROOT / "logs/sweep-state.json").read_text())
        records = state["comp_reviews"]
        self.assertEqual(40, len(records))
        self.assertEqual(
            18,
            sum(r["comp_verdict"] == "review_completed_open_actions" for r in records.values()),
        )
        self.assertEqual(
            22,
            sum(r["comp_verdict"] == "review_completed_actioned" for r in records.values()),
        )
        open_records = [
            r for r in records.values()
            if r["comp_verdict"] == "review_completed_open_actions"
        ]
        self.assertEqual(
            {"eligible_with_warning"},
            {r["propagation_eligibility"] for r in open_records},
        )
        self.assertEqual(
            1,
            sum(r["synthesis_eligibility"] == "blocked" for r in open_records),
        )
        for record in records.values():
            receipt = json.loads(
                (ROOT / record["comp_dir"] / "reviews" / "push-review.json").read_text()
            )
            provenance = receipt["independent_review"]
            self.assertTrue(provenance["completed"])
            self.assertTrue(provenance["review_log_git_path"].startswith("logs/comp-reviews/"))
            self.assertEqual(40, len(provenance["review_log_commit"]))
            self.assertEqual("completed_review_migration", receipt["binding_mode"])
            self.assertNotEqual("legacy_review_pending", receipt["comp_verdict"])
            if receipt["action_required"]:
                self.assertIn("lane_adjudication", receipt)


class DistributedSynthesisContractTests(unittest.TestCase):
    def test_domain_pair_plan_is_exhaustive(self):
        import itertools

        pairs = list(itertools.combinations(distributed.DOMAINS, 2))
        self.assertEqual(28, len(pairs))
        self.assertEqual(len(pairs), len(set(pairs)))

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
