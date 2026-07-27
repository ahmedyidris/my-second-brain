# JARVIS X — v2.0 "Ascension" Plan

---

## 1. THE IDENTITY

**JARVIS X** — *Just A Rather Very Intelligent System — X.*
- **The X:** the unknown variable, the tenth iteration, the sovereign edition. Not Stark's butler in the cloud — *your* resident intelligence, living on your own hardware.
- **Brand line:** *"JARVIS X — the system that runs the house."* / *«جارفيس إكس — النظام اللي بيدير البيت»*
- Bilingual by design: English and Arabic (Egyptian + formal MSA) are both first-class citizens.
- (Shelved alternates, if ever needed for a public/commercial name: SIRAJ سراج "the guiding light", HORUS, NADIM.)

---

## 2. WHAT CHANGES FROM v1 (reframe)

| Area | v1 (current blueprint) | v2 Ascension |
|---|---|---|
| Models | Router: local Ollama + Gemini/Groq/OpenRouter | **Universal Model Layer:** every provider behind one interface, incl. Claude/Gemini while subs live, hot-swap free tiers after |
| Platform | Pop!_OS only | **Linux-first → Windows → PWA (iOS/Android) → macOS** |
| Voice | Whisper + Piper scripts | **Multi-accent voice engine** (see §4) |
| Autonomy | Approval gates | **Constitutional autonomy** — laptop as body/home (see §5) |
| Income | Outlier + n8n gigs | + **Content Engine** (video/audio, bilingual) as stream #3 |
| Trading | Excluded | **Market Intelligence module — testnet/paper only**, live-capable behind hard gates (see §7) |
| Delivery | Scripts + CLI | **The JARVIS X App** — one branded product (see §8) |

---

## 3. UNIVERSAL MODEL LAYER (integration with all models)
- One `providers/` interface, one config: `jj ask "..." --tier local|fast|smart|long`.
- Registered providers: **Ollama (local)**, **Gemini CLI/API**, **Groq**, **OpenRouter** (28+ free models incl. DeepSeek/Llama), **Anthropic** (while sub lives, then optional API), **NVIDIA NIM free**, **Mistral free tier**.
- Router rules: privacy-sensitive → local only; long-context → Gemini; fast loops → Groq; fallback chain on quota errors; per-provider daily counters in SQLite.
- Every provider is optional. JARVIS X must boot and function with zero cloud keys.

## 4. VOICE ENGINE (accents & bilingual)
**Offline core (always works):** Faster-Whisper (STT, auto EN/AR detect) + **Piper** (TTS) — multiple en_US and en_GB voices, male & female, plus an Arabic voice; runs on your CPU.
**Online accent pack (free, needs internet):** **edge-tts** — Microsoft neural voices at $0:
- English: American (m/f), British (m/f), **Irish (en-IE)**, Australian, Indian; *Scottish is the thinnest in free TTS — nearest matches via community Piper voices; flagged best-effort.*
- Arabic: **Egyptian (ar-EG, male & female)** and **formal MSA (ar-SA and others)**.
**Config:** `voice:` block in config.yaml → `accent: us|gb|ie|eg|msa`, `gender: m|f`, `engine: piper|edge`. One command switches JARVIS X's entire manner of speech.
**Later (GPU box):** XTTS-class local voice cloning for a custom signature "Jarvis voice."

## 5. CONSTITUTIONAL AUTONOMY (the laptop as body & home)
JARVIS X gets real standing power, governed like a constitution — not a leash, not anarchy:
- **Body:** runs as systemd services (`jarvis-core`, `jarvis-scheduler`, `jarvis-voice`) under its own Linux user with full ownership of `~/jarvis/` (vault, DB, skills, media workspace). Auto-start on boot, self-restart on crash, weekly self-test.
- **Standing permissions (no approval needed):** read/organize its home, run scheduled jobs, call free APIs within quotas, draft content, propose skill diffs, index anything you drop into `inbox/`.
- **Gated actions (one-tap approval):** anything irreversible or external — sending messages/posts, deleting outside its home, spending any money, changing its own governing files, enabling any trading key.
- **Constitution file:** `CONSTITUTION.md` in git — the rules above, versioned; JARVIS X can *propose* amendments, only you merge them.
- **Black box + kill switch:** append-only audit log of every action; `jj halt` stops everything instantly.

This is the honest maximum of "self-governing" that is safe on real hardware. Fully unsupervised self-modification stays out — permanently.

