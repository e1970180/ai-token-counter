"""
ai_token_counter.tokenizers.openai module.

Purpose:
    Provides token counting functionality for OpenAI-compatible models
    using the tiktoken library.

Dependencies:
    tiktoken

Example:
    >>> from ai_token_counter.tokenizers.openai import count_tokens_tiktoken
    >>> count_tokens_tiktoken("Hello world", "cl100k_base")
    2
"""

import tiktoken
from tiktoken import Encoding


def count_tokens_tiktoken(
    text: str,
    encoding_name: str
) -> int:
    """
    Count the number of tokens in a text using a tiktoken encoding.

    Purpose:
        Encode the provided text using the specified tiktoken encoding
        and return the count of resulting tokens.

    Args:
        text (str): The input text to tokenize.
        encoding_name (str): Name of the tiktoken encoding (e.g., 'cl100k_base').

    Returns:
        int: The number of tokens produced by encoding the text.

    Raises:
        KeyError: If the specified encoding_name is not recognized by tiktoken.
        Exception: Propagates exceptions from the tiktoken library.

    Side effects:
        None

    Assumptions:
        The input text is a UTF-8 encoded Python string.
    """
    # Получить объект кодировщика по имени кодировки
    encoder: Encoding = tiktoken.get_encoding(encoding_name)
    # Закодировать текст в список идентификаторов токенов
    token_ids: list[int] = encoder.encode(text)
    return len(token_ids)
	
