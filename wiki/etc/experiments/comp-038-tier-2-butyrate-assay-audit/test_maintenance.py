from __future__ import annotations

import hashlib
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import ExitStack, redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock


SCRIPT_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("comp038_analyze_test", SCRIPT_DIR / "analyze.py")
ANALYZE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(ANALYZE)


def file_hashes(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class MaintenanceGuardTests(unittest.TestCase):
    def invoke(self, args: list[str], output_dir: Path) -> tuple[int, str, str, list[mock.Mock]]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        guarded_names = (
            "load_root_dotenv",
            "fetch_pubmed_snapshot",
            "write_json",
            "write_codex_packet",
            "write_summary",
            "OpenRouterClient",
        )
        guarded: list[mock.Mock] = []
        with ExitStack() as stack:
            stack.enter_context(mock.patch.object(ANALYZE, "OUTPUTS", output_dir))
            stack.enter_context(mock.patch.object(sys, "argv", ["analyze.py", *args]))
            for name in guarded_names:
                guarded.append(stack.enter_context(mock.patch.object(ANALYZE, name)))
            with redirect_stdout(stdout), redirect_stderr(stderr):
                try:
                    ANALYZE.main()
                    code = 0
                except SystemExit as exc:
                    code = int(exc.code)
        return code, stdout.getvalue(), stderr.getvalue(), guarded

    def assert_guarded_paths_unused(self, guarded: list[mock.Mock]) -> None:
        for item in guarded:
            self.assertFalse(item.called)

    def test_default_success_is_read_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "outputs"
            outputs.mkdir()
            for name in ANALYZE.CURRENT_OUTPUT_NAMES:
                (outputs / name).write_text(f"{name}\n")
            before = file_hashes(outputs)
            code, stdout, _stderr, guarded = self.invoke([], outputs)
            after = file_hashes(outputs)
        self.assertEqual(0, code)
        self.assertIn("Required-file check passed", stdout)
        self.assertEqual(before, after)
        self.assert_guarded_paths_unused(guarded)

    def test_absent_output_directory_is_not_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "absent" / "outputs"
            code, _stdout, _stderr, guarded = self.invoke([], outputs)
            self.assertFalse(outputs.exists())
        self.assertEqual(1, code)
        self.assert_guarded_paths_unused(guarded)

    def test_missing_verification_fails_without_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "outputs"
            outputs.mkdir()
            for name in ANALYZE.CURRENT_OUTPUT_NAMES:
                if name != "primary-source-verification-2026-07-24.json":
                    (outputs / name).write_text(f"{name}\n")
            before = file_hashes(outputs)
            code, stdout, _stderr, guarded = self.invoke([], outputs)
            after = file_hashes(outputs)
        self.assertEqual(1, code)
        self.assertIn("primary-source-verification-2026-07-24.json", stdout)
        self.assertEqual(before, after)
        self.assert_guarded_paths_unused(guarded)

    def test_directory_shaped_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "outputs"
            outputs.mkdir()
            for name in ANALYZE.CURRENT_OUTPUT_NAMES:
                path = outputs / name
                if name == "results.json":
                    path.mkdir()
                else:
                    path.write_text(f"{name}\n")
            code, stdout, _stderr, guarded = self.invoke([], outputs)
        self.assertEqual(1, code)
        self.assertIn("results.json", stdout)
        self.assert_guarded_paths_unused(guarded)

    def test_mutation_modes_require_explicit_authorization(self):
        with tempfile.TemporaryDirectory() as tmp:
            for mode in ("--prepare-codex", "--run-openrouter"):
                with self.subTest(mode=mode):
                    outputs = Path(tmp) / mode.removeprefix("-")
                    code, _stdout, stderr, guarded = self.invoke([mode], outputs)
                    self.assertEqual(2, code)
                    self.assertIn("--regenerate-current-outputs", stderr)
                    self.assertFalse(outputs.exists())
                    self.assert_guarded_paths_unused(guarded)

    def test_authorization_requires_a_mutation_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "outputs"
            code, _stdout, stderr, guarded = self.invoke(
                ["--regenerate-current-outputs"], outputs
            )
            self.assertFalse(outputs.exists())
        self.assertEqual(2, code)
        self.assertIn("requires either --prepare-codex", stderr)
        self.assert_guarded_paths_unused(guarded)

    def test_mutation_modes_are_mutually_exclusive(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = Path(tmp) / "outputs"
            code, _stdout, stderr, guarded = self.invoke(
                ["--prepare-codex", "--run-openrouter"], outputs
            )
            self.assertFalse(outputs.exists())
        self.assertEqual(2, code)
        self.assertIn("not allowed with argument", stderr)
        self.assert_guarded_paths_unused(guarded)


if __name__ == "__main__":
    unittest.main()
