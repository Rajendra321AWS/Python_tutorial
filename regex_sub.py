"""Replace digit sequences in text using regular expressions."""

import re

PATTERN = r"\d+"
REPLACEMENT = "#"

def replace_digits(text: str) -> str:
    """
    Replace all sequence of digits in the given text.
    args: 
        text: The input string.
        Returns: 
            A new string with each digit sequence replaced by '#'.
    """
    return re.sub(PATTERN, REPLACEMENT, text)

def main() -> None:
    """Run a simple demonstration."""
    sample_text = "Order 123 was placed on 2026-6-12."
    result = replace_digits(sample_text)
    print(f"Original text: {sample_text}")
    print(f"Modified text: {result}")

if __name__ == "__main__":
    main()
