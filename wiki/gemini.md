---
title: Gemini
tags: [provider, model-provider, cloud, google, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[universal-model-layer]], [[free-api-tiers]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[the-council]], [[groq]], [[openrouter]], [[ollama]], [[crostini]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Gemini

Google's model provider and API, one of the cloud providers behind the [[jarvis-x]] [[universal-model-layer]]. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), Gemini serves two Jarvis tiers, `quality` and `frontier`, both on `gemini-3.6-flash`. The handoff lists that model as free API access. The earlier plans cast Gemini as the long-context provider and as "The Analyst" in [[the-council]].

## In the plans

| Source | What it says about Gemini |
|--------|---------------------------|
| v2 Ascension Plan, reframe table (v1 column) | "Router: local Ollama + Gemini/Groq/OpenRouter" |
| v2 Ascension Plan, reframe table (v2 column) | "every provider behind one interface, incl. Claude/Gemini while subs live, hot-swap free tiers after" |
| v2 Ascension Plan, §3 | Registered provider: "Gemini CLI/API". Router rule: "long-context → Gemini". Tier set: `local\|fast\|smart\|long`. |
| DeepSeek Master Plan, Council table | Gemini is "The Analyst": "1M+ token context, large codebases", best for "Large-scale analysis, PDFs" |
| DeepSeek Master Plan, integration diagram | Gemini CLI appears as "(Analyst)" next to Claude Code and Codex CLI. PAL MCP "Links Claude Code, Codex, Gemini". |

## As-built tiers (as of the 2026-09-24 handoff)

All verified working via `POST /api/ask`:

| tier     | provider | model                     |
|----------|----------|---------------------------|
| quality  | gemini   | gemini-3.6-flash          |
| frontier | gemini   | gemini-3.6-flash          |

In the [[jarvis-x-openai-compatible-api]], both `"quality"` and `"frontier"` map to `"registry:quality"`, so a `/v1` request for `frontier` gets the `quality` model. The tier table above was verified through `POST /api/ask`, not `/v1`. The handoff doesn't say whether `registry.js` has a separate `frontier` entry. The full tier table is on [[jarvis-x-runtime]].

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** the plan gives Gemini the `long` tier ("long-context → Gemini"). The as-built system has no `long` tier. Gemini instead serves `quality` and `frontier`, both on `gemini-3.6-flash`. Unknown: whether `quality`/`frontier` replaced `long` or are a different design; whether `gemini-3.6-flash` meets the plan's long-context role or the Council's "1M+ token context" (the handoff says nothing about context length); and whether the "Gemini CLI" path in the plans is used at all. Left for the human to resolve.

## Fix 4 — keep the model name (the list is "stale")

From the handoff: "registry.js had gemini-3.6-flash. Google's models-list endpoint does NOT show this model (it's stale), but the model works. Do not change it to a model from the list — the list is wrong."

"Verified working: gemini-3.6-flash (with the key in .env)."

Gotcha 4 repeats it: "Google's models-list endpoint is stale. gemini-3.6-flash works even though it isn't listed. Don't trust the list."

Note: "stale" and "wrong" are the handoff's characterisation. What the handoff actually observed is that the model is missing from the list but works when called. It doesn't say why the list omits it.

## Checking the key (gotcha 9)

"Jarvis's quality tier maps to Gemini. If it returns ollama responses, the Gemini key is missing or invalid." To verify:

```bash
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"hi"}]}]}'
```

Implication: when the Gemini key is missing or invalid, the `quality` tier appears to fall back to [[ollama]] instead of returning an error. The handoff describes the symptom, not the fallback mechanism, and doesn't say which Ollama model answers.

## API key

- **`GEMINI_API_KEY`**: StarNet's registry reads this plain name (fix 9, see [[starnet]]). The StarNet launch passes it as `GEMINI_API_KEY="$GEMINI_API_KEY"`, and the gotcha 9 curl uses it too.
- Keys live in `~/.jarvis-x/.env` (chmod 600).
- Fix 1, the quoting bug in `registry.js` that sent `Authorization: Bearer "..."` with the quotes included, hit "every cloud call" and made "every provider" reject silently. See [[jarvis-x-runtime]].

## In StarNet

As of the 2026-09-24 handoff: "Groq/Gemini: keys verify as VALID but every run either returns HTTP 400 or kills the sidecar." Bug A is written up for Groq only. The handoff doesn't say whether the Gemini failures share its cause. See [[starnet]].

The handoff's IPv6-truncation note names only Groq and OpenRouter as Cloudflare-fronted ([[crostini]]). It doesn't say whether the Gemini endpoint is affected.

## Consumer app vs API (Bug E)

"Google AI Pro unlocks 3.1 Pro in the consumer app. The API tier for gemini-3.1-pro-preview is limit: 0 — paid API only."

The free Gemini API access the handoff lists is "gemini-3.6-flash (verified working)". See [[free-api-tiers]].

Implication: the v2 plan's "Claude/Gemini while subs live" assumed subscription-backed access. Per Bug E, a Google AI Pro subscription doesn't carry over to the API for `gemini-3.1-pro-preview`. If the Council's Analyst seat runs on the free API, the only Gemini model on Bug E's free list is `gemini-3.6-flash`. See [[the-council]].

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[starnet]] | [[the-council]] | [[groq]] | [[openrouter]] | [[ollama]] | [[crostini]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]]
