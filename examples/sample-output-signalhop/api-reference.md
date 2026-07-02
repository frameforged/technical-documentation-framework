# API Reference

Base URL: `https://api.signalhop.example/v1`

## Authentication

Every request carries an API key in the `Authorization` header:

```text
Authorization: Bearer sh_live_4f8a...
```

Keys are mode-scoped: `sh_test_` keys see only test-mode data, `sh_live_` keys only live-mode data. A request without a key, or with a revoked one, returns `401` with error code `invalid_api_key`.

## Rate limits

Publish requests (`POST /events`) are limited to 600 per minute per key; all other endpoints share a 1,200-per-minute pool. Exceeding a limit returns `429` with a `Retry-After` header in seconds. At sustained publish rates above 10 events per second, batch upstream or request a limit increase — client-side retry loops against a `429` only extend the outage.

## Error model

Errors share one shape:

```json
{
  "error": {
    "code": "payload_too_large",
    "message": "Payload is 412031 bytes; the maximum is 262144.",
    "request_id": "req_8c1d"
  }
}
```

`code` is stable and safe to branch on; `message` is human-readable and may change. Include `request_id` in support requests — it is the fastest path to the server-side log line.

| Status | Meaning |
|---:|---|
| 400 | Malformed request body or invalid field value |
| 401 | Missing, invalid, or revoked API key |
| 404 | Resource does not exist in this mode |
| 409 | Conflict, e.g. replaying a delivery that is still in progress |
| 413 | Payload exceeds 256 KB |
| 429 | Rate limit exceeded |
| 5xx | Signalhop-side failure; safe to retry with backoff |

## Publish an event

**`POST /events`**

Accepts one event and queues it for delivery to every matching active subscription. Returns `202`: acceptance means "durably stored", not "delivered" — delivery status lives on the deliveries resource.

### Request body

| Field | Type | Required | Notes |
|---|---|---:|---|
| `topic` | string | yes | Dot-separated, `[a-z0-9_.]`, max 128 chars |
| `payload` | object | yes | Arbitrary JSON, max 256 KB serialized |
| `idempotency_key` | string | no | Publishes with the same key within 24 h return the original event instead of creating a duplicate |

### Example

```bash
curl https://api.signalhop.example/v1/events \
  -H "Authorization: Bearer sh_live_4f8a..." \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "invoice.paid",
    "payload": {"invoice_id": "inv_991", "amount_cents": 12900},
    "idempotency_key": "inv_991-paid"
  }'
```

```json
{
  "id": "evt_3fa8",
  "topic": "invoice.paid",
  "created_at": "2026-07-02T09:15:04Z",
  "matched_subscriptions": 3
}
```

`matched_subscriptions: 0` is not an error; it means no active subscription matched the topic. If you expected a match, check for a paused subscription or a topic typo — `invoice.payed` will match nothing, silently.

### Errors

| Code | Cause | Handling |
|---|---|---|
| `invalid_topic` | Topic contains uppercase or disallowed characters | Fix the topic name; do not retry as-is |
| `payload_too_large` | Serialized payload over 256 KB | Send a reference (URL, ID) instead of the blob |
| `rate_limited` | Over 600 publishes/min | Back off per `Retry-After`, then batch upstream |

## Create a subscription

**`POST /subscriptions`**

Binds a topic pattern to an HTTPS endpoint. The response is the only time the signing `secret` is returned; store it on receipt.

### Request body

| Field | Type | Required | Notes |
|---|---|---:|---|
| `topic` | string | yes | Exact (`invoice.paid`) or prefix wildcard (`invoice.*`) |
| `endpoint_url` | string | yes | Must be HTTPS; private-network addresses are rejected |
| `status` | string | no | `active` (default) or `paused` |

### Example

```bash
curl https://api.signalhop.example/v1/subscriptions \
  -H "Authorization: Bearer sh_live_4f8a..." \
  -H "Content-Type: application/json" \
  -d '{"topic": "invoice.*", "endpoint_url": "https://example.com/hooks"}'
```

```json
{
  "id": "sub_7c21",
  "topic": "invoice.*",
  "endpoint_url": "https://example.com/hooks",
  "secret": "whsec_9k2m...",
  "status": "active"
}
```

### Errors

| Code | Cause | Handling |
|---|---|---|
| `endpoint_not_https` | URL scheme is not `https` | Webhook endpoints must terminate TLS |
| `endpoint_unreachable_class` | URL resolves to a private or loopback address | Expose the endpoint publicly or via a tunnel |
| `subscription_limit` | Topic already has 50 subscriptions | Consolidate consumers behind one endpoint |

## List deliveries

**`GET /deliveries`**

Returns delivery records, newest first, with every attempt embedded. This is the primary debugging surface: one query answers what was sent, when, and what the endpoint said.

### Query parameters

| Parameter | Type | Notes |
|---|---|---|
| `event_id` | string | All deliveries of one event |
| `subscription_id` | string | All deliveries to one subscription |
| `status` | string | `pending`, `succeeded`, `failed`, `dead_lettered` |
| `limit` / `cursor` | int / string | Pagination; `limit` max 100, default 25 |

### Example

```bash
curl "https://api.signalhop.example/v1/deliveries?event_id=evt_3fa8" \
  -H "Authorization: Bearer sh_live_4f8a..."
```

```json
{
  "data": [
    {
      "id": "dlv_a91f",
      "event_id": "evt_3fa8",
      "subscription_id": "sub_7c21",
      "status": "failed",
      "next_attempt_at": "2026-07-02T09:25:04Z",
      "attempts": [
        {"at": "2026-07-02T09:15:05Z", "response_status": 500, "response_body": "Internal Server Error"},
        {"at": "2026-07-02T09:15:35Z", "response_status": null, "error": "timeout after 10s"}
      ]
    }
  ],
  "next_cursor": null
}
```

A `response_status` of `null` means the attempt never got an HTTP response — timeout, TLS failure, or connection refused; the `error` field says which.

## Replay a delivery

**`POST /deliveries/{id}/replay`**

Re-sends a `dead_lettered` or `failed` delivery immediately, outside the retry schedule. Returns `202` and resets the attempt counter for one fresh attempt; it does not restart the whole 10-attempt schedule.

Replaying a delivery whose original event has expired (older than 7 days) returns `404` with code `event_expired`. Replaying one that is still `pending` returns `409` — the scheduler already owns it.

```bash
curl -X POST https://api.signalhop.example/v1/deliveries/dlv_a91f/replay \
  -H "Authorization: Bearer sh_live_4f8a..."
```

Replay is per-delivery and manual by design. Bulk recovery after a long outage is usually better served by letting the retry schedule drain naturally; replay is for the handful of dead-lettered stragglers afterwards.
