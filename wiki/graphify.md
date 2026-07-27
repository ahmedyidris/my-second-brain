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

- **805 nodes**, **1,974 edges**, **77 communities** (as of 2026-07-28, after .graphifyignore applied)
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

## MCP server

Graphify can expose a graph as an MCP tool server, letting any MCP-compatible agent query it without running graphify locally.

Requires the `[mcp]` extra (installs `mcp`, `uvicorn`, `httpx`, etc.):

```bash
uv tool install "graphifyy[mcp]" --force
```

```bash
# stdio (default) — spawned on demand by the agent
GRAPHIFY_PY=/home/jarvis/.local/share/uv/tools/graphifyy/bin/python
$GRAPHIFY_PY -m graphify.serve graphify-out/graph.json

# register with Claude Code (persists to ~/.claude.json)
claude mcp add graphify $GRAPHIFY_PY -- -m graphify.serve /abs/path/to/graphify-out/graph.json

# register with Kimi Code
kimi mcp add --transport stdio graphify -- $GRAPHIFY_PY -m graphify.serve graphify-out/graph.json

# HTTP — one server, whole team points at the URL
$GRAPHIFY_PY -m graphify.serve graphify-out/graph.json --transport http --port 8080
$GRAPHIFY_PY -m graphify.serve graphify-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

Both the positional argument and `--graph` flag are accepted:

```bash
$GRAPHIFY_PY -m graphify.serve graphify-out/graph.json
$GRAPHIFY_PY -m graphify.serve --graph graphify-out/graph.json   # same thing
```

For the HTTP transport: expose on `0.0.0.0` and set `--api-key` for a shared team endpoint with auth. With the default stdio transport, no network port is opened — the client spawns the server process directly.

**This vault**: graphify MCP server is registered in `~/.claude.json` (project-scoped). Claude Code spawns it automatically when graph tools are called.

## Advanced queries

```bash
# target a specific graph.json (not the default ./graphify-out/graph.json)
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json
```

## Workflow in CLAUDE.md

The vault `CLAUDE.md` instructs: run `graphify query "<question>"` before broad source browsing. The graph returns a scoped subgraph — much smaller context than raw grep. After modifying code/wiki, run `graphify update .` to keep the graph current.
