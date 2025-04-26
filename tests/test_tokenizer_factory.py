# tests/test_tokenizer_factory.py
"""
Tests for the tokenizer_factory module.
"""

import pytest
from ai_token_counter.tokenizer_factory import resolve_encoding_name


def test_resolve_alias_to_default_config():
    """Псевдоним модели из стандартного конфига корректно разрешается."""
    encoding = resolve_encoding_name(
        model_alias="gpt35", encoding_name=None, user_config=None
    )
    assert encoding == "cl100k_base"


def test_explicit_encoding_overrides_alias():
    """Явное encoding_name имеет приоритет над model_alias."""
    encoding = resolve_encoding_name(
        model_alias="gpt35", encoding_name="o200k_base", user_config=None
    )
    assert encoding == "o200k_base"


def test_unknown_alias_raises():
    """Неизвестный псевдоним модели вызывает ValueError."""
    with pytest.raises(ValueError):
        resolve_encoding_name(
            model_alias="unknown", encoding_name=None, user_config=None
        )


def test_user_config_override():
    """Пользовательский конфиг имеет приоритет над дефолтным."""
    custom = {"myalias": "custom_encoding"}
    encoding = resolve_encoding_name(
        model_alias="myalias", encoding_name=None, user_config=custom
    )
    assert encoding == "custom_encoding"
