# Model landscape research for Jarvis X (Chromebook, CPU-only)
# Date: 2026-09-25
# Author: research subagent in the Claude Code session (web research; not a human-written source)

---

## How to read this note

- **[F]** means the page was fetched and read directly.
- **[S]** means the fact comes from a web-search result excerpt for that exact URL; the page itself was not fetched. [S] facts may be stale or paraphrased, so treat them as medium confidence.
- The network proxy blocked direct fetches of ollama.com, docs.ollama.com, console.groq.com, groq.com, ai.google.dev, openrouter.ai, openai.com, developers.openai.com, platform.moonshot.ai, platform.kimi.ai, huggingface.co, blog.google and docs.cloud.google.com. GitHub, claude.com and platform.claude.com could be fetched.
- "Fits?" assumes ≤~8B parameters and a ≤~6GB download, with 6–9GB RAM free (the Chromebook: 14GB total, Chrome uses ~10GB, ~11GB free disk). "Borderline" means a 6–7.5GB download.

## 1. Chinese open-source families on the Ollama library

### Qwen (Alibaba)

| Family | Tag | Size / context | Fits? | Source |
|---|---|---|---|---|
| qwen3 | 0.6b / 1.7b | 523MB / 1.4GB, 40K | Yes | [S] https://ollama.com/library/qwen3/tags |
| qwen3 | 4b | 2.5GB, 256K | Yes | same |
| qwen3 | 8b (latest) | 5.2GB, 40K | Yes, tight | same |
| qwen3 | 14b / 30b / 32b / 235b | 9.3GB / 19GB / 20GB / 142GB | No | same |
| qwen3.5 (multimodal, 256K) | 0.8b / 2b / 4b | 1.0GB / 2.7GB / 3.4GB | Yes | [S] https://ollama.com/library/qwen3.5/tags |
| qwen3.5 | 9b | 6.6GB | Borderline | [S] https://ollama.com/library/qwen3.5:9b-q4_K_M |
| qwen3.5 | 27b / 35b / 122b | 17GB / 24GB / 81GB | No | [S] qwen3.5/tags |
| qwen3.5 | 397b-cloud | cloud; $0.60 in / $3.60 out per 1M | Cloud | [S] https://ollama.com/library/qwen3.5:397b-cloud |
| qwen3.6 | 27b / 35b (+ coding variants) | 18GB / 23GB | No | [S] https://ollama.com/library/qwen3.6/tags |
| qwen3.8 | 27b (latest) | 18GB, 256K | No | [S] https://ollama.com/library/qwen3.8/tags |
| qwen3-coder | 30b / 480b | 19GB / 290GB | No | [S] https://ollama.com/library/qwen3-coder/tags |
| qwen3-vl (256K) | 2b / 4b | 1.9GB / 3.3GB | Yes | [S] https://ollama.com/library/qwen3-vl/tags |
| qwen3-vl | 8b | 6.1GB | Borderline | same |
| qwen3-embedding | 0.6b / 4b / 8b | 639MB / 2.5GB / 4.7GB | Yes | [S] https://ollama.com/library/qwen3-embedding/tags |
| qwen2.5 (32K) | 0.5b / 1.5b / 3b / 7b | 398MB / 986MB / 1.9GB / 4.7GB | Yes | [S] https://ollama.com/library/qwen2.5/tags |
| qwen2.5-coder (32K) | 0.5b / 1.5b / 3b / 7b | 398MB / 986MB / 1.9GB / 4.7GB | Yes | [S] https://ollama.com/library/qwen2.5-coder/tags |

There is no small qwen3-coder, qwen3.6 or qwen3.8 tag; the smallest is about 18–19GB.

### DeepSeek

| Tag | Size | Fits? | Source |
|---|---|---|---|
| deepseek-r1:1.5b | 1.1GB | Yes | [S] https://ollama.com/library/deepseek-r1/tags |
| deepseek-r1:7b | 4.7GB | Yes | same |
| deepseek-r1:8b (latest) | 5.2GB | Yes, tight | same |
| deepseek-r1:14b / 32b / 70b / 671b | 9.0GB / 20GB / 43GB / 404GB | No | same |

