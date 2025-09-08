# 🐾 API Error Responses

All WOOFY McWOOFSON API endpoints return standardized error responses.

## Format

```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": { "optional": "context" }
  }
}
```

## Common Error Codes

| Code              | HTTP | Message                       |
|-------------------|------|-------------------------------|
| UNAUTHORIZED      | 401  | Invalid or missing token      |
| FORBIDDEN         | 403  | Insufficient permissions      |
| NOT_FOUND         | 404  | Resource not found            |
| RATE_LIMIT        | 429  | Too many requests             |
| SERVER_ERROR      | 500  | Internal server error         |
| VALIDATION_ERROR  | 400  | Invalid input                 |

## Example

```json
{
  "status": "error",
  "error": {
    "code": "NOT_FOUND",
    "message": "Document not found",
    "details": {
      "document_id": "doc-xyz"
    }
  }
}
```