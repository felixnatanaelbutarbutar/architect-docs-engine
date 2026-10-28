import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents" / "skills" / "architect-docs-engine" / "scripts"
sys.path.insert(0, str(SCRIPTS))
from install import install
from validate_skill import validate_skill

class SkillManifestTests(unittest.TestCase):
    def test_skill_resources_and_frontmatter_are_valid(self):
        self.assertTrue(validate_skill()["ok"])

    def test_installer_copies_skill_and_is_idempotent(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            target = Path(temp) / "target"
            target.mkdir()
            dest, backup = install("workspace", str(target))
            self.assertIsNone(backup)
            self.assertTrue((Path(dest) / "SKILL.md").is_file())
            self.assertEqual((Path(dest) / "SKILL.md").read_bytes(), (REPO / ".agents/skills/architect-docs-engine/SKILL.md").read_bytes())
            self.assertEqual(install("workspace", str(target))[0], dest)

    def test_installer_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            target = Path(temp) / "target"
            target.mkdir()
            dest, _ = install("workspace", str(target), dry_run=True)
            self.assertFalse(Path(dest).exists())

if __name__ == "__main__":
    unittest.main()