- deepseek-r1 context is 128K (160K on 671b).
- Cloud-only on Ollama: `deepseek-v3.2:cloud` (160K), `deepseek-v4-pro:cloud` (1M), `deepseek-v4-flash:cloud` (1M), `deepseek-v4.1-flash:cloud` (1M). [S] https://ollama.com/library/deepseek-v3.2/tags, https://ollama.com/library/deepseek-v4-flash/tags

### Zhipu (Z.ai) GLM

- `glm4:9b`: 5.5GB, q4_0, 9.4B parameters, 128K context. Borderline but workable. [S] https://ollama.com/library/glm4/tags
- `glm-4.7-flash` (30B-A3B MoE): 19GB and up. No. [S] https://ollama.com/library/glm-4.7-flash/tags
- Cloud: glm-4.6, glm-4.7, glm-5, glm-5.1, glm-5.2 (1M), glm-5.3, glm-5.3-flash. [S] https://ollama.com/library/glm-5.2:cloud

### Moonshot (Kimi): all cloud on Ollama

- `kimi-k2` (1T total / 32B active, 256K), `kimi-k2.5:cloud`, `kimi-k2.6:cloud` ($0.95 in / $4.00 out per 1M), `kimi-k2.7-code:cloud`, `kimi-k3:cloud` (2.81T). [S] https://ollama.com/library/kimi-k2, https://ollama.com/library/kimi-k2.6:cloud, https://ollama.com/library/kimi-k3:cloud

### MiniMax: cloud

- `minimax-m2:cloud` (230B total / 10B active), m2.1, m2.5, m2.7, `m3:cloud`. [S] https://ollama.com/library/minimax-m3:cloud

### OpenBMB MiniCPM-V (vision)

- `minicpm-v:8b` (v2.6): 5.5–5.7GB. `minicpm-v4.5:8b` (on Qwen3-8B): 5.9GB. Borderline but OK. [S] https://ollama.com/library/minicpm-v/tags, https://ollama.com/library/minicpm-v4.5

### Tencent and Baidu

- Tencent Hunyuan only as a community upload (`alibayram/hunyuan`); sizes unverified. No Baidu ERNIE found on Ollama.

### Ollama cloud: free or paid?

- Cloud models are hosted and "do not need to be downloaded"; access uses an API key or sign-in. [F] https://raw.githubusercontent.com/ollama/ollama/main/docs/cloud.mdx
- The free plan "includes a small amount of monthly usage for a set of starter models", with 1 concurrent request; pay-as-you-go credits unlock all models. [S] https://ollama.com/pricing, https://ollama.com/blog/transparent-pricing
- Billing is per token. Team is $500/month with $1,000 credits. Pro/Max prices come only from third-party excerpts, so they are unverified. Which models are in the free starter set is unverified.
- The local Ollama runtime itself is free.

## 2. Google open models on Ollama

| Tag | Size / context | Fits? | Source |
|---|---|---|---|
| gemma3:270m / 1b | 292MB / 815MB, 32K | Yes | [S] https://ollama.com/library/gemma3/tags |
| gemma3:4b | 3.3GB, 128K, vision | Yes | same |
| gemma3:12b / 27b | 8.1GB / 17GB | No | same |
| gemma3n:e2b / e4b | 5.6GB / 7.5GB | Borderline / borderline-no | [S] https://ollama.com/library/gemma3n/tags |
| gemma4:e2b-it-qat | 4.3GB, 128K | Yes | [S] https://ollama.com/library/gemma4:e2b-it-qat |
| gemma4:e2b / e4b / 12b | 7.2GB / 9.6GB / 7.6GB | No | [S] https://ollama.com/library/gemma4/tags |
| gemma4:26b / 31b | 19GB / 20GB | No | same |

The Gemma 4 sizes look unusual; check with `ollama show` before pulling.

## 3. OpenAI open-weight on Ollama

- `gpt-oss:20b` is a 14GB download (128K); `gpt-oss:120b` is 65GB. [S] https://ollama.com/library/gpt-oss/tags
- gpt-oss-20b "can run on systems with as little as 16GB memory". [S] https://ollama.com/blog/gpt-oss
- It does not fit a machine with 14GB total RAM and ~11GB free disk.

