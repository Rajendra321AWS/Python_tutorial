"""Program to demonstrate advanced string methods."""

def convert_case(text):
    """Printing string methods."""
    print("Upper case: ", text.upper())
    print("Lower case: ", text.lower())
    print("Title case: ", text.title())
    print("Swap case: ", text.swapcase())


def check_string(text):
    """Check string properties."""
    print("Is Alphabetic: ", text.isalpha())
    print("Is Numeric: ", text.isdigit())
    print("Is Alphanumeric: ", text.isalnum())
    print("Starts with 'Py': ", text.startswith("Py"))
    print("End with 'on': ", text.endswith("on"))


def search_and_replace(text):
    """Search and replace text."""
    print("Original string: ", text)
    print("Find Python: ", text.find("Python"))
    print("Replace 'Python' with 'Java'", text.replace("Python", "Java"))


def split_and_join(text):
    """Split and join string."""
    words = text.split()
    print("Split list: ", words)
    print("Joined Strings: ", "-".join(words))


def remove_spaces(text):
    """Remove spaces from string."""
    print("Original: ", repr(text))
    print("Strip : ", repr(text.strip()))
    print("LStrip : ", repr(text.lstrip()))
    print("RStrip : ", repr(text.rstrip()))


def count_occurrences(string):
    """Count word occurrences."""
    word = input("Enter Word to count: ")
    print(f"'{word}' occurs {string.count(word)} times.")


def main():
    """ Main program."""

    string = " Python programming is fun and Python is powerful "

    print("\n----Case conversion ----- ")
    convert_case(string)

    print("\n----String checking ----- ")
    check_string("Python123")

    print("\n----Search and Replace ----- ")
    search_and_replace(string)

    print("\n----Split and Join ----- ")
    split_and_join(string)

    print("\n----Remove spaces ----- ")
    remove_spaces(string)

    print("\n----Count occurrences ----- ")
    count_occurrences(string)


if __name__ == "__main__":
    main()
