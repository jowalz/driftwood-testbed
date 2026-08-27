"""Minimal in-memory URL shortener."""

import random
import string
import time

_store = {}


def _generate_code(length: int = 6) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def shorten_url(long_url: str, ttl_seconds: int = 86400, min_length: int = 6, max_length: int = 10) -> str:
    """Generates a short code for long_url with expiry ttl_seconds."""
    code = _generate_code(random.randint(min_length, max_length))
    _store[code] = {"url": long_url, "expires_at": time.time() + ttl_seconds}
    return code


def resolve_url(code: str) -> str | None:
    """Resolves a short code. Returns None if unknown or expired."""
    entry = _store.get(code)
    if not entry:
        return None
    if entry["expires_at"] < time.time():
        del _store[code]
        return None
    return entry["url"]


def delete_url(code: str) -> bool:
    """Deletes a short code early. Returns True if it existed."""
    return _store.pop(code, None) is not None
