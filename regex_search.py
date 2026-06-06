"""Return the first email address found in the given text."""

import re

def find_email(text):
    """Writing pattern to find email id"""

    pattern = r"[A-Za-z0-9./%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


# Main function.
def main():
    """Reun the email search example."""

    sample_text = "Please contact us ar support@example.com for assistance"

    email = find_email(sample_text)

    if email:
        print(f"Email found: {email}")
    else:
        print("No email found.")

if __name__== "__main__":
    main()
