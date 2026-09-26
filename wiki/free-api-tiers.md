---
title: Free API Tiers
tags: [concept, providers, free-tier, api-access, cost, jarvis-x]
sources:
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[groq]], [[gemini]], [[openrouter]], [[universal-model-layer]], [[the-council]], [[jarvis-x]], [[ollama]], [[constitutional-autonomy]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]], [[jarvis-x-hardware]]
last_updated: 2026-09-25
---

# Free API Tiers

The concept: **a consumer AI subscription is not API access.** What a program like [[jarvis-x]] can call for free is a much shorter list than what a paying app user can reach. The 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) records this as Bug E and lists what free API access there is. Two of its three entries are marked verified.

On 2026-09-25, web research ([[source-model-landscape-research]]) put numbers on the free tiers and found more free routes. The same day, the human ranked the providers ([[jarvis-x-model-priority]]). Both are covered in "Free tiers as of 2026-09-25 (research)" below.

## Bug E, in full

The handoff's text:

> **Bug E: Kimi / consumer AI subscriptions don't give API access**
>
> Google AI Pro unlocks 3.1 Pro in the consumer app. The API tier for gemini-3.1-pro-preview is limit: 0 — paid API only. Same for most consumer subscriptions. Free API access is limited to:
>
> · Gemini: gemini-3.6-flash (verified working)
> · Groq: openai/gpt-oss-20b, openai/gpt-oss-120b (verified)
> · OpenRouter: free models with shared-pool rate limits

## What is free (as of the 2026-09-24 handoff)

| Provider | Free API access | Marked in handoff | Used by as-built Jarvis? |
|----------|-----------------|-------------------|--------------------------|
| [[gemini]] | `gemini-3.6-flash` | verified working | Yes: `quality` and `frontier` tiers |
| [[groq]] | `openai/gpt-oss-20b`, `openai/gpt-oss-120b` | verified | Yes: `fast` and `smart` tiers; also [[aider]] |
| [[openrouter]] | free models with shared-pool rate limits | not marked verified | No: not in the tier table; the key is passed to [[starnet]] |

The as-built tier table has three providers. The third, [[ollama]] (`local` tier, `qwen2.5:3b`), runs on the machine itself and isn't a cloud API tier. See [[jarvis-x-runtime]] for the full table.

## What is not free (per the handoff)

- **`gemini-3.1-pro-preview` via API:** "limit: 0 — paid API only". This holds even with Google AI Pro, which "unlocks 3.1 Pro in the consumer app".
- **Kimi:** named in the Bug E heading next to "consumer AI subscriptions", with no further detail.
- **"Most consumer subscriptions":** the handoff doesn't list which ones. It names only Kimi and Google AI Pro.

## Free tiers as of 2026-09-25 (research)

A research subagent checked the free tiers on 2026-09-25 ([[source-model-landscape-research]]). The network proxy blocked most provider sites (console.groq.com, ai.google.dev, openrouter.ai, ollama.com, openai.com, platform.kimi.ai and others). GitHub and Anthropic's pages could be fetched.

\* Figures marked with an asterisk come from web-search excerpts, not fetched pages ("[S]" in the research note). Treat them as medium confidence and possibly stale. Unmarked figures come from pages that were fetched and read.

