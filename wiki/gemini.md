---
title: Gemini
tags: [provider, model-provider, cloud, google, free-tier, jarvis-x, entity]
sources:
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-model-landscape-research.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
related: [[universal-model-layer]], [[free-api-tiers]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[starnet]], [[the-council]], [[groq]], [[openrouter]], [[ollama]], [[crostini]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[source-model-landscape-research]], [[jarvis-x-hardware]]
last_updated: 2026-09-25
---

# Gemini

Google's model provider and API, one of the cloud providers behind the [[jarvis-x]] [[universal-model-layer]]. As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), Gemini serves two Jarvis tiers, `quality` and `frontier`, both on `gemini-3.6-flash`. The handoff lists that model as free API access. The earlier plans cast Gemini as the long-context provider and as "The Analyst" in [[the-council]].

Under the human's 2026-09-25 ruling ([[jarvis-x-model-priority]]), Google is slot 2: "the most free available from google". Google's open Gemma models are a separate case. They run locally, so they also fit slot 1 (see "Gemma" below).

\* Figures marked with an asterisk come from web-search excerpts in the 2026-09-25 research ([[source-model-landscape-research]]), not fetched pages. Treat them as medium confidence and possibly stale. The proxy blocked ai.google.dev, so every figure from Google's API docs carries the asterisk. The Gemini CLI figures were fetched from GitHub.

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

The 2026-09-25 research doesn't state context lengths for any Gemini model either, so the long-context question stays open.

## Gemini models (2026-09-25 research)

- **`gemini-3.6-flash`** is listed on Google's docs model page and marked GA*. The pricing excerpt shows its free-tier input as "Free of charge"*.
- **Other Flash models listed**\*: `gemini-3.8-flash` (the newest), `gemini-3.7-flash` and `gemini-3.5-flash`.
- **Flash-Lite models listed**\*: `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite` and `gemini-2.5-flash-lite`. There is also an alias, `gemini-flash-latest`*.
- **Google's guidance**: "For new projects use 3.5 Flash-Lite or 3.8 Flash."* The as-built tiers use 3.6 Flash, which that guidance doesn't name.

### Free tier and limits

- The pricing page says: "Start building free of charge with generous limits"*.
- Google publishes per-model rate limits only in AI Studio. A third party reports **~20 RPD** for the 3.5–3.8 Flash models and **~500 RPD** for 3.5 / 3.1 Flash-Lite (Sept 2026, scriptbyai.com). The research note doesn't mark whether that page was fetched, so treat the numbers as medium confidence at best.
- **Conflict: 3.8 Flash.** One excerpt says its API free tier is "Not available". A forum title reads "Gemini 3.8 Flash Free Tier 20 RPD". Unresolved.
- **Conflict: 3.1 Pro.** The excerpts disagree on whether 3.1 Pro has an API free tier. Bug E recorded `limit: 0` on `gemini-3.1-pro-preview` for this account (see "Consumer app vs API" below). Unresolved.

Implication: if the ~20 RPD report is right, the as-built `quality` and `frontier` tiers share about 20 free requests a day on `gemini-3.6-flash`, and the Flash-Lite models would allow far more. That rests on a third-party figure. Whether to switch models is for the human.

### The models list: endpoint vs docs page

> **Note (2026-09-24 handoff and 2026-09-25 research, not resolved):** the handoff says Google's models-list **endpoint** did not show `gemini-3.6-flash`, although the model works when called (fix 4, gotcha 4). The research says Google's **docs** model page lists `gemini-3.6-flash` as GA*. These are two different things, an API endpoint and a documentation page, so they don't necessarily contradict each other. The research doesn't report calling the models-list endpoint. Observation: both sources treat `gemini-3.6-flash` as a real, callable model name. They differ only on where it shows up. Left for the human.

## Gemini CLI free quota (2026-09-25 research)

Both documents were fetched from the `google-gemini/gemini-cli` GitHub repo:

| Route | Gemini CLI README | The repo's quota doc |
|-------|-------------------|----------------------|
| Google login (personal account) | "60 requests/min and 1,000 requests/day with personal Google account" | 1,000/day |
| Unpaid API key | "1000 requests/day with Gemini 3 (mix of flash and pro)" | 250/day, Flash only |

The two documents agree on the Google-login quota and **conflict on the API-key route**. Unresolved.

The v2 plan registers "Gemini CLI/API", and the DeepSeek master plan puts Gemini CLI in its integration diagram. The handoff doesn't say whether the Gemini CLI is installed or used, and none of the sources say whether it runs on [[crostini]].

