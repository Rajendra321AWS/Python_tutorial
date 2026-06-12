"""Demonstrate re.finditer."""

import re

def find_words(text, pattern):
    """Find and display all pattern matches."""
    matches = re.finditer(pattern, text)

    for match in matches:
        print(r"match: ", {match.group()})
        print(r"Start position: ", {match.start()})
        print(r"End position: ", {match.end()})
        print("_" * 20)

def main():
    """Program entry point."""
    text = "Python is powerful. Python is easy to learn."
    pattern = r"Python"
    print("search for pattern:", pattern)
    find_words(text, pattern)

if __name__ == "__main__":
    main()
