# ai-token-counter

Lightweight tool and Python package to count tokens in text using OpenAI-compatible tokenizers.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ai-token-counter.git
   cd ai-token-counter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

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

```
ai-token-counter/
├── ai_token_counter/
│   ├── __init__.py
│   ├── cli.py
│   ├── counter.py
│   ├── file_utils.py
│   ├── tokenizer_config.py
│   ├── tokenizer_factory.py
│   └── tokenizers/
│       ├── __init__.py
│       └── openai.py
├── tests/
│   ├── test_counter.py
│   ├── test_file_utils.py
│   └── test_tokenizer_factory.py
├── requirements.txt
├── .pylintrc
├── README.md
└── LICENSE
```

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
