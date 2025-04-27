"""
tests/test_tokenizer_factory_errors.py

Purpose:
    Unit tests for error handling in ai_token_counter.tokenizer_factory.
Dependencies:
    pytest
"""

import pytest
from ai_token_counter.tokenizer_factory import (
    merge_configs,
    resolve_encoding_name,
    get_tiktoken_encoder,
)
from ai_token_counter.tokenizer_config import TOKENIZER_CONFIG


def test_merge_configs_override():
    """
    merge_configs должен переопределять дефолтные значения пользовательскими.
    """
    default = {"a": "enc1", "b": "enc2"}
    user = {"B": "custom", "C": "enc3"}
    merged = merge_configs(default, user)
    assert merged["a"] == "enc1", "Default для 'a' не должен меняться"
    assert (
        merged["b"] == "custom"
    ), "Пользовательский override для 'b' должен применяться"
    assert merged["c"] == "enc3", "Новый ключ 'c' должен добавляться из user_config"


def test_resolve_no_params_raises_value_error():
    """
    resolve_encoding_name должен бросать ValueError, если оба параметра None.
    """
    with pytest.raises(ValueError):
        resolve_encoding_name(None, None, None)


def test_resolve_explicit_encoding():
    """
    resolve_encoding_name возвращает explicit encoding_name, игнорируя alias.
    """
    result = resolve_encoding_name("unknown", "cl100k_base", None)
    assert result == "cl100k_base"


def test_resolve_unknown_alias():
    """
    resolve_encoding_name должен бросать ValueError для неизвестного alias.
    """
    with pytest.raises(ValueError) as excinfo:
        resolve_encoding_name("nonexistent", None, None)
    assert "Unknown model alias" in str(excinfo.value)


def test_get_tiktoken_encoder_invalid():
    """
    get_tiktoken_encoder должен бросать ValueError для несуществующего encoding_name.
    """
    with pytest.raises(ValueError) as excinfo:
        get_tiktoken_encoder("invalid_encoding_name")
    assert "Failed to load tiktoken encoding" in str(excinfo.value)
