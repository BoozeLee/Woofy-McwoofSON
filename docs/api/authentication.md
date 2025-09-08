# 🐾 API Authentication

All WOOFY API endpoints require secure authentication.

## Supported Methods

- **Bearer Token (JWT):** Include in `Authorization` header.
- **AWS SigV4:** For AWS-integrated clients.

## Example

```http
POST /api/v1/documents/fetch HTTP/1.1
Authorization: Bearer {your_token}
Content-Type: application/json
```

## Token Expiry

- Tokens expire after 1 hour of inactivity.

## Error Codes

- 401 Unauthorized — invalid or missing token
- 403 Forbidden — insufficient permissions