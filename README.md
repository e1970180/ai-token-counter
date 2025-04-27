# ai-token-counter

Lightweight tool and Python package to count tokens in text using OpenAI-compatible tokenizers.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

```bash
# from PyPI
pip install ai-token-counter

# from source
git clone https://github.com/your-username/ai-token-counter.git
cd ai-token-counter
pip install -r requirements.txt
pip install .
```

## Quick Start

### Command-Line Interface (CLI)

Count tokens in a file:

```bash
ai-token-counter --file path/to/input.txt --model gpt-3.5-turbo
```

Count tokens via stdin:
```bash
echo "Hello, world!" | ai-token-counter --file - --model gpt35
```

Explicit encoding override:
```bash
ai-token-counter --file input.txt --encoding cl100k_base
```

### Python API

### Module Usage

Import and count tokens in your Python code:

```python
from ai_token_counter.counter import count_tokens

# Count tokens by model alias
count, encoding = count_tokens(
    source="examples/sample.txt",  # or '-' or a file-like object
    model_alias="gpt4o"
)
print(f"Tokens: {count}, Encoding used: {encoding}")
```

### Running as a Module

```bash
python -m ai_token_counter --file input.txt --model gpt4
```

## Development

- Code style: [black](https://github.com/psf/black) and [pylint](https://github.com/PyCQA/pylint) (configuration in `.pylintrc`).
- Tests: `pytest` (all tests are under `tests/`).

Run tests:
```bash
pytest
```

## Project Structure




## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
