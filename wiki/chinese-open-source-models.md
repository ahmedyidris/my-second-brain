---
title: Chinese Open-Source Models
tags: [concept, models, open-weights, local-ai, chinese-models, ollama, jarvis-x]
sources:
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x-model-priority]], [[ollama]], [[groq]], [[openrouter]], [[free-api-tiers]], [[the-council]], [[jarvis-x-hardware]], [[jarvis-x-runtime]], [[source-model-landscape-research]]
last_updated: 2026-09-25
---

# Chinese Open-Source Models

Open-weight model families from Chinese labs: Qwen (Alibaba), DeepSeek, GLM (Zhipu / Z.ai), Kimi (Moonshot), MiniMax and MiniCPM (OpenBMB). Tencent's Hunyuan shows up only as a community upload. For each family, this page records what runs locally on the current Chromebook through [[ollama]], what is cloud-only, and where it is hosted for free.

**Confidence marks:** a figure marked `*` comes from a web-search excerpt in [[source-model-landscape-research]], not a fetched page, so treat it as medium confidence (it may be stale or paraphrased). Unmarked research figures were fetched directly; as-built figures come from the 2026-09-24 handoff.

## Why it matters

The human's 2026-09-25 ruling ([[jarvis-x-model-priority]]) names these models: "also include top tier Chinese open source models in local first, ollama". Local models and free open-source tiers are slot 1, the top of the ladder.

