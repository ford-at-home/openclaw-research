---
title: "Building a Personal AI Assistant on AWS"
category: writing
tags: [openclaw, aws, ai, personal-assistant, blog-post, bedrock, telegram, voice-memo, knowledge-base]
date: "2026-04-14"
source: conversation
status: draft
---

# Building a Personal AI Assistant on AWS

## What Changed

Three things converged between 2023 and 2026:

1. **Context windows** grew by two orders of magnitude. Claude Sonnet 4.6 has a 200,000-token context window. Workspace files are ~6,650 tokens — 3% of that window.
2. **Models crossed the instruction-following threshold.** Nova 2 Lite degrades on instruction-following as context grows. Sonnet 4.6 holds the instructions at depth.
3. **Inference costs dropped** to where persistence is a feature, not a budget decision. Prompt caching brings input tokens to $0.30/M instead of $3.00/M.

## The Stack

- **OpenClaw** — open-source Node.js gateway
- **AWS EC2** — t4g.medium, ARM64/Graviton, no public ports, SSM access only
- **Amazon Bedrock** — Claude Sonnet 4.6 via IAM role, no credentials stored
- **Telegram** — bot-native, forum topics give isolated thread history

Six markdown files injected into every prompt: SOUL.md, USER.md, AGENTS.md, TOOLS.md, MEMORY.md, IDENTITY.md. ~6,650 tokens combined. To change behavior: edit a file, push, done. No restart required.

## Cost

| Service | Light (~10 turns/day) | Moderate (~50/day) | Heavy (~200/day) |
|---|---|---|---|
| EC2 t4g.medium | $26.93 | $26.93 | $26.93 |
| Claude Sonnet 4.6 | $9.45 | $47.25 | $189.00 |
| AWS Transcribe | $2.40 | $2.40 | $12.00 |
| Parallel AI (1 research/day) | $0.75 | $2.25 | $7.50 |
| **Total** | ~$39.53 | ~$78.83 | ~$235.43 |

Observed: heavy usage ran ~$125/month vs $189 projection — prompt caching cut input token costs by 10x.

## How It Works

**Stage 1 — Channel Normalization.** grammY (Telegram) normalizes every message to the same internal object before the model sees it.

**Stage 2 — Session Lock.** One session, one active task at a time. Prevents concurrent tool calls corrupting shared state.

**Stage 3 — Context Assembly.** Workspace files (re-read from disk every turn), MEMORY.md, session JSONL transcript, skill manifests (names only, full file loaded on demand).

**Stage 4 — Inference.** Structured function calling via Bedrock. Schema enforced at the provider level.

**Stage 5 — ReAct Loop.** Tool call → run tool → feed result back → next decision. No fixed depth limit.

**Stage 6 — Memory.** Flat files: MEMORY.md for persistent facts, memory/YYYY-MM-DD.md for daily log. Re-indexed into SQLite automatically. Human-readable, diffable, correctable.

**Stage 7 — Automation Substrate.** Hooks, cron, Task Flows, Webhooks plugin. Durable stateful orchestration vs. stateless trigger-action pipelines.

## The Knowledge Base

Voice memo → .oga file → S3 → AWS Transcribe → transcript → LLM integration pass → wiki pages (entities, concepts, synthesis) → GitHub commit → index rebuild → SSM notify → Telegram confirmation.

Flat file library, not a vector database. Index is ~15k tokens at 500 entries. Human-readable, correctable by editing files.

## The Research Agent

Parallel AI Task API. Structured query construction → async task submission → backoff polling → report received → GitHub commit → Actions rebuild → SSM notify → Telegram confirmation.

Fixed per-task pricing ($0.005–$0.250 depending on tier), not per-token.

## Emergent Patterns

**Skills as operational memory.** Every solved problem → a reusable skill. Each session starts from a richer baseline.

**The bot's self-healing instinct.** It works a thread when something breaks. But it fixes the diagnosed target, not necessarily the actual code path in use.

**The working loop.** Error → feed to model → fix or diagnostic step → run → feed output back. Human driving, AI navigating when environment gets noisy.

## Bug Appendix

**Bug 1: SSM Plugin install.** Manual .pkg extraction required. ARM64 vs x86_64 matters.

