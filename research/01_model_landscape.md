# 01 The Model Landscape (last verified: July 2026)

A field guide to every major LLM family currently in production use, grouped by lab. For each: who
builds it, how it's built (architecture), how big it is, how it's licensed, and what it's for.

---

## 1. OpenAI GPT family

**Current flagship:** GPT-5.6, shipped as three sizes from one family **Sol** (largest, flagship
reasoning/coding), **Terra** (balanced cost/intelligence), **Luna** (cheapest, high-volume). All three
share a knowledge cutoff and a ~1M-token context window, with reasoning effort selectable from `none`
up through `low/medium/high/xhigh/max` you pay more compute for deeper reasoning on the same model.

- **Architecture:** dense/MoE transformer (OpenAI doesn't publish exact parameter counts or MoE
  routing details for GPT-5.x)
- **Access:** closed weights, API + ChatGPT/Codex only
- **Notable:** GPT-5.6 also powers "ChatGPT Work," an agentic workspace product; the model line added
  native computer use and 1M context starting with GPT-5.5
- **License:** proprietary; the older **GPT-OSS** line is OpenAI's one open-weight offering, aimed at
  self-hosted/data-sovereignty use cases

## 2. Anthropic Claude family

**Current lineup:** **Claude Sonnet 5** (balanced, this is what's answering you right now), **Claude
Opus 4.8** (highest capability), **Claude Haiku 4.5** (fast/cheap), and the new **Mythos-tier**
models **Claude Mythos 5** and **Claude Fable 5** (same underlying model; Fable 5 has extra safety
gating on biology/cyber/LLM-R&D topics). Mythos Preview itself is restricted to a small set of trusted
orgs under Anthropic's "Project Glasswing."

- **Architecture:** dense transformer, details not public
- **Context window:** up to 1M tokens on Opus 4.8-and-later and the Mythos-tier models; a new tokenizer
  introduced around Opus 4.7 can produce meaningfully more tokens for the same text than older Claude
  models worth accounting for when comparing costs across Claude versions
- **Access:** closed weights, via API/Claude Platform, claude.ai, Claude Code, Claude Cowork, and
  Chrome/Excel/PowerPoint agent integrations
- **License:** proprietary

## 3. Google Gemini family

**Current lineup:** **Gemini 3.1 Pro** (flagship reasoning, 1M context, four thinking levels),
**Gemini 3.5 Flash** (newer, optimized for agentic/coding work, beats 3.1 Pro on some coding
benchmarks at lower cost), **Gemini 3.1 Flash-Lite** (budget tier), and **Gemini 3.1 Deep Think**
(extended-reasoning variant for research-grade problems).

- **Architecture:** natively multimodal transformer (text, image, audio, video in one model)
- **Context window:** 1M tokens standard on 3.1 Pro/3.5 Flash; pricing roughly doubles past 200K
  input tokens on the Pro tier
- **Access:** Google AI Studio / Vertex AI API, Gemini app, Google Workspace bundling
- **License:** proprietary

## 4. Meta Llama family

**Current lineup:** **Llama 4 Scout** (17B active / 109B total params, MoE, 16 experts, headline
**10M-token context window** the largest of any open-weight model), **Llama 4 Maverick** (400B
total / 17B active, stronger benchmarks, still huge context), and **Llama 4 Behemoth** (Meta's
largest model, used internally as a teacher model to distill Scout/Maverick never publicly
released).

- **Architecture:** Meta's first Mixture-of-Experts generation; natively multimodal, trained on ~200
  languages
- **Context window:** 10M tokens (Scout) but independent testing shows effective recall degrades
  well before the advertised limit, so it's most reliable for retrieval-style lookups in huge
  documents rather than synthesizing the entire window at once
- **Access:** open weights (downloadable, self-hostable via Ollama/vLLM/etc.) or hosted via cloud
  partners (AWS, NVIDIA, Databricks, Google Cloud)
- **License:** Meta's custom license — permissive but with a monthly-active-user cap and EU
  restrictions for very large operators
- **Reception note:** Llama 4 landed to a mixed reception; several original Llama researchers have
  since left Meta, and Meta's own leadership has publicly acknowledged the release underdelivered in
  places — worth knowing if you cite it as an unqualified "best open model"

## 5. Mistral AI

**Current lineup:** **Mistral Large 3** (flagship, now Apache 2.0), **Mistral Medium 3.5**
(multimodal/agentic), **Mistral Small 4** (efficient, includes Devstral-style agentic coding in a
small active-parameter footprint).

- **Architecture:** dense + efficient MoE variants depending on size
- **License:** now Apache 2.0 across the open lineup a meaningful shift from Mistral's earlier,
  more restrictive licensing
- **Positioning:** the default "European / open enterprise" pick relevant if EU data residency or
  non-US jurisdiction matters for a project
- **Multilingual:** Mistral Large 3 covers 80+ languages

## 6. xAI Grok family

**Current flagship:** **Grok 4.3** tends to lead pure reasoning benchmarks (logic, hard science,
math-heavy work).

- **Access:** the strongest capability tier sits behind the SuperGrok Heavy subscription; the API
  context window (128K) is notably smaller than the 1M offered by most 2026-era peers
- **License:** proprietary

## 7. DeepSeek

**Current lineup:** **DeepSeek V4 Pro** (frontier-adjacent quality, leads on competitive coding among
open-weight models) and **DeepSeek V4 Flash** (extremely cheap among the lowest per-token API
pricing in the entire market, ~$0.14/M input).

- **License:** MIT fully open, including for commercial and air-gapped/compliance-sensitive
  deployments
- **Positioning:** the "frontier-quality-at-a-fraction-of-the-cost" open-weight option; a serious pick
  wherever budget or self-hosting matters more than having the single highest benchmark score

## 8. Alibaba Qwen family

**Current lineup:** **Qwen 3.5 / Qwen 3.7 Max** (broad multilingual coverage 200+ languages/dialects,
the widest of any model family surveyed here), **Qwen3-Coder-Next** (small, 80B-total/3B-active,
Apache 2.0, built specifically for efficient self-hosted coding agents).

- **License:** open weights for most of the line (Apache 2.0 on the Coder variant); the flagship
  Max tier has moved to closed/API-only access
- **Positioning:** best pick when multilingual coverage (especially Chinese-language markets) or
  multimodal (vision/audio) support is the priority

## 9. Other open-weight names worth knowing

- **Kimi K2.6** (Moonshot AI) native multimodal (text/image/video), 256K context, strong agentic
  tool-use claims
- **GLM-5.2** (Z.ai) long-horizon coding focus, 1M context
- **MiniMax M3** competitive on SWE-bench-style coding benchmarks at low cost
- **Xiaomi MiMo** the edge-deployment specialist; small enough (down to ~3.5GB at INT4) to run on
  phones and embedded NPUs, which none of the flagship families target

---

## Quick-reference: how to think about "closed" vs "open" here

| | Closed (GPT, Claude, Gemini, Grok) | Open-weight (Llama, Mistral, DeepSeek, Qwen, Kimi, GLM, MiMo) |
|---|---|---|
| Access | API/app only, usage-based billing | Download + self-host, or hosted API from any provider |
| Data residency | Vendor's infrastructure | Your infrastructure  relevant for compliance-heavy work |
| Cost model | Per-token, can be high at frontier tier | Often per-token *or* hardware-only if self-hosted |
| Typical strength | Highest ceiling on hardest reasoning/agentic benchmarks | Best cost-to-capability ratio; catching up fast |
| Fine-tuning | Usually not possible (or very limited) | Fully fine-tunable |

The practical 2026 pattern most teams land on: **a closed frontier model for the hardest tasks, a
cheap open-weight API for high-volume work, and a self-hosted small model for privacy-sensitive or
offline cases** a portfolio, not a single winner.

---

### Sources
- OpenAI API model docs and release notes (developers.openai.com, releasebot.io)
- Anthropic model/product documentation
- Google Gemini pricing and model pages (eesel.ai, felloai.com, techjacksolutions.com, cloud.google.com)
- Meta Llama 4 guides (explainx.ai, ajianaz.dev, remoteopenclaw.com, Ars Technica)
- Open-weight landscape roundups (aimlapi.com, kingy.ai, computingforgeeks.com, localaimaster.com,
  theairankings.com, xiaomi-mimo-ai.com)
- Context window comparison tables (morphllm.com, digitalapplied.com)
