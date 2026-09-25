---
title: Free API Tiers
tags: [concept, providers, free-tier, api-access, cost, jarvis-x]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[groq]], [[gemini]], [[openrouter]], [[universal-model-layer]], [[the-council]], [[jarvis-x]], [[ollama]], [[constitutional-autonomy]], [[jarvis-x-runtime]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Free API Tiers

The concept: **a consumer AI subscription is not API access.** What a program like [[jarvis-x]] can call for free is a much shorter list than what a paying app user can reach. The 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) records this as Bug E and lists what free API access there is. Two of its three entries are marked verified.

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

## Implication — for the Jarvis X plans

This section is interpretation. The facts are from the sources in the frontmatter. The conclusions are this wiki's.

**The $0/month constraint.** The v2 plan's execution prompt binds everything to "CPU-only Y50-70, $0/month, 6-10 hrs/wk, Egypt/Payoneer, income-first 60/40". The plan also says "Every provider is optional. JARVIS X must boot and function with zero cloud keys". The master plan's principle is "You own everything. No subscriptions. No dependencies."

Under $0/month, cloud tiers are limited to the free list above. Observation: every cloud model in the as-built tier table is on that list.

**Plan entries that assume subscription-backed access:**

| Plan entry | Source | Bearing of Bug E |
|------------|--------|------------------|
| "incl. Claude/Gemini while subs live, hot-swap free tiers after" | v2 plan, reframe table | For Gemini, the subscription (Google AI Pro) does not extend to `gemini-3.1-pro-preview` over the API. The "free tiers after" half matches what was built. |
| Anthropic: "while sub lives, then optional API" | v2 plan §3 ([[universal-model-layer]]) | Unknown. The handoff doesn't mention Anthropic, and Anthropic is not in the as-built tier table. |
| "build Universal Model Layer ... *while you still have Claude*" | v2 plan, Wk 3-4 | Unknown. The handoff doesn't say how the layer was built or whether Claude access still exists. |
| Kimi K2.6 as "Long-Horizon Builder" | [[the-council]] (master plan) | A Kimi consumer subscription gives no API access, per the Bug E heading. |
| Gemini as "The Analyst", "1M+ token context" | [[the-council]] (master plan) | On the free API, only `gemini-3.6-flash` is listed. The handoff doesn't state its context length. |

Also relevant: the v2 plan's standing permissions ([[constitutional-autonomy]]) include "call free APIs within quotas". The handoff mentions two quota facts: `limit: 0` on `gemini-3.1-pro-preview`, and OpenRouter's "shared-pool rate limits" (not quantified).

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan registers "NVIDIA NIM free" and "Mistral free tier" as providers. The handoff says free API access "is limited to" Gemini, Groq and OpenRouter. Unknown: whether NVIDIA NIM and Mistral were tried and found not to be free on this account, or were never tried. The handoff's list may cover only what was tested. Left for the human to resolve.

## Related

[[groq]] | [[gemini]] | [[openrouter]] | [[universal-model-layer]] | [[the-council]] | [[jarvis-x]] | [[ollama]] | [[constitutional-autonomy]] | [[jarvis-x-runtime]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
