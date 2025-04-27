import pytest
from ai_token_counter.file_utils import read_source


def test_file_not_found():
    """Reading a nonexistent file should raise FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_source("no_such_file.txt")


def test_invalid_utf8(tmp_path):
    """Reading a file with invalid UTF-8 should raise UnicodeDecodeError."""
    bad_file = tmp_path / "bad.txt"
    bad_file.write_bytes(b"\xff\xfe\xfa")
    with pytest.raises(UnicodeDecodeError):
        read_source(str(bad_file))


def test_unsupported_type():
    """Passing an unsupported type should raise TypeError."""
    with pytest.raises(TypeError):
        read_source(123)  # type: ignore


def test_textio_io_error():
    """Error during read() of a TextIO object should raise IOError."""

    class BadReader:
        def read(self):
            raise RuntimeError("fail")

    with pytest.raises(IOError):
        read_source(BadReader())  # type: ignore
