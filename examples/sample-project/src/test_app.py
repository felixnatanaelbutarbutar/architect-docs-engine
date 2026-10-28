"""Executable tests for the synthetic in-process fixture."""
import json
import unittest

from app import TicketAPI

class TicketAPITests(unittest.TestCase):
    def setUp(self):
        self.api = TicketAPI()

    def test_create_then_list_ticket(self):
        status, created = self.api.handle("POST", "/tickets", json.dumps({"title": "Printer issue"}).encode())
        self.assertEqual(status, 201)
        self.assertEqual(created["ticket_id"], "T-0001")
        listed_status, listed = self.api.handle("GET", "/tickets")
        self.assertEqual(listed_status, 200)
        self.assertEqual(listed["items"], [created])

    def test_blank_title_is_rejected(self):
        status, response = self.api.handle("POST", "/tickets", b'{"title":"  "}')
        self.assertEqual((status, response["error"]), (422, "title_required"))

    def test_malformed_json_is_rejected(self):
        status, response = self.api.handle("POST", "/tickets", b"{")
        self.assertEqual((status, response["error"]), (400, "invalid_json"))

    def test_oversized_body_is_rejected(self):
        status, response = self.api.handle("POST", "/tickets", b"x" * 16_385)
        self.assertEqual((status, response["error"]), (413, "body_too_large"))

if __name__ == "__main__":
    unittest.main()
