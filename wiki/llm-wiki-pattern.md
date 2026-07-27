---
title: LLM Wiki Pattern
tags: [meta, pattern, knowledge-management, karpathy]
sources:
  - raw/2026-07-27-llm-wiki-pattern-why.md
  - raw/2026-07-27-llm-wiki-vault-structure.md
related: [[second-brain]], [[wiki-self-heal-skill]], [[llm-wiki-setup-skill]]
last_updated: 2026-07-27
---

# LLM Wiki Pattern

The Karpathy LLM wiki pattern: instead of re-pasting context into every chat session, the LLM reads each source once, extracts the knowledge, and writes it into an interlinked set of markdown files. Future queries read the wiki, not the sources. Knowledge is compiled once and kept current.

**Core insight:** most AI workflows are stateless — paste, answer, forget. The wiki pattern makes knowledge compound.

No vector database. No embeddings. No chunking pipeline. The folder is the app.

## Vault structure

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

## Three-layer mental model

| Layer | What it is | Rules |
|-------|-----------|-------|
| The map | `CLAUDE.md` at vault root | AI reads this first, every time. Contains routing table, naming conventions, workflows, guardrails. |
| The rooms | `raw/` and `wiki/` | `raw/` is immutable (read-only). `wiki/` is LLM-owned. |
| The workspace | Markdown files in each room | `[[wikilinks]]` between pages; `wiki/index.md` as catalog; `wiki/log.md` as timeline. |

## Three operations

- **Ingest** — read source → extract entities and concepts → write wiki pages → update index → log
- **Query** — read index → find relevant pages → synthesize with citations → offer to file good answers back
- **Lint** — scan for contradictions, orphans, missing pages, stale claims, data gaps → propose fixes

## Why it works at scale

`wiki/index.md` replaces RAG at small-to-moderate scale (hundreds of pages). Naming conventions replace a database. The routing table in `CLAUDE.md` replaces a search index. No infrastructure to maintain — the folder is the app.

## Skills

- `llm-wiki-setup` — installs the full vault structure in one pass
- `wiki-self-heal` — autonomous audit + research loop; runs on a schedule or on demand
