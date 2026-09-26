# StarNet on ChromeOS: install and run findings (2026-09-26)

These are session notes from answering Ahmed's ruling
(`raw/2026-09-26-ahmed-ruling-3-starnet-itself-on-chromeos.md`). I did the work
in a Debian cloud container, not on the Chromebook.

- StarNet version: upstream `androoAGI/starnet` at `7ee93cea`, package
  `starnet-harness` 0.12.4.
- Jarvis delivery: jarvis-x PR #37, commit `7aa69c1`.

## What StarNet is, at runtime

- **Engine:** `package.json` has `"engines": {"node": ">=18"}`. `npm start` runs `node sidecar/index.js`, which serves the whole product, UI and agent engine, on `127.0.0.1:8787` (the `PORT` env overrides it).
- **Linux support:** `INSTALL.md` says the public installers are Windows and macOS only, and that "Linux is not part of the public release train". The web mode is plain Node, and it ran here.
- **Runtime dependencies:** `@huggingface/transformers`, `ajv`, `kokoro-js`, `node-pty` and `ogg-opus-decoder`. The dev dependencies are `@napi-rs/canvas` and `@tauri-apps/cli`.
- **Repo size:** 3.3 GB. That is 1.6 GB of `.git`, plus `frontend/` 1.3 GB (`frontend/assets/industrial` alone is 1.2 GB), `website/` 1.3 GB, `docs/` 531 MB, `output/` 148 MB and `qa/` 57 MB.
- **What the app needs:** the sidecar requires only `sidecar/`, `shared/`, `frontend/` and `package.json`. A copy without `website/`, `docs/`, `output/` and `qa/` (1.3 GB) started with no errors and rendered the full UI.
- **Workspace lock:** current StarNet reclaims a dead workspace owner by itself (`sidecar/workspace-owner.js` checks the PID with `process.kill(pid, 0)`). The handoff's manual `WORKSPACE_BUSY` fix is for older checkouts.
- **Approval default:** StarNet's first-run "Create your Overseer" screen offers ASK FOR APPROVAL (the default) and FULL POWER ("uses the whole local computer without approval prompts").

## Install problems found, and fixes

1. **CUDA download.** `onnxruntime-node@1.24.3`'s postinstall downloads `Microsoft.ML.OnnxRuntime.Gpu.Linux` from nuget on linux/x64 by default. Here the download failed with `ECONNRESET`, and the whole `npm ci` failed. `ONNXRUNTIME_NODE_INSTALL=skip` (the package's own switch) avoids it. With that set, `npm ci --omit=dev` finished in 16 s.
2. **Bundled binaries.** `kokoro-js` ships its own `onnxruntime-node@1.21.0` with a 343 MB `libonnxruntime_providers_cuda.so` plus darwin/ and win32/ binaries inside the npm package. Deleting only the onnxruntime GPU/Mac/Windows binaries took node_modules from 1210 MB to 592 MB.
3. **node-pty.** It has prebuilds only for darwin and win32, so on Linux it compiles with node-gyp. That needs `build-essential` and `python3`.
4. **Fresh install size.** A fresh clone at depth 1, with `--filter=blob:none` and a sparse checkout excluding `website/`, `docs/`, `output/` and `qa/`, came to a 1.3 GB work tree, 0.9 GB of `.git` and 0.6 GB of pruned packages: about 2.8 GB in total.

## Runs through the Jarvis gateway (stand-in upstream model)

- **Provider probe:** StarNet's `/api/providers/probe` for `custom` (with `CUSTOM_OPENAI_BASE_URL` set) returned reachable and credentialVerified. `/api/models/custom` listed Jarvis's tiers and pinned models.
- **Agent runs:** `/api/run` with provider `custom` and model `fast` completed a chat run and a task run, each with reason `done` and $0.
  - The task run sent 87 tools through the gateway.
  - Background workers (skills, topic extraction) also used the custom provider.
- **Kill switch:** with `.jarvis-x-STOP` present, the run ended with `agent.run.error` and the message "Jarvis kill switch is engaged (.jarvis-x-STOP)".
- **No provider:** with no provider reachable, the run ended with "All providers failed for tier "fast": groq(no key) | openrouter(no key) | ollama(fetch failed)".
- **Memory:** StarNet used about 107 MB and the gateway about 52 MB of RSS.

## Launcher (`scripts/starnet.sh`, jarvis-x PR #37)

- **Commands:** doctor, install, start, stop, status, logs, clear-lock, prune.
- **What `start` does:**
  - removes `GROQ_API_KEY`, `GEMINI_API_KEY` and `OPENROUTER_API_KEY` from StarNet's environment (its own Groq path is Bug A);
  - sets `CUSTOM_OPENAI_BASE_URL=http://127.0.0.1:8010/v1` and `NODE_OPTIONS=--dns-result-order=ipv4first`.
- **Bug found and fixed while building it:** an unanchored `pgrep -f "node sidecar/index.js"` matched the shell that ran `stop`, and killed it. Matching is now `pgrep -u $(id -u) -f '^node sidecar/index\.js$'`.
- **Tests:** 17 assertions, offline, in CI. 12 of 12 mutations caught.

## Not verified

- Anything on the Chromebook itself: the Crostini build of node-pty, a real provider, and the GPU-less rendering of StarNet's station view in ChromeOS Chrome.
