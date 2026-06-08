"""Find all words starting with capital letters. """

import re

def find_capital_words(text):
    """Return list of words starting with uppercase letters."""

    pattern = r'\b[A-Z][a-z]*\b'
    matches = re.findall(pattern, text)
    return matches

# Main function
def main():
    """Main function to run the program."""
    sentence = input("Enter a sentence: ")
    result = find_capital_words(sentence)
    print("Capital words found:", result)

if __name__ == "__main__":
    main()
