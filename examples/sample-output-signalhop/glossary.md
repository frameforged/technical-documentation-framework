# Glossary

Terms are ordered by how early you meet them, not alphabetically — read top to bottom and each entry builds on the ones before it.

### Event

**Short definition:**
One immutable JSON document published to Signalhop for distribution.

**Meaning in this product:**
An event is what you publish: a topic name plus a payload of up to 256 KB. Signalhop assigns it an ID (`evt_...`) and stores it for 7 days. Publishing and delivering are separate acts — an event with no matching subscriptions is stored and delivered to no one.

**Example:**
`{"topic": "invoice.paid", "payload": {"invoice_id": "inv_991"}}` becomes event `evt_3fa8`.

**Common confusion:**
An event is not a delivery. One event produces zero or more deliveries, one per matched subscription.

**Related terms:** Topic, Delivery, Payload.

### Topic

**Short definition:**
A dot-separated routing name that connects events to subscriptions.

**Meaning in this product:**
Topics exist implicitly — the first event that uses a name creates it. Subscriptions match exactly (`invoice.paid`) or by prefix wildcard (`invoice.*`). Topic strings are limited to lowercase letters, digits, underscores, and dots.

**Example:**
`invoice.paid`, `invoice.payment_failed`, and a subscription on `invoice.*` receiving both.

**Common confusion:**
A topic is not a queue. It holds nothing and has no state; it is only a name that matching runs against at publish time.

**Related terms:** Event, Subscription.

### Subscription

**Short definition:**
A binding between a topic pattern and one HTTPS endpoint, with its own signing secret.

**Meaning in this product:**
Subscriptions decide who receives what. Each carries an endpoint URL, a secret used to sign deliveries to that endpoint, and a status. A paused subscription drops matched events silently rather than queuing them.

**Example:**
`sub_7c21` subscribes `https://example.com/hooks` to `invoice.*`.

**Common confusion:**
Pausing is not a maintenance mode. During endpoint downtime, leave the subscription active and let retries absorb the gap; pause only when decommissioning.

**Related terms:** Topic, Delivery, Signing secret.

### Delivery

**Short definition:**
The record of transporting one event to one subscription, including every attempt.

**Meaning in this product:**
The delivery is the unit of retry and the unit of debugging. It succeeds on the first 2xx response within 10 seconds and otherwise retries up to 10 times over about 24 hours, recording each attempt's timestamp, status code, and response excerpt.

**Example:**
Event `evt_3fa8` matched three subscriptions, producing deliveries `dlv_a91f`, `dlv_a920`, `dlv_a921` — each retrying independently.

**Common confusion:**
A delivery is not an attempt. One delivery contains up to 10 attempts; "the webhook failed" usually means "attempt 3 of delivery X failed", which the log distinguishes.

**Related terms:** Event, Subscription, Dead-letter queue, At-least-once.

### At-least-once

**Short definition:**
The guarantee that every matched event is delivered one or more times — with duplicates possible, exactly-once not promised.

**Meaning in this product:**
Any lost success response triggers a retry of an event the endpoint may already have processed. Consumers are expected to be idempotent, keyed on the `Signalhop-Event-Id` header.

**Example:**
An endpoint processes `evt_3fa8`, but the `200` is lost to a network fault; attempt 2 delivers the same event 30 seconds later, and the idempotency key turns it into a no-op.

**Common confusion:**
At-least-once also does not imply ordering. Deliveries retry independently, so later events can arrive first.

**Related terms:** Delivery, Idempotency, Replay.

### Idempotency

**Short definition:**
The property that processing the same input twice has the same effect as processing it once.

**Meaning in this product:**
Idempotency appears on both sides of Signalhop. Consumers deduplicate deliveries by event ID; publishers can pass an `idempotency_key` so that retrying a publish call cannot create a second event.

**Example:**
`INSERT ... ON CONFLICT DO NOTHING` on the event ID before processing.

**Common confusion:**
The publisher-side `idempotency_key` and the consumer-side event ID solve different duplications — a duplicate *publish* versus a duplicate *delivery*. Robust integrations use both.

**Related terms:** At-least-once, Event.

### Dead-letter queue

**Short definition:**
Storage for deliveries that exhausted all retry attempts.

**Meaning in this product:**
After the tenth failed attempt a delivery moves to status `dead_lettered` and is held for 7 days, during which it can be replayed. After 7 days the underlying event expires and the delivery is unrecoverable.

**Example:**
A 30-hour endpoint outage dead-letters the deliveries from its first few hours; a scripted replay recovers them afterwards.

**Common confusion:**
Dead-lettered does not mean deleted — for 7 days it is a recoverable state, and treating it as an alertable condition rather than a silent one is the operational best practice.

**Related terms:** Delivery, Replay.

### Replay

**Short definition:**
Manually re-sending a failed or dead-lettered delivery outside the retry schedule.

**Meaning in this product:**
`POST /deliveries/{id}/replay` grants the delivery one fresh attempt immediately. It does not restart the 10-attempt schedule, and it conflicts (`409`) with deliveries the scheduler still owns.

**Example:**
Replaying the stragglers after an outage that outlasted the retry window.

**Common confusion:**
Replay re-sends an existing delivery; publishing the event again creates a *new* event with a new ID, which defeats consumer-side deduplication.

**Related terms:** Dead-letter queue, Delivery.

### Signing secret

**Short definition:**
The per-subscription key used to authenticate deliveries via HMAC-SHA256.

**Meaning in this product:**
Each subscription gets its own secret (`whsec_...`), returned only once, at creation. Deliveries carry a `Signalhop-Signature` header computed over a timestamp and the raw body; endpoints verify it and reject the rest.

**Example:**
`t=1719912345,v1=5257a869...` verified against the raw request bytes.

**Common confusion:**
The signing secret is not the API key. The API key (`sh_live_...`) authenticates *you* to Signalhop; the signing secret authenticates *Signalhop* to your endpoint.

**Related terms:** Subscription, Delivery.
