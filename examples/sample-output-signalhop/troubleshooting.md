# Troubleshooting

Start every investigation at the delivery log, not at your application log: `GET /v1/deliveries?event_id=...` (or the Deliveries tab in the dashboard) shows each attempt with its timestamp, response status, and the first 1 KB of your server's response. Most problems identify themselves there. The entries below map the common signatures to causes.

## No delivery record exists at all

**Symptom:** The event was published (`202`, an `evt_` ID came back) but `GET /deliveries?event_id=...` returns an empty list.

**Cause:** No active subscription matched the topic at publish time. The two usual reasons: the subscription is paused (paused subscriptions drop events, they do not queue them), or the topic differs from the pattern — `invoice.payed` vs `invoice.paid` is the classic.

**Fix:** Compare the event's `topic` with `GET /subscriptions` output character by character, and check the `status` field. Note that `matched_subscriptions` in the publish response already told you this was coming: treat `0` as an alert condition in your publisher.

## Every attempt fails with 401

**Symptom:** Attempts reach your endpoint; your endpoint rejects them all as unauthorized.

**Cause:** Signature verification is failing. In order of frequency: the handler hashes parsed-and-reserialized JSON instead of the raw body; the secret in your config belongs to a different subscription (each subscription has its own); the secret is from the other mode (test vs live).

**Fix:** Log the received `Signalhop-Signature` header and your computed digest side by side for one request. If they differ, hash the raw bytes (see [getting-started.md](getting-started.md#step-2-verify-signatures)). If they match but verification still fails, your timestamp tolerance is rejecting — check for clock skew on the host; NTP drift beyond 5 minutes fails the replay check.

## Attempts time out although the endpoint works

**Symptom:** Attempts show `"error": "timeout after 10s"`, but hitting the endpoint manually responds fine.

**Cause:** The handler does real work before responding, and under webhook load that work exceeds 10 seconds — while your manual test, alone on an idle server, stays under it. Cold starts on serverless platforms produce the same signature: the first attempt after an idle period times out, the retry 30 seconds later succeeds.

**Fix:** Acknowledge first, process after ([getting-started.md](getting-started.md#step-3-respond-fast)). For cold starts, either keep the function warm or accept that attempt 1 fails and attempt 2 lands — the retry schedule exists for exactly this, but your consumer must be idempotent since the timed-out attempt may still have executed.

## The same event arrives more than once

**Symptom:** Your handler processed one event two or more times.

**Cause:** Not a bug. Delivery is at-least-once: any lost `200` — network fault, deploy restart mid-response, load balancer timeout — triggers a retry of an event you already processed.

**Fix:** Idempotent consumption, keyed on `Signalhop-Event-Id`. The pattern is three lines of SQL ([concepts.md](concepts.md#at-least-once-not-exactly-once)). If duplicates are frequent rather than occasional, something on your side is also failing to respond in time — check for the timeout signature above.

## Deliveries dead-letter during a known outage

**Symptom:** Your endpoint was down longer than a day; deliveries show `dead_lettered`.

**Cause:** The retry schedule spans roughly 24 hours. Outages longer than that exhaust all 10 attempts.

**Fix:** Dead-lettered deliveries are held for 7 days. Replay them once the endpoint is stable: list with `GET /deliveries?status=dead_lettered`, then `POST /deliveries/{id}/replay` for each. Replay grants one fresh attempt per call, so script the loop with a check on the result rather than firing all replays blind.

## TLS errors on every attempt

**Symptom:** Attempts show `"error": "tls handshake failed"`, with `response_status: null`.

**Cause:** Signalhop validates certificates strictly. Self-signed certificates, expired chains, and missing intermediates all fail — even when browsers, which cache intermediates, still show the site as fine.

**Fix:** Test with `openssl s_client -connect yourhost:443 -servername yourhost` from a fresh machine and fix what it reports. Certificate exceptions cannot be configured; the signing model assumes an untampered channel.

## Still stuck

Collect three identifiers before contacting support@signalhop.example: the event ID, the delivery ID, and the `request_id` from any API error you received. With those, support can trace the exact path; without them, the first reply will be a request for them.
