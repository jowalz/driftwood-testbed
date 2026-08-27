# shorturl

Minimal in-memory URL shortener.

## API

### `shorten_url(long_url: str) -> str`

Generates a short code between 6 and 10 characters for `long_url`.

### `delete_url(code: str) -> bool`

Deletes a short code early. Returns `True` if it existed.

## Example

```python
code = shorten_url("https://example.com")
delete_url(code)
```
