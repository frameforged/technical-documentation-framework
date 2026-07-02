# Getting Started

This walkthrough takes you from an API key to a verified, signed webhook landing on your server. Budget about fifteen minutes; the only prerequisites are a publicly reachable HTTPS endpoint and any language that can compute an HMAC.

Test keys (`sh_test_...`) and live keys (`sh_live_...`) hit the same API but separate data. Everything below uses test mode; nothing you create here touches production traffic.

## Step 1: Create a subscription

Point a subscription at your endpoint and choose which topics it should receive:

```bash
curl https://api.signalhop.example/v1/subscriptions \
  -H "Authorization: Bearer sh_test_4f8a..." \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "invoice.*",
    "endpoint_url": "https://example.dev/webhooks/signalhop"
  }'
```

The response contains two values you must store:

```json
{
  "id": "sub_7c21",
  "topic": "invoice.*",
  "endpoint_url": "https://example.dev/webhooks/signalhop",
  "secret": "whsec_9k2m...",
  "status": "active"
}
```

The `secret` is shown **only in this response**. It is per-subscription, and your endpoint needs it to verify signatures. Treat it like a password: environment variable or secret store, never source control.

## Step 2: Verify signatures

Every delivery carries a `Signalhop-Signature` header:

```text
Signalhop-Signature: t=1719912345,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e77a0e56ff536d0ce8e108d8bd
```

`t` is a Unix timestamp; `v1` is HMAC-SHA256 of the string `{t}.{raw_body}` using your subscription secret. Verification in Python:

```python
import hashlib, hmac, time

def verify(raw_body: bytes, header: str, secret: str) -> bool:
    parts = dict(p.split("=", 1) for p in header.split(","))
    if abs(time.time() - int(parts["t"])) > 300:
        return False  # older than 5 minutes: possible replay
    signed = f"{parts['t']}.".encode() + raw_body
    expected = hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, parts["v1"])
```

Two rules keep this correct:

1. **Hash the raw request bytes.** If your framework parses JSON before your handler runs, get the original body back (`request.get_data()` in Flask, `express.raw()` middleware in Express). Re-serialized JSON reorders keys and the digest will not match.
2. **Use a constant-time comparison** (`hmac.compare_digest`, not `==`) so response timing leaks nothing about the expected value.

Reject anything that fails verification with a `401` — those requests did not come from Signalhop.

## Step 3: Respond fast

Signalhop marks a delivery successful only if your endpoint returns 2xx within 10 seconds. Do not spend that budget doing real work:

```python
@app.post("/webhooks/signalhop")
def receive():
    if not verify(request.get_data(), request.headers["Signalhop-Signature"], SECRET):
        return "", 401
    queue.enqueue(process_event, request.get_json())  # hand off
    return "", 200                                    # acknowledge immediately
```

The acknowledge-then-process pattern matters more than it looks. A handler that processes inline and takes 11 seconds fails at the timeout on every attempt — so Signalhop retries an event your server may have already processed, up to 10 times. Enqueue first, return `200`, process from the queue.

Because delivery is at-least-once, `process_event` must also be idempotent; keying on the `Signalhop-Event-Id` header is the standard approach ([concepts.md](concepts.md#at-least-once-not-exactly-once) shows the SQL).

## Step 4: Publish a test event

```bash
curl https://api.signalhop.example/v1/events \
  -H "Authorization: Bearer sh_test_4f8a..." \
  -H "Content-Type: application/json" \
  -d '{"topic": "invoice.paid", "payload": {"invoice_id": "inv_991", "amount_cents": 12900}}'
```

Within a few seconds your endpoint receives:

```http
POST /webhooks/signalhop HTTP/1.1
Signalhop-Event-Id: evt_3fa8
Signalhop-Topic: invoice.paid
Signalhop-Signature: t=1719912345,v1=5257a869...

{"invoice_id": "inv_991", "amount_cents": 12900}
```

If nothing arrives, the delivery log has the answer before you start guessing: `GET /v1/deliveries?event_id=evt_3fa8` shows every attempt with its response code. The three most common first-run failures — `401` from signature bugs, timeouts from slow handlers, and TLS errors from self-signed certificates — are worked through in [troubleshooting.md](troubleshooting.md).

## Going to production

Swap the test key for a live key and re-create your subscriptions in live mode — subscriptions do not carry over between modes, which prevents a test publish from ever reaching a production endpoint. Before switching, confirm three things: your secret storage holds the *live* subscription secrets, your endpoint's p95 response time is comfortably under 10 seconds, and your consumer is idempotent under a deliberately duplicated event (replay one from the dashboard to test this).
