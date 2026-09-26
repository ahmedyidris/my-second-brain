---
title: Jarvis X Runtime
tags: [jarvis-x, runtime, deployment, entity, as-built]
sources:
  - raw/2026-09-26-starnet-gateway-and-station-build.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[jarvis-x-openai-compatible-api]], [[hermes-agent]], [[jarvis-x-voice-engine]], [[jarvis-x-app]], [[universal-model-layer]], [[ollama]], [[groq]], [[gemini]], [[crostini]], [[jarvis-x-hardware]], [[constitutional-autonomy]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-station-view]], [[free-api-tiers]], [[aider]], [[starnet]], [[openrouter]], [[jarvis-x-starnet-gateway]]
last_updated: 2026-09-26
---

# Jarvis X Runtime

The as-built deployment of [[jarvis-x]], as of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]). This page records what is actually running, how it is launched and tested, and the fixes that got it there. For what the plans intended, see [[jarvis-x]], [[universal-model-layer]] and [[jarvis-x-plan-vs-reality]].

## Repo and location

| Item | Value (as of the 2026-09-24 handoff) |
|------|--------------------------------------|
| Location | `~/jarvis-x` |
| Repo | https://github.com/ahmedyidris/jarvis-x |
| Branch | `master` |
| Latest commit | `99652aa` — feat(api): OpenAI-compatible /v1/chat/completions + /v1/models |
| Persona file | `~/jarvis-x/config/system_prompt.txt` |
| Supervisor config | `~/jarvis-x/config/supervisord.conf` (from the status command in PART 4) |
| API keys | `~/.jarvis-x/.env` (chmod 600) |

## Services

Managed by supervisord under the systemd unit `jarvis-supervisord.service`.

| Service | State (2026-09-24) | Notes |
|---------|--------------------|-------|
| `hermes-agent` | RUNNING | See [[hermes-agent]] |
| `hermes-api` | RUNNING | uvicorn, port 8000 |
| `tts-worker` | RUNNING (degraded) | Chatterbox model absent, returns 500 on `/synthesize` — see [[jarvis-x-voice-engine]] |

Implication: the [[jarvis-x-openai-compatible-api]] endpoints live at `127.0.0.1:8000`, the same port as `hermes-api`, so `app.py` (and presumably `POST /api/ask`) appears to be what the `hermes-api` uvicorn process serves. The handoff does not state this mapping outright.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan's [[constitutional-autonomy]] section describes systemd services `jarvis-core`, `jarvis-scheduler`, `jarvis-voice` running under Jarvis's own Linux user with ownership of `~/jarvis/`. The handoff shows one systemd unit (`jarvis-supervisord.service`) supervising `hermes-agent`, `hermes-api`, `tts-worker`, with source in `~/jarvis-x`. The handoff does not say which Linux user the services run as, or whether the plan's service layout was abandoned or simply not built yet. Left for the human to resolve.

## Model tiers

All verified working via `POST /api/ask`, as of the 2026-09-24 handoff:

| tier     | provider | model                     |
|----------|----------|---------------------------|
| local    | ollama   | qwen2.5:3b                |
| fast     | groq     | openai/gpt-oss-20b        |
| smart    | groq     | openai/gpt-oss-120b       |
| quality  | gemini   | gemini-3.6-flash          |
| frontier | gemini   | gemini-3.6-flash          |

This is the live form of the [[universal-model-layer]]. Provider details: [[ollama]], [[groq]], [[gemini]]. The same tier names are accepted by the `model` field of the [[jarvis-x-openai-compatible-api]]. The cloud models here (`openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `gemini-3.6-flash`) are the ones the handoff lists as free API access under Bug E — see [[free-api-tiers]]. [[openrouter]], the third provider on that list, has no tier in this table.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan's tier set is `local|fast|smart|long` (`jj ask "..." --tier ...`), with long-context routed to Gemini. The plan also lists Anthropic among its registered providers ("while sub lives, then optional API") but does not assign it a tier; the `smart` placement on [[universal-model-layer]]'s provider table is this wiki's inference. The as-built tiers are `local | fast | smart | quality | frontier`, with `smart` on Groq and `quality`/`frontier` on Gemini. The handoff does not mention a `long` tier, the `jj` CLI, or Anthropic. Left for the human to resolve.

## Fixes that landed

The handoff lists ten fixes. Those that touch Jarvis or the machine it runs on (— = no commit stated):

| # | Fix | Commit | Detail page |
|---|-----|--------|-------------|
| 1 | Env var quoting bug in `registry.js` | — | below |
| 2 | System prompt dropped on registry tiers | `4281158` | below, [[hermes-agent]] |
| 3 | Groq fast model 404 (`groq/compound-mini` → `openai/gpt-oss-20b`) | `b634ed8` | [[groq]] |
| 4 | Gemini model name: keep `gemini-3.6-flash` (models-list is stale) | — | [[gemini]] |
| 5 | IPv6 truncation (Crostini + Cloudflare) | — | [[crostini]] |
| 6 | systemd `EnvironmentFile` for Jarvis | — | below |
| 7 | OpenAI-compatible adapter in `app.py` | not stated (inference: probably `99652aa`, whose message matches) | [[jarvis-x-openai-compatible-api]] |
| 8 | Ollama model directory | — | [[ollama]] |

Fixes 9 and 10 are StarNet-side — see [[starnet]]. The handoff does not label fixes 3 and 4 with a project; their `registry.js` targets match the Jarvis tier table above.

### Fix 1 — env var quoting bug

`registry.js` read `.env` as text and kept surrounding quotes on every key. Every cloud call went out as `Authorization: Bearer "gsk_..."` — quotes and all. Every provider rejected silently.

Fix — strip quotes from `.env`:

```bash
sed -i 's/^\([A-Z_]*\)="\(.*\)"$/\1=\2/' ~/.jarvis-x/.env
```

### Fix 2 — system prompt dropped on registry tiers

The `registry:` branch in `hermes.py` replaced the curl command without including the system prompt. So fast/smart/frontier all answered "I am Qwen" despite the prompt forbidding it.

Fix: prepend system in the registry branch (committed as `4281158`).

### Fix 6 — systemd EnvironmentFile

Jarvis services were starting without API keys because systemd units don't inherit shell exports. Fix — a drop-in for the supervisord unit:

```bash
sudo mkdir -p /etc/systemd/system/jarvis-supervisord.service.d
sudo tee /etc/systemd/system/jarvis-supervisord.service.d/env.conf > /dev/null << 'EOF'
[Service]
EnvironmentFile=/home/ahmedyidris/.jarvis-x/.env
Environment="NODE_OPTIONS=--dns-result-order=ipv4first"
EOF
sudo systemctl daemon-reload
sudo systemctl restart jarvis-supervisord.service
```

The `NODE_OPTIONS` line is the Node-side half of the IPv6 workaround ([[crostini]]).

## Launch and test

Services run automatically under systemd. To restart:

```bash
sudo systemctl restart jarvis-supervisord.service
sleep 8
supervisorctl -c ~/jarvis-x/config/supervisord.conf status
```

To test:

```bash
curl -s http://127.0.0.1:8000/v1/models | python3 -m json.tool
curl -s -XPOST http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"smart","messages":[{"role":"user","content":"Say ready"}]}' \
  | python3 -m json.tool
