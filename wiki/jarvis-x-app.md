---
title: Jarvis X App
tags: [jarvis-x, v2, delivery, pwa, app]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[jarvis-x]], [[jarvis-x-hardware]], [[universal-model-layer]], [[constitutional-autonomy]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[jarvis-x-station-view]], [[starnet]], [[crostini]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
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

## As-built (2026-09-24 handoff)

As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]):

- **Backend:** FastAPI `app.py`. Its `/v1/*` endpoints are at `127.0.0.1:8000`, the port of the `hermes-api` uvicorn service (implication: `hermes-api` serves `app.py`; the handoff does not state this outright). `POST /api/ask` is the endpoint used to verify the model tiers. The handoff does not say which file defines it. See [[jarvis-x-runtime]].
- **Frontend:** a React SPA ("Jarvis's existing React frontend"), served by the wildcard route `@app.get("/{full_path:path}")`, which returns `index.html`.
- **OpenAI-compatible endpoints (landed in commit `99652aa`):** `GET /v1/models` and `POST /v1/chat/completions` were added to `app.py`, registered before the wildcard route so the wildcard doesn't catch `GET /v1/models`. `model` takes a tier name (`local | fast | smart | quality | frontier`), the response is the standard OpenAI `chat.completion` shape, and the persona from `config/system_prompt.txt` is prepended server-side. It is a chat API only and doesn't read the filesystem, so callers (Aider, Continue, [[starnet]] agents) must include file contents themselves. Routing StarNet through it (`CUSTOM_OPENAI_BASE_URL`) is blocked by StarNet's Bug C. Full detail, including the `tier_to_model` block and required imports: [[jarvis-x-openai-compatible-api]].
- **Planned (not yet built):** a "Station" tab in the React frontend (handoff Priority 3) for multi-agent work, instead of building [[starnet]] out as a full parallel platform. The scope is a roster at `config/agents.yaml`, four `app.py` endpoints (list, chat, transcript, task), a simple grid UI and one background worker per agent. The handoff frames it as "a real weekend project", since Jarvis already has ~80% of StarNet's useful features. See [[jarvis-x-station-view]].
- The handoff does not mention PWA installation or phone access.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** this page's timeline has a Tauri Windows build in Wk 7–8 (the plan's Wk 7–8 line reads "content engine v1 → first 5 bilingual pieces; Windows run-through" and does not mention Tauri; its architecture section says the UI is wrapped with Tauri "later for Windows/macOS desktop builds"). The handoff says the Tauri build is 30–60 min and needs 8GB disk + 6GB RAM, and is "rebuildable but not useful for daily work on this hardware"; StarNet's Tauri shell was built once and then deleted (slow, no benefit over web); and PART 8 says "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function." The only Tauri build the handoff records is StarNet's, so it is not stated whether the build figures and the PART 8 rule refer to StarNet's shell, a Jarvis shell, or both. Either way, this concerns daily use on the current machine and does not necessarily cancel a Tauri build for distribution (the plan's Windows target). Whether the Tauri step stays in the roadmap is for the human to decide.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** this page's rollout table lists ① Linux (Pop!_OS) as "Native, already running". The raw v2 plan's platform order reads "① Linux (native, first)". "Pop!_OS" comes from the plan's v1 platform column ("Pop!_OS only") and its execution prompt ("a fresh Pop!_OS terminal"), and the plan text does not contain "already running". The handoff's Jarvis runs on Crostini (Debian 13 trixie) on an ASUS Chromebook ([[crostini]]). The handoff does not say whether Pop!_OS is still a target. The table wording is kept as it was. Left for the human to resolve.

Note: the handoff lists Node 22.x as "bundled for Tauri" alongside the system Node 20.x.
