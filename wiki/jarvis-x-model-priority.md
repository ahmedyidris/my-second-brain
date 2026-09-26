---
title: Jarvis X Model Priority
tags: [jarvis-x, models, providers, ruling, local-first, chromebook]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
related: [[universal-model-layer]], [[free-api-tiers]], [[ollama]], [[chinese-open-source-models]], [[groq]], [[gemini]], [[openrouter]], [[the-council]], [[hermes-agent]], [[jarvis-x-hardware]], [[crostini]], [[jarvis-x]], [[jarvis-x-runtime]], [[jarvis-x-plan-vs-reality]], [[source-model-landscape-research]]
last_updated: 2026-09-25
---

# Jarvis X Model Priority

The human's ruling, from 2026-09-25, on which models and providers [[jarvis-x]] plans should reach for first. It sits on top of the [[universal-model-layer]]: the layer says how providers plug in, and this page says in what order to prefer them.

**Confidence marks:** a figure marked `*` comes from a web-search excerpt in [[source-model-landscape-research]], not a fetched page, so treat it as medium confidence (it may be stale or paraphrased). Unmarked research figures were fetched directly; as-built figures come from the 2026-09-24 handoff.

## The ruling (verbatim)

> "priority for plans, local models and free open source tiers that could work on any machine specially chrome os, then most free available from google then Anthropic then open ai, if kimi is not free treat as a paid subscription and put in paid tiers slot but also include top tier Chinese open source models in local first, ollama…."

Source: `raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md`.

## The ladder

| Priority | Slot | What goes here |
|----------|------|----------------|
| 1 | **Local and free open-source** | Local models on [[ollama]] and free open-source tiers that "could work on any machine specially chrome os". This slot explicitly includes "top tier Chinese open source models" via Ollama. |
| 2 | **Google, free** | "the most free available from google" |
| 3 | **Anthropic** | Anthropic models |
| 4 | **OpenAI** | OpenAI models |
| Paid | **Paid models, standalone** | Kimi's paid API models ("if kimi is not free", and "if it's paid put it as standalone paid model"). $0/month still binds, so these are options only. |

**Kimi:** under the follow-up ruling (below), a paid Kimi model is listed as a standalone paid model, with no ranking against Anthropic or OpenAI. Any free Kimi route goes in the free tiers, under the provider that serves it.

## Follow-up rulings (2026-09-25, second reply)

Source: `raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md`. These answer the questions this page had left open.

1. **Free counts as free.** "If it's free make it count as free", and "if free 100% should be in free tier". Keep each model's official name, even when it says OpenAI (e.g. `openai/gpt-oss-120b`). So gpt-oss on a free provider tier is in the free tier.
2. **Fits both → both.** "if it fits both let it be in both". Gemma is listed under local/open (slot 1) and under Google (slot 2).
3. **Organize by provider.** "Kimi is Kimi". A paid Kimi model is a "standalone paid model", and a free one goes in the free tiers "and also how it should be accessible". More generally, "all models that are free and accessible through a provider should be done through and under that provider even if it could be done through another one, it will also be there". So a model free through two providers is listed under both.
4. **Tier names stay as they are** (`local`, `fast`, `smart`, `quality`, `frontier`). "copy Starnet way, it should be either by provider using api or local": each model is picked either locally or from a provider through its API, the way StarNet's model picker works (e.g. "OLLAMA → qwen2.5:7b").
5. **Lenovo:** "ignore it for now" ([[jarvis-x-hardware]]).
6. **stream:false:** "I don't know". Still open ([[starnet]]).
7. **Budget:** "Still zero but leave it as an option". $0/month still binds; paid routes stay listed as options.
8. **Tokens:** "Yes we need more tokens". See "Getting more tokens" below.

## What "any machine, especially ChromeOS" rules out

The current machine is the Chromebook ([[jarvis-x-hardware]]): CPU-only, 14GB RAM with Chrome using ~10GB of it, and ~11GB free disk. Implication: a slot-1 local model has to run on the CPU inside that memory and disk. Large open models can only fill slot 1 through a free hosted tier, not locally.

