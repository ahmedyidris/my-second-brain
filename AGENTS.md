# LLM Wiki — AGENTS.md

This folder is a Karpathy-style LLM wiki. If you are Claude Code, read `CLAUDE.md` instead — it has the full schema. This file is the minimal mirror for OpenAI Codex and other agents.

## Layout

- `raw/` — source documents. **Read only. Never modify.**
- `wiki/` — your workspace. Create and update markdown files here.
- `wiki/index.md` — catalog of every page. Read this first on any query.
- `wiki/log.md` — append-only operation log.

## Page format

Frontmatter: `title`, `tags`, `sources`, `related`, `last_updated`. Use `[[wikilinks]]` for cross-references. One concept per page.

## Log format

Every operation appends one entry:

```
## [YYYY-MM-DD] <op> | <title>
```

Ops: `ingest`, `query`, `lint`, `update`, `init`.

## Operations

**Ingest**: read source → report takeaways → identify affected pages → update existing + create new → update index → append log.

**Query**: read index → find pages → synthesize with citations → offer to file good answers back as new pages.

**Lint**: scan for contradictions, stale claims, orphans, missing pages, missing cross-refs, data gaps → propose severity-ranked fixes.

## Guardrails

- Never modify files in `raw/`.
- Never delete wiki pages without explicit confirmation — flag instead.
- Never add factual claims without sources.
- Never fabricate citations.
- Never silently resolve contradictions — note them.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
