"""
tokenizer_comparison.py

Runs the same block(s) of text through several REAL, publicly downloadable tokenizers
and prints a side-by-side comparison of token counts.

This is meant to be run on YOUR machine (not in a sandboxed/offline environment) because
tiktoken and Hugging Face tokenizers need to download their vocab/merge files on first use.

Setup:
    pip install tiktoken transformers sentencepiece

Some Hugging Face tokenizers (e.g. Llama, Mistral) are "gated" and require you to:
    1. Create a free account at https://huggingface.co
    2. Accept the model license on the model's page (e.g. meta-llama/Llama-4-Scout-...)
    3. Run `huggingface-cli login` once with an access token

Claude and Gemini do not publish downloadable tokenizer files, so they are NOT included here.
To measure their token counts, use:
    - Anthropic's token counting endpoint (client.messages.count_tokens(...))
    - The `usageMetadata.promptTokenCount` field in a Gemini API response

Usage:
    python tokenizer_comparison.py
"""

from __future__ import annotations
import sys

# 1. Define the text samples you want to compare.
#    Add your own here -- e.g. an Urdu/English code-switched paragraph is a
#    genuinely interesting, under-explored comparison.

SAMPLES = {
    "english_prose": (
        "The quick brown fox jumps over the lazy dog. Large language models "
        "process text as sequences of tokens, not characters or words."
    ),
    "urdu_english_mixed": (
        "Mujhe lagta hai ke yeh model kaafi accha perform kar raha hai, "
        "lekin ہمیں tokenization ke effects samajhna zaroori hai۔"
    ),
    "code_snippet": (
        "def tokenize(text: str) -> list[int]:\n"
        "    return [ord(c) for c in text if not c.isspace()]\n"
    ),
    "url_and_symbols": (
        "Check https://example.com/path?query=1&other=2 for details -- "
        "cost was $19.99 (+15% tax) => total ~$22.99!!"
    ),
}


def count_tiktoken(text: str, encoding_name: str = "o200k_base") -> int | None:
    """Token count using OpenAI's tiktoken (used by GPT-4o/GPT-5.x family)."""
    try:
        import tiktoken
    except ImportError:
        print("  [skip] pip install tiktoken", file=sys.stderr)
        return None
    try:
        enc = tiktoken.get_encoding(encoding_name)
        return len(enc.encode(text))
    except Exception as e:  # first-run download blocked/offline, etc.
        print(f"  [skip] tiktoken '{encoding_name}' unavailable: {e}", file=sys.stderr)
        return None


def count_hf_tokenizer(text: str, model_id: str) -> int | None:
    """Token count using a real Hugging Face AutoTokenizer for an open model."""
    try:
        from transformers import AutoTokenizer
    except ImportError:
        print("  [skip] pip install transformers", file=sys.stderr)
        return None
    try:
        tok = AutoTokenizer.from_pretrained(model_id)
    except Exception as e:  # gated repo, no internet, etc.
        print(f"  [skip] could not load {model_id}: {e}", file=sys.stderr)
        return None
    return len(tok.encode(text))


# Map of "friendly name" -> (loader function, argument)
# Add/remove rows here as you get access to more tokenizers.

TOKENIZERS = {
    "GPT (tiktoken o200k_base)": lambda t: count_tiktoken(t, "o200k_base"),
    "GPT (tiktoken cl100k_base, legacy)": lambda t: count_tiktoken(t, "cl100k_base"),
    "Llama 3/4 family": lambda t: count_hf_tokenizer(t, "meta-llama/Meta-Llama-3-8B"),
    "Mistral family": lambda t: count_hf_tokenizer(t, "mistralai/Mistral-7B-v0.1"),
    "Qwen family": lambda t: count_hf_tokenizer(t, "Qwen/Qwen2.5-7B"),
}


def main() -> None:
    col_width = 34
    for sample_name, text in SAMPLES.items():
        print(f"\n=== Sample: {sample_name} ===")
        print(f'"{text[:80]}{"..." if len(text) > 80 else ""}"')
        print("-" * (col_width + 12))
        results = {}
        for name, fn in TOKENIZERS.items():
            count = fn(text)
            results[name] = count
            display = str(count) if count is not None else "n/a"
            print(f"{name:<{col_width}} {display}")

        # Simple tokens-per-word ratio, useful for quick cost comparisons
        n_words = len(text.split())
        print(f"\n(word count for reference: {n_words})")
        for name, count in results.items():
            if count:
                print(f"  {name}: {count / n_words:.2f} tokens/word")


if __name__ == "__main__":
    main()
