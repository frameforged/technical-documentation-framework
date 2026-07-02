# API Documentation Rules

## Purpose

Create API documentation that is usable by developers and integrators.

## Required endpoint fields

Each endpoint must include:

- Purpose
- HTTP method
- Path
- Authentication requirement
- Required permissions
- Request headers
- Path parameters
- Query parameters
- Request body
- Response body
- Status codes
- Error cases
- Example request
- Example response
- Notes and constraints

## Endpoint template

```md
## Endpoint Name

**Method:** `POST`  
**Path:** `/api/example`  
**Purpose:**  
...

### Authentication

...

### Permissions

...

### Request Headers

| Header | Required | Description |
|---|---:|---|

### Request Body

```json
{
  "field": "value"
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

### Error Cases

| Error | Cause | Recommended Handling |
|---|---|---|

### Example

...

### Notes

...
```

## Do not invent APIs

If the user did not provide endpoint details, create a proposed API section only if explicitly requested, and clearly label it as a proposed structure.
