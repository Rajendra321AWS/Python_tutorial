"""Demonstrate of commonly used python regex methods."""

import re

TEXT = (
    "my phone number is 9866098660 "
    "and my email id is text123@gmail.com."
)


def demo_match():
    """Demonstrate re.match()."""
    result = re.match(r"my", TEXT)

    if result:
        print("1. match(): ", result.group())
    else:
        print("1. match(): No match")


def demo_search():
    """Demonstrate re.search()."""
    result = re.search(r"\d{10}", TEXT)

    if result:
        print("2. search():", result.group())
    else:
        print("2. search(): Not matched")


def demo_findall():
    """Demonstrate re.findall()."""
    result = re.findall(r"\d", TEXT)
    print("3. findall()", result)


def demo_finditer():
    """Demonstrate re.finditer()."""
    print("4. finditer(): ")

    for match_obj in re.finditer(r"\d+", TEXT):
        print(
            f"match: {match_obj.group()} "
            f"Position: {match_obj.span()}"
        )


def demo_fullmatch():
    """Demonstrate re.fullmatch()."""
    result = re.fullmatch(r"\d+", "0123")

    if result:
        print("5. fullmatch(): Full match successfull")
    else:
        print("5. fullmatch(): Full match failed")


def demo_split():
    """Demonstrate re.split()."""
    sample_data = "apple, banana; Orange, grape"

    result = re.split(r"[,; ]+", sample_data)
    print("6. split(): ", result)


def demo_sub():
    """Demonstrate re.sub()."""
    result = re.sub(r"\d", "*", TEXT)
    print("7. sub(): ", result)


def demo_subn():
    """Demonstrate re.subn()."""
    result, count = re.subn(r"\d", "#", TEXT)

    print("8. re.subn(): ", result)
    print("Replacement: ", count)


def demo_compile():
    """Demonstrate re.compile()."""
    pattern = re.compile(r"\w+@\w+\.\w+")
    result = pattern.search(TEXT)

    if result:
        print("9. compile(): ", result.group())


def main():
    """Execute all RegEx methods."""
    demo_match()
    demo_search()
    demo_findall()
    demo_finditer()
    demo_fullmatch()
    demo_split()
    demo_sub()
    demo_subn()
    demo_compile()

if __name__ == "__main__":
    main()
