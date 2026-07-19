# 02 — Tokenization Deep Dive: why the same sentence isn't the same number of tokens

This is the part most comparisons skip, and it's where a lot of "interesting" research actually
lives. Two models can read the exact same English sentence and disagree on how many tokens it costs —
and that difference is entirely about *tokenizer design*, not intelligence.

## What a tokenizer actually does

An LLM doesn't read letters or words. It reads integers. A tokenizer is the fixed lookup table (plus
a merge algorithm) that turns text into a sequence of integers, and back again. Every model is trained
against one specific tokenizer — you cannot swap tokenizers after training without retraining the
model.

Three families dominate:

### 1. Byte-Pair Encoding (BPE) — GPT family, Llama, Mistral
Starts from individual bytes/characters, then iteratively merges the most frequent adjacent pair into
a new token, repeating until it hits a target vocabulary size (commonly 32K–128K+ tokens). Common
words end up as single tokens; rare words get split into subword chunks. OpenAI's implementation is
called **tiktoken** and is the fastest publicly available production BPE implementation.

### 2. SentencePiece (BPE or Unigram mode) — Llama, Mistral, Qwen, Gemma
Treats the input as a raw stream (no assumption that whitespace separates words — important for
Chinese, Japanese, Thai, etc.) and can run either BPE-style merging or a probabilistic "Unigram"
model that picks the most likely segmentation. This is why SentencePiece-based tokenizers tend to
handle non-English text more gracefully than pure whitespace-aware BPE.

### 3. Byte-level BPE variants — Claude, Gemini
Anthropic and Google don't publish exact tokenizer specs, but both use byte-level BPE-style schemes
tuned on their own training mixes. The practical effect: token counts for the same text will differ
from OpenAI's tiktoken counts, sometimes significantly.

## Why this matters in practice

- **Cost:** API pricing is per-token. If Model A tokenizes a paragraph into 500 tokens and Model B
  tokenizes the *same* paragraph into 650 tokens, Model B costs 30% more for identical input — even
  at an identical per-token rate.
- **Effective context window:** A "1M-token context window" holds different amounts of *actual text*
  depending on the tokenizer. A verbose tokenizer eats into your budget faster.
- **A real, current example:** as of mid-2026, Anthropic's newer tokenizer (introduced around Claude
  Opus 4.7) can produce up to ~35% more tokens for the same text than pre-4.7 Claude models. That's a
  meaningful swing to be aware of if you're comparing Claude generations on cost, not just capability.
- **Non-English text:** languages without whitespace word boundaries (Chinese, Japanese, Thai, etc.)
  or with rich morphology (Arabic, Urdu, Finnish) tend to tokenize *less* efficiently on
  English-optimized vocabularies — the same sentence can cost 2–3x more tokens than an equivalent
  English sentence on some tokenizers. This is a genuinely underexplored angle for a portfolio
  project: **since you work with Urdu/English bilingual text (e.g. Hifazat), tokenizer efficiency on
  Urdu specifically is a great original experiment** — run the same Urdu paragraph through several
  tokenizers and compare token counts. Nobody's benchmark table covers this; you'd be generating new
  data, not repeating someone else's.

## Vocabulary size, roughly, by family

| Family | Tokenizer type | Typical vocab size |
|---|---|---|
| GPT (tiktoken, `o200k_base`-era) | Byte-level BPE | ~200K |
| Llama 3/4 | SentencePiece BPE | ~128K |
| Mistral | SentencePiece BPE (Tekken tokenizer in newer models) | ~130K–150K |
| Qwen | Byte-level BPE | ~150K |
| Claude | Proprietary byte-level BPE | not published; changed materially at Opus 4.7 |
| Gemini | SentencePiece-derived | not fully published |

(Exact current numbers shift release-to-release — treat this table as "the right order of magnitude,"
and verify against the current tokenizer file if you need an exact count for a paper or report.)

## How to actually measure this yourself (not just read about it)

Don't take vendor claims at face value — measure it. `code/tokenizer_comparison.py` in this repo runs
the *same* text block through:
- `tiktoken` (OpenAI's real tokenizer, works offline once cached)
- Hugging Face `AutoTokenizer` for any open model (Llama, Mistral, Qwen — these are the real trained
  tokenizers, not approximations)

and prints a side-by-side token count table. Claude and Gemini don't publish downloadable tokenizer
files, so for those two the practical workaround is: call each API with `count_tokens` (Anthropic
exposes a token-counting endpoint) or compare the `usage` field returned in a normal API response.

## Suggested original experiments (things not already in a blog post somewhere)

1. **Urdu/English code-switching cost** — since you write bilingual text often, measure token cost for
   a paragraph that mixes Urdu script, Roman Urdu, and English mid-sentence. Tokenizers handle
   code-switching very differently.
2. **Token efficiency vs. compression** — pick a fixed 500-word technical paragraph (e.g. from your
   DDoS detection writeup) and rank every tokenizer by tokens-per-word. This gives you a genuinely
   reusable "cost multiplier" table for budgeting API costs across providers.
3. **Degenerate cases** — try tokenizing: a long run of emoji, a URL, a code snippet with heavy
   symbols, and a markdown table. BPE-style tokenizers behave very unevenly outside natural-language
   prose — a good demonstration of where "context window" specs can be misleading for code-heavy or
   symbol-heavy prompts.
