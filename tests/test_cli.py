import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents/skills/architect-docs-engine/scripts"
sys.path.insert(0, str(SCRIPTS))
from cli import main

class CLITests(unittest.TestCase):
    def test_help_and_inspect_commands(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--help"]), 0)
        self.assertIn("inspect", output.getvalue())
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(main(["inspect", "--project", temp, "--json"]), 0)
            self.assertIn('"files_scanned": 0', output.getvalue())

    def test_invalid_invocation_uses_exit_code_two(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            self.assertEqual(main(["inspect"]), 2)

if __name__ == "__main__":
    unittest.main()
