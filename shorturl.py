"""Minimaler In-Memory URL-Shortener."""

import random
import string
import time

_store = {}


def _generate_code(length: int = 6) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def shorten_url(long_url: str, ttl_seconds: int = 86400, code_length: int = 8) -> str:
    """Erzeugt einen Kurzcode fuer long_url mit Ablaufzeit ttl_seconds."""
    code = _generate_code(code_length)
    _store[code] = {"url": long_url, "expires_at": time.time() + ttl_seconds}
    return code


def resolve_url(code: str) -> str | None:
    """Loest einen Kurzcode auf. Gibt None zurueck, wenn unbekannt oder abgelaufen."""
    entry = _store.get(code)
    if not entry:
        return None
    if entry["expires_at"] < time.time():
        del _store[code]
        return None
    return entry["url"]


def delete_url(code: str) -> bool:
    """Loescht einen Kurzcode vorzeitig. Gibt True zurueck, wenn er existierte."""
    return _store.pop(code, None) is not None
