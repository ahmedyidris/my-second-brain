---
title: Jarvis X OpenAI-Compatible API
tags: [jarvis-x, api, openai-compatible, entity, as-built]
sources:
  - raw/2026-09-26-starnet-gateway-and-station-build.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x-runtime]], [[jarvis-x-app]], [[universal-model-layer]], [[aider]], [[starnet]], [[hermes-agent]], [[jarvis-x]], [[jarvis-x-station-view]], [[ollama]], [[groq]], [[gemini]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-starnet-gateway]]
last_updated: 2026-09-26
---

# Jarvis X OpenAI-Compatible API

An adapter in Jarvis's `app.py` that exposes the [[universal-model-layer]] tiers behind the OpenAI chat-completions interface, so OpenAI-compatible clients can talk to [[jarvis-x]]. The handoff names Aider, Continue and StarNet agents as callers (Bug B below). Live as of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]); the repo's latest commit at that point is `99652aa` — feat(api): OpenAI-compatible /v1/chat/completions + /v1/models. Runs as part of the [[jarvis-x-runtime]].

## Endpoints

| Method | URL |
|--------|-----|
| GET | `http://127.0.0.1:8000/v1/models` |
| POST | `http://127.0.0.1:8000/v1/chat/completions` |

`/v1/chat/completions`:

- `model` field accepts: `local | fast | smart | quality | frontier`
- returns OpenAI `chat.completion` shape
- persona loaded from `config/system_prompt.txt` and prepended

The tiers map to providers as listed on [[jarvis-x-runtime]] (local → [[ollama]], fast/smart → [[groq]], quality/frontier → [[gemini]]).

## Implementation (fix 7)

Added `/v1/chat/completions` and `/v1/models` to `app.py`. They are placed BEFORE the SPA wildcard route (`@app.get("/{full_path:path}")`) — otherwise the wildcard catches `GET /v1/models` and serves `index.html`. Implication: that `index.html` is the entry point of Jarvis's React frontend (see [[jarvis-x-app]]).

Imports needed at top of `app.py`:

- `Request` in the fastapi import block
- `import time`
- `JSONResponse` in the `from fastapi.responses` line

Tier → model resolution:

```python
tier_to_model = {
    "local":    "qwen2.5:3b",
    "fast":     "registry:fast",
    "smart":    "registry:smart",
    "quality":  "registry:quality",
    "frontier": "registry:quality",
}
```

Note: `frontier` currently resolves to `registry:quality` in this adapter. Separately, the PART 1 tier table (verified via `POST /api/ask`, not via `/v1`) lists the same model, `gemini-3.6-flash`, for both `quality` and `frontier`. The handoff does not say whether these two facts are connected.

Implication: the `registry:` values appear to feed the `registry:` branch in `hermes.py` (fix 2 on [[hermes-agent]] / [[jarvis-x-runtime]]), which routes to the cloud providers. The handoff names both but does not spell out the call path.

## Test

```bash
curl -s http://127.0.0.1:8000/v1/models | python3 -m json.tool
curl -s -XPOST http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"smart","messages":[{"role":"user","content":"Say ready"}]}' \
  | python3 -m json.tool
```

## Bug B — the endpoint doesn't read files

`POST /v1/chat/completions` with a question about a file returns "I don't have that file" because Jarvis is a chat API. It doesn't read the filesystem.

This is expected behavior. Callers (Aider, Continue, StarNet agents) must read the file themselves and include its content in the message.

Note: the handoff's launch command for [[aider]] points it at `groq/openai/gpt-oss-120b` directly, not at this adapter. The handoff gives no command for pointing Aider at `http://127.0.0.1:8000/v1`.

## Priority 2 — route StarNet through Jarvis

The plan is to point [[starnet]] at this adapter, via its custom-provider support:

- StarNet's launch command already passes `CUSTOM_OPENAI_BASE_URL="http://127.0.0.1:8000/v1"` and `CUSTOM_OPENAI_KEY="sk-jarvis-local"`.
- The handoff's stated goal: "all StarNet traffic goes through Jarvis, which handles fallbacks and never dies on truncation." That is the handoff's claim about Jarvis's behaviour; the handoff does not document a test of the fallback or truncation handling.
- **Blocked by StarNet Bug C:** adding `http://127.0.0.1:8000/v1` as a custom provider in the StarNet UI fails verification, even with a valid key. The env-var path (`CUSTOM_OPENAI_BASE_URL` at launch) may bypass the UI verification if StarNet reads it at boot — not yet confirmed. See [[starnet]].

The handoff does not say whether this adapter checks the bearer key, or what `sk-jarvis-local` is validated against.

## StarNet can't use this endpoint (found 2026-09-26)

Source: `raw/2026-09-26-starnet-gateway-and-station-build.md`, from reading `app.py` and StarNet's adapter.

- **No streaming.** This endpoint returns one JSON `chat.completion` body. StarNet always requests and parses a streamed (SSE) reply, so it reads zero text events.
- **Headers late.** Headers go out only after the whole answer, and StarNet aborts after 30s without them.
- **Conversation lost.** Only the last user message is kept, and the caller's system prompt is replaced with Jarvis's persona.
- **No tools.** `tools` are dropped.

> **Disagreement (2026-09-24 handoff vs 2026-09-26 code reading):** the handoff names StarNet agents as callers of this adapter and makes it the Priority 2 target. As built, it suits Aider- and Continue-style callers that use one prompt and one reply, but not StarNet. The fix built is a separate endpoint, [[jarvis-x-starnet-gateway]] on port 8010, so this adapter stays as it is.

## "Do not re-enable stream: false"

PART 8 of the handoff says: "Do not re-enable stream: false on the OpenAI-compatible adapter. It breaks all providers."

> **Ambiguity:** in context this most likely refers to StarNet's `sidecar/providers/openai-compatible.js`, not to this `app.py` adapter. Under Bug A (StarNet Groq runs kill the sidecar) the handoff says "The stream: false patch made it worse (broke Ollama too). It was reverted." Nothing in the handoff says `stream: false` was ever applied to Jarvis's `app.py`. The handoff also does not say whether this adapter supports streaming responses. Left for the human to confirm. (Partly answered 2026-09-26: `app.py` shows this adapter does **not** stream. Which adapter PART 8 meant is still open.)

## Related

[[jarvis-x-runtime]] | [[jarvis-x-app]] | [[universal-model-layer]] | [[hermes-agent]] | [[aider]] | [[starnet]] | [[jarvis-x-station-view]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
