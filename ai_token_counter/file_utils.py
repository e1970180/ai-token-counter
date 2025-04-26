"""
Module: file_utils.py

Purpose:
    Provides the `read_source` function to load text from a file path,
    standard input (`'-'`), or any file-like object.

Provides a unified interface for CLI and API consumers to load input text.
"""

import sys
from pathlib import Path
from typing import Union, TextIO


def read_source(source: Union[str, Path, TextIO]) -> str:
    """
    Read text from a file path, standard input indicator, or file-like object.

    Args:
        source (str | Path | TextIO): Path to file, '-' to read from stdin,
        or an open TextIO object.

    Returns:
        str: The full text content as a string.

    Raises:
        FileNotFoundError: If the file path does not exist.
        IOError: On other I/O failures reading file or TextIO.
        UnicodeDecodeError: If the file content cannot be decoded as UTF-8.
        TypeError: If the source type is not supported.
    Side effects:
        ?May consume sys.stdin if source is '-'.
    Assumptions:
        Input files are encoded in UTF-8. TextIO objects provide text mode.
    """
    # Handle file path or stdin indicator
    if isinstance(source, (str, Path)):
        src = str(source)
        if src == "-":
            # Read from standard input
            return sys.stdin.read()
        # Read from file system
        path = Path(src)
        try:
            # Read text in UTF-8
            return path.read_text(encoding="utf-8")
        except FileNotFoundError as e:
            # File not found
            raise FileNotFoundError(f"File not found: {src}") from e
        except UnicodeDecodeError as e:
            # Invalid UTF-8 in file
            raise UnicodeDecodeError(
                e.encoding, e.object, e.start, e.end, f"Invalid UTF-8 in file '{src}'"
            ) from e
        except IOError as e:
            # Other I/O errors
            raise IOError(f"Error reading file '{src}': {e}") from e

    # Handle file-like object
    if hasattr(source, "read"):
        try:
            return source.read()
        except Exception as e:
            raise IOError(f"Error reading from TextIO object: {e}") from e

    # Unsupported source type
    raise TypeError(f"Unsupported source type: {type(source)}")