Jarvis already runs one. The as-built `local` tier is `qwen2.5:3b` (Alibaba's Qwen), and StarNet's agent Raqib runs `qwen2.5:7b` ("slow — ~10 tok/s") ([[jarvis-x-runtime]]).

Implication: the big models in these families (Kimi K2/K3, DeepSeek-V4, GLM-5, MiniMax M2/M3, qwen3.6, qwen3.8, qwen3-coder) are cloud-only on Ollama or far too big for the Chromebook. Locally, the ruling can be met only with the smaller siblings: qwen3 up to 8b, qwen3.5 up to 9b, deepseek-r1 up to 8b, glm4:9b and MiniCPM-V 8b, with the 8–9b builds tight or borderline. The bigger models reach slot 1 only through a free hosted tier, and the ones found are listed but unverified (see below).

## What "fits" means here

The Chromebook is CPU-only (11th Gen i5, no GPU), with 14GB RAM, of which Chrome uses ~10GB, and ~11GB free disk ([[jarvis-x-hardware]]). The research's test: ≤~8B parameters and a ≤~6GB download, with 6–9GB RAM free. "Borderline" means a 6–7.5GB download. Sizes below are download sizes.

## At a glance

| Family | Lab | Fits locally (Ollama) | Cloud-only on Ollama | Free hosted |
|--------|-----|-----------------------|----------------------|-------------|
| Qwen | Alibaba | Yes: qwen2.5, qwen2.5-coder, qwen3 up to 8b, qwen3.5 up to 4b (9b borderline), qwen3-vl 2b/4b, qwen3-embedding | `qwen3.5:397b-cloud`* | [[groq]] lists `qwen/qwen3.8-27b`* (free limits unverified); [[openrouter]] `:free` IDs listed |
| DeepSeek | DeepSeek | Yes: deepseek-r1 1.5b / 7b / 8b | DeepSeek-V3.2, V4-Pro, V4-Flash, V4.1-Flash* | OpenRouter `:free` IDs listed; none found on Groq* |
| GLM | Zhipu (Z.ai) | Borderline: `glm4:9b` | glm-4.6 through glm-5.3* | OpenRouter `:free` IDs listed |
| Kimi | Moonshot | No | All of them* | OpenRouter `:free` IDs listed; deprecated on Groq* |
| MiniMax | MiniMax | No | All of them (m2 through m3)* | OpenRouter `:free` IDs listed |
| MiniCPM-V | OpenBMB | Borderline: `minicpm-v:8b`, `minicpm-v4.5:8b` | Not covered by the research | Not covered by the research |
| Hunyuan | Tencent | Only the community upload `alibayram/hunyuan`; sizes unverified | Not covered by the research | Not covered by the research |

All OpenRouter `:free` IDs are from search excerpts*, and the current availability of each is unverified (retired pages can stay indexed). OpenRouter's free limits: 50 requests/day without credits; a one-time $10 credit purchase raises it to 1,000/day; both capped at 20 RPM*.

No Baidu ERNIE model was found on Ollama.

## Qwen (Alibaba)

**Present now** (handoff): `qwen2.5:7b` (4.7GB), `qwen2.5:3b` (1.9GB), `qwen2.5-coder:7b` (4.7GB), `qwen2.5-coder:3b` (1.9GB).

| Family | Tag | Size / context | Fits? |
|--------|-----|----------------|-------|
| qwen3 | 0.6b / 1.7b | 523MB / 1.4GB, 40K* | Yes |
| qwen3 | 4b | 2.5GB, 256K* | Yes |
| qwen3 | 8b (latest) | 5.2GB, 40K* | Yes, tight |
| qwen3 | 14b / 30b / 32b / 235b | 9.3GB / 19GB / 20GB / 142GB* | No |
| qwen3.5 (multimodal, 256K) | 0.8b / 2b / 4b | 1.0GB / 2.7GB / 3.4GB* | Yes |
| qwen3.5 | 9b | 6.6GB* | Borderline |
| qwen3.5 | 27b / 35b / 122b | 17GB / 24GB / 81GB* | No |
| qwen3.6 | 27b / 35b (+ coding variants) | 18GB / 23GB* | No |
| qwen3.8 | 27b (latest) | 18GB, 256K* | No |
| qwen3-coder | 30b / 480b | 19GB / 290GB* | No |
| qwen3-vl (256K) | 2b / 4b | 1.9GB / 3.3GB* | Yes |
| qwen3-vl | 8b | 6.1GB* | Borderline |
| qwen3-embedding | 0.6b / 4b / 8b | 639MB / 2.5GB / 4.7GB* | Yes |
| qwen2.5 (32K) | 0.5b / 1.5b / 3b / 7b | 398MB / 986MB / 1.9GB / 4.7GB* | Yes |
| qwen2.5-coder (32K) | 0.5b / 1.5b / 3b / 7b | 398MB / 986MB / 1.9GB / 4.7GB* | Yes |

There is no small qwen3-coder, qwen3.6 or qwen3.8 tag; the smallest is about 18–19GB*.

- **Cloud-only on Ollama:** `qwen3.5:397b-cloud`, at $0.60 in / $3.60 out per 1M*.
- **Groq:** `qwen/qwen3.8-27b` is listed, with a paid price of $0.80 in / $4.00 out per 1M*. Its free-tier limits were not verified. `qwen/qwen3-32b` is deprecated (announced June 17, 2026)*.
- **OpenRouter `:free`:** `qwen/qwen3.8-27b:free`, `qwen/qwen3-coder:free`, `qwen/qwen3.6-plus:free`*.

## DeepSeek

| Tag | Size | Fits? |
|-----|------|-------|
| `deepseek-r1:1.5b` | 1.1GB* | Yes |
| `deepseek-r1:7b` | 4.7GB* | Yes |
| `deepseek-r1:8b` (latest) | 5.2GB* | Yes, tight |
| `deepseek-r1:14b` / `32b` / `70b` / `671b` | 9.0GB / 20GB / 43GB / 404GB* | No |

deepseek-r1's context is 128K (160K on the 671b)*.

- **Cloud-only on Ollama:** `deepseek-v3.2:cloud` (160K), `deepseek-v4-pro:cloud` (1M), `deepseek-v4-flash:cloud` (1M), `deepseek-v4.1-flash:cloud` (1M)*. Their Ollama cloud prices are not covered by the research.
- **Groq:** no DeepSeek model found*.
- **OpenRouter `:free`:** `deepseek/deepseek-v4-flash:free`, `deepseek/deepseek-r1:free`, `deepseek/deepseek-chat-v3-0324:free`*.

## GLM (Zhipu / Z.ai)

- `glm4:9b`: 5.5GB, q4_0, 9.4B parameters, 128K context. Borderline but workable*.
- `glm-4.7-flash` (a 30B-A3B mixture-of-experts): 19GB and up. Doesn't fit*.
- **Cloud-only on Ollama:** glm-4.6, glm-4.7, glm-5, glm-5.1, glm-5.2 (1M), glm-5.3, glm-5.3-flash*. Prices not covered by the research.
- **Groq:** not covered by the research.
- **OpenRouter `:free`:** `z-ai/glm-5.2:free`, `z-ai/glm-5.1:free`, `z-ai/glm-4.5-air:free`*.

## Kimi (Moonshot)

Every Kimi model on Ollama is cloud-only, so nothing runs locally on the Chromebook.

- **Cloud-only on Ollama:** `kimi-k2` (1T total / 32B active, 256K), `kimi-k2.5:cloud`, `kimi-k2.6:cloud` ($0.95 in / $4.00 out per 1M), `kimi-k2.7-code:cloud`, `kimi-k3:cloud` (2.81T)*.
- **Open weights (fetched):** Kimi K2's weights are under a Modified MIT License. Kimi K3 is 2.8T total / 104B active parameters with a 1M context, and its weights are on Hugging Face under the "Kimi K3 License" (see Licenses below). Implication: Kimi K2 and K3 are far too big for local use on this machine.
- **Kimi API:** paid. "There is no permanent Kimi API free tier for production usage."* Prices per 1M tokens: K3 $3.00 in (cache miss) / $0.30 (cache hit) / $15.00 out; K2.6 $0.95 in / $4.00 out; K2.7 Code $0.95 / $0.19 / $4.00 standard ($8.00 high-speed)*.
- **Groq:** `moonshotai/kimi-k2-instruct-0905` is deprecated (announced Mar 23, 2026, replaced by gpt-oss-120b)*.
- **OpenRouter `:free`:** `moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`, `moonshotai/kimi-dev-72b:free`*. Availability unverified.

Under the ruling, Kimi goes in the paid slot because its API is not free. The one possible free route is OpenRouter `:free`, if still live ([[jarvis-x-model-priority]]).

## MiniMax

- **Cloud-only on Ollama:** `minimax-m2:cloud` (230B total / 10B active), m2.1, m2.5, m2.7, `minimax-m3:cloud`*. Nothing runs locally. Prices not covered by the research.
- **OpenRouter `:free`:** `minimax/minimax-m2.5:free`, `minimax/minimax-m2:free`*.

## MiniCPM-V (OpenBMB, vision)

- `minicpm-v:8b` (v2.6): 5.5–5.7GB*. `minicpm-v4.5:8b` (built on Qwen3-8B): 5.9GB*. Borderline but OK.
- The size of `openbmb/minicpm-v4` is unverified.

## Tencent Hunyuan

Per the research, Hunyuan is on Ollama only as a community upload, `alibayram/hunyuan`. Its sizes are unverified.

## Licenses

The research has licenses only for Kimi. Both were fetched from Moonshot's GitHub:

| Model | License | Key terms |
|-------|---------|-----------|
| Kimi K2 | Modified MIT License | MIT, plus a "Kimi K2" display requirement above 100M monthly active users or $20M monthly revenue. https://raw.githubusercontent.com/MoonshotAI/Kimi-K2/main/LICENSE |
| Kimi K3 | "Kimi K3 License" | MIT-style. A separate agreement is needed for model-as-a-service revenue above $20M over 12 months. A branding rule applies above 100M monthly active users or $20M monthly revenue. https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/LICENSE |

The licenses for Qwen, DeepSeek, GLM, MiniMax, MiniCPM and Hunyuan are not covered by the research.

## The Council's DeepSeek and Kimi seats

[[the-council]] has three seats on these families: Kimi K2.6 (Long-Horizon Builder), DeepSeek V4-Pro (Refactorer) and DeepSeek V4-Flash (Fast Sub-Agent).

- On Ollama, all three are cloud-only: `kimi-k2.6:cloud`, `deepseek-v4-pro:cloud` and `deepseek-v4-flash:cloud`*. Implication: none of them can run locally on the Chromebook.
- Possible free routes: OpenRouter `deepseek/deepseek-v4-flash:free` and `moonshotai/kimi-k2.6:free`*, both unverified. The research found no `:free` ID for DeepSeek V4-Pro.
- The Kimi seat goes in the paid slot under the ruling. The handoff's Bug E adds that a consumer Kimi subscription gives no API access ([[free-api-tiers]]).

## Recommended picks for the Chromebook (inference)

> **Recommendation, not fact.** The researcher's recommended local-first stack is on [[jarvis-x-model-priority]]. Its Chinese-model picks: `qwen3:4b` or `qwen3.5:4b` for everyday chat, `qwen3:8b` in place of `qwen2.5:7b`, keep `qwen2.5-coder:3b` / `:7b` for coding, `deepseek-r1:8b` for reasoning, `qwen3-vl:4b` for vision, `qwen3:1.7b` or `qwen3.5:0.8b` as a tiny router, and `qwen3-embedding:0.6b` as an embeddings option. Load one model at a time, and with ~11GB free disk, `ollama rm` whatever a new model replaces.

## Related

[[jarvis-x-model-priority]] | [[ollama]] | [[groq]] | [[openrouter]] | [[free-api-tiers]] | [[the-council]] | [[jarvis-x-hardware]] | [[jarvis-x-runtime]] | [[source-model-landscape-research]]