## 6. CONTENT & MONETIZATION ENGINE (money stream #3)
Pipeline (all free-tier): topic queue in vault → script drafted by the Council → **voiceover via edge-tts/Piper** (your accent choice) → assembly via **ffmpeg** templates (stock/AI images + subtitles, Arabic & English) → you approve → publish.
- **Focus niches:** Arabic-language AI explainers (hugely under-served vs English) and bilingual tech shorts. Your Egyptian Arabic is the moat.
- **Music:** treat as *content garnish*, not a stream — free AI-music tiers don't grant commercial rights; don't monetize music until a paid tier is justified by revenue.
- **Honest math:** YouTube requires 1k subs + 4k watch-hours (or 10M Shorts views) before payouts — expect **months of $0**, then compounding. JARVIS X runs this stream mostly on autopilot, so its cost is low; treat all revenue as bonus on top of Outlier + gigs, never instead of them.

## 7. MARKET INTELLIGENCE MODULE (the trading answer)
What gets built now — genuinely useful, zero capital at risk:
- **Binance Spot Testnet + read-only market data:** price feeds, watchlists, a daily Arabic/English market brief, alert rules ("BTC -5% in 24h → notify me").
- **Paper-trading engine:** JARVIS X simulates any strategy *you* define, logs every simulated trade to a journal, and reports monthly stats honestly (win rate, drawdown, vs. simply holding).
- **Hard gates before ever going live:** (1) 3+ months of logged paper results you have personally reviewed, (2) surplus money only — never income you need, (3) live API keys with trade permission are activated by you, manually, withdrawals-disabled, never stored by default.
- **What JARVIS X will not do:** invent strategies presented as advice, or promise returns. The module is infrastructure; strategy and risk stay yours. Your v1 blueprint's warning stands — for undercapitalized traders this is negative-EV; the testnet module gives you the machine without the trap.

## 8. THE JARVIS X APP + BRAND (final stage)
- **Architecture:** FastAPI backend (already the daemon) + one **web UI** served locally → installable as a **PWA** on your phone (this is the iOS/Android answer at $0). Same UI wrapped with **Tauri** later for Windows/macOS desktop builds.
- **Platform order & why:** ① Linux (native, first) ② Windows (biggest client market for your gigs) ③ PWA → covers iPhone/iPad/Android immediately, no Apple fees ④ macOS/native iOS only after the GPU box & revenue (needs Mac hardware + $99/yr).
- **Brand kit (self-inspired, as requested):** name JARVIS X; mark = an arc-reactor ring forming the letter X; palette **obsidian black + arc gold** (kept from your Gothic-Arcane doctrine); brand voice = calm, precise, bilingual. JARVIS X generates its own brand assets as one of its first content-engine jobs — *the system literally brands itself.*
- **Definition of "finished v2.0":** one installer script → services up → web UI on phone & laptop → voice chat in chosen accent → 3 automations live → content pipeline has produced 10 published pieces → daily market brief arriving → constitution + audit log active.

## 9. UPDATED 12-WEEK OVERLAY (v2 items slot into the existing plan)
- **Wk 1-2:** unchanged (extraction sprint + income) **+ register handles/domain for Jarvis X** ($0-12; note "Jarvis" is crowded online — grab a distinctive handle like @jarvisx-ai or use SIRAJ as the public alias if handles are taken).
- **Wk 3-4 (Claude Code sprint):** build Universal Model Layer + Constitution/audit-log skeleton *while you still have Claude*.
- **Wk 5-6:** voice engine w/ accent config; PWA-ready web UI shell.
- **Wk 7-8:** content engine v1 → first 5 bilingual pieces; Windows run-through.
- **Wk 9-10:** Market Intelligence (testnet + daily brief); income scale-up unchanged.
- **Wk 11-12:** brand kit, installer, docs → **tag JARVIS X v2.0**, demo video (made *by* Jarvis X's own pipeline — that is the launch content).

---

## 10. THE PROMPT (paste this to me to execute)

> **JARVIS X Ascension — execute.** Read the Unified Master Blueprint and the JARVIS X v2.0 Ascension Plan in project knowledge; v2 overrides v1 where they conflict, and my constraints (CPU-only Y50-70, $0/month, 6-10 hrs/wk, Egypt/Payoneer, income-first 60/40) still bind everything.
> Confirm in 3 lines: current week, what's expiring soonest, and today's single priority.
> Then execute the current week's v2 overlay item: give me complete, deterministic scripts/commands for a fresh Pop!_OS terminal — Universal Model Layer, Constitution + audit log, voice engine with accent config, PWA UI, content pipeline, or testnet market module, whichever the week calls for. Respect the constitution: anything irreversible gets an approval step; the trading module stays testnet/paper with live-gates intact; never design self-modification without my merge.
> End with: git commit message, updated Context block, progress %, and next session's task.

---
*JARVIS X — Sovereign. Bilingual. Yours. The system that runs the house.*
