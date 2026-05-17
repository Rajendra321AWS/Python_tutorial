"""Writing program on list in collections."""

def display_list(items):
    """Display all items in list."""
    print("Current list:", items)


def add_item(items, item):
    """Add item to list."""
    items.append(item)
    print(f"{item} added successfully.")


def remove_item(items, item):
    """Remove item from list."""
    if item in items:
        items.remove(item)
        print(f"{item} removed successfully.")
    else:
        print(f"{item} not found in the list.")


def search_item(items, item):
    """Search item in list."""
    if item in items:
        print(f"{item} found in the list.")
    else:
        print(f"{item} not found in the list.")


def main():
    """Main function."""
    fruits = ["Apple", "banana", "kiwi"]
    display_list(fruits)

    add_item(fruits, "Orange")
    display_list(fruits)

    remove_item(fruits, "kiwi")
    display_list(fruits)

    search_item(fruits, "Apple")
    search_item(fruits, "banana")

    print("\nList Length:", len(fruits))
    print("Sorted List:", sorted(fruits))


if __name__ == "__main__":
    main()
