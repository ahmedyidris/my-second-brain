---
permalink: second-brain/raw/2026-07-27-llm-wiki-vault-structure
title: 2026-07-27-llm-wiki-vault-structure
type: note
---

# LLM Wiki Vault Structure

```
<your-vault>/
├── CLAUDE.md              # the map — AI reads this first
├── AGENTS.md              # mirror for Codex and other agents
├── raw/                   # immutable sources (LLM reads, never writes)
└── wiki/                  # LLM-owned markdown
    ├── index.md           # catalog of every page
    ├── log.md             # chronological operation log
    └── <pages>.md         # entity / concept / analysis pages
```