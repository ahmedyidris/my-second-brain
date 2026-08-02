---
title: ChromaDB
tags: [tool, vector-database, embeddings, rag, infrastructure]
sources:
  - https://www.trychroma.com/products/chromadb (accessed 2026-08-02)
  - https://realpython.com/chromadb-vector-database/ (accessed 2026-08-02)
  - https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide (accessed 2026-08-02)
  - https://www.geeksforgeeks.org/nlp/introduction-to-chromadb/ (accessed 2026-08-02)
related: [[obsidian]], [[jarvis-x]], [[ollama]], [[second-brain]], [[ruflo]]
last_updated: 2026-08-02
---

# ChromaDB

An open-source vector database (Apache 2.0 licensed) built for retrieval-augmented generation (RAG) and semantic search. Embeds directly into a Python or JavaScript application rather than requiring a separate managed service.

## Key characteristics

- Handles embedding, vector search, text search, document storage, and multimodal search internally — raw text goes in, semantic search comes out, without hand-rolling vector math.
- Default embedding model is `all-MiniLM-L6-v2`, producing 384-dimension vectors.
- Persists to disk by default (DuckDB + Apache Parquet under the hood in local mode), so development data survives restarts with no extra configuration.
- Runs via `pip`, `npm`, or Docker, in either in-memory or persistent mode.

## Role in this vault's ecosystem

ChromaDB is the vector-search backbone behind [[obsidian]]'s second-brain layer in [[jarvis-x]]'s memory stack — [[ollama]]'s `nomic-embed-text` model generates the embeddings ChromaDB indexes. [[ruflo]]'s `ruflo-rag-memory` plugin maps to this same Obsidian+ChromaDB pairing. It sits at the opposite end of the second-brain spectrum from the [[llm-wiki-pattern]] used in this vault: ChromaDB is embeddings-and-app-dependent, the wiki pattern is pure markdown with no vector store at all (see [[second-brain]] for the comparison).