**Bug 2: SSM + WebSockets.** SSM port forwarding drops persistent WebSocket connections. Control UI QR flow requires persistent WebSocket. Three hours lost.

**Bug 3: WhatsApp death spiral.** Health monitor restarts → stale credentials → Baileys retries → rate limit → repeat. Fix: stop service, delete credentials, pair fresh via terminal QR. Don't use WhatsApp for bots.

**Bug 4: Wrong Telegram config key.** `token` rejected, `botToken` required. Schema validator catches it but doesn't name the field.

**Bug 5: API key never reached the process.** .env file correct, .profile source present — but systemd doesn't source .profile. Fix: EnvironmentFile= in service unit. Verify via /proc/<pid>/environ.

**Bug 6: Voice memos silently ignored.** Gateway delivers a file path annotation. Model can't read audio. Every voice memo discarded since Telegram was connected.

**Bug 7: Wrong model was running.** Config change never deployed to EC2. Nova 2 Lite ran for days while Sonnet was assumed. Tell: workspace files progressively ignored as context grew. Fix: one sed command, restart.

**Bug 8: Bot diagnosed the wrong code path (the Sisyphus bug).** ingest-voice.sh sources lib/git.sh but never calls any of its functions. Inline git push on line ~229 had no retry logic. Bot fixed lib/git.sh correctly and repeatedly — the wrong file. Fix required human structural reading of the scripts. Race condition test (second local clone positioned 1 commit ahead) would have caught this immediately.

**Bug 9: IAM permission prefix mismatch.** ingest-voice.sh used openclaw-wiki-* job names. IAM policy allowed openclaw-voice-*. Silent failure at runtime, not at deploy.

**Bug 10 (implicit): fileb:// vs file://.** AWS CLI's --body file:// validates for ASCII. Prompt contained em-dashes. Fix: fileb:// passes raw bytes, skips ASCII check.

**Bug 11 (implicit): git pull --rebase syntax.** `git pull --rebase origin HEAD` is wrong syntax. Should be `git pull --rebase origin main`. Retry logic never executed despite being present.

**Bug 12: Research output rendering as raw JSON.** output_schema: { type: "auto" } returns JSON. output_schema: { type: "text" } returns readable markdown. One parameter, one week of broken reports.

**Bug 13: Speech-to-text errors propagating through the pipeline.** Lagos transcription error written to wiki. Fix: edit file, commit, done. Traceability only possible because memory is files, not vector embeddings.

## What's Next

- Knowledge base enrichment propagation (semantic cross-linking across wiki graph)
- Transcription upgrade to Whisper
- Structured self-improvement via GitHub issues → cloud agent → deployed changes
- Dedicated Q&A Telegram topic grounded in the full KB

---

## Additional Bug Details (from Ford, post-draft)

### Bug 9 (continued): IAM Prefix Mismatch
The fix is simple — align the prefix in the script to match the policy. Finding it requires knowing to look at the IAM policy at all.

### Bug 10: Non-ASCII Characters in AWS CLI Request
wiki-integrate.sh included em-dashes in the prompt template. AWS CLI's `--body file://` expects ASCII and rejects anything else. Fix: `fileb://` reads raw bytes, handles any encoding. Use fileb:// any time a request body might include typographic punctuation.

### Bug 11: GitHub Actions Multi-Line Output Parsing
grep -m1 on frontmatter worked until body content matched the pattern. Multi-line values written via `echo "summary=..." >> $GITHUB_OUTPUT` are truncated. Fix: Python frontmatter parser + heredoc delimiter syntax for multi-line GITHUB_OUTPUT values.

### Bug 12: Research Output as Raw JSON
Parallel AI's `output_schema: { type: "auto" }` returns structured JSON. `{ type: "text" }` returns readable markdown. One parameter change deleted an entire downstream reformatting pipeline stage and the bugs it contained.

### Bug 13: Speech-to-Text Errors Propagating
Transcribe heard "Lagos" instead of "Richmond." LLM pass treated transcript as ground truth. Seven files required correction. 

Governance response: all transcribed content is a draft. Human review before promotion to canonical pages. Corrections commit with provenance notes. Raw transcripts stay immutable — the error chain must always be traceable.
