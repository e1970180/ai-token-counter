# ai_token_counter/counter.py
"""
Main logic for counting tokens in text sources.

This module provides the public API function `count_tokens`, which reads
text from a file path, stdin, or file-like object, resolves the appropriate
tokenizer encoding, and returns the token count along with the encoding name.
"""

from typing import Optional, Tuple, Union, Mapping
from pathlib import Path
import sys

from .file_utils import read_source
from .tokenizer_factory import resolve_encoding_name
from .tokenizers.openai import count_tokens_tiktoken


def count_tokens(
    source: Union[str, Path, sys.stdin.__class__],
    model_alias: Optional[str] = None,
    encoding_name: Optional[str] = None,
    config: Optional[Mapping[str, str]] = None,
) -> Tuple[int, str]:
    """
    Count tokens in the given text source using the specified model alias or encoding.

    Purpose:
        Read text from `source`, determine the encoding (via explicit `encoding_name`
        or `model_alias`), count tokens, and return the count and the encoding used.

    Args:
        source (str | Path | TextIO): Path to file, '-' for stdin, or file-like object.
        model_alias (Optional[str]): Case-insensitive alias for the AI model.
        encoding_name (Optional[str]): Explicit name of the tiktoken encoding.
        config (Optional[Mapping[str, str]]): Override mapping for model aliases.

    Returns:
        Tuple[int, str]: (token_count, actual_encoding_name)

    Raises:
        ValueError: If neither `model_alias` nor `encoding_name` is provided.
        FileNotFoundError: If file path does not exist.
        IOError: On I/O errors reading the source.
        UnicodeDecodeError: If input is not valid UTF-8.
        TypeError: If `source` is of unsupported type.
    Side effects:
        None
    """
    # Проверка обязательных параметров перед чтением входа
    if model_alias is None and encoding_name is None:
        raise ValueError("One of `model_alias` or `encoding_name` must be specified.")

    # Чтение текста из файла, stdin или файла-объекта
    text = read_source(source)

    # Определение имени кодировки
    encoding = resolve_encoding_name(
        model_alias=model_alias, encoding_name=encoding_name, user_config=config
    )

    # Подсчёт токенов и возврат результата
    token_count = count_tokens_tiktoken(text=text, encoding_name=encoding)
    return token_count, encoding
