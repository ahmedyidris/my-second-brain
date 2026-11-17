---
title: llm-wiki-setup Skill
tags: [skill, meta, setup, llm-wiki]
sources:
  - raw/ai-second-brain-skills/llm-wiki-setup/SKILL.md
related: [[llm-wiki-pattern]], [[wiki-self-heal-skill]], [[second-brain]]
last_updated: 2026-07-27
---

# llm-wiki-setup Skill

Installs the Karpathy LLM wiki pattern into any folder in one pass. Creates `CLAUDE.md`, `AGENTS.md`, `raw/`, `wiki/index.md`, `wiki/log.md`, `.gitignore`, and commits the initial scaffold.

Installed at `~/.claude/skills/llm-wiki-setup` → invoked as `/llm-wiki-setup` in Claude Code.

## What it creates

```
<vault>/
├── CLAUDE.md              # the map — routing table, schema, workflows, guardrails
├── AGENTS.md              # minimal mirror for Codex and other non-Claude agents
├── .gitignore
├── raw/                   # immutable sources (LLM reads, never writes)
│   └── .gitkeep
└── wiki/
    ├── index.md           # catalog of every page, by category
    └── log.md             # chronological operation log
```

## Setup choices (asked once)

1. **Vault path** — absolute path, created if it doesn't exist
2. **Flat or nested** — flat (default, Karpathy's preference) or nested (`wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/analyses/`)
3. **Hot cache** — optional `wiki/hot.md` rolling 500-char buffer for recent context

## Safety

Will not overwrite an existing `CLAUDE.md` or `wiki/` without explicit confirmation.

## Installation

```bash
git clone https://github.com/NulightJens/ai-second-brain-skills.git ~/ai-second-brain-skills
ln -s ~/ai-second-brain-skills/llm-wiki-setup ~/.claude/skills/llm-wiki-setup
```

## Active vaults

- `~/my-second-brain` — initialized 2026-07-27, flat layout
- `~/research-vault` — initialized 2026-07-27, flat layout
