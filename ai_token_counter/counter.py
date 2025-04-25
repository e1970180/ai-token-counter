'''
Module: counter.py

Purpose:
    Provide API for token counting: read source, resolve encoding, count tokens, return result.

This module offers a unified function for both CLI and importable API use.
'''

from pathlib import Path
from typing import Optional, Tuple, Mapping, Union, TextIO

from .file_utils import read_source
from .tokenizer_factory import resolve_encoding_name, get_tiktoken_encoder
from .tokenizer_config import TOKENIZER_CONFIG


def count_tokens(
    source: Union[str, Path, TextIO],
    model_alias: Optional[str] = None,
    encoding_name: Optional[str] = None,
    user_config: Optional[Mapping[str, str]] = None,
) -> Tuple[int, str]:
    """
    Count tokens from a text source and return both count and used encoding.

    Args:
        source: Path to text file, '-' for stdin, or TextIO object.
        model_alias: Optional model alias to resolve encoding if encoding_name is None.
        encoding_name: Optional explicit encoding name to use (overrides alias).
        user_config: Optional mapping for custom alias-to-encoding overrides.

    Returns:
        A tuple of (token_count, resolved_encoding_name).

    Raises:
        ValueError: If neither model_alias nor encoding_name is provided, or alias unknown.
        FileNotFoundError: If file path does not exist.
        IOError: For I/O errors reading source.
        UnicodeDecodeError: If text read is not valid UTF-8.
    Side effects:
        Reads sys.stdin if source is '-'.
    Assumptions:
        Source text is UTF-8 encoded. user_config keys are lowercase.
    """
    # Read text content from provided source
    text = read_source(source)

    # Determine encoding name (explicit override or alias mapping)
    resolved_name = resolve_encoding_name(
        model_alias=model_alias,
        encoding_name=encoding_name,
        user_config=user_config,
    )

    # Count tokens using tiktoken encoder
    encoder = get_tiktoken_encoder(
        model_alias=model_alias,
        encoding_name=encoding_name,
        user_config=user_config,
    )
    token_ids = encoder.encode(text)
    count = len(token_ids)

    return count, resolved_name


# Example usage for module import
if __name__ == "__main__":
    import sys
    from .cli import parse_arguments

    args = parse_arguments()
    count, encoding = count_tokens(
        source=args.file,
        model_alias=args.model,
        encoding_name=None,
    )
    print(count)
