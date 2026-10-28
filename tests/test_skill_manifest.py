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

    def test_visual_guidance_has_antigeneric_and_rendered_review_rules(self):
        guide = (REPO / ".agents/skills/architect-docs-engine/references/design-and-accessibility.md").read_text(encoding="utf-8")
        self.assertIn("Anti-generic visual guardrails", guide)
        self.assertIn("Do not default to purple/blue gradients", guide)
        self.assertIn("Do not add decorative icons", guide)
        self.assertIn("Visual review gate", guide)
        self.assertIn("does not itself render or certify a frontend", guide)

    def test_security_guidance_covers_bots_and_agent_boundaries(self):
        guide = (REPO / ".agents/skills/architect-docs-engine/references/security-and-abuse-resistance.md").read_text(encoding="utf-8")
        self.assertIn("Bots, abuse, and resource limits", guide)
        self.assertIn("prompt injection cannot be fully eliminated", guide.lower())
        self.assertIn("outside the model", guide)
        self.assertIn("OWASP Bot Management", guide)

    def test_ux_guidance_does_not_default_forms_to_popups(self):
        guide = (REPO / ".agents/skills/architect-docs-engine/references/ux-interaction-patterns.md").read_text(encoding="utf-8")
        self.assertIn("page first, no popup by default", guide.lower())
        self.assertIn("Do not put a primary, long, multi-step", guide)
        self.assertIn("WAI-ARIA Authoring Practices", guide)

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
