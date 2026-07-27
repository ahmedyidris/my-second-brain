---
title: Ollama
tags: [jarvis-x, tool, local-ai, infrastructure]
sources:
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[jarvis-x-hardware]]
last_updated: 2026-07-27
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
