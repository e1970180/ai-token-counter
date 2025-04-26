"""
Module: __main__.py

Purpose:
    Package entry point for ai_token_counter, enabling `python -m ai_token_counter` execution.

Delegates argument parsing and token counting to cli and counter modules.
"""

import sys

from ai_token_counter.cli import parse_arguments
from ai_token_counter.counter import count_tokens


def main() -> None:
    """
    Execute the token counting flow with targeted error handling.

    Purpose:
        Parse command-line arguments, delegate to the core `count_tokens` API,
        and output the token count or an error message.

    Args:
        None

    Returns:
        None

    Raises:
        (none — unhandled exceptions will propagate)

    Side effects:
        Prints to stdout or stderr and exits the process.

    Assumptions:
        `parse_arguments()` returns valid attributes: file, model, encoding.
        `count_tokens()` may raise ValueError, FileNotFoundError,
        UnicodeError, IOError, TypeError.
    """
    args = parse_arguments()
    try:
        count, _ = count_tokens(
            source=args.file,
            model_alias=args.model,
            encoding_name=args.encoding,
        )
    except (ValueError, FileNotFoundError, UnicodeError, IOError, TypeError) as err:
        # Handle only expected failures with a clean exit code
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

    # Successful execution
    print(count)


if __name__ == "__main__":
    main()
