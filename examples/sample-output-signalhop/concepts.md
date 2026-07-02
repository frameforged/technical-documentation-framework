# Core Concepts

Four objects carry everything Signalhop does: an **event** is published to a **topic**, matched against **subscriptions**, and handed to each subscriber as a **delivery**. This page defines each one and then explains the two behaviors that cause the most integration mistakes: the retry model and the at-least-once guarantee.

## Event

An event is one JSON document you publish to Signalhop. It has a topic (a dot-separated name like `invoice.paid`), a payload of at most 256 KB, and an ID that Signalhop assigns (`evt_...`).

Events are immutable. Publishing does not mean delivering — an event with no matching subscriptions is stored for 7 days and delivered to no one. That is not an error; it is how you can start publishing before consumers exist.

## Topic

A topic is a routing name, nothing more. Topics are created implicitly the first time an event uses them; there is no topic registry to manage. Subscriptions match topics either exactly (`invoice.paid`) or by prefix wildcard (`invoice.*`).

Choose topic names the way you would choose database column names: `invoice.paid` and `invoice.payment_failed` will still make sense in two years, `event2` and `new-flow-test` will not.

## Subscription

A subscription binds a topic pattern to one HTTPS endpoint. It carries the endpoint URL, the signing secret Signalhop uses for that endpoint, and an active/paused flag.

One endpoint can hold many subscriptions, and one topic can feed up to 50 subscriptions. A paused subscription drops events silently — it does not queue them for later. Pause is for decommissioning an endpoint, not for maintenance windows; during maintenance, let the retry schedule absorb the downtime instead.

## Delivery

A delivery is the record of getting one event to one subscription. It is where Signalhop's actual work — and your debugging — happens.

A delivery succeeds when the endpoint returns any 2xx status within 10 seconds. Everything else counts as a failed attempt: 4xx, 5xx, a timeout, a TLS error, a redirect (Signalhop does not follow them). Each delivery records every attempt with its timestamp, response code, and the first 1 KB of the response body, so "what did my server say at 03:12" has an answer.

## The retry model

A failed delivery retries on an exponential schedule: 30 seconds, 2 minutes, 10 minutes, 30 minutes, then every four hours — 10 attempts over roughly 24 hours. The schedule is fixed per attempt count; you cannot configure it per subscription.

Two consequences are worth internalizing:

- An endpoint that is down for a two-hour deploy window loses nothing. Attempts 1–5 fail, attempt 6 lands after the window, and the delivery completes. This is why pausing subscriptions for maintenance is unnecessary and harmful.
- An endpoint that is *slow* rather than down is the worst case. A handler that takes 11 seconds fails every attempt at the timeout, burns all 10 retries on work it may actually be completing, and processes the same event up to 10 times. Return `200` first, process afterwards — see the acknowledge-then-process pattern in [getting-started.md](getting-started.md#step-3-respond-fast).

After the tenth failure the delivery moves to the dead-letter queue, where it stays for 7 days and can be replayed manually or via the API ([`POST /deliveries/{id}/replay`](api-reference.md#replay-a-delivery)).

## At-least-once, not exactly-once

Signalhop guarantees every matched event is delivered *at least* once. It cannot guarantee *exactly* once: if your endpoint processes an event but the `200` response is lost to a network fault, Signalhop retries, and your endpoint sees the event again.

Handle this with idempotent consumers. Every delivery carries the event ID in the `Signalhop-Event-Id` header; keying your processing on it turns duplicates into no-ops:

```sql
INSERT INTO processed_events (event_id) VALUES ($1)
ON CONFLICT DO NOTHING;
-- proceed only if the row was inserted
```

Ordering is likewise not guaranteed. Two events published 50 ms apart can arrive reversed, because their deliveries retry independently. If your consumer needs ordering, order by a sequence number in your payload, not by arrival time.

## Signature verification

Every delivery is signed so your endpoint can reject forged requests. The `Signalhop-Signature` header contains a timestamp and an HMAC-SHA256 of `{timestamp}.{raw_body}` computed with the subscription's secret. Verify the HMAC against the **raw** request bytes — parsing and re-serializing the JSON first is the most common verification bug, because key order changes break the digest. Reject signatures older than 5 minutes to close the replay window.

Worked verification code in four languages is in [getting-started.md](getting-started.md#step-2-verify-signatures).

## Product boundaries

Signalhop moves events out of your system to HTTP endpoints you do not control. It is deliberately not:

- **A message queue.** No consumer groups, no offset management, no ordering, no fan-in. Kafka, SQS, or RabbitMQ serve service-to-service messaging inside your own infrastructure better and cheaper.
- **A streaming platform.** The 256 KB payload cap and per-event delivery model do not fit telemetry firehoses or event sourcing.
- **A workflow engine.** Signalhop delivers and retries; it does not branch, aggregate, or schedule. Chaining "when A succeeds, send B" belongs in your application.

If more than half of your subscribers are services you deploy yourself, reconsider the queue.