```

### Hermes CLI

```bash
set -a && source ~/.jarvis-x/.env && set +a
hermes
```

`~/.bashrc` needs: `export PATH="$HOME/venv-ai/bin:$PATH"`

The handoff's [[aider]] launch command also runs from `~/jarvis-x`.

### Ports in use (read from the repo, 2026-09-26)

| Port | Service | Where it is set |
|------|---------|-----------------|
| 8000 | `hermes-api` (app.py) | `config/supervisord.conf` |
| 8001 | `tts-worker` | `code/tts_worker.py`, app.py `TTS_WORKER_URL` |
| 8002 | dashboard backend | `code/reply/tools/weather.py`, `dashboard/` |
| 8010 | [[jarvis-x-starnet-gateway]] (built, not merged) | `code/openai-gateway.js` |
| 8787 | [[starnet]] sidecar | StarNet |
| 11434 | [[ollama]] | systemd |

Source: `raw/2026-09-26-starnet-gateway-and-station-build.md`.

## Planned additions (PART 7)

- **Priority 3:** a "Station" tab in Jarvis's existing React frontend, with a roster at `config/agents.yaml` and four endpoints in `app.py` (list, chat, transcript, task) — see [[jarvis-x-station-view]].
  - Built 2026-09-26 (jarvis-x PR #38), not merged. The endpoints live in `code/station/` and are mounted into `app.py` with one call that the local session still has to add.
- **Priority 2** (StarNet through Jarvis) was built as a separate gateway on port 8010 (jarvis-x PR #37, not merged). See [[jarvis-x-starnet-gateway]].
- **Priority 4:** obtain the chatterbox checkpoint (~5GB), place it at `~/jarvis-x/voices/chatterbox-eg/`, restart `tts-worker` — see [[jarvis-x-voice-engine]].

## Environment

The machine is an ASUS Chromebook running Crostini (Debian 13 trixie) — see [[crostini]] for its network and memory quirks and [[jarvis-x-hardware]] for the hardware.

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** [[jarvis-x-hardware]] describes the body as a Lenovo Y50-70 on Pop!_OS 24.04 LTS. The handoff's environment is an ASUS Chromebook (11th Gen i5, no GPU, 14GB RAM) under Crostini. The handoff does not say whether the Lenovo was retired or is still part of the plan.

> **Resolved by the human (2026-09-25):** the Chromebook is the current machine ("Current machine is chrome boo[k]"). See [[jarvis-x-hardware]].

| Item | Value (as of the 2026-09-24 handoff) |
|------|--------------------------------------|
| Python | 3.11 in `~/venv-ai` (uv-managed) |
| Node | 20.x (system), 22.x (bundled for Tauri) |

Key paths:

- `~/.jarvis-x/.env` — API keys (chmod 600)
- `~/jarvis-x/` — Jarvis source
- `~/starnet/` — StarNet source ([[starnet]])
- `~/.local/share/StarNet/workspaces/` — StarNet state
- `~/.ollama/models/` OR `/usr/share/ollama/.ollama/models` — Ollama models (check which one is active; see [[ollama]])

## Gotchas

- **Gotcha 2:** Never paste Python or YAML into bash. If it's not a shell command, put it in a file first with a heredoc.
- **Gotcha 9:** Jarvis's quality tier maps to Gemini. If it returns ollama responses, the Gemini key is missing or invalid. The verify curl is on [[gemini]]. Implication: the quality tier appears to fall back to the local Ollama tier when the Gemini call fails, rather than erroring — the handoff describes the symptom, not the fallback mechanism.

## Rules (PART 8)

- Do not put API keys in git. `.env` is gitignored — keep it that way.
- Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern.

Compare with [[constitutional-autonomy]], the plan's model of which actions need approval.

## Related

[[jarvis-x]] | [[jarvis-x-openai-compatible-api]] | [[hermes-agent]] | [[jarvis-x-voice-engine]] | [[jarvis-x-app]] | [[universal-model-layer]] | [[ollama]] | [[groq]] | [[gemini]] | [[crostini]] | [[jarvis-x-hardware]] | [[aider]] | [[starnet]] | [[jarvis-x-station-view]] | [[free-api-tiers]] | [[openrouter]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
