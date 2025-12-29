# QA API Automation – Reqres (Mock-based)

This project is a small API automation framework built to demonstrate
a clean and scalable approach to testing REST APIs using Python.

The focus of the project is **client-side API testing**, contract validation,
and stable mock-based tests without dependency on external services.

---

## 1. Tech Stack

- Python 3.12
- pytest
- requests
- responses
- pydantic

---

## 2. Testing Scope

This framework focuses on the API Client layer and validates:

- request/response contracts
- client-side behavior
- error handling and edge cases
- HTTP metadata (status codes, headers)

It intentionally avoids:
- UI testing
- integration with real external APIs
- database validation

---

## 3. Project Structure

```text
api/
├── clients/
│   ├── base_client.py        # HTTP layer (requests wrapper)
│   └── reqres_client.py      # Business API client (Reqres endpoints)
│
├── models/
│   ├── user_models.py        # Pydantic models for user responses
│   └── auth_models.py        # Pydantic models for auth responses
│
├── config.py                 # Base URL and shared config
│
tests/
├── test_users.py             # User-related API tests (mocked)
├── test_auth.py              # Auth-related API tests (mocked)
├── test_base_client.py       # Infrastructure tests for BaseClient
│
└── conftest.py               # pytest fixtures
```

---

## 4. Architecture Overview

**BaseClient**

BaseClient is a low-level HTTP wrapper around the requests library.
It is responsible for:

- sending HTTP requests
- handling timeouts
- parsing JSON responses safely
- returning a unified ApiResponse object
- preserving response metadata (headers, status code, raw text)

This layer is independent of any specific API.

---

## 5. ReqresClient

ReqresClient is a higher-level client that describes
business endpoints of the Reqres API, such as:

- login
- get user
- list users

It delegates all HTTP logic to BaseClient.

---

## 6. Pydantic Models

Pydantic models are used to validate API response contracts.
They ensure that the structure of the response matches expectations
without writing multiple field-level assertions.

---

## 7. Mock-based Testing (responses)

All API tests use the responses library to mock HTTP responses.
This allows tests to:

- run without internet access
- avoid external API instability
- be deterministic and CI-friendly

The tests validate client behavior, not the real Reqres service.

---

## 8. Test Coverage

The project includes the following test types:

- Smoke API tests (happy paths)
- Negative scenarios (validation and error cases)
- Contract validation using Pydantic
- Infrastructure tests for HTTP response handling (headers, status codes)
- Parametrized tests for multiple error cases

---

## 9. Running the Tests

```powershell
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
pytest -v
```

---

## 10. Purpose

This project demonstrates:

- clean separation of concerns in API automation
- scalable client-based API testing
- practical usage of mocks and contracts
- real-world testing patterns used in production teams

---

## Author

**Dmytro Litvinov**

LinkedIn:  
[Dmytro Litvinov](https://www.linkedin.com/in/dmytro-litvinov-2b319b235)

---

## License

This project is released under the MIT License
You are free to use, modify, and distribute it with attribution