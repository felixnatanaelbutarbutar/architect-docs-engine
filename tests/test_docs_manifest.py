import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents/skills/architect-docs-engine/scripts"
FIXTURE = REPO / "examples/sample-project"
sys.path.insert(0, str(SCRIPTS))
from common import canonical_names, load_manifest
from validate_config import validate_config
from validate_docs import validate_docs
from report_audit import main as audit_report_main
from report_audit import build_report
from snapshot_workspace import snapshot_workspace

class DocsManifestTests(unittest.TestCase):
    def test_fixture_has_exact_canonical_suite_and_valid_config(self):
        result = validate_docs(FIXTURE)
        self.assertEqual(len(load_manifest()["documents"]), 21)
        self.assertEqual(len(canonical_names()), 21)
        self.assertEqual(result["present_documents"], 21)
        self.assertTrue(result["ok"], result["findings"])
        self.assertTrue(validate_config(FIXTURE)["ok"])

    def test_missing_document_fails_full_suite_audit(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE / "docs", root / "docs")
            (root / "docs" / "PRD.md").unlink()
            result = validate_docs(root)
            self.assertFalse(result["ok"])
            self.assertTrue(any(f["code"] == "missing_document" and "PRD.md" in f["message"] for f in result["findings"]))

    def test_nested_markdown_is_extra_not_a_duplicate_suite_file(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE / "docs", root / "docs")
            nested = root / "docs/archive/PRD.md"
            nested.parent.mkdir(); nested.write_text("Archived copy", encoding="utf-8")
            result = validate_docs(root)
            self.assertFalse(result["ok"])
            self.assertIn("archive/PRD.md", result["extra_markdown_documents"])

    def test_local_heading_anchors_are_checked(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE / "docs", root / "docs")
            shutil.copy(FIXTURE / "project-brief.md", root / "project-brief.md")
            hub = root / "docs/README.md"
            original = hub.read_text(encoding="utf-8")
            hub.write_text(original + "\n[Valid section](PRD.md#problem-and-evidence)\n", encoding="utf-8")
            self.assertTrue(validate_docs(root)["ok"])
            hub.write_text(original + "\n[Missing section](PRD.md#missing-section)\n", encoding="utf-8")
            result = validate_docs(root)
            self.assertFalse(result["ok"])
            self.assertTrue(any(f["code"] == "broken_anchor" for f in result["findings"]))

    def test_n_a_is_reasoned_and_no_ui_is_invented(self):
        from check_traceability import check_traceability
        result = check_traceability(FIXTURE)
        self.assertTrue(result["ok"], result["findings"])
        self.assertGreater(result["counts"]["not_applicable"], 0)
        self.assertNotIn("UI-001", result["definitions"])
        self.assertIn("N/A —", (FIXTURE / "docs/TRACEABILITY.md").read_text(encoding="utf-8"))

    def test_unresolved_evidence_is_reported_not_fabricated(self):
        from check_traceability import check_traceability
        text = (FIXTURE / "docs/PRD.md").read_text(encoding="utf-8")
        self.assertIn("Unresolved — authentication", text)
        self.assertGreater(check_traceability(FIXTURE)["counts"]["unresolved"], 0)

    def test_unresolved_decisions_block_readiness_not_mechanical_audit(self):
        report = build_report(FIXTURE)
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["release_readiness"], "blocked")
        self.assertEqual(report["blockers"], [])
        self.assertTrue(report["readiness_blockers"])

    def test_secret_like_value_is_flagged_without_echoing_value(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE / "docs", root / "docs")
            secret = "AKIA" + "1234567890ABCDEF"
            path = root / "docs" / "SECURITY.md"
            path.write_text(path.read_text(encoding="utf-8") + f"\nExample: {secret}\n", encoding="utf-8")
            result = validate_docs(root)
            finding = next(f for f in result["findings"] if f["code"] == "secret_like")
            self.assertNotIn(secret, finding["message"])

    def test_malformed_and_escaping_config_are_rejected(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); (root / "architect-docs.config.json").write_text("{broken", encoding="utf-8")
            self.assertFalse(validate_config(root)["ok"])
            (root / "architect-docs.config.json").write_text(json.dumps({"docs":{"output_dir":"../elsewhere"}}), encoding="utf-8")
            self.assertFalse(validate_config(root)["ok"])
            (root / "architect-docs.config.json").write_text(json.dumps({"requirements_sources":["../outside.md"]}), encoding="utf-8")
            self.assertFalse(validate_config(root)["ok"])

    def test_report_writer_supports_dry_run_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE, root, dirs_exist_ok=True)
            args = ["--project", str(root), "--output", "audit.json"]
            self.assertEqual(audit_report_main(args + ["--dry-run"]), 0)
            output = root / "docs/audit.json"
            self.assertFalse(output.exists())
            self.assertEqual(audit_report_main(args), 0)
            self.assertTrue(output.is_file())
            self.assertEqual(audit_report_main(args), 1)

    def test_source_snapshot_preview_and_staleness_detection(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp)
            shutil.copytree(FIXTURE, root, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".architect-docs"))
            preview = snapshot_workspace(root, dry_run=True)
            self.assertFalse(preview["would_write"])
            self.assertFalse((root / ".architect-docs/source-snapshot.json").exists())
            snapshot_workspace(root, write=True)
            self.assertEqual(build_report(root)["checks"]["source_freshness"]["status"], "CURRENT")
            source = root / "src/app.py"
            source.write_text(source.read_text(encoding="utf-8") + "\n# changed after baseline\n", encoding="utf-8")
            result = build_report(root)
            self.assertEqual(result["checks"]["source_freshness"]["status"], "STALE")
            self.assertIn("src/app.py", result["checks"]["source_freshness"]["changes"]["changed"])

    def test_review_simulation_preserves_unrelated_manual_text(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = Path(temp); shutil.copytree(FIXTURE / "docs", root / "docs")
            path = root / "docs" / "SECURITY.md"
            manual = "Human-maintained review note: retain this sentence."
            path.write_text(path.read_text(encoding="utf-8") + "\n" + manual + "\n", encoding="utf-8")
            original = path.read_bytes()
            validate_docs(root)  # Read-only review; semantic updates are agent-driven.
            self.assertEqual(path.read_bytes(), original)

if __name__ == "__main__":
    unittest.main()
