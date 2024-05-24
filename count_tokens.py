import tiktoken
import argparse


def count_tokens(file_path):
    # Load the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Read the text file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.encode(text)

    # Return the number of tokens formatted with commas
    return "{:,}".format(len(tokens))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count the number of tokens in a text file."
    )
    parser.add_argument("file_path", type=str, help="Path to the .txt file.")

    args = parser.parse_args()

    num_tokens = count_tokens(args.file_path)
    print(f"Number of tokens: {num_tokens}")
