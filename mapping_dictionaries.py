"""Basic dictionary program using functions."""

def show_dictionary(data):
    """Display dictionary items."""
    print("Dictionary values:", data)


def add_item(data, key, value):
    """Add item in dictionary."""
    data[key] = value
    print(f"{key} added successfully.")


# Main program
def main():
    """Main function."""

    student = {"name": "raj", "course": "python"}
    show_dictionary(student)
    add_item(student, "age", 21)
    show_dictionary(student)


main()
