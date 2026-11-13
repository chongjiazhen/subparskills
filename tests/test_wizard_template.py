from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WizardPromptTests(unittest.TestCase):
    def run_library(self, directory, script, *, input="", extra_env=None):
        bash = shutil.which("bash")
        self.assertIsNotNone(bash, "These behavioral tests require real Bash on PATH")
        template = (ROOT / "skills" / "wizard" / "template.sh").read_text(
            encoding="utf-8"
        )
        library, marker, _ = template.partition("# STAGES:")
        self.assertTrue(marker, "Library boundary missing; do not run example stages")
        environment = os.environ.copy()
        for name in ("BASH_ENV", "ENV"):
            environment.pop(name, None)
        environment["ENV_FILE"] = ".env"
        environment.update(extra_env or {})
        result = subprocess.run(
            [bash, "--noprofile", "--norc", "-c", library + "\n" + script],
            cwd=directory, env=environment, input=input.encode("utf-8"),
            capture_output=True, timeout=10,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        return result.stdout.decode("utf-8")

    def test_prompts_fail_on_empty_eof_even_with_saved_default(self) -> None:
        for prompt in ("ask", "ask_secret"):
            for saved_default in (False, True):
                with self.subTest(prompt=prompt, saved_default=saved_default):
                    with tempfile.TemporaryDirectory(prefix="wizard-eof-") as directory:
                        (Path(directory) / ".env").write_text(
                            "WIZARD_TEST_VALUE=synthetic-default\n" if saved_default else "",
                            encoding="utf-8",
                        )
                        output = self.run_library(directory, f'''
if {prompt} WIZARD_TEST_VALUE "Synthetic prompt:"; then
    prompt_status=0
else
    prompt_status=$?
fi
printf '\\nPROMPT_STATUS=%s\\n' "$prompt_status"
''')
                        status_line = output.splitlines()[-1]
                        self.assertTrue(status_line.startswith("PROMPT_STATUS="), output)
                        self.assertNotEqual(
                            0, int(status_line.partition("=")[2]),
                            f"{prompt} accepted empty EOF (saved_default={saved_default})",
                        )

    def test_prompts_preserve_enter_default_and_supplied_values(self) -> None:
        for prompt in ("ask", "ask_secret"):
            for entered, expected in (("\n", "synthetic-default"),
                                      ("  synthetic\\value  \n", "  synthetic\\value  "),
                                      ("synthetic-no-newline", "synthetic-no-newline")):
                with self.subTest(prompt=prompt, entered=entered):
                    with tempfile.TemporaryDirectory(prefix="wizard-input-") as directory:
                        (Path(directory) / ".env").write_text(
                            "WIZARD_TEST_VALUE=synthetic-default\n", encoding="utf-8", newline="\n"
                        )
                        output = self.run_library(directory, f'''
{prompt} WIZARD_TEST_VALUE "Synthetic prompt:"
printf '\\nVALUE=<%s>\\n' "$WIZARD_TEST_VALUE"
''', input=entered)
                        self.assertEqual(f"VALUE=<{expected}>", output.splitlines()[-1])

    def test_values_round_trip_through_bash_source_and_existing_without_evaluation(self):
        value = "  synthetic # $HOME O'Brien \\path $(touch evaluated) `touch evaluated`  "
        with tempfile.TemporaryDirectory(prefix="wizard-quote-") as directory:
            output = self.run_library(directory, '''
write_env WIZARD_TEST_VALUE "$SYNTHETIC_VALUE"
printf 'EXISTING=<%s>\\n' "$(_existing WIZARD_TEST_VALUE)"
source "$ENV_FILE"
printf 'SOURCED=<%s>\\n' "$WIZARD_TEST_VALUE"
''', extra_env={"SYNTHETIC_VALUE": value})
            self.assertIn(f"EXISTING=<{value}>\n", output)
            self.assertIn(f"SOURCED=<{value}>\n", output)
            self.assertFalse((Path(directory) / "evaluated").exists())
            # Reading an unquoted legacy value must not execute shell syntax either.
            (Path(directory) / ".env").write_text(
                "WIZARD_TEST_VALUE=$(touch evaluated)\n", encoding="utf-8", newline="\n"
            )
            output = self.run_library(directory, '_existing WIZARD_TEST_VALUE')
            self.assertEqual("$(touch evaluated)", output)
            self.assertFalse((Path(directory) / "evaluated").exists())

    @unittest.skipIf(os.name == "nt", "POSIX symlink and mode contract requires Linux filesystem")
    def test_write_preserves_symlink_target_and_existing_mode(self):
        with tempfile.TemporaryDirectory(prefix="wizard-preserve-") as directory:
            root = Path(directory)
            target = root / "target.env"
            target.write_text("OTHER=keep\nWIZARD_TEST_VALUE=old\n", encoding="utf-8")
            target.chmod(0o640)
            link = root / ".env"
            link.symlink_to(target.name)
            self.run_library(directory, 'write_env WIZARD_TEST_VALUE synthetic-new')
            self.assertTrue(link.is_symlink(), "write_env replaced the symlink")
            self.assertEqual(target.name, os.readlink(link))
            self.assertEqual(0o640, target.stat().st_mode & 0o777)
            self.assertEqual("OTHER=keep\nWIZARD_TEST_VALUE='synthetic-new'\n",
                             target.read_text(encoding="utf-8"))

    @unittest.skipIf(os.name == "nt", "POSIX mode contract requires Linux filesystem")
    def test_new_env_file_is_private_under_permissive_umask(self):
        with tempfile.TemporaryDirectory(prefix="wizard-private-") as directory:
            self.run_library(directory, 'umask 000; write_env WIZARD_TEST_VALUE synthetic')
            self.assertEqual(0o600, (Path(directory) / ".env").stat().st_mode & 0o777)

    def test_missing_browser_opener_warns_visibly(self):
        with tempfile.TemporaryDirectory(prefix="wizard-browser-") as directory:
            output = self.run_library(directory, '''
PATH="$PWD/empty-path"
open_url 'https://example.invalid/synthetic'
''')
            self.assertIn("couldn't open a browser", output)
            self.assertIn("visit it manually: https://example.invalid/synthetic", output)
            self.assertEqual([], list(Path(directory).iterdir()))


if __name__ == "__main__":
    unittest.main()