The research's working test for "fits" on this machine is ≤~8B parameters and a ≤~6GB download, with 6–9GB RAM free. "Borderline" means a 6–7.5GB download ([[source-model-landscape-research]]).

## Catalog by access route (2026-09-25)

Per follow-up ruling 3, each free model is listed under every provider that serves it free, so a model can appear more than once. Per ruling 4, a model is reached one of two ways: **local** (Ollama on the Chromebook) or **a provider's API**. Each route shows its slot on the ladder.

Drawn from the 2026-09-25 web research ([[source-model-landscape-research]]) and the 2026-09-24 handoff. Sizes are download sizes. Free tiers and model lists change often, so re-check before building on any single entry.

### Local: Ollama on the Chromebook (free; slot 1, and Gemma also slot 2)

The full per-family lists, including what doesn't fit, are on [[chinese-open-source-models]] and [[ollama]].

| Model (official Ollama tag) | Size | Fits the Chromebook? | Notes |
|--------|------|----------------------|-------|
| `qwen2.5:3b` | 1.9GB | Present now | Jarvis `local` tier (handoff) |
| `qwen2.5:7b` | 4.7GB | Present now | StarNet's Raqib, "slow — ~10 tok/s" (handoff) |
| `qwen2.5-coder:3b` / `:7b` | 1.9GB / 4.7GB | Present now | Coding models |
| `nomic-embed-text` | 274MB | Present now | Embeddings |
| `qwen3:0.6b` / `1.7b` / `4b` | 523MB* / 1.4GB* / 2.5GB* | Yes | Alibaba; the 4b has 256K context* |
| `qwen3:8b` | 5.2GB* | Yes, tight | Alibaba |
| `qwen3.5:0.8b` / `2b` / `4b` | 1.0GB* / 2.7GB* / 3.4GB* | Yes | Alibaba; multimodal, 256K* |
| `qwen3.5:9b` | 6.6GB* | Borderline | Alibaba |
| `qwen3-vl:2b` / `4b` | 1.9GB* / 3.3GB* | Yes | Alibaba; vision |
| `qwen3-embedding:0.6b` | 639MB* | Yes | Alibaba; embeddings |
| `deepseek-r1:1.5b` / `7b` / `8b` | 1.1GB* / 4.7GB* / 5.2GB* | Yes (8b tight) | DeepSeek; 128K context* |
| `glm4:9b` | 5.5GB* | Borderline but workable | Zhipu; 128K context* |
| `minicpm-v:8b` / `minicpm-v4.5:8b` | 5.5–5.7GB* / 5.9GB* | Borderline but OK | OpenBMB; vision |
| `gemma3:270m` / `1b` / `4b` | 292MB* / 815MB* / 3.3GB* | Yes | Google's open models: also listed under Google (ruling 2) |
| `gemma4:e2b-it-qat` | 4.3GB* | Yes | The only Gemma 4 build that fits; also under Google |

Doesn't fit locally: `gpt-oss:20b` is a 14GB download*. See [[ollama]] for the full list.

### Groq API: free tier (slot 1)

| Model (official ID) | Free? | Limits / notes |
|---------------------|-------|----------------|
| `openai/gpt-oss-120b` | Yes (as built: `smart` tier) | 30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD per organization, measured Sept 14, 2026. The source is a fetched third-party GitHub issue, matching an excerpt of Groq's rate-limits page*. OpenAI's open-weight model; per ruling 1 it counts as free and keeps its official name. |
| `openai/gpt-oss-20b` | Yes (as built: `fast` tier) | The same numbers, from third-party excerpts only*. |
| `qwen/qwen3.8-27b` | Listed* | Paid price $0.80 in / $4.00 out per 1M*. Free-tier limits not verified. |

