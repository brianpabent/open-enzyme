from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


comp_review = load("comp_review_test", ROOT / "scripts" / "comp-review.py")
manifest = load("comp_manifest_test", ROOT / "scripts" / "comp-review-manifest.py")


class CompReviewContractTests(unittest.TestCase):
    def test_structured_verdict_keeps_lane_eligibility_separate(self):
        parsed = comp_review.parse_final(
            """COMP_VERDICT: clean_with_limitations
PROPAGATION_ELIGIBILITY: eligible_with_warning
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
REVIEWED_SNAPSHOT: manifest:abc

# Independent comp review — comp-047
"""
        )
        self.assertEqual("eligible_with_warning", parsed["PROPAGATION_ELIGIBILITY"])
        self.assertEqual("blocked", parsed["SYNTHESIS_ELIGIBILITY"])

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

    def test_comp_workflow_replaces_receipts_not_immutable_logs(self):
        text = (ROOT / ".github/workflows/comp-review.yml").read_text()
        self.assertIn("push-review.manifest", (ROOT / "scripts/comp-review.py").read_text())
        self.assertNotIn("logs/comp-reviews", text)


if __name__ == "__main__":
    unittest.main()
