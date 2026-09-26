---
title: Hermes Agent
tags: [jarvis-x, component, agent, local-ai]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
  - raw/2026-09-25-ahmed-rulings-machine-and-model-priority.md
  - raw/2026-09-25-model-landscape-research.md
related: [[jarvis-x]], [[the-council]], [[self-improvement-loop]], [[jarvis-x-runtime]], [[aider]], [[jarvis-x-voice-engine]], [[jarvis-x-openai-compatible-api]], [[ollama]], [[jarvis-x-model-priority]], [[chinese-open-source-models]], [[jarvis-x-hardware]], [[groq]], [[gemini]], [[source-jarvis-x-starnet-handoff]], [[source-model-landscape-research]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-25
---

# Hermes Agent

The core reasoning brain of [[jarvis-x]]. A self-improving local agent with 70+ default skills and cross-session memory. Runs entirely on local hardware via Ollama.

## Key features

- Writes its own new skills automatically (automatic skill creation)
- Cross-session conversation memory
- 70+ default tools: file edit, command run, web browse
- Structured JSON function/tool calling
- Local-first: no cloud dependency

## Models

| Model | Use case | Speed on CPU |
|-------|----------|-------------|
| llama3.2:3b | Primary (CPU) | 8–12 t/s |
| qwen3:1.5b | Fast alternative | 15–20 t/s |
| hermes3:8b | Future (GPU/16GB RAM) | 1–3 t/s |

These are the master plan's picks, written for the Lenovo Y50-70. See the next section for the current machine.

## Local models under the 2026-09-25 ruling

Under the human's 2026-09-25 ruling, Hermes's local model choices follow [[jarvis-x-model-priority]] (local and free open-source first, including Chinese open models via Ollama) and [[ollama]] (what fits the current machine).

- **The plan's `hermes3:8b` is Lenovo-era.** The master plan marks it "Future (GPU/16GB RAM)". The Chromebook ([[jarvis-x-hardware]]) has 14GB RAM and no GPU. Implication: it meets neither part of that condition.
- **Is a `hermes3` tag still on the Ollama library?** Not covered by the research ([[source-model-landscape-research]]).
- **As built,** the Jarvis `local` tier runs `qwen2.5:3b` ([[jarvis-x-runtime]]).
- **Candidates:** see "Recommended local-first stack for the Chromebook (inference)" on [[jarvis-x-model-priority]], and [[chinese-open-source-models]] for what else fits. That stack is the researcher's recommendation, not a tested choice, and it doesn't pick a model for Hermes specifically.

## Installation

```bash
ollama launch hermes
# or
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

## Role in the system

Part of [[the-council]] as "Core Agent Brain". Powers the [[self-improvement-loop]] — analyzes its own daily logs, generates improved prompts and new tools, auto-implements with safety checks.

## As-built (2026-09-24 handoff)

As of the 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]), the running deployment ([[jarvis-x-runtime]]) has two supervisord services with Hermes names, both RUNNING under the systemd unit `jarvis-supervisord.service`:

| Service | State | Notes |
|---------|-------|-------|
| `hermes-agent` | RUNNING | — |
| `hermes-api` | RUNNING | uvicorn, port 8000 |

The same supervisord group also runs `tts-worker` (degraded; see [[jarvis-x-voice-engine]]).

The handoff names these only by their service names, `hermes-agent` and `hermes-api`. It does not say whether they are the Nous Research Hermes Agent described above, how they were installed, or which of the features listed above (skill creation, cross-session memory, 70+ tools) are active.

### The `registry:` branch in `hermes.py`

`hermes.py` has a `registry:` branch that routes the registry (cloud) tiers; fix 2 below names fast/smart/frontier as going through it. See [[jarvis-x-runtime]] for the tier table. Implication: the `/v1` adapter's `tier_to_model` maps `fast`, `smart`, `quality` and `frontier` to `registry:*` values ([[jarvis-x-openai-compatible-api]]), which appear to feed this branch. The handoff names both but does not spell out the call path.

**Fix 2 (system prompt dropped on registry tiers):** the `registry:` branch in `hermes.py` replaced the curl command without including the system prompt. So fast/smart/frontier all answered "I am Qwen" despite the prompt forbidding it. Fix: prepend system in the registry branch (committed as `4281158`).

### Hermes CLI

```bash
set -a && source ~/.jarvis-x/.env && set +a
hermes
```

`~/.bashrc` needs: `export PATH="$HOME/venv-ai/bin:$PATH"`

Implication: the `hermes` executable appears to live in `~/venv-ai/bin` (the uv-managed Python 3.11 venv); the handoff states only the PATH requirement.

### Aider (separate coding agent)

The handoff launches [[aider]] with `--model groq/openai/gpt-oss-120b`, which is the same model as the `smart` tier. Aider calls [[groq]] directly and does not go through Hermes or the `/v1` adapter. See [[aider]] for the launch block and the gotcha about never pasting shell commands into Aider's prompt.

### Disagreements with the plan

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** this page says Hermes "runs entirely on local hardware via Ollama" and is "Local-first: no cloud dependency". The handoff shows the `registry:` tiers in `hermes.py` routed to cloud providers — `fast`/`smart` on [[groq]] and `quality`/`frontier` on [[gemini]] — with only the `local` tier on [[ollama]]. The handoff does not say whether Hermes can still run with the cloud tiers unavailable. Left for the human to resolve.

> **Disagreement (2026-09-24 handoff vs DeepSeek Jarvis X Master Plan):** the Models table above lists `llama3.2:3b`, `qwen3:1.5b` and `hermes3:8b`. The as-built `local` tier is `qwen2.5:3b`, and none of the three planned models appear in the handoff's list of Ollama models present (`qwen2.5:7b`, `qwen2.5:3b`, `qwen2.5-coder:7b`, `qwen2.5-coder:3b`, `nomic-embed-text`). The handoff does not say why the model choice changed. Left for the human to resolve.
>
> **Resolved by the human (2026-09-25), machine part only:** the Chromebook is current, so the handoff's machine is the one to plan for. The model choice itself stays open: the ruling sets a priority order ([[jarvis-x-model-priority]]), not specific models for Hermes.

## Related

[[jarvis-x]] | [[jarvis-x-runtime]] | [[aider]] | [[jarvis-x-openai-compatible-api]] | [[the-council]] | [[self-improvement-loop]] | [[ollama]] | [[jarvis-x-model-priority]] | [[chinese-open-source-models]] | [[jarvis-x-hardware]] | [[groq]] | [[gemini]] | [[source-jarvis-x-starnet-handoff]] | [[source-model-landscape-research]] | [[jarvis-x-plan-vs-reality]]
