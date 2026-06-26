"""Simple file handling program."""

def main():
    """Write and read a file."""
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Hello Python.")

    with open("sample.txt", "r", encoding="utf-8") as file:
        print(  file.read())

if __name__ == "__main__":
    main()
