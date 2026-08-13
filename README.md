# passgen

A small, secure command-line password generator written in Python.

`passgen` uses Python's `secrets` module for password generation and lets you control password length, character categories, excluded characters, and output destination from the command line.

## Features

- Cryptographically secure random selection via `secrets`.
- 12-character passwords by default.
- Uppercase letters, lowercase letters, digits, and special characters enabled by default.
- `--no-*` flags for disabling individual character categories.
- Ability to exclude specific characters.
- Optional output to a file.
- Configuration validation with explicit custom exceptions.
- Clear separation between CLI parsing, configuration, generation, and file output.

## Requirements

- Python 3.9+

## Installation

### With `pip`

```bash
pip install .
```

### With `uv`

```bash
uv sync
```

After installation, the `passgen` command is available in the active environment.

## Usage

Generate a default password:

```bash
passgen
```

Generate a 20-character password:

```bash
passgen --length 20
```

Disable special characters:

```bash
passgen --no-special
```

Generate a password using only letters:

```bash
passgen --no-digits --no-special
```

Exclude ambiguous characters:

```bash
passgen --exclude "0O1lI"
```

Save the generated password to a file:

```bash
passgen --output password.txt
```

Combine options:

```bash
passgen --length 24 --no-special --exclude "0O1lI" --output password.txt
```

Show all available options:

```bash
passgen --help
```

## Command-line options

| Option | Description | Default |
| --- | --- | --- |
| `--length N` | Password length | `12` |
| `--no-uppercase` | Disable uppercase letters | Enabled |
| `--no-lowercase` | Disable lowercase letters | Enabled |
| `--no-digits` | Disable digits | Enabled |
| `--no-special` | Disable special characters | Enabled |
| `--exclude CHARS` | Characters that must not appear in the password | None |
| `--output FILE` | Save the generated password to a file | stdout |

At least one character category must remain enabled. The password length must also be large enough to satisfy the selected character-category requirements.

## Output

Without `--output`, the password is written to stdout.

With `--output`, the generated password is written to the specified file using UTF-8 encoding.

## Project structure

```text
passgen/
├── src/
│   └── passgen/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── exception.py
│       ├── file_manager.py
│       ├── main.py
│       └── password_generator.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

The project follows a simple separation of responsibilities:

- `cli.py` — command-line argument parsing.
- `config.py` — immutable configuration and validation.
- `password_generator.py` — password generation logic.
- `file_manager.py` — file output.
- `exception.py` — domain-specific exceptions.
- `main.py` — application orchestration.

## Security notes

The generator uses `secrets.choice()` instead of the standard pseudo-random functions intended for non-security-sensitive tasks.

When multiple character categories are enabled, the generator guarantees that at least one character from each selected category is present. The remaining characters are selected from the combined allowed pool and the final password is shuffled using a cryptographically secure random source.

Do not use generated passwords in plaintext command history, shell scripts, or logs. When saving passwords to files, protect the file with appropriate filesystem permissions and avoid committing password files to source control.

## Development

Create a local environment with `uv`:

```bash
uv sync
```

Run the application locally:

```bash
uv run passgen --help
```

Run tests (when the test suite is present):

```bash
uv run pytest
```

## Roadmap

Potential future improvements include:

- a complete automated test suite for CLI, validation, generator, and file output;
- configurable output modes suitable for shell pipelines and scripting;
- password strength / entropy reporting;
- generation of multiple passwords in one invocation;
- configurable character sets and presets;
- safer output-file handling, including explicit overwrite control;
- packaging and CI checks for linting, typing, and tests.

## License

No license has been specified yet.
