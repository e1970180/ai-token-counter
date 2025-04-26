"""
Module: __main__.py

Purpose:
    Package entry point for ai_token_counter,
    enabling execution via `python -m ai_token_counter`.
    Delegates CLI parsing and token counting.
"""

import sys

from .cli import parse_arguments
from .counter import count_tokens


def main() -> None:
    """
    Main entry point: parse arguments, perform token count, and output result or error.

    Side effects:
        Writes to stdout or stderr, exits on error.
    """
    args = parse_arguments()
    try:
        count, _ = count_tokens(
            source=args.file,
            model_alias=args.model,
            encoding_name=args.encoding,
        )
        print(count)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
