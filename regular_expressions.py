"""Extract numbers from string using regular expressions."""

import re

def extract_numbers(text):
    """Extract all numbers from given text."""

    return re.findall(r"\d+", text)

def main():
    """Run the program."""
    text = "My age is 25 and my score is 95"
    numbers = extract_numbers(text)
    print(numbers)

if __name__=="__main__":
    main()

