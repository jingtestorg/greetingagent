# Specification: hello-world-greeting-agent

> **Guidelines**: Read [../guidelines.md](../guidelines.md) and [../guidelines-agent.md](../guidelines-agent.md) before executing ANY tasks below.
> **Python Guidelines**: Read [../guidelines-agent-python.md](../guidelines-agent-python.md) for Python-specific patterns.
> **MCP Guidelines**: Read [../guidelines-agent-mcp.md](../guidelines-agent-mcp.md) for MCP patterns.

Asset path: `assets/hello-world-greeting-agent/`

Check off items as completed.

## Setup

- [x] Invoke `setup-solution` skill to scaffold `solution.yaml` and `assets/hello-world-greeting-agent/asset.yaml`
- [x] Invoke `agent` skill bootstrap from `assets/hello-world-greeting-agent/` to scaffold the Python A2A project structure

## Greeting Tool (R1)

- [x] Create `assets/hello-world-greeting-agent/app/tools/greet.py` with a `greet` tool function:
  - Accepts `name: str` parameter
  - Returns `f"Hello, {name}!"` string
  - Includes input validation: if `name` is empty/blank, return `"Hello!"`
  - Docstring clearly describes the tool purpose

## Agent Configuration (R2 — A2A Protocol)

- [x] Configure agent card in `assets/hello-world-greeting-agent/app/agent.py`:
  - Agent name: `hello-world-greeting-agent`
  - Description: `A simple greeting agent that greets users by name`
  - Register the `greet` tool with the agent
- [x] Ensure `/.well-known/agent.json` is served and returns correct agent card
- [x] Add `@agent_model` decorator for primary model (gpt-4o or equivalent via LiteLLM)
- [x] Add `@agent_model` decorator for fallback model
- [x] Add `@agent_config` decorator for temperature
- [x] Add `@agent_config` decorator for agent memory TTL
- [x] Add `@prompt_section` decorator with system prompt:
  - Instructs agent to use the `greet` tool when user provides a name
  - Never fabricate or hallucinate responses
  - Fallback to generic greeting if no name provided

## Business Step Instrumentation (Milestones)

- [x] Instrument `app/agent.py` or `app/tools/greet.py` with structured logging for all milestones:
  - `M1.achieved`: agent scaffolded and A2A server started successfully
  - `M1.missed`: agent scaffolding failed — check project structure
  - `M2.achieved`: greeting tool implemented and returning correct response
  - `M2.missed`: greeting tool not returning expected response
  - `M3.achieved`: all unit tests passed
  - `M3.missed`: one or more unit tests failed
  - `M4.achieved`: agent deployed and A2A endpoint responding
  - `M4.missed`: agent deployment failed or endpoint unreachable
  - `M5.achieved`: demo-ready — greeting response under 1 second
  - `M5.missed`: response time exceeded 1 second threshold
- [x] Add OpenTelemetry span for the `greet` tool execution using `@tracer.start_as_current_span("greet")` or context manager form (NOT inside async generators)
- [x] Verify instrumentation: `grep -r "M[0-9]\.achieved" assets/hello-world-greeting-agent/app/` must return results

## Tests (R3)

- [x] Create `assets/hello-world-greeting-agent/tests/test_greet_tool.py`:
  - Test: `greet("Alice")` returns `"Hello, Alice!"`
  - Test: `greet("")` returns `"Hello!"`
  - Test: `greet("  ")` (whitespace-only) returns `"Hello!"`
- [x] Create `assets/hello-world-greeting-agent/tests/test_agent_integration.py`:
  - End-to-end test: send a greeting request through the agent graph
  - Mock the LLM (ChatLiteLLM) to return a canned response
  - Assert agent returns a greeting string containing the provided name
- [x] Run tests: `cd assets/hello-world-greeting-agent && pytest`
- [x] Verify coverage ≥ 70% (achieved: 75%)
- [x] Confirm `test_report.json` is generated

## Validation

- [x] `grep -r "M[0-9]\.achieved" assets/hello-world-greeting-agent/app/` — must return results ✓
- [x] `grep -r "sap_cloud_sdk.agent_decorators" assets/hello-world-greeting-agent/app/` — must return results ✓
- [x] `grep -c "^@agent_model\|^@agent_config\|^@prompt_section" assets/hello-world-greeting-agent/app/agent.py` — 10 decorators ✓
- [x] `ls assets/hello-world-greeting-agent/test_report.json` — exists ✓
