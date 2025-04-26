"""
Module: __main__.py

Purpose:
    Package entry point for ai_token_counter,
    enabling execution via `python -m ai_token_counter`.
    Delegates CLI parsing and token counting.
"""

import sys

from ai_token_counter.cli import parse_arguments
from ai_token_counter.counter import count_tokens


def main() -> None:
    """
    Execute the token counting flow with targeted exception handling.

        Args:
            None

        Returns:
            None

        Raises:
            None: unexpected exceptions will propagate and display a full traceback.

        Side effects:
            Prints the token count to stdout on success, or an error message to stderr
            with exit code 1 on known failures.
    """
    args = parse_arguments()
    try:
        count, _ = count_tokens(
            source=args.file,
            model_alias=args.model,
            encoding_name=args.encoding,
        )
    except (ValueError, FileNotFoundError, UnicodeError, IOError, TypeError) as err:
        # Handle only anticipated error types and exit cleanly
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)
    else:
        # On success, output only the token count
        print(count)


if __name__ == "__main__":
    main()
