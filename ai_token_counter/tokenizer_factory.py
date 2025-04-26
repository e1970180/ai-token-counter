"""
Module: tokenizer_factory.py

Purpose:
    Resolve model alias or encoding name into a tiktoken encoding instance.
    Allows merging default and user-provided mappings.
"""

from typing import Mapping, Optional

import tiktoken
from ai_token_counter.tokenizer_config import TOKENIZER_CONFIG


def resolve_encoding_name(
    model_alias: Optional[str] = None,
    encoding_name: Optional[str] = None,
    user_config: Optional[Mapping[str, str]] = None,
) -> str:
    """
    Determine the tiktoken encoding name based on model alias or explicit encoding.

    Args:
        model_alias: AI model alias (case-insensitive). Priority if encoding_name is None.
        encoding_name: Explicit tiktoken encoding name (overrides model_alias mapping).
        user_config: Optional mapping of aliases to encoding names to override defaults.

    Returns:
        The resolved tiktoken encoding name.

    Raises:
        ValueError: If neither encoding_name nor model_alias is provided,
            or if model_alias is unknown in the merged configuration.
    Side effects:
        None
    Assumptions:
        Default TOKENIZER_CONFIG keys are lowercase. user_config keys should be lowercase.
    """
    # Merge default and user-provided mappings (user overrides defaults)
    merged = dict(TOKENIZER_CONFIG)
    if user_config:
        merged.update({k.lower(): v for k, v in user_config.items()})

    # Explicit encoding_name has highest priority
    if encoding_name:
        return encoding_name

    # Require model_alias if encoding_name is not given
    if not model_alias:
        raise ValueError("Either model_alias or encoding_name must be provided.")

    alias_key = model_alias.lower()
    if alias_key not in merged:
        raise ValueError(f"Unknown model alias: '{model_alias}'.")

    return merged[alias_key]


def get_tiktoken_encoder(
    model_alias: Optional[str] = None,
    encoding_name: Optional[str] = None,
    user_config: Optional[Mapping[str, str]] = None,
) -> tiktoken.Encoding:
    """
    Obtain a tiktoken.Encoding instance for tokenization.

    Args:
        model_alias: AI model alias to resolve encoding name if encoding_name is None.
        encoding_name: Explicit encoding name to load.
        user_config: Optional overrides for alias-to-encoding mapping.

    Returns:
        A tiktoken.Encoding object corresponding to the resolved encoding name.

    Raises:
        ValueError: If resolution fails or tiktoken cannot load the encoding.
    Side effects:
        May raise errors from tiktoken.get_encoding if encoding is invalid.
    """
    name = resolve_encoding_name(model_alias, encoding_name, user_config)
    # Load encoder from tiktoken
    try:
        encoder = tiktoken.get_encoding(name)
    except Exception as e:
        raise ValueError(f"Failed to load tiktoken encoding '{name}': {e}")

    return encoder