Groq deprecations*: `moonshotai/kimi-k2-instruct-0905` (announced Mar 23, 2026, replaced by gpt-oss-120b), and `qwen/qwen3-32b`, `llama-4-scout`, `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` (announced June 17, 2026). No DeepSeek model was found on Groq*. Details on [[groq]].

### OpenRouter API: `:free` models (slot 1; Gemma also slot 2)

Current availability of each `:free` model is unverified, because retired pages can stay indexed. Limits: 50 requests/day without credits; a one-time $10 credit purchase raises it to 1,000/day; both capped at 20 RPM*. Under ruling 7 the $10 is an option, not a default. `openrouter/free` picks a free model automatically*. Details on [[openrouter]].

| Vendor | `:free` model IDs* |
|--------|--------------------|
| DeepSeek | `deepseek/deepseek-v4-flash:free`, `deepseek/deepseek-r1:free`, `deepseek/deepseek-chat-v3-0324:free` |
| Qwen | `qwen/qwen3.8-27b:free`, `qwen/qwen3-coder:free`, `qwen/qwen3.6-plus:free` |
| Kimi | `moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`, `moonshotai/kimi-dev-72b:free` |
| GLM | `z-ai/glm-5.2:free`, `z-ai/glm-5.1:free`, `z-ai/glm-4.5-air:free` |
| MiniMax | `minimax/minimax-m2.5:free`, `minimax/minimax-m2:free` |
| Gemma | `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, `google/gemma-3-27b-it:free`, `google/gemma-3-4b-it:free`, `google/gemma-3n-e4b-it:free` (also under Google) |
| gpt-oss | `openai/gpt-oss-120b:free`, `openai/gpt-oss-20b:free` (also under Groq) |

### Ollama cloud: free plan (slot 1)

"A small amount of monthly usage for a set of starter models", with 1 concurrent request*. Which models are in the starter set is unverified. Beyond the allowance, billing is per token* ([[ollama]]).

### Google: Gemini API free tier, Gemini CLI, Gemma (slot 2; Gemma also slot 1)

| Route / model | What is free | Notes |
|--------|--------------|-------|
| Gemini API: `gemini-3.6-flash` | Listed and GA on Google's model docs*; the pricing excerpt shows its free-tier input as "Free of charge"* | As built for `quality` and `frontier`, and verified working (handoff). Handoff gotcha 4: the API's models-list endpoint doesn't show it, but it works ([[gemini]]). |
| Gemini API: other Flash and Flash-Lite models | `gemini-3.8-flash` (newest), `gemini-3.7-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`, alias `gemini-flash-latest`* | Google's guidance: "For new projects use 3.5 Flash-Lite or 3.8 Flash."* The pricing page says "Start building free of charge with generous limits"*. Conflict: one excerpt says 3.8 Flash has no API free tier ("Not available"), and a forum title says "Gemini 3.8 Flash Free Tier 20 RPD". Official per-model limits are published only in AI Studio. A third-party site reports ~20 RPD for the 3.5–3.8 Flash models and ~500 RPD for 3.5 / 3.1 Flash-Lite (Sept 2026; not verified). |
| Gemini CLI, Google login | "60 requests/min and 1,000 requests/day with personal Google account" (CLI README) | The repo's quota doc also says 1,000/day for Google login. |
| Gemini CLI, unpaid API key | README: "1000 requests/day with Gemini 3 (mix of flash and pro)". Quota doc: 250/day, Flash only. | These two fetched pages conflict. |
| Gemma, local on [[ollama]] | `gemma3:270m` / `1b` / `4b` and `gemma4:e2b-it-qat` (also under Local) | Google's open models. The Gemma 4 sizes look unusual; check with `ollama show` before pulling. |
| Gemma, hosted on OpenRouter | The five `google/gemma-*:free` IDs (also under OpenRouter)* | Availability unverified. |

Not free: the handoff's Bug E says the API tier for `gemini-3.1-pro-preview` is "limit: 0 — paid API only". The research found conflicting excerpts on whether 3.1 Pro has a free tier.

### Paid, standalone (options only: $0/month still binds)

#### Anthropic API (slot 3)

No ongoing free API tier: "New users receive a small amount of free credits to test the API." Prices from the fetched Claude pricing page:

| Model | Price per MTok (in / out) |
|-------|---------------------------|
| Haiku 4.5 | $1 / $5 |
| Sonnet 5 | $2 / $10 |
| Opus 5.5 | $4 / $20 |
| Fable 5.1 | $10 / $50 |

The Batch API is 50% off.

#### OpenAI API (slot 4)

- Prices are unverified: the proxy blocked the OpenAI pricing page.
- OpenAI's rate-limits guide lists a "Free" usage tier ("User must be in an allowed geography", $100/month usage limit)*. Which models it can use is unverified.
- OpenAI's open-weight gpt-oss models are free on Groq and OpenRouter, so they're listed under those providers above (ruling 1). This slot is OpenAI's own paid API.
- Locally, `gpt-oss:20b` is a 14GB download* and doesn't fit the Chromebook ([[ollama]]).

#### Kimi API (Moonshot), paid

"Kimi is Kimi": each paid Kimi model is a standalone paid entry (ruling 3).

| Model / route | Cost | Notes |
|-------|------|-------|
| Kimi K3 (API) | $3.00 in (cache miss) / $0.30 (cache hit) / $15.00 out per 1M* | "There is no permanent Kimi API free tier for production usage."* |
| Kimi K2.6 (API) | $0.95 in / $4.00 out per 1M* | |
| Kimi K2.7 Code (API) | $0.95 / $0.19 / $4.00 standard ($8.00 high-speed) per 1M* | |
| Kimi on Ollama cloud | `kimi-k2.6:cloud` $0.95 in / $4.00 out per 1M* | Every Kimi model on Ollama is cloud-only*. Billed per token*. |
| Groq | none now | `moonshotai/kimi-k2-instruct-0905` is deprecated* |
| Open weights | Kimi K2 (1T total / 32B active*) under a Modified MIT License; Kimi K3 (2.8T total / 104B active, 1M context) under the "Kimi K3 License" | Implication: far too big for the Chromebook's 14GB RAM and ~11GB free disk. Details on [[chinese-open-source-models]]. |

Free Kimi routes, if live, are listed under OpenRouter above (`moonshotai/kimi-k2.6:free` and others*). The handoff's Bug E also says consumer subscriptions, Kimi's included, don't give API access ([[free-api-tiers]]).

## Getting more tokens (follow-up ruling 8)

> **Recommendation (interpretation), not a ruling.** Each figure is as marked above.

- **Spread the load across free routes.** Each provider has its own free quota, so the total free budget is roughly their sum:
  - Groq gpt-oss-120b: 1,000 RPD / 200,000 TPD;
  - Gemini CLI with Google login: 1,000 requests/day;
  - OpenRouter: 50 requests/day free (1,000/day after the optional one-time $10);
  - Ollama cloud: a small free allowance;
  - local Ollama: no quota, only machine speed.
- **For Gemini volume, add Flash-Lite.** It reportedly has ~500 RPD free*, against ~20 RPD* for the Flash models, including the `gemini-3.6-flash` that `quality` and `frontier` use now. Google itself suggests 3.5 Flash-Lite for new projects*. Keep 3.6 Flash for quality, and use Flash-Lite for bulk work or as a fallback.
- **Where to change it:** in Jarvis's provider registry (`registry.js`, [[universal-model-layer]]). That's a code change in the jarvis-x repo, not this vault. Test it on the Chromebook with the real key first: handoff gotcha 4 warns that Google's model list can be wrong about what works.

## Recommended local-first stack for the Chromebook (inference)

> **Recommendation, not fact.** This is the researcher's inference in [[source-model-landscape-research]], adapted here. Nobody has tested it on the machine. The sizes marked `*` come from search excerpts.

| Role | Recommended | Size | Notes |
|------|-------------|------|-------|
| Everyday chat/agent | `qwen3:4b` or `qwen3.5:4b` | 2.5GB* / 3.4GB* | `qwen3:4b` has 256K context*; `qwen3.5:4b` is multimodal |
| Higher-quality local | `qwen3:8b` in place of `qwen2.5:7b`; `qwen3.5:9b` only if RAM allows | 5.2GB* / 6.6GB* | |
| Coding | keep `qwen2.5-coder:3b` / `:7b` | 1.9GB / 4.7GB | No small qwen3-coder exists* |
| Reasoning | `deepseek-r1:8b`, or qwen3's thinking mode | 5.2GB* | |
| Vision | `qwen3-vl:4b` or `gemma3:4b`; `gemma4:e2b-it-qat` is the only Gemma 4 build that fits | 3.3GB* / 3.3GB* / 4.3GB* | Check Gemma 4 sizes with `ollama show` before pulling |
| Tiny router/classifier | `qwen3:1.7b`, `qwen3.5:0.8b` or `gemma3:1b` | 1.4GB* / 1.0GB* / 815MB* | |
| Embeddings | keep `nomic-embed-text`, or try `qwen3-embedding:0.6b` | 274MB / 639MB* | |
| Avoid locally | `gpt-oss:20b` (14GB*), qwen3.6 / 3.8 / coder, `glm-4.7-flash`, and all Kimi, MiniMax, DeepSeek-V4 and GLM-5 models | | Too large, or cloud-only on Ollama |

Operating advice, from the same research:

- **Load one model at a time.** The as-built Ollama override already sets `OLLAMA_MAX_LOADED_MODELS=1` and `OLLAMA_NUM_PARALLEL=1` (fix 8, [[ollama]]).
- **Mind the disk budget.** With ~11GB free, pull models one by one and `ollama rm` the ones they replace.
- Arithmetic: the five models present total about 13.5GB. Swapping `qwen2.5:7b` (4.7GB) for `qwen3:8b` (5.2GB*) costs about 0.5GB net.
- Implication: handoff gotcha 7 ("Chrome tabs eat 10GB of your 14GB. Before any heavy build, close them. free -h should show 6GB+ available.") is written for builds, but the same check applies before loading a 5–7GB model.

## How the as-built tiers line up

As of the 2026-09-24 handoff ([[jarvis-x-runtime]]). Tier names stay as they are (follow-up ruling 4). Each tier is a route: local, or a provider's API.

| Tier | Route (provider → model) | Slot |
|------|--------------------------|------|
| `local` | local → [[ollama]] `qwen2.5:3b` (Alibaba's Qwen, a Chinese open model) | 1 |
| `fast` | [[groq]] API → `openai/gpt-oss-20b` | 1: free, so it counts as free under ruling 1, keeping its official OpenAI name |
| `smart` | [[groq]] API → `openai/gpt-oss-120b` | 1: same |
| `quality` / `frontier` | [[gemini]] API → `gemini-3.6-flash` | 2 (Google, free) |

The as-built routing already follows the ladder's order, with no Anthropic or OpenAI paid API tier in use. The plan's `smart` = Anthropic ([[universal-model-layer]]) would be slot 3, a paid option.

## Still open

1. **stream:false:** which adapter the "do not re-enable stream: false" warning refers to is still unknown (follow-up ruling 6: "I don't know"). See [[starnet]].
2. **Search-excerpt figures:** everything marked `*` still needs checking on the machine: `ollama show` for sizes, the Groq console for limits, and AI Studio for Gemini limits.
3. **The Flash-Lite change:** adding a Flash-Lite tier or fallback in Jarvis is recommended (see "Getting more tokens") but not yet made. It needs testing on the Chromebook.

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[ollama]] | [[chinese-open-source-models]] | [[groq]] | [[gemini]] | [[openrouter]] | [[the-council]] | [[hermes-agent]] | [[jarvis-x-hardware]] | [[crostini]] | [[jarvis-x]] | [[jarvis-x-runtime]] | [[jarvis-x-plan-vs-reality]] | [[source-model-landscape-research]]
