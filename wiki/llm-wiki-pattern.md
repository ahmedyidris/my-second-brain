---
title: LLM Wiki Pattern
tags: [meta, pattern, knowledge-management, karpathy]
sources:
  - raw/2026-07-27-llm-wiki-pattern-why.md
  - raw/2026-07-27-llm-wiki-vault-structure.md
  - raw/2026-07-27-llm-wiki-skills-install.md
  - raw/2026-07-27-llm-wiki-query-patterns.md
  - raw/2026-07-27-llm-wiki-self-heal-prompt.md
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

## Example queries

Three prompts that put the wiki to work:

**Contradiction/synthesis:**
> "Where do my sources agree and disagree about `<topic>`?"

Reads all pages for the topic, surfaces agreements and conflicts, cites specific pages and their `sources:` frontmatter. Only works if pages have honest `sources:` — the guardrails pay off here.

**Audit/lint:**
> "What are the gaps in my wiki right now?"

Triggers the lint workflow: orphan pages, missing cross-references, concepts referenced ≥2 times without their own page, stale claims, data gaps. Returns a severity-ranked list.

**Autonomous self-heal:**
> "Run wiki-self-heal on this vault"

Runs the full `wiki-self-heal` skill loop: creates a `wiki-heal/YYYY-MM-DD` branch, audits for 6 gap types, researches and fills the top-N high-severity gaps, commits — never auto-merges. For audit-only: "Run wiki-self-heal audit-only" or "dry run wiki-self-heal".

**Query + file-back:**
> "Write a comparison page for X vs Y and file it back into the wiki."

Synthesizes from existing pages, writes a new analysis page (`wiki/x-vs-y-comparison.md`), adds it to `wiki/index.md` under Analyses, links it bidirectionally from both X and Y pages. Good answers compound — they don't disappear into chat history.

## Installation

Skills live at https://github.com/NulightJens/ai-second-brain-skills. Install once per machine:

```bash
git clone https://github.com/NulightJens/ai-second-brain-skills.git ~/ai-second-brain-skills
ln -s ~/ai-second-brain-skills/llm-wiki-setup  ~/.claude/skills/llm-wiki-setup
ln -s ~/ai-second-brain-skills/wiki-self-heal  ~/.claude/skills/wiki-self-heal
```

After this, `/llm-wiki-setup` and `/wiki-self-heal` are available in Claude Code.