| Provider | Free route | Limits | How sure |
|----------|------------|--------|----------|
| [[groq]] | Free tier on `openai/gpt-oss-120b` and `openai/gpt-oss-20b` (both still listed*) | `gpt-oss-120b`: **30 RPM, 1,000 RPD, 8,000 TPM, 200,000 TPD** per organization, measured Sept 14, 2026. `gpt-oss-20b`: the same numbers*, but only from third-party excerpts | The 120b figures come from a fetched GitHub issue (a third party's measurement). Groq's own rate-limits page agrees in a search excerpt* |
| [[openrouter]] | `:free` models, plus the `openrouter/free` auto-router* | 50 requests/day without credits; 1,000/day after a one-time $10 credit purchase; 20 RPM in both cases* | Everything is from search excerpts. Whether each `:free` model is still live is unverified; retired pages can stay indexed |
| [[gemini]] API | A free tier: "Start building free of charge with generous limits"*. The pricing excerpt shows `gemini-3.6-flash` free-tier input as "Free of charge"* | Official per-model limits are published only in AI Studio. A third party reports **~20 RPD** for the 3.5–3.8 Flash models and **~500 RPD** for 3.5 / 3.1 Flash-Lite (Sept 2026) | The per-model numbers are a third-party report (scriptbyai.com), and the research note doesn't mark it fetched or excerpted |
| Gemini CLI, Google login | Free quota | "60 requests/min and 1,000 requests/day with personal Google account" | Fetched (the Gemini CLI README) |
| Gemini CLI, API key | Free quota | **Conflict.** The README says "1000 requests/day with Gemini 3 (mix of flash and pro)". The repo's quota doc says 250/day, Flash only, for an unpaid API key | Both fetched; they disagree |
| [[ollama]] cloud | Free plan: "a small amount of monthly usage for a set of starter models", 1 concurrent request*. Pay-as-you-go credits unlock all models* | Not quantified. Which models are in the free starter set is unverified. Billing beyond it is per token | Fetched docs confirm only that cloud models are hosted, need no download, and use an API key or sign-in. The local Ollama runtime is free |
| Kimi (Moonshot) | **None.** "There is no permanent Kimi API free tier for production usage."* | — | Search excerpt. Kimi on Groq is deprecated*; see [[groq]] |
| Anthropic | **No ongoing free tier.** "New users receive a small amount of free credits to test the API." | Credits, not a tier | Fetched (platform.claude.com pricing) |
| OpenAI | A "Free" usage tier in the rate-limits guide: "User must be in an allowed geography", $100/month usage limit* | Which models it can use is unverified | Search excerpt; the OpenAI pricing page was blocked |

Notes on the table:

- **Bug E still holds.** The research is consistent with all three Bug E entries: both Groq gpt-oss models are still listed*, `gemini-3.6-flash` shows free-tier input*, and OpenRouter has free models with limits*. It adds two free routes the handoff doesn't mention: the Ollama cloud free plan and the Gemini CLI quota.
- **Gemini 3.1 Pro.** Bug E observed `limit: 0` on `gemini-3.1-pro-preview` for this account. The research found conflicting excerpts on whether 3.1 Pro has an API free tier at all. The two aren't necessarily in conflict (one is an observed account limit, the other is mixed web excerpts). Not resolved here; see [[gemini]].
- **Gemini 3.8 Flash.** The excerpts conflict: one says the free tier is "Not available", while a forum title reads "Gemini 3.8 Flash Free Tier 20 RPD". Unresolved.
- **Not covered.** The research note doesn't cover NVIDIA NIM or Mistral, so the disagreement about them below stays open.
- **"Shared-pool" limits.** The handoff's "shared-pool rate limits" for OpenRouter is still unexplained. The research figures are per-account caps.

### How this maps to the 2026-09-25 ruling

Follow-up rulings (2026-09-25, second reply, `raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md`):

- **Free counts as free.** A model that is 100% free is in the free tier under its official name, even an OpenAI-named one.
- **List free models by provider.** A free model is listed under every provider that serves it free. The full catalog, laid out this way, is on [[jarvis-x-model-priority]].
- **Budget:** "Still zero but leave it as an option". Paid routes, including OpenRouter's one-time $10, stay listed as options only.

The human's ruling ([[jarvis-x-model-priority]]) sets the order for plans:

1. Local models and free open-source tiers "that could work on any machine specially chrome os", including "top tier Chinese open source models" via Ollama.
2. "the most free available from google".
3. Anthropic.
4. OpenAI.

Kimi goes in the paid slot: "if kimi is not free treat as a paid subscription".

The ruling names only Google, Anthropic, OpenAI and Kimi, so the slot for every other route below is this wiki's interpretation.

| Free route | Slot (interpretation) | Why |
|------------|-----------------------|-----|
| Local [[ollama]] models (Qwen, DeepSeek, GLM and small Gemma tags that fit the Chromebook) | 1 | Local and open. They have to fit a CPU-only machine with ~11GB free disk. The research note's fit judgments assume 6–9GB RAM free ([[jarvis-x-hardware]]). See [[chinese-open-source-models]] |
| [[groq]] free tier | 1 | A free hosted tier for open-weight models. But gpt-oss is made by OpenAI, which is slot 4 as a maker. Resolved by follow-up ruling 1: free counts as free, so it stays in slot 1 under its official name ([[jarvis-x-model-priority]]) |
| [[openrouter]] `:free` models | 1 | Free hosted open models, including Chinese families and Kimi `:free` listings* |
| [[ollama]] cloud free plan | 1, probably | Free, but the starter model set is unverified and anything beyond it is billed per token |
| Gemma open models (local via Ollama, or `:free` on OpenRouter*) | 1 (also 2) | Open and runnable locally, so slot 1. Also "from google", so slot 2. Resolved by follow-up ruling 2: "if it fits both let it be in both" ([[jarvis-x-model-priority]]) |
| [[gemini]] API free tier; Gemini CLI free quota | 2 | "the most free available from google" |
| Anthropic new-user credits | 3 | A small one-time amount; no ongoing free tier |
| OpenAI "Free" usage tier* | 4 | Which models it covers is unverified |
| Kimi API | Paid | The API is paid*. The research note's verdict (its inference) is that the only possible free route is OpenRouter's Kimi `:free` listings, and only if they are still live |

Observation: every cloud model in the as-built tier table comes from slot 1 or 2. See [[jarvis-x-model-priority]].

Open question: the ruling creates a "paid tiers slot", and OpenRouter's higher daily cap needs a one-time $10 credit purchase. The ruling doesn't mention the v2 plan's "$0/month" constraint (below). Whether any paid route is allowed at all is left for the human.

## Implication — for the Jarvis X plans

This section is interpretation. The facts are from the sources in the frontmatter. The conclusions are this wiki's.

**The $0/month constraint.** The v2 plan's execution prompt binds everything to "CPU-only Y50-70, $0/month, 6-10 hrs/wk, Egypt/Payoneer, income-first 60/40". The plan also says "Every provider is optional. JARVIS X must boot and function with zero cloud keys". The master plan's principle is "You own everything. No subscriptions. No dependencies." (The 2026-09-25 ruling names the Chromebook, not the Y50-70, as the current machine. See [[jarvis-x-hardware]].)

Under $0/month, cloud tiers are limited to the free list above. Observation: every cloud model in the as-built tier table is on that list. The 2026-09-25 research adds more free routes and puts numbers on their limits (see above).

**Plan entries that assume subscription-backed access:**

| Plan entry | Source | Bearing of Bug E |
|------------|--------|------------------|
| "incl. Claude/Gemini while subs live, hot-swap free tiers after" | v2 plan, reframe table | For Gemini, the subscription (Google AI Pro) does not extend to `gemini-3.1-pro-preview` over the API. The "free tiers after" half matches what was built. |
| Anthropic: "while sub lives, then optional API" | v2 plan §3 ([[universal-model-layer]]) | Unknown. The handoff doesn't mention Anthropic, and Anthropic is not in the as-built tier table. Update (2026-09-25): the research found no ongoing free Anthropic API tier, only a small amount of free credits for new users. The ruling puts Anthropic in slot 3. |
| "build Universal Model Layer ... *while you still have Claude*" | v2 plan, Wk 3-4 | Unknown. The handoff doesn't say how the layer was built or whether Claude access still exists. |
| Kimi K2.6 as "Long-Horizon Builder" | [[the-council]] (master plan) | A Kimi consumer subscription gives no API access, per the Bug E heading. Update (2026-09-25): the Kimi API is paid*, and the ruling puts Kimi in the paid slot. |
| Gemini as "The Analyst", "1M+ token context" | [[the-council]] (master plan) | On the free API, only `gemini-3.6-flash` is listed. The handoff doesn't state its context length. Update (2026-09-25): the research lists more Flash and Flash-Lite models, but it doesn't state their context lengths either. |

Also relevant: the v2 plan's standing permissions ([[constitutional-autonomy]]) include "call free APIs within quotas". The handoff mentions two quota facts: `limit: 0` on `gemini-3.1-pro-preview`, and OpenRouter's "shared-pool rate limits" (not quantified). The 2026-09-25 research quantifies the quotas for Groq, OpenRouter and the Gemini CLI (table above).

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan registers "NVIDIA NIM free" and "Mistral free tier" as providers. The handoff says free API access "is limited to" Gemini, Groq and OpenRouter. Unknown: whether NVIDIA NIM and Mistral were tried and found not to be free on this account, or were never tried. The handoff's list may cover only what was tested. Left for the human to resolve. (The 2026-09-25 research doesn't cover NVIDIA NIM or Mistral either.)

## Related

[[groq]] | [[gemini]] | [[openrouter]] | [[universal-model-layer]] | [[the-council]] | [[jarvis-x]] | [[ollama]] | [[constitutional-autonomy]] | [[jarvis-x-runtime]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[source-model-landscape-research]] | [[jarvis-x-hardware]]
