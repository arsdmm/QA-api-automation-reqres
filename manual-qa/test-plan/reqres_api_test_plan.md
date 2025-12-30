# Reqres API Test Plan

## 1. Introduction

This document describes the test plan for the Reqres API.
The purpose of this test plan is to define the testing scope, test approach,
resources, and deliverables for manual and automated API testing activities.

This test plan follows a practical QA approach and reflects real-world
testing workflows used in modern software development teams.

---

## 2. Scope

### 2.1 In Scope

The following areas are included in the testing scope:

- User-related API endpoints
- Authentication (login) endpoint
- Positive and negative API scenarios
- Response contract validation
- HTTP status codes and response headers
- Client-side API behavior

### 2.2 Out of Scope

The following areas are excluded from testing:

- UI testing
- Performance and load testing
- Security and penetration testing
- Database validation
- Integration with real external services

---

## 3. Test Items

The following API components will be tested:

- POST /api/login
- GET /api/users/{id}
- GET /api/users
- API response structure and data types
- Error responses and validation messages

---

## 4. Test Approach

Testing will be performed using a combination of manual testing and automated
API testing.

### Manual Testing

Manual testing will be used to:

- design test scenarios and test cases
- identify edge cases and negative scenarios
- validate expected API behavior
- document defects and inconsistencies

### Automated Testing

Automated testing will be used to:

- cover critical and repetitive scenarios
- validate API response contracts using Pydantic models
- ensure regression safety
- provide fast feedback during development

All automated API tests are based on mocked HTTP responses to ensure
deterministic and stable test execution.

---

## 5. Test Types

The following test types will be performed:

- Smoke testing
- Functional testing
- Negative testing
- Contract testing
- Regression testing

---

## 6. Test Environment

### 6.1 System Under Test

- API: Reqres API (mocked)

### 6.2 Tools and Technologies

- Programming Language: Python
- Test Framework: pytest
- HTTP Client: requests
- Mocking Library: responses
- Data Validation: Pydantic

### 6.3 Operating Systems

- Windows
- Linux
- macOS

---

## 7. Entry and Exit Criteria

### 7.1 Entry Criteria

Testing activities may begin when:

- API requirements are defined
- Test plan is approved
- Test cases are prepared and reviewed

### 7.2 Exit Criteria

Testing activities may be finished when:

- All planned test cases are executed
- Critical defects are fixed or accepted
- Automated tests are passing successfully
- Test results are documented

---

## 8. Test Deliverables

The following deliverables will be produced:

- Test Plan document
- Manual test cases
- Bug reports
- Automated API test suite
- Test execution summary

---

## 9. Risks and Mitigation

|            Risk            |             Impact             |                Mitigation               |
|----------------------------|--------------------------------|-----------------------------------------|
| API specification changes  | Test cases may become outdated | Regular review and updates              |
| Insufficient test coverage | Defects may go undetected      | Test case reviews and coverage analysis |
| Mock data inconsistency    | False positives or negatives   | Centralized mock definitions            |

---

## 10. Responsibilities

|     Role    |            Responsibilities               |
|-------------|-------------------------------------------|
| QA Engineer | Test planning, manual testing, automation |
| Developer   | Bug fixing and technical support          |
| QA Lead     | Review and approval of test artifacts     |

---

## 11. Approval

|       Name      |     Role    |    Date    | Signature |
|-----------------|-------------|------------|-----------|
| Dmytro Litvinov | QA Engineer | 12/29/2025 |     DL    |
