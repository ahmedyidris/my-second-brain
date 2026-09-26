# StarNet gateway and Station tab: build notes (2026-09-25/26)

Session notes from a Claude Code remote session. The work was done at
Ahmed's request "A then C, go ahead": A was routing StarNet through Jarvis
(handoff Priority 2), and C was the Station tab (handoff Priority 3).

Every finding below comes from one of three places:
- reading the code, cited by file;
- running StarNet's own adapter against a test server in the session container;
- a jarvis-x pull request.

None of it was run on the Chromebook.

## Code read

- **jarvis-x** at master `5c64271`: `app.py` (read only, since it is local-owned per HANDOFF.md), `hermes.py`, `code/providers/registry.js`, `code/providers/cli.js`, `code/reply/engine.py`, `config/supervisord.conf`, `code/tts_worker.py`, `web/src/`.
- **StarNet** at upstream `androoAGI/starnet` head `7ee93cea`, which is NOT Ahmed's local branch `feat/harness-backend`: `sidecar/providers/openai-compatible.js`, `sidecar/providers/registry.js`, `sidecar/providers/provider.js`, `sidecar/index.js` (`handleProviderProbe`, `handleProviderValidate`, `providerRuntimeBaseUrl`, `providerHasCredential`), `frontend/app/harness.js`, `frontend/app/stationui.js`, `shared/specialties.js`, `LICENSE`.
- **StarNet's license:** MIT, "Copyright (c) 2026 Andrew Sims".

## Findings about StarNet's OpenAI-compatible adapter

1. **It always streams.** It sends `stream: true` plus `stream_options: {include_usage: true}` and the header `Accept: text/event-stream`.
   - It parses only lines starting with `data:`, skips lines starting with `:`, and treats `data: [DONE]` as the end sentinel.
   - It reads `choices[0].delta` (or `.message`) for `content` and `tool_calls`, `finish_reason`, and `usage`.
2. **Tested:** against app.py's current `/v1` reply shape (one plain JSON `chat.completion` body), StarNet's adapter yields zero text events. The run ends as `{"type":"done","finishReason":null,"truncated":true}`, with nothing in it.
3. **Connect ceiling.** StarNet aborts a request whose response headers take longer than `SKYNET_PROVIDER_CONNECT_MS`, which defaults to 30s. Its idle watchdog `SKYNET_PROVIDER_IDLE_MS` defaults to 300s.
4. **app.py's `/v1` loses the conversation.** It keeps only the last user message, replaces the caller's system prompt with Jarvis's persona, and drops `tools`.
5. **Custom provider profile** (`id: 'custom'`):
   - It needs no key (`keyRequired: false`, `modelsRequireAuth: false`).
   - Base URL env: `CUSTOM_OPENAI_BASE_URL` or `OPENAI_COMPATIBLE_BASE_URL`. Key env: `CUSTOM_OPENAI_KEY` or `OPENAI_COMPATIBLE_KEY`.
   - `providerHasCredential` needs only the base URL.
6. **Custom-provider key check** (`/api/providers/validate`):
   - It runs only when a key is typed.
   - It lists `/models`, then streams "Reply with OK." to the selected model (or `models[0]`) with a hard 15s budget.
   - On timeout it reports "the endpoint accepted the request but did not answer".
   - Its "answered" test accepts a bare `done` event. Against app.py's JSON shape the check would therefore PASS if it finished in time, even though real runs would be empty.
7. **The settings URL field adds `https://`** to a value typed without a scheme (`stationui.js`). Typing `127.0.0.1:8000/v1` therefore becomes `https://127.0.0.1:8000/v1`, which fails TLS against a plain-HTTP server.
8. **Tool gating.** StarNet refuses a task up front only when the catalog says `supportsTools === false`. An absent value (null) never refuses.
9. **Raqib is not in StarNet's code.** He is Ahmed's own agent, stored in local StarNet data. StarNet ships role templates ("specialties"): Strategist, Researcher, Scriptwriter and others.

### Bug C: candidate causes, ranked, none confirmed on the machine

