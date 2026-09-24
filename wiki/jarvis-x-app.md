---
title: Jarvis X App
tags: [jarvis-x, v2, delivery, pwa, app]
sources:
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[jarvis-x-hardware]], [[universal-model-layer]], [[constitutional-autonomy]], [[starnet]]
last_updated: 2026-09-24
---

# Jarvis X App

The v2 delivery architecture for [[jarvis-x]]: one branded product that runs on Linux, Windows, iPhone, Android, and eventually macOS — all from a single codebase.

## Architecture

- **Backend:** FastAPI daemon (already the core service)
- **Frontend:** web UI served locally → installable as a **PWA** on any device
- **Desktop (later):** same UI wrapped with **Tauri** for Windows/macOS native builds

## Platform rollout order

| Order | Platform | Why |
|-------|----------|-----|
| ① | Linux (Pop!_OS) | Native, already running |
| ② | Windows | Biggest client market for AI gigs |
| ③ | PWA (iOS + Android) | Covers mobile at $0 — no Apple developer fee needed |
| ④ | macOS / native iOS | After GPU box + revenue; needs Mac hardware + $99/yr |

## Brand kit (self-generated)

- **Name:** JARVIS X
- **Mark:** arc-reactor ring forming the letter X
- **Palette:** obsidian black + arc gold (Gothic-Arcane doctrine)
- **Voice:** calm, precise, bilingual (EN + AR)

JARVIS X generates its own brand assets as one of its first [[jarvis-x-content-engine]] jobs — *the system literally brands itself.*

## Definition of done (v2.0)

One installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → [[constitutional-autonomy]] + audit log active.

## Timeline

Built in Wk 5–6 of the 12-week overlay: PWA-ready web UI shell after voice engine. Tauri Windows build in Wk 7–8.

## OpenAI-compatible adapter (landed 2026-09-24, commit `99652aa`)

`app.py` now exposes an OpenAI-compatible surface on top of the FastAPI backend:

- `GET http://127.0.0.1:8000/v1/models`
- `POST http://127.0.0.1:8000/v1/chat/completions` — accepts `model: local | fast | smart | quality | frontier`, returns the standard OpenAI `chat.completion` shape. Persona is loaded from `config/system_prompt.txt` and prepended server-side.

Tier-to-model resolution in `app.py`:

```python
tier_to_model = {
    "local":    "qwen2.5:3b",
    "fast":     "registry:fast",
    "smart":    "registry:smart",
    "quality":  "registry:quality",
    "frontier": "registry:quality",
}
```

Implementation note: the new routes must be registered **before** the SPA wildcard route (`@app.get("/{full_path:path}")`) — otherwise the wildcard intercepts `GET /v1/models` and serves `index.html` instead.

Required imports added to `app.py`: `Request` in the fastapi import block, `import time`, `JSONResponse` from `fastapi.responses`.

This endpoint is a chat API only — it does not read the filesystem. Callers (Aider, Continue, [[starnet]] agents) must read files themselves and include content in the message. This is expected behavior, not a bug.

**Consumer: [[starnet]].** The plan is to route StarNet traffic through this adapter (`CUSTOM_OPENAI_BASE_URL=http://127.0.0.1:8000/v1`) so Jarvis handles provider fallbacks and StarNet never dies on Groq truncation. As of 2026-09-24 this is blocked: StarNet's UI-side custom-provider verification rejects `127.0.0.1` even with a valid key (StarNet Bug C). The env-var path at StarNet launch time may bypass that UI check — not yet confirmed. This is StarNet's Priority 2 open item.

## Station tab (proposed, not yet built)

Explicit direction as of 2026-09-24: instead of continuing to build out [[starnet]] as a full parallel platform, add a "Station" tab to this app's existing React frontend. Scope: a roster file at `config/agents.yaml`, four new endpoints in `app.py` (list, chat, transcript, task), a simple grid UI in React, one background worker per agent. Framed as "a real weekend project" — achievable, versus StarNet's larger ambition. Rationale: Jarvis X already covers ~80% of StarNet's useful features.
