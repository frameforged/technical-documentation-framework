# Signalhop

> This package is a reference output of the Technical Documentation Framework. Signalhop is a fictional product; every fact in these files was invented for the example. See [examples/README.md](../README.md) for context.

Signalhop delivers webhooks so your application does not have to. You publish an event once; Signalhop signs it, delivers it to every subscribed endpoint, retries the failures for up to 24 hours, and keeps a searchable record of every attempt.

## What it does

Sending a webhook looks trivial — an HTTP POST — until a subscriber's server goes down for an afternoon. Then you need retry queues, backoff schedules, signature verification, dead-letter storage, and a way to answer "did customer X ever receive event Y?". Signalhop packages that operational layer behind one publish call.

## Who it is for

Backend teams that emit events to third-party or customer-owned endpoints: SaaS platforms notifying integrations, payment systems confirming transactions, internal services fanning out domain events. If all your consumers live inside one network and one team, a message queue is usually the better tool — the [product boundaries section of concepts.md](concepts.md#product-boundaries) explains why.

## Quick start

```bash
curl https://api.signalhop.example/v1/events \
  -H "Authorization: Bearer sh_test_4f8a..." \
  -H "Content-Type: application/json" \
  -d '{"topic": "invoice.paid", "payload": {"invoice_id": "inv_991", "amount_cents": 12900}}'
```

Every endpoint subscribed to `invoice.paid` receives the payload within seconds, signed with its own secret. The full walkthrough, including endpoint verification, is in [getting-started.md](getting-started.md).

## Documentation map

| Document | Read it when |
|---|---|
| [getting-started.md](getting-started.md) | You are integrating for the first time |
| [concepts.md](concepts.md) | You need to understand events, subscriptions, deliveries, and the retry model |
| [api-reference.md](api-reference.md) | You are writing code against the REST API |
| [troubleshooting.md](troubleshooting.md) | Deliveries are failing or missing |
| [glossary.md](glossary.md) | A term in these docs is unclear |

## Support

Delivery logs in the dashboard answer most "where is my webhook?" questions; [troubleshooting.md](troubleshooting.md) maps the common failure signatures to causes. Anything else: support@signalhop.example.
