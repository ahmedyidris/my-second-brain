---
title: Ollama
tags: [jarvis-x, tool, local-ai, infrastructure, as-built, chromebook]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
related: [[jarvis-x]], [[hermes-agent]], [[universal-model-layer]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[jarvis-x-hardware]], [[obsidian]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[gemini]], [[groq]], [[openrouter]], [[crostini]], [[ipv6-dns-truncation-crostini]], [[free-api-tiers]], [[aider]], [[source-jarvis-x-starnet-handoff]], [[source-model-landscape-research]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-25
---

# Ollama

Local model runtime for [[jarvis-x]]. Runs LLMs on-device — the foundation of the zero-cloud-keys constraint. Powers [[hermes-agent]] and the `local` tier of the [[universal-model-layer]].

Under the human's 2026-09-25 ruling ([[jarvis-x-model-priority]]), local models are slot 1, the top of the ladder, and the ruling asks to "include top tier Chinese open source models in local first, ollama" ([[chinese-open-source-models]]). The local Ollama runtime itself is free. Ollama also sells hosted cloud models; see "Ollama cloud" below.

**Confidence marks:** a figure marked `*` comes from a web-search excerpt in [[source-model-landscape-research]], not a fetched page, so treat it as medium confidence (it may be stale or paraphrased). Unmarked research figures were fetched directly; as-built figures come from the 2026-09-24 handoff.

## Install

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Current machine: ASUS Chromebook

> **Resolved by the human (2026-09-25):** the Chromebook is the current machine ([[jarvis-x-hardware]]). The Lenovo Y50-70 model list from the July plans is kept below under "Earlier plan (Lenovo Y50-70)".

The Chromebook runs Linux under [[crostini]]: CPU-only (11th Gen i5, no GPU), 14GB RAM with Chrome using ~10GB of it, and ~11GB free disk. Every local model has to fit inside that.

The first parts of this section are what the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) records about Ollama on the Chromebook. The recommended models and the "doesn't fit" list come from the 2026-09-25 research.

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

### Recommended models for the Chromebook (2026-09-25)

> **Recommendation (inference), not fact.** This is the researcher's recommended local-first stack from [[source-model-landscape-research]]. Nobody has tested it on the machine. The same list, with its place on the priority ladder, is on [[jarvis-x-model-priority]].

The research's test for "fits": ≤~8B parameters and a ≤~6GB download, with 6–9GB RAM free. "Borderline" means a 6–7.5GB download.

| Role | Recommended | Size |
|------|-------------|------|
| Everyday chat/agent | `qwen3:4b` (256K context*) or `qwen3.5:4b` (multimodal) | 2.5GB* / 3.4GB* |
| Higher-quality local | `qwen3:8b` in place of `qwen2.5:7b`; `qwen3.5:9b` only if RAM allows | 5.2GB* / 6.6GB* |
| Coding | keep `qwen2.5-coder:3b` / `:7b` (no small qwen3-coder exists*) | 1.9GB / 4.7GB |
| Reasoning | `deepseek-r1:8b`, or qwen3's thinking mode | 5.2GB* |
| Vision | `qwen3-vl:4b` or `gemma3:4b`; `gemma4:e2b-it-qat` is the only Gemma 4 build that fits | 3.3GB* / 3.3GB* / 4.3GB* |
| Tiny router/classifier | `qwen3:1.7b`, `qwen3.5:0.8b` or `gemma3:1b` | 1.4GB* / 1.0GB* / 815MB* |
| Embeddings | keep `nomic-embed-text`, or try `qwen3-embedding:0.6b` | 274MB / 639MB* |

- **Load one model at a time.** The fix-8 override below already sets `OLLAMA_MAX_LOADED_MODELS=1` and `OLLAMA_NUM_PARALLEL=1`.
- **Mind the disk.** With ~11GB free, pull models one by one and `ollama rm` the ones they replace.
- The Gemma 4 sizes look unusual; check with `ollama show` before pulling.
- Other families that fit (`glm4:9b` and MiniCPM-V, both borderline) are on [[chinese-open-source-models]].

