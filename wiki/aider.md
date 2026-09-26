---
title: Aider
tags: [tool, coding-agent, jarvis-x, groq]
sources:
  - raw/2026-09-25-ahmed-rulings-2-providers-tiers-direction.md
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
related: [[groq]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[the-council]], [[crostini]], [[ollama]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x]], [[free-api-tiers]], [[jarvis-x-plan-vs-reality]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[source-model-landscape-research]]
last_updated: 2026-09-25
---

# Aider

The coding agent used on the [[jarvis-x]] source tree as of the 2026-09-24 handoff. It's launched from `~/jarvis-x` and pointed straight at [[groq]]'s `openai/gpt-oss-120b`.

## Launch

```bash
set -a && source ~/.jarvis-x/.env && set +a
cd ~/jarvis-x
aider --model groq/openai/gpt-oss-120b --no-show-model-warnings
```

| Part | Notes (per handoff) |
|------|---------------------|
| `set -a && source ~/.jarvis-x/.env && set +a` | Loads the API keys from `~/.jarvis-x/.env` (chmod 600). The StarNet and Hermes CLI launches use the same line. |
| `cd ~/jarvis-x` | The Jarvis source tree ([[jarvis-x-runtime]]) |
| `--model groq/openai/gpt-oss-120b` | Groq's `openai/gpt-oss-120b`, the same model behind Jarvis's `smart` tier |

## Using Aider

| Input at Aider's `>` prompt | Effect |
|-----------------------------|--------|
| `/add <path>` | Include a file |
| Plain text on its own line | A question to the model |
| `/exit` | Quit |

## Gotcha — never paste shell commands into Aider

> Never paste shell commands into Aider. Inside Aider's > prompt, only /commands or natural language. Anything else gets sent to the model as a question.

(Gotcha 1 in the handoff's PART 6.)

## Which backend Aider talks to

- **As launched in the handoff:** Groq directly (`groq/` model prefix), not through Jarvis. See [[groq]] for the fast/smart models. `openai/gpt-oss-120b` is on the handoff's free API list (Bug E, "verified") — see [[free-api-tiers]].
- **Jarvis `/v1` endpoint (Bug B):** the handoff names Aider as one of the callers of Jarvis's `/v1/chat/completions` (with Continue and StarNet agents). These callers "must read the file themselves and include its content in the message", because Jarvis is a chat API and doesn't read the filesystem ([[jarvis-x-openai-compatible-api]]). Implication: if Aider is pointed at Jarvis, file context has to come from Aider's side, for example via `/add`. The handoff gives no command for pointing Aider at the Jarvis endpoint.
- **Network:** Groq is Cloudflare-fronted. On [[crostini]] the IPv6 path truncates POST bodies to such APIs. The handoff doesn't report whether Aider was affected.
- **Local models:** [[ollama]] has `qwen2.5-coder:7b` (4.7GB) and `qwen2.5-coder:3b` (1.9GB) installed. The handoff doesn't say they're used with Aider.

## Under the 2026-09-25 priority ruling

The human's 2026-09-25 ruling puts local models and free open-source tiers first ([[jarvis-x-model-priority]]).

- **Local option:** a local slot-1 coding option on the Chromebook is Ollama's `qwen2.5-coder:3b` or `qwen2.5-coder:7b` (Alibaba's Qwen, a Chinese open model), already installed per the handoff. Per the 2026-09-25 research there's no small qwen3-coder: its smallest tag is `qwen3-coder:30b` at 19GB (search excerpt, medium confidence). The research's own suggestion is to keep `qwen2.5-coder:3b` / `:7b` for coding; that's its inference, not a fact ([[chinese-open-source-models]], [[source-model-landscape-research]]).
- **Pointing Aider at Ollama:** no source in this vault gives a command for it, so running Aider on a local Ollama model is possible in principle but unverified here.
- **As built:** the launch above uses Groq's free `openai/gpt-oss-120b`. [[jarvis-x-model-priority]] reads it as slot 1, a free hosted tier. It's OpenAI's open-weight model, so its slot was an open question. **Resolved (2026-09-25, follow-up ruling 1):** free counts as free, keeping the official name, so Groq's free `openai/gpt-oss-*` models are in the free tier (slot 1). The research gives Groq's free-tier limits for it as 30 RPM, 1,000 RPD, 8,000 TPM and 200,000 TPD per organization, measured Sept 14, 2026 (fetched).

## Place in the Council

The [[the-council]] roster from the earlier plans gives implementation to Claude Code (Lead Developer) and review to Codex CLI (Code Reviewer). The handoff shows Aider as the coding agent actually in use. It doesn't say whether Aider replaces or supplements those seats. The coding-agent row of [[jarvis-x-plan-vs-reality]] records this as an open question. Under the 2026-09-25 ruling, Claude Code (Anthropic) is slot 3 and Codex CLI (OpenAI) is slot 4 ([[the-council]]).
