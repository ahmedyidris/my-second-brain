---
title: Jarvis X Model Priority
tags: [jarvis-x, models, providers, ruling, local-first, chromebook]
sources:
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
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
| Paid | **Paid subscriptions** | Kimi, "if kimi is not free" |

The ruling ranks Anthropic above OpenAI, but it doesn't say where Kimi sits relative to them inside the paid group. Open question for the human.

## What "any machine, especially ChromeOS" rules out

The current machine is the Chromebook ([[jarvis-x-hardware]]): CPU-only, 14GB RAM with Chrome using ~10GB of it, and ~11GB free disk. Implication: a slot-1 local model has to run on the CPU inside that memory and disk. Large open models can only fill slot 1 through a free hosted tier, not locally.

The research's working test for "fits" on this machine is ≤~8B parameters and a ≤~6GB download, with 6–9GB RAM free. "Borderline" means a 6–7.5GB download ([[source-model-landscape-research]]).

## Concrete options per slot (2026-09-25)

Drawn from the 2026-09-25 web research ([[source-model-landscape-research]]) and the 2026-09-24 handoff. Sizes are download sizes. Free tiers and model lists change often, so re-check before building on any single entry.

### Slot 1: local and free open-source

**Local on the Chromebook, via [[ollama]].** The full per-family lists, including what doesn't fit, are on [[chinese-open-source-models]] and [[ollama]].

| Option | Size | Fits the Chromebook? | Notes |
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
| `gemma3:270m` / `1b` / `4b` | 292MB* / 815MB* / 3.3GB* | Yes | Google's open models, so also slot 2 (see question (b)) |
| `gemma4:e2b-it-qat` | 4.3GB* | Yes | The only Gemma 4 build that fits |

**Free hosted open-source tiers.**

