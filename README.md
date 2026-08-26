# shorturl

Minimal in-memory URL shortener.

## API

### `shorten_url(long_url: str) -> str`

Generates a 6-character short code for `long_url`. Links expire after 1 hour.

### `resolve_url(code: str) -> str`

Resolves a short code to the original URL. Raises `KeyError` if the code is unknown or expired.

## Example

```python
code = shorten_url("https://example.com")
resolve_url(code)  # "https://example.com"
```
