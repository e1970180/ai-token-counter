# tests/test_integration.py

"""
Integration tests for the ai_token_counter CLI via module execution.

Purpose:
    Verify end-to-end behavior of the program:
    - Reading from a file path and using a model alias.
    - Reading from stdin and using an explicit encoding.
    - Handling of unknown model aliases.
"""

import subprocess
import sys


def run_module(args, input_text=None):
    """
    Run `ai_token_counter` as a module and capture its output.

    Args:
        args (list[str]): Command-line arguments for the module.
        input_text (str | None): Text to send to stdin, if any.

    Returns:
        tuple[int, str, str]: (return_code, stdout, stderr)

    Side effects:
        None
    """
    cmd = [sys.executable, "-m", "ai_token_counter"] + args
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = proc.communicate(input=input_text)
    return proc.returncode, stdout.strip(), stderr.strip()


def test_integration_file_and_model_alias(tmp_path):
    """
    Count tokens from a file using the 'gpt35' alias.
    """
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello world", encoding="utf-8")

    code, out, err = run_module(["--file", str(file_path), "--model", "gpt35"])
    assert code == 0
    assert err == ""
    assert out.isdigit()
    assert int(out) >= 2


def test_integration_stdin_and_encoding():
    """
    Count tokens from stdin using explicit encoding 'cl100k_base'.
    """
    input_text = "Foo bar baz"
    code, out, err = run_module(
        ["--file", "-", "--encoding", "cl100k_base"],
        input_text=input_text,
    )
    assert code == 0
    assert err == ""
    assert out.isdigit()
    assert int(out) >= 2


def test_integration_unknown_model(tmp_path):
    """
    Ensure unknown model alias results in non-zero exit and error message.
    """
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Test data", encoding="utf-8")

    code, _, err = run_module(["--file", str(file_path), "--model", "unknown"])
    assert code != 0
    assert "Unknown model alias" in err or "Error:" in err
