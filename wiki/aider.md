---
title: Aider
tags: [tool, coding-agent, jarvis-x, groq]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[groq]], [[jarvis-x-runtime]], [[jarvis-x-openai-compatible-api]], [[the-council]], [[crostini]], [[ollama]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x]], [[free-api-tiers]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
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

## Place in the Council

The [[the-council]] roster from the earlier plans gives implementation to Claude Code (Lead Developer) and review to Codex CLI (Code Reviewer). The handoff shows Aider as the coding agent actually in use. It doesn't say whether Aider replaces or supplements those seats. The coding-agent row of [[jarvis-x-plan-vs-reality]] records this as an open question.