| Option | What is free | Limits | Confidence |
|--------|--------------|--------|------------|
| [[groq]] free tier | `openai/gpt-oss-120b` and `openai/gpt-oss-20b` are still listed*. `qwen/qwen3.8-27b` is listed* (paid price $0.80 in / $4.00 out per 1M*). | gpt-oss-120b: 30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD per organization, measured Sept 14, 2026 (a fetched third-party GitHub issue, matching an excerpt of Groq's rate-limits page*). gpt-oss-20b: the same numbers, from third-party excerpts only*. Qwen free limits: not verified. | Both gpt-oss models verified working as built (handoff Bug E). |
| [[openrouter]] `:free` models | DeepSeek, Qwen, Kimi, GLM, MiniMax, Gemma and gpt-oss IDs*. `openrouter/free` picks a free model automatically*. | 50 requests/day without credits; a one-time $10 credit purchase raises it to 1,000/day; both capped at 20 RPM* | Current availability of each `:free` model is unverified (retired pages can stay indexed). |
| Ollama cloud free plan | "a small amount of monthly usage for a set of starter models", with 1 concurrent request* | Which models are in the starter set is unverified. Beyond the allowance, billing is per token* ([[ollama]]). | Medium |

Groq deprecations*: `moonshotai/kimi-k2-instruct-0905` (announced Mar 23, 2026, replaced by gpt-oss-120b), and `qwen/qwen3-32b`, `llama-4-scout`, `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` (announced June 17, 2026). No DeepSeek model was found on Groq*.

### Slot 2: Google, free

| Option | What is free | Notes |
|--------|--------------|-------|
| Gemini API free tier: `gemini-3.6-flash` | Listed and GA on Google's model docs*; the pricing excerpt shows its free-tier input as "Free of charge"* | As built for `quality` and `frontier`, and verified working (handoff). Handoff gotcha 4: the API's models-list endpoint doesn't show it, but it works ([[gemini]]). |
| Gemini API free tier: other Flash and Flash-Lite models | `gemini-3.8-flash` (newest), `gemini-3.7-flash`, `gemini-3.5-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`, alias `gemini-flash-latest`* | Google's guidance: "For new projects use 3.5 Flash-Lite or 3.8 Flash."* The pricing page says "Start building free of charge with generous limits"*. Conflict: one excerpt says 3.8 Flash has no API free tier ("Not available"), and a forum title says "Gemini 3.8 Flash Free Tier 20 RPD". Official per-model limits are published only in AI Studio. A third-party site reports ~20 RPD for the 3.5–3.8 Flash models and ~500 RPD for 3.5 / 3.1 Flash-Lite (Sept 2026; not verified). |
| Gemini CLI, Google login | "60 requests/min and 1,000 requests/day with personal Google account" (CLI README) | The repo's quota doc also says 1,000/day for Google login. |
| Gemini CLI, unpaid API key | README: "1000 requests/day with Gemini 3 (mix of flash and pro)". Quota doc: 250/day, Flash only. | These two fetched pages conflict. |
| Gemma, run locally on [[ollama]] | `gemma3:270m` / `1b` / `4b` and `gemma4:e2b-it-qat` (see slot 1) | Google's open models. The Gemma 4 sizes look unusual; check with `ollama show` before pulling. |
| Gemma, hosted | OpenRouter `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, `google/gemma-3-27b-it:free`, `google/gemma-3-4b-it:free`, `google/gemma-3n-e4b-it:free`* | Availability unverified. |

Not free: the handoff's Bug E says the API tier for `gemini-3.1-pro-preview` is "limit: 0 — paid API only". The research found conflicting excerpts on whether 3.1 Pro has a free tier.

### Slot 3: Anthropic (paid)

No ongoing free API tier: "New users receive a small amount of free credits to test the API." Prices from the fetched Claude pricing page:

| Model | Price per MTok (in / out) |
|-------|---------------------------|
| Haiku 4.5 | $1 / $5 |
| Sonnet 5 | $2 / $10 |
| Opus 5.5 | $4 / $20 |
| Fable 5.1 | $10 / $50 |

The Batch API is 50% off.

### Slot 4: OpenAI (paid API)

- Prices are unverified: the proxy blocked the OpenAI pricing page.
- OpenAI's rate-limits guide lists a "Free" usage tier ("User must be in an allowed geography", $100/month usage limit)*. Which models it can use is unverified.
- The research's note: the practical free OpenAI path is gpt-oss through Groq, OpenRouter `:free` or Ollama cloud. Where gpt-oss sits on the ladder is question (a) below.
- Locally, `gpt-oss:20b` is a 14GB download* and doesn't fit the Chromebook ([[ollama]]).

### Paid slot: Kimi

| Route | Cost | Notes |
|-------|------|-------|
| Kimi API (Moonshot) | Per 1M tokens: K3 $3.00 in (cache miss) / $0.30 (cache hit) / $15.00 out; K2.6 $0.95 in / $4.00 out; K2.7 Code $0.95 / $0.19 / $4.00 standard ($8.00 high-speed)* | "There is no permanent Kimi API free tier for production usage."* |
| Ollama cloud | `kimi-k2.6:cloud` $0.95 in / $4.00 out per 1M* | Every Kimi model on Ollama is cloud-only*. Billed per token*. |
| Groq | none now | `moonshotai/kimi-k2-instruct-0905` is deprecated* |
| OpenRouter | `moonshotai/kimi-k2.6:free`, `moonshotai/kimi-k2:free`, `moonshotai/kimi-dev-72b:free` are listed* | Availability unverified |
| Open weights | Kimi K2 (1T total / 32B active*) under a Modified MIT License; Kimi K3 (2.8T total / 104B active, 1M context) under the "Kimi K3 License" | Implication: far too big for the Chromebook's 14GB RAM and ~11GB free disk. Details on [[chinese-open-source-models]]. |

The handoff's Bug E also says consumer subscriptions, Kimi's included, don't give API access ([[free-api-tiers]]).

## Verdict on Kimi

Per the research, Kimi is not free as an API. Under the ruling ("if kimi is not free treat as a paid subscription and put in paid tiers slot"), **Kimi goes in the paid slot**. That includes the Kimi K2.6 seat on [[the-council]].

A free route may exist: OpenRouter lists `moonshotai/kimi-k2.6:free`*, but whether it is still live is unverified. If it is confirmed live, the human can revisit whether Kimi through OpenRouter counts as a slot-1 free hosted tier.

## Interpretation questions for the human

### (a) gpt-oss: slot 1 or slot 4?

gpt-oss is an OpenAI open-weight model. It is served free on [[groq]] (the as-built `fast` and `smart` tiers) and listed as OpenRouter `:free`*. Does it sit in slot 1 (free open-source tier) or slot 4 (OpenAI)?

**Interpretation, not a ruling:** slot 1. It is free and open-weight, and the ruling's "open ai" most plausibly means OpenAI's paid API. The as-built table below places `fast` and `smart` in slot 1 on this reading. If the human meant anything from OpenAI, both tiers move to slot 4, and slot 1's hosted options shrink to Groq's Qwen, OpenRouter `:free` and the Ollama cloud free plan.

### (b) Gemma: slot 1 and slot 2

Gemma is Google's open model family. Run locally on [[ollama]], it is a local open model that works on the Chromebook (slot 1). It is also "from google" (slot 2). It satisfies both. Implication: this changes little in practice, because slot 1 outranks slot 2, so a local Gemma is picked at slot-1 priority either way. Open question: should plans list Gemma under slot 1, slot 2, or both?

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

As of the 2026-09-24 handoff ([[jarvis-x-runtime]]):

| Tier | As built | Slot under the ruling |
|------|----------|-----------------------|
| `local` | [[ollama]] `qwen2.5:3b` (Alibaba's Qwen, a Chinese open model) | 1 |
| `fast` | [[groq]] `openai/gpt-oss-20b` | 1, as a free hosted tier (Bug E lists it as free API access) |
| `smart` | [[groq]] `openai/gpt-oss-120b` | 1, as a free hosted tier (Bug E lists it as free API access) |
| `quality` / `frontier` | [[gemini]] `gemini-3.6-flash` | 2 (Google, free: Bug E lists it as free API access) |

Implication: the as-built routing already follows the ruling's order, with no Anthropic or OpenAI API tier in use. The plan's `smart` = Anthropic ([[universal-model-layer]]) moves to slot 3 under the ruling.

The slot-1 placement of `fast` and `smart` rests on reading gpt-oss as a free open-source tier rather than as OpenAI (question (a) above).

## Open questions for the human

1. Where does Kimi sit relative to Anthropic and OpenAI inside the paid group?
2. (a) Is gpt-oss slot 1 (free open-weight) or slot 4 (OpenAI)?
3. (b) Should Gemma be listed under slot 1, slot 2, or both?
4. If OpenRouter's `moonshotai/kimi-k2.6:free` is confirmed live, does Kimi move up from the paid slot?

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[ollama]] | [[chinese-open-source-models]] | [[groq]] | [[gemini]] | [[openrouter]] | [[the-council]] | [[hermes-agent]] | [[jarvis-x-hardware]] | [[crostini]] | [[jarvis-x]] | [[jarvis-x-runtime]] | [[jarvis-x-plan-vs-reality]] | [[source-model-landscape-research]]
