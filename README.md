# Token Counter with tiktoken

A Python script to count the number of tokens in a `.txt` file using the `tiktoken` library from OpenAI.

## Requirements

- Python 3.x
- Poetry
- `tiktoken` library

## Installation

1. **Clone the repository**.

2. **Install the required library**:
    ```bash
    poetry install
    ```

## Usage

1. **Activate the python environment (manually or with poetry)**.
    ```bash
    . .venv/bin/activate
    ```

2. **Run the script**:
    ```bash
    python token_calculator/count_tokens.py path/to/your/file.txt
    ```

    Or using poetry:

    ```bash
    poetry run count_tokens path/to/your/file.txt
    ```

    Replace `path/to/your/file.txt` with the actual path to the `.txt` file.

3. **Output**: The script will print the number of tokens in the specified text file.

## Example

```bash
python count_tokens.py example.txt
```

This will output the number of tokens in `example.txt`.
