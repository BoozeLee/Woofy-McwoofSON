# 🐾 WOOFY API Endpoints

This document details all available API endpoints for the WOOFY McWOOFSON platform.

---

## List of Endpoints

### 1. Fetch Document

- **Path:** `/api/documents/fetch`
- **Method:** `POST`
- **Authentication:** Required (Bearer Token)
- **Request Body:**
  ```json
  {
    "document_id": "string"
  }
  ```
- **Response:**
  ```json
  {
    "status": "success",
    "document": { ... }
  }
  ```
- **Error Codes:**  
  - 401 Unauthorized  
  - 404 Not Found  
  - 429 Rate Limit

---

### 2. Run Security Scan

- **Path:** `/api/security/scan`
- **Method:** `POST`
- **Authentication:** Required (Bearer Token)
- **Request Body:** None
- **Response:**
  ```json
  {
    "status": "success",
    "scan_report": { ... }
  }
  ```
- **Error Codes:**  
  - 401 Unauthorized  
  - 500 Internal Error

---

## Versioning

- Current API Version: `v1`
- All endpoints are prefixed with `/api/v1/` in production.

## Rate Limits

- Default: 60 requests/minute per user.

## See Also

- [Authentication](authentication.md)
- [API Examples](examples.md)