---
title: ChromaDB
tags: [tool, vector-database, embeddings, rag, infrastructure]
sources:
  - https://github.com/chroma-core/chroma (accessed 2026-08-16)
  - https://realpython.com/chromadb-vector-database/ (accessed 2026-08-16)
related: [[obsidian]], [[ollama]], [[jarvis-x]], [[ruflo]], [[second-brain]], [[source-deepseek-jarvis-x-master-plan]]
last_updated: 2026-08-16
---

# ChromaDB

An open-source vector database — "AI-native" data infrastructure for storing and querying embeddings. Referenced across 7 pages in this vault ([[obsidian]], [[jarvis-x]], [[ollama]], [[ruflo]], [[second-brain]], [[source-deepseek-jarvis-x-master-plan]], `wiki/index.md`) as the vector-search half of Jarvis X's memory stack, but had never had its own page until this pass.

## What it does

- Stores embeddings + metadata, then finds nearest-neighbor matches for a query embedding — the core primitive behind retrieval-augmented generation (RAG) and semantic search.
- Simple API: create a collection, add documents (auto-embedded and auto-tokenized if you don't supply vectors yourself), query by text or vector.
- Uses HNSW (Hierarchical Navigable Small World) graphs for approximate nearest-neighbor search over high-dimensional vectors.
- Supports metadata filtering alongside vector similarity (e.g. "semantically similar AND tag=jarvis-x").

## Deployment modes

- **In-process/embedded** — runs inside your Python/JS process, persists to a local directory. This is the mode implied by this vault's `brain-mcp` setup (see [[obsidian]]).
- **Client-server** — `chroma run --path /chroma_db_path` starts a standalone server other processes talk to over HTTP.
- **Chroma Cloud** — hosted/serverless option (not used in this vault's local-first, zero-cloud-keys design — see [[jarvis-x]] sovereignty principles).

## License & install

Apache 2.0. `pip install chromadb` (Python) or `npm install chromadb` (JS/TS).

## Role in this vault's stack

In [[jarvis-x]], ChromaDB is the vector-search backend behind [[obsidian]]'s "second brain" layer, reached via `brain-mcp`. [[ollama]]'s `nomic-embed-text` model supplies the embeddings that ChromaDB indexes — the two tools are paired: Ollama embeds, ChromaDB stores and searches. [[ruflo]]'s `ruflo-rag-memory` plugin maps to this same Obsidian+ChromaDB combination (per [[ruflo]]'s plugin table).

Distinct from [[graphify]]'s approach: graphify builds an explicit AST/LLM-extracted graph with typed edges (no embeddings at all), while ChromaDB does purely embedding-similarity retrieval. The two are complementary retrieval strategies, not competitors — see [[graphify]] and [[llm-wiki-pattern]] for why this vault itself uses neither (the wiki pattern reads `wiki/index.md` instead of embedding/graph retrieval).
