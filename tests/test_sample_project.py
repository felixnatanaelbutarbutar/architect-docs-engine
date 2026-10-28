import sys
import unittest
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "examples/sample-project/src"
sys.path.insert(0, str(SRC))
from app import TicketAPI

class SampleProjectTests(unittest.TestCase):
    def test_handler_contract(self):
        api = TicketAPI()
        status, created = api.handle("POST", "/tickets", b'{"title":"fixture"}')
        self.assertEqual(status, 201)
        self.assertEqual(api.handle("GET", "/tickets")[1]["items"], [created])

if __name__ == "__main__":
    unittest.main()
