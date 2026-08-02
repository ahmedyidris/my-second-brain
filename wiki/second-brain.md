---
title: Second Brain
tags: [meta, knowledge-management, pattern]
sources:
  - raw/2026-07-27-llm-wiki-pattern-why.md
related: [[llm-wiki-pattern]], [[jarvis-x]], [[research-vault]], [[obsidian]], [[chromadb]]
last_updated: 2026-07-27
---

# Second Brain

A personal knowledge management system that externalises memory, thinking, and synthesis into a persistent, queryable store — so knowledge accumulates across sessions instead of evaporating after each conversation or project.

The term was popularised by Tiago Forte ("Building a Second Brain"). The LLM variant applies the same principle but replaces manual note-taking with an AI that reads, extracts, and writes on your behalf.

## The problem it solves

Default AI workflow: paste context → get answer → start new chat → paste again. Nothing compounds.

A second brain breaks that loop: knowledge is compiled once from sources and kept current in a structured wiki. Future queries read the wiki, not the raw sources.

## Implementations in this vault

- `~/my-second-brain` — primary vault, [[jarvis-x]]-focused ([[llm-wiki-pattern]] structure)
- `~/research-vault` — secondary vault for research topics ([[research-vault]])

## The LLM wiki variant

The [[llm-wiki-pattern]] is the specific implementation used here: no vector database, no embeddings — just markdown files, `[[wikilinks]]`, and a routing table in `CLAUDE.md`. The folder is the app.

[[obsidian]] is an alternative/complementary tool: a GUI markdown editor with plugin ecosystem, used as the second-brain layer in [[jarvis-x]]'s memory stack alongside [[chromadb]].
