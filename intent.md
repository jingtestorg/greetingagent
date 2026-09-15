# Hello World Greeting Agent

Simple AI agent that greets users by name.

## Business challenge

Build a hello world AI agent that demonstrates the agent framework capability by greeting users by name, serving as a reusable template for future agent development.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Demo error rate | — | 0 errors | Demo day | AI Agent capability demonstration | user |
| Greeting response time | — | < 1 second | — | User interaction | user |
| Reusability | — | Template adopted by team | — | Agent development framework | user |

## Key Milestones

1. **Agent scaffolded** — Python agent project created with A2A protocol structure
2. **Greeting tool implemented** — Agent can accept a name and return a personalized greeting
3. **Agent tested** — Unit tests pass with zero errors
4. **Agent deployed** — Agent is running and accessible via A2A endpoint
5. **Demo ready** — End-to-end greeting verified with sub-second response

## Business Architecture (RBA)

### End-to-End Process

Lead to Cash (generic)

### Process Hierarchy

```
Lead to Cash
└── Manage Customers and Channels (generic)
    └── Manage customers (generic) [BPS-370]
        └── Manage customer experience
```

### Summary

A hello world greeting agent maps to the Lead to Cash E2E process under "Manage customers", as its core function is personalized user engagement and interaction.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Data Product ORD ID | Gap? | Notes / assumptions |
| ---------------------- | ----------------------- | ---------- | ----------------- | ------------------ | ------------------- | ---- | ------------------- |
| Personalized user greeting | No standard SAP product covers this | — | — | — | — | Yes | Custom AI agent required |
| Agent framework / runtime | SAP AI Core | — | — | — | — | No | Platform available |

### Key findings
- No standard SAP product provides a hello world greeting agent out of the box
- Custom Python AI agent (A2A protocol) is the right approach
- No external API integration required — agent is self-contained
- SAP Build platform provides the deployment runtime
- Solution serves as a reusable template for future agent development

## Recommendations

### Hello World Greeting Agent

#### Executive Summary

Lightweight Python A2A agent that greets users by name for demo and template use.

#### Recommended Solution

A pro-code Python AI agent following the A2A protocol. The agent exposes a greeting tool that accepts a user name and returns a personalized greeting message. It includes OpenTelemetry instrumentation and unit tests, making it a reusable template.

#### Recommended solution category

AI Agent

#### Intent fit
95%
