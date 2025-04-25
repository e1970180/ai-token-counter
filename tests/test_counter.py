# tests/test_counter.py
"""
Tests for the counter module.
"""

import io
import pytest
from pathlib import Path
from ai_token_counter.counter import count_tokens


def test_count_tokens_file(tmp_path):
    """Проверить подсчёт токенов в файле по псевдониму модели."""
    content = "Hello world"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content, encoding="utf-8")

    count, encoding = count_tokens(source=str(file_path), model_alias="gpt35")
    assert isinstance(count, int)
    assert count == 2  # «Hello» и «world»
    assert encoding == "cl100k_base"


def test_count_tokens_stdin(tmp_path, monkeypatch):
    """Проверить чтение из stdin при source='-'."""
    content = "Test input"
    stdin = io.StringIO(content)
    monkeypatch.setattr("sys.stdin", stdin)

    count, encoding = count_tokens(source="-", encoding_name="cl100k_base")
    assert count == 2  # «Test» и «input»
    assert encoding == "cl100k_base"


def test_count_tokens_no_alias_and_no_encoding():
    """При отсутствии model_alias и encoding_name должен быть ValueError."""
    with pytest.raises(ValueError):
        count_tokens(source="does_not_matter", model_alias=None, encoding_name=None)