## Gemma: Google's open models (slot 1)

Google's open Gemma models are on the [[ollama]] library and on [[openrouter]] as `:free` listings*. The research note judges these local tags a fit for the Chromebook, assuming ≤~6GB downloads and 6–9GB RAM free ([[jarvis-x-hardware]]):

- `gemma3:270m`, `gemma3:1b` and `gemma3:4b` (3.3GB, 128K, vision)*
- `gemma4:e2b-it-qat` (4.3GB, 128K)*. It is the only Gemma 4 build that fits. The research warns that the Gemma 4 sizes look unusual, so check them with `ollama show` before pulling.

Full tag details are on [[ollama]].

Under the ruling, Gemma run locally fits slot 1 ("local models ... that could work on any machine specially chrome os"). It is also "from google", which is slot 2. **Tokens (2026-09-25, follow-up ruling 8):** "Yes we need more tokens". Recommendation (interpretation): add a Flash-Lite model for volume or as a fallback, keeping `gemini-3.6-flash` for quality, because Flash-Lite reportedly has ~500 RPD free against ~20 RPD for Flash*. That's a change to Jarvis's registry, to be tested on the Chromebook first (gotcha 4). See [[jarvis-x-model-priority]], "Getting more tokens".

**Resolved (2026-09-25, follow-up ruling 2):** "if it fits both let it be in both", so Gemma is listed under both. Slot 1 outranks slot 2, so in practice a local Gemma is picked at slot-1 priority either way.

## Under the 2026-09-25 ruling

The ruling puts "the most free available from google" in slot 2, after local and free open-source (slot 1) and before Anthropic (slot 3) and OpenAI (slot 4). See [[jarvis-x-model-priority]].

The slot-2 candidates found so far:

| Route | Free allowance | How sure |
|-------|----------------|----------|
| Gemini API, `gemini-3.6-flash` (as built) | Free-tier input "Free of charge"*; ~20 RPD (third-party report) | Medium |
| Gemini API, Flash-Lite models | ~500 RPD (third-party report) | Medium at best |
| Gemini API, 3.8 Flash | Conflicting | Low |
| Gemini CLI, Google login | 1,000 requests/day, 60/min | Fetched |
| Gemini CLI, unpaid API key | 1,000/day or 250/day Flash only | Fetched, but the two documents conflict |

Implication (interpretation): "most free" could favour the Gemini CLI Google-login quota, or the Flash-Lite models, over the Flash models the as-built tiers use. The figures are third-party or in conflict. The CLI is a separate tool, not the API `registry.js` calls. Left for the human.

## Fix 4 — keep the model name (the list is "stale")

From the handoff: "registry.js had gemini-3.6-flash. Google's models-list endpoint does NOT show this model (it's stale), but the model works. Do not change it to a model from the list — the list is wrong."

"Verified working: gemini-3.6-flash (with the key in .env)."

Gotcha 4 repeats it: "Google's models-list endpoint is stale. gemini-3.6-flash works even though it isn't listed. Don't trust the list."

Note: "stale" and "wrong" are the handoff's characterisation. What the handoff actually observed is that the model is missing from the list but works when called. It doesn't say why the list omits it. The 2026-09-25 research found the model on Google's docs page (see "The models list: endpoint vs docs page" above).

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

The 2026-09-25 research found conflicting excerpts on whether 3.1 Pro has any API free tier (see "Free tier and limits" above). This doesn't change the handoff's observation for this account.

Implication: the v2 plan's "Claude/Gemini while subs live" assumed subscription-backed access. Per Bug E, a Google AI Pro subscription doesn't carry over to the API for `gemini-3.1-pro-preview`. If the Council's Analyst seat runs on the free API, the only Gemini model on Bug E's free list is `gemini-3.6-flash`. See [[the-council]]. The 2026-09-25 research lists more Flash and Flash-Lite models that may have free tiers, at medium confidence.

## Related

[[universal-model-layer]] | [[free-api-tiers]] | [[jarvis-x-runtime]] | [[jarvis-x-openai-compatible-api]] | [[starnet]] | [[the-council]] | [[groq]] | [[openrouter]] | [[ollama]] | [[crostini]] | [[source-jarvis-x-starnet-handoff]] | [[jarvis-x-plan-vs-reality]] | [[jarvis-x-model-priority]] | [[source-model-landscape-research]] | [[jarvis-x-hardware]]
