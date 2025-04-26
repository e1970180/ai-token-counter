"""
ai_token_counter.tokenizer_factory module.

Purpose:
    Resolve tiktoken encoding names from model aliases or explicit encoding names,
    and provide factory functions for tiktoken encoders.

Dependencies:
    tiktoken
    typing.Mapping, typing.Optional
    ai_token_counter.tokenizer_config.TOKENIZER_CONFIG
"""

from typing import Mapping, Optional
import tiktoken
from tiktoken import Encoding

from ai_token_counter.tokenizer_config import TOKENIZER_CONFIG


def merge_configs(
    default: Mapping[str, str], user: Optional[Mapping[str, str]]
) -> dict[str, str]:
    """
    Merge default tokenizer config with user-provided overrides.

    Purpose:
        Produce a combined alias-to-encoding mapping, where user overrides
        take precedence over defaults.

    Args:
        default (Mapping[str, str]): Base mapping of model alias to encoding name.
        user (Optional[Mapping[str, str]]): Optional user-provided overrides.

    Returns:
        dict[str, str]: Merged mapping with lowercase keys.
    """
    merged = {alias.lower(): encoding for alias, encoding in default.items()}
    if user:
        for alias, encoding in user.items():
            merged[alias.lower()] = encoding
    return merged


def resolve_encoding_name(
    model_alias: Optional[str] = None,
    encoding_name: Optional[str] = None,
    user_config: Optional[Mapping[str, str]] = None,
) -> str:
    """
    Determine the tiktoken encoding name based on model alias or explicit encoding.

    Purpose:
        Use explicit encoding_name if provided; otherwise map model_alias
        via merged default and user configuration.

    Args:
        model_alias (Optional[str]): Case-insensitive alias for the AI model.
        encoding_name (Optional[str]): Explicit tiktoken encoding name.
        user_config (Optional[Mapping[str, str]]): User-provided alias->encoding mapping.

    Returns:
        str: The resolved encoding name.

    Raises:
        ValueError: If neither model_alias nor encoding_name is specified,
                    or if model_alias is not found in the configuration.
    """
    # Explicit encoding overrides alias
    if encoding_name:
        return encoding_name

    if not model_alias:
        raise ValueError("One of `model_alias` or `encoding_name` must be specified.")

    config = merge_configs(TOKENIZER_CONFIG, user_config)
    alias_lower = model_alias.lower()
    try:
        return config[alias_lower]
    except KeyError as e:
        raise ValueError(f"Unknown model alias: {model_alias}") from e


def get_tiktoken_encoder(encoding_name: str) -> Encoding:
    """
    Retrieve a tiktoken Encoding instance for the given encoding name.

    Purpose:
        Wrap tiktoken.get_encoding, adding context to errors.

    Args:
        encoding_name (str): Name of the tiktoken encoding (e.g., 'cl100k_base').

    Returns:
        Encoding: The tiktoken encoder object.

    Raises:
        ValueError: If the encoding_name is not recognized by tiktoken.
    """
    try:
        return tiktoken.get_encoding(encoding_name)
    except KeyError as e:
        raise ValueError(
            f"Failed to load tiktoken encoding '{encoding_name}': {e}"
        ) from e
    except Exception as e:
        raise ValueError(
            f"Failed to load tiktoken encoding '{encoding_name}': {e}"
        ) from e
