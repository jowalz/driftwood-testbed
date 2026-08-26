# shorturl

Minimaler In-Memory URL-Shortener.

## API

### `shorten_url(long_url: str) -> str`

Erzeugt einen 6-stelligen Kurzcode für `long_url`. Links laufen nach 1 Stunde ab.

### `resolve_url(code: str) -> str`

Löst einen Kurzcode zur Original-URL auf. Wirft `KeyError`, wenn der Code unbekannt oder abgelaufen ist.

## Beispiel

```python
code = shorten_url("https://example.com")
resolve_url(code)  # "https://example.com"
```
