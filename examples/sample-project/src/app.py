"""Fictional in-memory ticket API used only as a documentation fixture."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

class TicketAPI:
    """Small deterministic handler; a real HTTP server adapter is intentionally absent."""

    def __init__(self) -> None:
        self._tickets: list[dict[str, Any]] = []

    def handle(self, method: str, path: str, body: bytes = b"") -> tuple[int, dict[str, Any]]:
        if path == "/tickets" and method == "POST":
            if len(body) > 16_384:
                return 413, {"error": "body_too_large"}
            try:
                payload = json.loads(body.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                return 400, {"error": "invalid_json"}
            if not isinstance(payload, dict) or not isinstance(payload.get("title"), str) or not payload["title"].strip():
                return 422, {"error": "title_required"}
            if "description" in payload and not isinstance(payload["description"], str):
                return 422, {"error": "description_must_be_text"}
            ticket = {"ticket_id": f"T-{len(self._tickets) + 1:04d}", "title": payload["title"].strip(),
                      "description": payload.get("description", ""), "status": "open",
                      "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            self._tickets.append(ticket)
            return 201, ticket.copy()
        if path == "/tickets" and method == "GET":
            return 200, {"items": [item.copy() for item in self._tickets]}
        return 404, {"error": "not_found"}
