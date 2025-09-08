# 🐾 API Example Calls

## Fetch a Document

```bash
curl -X POST https://api.woofy.example.com/api/v1/documents/fetch \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"document_id": "doc-123"}'
```

## Run a Security Scan

```bash
curl -X POST https://api.woofy.example.com/api/v1/security/scan \
  -H "Authorization: Bearer $TOKEN"
```