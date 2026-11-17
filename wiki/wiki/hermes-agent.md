---
title: Hermes Agent
tags: [jarvis-x, component, agent, local-ai]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[the-council]], [[self-improvement-loop]], [[ollama]]
last_updated: 2026-09-24
---

# Hermes Agent

The core reasoning brain of [[jarvis-x]]. A self-improving local agent with 70+ default skills and cross-session memory. Runs entirely on local hardware via Ollama.

## Key features

- Writes its own new skills automatically (automatic skill creation)
- Cross-session conversation memory
- 70+ default tools: file edit, command run, web browse
- Structured JSON function/tool calling
- Local-first: no cloud dependency

## Models

| Model | Use case | Speed on CPU |
|-------|----------|-------------|
| llama3.2:3b | Primary (CPU) | 8–12 t/s |
| qwen3:1.5b | Fast alternative | 15–20 t/s |
| hermes3:8b | Future (GPU/16GB RAM) | 1–3 t/s |

## Installation

```bash
ollama launch hermes
# or
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Role in the system

Part of [[the-council]] as "Core Agent Brain". Powers the [[self-improvement-loop]] — analyzes its own daily logs, generates improved prompts and new tools, auto-implements with safety checks.

## Operational status (2026-09-24)

Running as `hermes-agent` under `supervisord` (systemd unit `jarvis-supervisord.service`), alongside `hermes-api` (uvicorn, port 8000) and `tts-worker`. Also available as a standalone CLI:

```bash
set -a && source ~/.jarvis-x/.env && set +a
hermes
```

Requires `~/.bashrc` to have `export PATH="$HOME/venv-ai/bin:$PATH"`.

Also usable as a coding agent via Aider, pointed at the `smart` tier:

```bash
set -a && source ~/.jarvis-x/.env && set +a
cd ~/jarvis-x
aider --model groq/openai/gpt-oss-120b --no-show-model-warnings
```

Gotcha: inside Aider's prompt, only `/commands` or natural language are safe — never paste raw shell commands there, they get sent to the model as a question instead of executing.
