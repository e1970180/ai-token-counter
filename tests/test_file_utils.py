# tests/test_file_utils.py
"""
Tests for the file_utils module.
"""

import io
import pytest
from ai_token_counter.file_utils import read_source


def test_read_source_from_path(tmp_path):
    """Чтение текста из файла по пути."""
    file_path = tmp_path / "data.txt"
    text = "Sample data"
    file_path.write_text(text, encoding="utf-8")

    result = read_source(str(file_path))
    assert result == text


def test_read_source_from_file_object():
    """Чтение текста из объекта TextIO."""
    stream = io.StringIO("Stream data")
    result = read_source(stream)
    assert result == "Stream data"


def test_read_source_invalid_type():
    """Передача неподдерживаемого типа source вызывает TypeError."""
    with pytest.raises(TypeError):
        read_source(12345)
