# Architecture Documentation Rules

## Purpose

Document the product architecture clearly enough for architects, developers, and platform teams to understand system behavior.

## Required architecture topics

- System context
- Component responsibilities
- Runtime flow
- Data flow
- Integration points
- Security model
- Deployment model when known
- Failure handling
- Observability
- Scalability considerations
- Technical decisions
- Known limitations

## Component table

```md
| Component | Responsibility | Inputs | Outputs | Dependencies | Failure Mode |
|---|---|---|---|---|---|
```

## Runtime flow format

```md
## Runtime Flow

1. The request enters through ...
2. The system validates ...
3. The orchestration layer ...
4. The component ...
5. The response is returned ...
```

## Diagrams

Produce diagrams, do not merely recommend them. For any architecture document, generate Mermaid source for at least the runtime flow (sequence diagram) and the component relationships (flowchart); add data-flow, deployment, or state diagrams when the product calls for them.

```mermaid
sequenceDiagram
    participant P as Publisher
    participant S as Signalhop API
    participant Q as Delivery Scheduler
    participant E as Subscriber Endpoint
    P->>S: POST /events
    S-->>P: 202 (event stored)
    S->>Q: enqueue deliveries per subscription
    Q->>E: POST payload (signed)
    alt 2xx within 10 s
        E-->>Q: 200
    else failure or timeout
        Q->>Q: schedule retry (backoff)
    end
```

Rules:

- Keep the Mermaid source in the Markdown next to the section it illustrates, so it stays editable and diffable.
- A diagram shows what prose states; the surrounding text must still describe the flow. Readers of formats that strip diagrams lose nothing essential.
- For output formats that cannot render Mermaid (DOCX, PDF), render to PNG/SVG during Phase 10 — `output-formats/SKILL.md` covers the tooling.
- Do not claim that a diagram exists unless it was provided or generated, and do not diagram architecture the user never described: a diagram of an assumed design is an assumption and must be labeled as one.