### What doesn't fit on the Chromebook

| Model | Download size | Note |
|-------|---------------|------|
| `gpt-oss:20b` | 14GB* (128K context) | Ollama says gpt-oss-20b "can run on systems with as little as 16GB memory"*. It doesn't fit 14GB total RAM and ~11GB free disk. It is served free on [[groq]] instead. |
| `gpt-oss:120b` | 65GB* | |
| `qwen3:14b` / `30b` / `32b` / `235b` | 9.3GB / 19GB / 20GB / 142GB* | |
| `qwen3.5:27b` / `35b` / `122b` | 17GB / 24GB / 81GB* | |
| `qwen3.6:27b` / `35b` (+ coding variants) | 18GB / 23GB* | No small qwen3.6 tag exists |
| `qwen3.8:27b` | 18GB* | No small qwen3.8 tag exists |
| `qwen3-coder:30b` / `480b` | 19GB / 290GB* | No small qwen3-coder tag exists |
| `deepseek-r1:14b` / `32b` / `70b` / `671b` | 9.0GB / 20GB / 43GB / 404GB* | |
| `glm-4.7-flash` | 19GB and up* | |
| `gemma3:12b` / `27b` | 8.1GB / 17GB* | |
| `gemma3n:e2b` / `e4b` | 5.6GB / 7.5GB* | Borderline / borderline-no |
| `gemma4:e2b` / `e4b` / `12b` | 7.2GB / 9.6GB / 7.6GB* | Sizes look unusual; check with `ollama show` |
| `gemma4:26b` / `31b` | 19GB / 20GB* | |
| All Kimi, MiniMax, DeepSeek-V3.2/V4 and GLM-4.6 to GLM-5.3 models | none (cloud-only) | See "Ollama cloud" below |

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

## Ollama cloud

Ollama also hosts models it runs for you. The 2026-09-24 handoff doesn't mention Ollama cloud, so it isn't part of the as-built setup.

