import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents/skills/architect-docs-engine/scripts"
sys.path.insert(0, str(SCRIPTS))
from scan_workspace import scan_workspace

class WorkspaceScanTests(unittest.TestCase):
    def test_skips_secret_files_git_and_oversized_files(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp)
            fake_assignment = "ACCESS_TOKEN=" + "fixture-secret-value-not-real"
            (root / ".git").mkdir(); (root / ".git" / "config").write_text("private")
            (root / ".env").write_text(fake_assignment)
            (root / "id_rsa").write_text("key material")
            (root / "large.txt").write_bytes(b"x" * 1_000_001)
            (root / "visible.py").write_text(fake_assignment + "\n", encoding="utf-8")
            result = scan_workspace(root)
            names = {entry["path"] for entry in result["inventory"]}
            self.assertNotIn(".git/config", names)
            self.assertNotIn(".env", names)
            self.assertNotIn("id_rsa", names)
            self.assertNotIn("large.txt", names)
            safe_entry = next(entry for entry in result["inventory"] if entry["path"] == "visible.py")
            self.assertIn("content_check", safe_entry)
            self.assertNotIn("fixture-secret-value-not-real", json.dumps(result))
            self.assertGreaterEqual(result["skipped_counts"]["sensitive"], 2)

    def test_skips_external_file_symlink(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp, tempfile.TemporaryDirectory(dir=REPO) as outside:
            root = Path(temp)
            external = Path(outside) / "external.txt"; external.write_text("outside", encoding="utf-8")
            try:
                (root / "escape.txt").symlink_to(external)
            except (OSError, NotImplementedError):
                self.skipTest("Symlink creation is unavailable in this environment")
            result = scan_workspace(root)
            self.assertNotIn("escape.txt", {entry["path"] for entry in result["inventory"]})
            self.assertEqual(result["skipped_counts"]["symlink_escape"], 1)

    def test_empty_project_and_non_ascii_filename(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp)
            self.assertEqual(scan_workspace(root)["files_scanned"], 0)
            (root / "naïve-資料.md").write_text("synthetic", encoding="utf-8")
            self.assertEqual(scan_workspace(root)["inventory"][0]["path"], "naïve-資料.md")

if __name__ == "__main__":
    unittest.main()
