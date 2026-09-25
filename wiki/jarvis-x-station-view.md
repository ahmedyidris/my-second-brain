---
title: Jarvis X Station View
tags: [jarvis-x, multi-agent, frontend, planned]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[starnet]], [[the-council]], [[jarvis-x-app]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Jarvis X Station View

A planned **"Station" tab** in [[jarvis-x]]'s existing React frontend. It's meant to give Jarvis a multi-agent station of its own instead of a clone of [[starnet]]. **Status: not started as of the 2026-09-24 handoff.** It is Priority 3 in the handoff's "what to try next" list, so it's a plan, not a feature.

## Status

| Item | Value |
|------|-------|
| Status | Planned, not started (as of the 2026-09-24 handoff) |
| Priority | 3 of 4 in PART 7 ("what to try next") |
| Replaces | Building a [[starnet]] clone |
| Effort (per handoff) | "a real weekend project" |

## Planned elements

The handoff's plan, as written (PART 7, Priority 3): "Instead of a StarNet clone, add a 'Station' tab to Jarvis's existing React frontend."

| Element | Plan |
|---------|------|
| Where | "Station" tab in Jarvis's existing React frontend |
| Roster | `config/agents.yaml` |
| Backend | Four endpoints in `app.py`: list, chat, transcript, task |
| UI | Simple grid UI in React |
| Workers | One background worker per agent |

> This is a real weekend project. StarNet is the ambition; a station tab in Jarvis is achievable.

## Why a station tab instead of StarNet

From PART 8 ("what not to do"):

> Do not chase a StarNet clone. Jarvis already has 80% of StarNet's useful features. Add a station view to Jarvis instead.

Supporting context from the same handoff:

- As of the handoff, [[starnet]] works only with Ollama. Groq runs kill its sidecar (Bug A), and its UI rejects Jarvis's localhost endpoint as a custom provider (Bug C).
- Jarvis already has working `local | fast | smart | quality | frontier` tiers and an OpenAI-compatible `/v1` adapter ([[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]]).
- PART 8 also says "Do not build the Tauri desktop shell for daily use. Web UI is faster and identical in function." The line doesn't name a project, but the only Tauri shell the handoff describes is StarNet's (PART 1; gotcha 8 on the 30-60 min build). Implication: it also argues for putting the station in the web frontend rather than in a desktop build.

## Where it would sit in the as-built runtime

- `app.py` already holds the `/v1/models` and `/v1/chat/completions` adapter, served at `http://127.0.0.1:8000`. The handoff lists `hermes-api` as "uvicorn, port 8000". Implication: the four station endpoints would join that same FastAPI app ([[jarvis-x-runtime]]).
- Fix 7 in the handoff put the `/v1` routes BEFORE the SPA wildcard route (`@app.get("/{full_path:path}")`), because otherwise "the wildcard catches GET /v1/models and serves index.html". Implication: the station endpoints would need the same ordering.
- Bug B: the Jarvis chat API doesn't read the filesystem, and callers must include file contents themselves ([[jarvis-x-openai-compatible-api]]). Implication: an agent worker that needs file context would have to send it in the message.

## Open questions (not specified by the handoff)

- URL paths and request/response shapes for the list, chat, transcript and task endpoints
- The schema of `config/agents.yaml`
- Which model tier each agent uses
- How the per-agent background workers are run and supervised (the handoff doesn't say whether they would be supervisord programs like `hermes-agent`, `hermes-api` and `tts-worker`)

## Relation to the Council and the App

- **[[the-council]]:** the earlier plans describe a multi-agent roster of models with named roles. The DeepSeek master plan's file-structure appendix already lists a `config/agents.yaml` under `jarvis-x/config/`. The handoff proposes the same path for the station roster but doesn't connect it to the Council. Whether the station roster would carry the Council's seats is an interpretation, not stated in either source.
- **[[jarvis-x-app]]:** the v2 plan's delivery architecture is a FastAPI backend plus a locally served web UI, installable as a PWA, with the same UI wrapped with Tauri later for Windows/macOS desktop builds. The handoff calls the as-built UI "Jarvis's existing React frontend". Implication (not stated in the handoff): that React frontend is the as-built form of the v2 plan's web UI, so the station tab would live there. The handoff doesn't say whether it is PWA-installable, and doesn't say whether PART 8's Tauri line applies to the v2 plan's later Windows/macOS Tauri wrapper.
- **[[jarvis-x-plan-vs-reality]]** compares the plans with the as-built state more broadly.
