# API Endpoints Documentation

This document provides an overview of the various API endpoints available in the Woofy McWoofson project, including their usage, request/response formats, and examples.

## Base URL

The base URL for all API requests is:

```
https://api.bakerystreet.example.com/v1
```

## Endpoints

### 1. Dog-themed Health Check

- **Endpoint:** `/woof`
- **Method:** `GET`
- **Description:** Returns a friendly woof if the API is running.

#### Request

No parameters are required.

#### Response

- **Status Code:** `200 OK`
- **Content:**
  ```json
  {
    "message": "Woof! 🐾 The API is live."
  }
  ```

### 2. Trigger an Automation Workflow

- **Endpoint:** `/automation/run`
- **Method:** `POST`
- **Description:** Triggers a specified automation workflow.

#### Request

- **Content-Type:** `application/json`
- **Body:**
  ```json
  {
    "workflow": "google-drive-backup",
    "params": {
      // Additional parameters specific to the workflow
    }
  }
  ```

#### Response

- **Status Code:** `202 Accepted`
- **Content:**
  ```json
  {
    "runId": "12345",
    "status": "pending"
  }
  ```

- **Error Responses:**
  - **Status Code:** `400 Bad Request`
  - **Status Code:** `401 Unauthorized`

### 3. Fetch Audit Logs (Admin Only)

- **Endpoint:** `/audit/logs`
- **Method:** `GET`
- **Description:** Retrieves audit logs for administrative purposes.

#### Request Parameters

- **Query Parameter:** `since` (optional) - Return logs since this time.

#### Response

- **Status Code:** `200 OK`
- **Content:**
  ```json
  [
    {
      "timestamp": "2025-09-08T12:00:00Z",
      "event": "User logged in",
      "user": "admin"
    },
    // More log entries
  ]
  ```

- **Error Responses:**
  - **Status Code:** `401 Unauthorized`
  - **Status Code:** `403 Forbidden`

## Conclusion

This document serves as a guide for developers and users to understand how to interact with the Woofy McWoofson API. For further details, please refer to the OpenAPI specification located in `docs/api/openapi.yaml`.