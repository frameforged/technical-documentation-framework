# API Endpoint Template

```md
## [Endpoint Name]

**Method:** `[GET|POST|PUT|PATCH|DELETE]`  
**Path:** `/path`  
**Purpose:**  
[Explain what this endpoint does.]

### Authentication

[Explain authentication requirements.]

### Permissions

[Explain required permission or role.]

### Request Headers

| Header | Required | Description |
|---|---:|---|
| `Authorization` | Yes | Bearer token or other credential. |

### Path Parameters

| Parameter | Type | Required | Description |
|---|---|---:|---|

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---:|---|

### Request Body

```json
{
  "example": "value"
}
```

### Response Body

```json
{
  "result": "value"
}
```

### Status Codes

| Status | Meaning |
|---:|---|
| 200 | Success |
| 400 | Invalid request |
| 401 | Authentication required |
| 403 | Permission denied |
| 404 | Resource not found |
| 500 | Internal error |

### Error Cases

| Error | Cause | Recommended Handling |
|---|---|---|

### Example Request

```bash
curl -X POST "https://example.com/path" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"example":"value"}'
```

### Example Response

```json
{
  "result": "value"
}
```

### Notes

[Important constraints, limits, or edge cases.]
```
