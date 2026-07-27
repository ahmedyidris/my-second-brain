# Ruflo — Self-Learning / Self-Optimizing Agent Architecture

```
User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers
                          ^                           |
                          +---- Learning Loop <-------+
```

Components:
- Ruflo: the CLI/MCP entry point (user-facing interface)
- Router: directs requests to the right swarm/agent
- Swarm: orchestrates a group of agents working in parallel
- Agents: the workers that execute tasks
- Memory: persistent storage agents read/write across sessions
- LLM Providers: the model backends (local or cloud)
- Learning Loop: feedback path from agents + memory back to the router — enables self-optimization
