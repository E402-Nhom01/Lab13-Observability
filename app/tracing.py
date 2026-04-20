from __future__ import annotations

import os
from typing import Any
import contextlib

try:
    from langfuse import get_client, observe, propagate_attributes
except ImportError:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    @contextlib.contextmanager
    def propagate_attributes(**kwargs: Any):
        yield

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    langfuse_context = _DummyContext()
else:
    class _LangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            pass # Removed in Langfuse 4; trace attributes handled by propagate_attributes.

        def update_current_observation(self, **kwargs: Any) -> None:
            client = get_client()
            if hasattr(client, "update_current_generation"):
                client.update_current_generation(
                    metadata=kwargs.get("metadata"),
                    usage_details=kwargs.get("usage_details"),
                )

    langfuse_context = _LangfuseContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
