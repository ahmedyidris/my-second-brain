---
title: Jarvis X StarNet Gateway
tags: [jarvis-x, starnet, api, openai-compatible, gateway, entity, built-not-merged]
sources:
  - raw/2026-09-26-starnet-gateway-and-station-build.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[starnet]], [[jarvis-x-openai-compatible-api]], [[jarvis-x-runtime]], [[universal-model-layer]], [[jarvis-x-station-view]], [[groq]], [[gemini]], [[openrouter]], [[ollama]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[jarvis-x-model-priority]], [[constitutional-autonomy]]
last_updated: 2026-09-26
---

# Jarvis X StarNet Gateway

A second OpenAI-compatible endpoint for [[jarvis-x]], built so that [[starnet]] can use Jarvis's model tiers. It is `code/openai-gateway.js`, a separate Node process on **`127.0.0.1:8010`**. This is the handoff's Priority 2 ("Route StarNet through Jarvis").

**Status:** built, in jarvis-x PR #37 (draft, CI green), not merged, and **not yet run on the Chromebook**.

## Why a second endpoint

[[jarvis-x-openai-compatible-api]] (app.py's `/v1` on :8000) can't serve StarNet. The reasons below come from StarNet's own adapter code, and the first was reproduced with it:

| StarNet needs | app.py `/v1` does | Result |
|---|---|---|
| a streamed (SSE) reply ending in `data: [DONE]` | one plain JSON body | StarNet reads **zero** text events. The run ends "done, truncated" with nothing in it. |
| response headers within 30s | headers only after the whole answer | a slow local answer is aborted |
| its own system prompt and history | the last user message only, with Jarvis's persona swapped in | the agent loses its identity and history |
| `tools` passed through | dropped | no task can run |

`app.py` is local-owned (see [[jarvis-x-runtime]]) and its `/v1` still suits Aider and Continue, so the fix is a separate process rather than an edit to it.

## How it works

- **Pass-through.** It uses the same provider chains as [[universal-model-layer]]'s `registry.js`, with the same fallback order and the same on-disk daily quota.
- **Streaming.** Calls to the providers are non-streamed, the path `registry.js` already proves works from [[crostini]]. The finished answer is replayed to StarNet as SSE: headers first, then a keepalive every 10s. StarNet then streams only from 127.0.0.1, which removes the leading suspect for StarNet's Bug A (the Cloudflare/IPv6 issue, see [[ipv6-dns-truncation-crostini]]). Bug A itself is still undiagnosed.
- **Model ids.**
  - `fast`, `smart`, `quality`, `frontier`, `local` mean the same as on app.py. `fast` is listed first.
  - `provider/model` pins one route. Cloud models are limited to `registry.js`'s free list, so it is **$0 by construction** ([[jarvis-x-model-priority]]).
  - `ollama/<any pulled model>` also works.
- **Gemini** goes through its OpenAI-compatible URL, because that one carries tool calls. Unverified on the machine; if it fails, the chain falls through to [[groq]], then local.
- **Safety.**
  - The kill switch returns 503 before any provider is called ([[constitutional-autonomy]]).
  - It listens on loopback only, and rejects foreign Host headers and non-JSON bodies.
  - An optional bearer token is set with `JX_GATEWAY_KEY`.

## Port

8010. The first push used 8001, which belongs to tts-worker. It was caught before merge, and a test now reads every Jarvis file that binds a port and fails on a collision:

| Port | Service |
|---|---|
| 8000 | app.py |
| 8001 | tts-worker |
| 8002 | dashboard |
| 8787 | StarNet |

## StarNet side

Start StarNet with `CUSTOM_OPENAI_BASE_URL="http://127.0.0.1:8010/v1"`. In StarNet's settings, type the URL **with `http://`**, leave the key empty, and pick model `fast`. Full steps are in the repo's `docs/STARNET_GATEWAY.md`.

## Verification

- **Tests:** 56 offline assertions in CI. 32 of 33 mutations were caught; the one escape changes nothing.
- **Contract check:** StarNet's real adapter was run against the gateway with a fake upstream. It received text, parallel tool calls, `finish_reason` and usage. A reply slower than StarNet's connect ceiling still arrived.
- **Not verified:** a live upstream on the Chromebook.

## Related

[[starnet]] | [[jarvis-x-openai-compatible-api]] | [[jarvis-x-runtime]] | [[universal-model-layer]] | [[jarvis-x-station-view]] | [[jarvis-x-model-priority]]
