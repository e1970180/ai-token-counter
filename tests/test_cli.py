'''
File: tests/test_cli.py

Purpose:
    Pytest tests for the CLI interface and module entry point of ai-token-counter.

Tests:
    - Invocation of the CLI parser via module
    - Counting tokens from a file and from stdin
    - Error on missing mandatory arguments
'''
import subprocess
import sys
import os
import pytest

from pathlib import Path

# Helper to run the CLI and capture output

def run_cli(args, input_text=None):
    cmd = [sys.executable, '-m', 'ai_token_counter'] + args
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = proc.communicate(input=input_text)
    return proc.returncode, stdout.strip(), stderr.strip()


def test_count_file(tmp_path):
    # Create a temporary file with known content
    content = 'Hello world'
    file_path = tmp_path / 'sample.txt'
    file_path.write_text(content, encoding='utf-8')

    # Run CLI
    code, out, err = run_cli(['--file', str(file_path), '--model', 'gpt35'])
    # 'Hello world' should encode to 3 tokens: ['Hello',' world'] plus maybe leading tokens count
    assert code == 0
    assert out.isdigit()
    assert err == ''


def test_count_stdin():
    input_text = 'Test input for CLI'
    code, out, err = run_cli(['--file', '-', '--encoding', 'cl100k_base'], input_text=input_text)
    assert code == 0
    assert out.isdigit()
    assert err == ''


def test_missing_args():
    # Missing both model and encoding
    code, out, err = run_cli(['--file', 'dummy.txt'])
    assert code != 0
    assert 'error' in err.lower()


def test_unknown_alias(tmp_path):
    # Unknown model alias should produce error
    content = 'Sample'
    file_path = tmp_path / 's.txt'
    file_path.write_text(content, encoding='utf-8')
    code, out, err = run_cli(['--file', str(file_path), '--model', 'unknownmodel'])
    assert code != 0
    assert 'unknown model alias' in err.lower() or 'error' in err.lower()