- Cloud models are hosted and "do not need to be downloaded"; access uses an API key or sign-in (fetched from Ollama's `docs/cloud.mdx` on GitHub).
- **Free plan:** it "includes a small amount of monthly usage for a set of starter models", with 1 concurrent request*. Pay-as-you-go credits unlock all models*. Which models are in the free starter set is unverified.
- **Billing:** per token*. The Team plan is $500/month with $1,000 credits*. Pro and Max prices come only from third-party excerpts, so they are unverified.

Cloud-only families on the Ollama library:

| Family | Cloud tags | Listed price per 1M |
|--------|-----------|---------------------|
| Kimi (Moonshot) | `kimi-k2`, `kimi-k2.5:cloud`, `kimi-k2.6:cloud`, `kimi-k2.7-code:cloud`, `kimi-k3:cloud`* | `kimi-k2.6:cloud`: $0.95 in / $4.00 out* |
| DeepSeek | `deepseek-v3.2:cloud` (160K), `deepseek-v4-pro:cloud`, `deepseek-v4-flash:cloud`, `deepseek-v4.1-flash:cloud` (1M)* | not covered by the research |
| GLM (Zhipu) | glm-4.6, glm-4.7, glm-5, glm-5.1, glm-5.2 (1M), glm-5.3, glm-5.3-flash* | not covered by the research |
| MiniMax | `minimax-m2:cloud`, m2.1, m2.5, m2.7, `minimax-m3:cloud`* | not covered by the research |
| Qwen (largest only) | `qwen3.5:397b-cloud`* | $0.60 in / $3.60 out* |

Interpretation under the ruling: the free plan's allowance is a slot-1 free hosted tier; per-token usage beyond it is paid. Kimi on Ollama cloud is per-token billed, so it stays in the paid slot ([[jarvis-x-model-priority]]).

## Role in Jarvis X (per the plans)

- Serves as the `local` tier in [[universal-model-layer]] (`jj ask --tier local`)
- Privacy-sensitive queries always route here — nothing leaves the machine
- [[hermes-agent]] runs on top of Ollama models
- `nomic-embed-text` powers ChromaDB vector search in [[obsidian]]

The bullets above describe the plan. In the 2026-09-24 handoff, the `local` tier is reached through `POST /api/ask` and the `/v1` adapter (`"model": "local"`). The handoff doesn't mention a `jj` CLI or privacy-based routing, so whether either exists is unknown. See "Current machine: ASUS Chromebook" above.

## Earlier plan (Lenovo Y50-70)

This is the July 2026 master plan's view, written for the Lenovo Y50-70 on Pop!_OS. It is kept as the plans' record; the 2026-09-25 ruling makes the Chromebook current ([[jarvis-x-hardware]]).

### Essential models (CPU-first, Lenovo Y50-70)

From the July 2026 master plan. For the models on the current machine, see "Current machine: ASUS Chromebook" above.

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

### Hardware constraint (Lenovo)

On the Lenovo Y50-70 the plan described (CPU-only in practice because its GPU was undetected, 7.7GB RAM), `hermes3:8b` is too slow for interactive use (1–3 t/s). The plan marks it "Future (GPU/16GB RAM)". That takes more than the plan's Phase 1 upgrade, which is "16GB DDR3L RAM + 2TB SSD". The GPU path comes later: Phase 2 is the eGPU (ADT-Link R43SG + 850W PSU), and Phase 3 is the NVIDIA RTX 3090 (24GB VRAM) ([[jarvis-x-hardware]]).

> **Corrected (2026-09-25):** this page previously said `hermes3:8b` was "Unlocked after Phase 1 hardware upgrade (16GB RAM + GPU)". The master plan's hardware upgrade roadmap gives Phase 1 as "16GB DDR3L RAM + 2TB SSD", with no GPU. The eGPU is Phase 2 and the RTX 3090 is Phase 3. The plan itself doesn't tie `hermes3:8b` to a phase. The old sentence also called the Lenovo "the current [[jarvis-x-hardware]]"; the 2026-09-25 ruling makes the Chromebook current.

These figures describe the Lenovo Y50-70 in the earlier plans. The disagreement with the 2026-09-24 handoff's machine is noted below.

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** the "Essential models (CPU-first, Lenovo Y50-70)" list above (`llama3.2:3b`, `qwen3:1.5b`, `nomic-embed-text`, `hermes3:8b`) and the "7.7GB RAM" hardware constraint come from the earlier plans. They describe a Lenovo Y50-70. The handoff's machine is an ASUS Chromebook with 14GB RAM (11th Gen i5, no GPU). Its models are the `qwen2.5` family plus `nomic-embed-text`. Of the plan's list, only `nomic-embed-text` is present, at 274MB against the plan's "~0.5GB" estimate. Unknown: whether the plan's model list was deliberately replaced, and whether the hermes3:8b "unlock" condition still applies on the new machine. The handoff's ~10 tok/s for `qwen2.5:7b` is reported for different hardware and a different model than the plan's 1–3 t/s for `hermes3:8b`, so the two figures are not directly comparable. Both are kept. Left for the human to resolve.
>
> **Resolved by the human (2026-09-25): the Chromebook is current.** That settles the machine. The model questions above stay open: the ruling sets a priority order ([[jarvis-x-model-priority]]), not a model list, and it doesn't address `hermes3:8b`. Implication: the Chromebook has 14GB RAM and no GPU, so it meets neither part of the plan's "GPU/16GB RAM" condition.

## Related

[[jarvis-x]] | [[hermes-agent]] | [[universal-model-layer]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[jarvis-x-hardware]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[starnet]] | [[gemini]] | [[groq]] | [[openrouter]] | [[crostini]] | [[free-api-tiers]] | [[aider]] | [[source-jarvis-x-starnet-handoff]] | [[source-model-landscape-research]] | [[jarvis-x-plan-vs-reality]]
