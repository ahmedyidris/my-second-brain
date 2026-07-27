---
title: Constitutional Autonomy
tags: [jarvis-x, governance, v2, autonomy]
sources:
  - raw/Jarvis X Resources/Jarvis X/Jarvis_X_v2_Ascension_Plan.md
  - raw/Jarvis X Resources/DeepSeek Files/DeepSeek_Jarvis_X_Master_Plan.md
related: [[jarvis-x]], [[self-improvement-loop]]
last_updated: 2026-07-27
---

# Constitutional Autonomy

The governance model for [[jarvis-x]]. Not a leash, not anarchy — real standing power governed like a constitution. [[jarvis-x]] runs as systemd services under its own Linux user with full ownership of `~/jarvis/`.

## Services

- `jarvis-core`
- `jarvis-scheduler`
- `jarvis-voice`

Auto-start on boot, self-restart on crash, weekly self-test.

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
