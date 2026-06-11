"""Demonstrate the ise of finditer()."""
import re

TEXT = "Python is fun. Python is powerful. Python is easy to learn."
PATTERN = r"Python"

def main():
    """Find and display all matches."""
    matches = re.finditer(PATTERN, TEXT)

    print("Matches found: ")
    for match in matches:
        print(
            f"matched '{match.group()}'"
            f"at position {match.start()} to {match.end()}"
        )

if __name__ == "__main__":
    main()
