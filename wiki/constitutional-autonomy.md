---
title: Constitutional Autonomy
tags: [jarvis-x, governance, v2, autonomy, safety]
sources:
  - raw/2026-09-24-jarvis-x-starnet-handoff.md
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[self-improvement-loop]], [[the-council]], [[jarvis-x-runtime]], [[starnet]], [[source-jarvis-x-starnet-handoff]], [[jarvis-x-plan-vs-reality]]
last_updated: 2026-09-24
---

# Constitutional Autonomy

The governance model for [[jarvis-x]]. Not a leash, not anarchy — real standing power governed like a constitution. [[jarvis-x]] runs as systemd services under its own Linux user with full ownership of `~/jarvis/`.

## Services

- `jarvis-core`
- `jarvis-scheduler`
- `jarvis-voice`

Auto-start on boot, self-restart on crash, weekly self-test.

> **Disagreement (2026-09-24 handoff vs Jarvis X v2 Ascension Plan):** The v2 plan says [[jarvis-x]] runs as systemd services `jarvis-core`, `jarvis-scheduler` and `jarvis-voice`, under its own Linux user that fully owns `~/jarvis/`. The handoff shows something different. supervisord runs `hermes-agent`, `hermes-api` (uvicorn, port 8000) and `tts-worker`, and is itself managed by the systemd unit `jarvis-supervisord.service`. The source lives in `~/jarvis-x`, and the unit's env file is `/home/ahmedyidris/.jarvis-x/.env` (see [[jarvis-x-runtime]]). Unknown: whether a dedicated Linux user exists (the handoff doesn't say which user the services run as, though the env file sits under the human's home directory); whether the three planned services were renamed, merged or never built; and whether a weekly self-test exists. On auto-start and restarts, the handoff only says "Services run automatically under systemd." Left for the human to resolve.

## Standing permissions (no approval needed)

- Read/organize its home directory
- Run scheduled jobs
- Call free APIs within quotas
- Draft content
- Propose skill diffs
- Index anything dropped into `inbox/`

## Gated actions (one-tap approval required)

Anything irreversible or external:
- Sending messages or posts
- Deleting files outside its home
- Spending money
- Changing its own governing files
- Enabling any trading API key

## The constitution file

`CONSTITUTION.md` in git — rules above, versioned. [[jarvis-x]] can *propose* amendments; only the human merges them.

## Safety controls

- **Black box:** append-only audit log of every action
- **Kill switch:** `jj halt` stops everything instantly
- **Hard limit:** fully unsupervised self-modification stays out permanently

This is the honest maximum of "self-governing" that is safe on real hardware.

The agents governed by this constitution form [[the-council]]. Gated actions require one-tap approval from the human before any council member can execute them.

## Practical safety lessons (2026-09-24 handoff)

The 2026-09-24 handoff ([[source-jarvis-x-starnet-handoff]]) lists these rules in its "what not to do" section (PART 8), based on what went wrong on the machine:

| Rule (verbatim) | Context from the handoff |
|-----------------|--------------------------|
| "Do not run YOLO-mode agents on this machine. The venv and StarNet workspace have both been destroyed by that pattern." | The Python venv is `~/venv-ai` (3.11, uv-managed). [[starnet]] state lives in `~/.local/share/StarNet/workspaces/`. Inference: these are the "venv" and "StarNet workspace" meant; the handoff doesn't name the paths in this line. |
| "Do not put API keys in git. .env is gitignored — keep it that way." | API keys live in `~/.jarvis-x/.env` (chmod 600). They reach the Jarvis services via the systemd `EnvironmentFile=/home/ahmedyidris/.jarvis-x/.env` drop-in, and reach shells via `set -a && source ~/.jarvis-x/.env && set +a` ([[jarvis-x-runtime]]). Unknown: which `.env` the "gitignored" line means. `~/.jarvis-x/.env` sits outside the `~/jarvis-x` source tree, and the handoff doesn't say whether the repo has its own `.env`. |

Interpretation (not stated in the handoff): the YOLO-mode lesson fits the reasoning behind the gated-actions model above. The losses it describes (a destroyed venv and a destroyed StarNet workspace) are the kind of irreversible action that approval gates exist to catch. The handoff doesn't define "YOLO-mode", doesn't say which agents were run that way, and doesn't say whether they were Jarvis or Council agents governed by this constitution.

**Not covered by the handoff:** `CONSTITUTION.md`, the append-only audit log ("black box") and the `jj halt` kill switch aren't mentioned. Their as-built status is unknown. See [[jarvis-x-plan-vs-reality]].