## 4. Groq free tier

- `openai/gpt-oss-120b` and `openai/gpt-oss-20b` are still listed. [S] https://console.groq.com/docs/models
- `qwen/qwen3.8-27b` is listed (paid price $0.80 / $4.00 per 1M). [S] https://console.groq.com/docs/model/qwen/qwen3.8-27b
- Deprecated: `moonshotai/kimi-k2-instruct-0905` (announced Mar 23, 2026, replaced by gpt-oss-120b); `qwen/qwen3-32b`, `llama-4-scout`, `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` (announced June 17, 2026). [S] https://console.groq.com/docs/deprecations
- Free-tier limits for `openai/gpt-oss-120b`: 30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD per organization, measured Sept 14, 2026. [F] https://github.com/Antoniodeoliveirasegura/boilerindy/issues/253 and [S] https://console.groq.com/docs/rate-limits. The same numbers for gpt-oss-20b come only from third-party excerpts.
- Chinese models on Groq now: Qwen yes; Kimi no (deprecated); DeepSeek none found.

## 5. OpenRouter free models

All [S]; current availability of each `:free` model is unverified (retired pages can stay indexed).

| Vendor | `:free` IDs found |
|---|---|
| DeepSeek | `deepseek/deepseek-v4-flash:free`, `deepseek/deepseek-r1:free`, `deepseek/deepseek-chat-v3-0324:free` |
| Qwen | `qwen/qwen3.8-27b:free`, `qwen/qwen3-coder:free`, `qwen/qwen3.6-plus:free` |
| Kimi | `moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`, `moonshotai/kimi-dev-72b:free` |
| GLM | `z-ai/glm-5.2:free`, `z-ai/glm-5.1:free`, `z-ai/glm-4.5-air:free` |
| MiniMax | `minimax/minimax-m2.5:free`, `minimax/minimax-m2:free` |
| Gemma | `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, `google/gemma-3-27b-it:free`, `google/gemma-3-4b-it:free`, `google/gemma-3n-e4b-it:free` |
| gpt-oss | `openai/gpt-oss-120b:free`, `openai/gpt-oss-20b:free` |
| Router | `openrouter/free` picks a free model automatically |

- Limits: 50 requests/day without credits; a one-time $10 credit purchase raises it to 1,000/day; both capped at 20 RPM. [S] https://openrouter.ai/docs/api_reference/limits

## 6. Google free tier

- Gemini API pricing page: "Start building free of charge with generous limits". [S] https://ai.google.dev/gemini-api/docs/pricing
- `gemini-3.6-flash` is listed and GA. [S] https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash. The pricing excerpt shows its free-tier input as "Free of charge".
- Other Flash models listed: `gemini-3.8-flash` (newest), `gemini-3.7-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`, alias `gemini-flash-latest`. Google's guidance: "For new projects use 3.5 Flash-Lite or 3.8 Flash." [S] https://ai.google.dev/gemini-api/docs/models
- Conflicts: whether 3.8 Flash has an API free tier (one excerpt "Not available"; a forum title "Gemini 3.8 Flash Free Tier 20 RPD"), and whether 3.1 Pro has one.
- Per-model rate limits are published only in AI Studio. A third party reports ~20 RPD for the 3.5–3.8 Flash models and ~500 RPD for 3.5 / 3.1 Flash-Lite (Sept 2026). https://www.scriptbyai.com/gemini-api-free-tier-limits/
- Gemini CLI README: Google login gives "60 requests/min and 1,000 requests/day with personal Google account"; an API key gives "1000 requests/day with Gemini 3 (mix of flash and pro)". [F] https://github.com/google-gemini/gemini-cli/blob/main/README.md. The repo's quota doc instead says 1,000/day for Google login and 250/day, Flash only, for an unpaid API key. [F] https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/resources/quota-and-pricing.md. These conflict for the API-key route.

## 7. Kimi / Moonshot

- The API is paid: "There is no permanent Kimi API free tier for production usage." [S] https://www.kimi.ai/help/kimi-api/api-pricing, https://platform.kimi.ai/docs/pricing/chat
- API prices per 1M tokens: K3 $3.00 in (cache miss) / $0.30 (cache hit) / $15.00 out; K2.6 $0.95 in / $4.00 out; K2.7 Code $0.95 / $0.19 / $4.00 standard ($8.00 high-speed). [S] same
- Open weights: Kimi K2 is under a Modified MIT License (MIT plus a "Kimi K2" display requirement above 100M MAU or $20M monthly revenue). [F] https://raw.githubusercontent.com/MoonshotAI/Kimi-K2/main/LICENSE. Kimi K3 (2.8T total / 104B active, 1M context) has weights on Hugging Face under the "Kimi K3 License" (MIT-style; a separate agreement for model-as-a-service revenue above $20M over 12 months; branding rule above 100M MAU or $20M monthly revenue). [F] https://github.com/MoonshotAI/Kimi-K3, https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/LICENSE
- Free elsewhere: Groq no (deprecated); OpenRouter `kimi-k2.6:free` and `kimi-k2:free` are listed but availability is unverified; Ollama cloud is per-token billed.
- Verdict: Kimi belongs in the paid slot; the only possible free route is OpenRouter `:free`, if still live.

## 8. Anthropic and OpenAI

- Anthropic: no ongoing free API tier; "New users receive a small amount of free credits to test the API." [F] https://platform.claude.com/docs/en/about-claude/pricing. Prices per MTok: Haiku 4.5 $1 / $5; Sonnet 5 $2 / $10; Opus 5.5 $4 / $20; Fable 5.1 $10 / $50; Batch API 50% off. [F] same
- OpenAI: the pricing page was blocked, so prices are unverified. The rate-limits guide lists a "Free" usage tier ("User must be in an allowed geography", $100/month usage limit); which models it can use is unverified. [S] https://developers.openai.com/api/docs/guides/rate-limits. The practical free OpenAI path is gpt-oss through Groq, OpenRouter `:free` or Ollama cloud.

## Recommended local-first stack for this Chromebook (the researcher's inference, not a fact)

1. Everyday chat/agent: `qwen3:4b` (2.5GB, 256K) or `qwen3.5:4b` (3.4GB, multimodal).
2. Higher-quality local: `qwen3:8b` (5.2GB) in place of qwen2.5:7b; `qwen3.5:9b` (6.6GB) only if RAM allows.
3. Coding: keep `qwen2.5-coder:3b` / `:7b` (no small qwen3-coder exists).
4. Reasoning: `deepseek-r1:8b` (5.2GB) or qwen3's thinking mode.
5. Vision: `qwen3-vl:4b` (3.3GB) or `gemma3:4b` (3.3GB); `gemma4:e2b-it-qat` (4.3GB) is the only Gemma 4 build that fits.
6. Tiny router/classifier: `qwen3:1.7b`, `qwen3.5:0.8b` or `gemma3:1b`.
7. Embeddings: keep `nomic-embed-text` or try `qwen3-embedding:0.6b` (639MB).
8. Avoid locally: gpt-oss:20b (14GB), qwen3.6 / 3.8 / coder, glm-4.7-flash, and all Kimi, MiniMax, DeepSeek-V4 and GLM-5 models.

Load one model at a time; with ~11GB free disk, pull models one by one and `ollama rm` what they replace.

## Could not verify

Everything on ollama.com, console.groq.com, ai.google.dev, openrouter.ai, openai.com and platform.kimi.ai (search excerpts only); Ollama Pro/Max prices and the free starter-model list; Groq's Qwen free limits; live availability of each OpenRouter `:free` model; Gemini 3.8 Flash / 3.1 Pro free-tier status and official per-model limits; the Gemini CLI API-key limit (1,000/day vs 250/day Flash-only); all OpenAI prices; Kimi K2.6's cache-hit price; some Ollama sizes (qwen2.5:72b, embeddinggemma, openbmb/minicpm-v4, alibayram/hunyuan). The Gemma 4 e2b/e4b sizes should be checked with `ollama show`.