1. **The 15s key check hit a slow model.** app.py's `/v1/models` lists `local` first, and app.py sends no headers until the answer exists.
2. **A missing `http://` got replaced with `https://`.** See finding 7.
3. **Ahmed's local branch differs from upstream.**

## Ports in use on Jarvis (from the repo)

| Port | Service |
|---|---|
| 8000 | app.py / hermes-api |
| 8001 | tts-worker (app.py `TTS_WORKER_URL`, `code/tts_worker.py`) |
| 8002 | dashboard backend (`code/reply/tools/weather.py`, `dashboard/`) |
| 8787 | StarNet |
| 11434 | ollama |

## What was built

### A: StarNet → Jarvis gateway (jarvis-x PR #37, draft, CI green)

- `code/openai-gateway.js` is a separate Node process on `127.0.0.1:8010`.
  - The first push defaulted to 8001, tts-worker's port. It was caught before merge and moved to 8010, and a test now pins it against the ports above.
- It passes requests through over registry.js's tier chains, with the same fallback and on-disk quota (`registry.js` gains one export, `bumpQuota`).
- Upstream calls are non-streamed. The answer is re-emitted to StarNet as SSE: headers and the role chunk go out immediately, then a keepalive every 10s.
- It keeps full messages (StarNet's `agentId` fields are stripped) and passes tools through.
- Model ids:
  - tier ids `fast`, `smart`, `quality`, `frontier`, `local` (`fast` is listed first);
  - pinned `provider/model` ids, where cloud models are limited to registry.js's free list;
  - `ollama/<any pulled model>`.
- **Safety:**
  - the kill switch returns 503;
  - it listens on loopback only;
  - it rejects any Host header other than localhost, and any body that isn't JSON;
  - an optional bearer token is set with `JX_GATEWAY_KEY`.
- **Tests:** 56 assertions, offline, in CI. 32 of 33 mutations were caught; the one escape changes nothing.
- **Contract check:** StarNet's real adapter was run against the gateway with a fake upstream. It received text, parallel tool calls, `finish_reason` and usage. A reply slower than the connect ceiling still arrived.
- **Doc:** `docs/STARNET_GATEWAY.md`.

### C: Station tab (jarvis-x PR #38, draft)

- `config/agents.yaml` holds four agents:
  - Raqib (Overseer, tier `smart`, which ends on `qwen2.5:7b`);
  - Researcher and Strategist (`smart`);
  - Scriptwriter (`quality`).
  - These roles are adapted from StarNet's specialties, with MIT credit in the file.
- `code/station/` contains:
  - a strict roster loader;
  - an append-only per-agent JSONL store under `logs/station/<id>/`;
  - one worker thread per agent;
  - FastAPI routes behind `require_token`: `GET /api/station/agents`, `POST .../{id}/chat`, `GET .../{id}/transcript`, `POST .../{id}/task`, `GET .../{id}/tasks`.
- Models are reached through `node code/providers/cli.js <tier> <prompt>`, the same bridge `hermes.py` uses.
- Agents write text only. The kill switch is checked before every model call. A task queued before the switch is pulled is marked `stopped` and never replayed.
- **Web:** a Station entry in the Dashboard tabs, `web/src/components/dashboard/Station.tsx`.
- **app.py is not touched.** Local must add `from code.station import mount_station` and `mount_station(app, require_token, Path(__file__).parent)`. The helper moves its routes ahead of the SPA catch-all itself.
- **Tests:** 64 pytest tests, in CI with the dependencies pinned to venv-ai's versions. 28 of 28 mutations were caught.
- **Browser check:** the built UI was driven in headless Chromium with a stand-in model. A chat reply appeared, an Arabic task reached "done" (shown right-to-left), and the kill switch banner disabled Send.
- **Doc:** `docs/STATION.md`.

### Also

- jarvis-x PR #35 (verbatim handoff doc) had a HANDOFF.md conflict with master. I merged master in, keeping both sides' rows.

## Not verified (needs the Chromebook)

- A live upstream through either piece.
- Gemini's OpenAI-compatible URL, which the gateway uses for the `quality` tier.
- Ollama's default context window against StarNet-sized prompts.
