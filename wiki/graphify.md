---
title: Graphify
tags: [tooling, knowledge-graph, codebase, navigation]
sources:
  - raw/2026-07-28-graphify-output-structure.md
related: [[llm-wiki-pattern]], [[second-brain]], [[jarvis-x]], [[the-council]]
last_updated: 2026-07-28
---

# Graphify

A knowledge graph tool that maps any project (code, docs, markdown) into a queryable graph — no embeddings, no vector store. Uses tree-sitter AST for code (free, local, deterministic) and an LLM for semantic passes on docs/images/PDFs.

## Install

```bash
# Recommended (isolated env):
uv tool install graphifyy
# if 'graphify' not found after: uv tool update-shell

# Alternatives:
pipx install graphifyy
pip install graphifyy   # may need PATH setup
```

Then register the skill with your AI assistant:

```bash
graphify install
```

## Output

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

## Commands

```bash
graphify update .                    # rebuild graph (AST-only, free)
graphify query "how does X work"     # scoped subgraph for a question
graphify path "concept-A" "concept-B"  # relationship path between two nodes
graphify explain "concept"           # focused explanation of one concept
```

## This vault (~/my-second-brain)

- **1,199 nodes**, **2,497 edges**, **109 communities** (as of 2026-07-28)
- `graphify-out/graph.html` — interactive browser view
- `graphify-out/GRAPH_REPORT.md` — highlights and suggested queries

## .graphifyignore

Controls which files graphify indexes. Same syntax as `.gitignore`. Place in the project root.

```
# Exclude noisy dirs
node_modules/
dist/
*.generated.py

# Only index src/, ignore everything else
*
!src/
!src/**
```

## Example output

```
$ graphify explain "APIRouter"
Node: APIRouter
  Source:    routing.py L2210
  Community: 2
  Degree:    47

Connections (47):
  --> RequestValidationError [uses] [INFERRED]
  --> Dependant [uses] [INFERRED]
  --> .get() [method] [EXTRACTED]
  <-- __init__.py [imports] [EXTRACTED]
  ...

$ graphify path "FastAPI" "ModelField"
Shortest path (3 hops):
  FastAPI --uses--> DefaultPlaceholder <--references-- get_request_handler() --references--> ModelField
```

Each edge is tagged `EXTRACTED` (read directly from source) or `INFERRED` (resolved by graphify) — you can tell what was explicit vs. inferred.

## Workflow in CLAUDE.md

The vault `CLAUDE.md` instructs: run `graphify query "<question>"` before broad source browsing. The graph returns a scoped subgraph — much smaller context than raw grep. After modifying code/wiki, run `graphify update .` to keep the graph current.
