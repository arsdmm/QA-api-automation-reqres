from __future__ import annotations

from typing import Any, Dict, Optional

from .base_client import BaseClient, ApiResponse


class ReqresClient(BaseClient):

    def login(self, email: str, password: str) -> ApiResponse:
        payload = {"email": email, "password": password}
        return self.post("/api/login", json=payload)

    def login_missing_password(self, email: str) -> ApiResponse:
        payload = {"email": email}
        return self.post("/api/login", json=payload)

    def list_users(self, page: int = 1) -> ApiResponse:
        return self.get("/api/users", params={"page": page})

    def get_user(self, user_id: int) -> ApiResponse:
        return self.get(f"/api/users/{user_id}")

    def create_user(self, name: str, job: str) -> ApiResponse:
        payload = {"name": name, "job": job}
        return self.post("/api/users", json=payload)

    def update_user(self, user_id: int, name: Optional[str] = None, job: Optional[str] = None) -> ApiResponse:
        payload: Dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if job is not None:
            payload["job"] = job
        return self.put(f"/api/users/{user_id}", json=payload)

    def delete_user(self, user_id: int) -> ApiResponse:
        return self.delete(f"/api/users/{user_id}")
