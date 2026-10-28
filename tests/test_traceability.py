import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / ".agents/skills/architect-docs-engine/scripts"
FIXTURE = REPO / "examples/sample-project"
sys.path.insert(0, str(SCRIPTS))
from check_traceability import check_traceability

class TraceabilityTests(unittest.TestCase):
    def copy_fixture(self, temp):
        root = Path(temp) / "project"
        root.mkdir()
        shutil.copytree(FIXTURE / "docs", root / "docs")
        return root

    def test_many_to_many_references_and_coverage_counts(self):
        result = check_traceability(FIXTURE)
        self.assertEqual(result["counts"]["dangling"], 0)
        self.assertEqual(result["counts"]["duplicate"], 0)
        self.assertGreaterEqual(len(result["references"]["REQ-001"]), 3)
        self.assertGreater(result["counts"]["covered"], 0)

    def test_duplicate_definition_and_dangling_tc_are_detected(self):
        with tempfile.TemporaryDirectory(dir=REPO) as temp:
            root = self.copy_fixture(temp)
            prd = root / "docs/PRD.md"
            prd.write_text(prd.read_text(encoding="utf-8") + "\n**REQ-001** — duplicate fixture definition.\n", encoding="utf-8")
            trace = root / "docs/TRACEABILITY.md"
            trace.write_text(trace.read_text(encoding="utf-8") + "\nRegression target: **TC-999**.\n", encoding="utf-8")
            result = check_traceability(root)
            self.assertIn("REQ-001", result["duplicate_ids"])
            self.assertIn("TC-999", result["dangling_ids"])
            self.assertFalse(result["ok"])

if __name__ == "__main__":
    unittest.main()
