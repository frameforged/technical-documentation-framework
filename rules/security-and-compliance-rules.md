# Security and Compliance Rules

## Purpose

Ensure technical documentation addresses security, privacy, authorization, auditability, and compliance-sensitive behavior when relevant.

## Required topics when applicable

- Authentication
- Authorization
- Role-based access control
- Data classification
- Sensitive data handling
- Audit logging
- Trace redaction
- Tool execution permissions
- Secret management
- Network boundaries
- Encryption
- Retention policy
- Compliance constraints

## Security documentation pattern

```md
## Security Model

### Authentication

### Authorization

### Data Access

### Sensitive Data Handling

### Audit and Traceability

### Known Security Boundaries

### Recommended Operational Controls
```

## AI-specific security notes

When documenting AI or agentic systems, consider:

- Prompt injection risks
- Unauthorized tool execution
- Sensitive data leakage through memory
- Unsafe long-term memory writes
- Excessive trace visibility
- Human approval requirements for high-impact actions
- Guardrail placement across input, planning, execution, and output

## No unsupported compliance claims

Do not state that a product is compliant with a regulation or standard unless the user provides that fact.

Use:

> The product may need additional controls for GDPR, PCI DSS, HIPAA, or internal compliance requirements depending on deployment context.
