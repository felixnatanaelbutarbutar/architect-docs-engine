import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents/skills/architect-docs-engine/scripts"
sys.path.insert(0, str(SCRIPTS))
from install import install

class SafePathTests(unittest.TestCase):
    def test_installer_refuses_populated_destination_by_default(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            target = Path(temp) / "target"; target.mkdir()
            destination = target / ".agents/skills/architect-docs-engine"
            destination.mkdir(parents=True); (destination / "manual.txt").write_text("preserve me")
            with self.assertRaises(FileExistsError):
                install("workspace", str(target))
            self.assertEqual((destination / "manual.txt").read_text(), "preserve me")

    def test_workspace_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp, tempfile.TemporaryDirectory(dir=REPO) as outside:
            target = Path(temp) / "target"; target.mkdir()
            try:
                (target / ".agents").symlink_to(Path(outside), target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Symlink creation is unavailable in this environment")
            with self.assertRaises(ValueError):
                install("workspace", str(target), dry_run=True)

    def test_force_backs_up_existing_install_before_replacement(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            target = Path(temp) / "target"; target.mkdir()
            destination = target / ".agents/skills/architect-docs-engine"
            destination.mkdir(parents=True); (destination / "manual.txt").write_text("keep in backup", encoding="utf-8")
            installed, backup = install("workspace", str(target), force=True)
            self.assertTrue((Path(installed) / "SKILL.md").is_file())
            self.assertTrue((Path(backup) / "manual.txt").is_file())
            self.assertEqual((Path(backup) / "manual.txt").read_text(encoding="utf-8"), "keep in backup")

if __name__ == "__main__":
    unittest.main()
