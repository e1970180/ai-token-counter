"""
Module: file_utils.py

Purpose:
    Read all text content from a given source: file path, standard input, or IO object.

Provides a unified interface for CLI and API consumers to load input text.
"""

import sys
from pathlib import Path
from typing import Union, TextIO


def read_source(source: Union[str, Path, TextIO]) -> str:
    """
    Read text from a file path, standard input indicator, or file-like object.

    Args:
        source: Path to a text file, '-' to read from sys.stdin, or a TextIO object.

    Returns:
        The full text content as a string.

    Raises:
        FileNotFoundError: If the provided file path does not exist.
        IOError: For IO-related errors when reading a file.
        UnicodeDecodeError: If the file content cannot be decoded as UTF-8.
        TypeError: If the source type is not supported.
    Side effects:
        May consume sys.stdin if source is '-'.
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
        except FileNotFoundError:
            raise
        except UnicodeDecodeError:
            raise
        except Exception as e:
            # Propagate as generic IOError
            raise IOError(f"Error reading file '{src}': {e}")

    # Handle file-like object
    if hasattr(source, "read"):
        try:
            return source.read()
        except Exception as e:
            raise IOError(f"Error reading from TextIO object: {e}")

    # Unsupported source type
    raise TypeError(f"Unsupported source type: {type(source)}")
