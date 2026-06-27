Here's an interactive reference widget for the `requests` module, covering GET, POST, PATCH, and DELETE with real, runnable-style examples:Click through each tab for the full code. Here's a quick mental model for when to use each method:

| Method | Purpose | Has body? | Idempotent? |
|--------|---------|-----------|-------------|
| `GET` | Read / fetch | No | Yes |
| `POST` | Create new | Yes | No |
| `PATCH` | Partial update | Yes | Usually |
| `DELETE` | Remove | Rarely | Yes |

**Three things to always include:**

- `timeout=10` — prevents your program hanging forever if the server goes silent
- `response.raise_for_status()` — turns 4xx/5xx into a Python exception instead of silently succeeding
- A `requests.Session()` when making multiple calls to the same host — it reuses the TCP connection and lets you set shared headers once

Install the library with `pip install requests` if you haven't already.
