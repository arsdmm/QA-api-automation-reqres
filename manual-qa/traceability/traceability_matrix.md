# Reqres API – Traceability Matrix

## Overview

This traceability matrix maps manual test cases to automated API tests.
It ensures that critical functional scenarios are covered by automation
and provides visibility into manual-only coverage.

---

## Traceability Matrix

| Requirement / Feature | Manual Test Case ID | Automated Test | Automation Status |
|----------------------|--------------------|----------------|-------------------|
| User login (success) | TC-AUTH-001 | test_login_success | Automated |
| Login without password | TC-AUTH-002 | test_login_missing_password | Automated |
| Login without email | TC-AUTH-003 | test_login_missing_email | Automated |
| Login with invalid email format | TC-AUTH-004 | test_login_invalid_email | Automated |
| Empty login request body | TC-AUTH-005 | test_login_empty_payload | Automated |
| Get existing user by ID | TC-USER-001 | test_get_single_user_success | Automated |
| Get non-existing user | TC-USER-002 | test_get_single_user_not_found | Automated |
| Invalid user ID format | TC-USER-003 | test_get_user_invalid_id | Automated |
| User response schema validation | TC-USER-004 | test_user_response_contract | Automated |
| Get list of users | TC-USERS-001 | test_list_users_success | Automated |
| List users response schema | TC-USERS-002 | test_list_users_contract | Automated |
| Pagination fields validation | TC-USERS-003 | test_list_users_pagination_fields | Automated |
| Invalid query parameters | TC-USERS-004 | Not automated | Manual |
| Error message format validation | TC-ERR-001 | test_error_response_format | Automated |
| HTTP status code validation | TC-ERR-002 | test_http_status_codes | Automated |
| Response headers validation | TC-ERR-003 | test_response_headers | Automated |

---

## Notes

- High-priority and critical scenarios are covered by automated tests.
- Low-risk or exploratory scenarios remain manual by design.
- Automation coverage can be expanded as new requirements appear.
- Automated test names correspond to pytest test functions in the test suite.

---

## Automation Summary

- **Total manual test cases:** 16  
- **Automated:** 14  
- **Manual-only:** 2  

Automation focuses on stable, repeatable, and high-impact scenarios.
