# Reqres API – Sample Bug Reports

## Bug Report Template

**Bug ID:** BR-XXX  
**Title:** Short clear summary of the issue  
**Environment:** Windows 11, Python 3.12, requests X.X.X (if applicable)  
**Endpoint:** GET/POST /api/...  
**Severity:** Blocker / Critical / Major / Minor / Trivial  
**Priority:** High / Medium / Low  
**Status:** New / Open / In Progress / Fixed / Closed  
**Reported by:** Dmytro Litvinov  
**Date:** YYYY-MM-DD  

### Preconditions
- List any required setup or test data.

### Steps to Reproduce
1. Step 1  
2. Step 2  
3. Step 3  

### Actual Result
- What actually happened (include status code + response snippet if relevant).

### Expected Result
- What should have happened (include expected status code + key fields).

### Attachments / Evidence
- Request payload
- Response payload
- Logs / screenshots (if relevant)

### Notes
- Additional context, assumptions, suspected root cause.

---

## BR-001 – Login accepts whitespace-only password and returns non-standard error

**Bug ID:** BR-001  
**Title:** Login with whitespace-only password returns inconsistent error message format  
**Environment:** Reqres API, mocked response validation  
**Endpoint:** POST /api/login  
**Severity:** Minor  
**Priority:** Medium  
**Status:** New  
**Reported by:** Dmytro Litvinov  
**Date:** 2025-12-29  

### Preconditions
- None

### Steps to Reproduce
1. Send `POST /api/login`
2. Use payload:
   ```json
   {
     "email": "eve.holt@reqres.in",
     "password": "   "
   }
    ```
### Actual Result 

- `400 Bad Request`
- Error response format differs from other validation errors.

### Expected Result

- `400 Bad Request`
- Error response follows standard contract:
    ```json
    {
     "error": "<message>"
    }
    ```

### Notes

- Inconsistent error format complicates client-side validation.

---

## BR-002 – GET user returns 200 OK for non-existing ID

**Bug ID:** BR-002  
**Title:** GET user for non-existing ID returns 200 OK
**Environment:** Reqres API (mocked)
**Endpoint:** GET /api/users/{id} 
**Severity:** Major  
**Priority:** High  
**Status:** New  
**Reported by:** Dmytro Litvinov  
**Date:** 2025-12-29  

### Preconditions

- Use non-existing user ID (e.g. `999`)

### Steps to Reproduce

1. Send `GET /api/users/999`

### Actual Result 

- `200 OK`
- Empty or missing data field.

### Expected Result

- `404 Not Found`
- Error response returned.

### Notes

- Breaks client expectations and response contract validation.

---

## BR-003 – Duplicate user IDs across paginated responses

**Bug ID:** BR-003  
**Title:** Duplicate user IDs returned across pages
**Environment:** Reqres API (mocked)
**Endpoint:** GET /api/users?page=1, page=2
**Severity:** Minor 
**Priority:** Low
**Status:** New  
**Reported by:** Dmytro Litvinov  
**Date:** 2025-12-29  

### Preconditions

- Pagination enabled

### Steps to Reproduce

1. Send `GET /api/users?page=1`
2. Collect all `data[].id`
3. Send `GET /api/users?page=2`
4. Compare IDs

### Actual Result 

- One or more IDs are duplicated across pages.

### Expected Result

- User IDs are unique across paginated results.

### Notes

- Impacts client-side aggregation and analytics logic.

---

## BR-004 – Duplicate user IDs across paginated responses

**Bug ID:** BR-004 
**Title:** Missing `Content-Type: application/json` header
**Environment:** Reqres API (mocked)
**Endpoint:** Multiple endpoints
**Severity:** Minor 
**Priority:** Medium
**Status:** New  
**Reported by:** Dmytro Litvinov  
**Date:** 2025-12-29  

### Steps to Reproduce

1. Send any valid API request
2. Inspect response headers

### Actual Result 

- `Content-Type` header is missing or incorrect.

### Expected Result

- Header present:

    ```pgsql
        Content-Type: application/json; charset=utf-8
    ```

### Notes

- Some HTTP clients rely on this header for response parsing.