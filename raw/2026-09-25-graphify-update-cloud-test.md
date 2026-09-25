# graphify `update` test from a cloud checkout
# Date: 2026-09-25
# Author: Claude Code session (observed tool output, recorded verbatim; not a human-written source)

---

## Setup

- graphify installed with `pip install graphifyy` into a scratch venv. `pip show graphifyy` reported `Version: 0.9.67`.
- The vault was copied (without `.git`) into a scratch directory, and the command was run on that copy only, never on the real vault.
- The cloud checkout lacks the gitignored, local-only files that the committed `graphify-out/manifest.json` lists (for example `raw/Apps Downloaded/...`).

## `graphify --help` (excerpt, verbatim)

```
  update <path>           re-extract code files and update the graph (no LLM needed)
    --force                 overwrite graph.json even if the rebuild has fewer nodes
                            (also: GRAPHIFY_FORCE=1 env var; use after refactors that delete code)
    --no-cluster            skip clustering, write raw extraction only
```

## Run on the copy (verbatim)

```
before nodes 811 links 1980
Re-extracting code files in . (no LLM needed)...
[graphify watch] 3 file(s) not classified (no supported extension or shebang), skipped: .gitignore, .gitkeep, .graphifyignore
[graphify watch] community set changed since labeling (63 saved labels, 78 communities now; renamed 17 community(ies) by their hub). Run `graphify label` to refresh names with the LLM.
[graphify] backed up curated graph (4 files) -> 2026-09-25/
[graphify watch] Rebuilt: 585 nodes, 860 edges, 78 communities
[graphify watch] graph.json, graph.html and GRAPH_REPORT.md updated in graphify-out
Code graph updated. For doc/paper/image changes run /graphify --update in your AI assistant.
Tip: set GEMINI_API_KEY or GOOGLE_API_KEY to use Gemini for semantic extraction.
after nodes 585 links 860
```

## What was observed

- `graphify update .` re-extracted code only. Its own output says doc changes need `/graphify --update` in the AI assistant.
- From a checkout missing the local-only files, it rewrote `graph.json` with 585 nodes where the committed graph had 811, even without `--force`. It backed up the previous graph to a dated folder, `2026-09-25/`, first.
