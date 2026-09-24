---
title: Ollama
tags: [jarvis-x, tool, local-ai, infrastructure]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[jarvis-x-hardware]], [[starnet]]
last_updated: 2026-09-24
---

# Ollama

Local model runtime for [[jarvis-x]]. Runs LLMs on-device — the foundation of the zero-cloud-keys constraint. Powers [[hermes-agent]] and the `local` tier of the [[universal-model-layer]].

## Install

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Essential models (CPU-first, Lenovo Y50-70)

| Model | Size | Speed on CPU | Use |
|-------|------|-------------|-----|
| llama3.2:3b | ~2GB | 8–12 t/s | Primary agent |
| qwen3:1.5b | ~1GB | 15–20 t/s | Fast alternative |
| nomic-embed-text | ~0.5GB | Fast | Embeddings for ChromaDB/[[obsidian]] |
| hermes3:8b | ~5.5GB | 1–3 t/s | Future — needs 16GB RAM + GPU |

```bash
ollama pull llama3.2:3b
ollama pull qwen3:1.5b
ollama pull nomic-embed-text
```

## Role in Jarvis X

- Serves as the `local` tier in [[universal-model-layer]] (`jj ask --tier local`)
- Privacy-sensitive queries always route here — nothing leaves the machine
- [[hermes-agent]] runs on top of Ollama models
- `nomic-embed-text` powers ChromaDB vector search in [[obsidian]]

## Hardware constraint

On the current [[jarvis-x-hardware]] (CPU-only, 7.7GB RAM), `hermes3:8b` is too slow for interactive use (1–3 t/s). Unlocked after Phase 1 hardware upgrade (16GB RAM + GPU).

## Models observed on Crostini (2026-09-24)

Separate from the table above — these are the models actually present in the 2026-09-24 handoff's environment (see the hardware contradiction noted in [[jarvis-x-hardware]]):

- `qwen2.5:7b` (4.7GB) — working model for [[starnet]]'s Raqib agent, ~10 tok/s
- `qwen2.5:3b` (1.9GB) — Jarvis X `local` tier
- `qwen2.5-coder:7b` (4.7GB)
- `qwen2.5-coder:3b` (1.9GB)
- `nomic-embed-text` (274MB)

## systemd model-directory fix

Ollama's systemd unit runs as user `ollama`, which could not read `~/.ollama` (the user's home directory). Fixed by pointing it at the system-wide model path instead:

```bash
sudo tee /etc/systemd/system/ollama.service.d/override.conf >/dev/null << 'EOF'
[Service]
Environment="OLLAMA_MODELS=/usr/share/ollama/.ollama/models"
Environment="OLLAMA_NUM_PARALLEL=1"
Environment="OLLAMA_KEEP_ALIVE=5m"
Environment="OLLAMA_MAX_LOADED_MODELS=1"
Environment="OLLAMA_FLASH_ATTENTION=1"
EOF
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Gotcha: `ollama list` only shows the models in whichever `OLLAMA_MODELS` directory the running systemd unit is actually pointed at. If expected models are missing, check `/etc/systemd/system/ollama.service.d/override.conf` (or lack thereof) before assuming they need re-pulling — they may simply be in `~/.ollama/models` while the service reads `/usr/share/ollama/.ollama/models`, or vice versa.
