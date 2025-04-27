"""
Module: cli.py

Purpose:
    Parse command-line arguments for ai-token-counter CLI.

"""

import argparse

# import sys
# from argparse import Namespace


def parse_arguments() -> argparse.Namespace:
    """
    Parse CLI arguments for the ai-token-counter tool.

    Returns:
        Namespace with attributes:
            file: path to input file or '-' for stdin
            model: model alias to resolve encoding
            encoding: explicit tiktoken encoding name (overrides model)
    """
    parser = argparse.ArgumentParser(
        prog="ai-token-counter",
        description="Count tokens in text using tiktoken encodings for various AI models.",
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to input text file or '-' to read from stdin.",
    )
    parser.add_argument(
        "-m",
        "--model",
        required=False,
        help="AI model alias (e.g., gpt-3.5-turbo). Case-insensitive.",
    )
    parser.add_argument(
        "--encoding",
        required=False,
        help="Explicit tiktoken encoding name (overrides model alias mapping).",
    )
    parsed_args = parser.parse_args()

    # Validate that at least one of model or encoding is provided
    if not parsed_args.model and not parsed_args.encoding:
        parser.error("either --model or --encoding must be specified.")

    return parsed_args


# if __name__ == "__main__":
#     # Entry point when module is run directly
#     args = parse_arguments()
#     # Delegate main logic to counter module
#     from .counter import count_tokens

#     try:
#         count, _ = count_tokens(
#             source=args.file,
#             model_alias=args.model,
#             encoding_name=args.encoding,
#         )
#         # Output only the token count
#         print(count)

#     except (ValueError, FileNotFoundError, UnicodeError, IOError) as err:
#         print(f"Error: {err}", file=sys.stderr)
#         sys.exit(1)
#     else:
#         print(count)
