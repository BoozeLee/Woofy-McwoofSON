# Example API Requests and Responses

This document provides example requests and responses for the Bakery Street Project API. Each example includes the HTTP method, endpoint, request body (if applicable), and the expected response.

## 1. Dog-themed Health Check

### Request

**Method:** GET  
**Endpoint:** `/woof`

```http
GET https://api.bakerystreet.example.com/v1/woof
```

### Response

**Status Code:** 200 OK

```json
{
  "message": "Woof! 🐾 The API is live."
}
```

---

## 2. Trigger an Automation Workflow

### Request

**Method:** POST  
**Endpoint:** `/automation/run`  
**Request Body:**

```json
{
  "workflow": "google-drive-backup",
  "params": {
    "folderId": "12345",
    "includeSubfolders": true
  }
}
```

### Response

**Status Code:** 202 Accepted

```json
{
  "runId": "abc123",
  "status": "pending"
}
```

---

## 3. Fetch Audit Logs

### Request

**Method:** GET  
**Endpoint:** `/audit/logs?since=2023-09-01T00:00:00Z`

```http
GET https://api.bakerystreet.example.com/v1/audit/logs?since=2023-09-01T00:00:00Z
```

### Response

**Status Code:** 200 OK

```json
[
  {
    "timestamp": "2023-09-08T12:00:00Z",
    "event": "Automation run started",
    "user": "admin"
  },
  {
    "timestamp": "2023-09-08T12:05:00Z",
    "event": "Audit log fetched",
    "user": "admin"
  }
]
```

---

## Notes

- Ensure that all requests include the necessary authentication headers as outlined in the authentication documentation.
- Modify the request parameters as needed to fit specific use cases.