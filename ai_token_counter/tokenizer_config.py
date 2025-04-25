'''
Module: tokenizer_config.py

Purpose:
    Central storage for mapping AI model aliases to tiktoken encoding names.

This configuration enables easy extension and override of model-to-encoding mappings.
'''

# Default mapping of model aliases (case-insensitive) to tiktoken encoding names
# Keys: model alias in lowercase; Values: corresponding tiktoken encoding name
TOKENIZER_CONFIG: dict[str, str] = {
    # OpenAI GPT-3.5 and GPT-4 families
    "gpt-3.5-turbo": "cl100k_base",  # primary alias for GPT-3.5-Turbo
    "gpt35": "cl100k_base",         # shorthand alias
    "gpt-4": "cl100k_base",         # GPT-4 uses same encoding as GPT-3.5
    "gpt4": "cl100k_base",          # shorthand alias

    # GPT-4o (omni) for overheard / multimodal
    "gpt4o": "o200k_base",          # alias for GPT-4o requiring larger token space
    "gpt-4o": "o200k_base",         # hyphenated alias

    # Direct encoding names
    "cl100k_base": "cl100k_base",   # direct reference
    "o200k_base": "o200k_base",     # direct reference
}

# TODO: Merge with user-provided config in tokenizer_factory to allow overrides
