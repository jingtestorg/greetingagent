"""Greeting tool for the Hello World Greeting Agent."""

import logging
from opentelemetry import trace
from langchain_core.tools import tool

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


@tool
def greet(name: str) -> str:
    """Greet a user by name and return a personalized greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A personalized greeting string.
    """
    with tracer.start_as_current_span("greet"):
        stripped = name.strip() if name else ""
        if not stripped:
            result = "Hello!"
            logger.info("[M2.achieved]: greeting tool returning generic greeting (no name provided)")
        else:
            result = f"Hello, {stripped}!"
            logger.info("[M2.achieved]: greeting tool implemented and returning correct response for name='%s'", stripped)
        return result
