"""Simple file handling program."""

from pathlib import Path

FILE_NAME ="sample.txt"

def write_file(file_path: str, content: str) -> None:
    """Write content to a file."""
    path = Path(file_path)

    with path.open("w", encoding="utf-8") as file:
        file.write(content)

def read_file(file_path: str) -> str:
    """Read and return file content."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return file.read()

def main() -> None:
    """Main function."""
    text = "Hello raj, this is file handling program."
    write_file(FILE_NAME, text)
    content = read_file(FILE_NAME)

    print("File content: ")
    print(content)

if __name__ == "__main__":
    main()
