# Reqres API – Traceability Matrix

## Overview

This traceability matrix maps manual test cases to the current automated API tests
implemented in the project (`tests/test_auth.py`, `tests/test_users.py`, `tests/test_base_client.py`).

Where one automated test covers multiple manual scenarios (e.g. parametrized tests),
the mapping is listed as one-to-many.

---

## Traceability Matrix

| Feature / Area | Manual Test Case ID | Manual Title | Automated Test (pytest) | Coverage |
|---|---|---|---|---|
| Auth | TC-AUTH-001 | Successful login with valid credentials | `test_login_success_mock` (tests/test_auth.py) | Automated |
| Auth | TC-AUTH-002 | Login with missing password | `test_login_missing_password_mock` (tests/test_auth.py) | Automated |
| Auth | TC-AUTH-003 | Login with missing email | `test_login_errors_mock` param: `{"password":"123"}` (tests/test_auth.py) | Automated (param) |
| Auth | TC-AUTH-004 | Login with invalid email format | `test_login_errors_mock` param: `{"email":"x","password":"y"}` (tests/test_auth.py) | Automated (param) |
| Auth | TC-AUTH-005 | Login with empty request body | Not implemented | Manual |
| Users | TC-USER-001 | Get existing user by ID | `test_get_user_mock` (tests/test_users.py) | Automated |
| Users | TC-USER-002 | Get user with non-existing ID | `test_get_user_not_found_mock` (tests/test_users.py) | Automated |
| Users | TC-USER-003 | Get user with invalid ID format | Not implemented | Manual |
| Users | TC-USER-004 | Validate user response schema | `test_get_user_mock` (SingleUserResponse validation) (tests/test_users.py) | Automated |
| Users | TC-USERS-001 | Get list of users | `test_list_users_mock` (tests/test_users.py) | Automated |
| Users | TC-USERS-002 | Validate list users response schema | `test_list_users_mock` (ListUsersResponse validation) (tests/test_users.py) | Automated |
| Users | TC-USERS-003 | Validate pagination fields | `test_list_users_mock` (checks `page`) (tests/test_users.py) | Automated (partial) |
| Users | TC-USERS-004 | Get users with invalid query parameters | Not implemented | Manual |
| Errors | TC-ERR-001 | Validate error message format | `test_login_missing_password_mock` + `test_login_errors_mock` (ErrorResponse validation) (tests/test_auth.py) | Automated |
| Errors | TC-ERR-002 | Validate HTTP status codes | Multiple tests assert status codes (auth/users) | Automated |
| Headers | TC-ERR-003 | Validate response headers | `test_baseclient_sets_content_type_in_headers` (tests/test_base_client.py) | Automated |

---

## Notes

- `test_login_errors_mock` is parametrized and covers multiple negative login scenarios:
  - missing email
  - invalid credentials / user not found
- Pagination validation is currently **partial** (page field asserted). If you want full pagination coverage,
  add assertions for fields like `per_page`, `total`, `total_pages` (if your mocked response includes them).
- Manual-only cases are intentionally left for future automation expansion or exploratory coverage.

---

## Automation Summary

- **Total manual test cases:** 16
- **Automated (fully or partially):** 12
- **Manual-only:** 4

Manual-only cases:
- TC-AUTH-005 (empty body)
- TC-USER-003 (invalid ID format)
- TC-USERS-004 (invalid query params)
- TC-USERS-003 (full pagination fields: partial automation only)
