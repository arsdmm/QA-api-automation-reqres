from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests


@dataclass
class ApiResponse:
    status_code: int
    json: Optional[Dict[str, Any]]
    text: str
    headers: Dict[str, str]


class BaseClient:

    def __init__(self, base_url: str, timeout_seconds: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url}{path}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ApiResponse:
        response = self.session.request(
            method=method.upper(),
            url=self._url(path),
            params=params,
            json=json,
            headers=headers,
            timeout=self.timeout_seconds,
        )

        parsed_json: Optional[Dict[str, Any]]
        try:
            parsed_json = response.json()
        except ValueError:
            parsed_json = None

        return ApiResponse(
            status_code=response.status_code,
            json=parsed_json,
            text=response.text,
            headers=dict(response.headers),
        )

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self.request("GET", path, params=params, headers=headers)

    def post(self, path: str, *, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self.request("POST", path, json=json, headers=headers)

    def put(self, path: str, *, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self.request("PUT", path, json=json, headers=headers)

    def delete(self, path: str, *, headers: Optional[Dict[str, str]] = None) -> ApiResponse:
        return self.request("DELETE", path, headers=headers)
