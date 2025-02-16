"""Provides locale support using Fluent.

Loads all .ftl files from locales/<locale> directory and exposes a translator function.
"""

from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Protocol

from fluent.runtime import FluentBundle, FluentResource


class Translator(Protocol):
    def __call__(self, key: str, **kwargs: Any) -> str: ...


class FluentWrapper:
    """Wrapper around FluentBundle for convenient string formatting."""

    def __init__(self, bundle: FluentBundle) -> None:
        self.bundle = bundle
        self.locale_str = str(bundle.locales[0])

    def __call__(self, key: str, **kwargs: Any) -> str:
        """Retrieve a localized string for the given key, formatting with kwargs.

        Args:
            key: The message id.
            **kwargs: Values to substitute in the message.

        Returns:
            The localized string, or the key if not found.
        """
        if not self.bundle.has_message(key):
            return key
        message = self.bundle.get_message(key)
        if message.value:
            pattern, errors = self.bundle.format_pattern(message.value, kwargs)
            return pattern if isinstance(pattern, str) else key
        return key


@lru_cache(maxsize=10)
def create_fluent_wrapper(locale: Optional[str] = None) -> Translator:
    """Creates a cached FluentWrapper instance for the specified locale.

    Loads all .ftl files from the locale directory and combines them into a single bundle.

    Args:
        locale: Locale identifier (e.g., "en_US"). Defaults to "en_US" if not provided.

    Returns:
        A FluentWrapper instance.
    """
    if locale is None:
        locale = "en_US"
    bundle = FluentBundle([locale])
    locale_dir = Path("locales") / locale
    if locale_dir.is_dir():
        for file_path in locale_dir.glob("*.ftl"):
            resource = FluentResource(file_path.read_text(encoding="utf-8"))
            bundle.add_resource(resource)
    return FluentWrapper(bundle)
