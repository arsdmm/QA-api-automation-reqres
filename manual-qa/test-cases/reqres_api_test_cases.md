# Reqres API – Manual Test Cases

## Overview

This document contains manual test cases for the Reqres API.
Test cases cover core functional scenarios, negative cases,
and validation of API behavior.

Each test case has a unique ID that can be referenced
in automated tests and the traceability matrix.

---

## Test Cases – Authentication (Login)

| Test Case ID | Title | Endpoint | Preconditions | Steps | Expected Result | Priority |
|-------------|------|----------|---------------|-------|-----------------|----------|
| TC-AUTH-001 | Successful login with valid credentials | POST /api/login | Valid email and password | 1. Send login request with valid credentials | 200 OK, token returned | High |
| TC-AUTH-002 | Login with missing password | POST /api/login | Valid email | 1. Send login request without password | 400 Bad Request, error message returned | High |
| TC-AUTH-003 | Login with missing email | POST /api/login | Valid password | 1. Send login request without email | 400 Bad Request, error message returned | High |
| TC-AUTH-004 | Login with invalid email format | POST /api/login | Invalid email | 1. Send login request with invalid email format | 400 Bad Request | Medium |
| TC-AUTH-005 | Login with empty request body | POST /api/login | None | 1. Send login request with empty body | 400 Bad Request | Medium |

---

## Test Cases – Get Single User

| Test Case ID | Title | Endpoint | Preconditions | Steps | Expected Result | Priority |
|-------------|------|----------|---------------|-------|-----------------|----------|
| TC-USER-001 | Get existing user by ID | GET /api/users/{id} | Valid user ID | 1. Send GET request with valid user ID | 200 OK, user data returned | High |
| TC-USER-002 | Get user with non-existing ID | GET /api/users/{id} | Invalid user ID | 1. Send GET request with non-existing ID | 404 Not Found | High |
| TC-USER-003 | Get user with invalid ID format | GET /api/users/{id} | Invalid ID format | 1. Send GET request with string ID | 404 Not Found | Medium |
| TC-USER-004 | Validate user response schema | GET /api/users/{id} | Valid user ID | 1. Send GET request | Response matches expected contract | High |

---

## Test Cases – List Users

| Test Case ID | Title | Endpoint | Preconditions | Steps | Expected Result | Priority |
|-------------|------|----------|---------------|-------|-----------------|----------|
| TC-USERS-001 | Get list of users | GET /api/users | None | 1. Send GET request | 200 OK, list of users returned | High |
| TC-USERS-002 | Validate list users response schema | GET /api/users | None | 1. Send GET request | Response structure is valid | High |
| TC-USERS-003 | Validate pagination fields | GET /api/users | None | 1. Send GET request | Pagination fields present | Medium |
| TC-USERS-004 | Get users with invalid query parameters | GET /api/users | Invalid params | 1. Send GET request with invalid params | 200 OK or handled error | Low |

---

## Test Cases – Error Handling

| Test Case ID | Title | Endpoint | Preconditions | Steps | Expected Result | Priority |
|-------------|------|----------|---------------|-------|-----------------|----------|
| TC-ERR-001 | Validate error message format | Any | Error scenario | 1. Trigger API error | Error response contains message field | Medium |
| TC-ERR-002 | Validate HTTP status codes | Any | Error scenario | 1. Trigger API error | Correct HTTP status returned | High |
| TC-ERR-003 | Validate response headers | Any | Valid request | 1. Send request | Headers are present and valid | Low |

---

## Notes

- Test cases marked as **High priority** are candidates for automation.
- Automated test coverage is implemented for critical authentication
  and user-related scenarios.
- Test case IDs are used for traceability between manual and automated tests.

---
