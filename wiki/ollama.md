---
title: Ollama
tags: [jarvis-x, tool, local-ai, infrastructure, as-built]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[jarvis-x-hardware]], [[obsidian]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[gemini]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[free-api-tiers]], [[aider]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Ollama

Local model runtime for [[jarvis-x]]. Runs LLMs on-device — the foundation of the zero-cloud-keys constraint. Powers [[hermes-agent]] and the `local` tier of the [[universal-model-layer]].

## Install

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Essential models (CPU-first, Lenovo Y50-70)

From the July 2026 master plan. For the models on the machine in the 2026-09-24 handoff, see the "As-built (2026-09-24 handoff)" section below.

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

The bullets above describe the plan. In the 2026-09-24 handoff, the `local` tier is reached through `POST /api/ask` and the `/v1` adapter (`"model": "local"`). The handoff doesn't mention a `jj` CLI or privacy-based routing, so whether either exists is unknown. See the "As-built (2026-09-24 handoff)" section below.

## Hardware constraint

On the current [[jarvis-x-hardware]] (CPU-only, 7.7GB RAM), `hermes3:8b` is too slow for interactive use (1–3 t/s). Unlocked after Phase 1 hardware upgrade (16GB RAM + GPU).

These figures describe the Lenovo Y50-70 in the earlier plans. The disagreement with the 2026-09-24 handoff's machine is noted below.

## As-built (2026-09-24 handoff)

What the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) records about Ollama on the ASUS Chromebook ([[crostini]]).

### Role, as of the 2026-09-24 handoff

| Where | Model | Notes |
|-------|-------|-------|
| Jarvis `local` tier | `qwen2.5:3b` | Verified working via `POST /api/ask` ([[jarvis-x-runtime]]) |
| StarNet agent Raqib (Overseer) | `qwen2.5:7b` | "slow — ~10 tok/s". Launch step: "Set Raqib's model to OLLAMA → qwen2.5:7b" ([[starnet]]) |

- In the [[jarvis-x-openai-compatible-api]], `"local": "qwen2.5:3b"` is the only tier mapped straight to a model name. The other four map to `registry:` entries: `fast`, `smart` and `quality` to their own names, and `frontier` to `registry:quality`.
- In StarNet, "Currently: only Ollama works as provider". Groq and Gemini runs return HTTP 400 or kill the sidecar.
- Under StarNet's Bug A, the handoff says: "The stream: false patch made it worse (broke Ollama too). It was reverted." It doesn't say which file the patch changed. PART 8 separately warns: "Do not re-enable stream: false on the OpenAI-compatible adapter. It breaks all providers." Ambiguous: "the OpenAI-compatible adapter" could mean StarNet's `sidecar/providers/openai-compatible.js` or Jarvis's `/v1` adapter in `app.py` (fix 7). The handoff doesn't say which.
- Gotcha 9: "Jarvis's quality tier maps to Gemini. If it returns ollama responses, the Gemini key is missing or invalid." Implication: when the Gemini key is missing or invalid, Ollama appears to act as the fallback for `quality`. The handoff describes the symptom, not the mechanism, and doesn't say which Ollama model answers (see [[gemini]]).

### Models present (as of the 2026-09-24 handoff)

| Model | Size | Used by (per handoff) |
|-------|------|-----------------------|
| qwen2.5:7b | 4.7GB | StarNet's Raqib |
| qwen2.5:3b | 1.9GB | Jarvis `local` tier |
| qwen2.5-coder:7b | 4.7GB | not stated |
| qwen2.5-coder:3b | 1.9GB | not stated |
| nomic-embed-text | 274MB | not stated |

The handoff doesn't say the `qwen2.5-coder` models are used with [[aider]], which it launches against Groq's `openai/gpt-oss-120b`.

Implication (arithmetic): the five models add up to about 13.5GB. The disk had ~11GB free after cleanup ([[crostini]]).

### Model directory fix (fix 8)

"Ollama's systemd unit ran as user ollama and couldn't read ~/.ollama. Pointed it at the system path:"

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

| Setting | Value |
|---------|-------|
| `OLLAMA_MODELS` | `/usr/share/ollama/.ollama/models` |
| `OLLAMA_NUM_PARALLEL` | `1` |
| `OLLAMA_KEEP_ALIVE` | `5m` |
| `OLLAMA_MAX_LOADED_MODELS` | `1` |
| `OLLAMA_FLASH_ATTENTION` | `1` |

The handoff lists these values without explaining the last four.

### Which models directory is active

The key path, as the handoff gives it: "`~/.ollama/models/` OR `/usr/share/ollama/.ollama/models` — Ollama models (check which one is active)".

Gotcha 10: "ollama list shows only the active OLLAMA_MODELS directory. If models are missing, check which directory the systemd unit is pointed at."

```bash
ollama list
```

Practical note: if expected models are missing, check `/etc/systemd/system/ollama.service.d/override.conf`, or whether it exists at all, before assuming they need re-pulling. They may simply be in `~/.ollama/models` while the service reads `/usr/share/ollama/.ollama/models`, or the other way round.

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** the "Essential models (CPU-first, Lenovo Y50-70)" list above (`llama3.2:3b`, `qwen3:1.5b`, `nomic-embed-text`, `hermes3:8b`) and the "7.7GB RAM" hardware constraint come from the earlier plans. They describe a Lenovo Y50-70. The handoff's machine is an ASUS Chromebook with 14GB RAM (11th Gen i5, no GPU). Its models are the `qwen2.5` family plus `nomic-embed-text`. Of the plan's list, only `nomic-embed-text` is present, at 274MB against the plan's "~0.5GB" estimate. Unknown: whether the plan's model list was deliberately replaced, and whether the hermes3:8b "unlock" condition still applies on the new machine. The handoff's ~10 tok/s for `qwen2.5:7b` is reported for different hardware and a different model than the plan's 1–3 t/s for `hermes3:8b`, so the two figures are not directly comparable. Both are kept. Left for the human to resolve.

## Related

[[jarvis-x]] | [[hermes-agent]] | [[universal-model-layer]] | [[jarvis-x-hardware]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[starnet]] | [[gemini]] | [[crostini]] | [[free-api-tiers]] | [[aider]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
