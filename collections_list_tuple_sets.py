"""Python program on List, Tuple and sets using functions."""

# ------------ LIST FUNCTIONS ------------
def list_example():
    """Function for list example."""
    fruits = ["Apple", "Banana", "Mango"]

    fruits.append("Orange")
    fruits.remove("Mango")

    print("List items:", fruits)


# ------------ TUPLE FUNCTIONS ------------
def tuple_example():
    """Function for tuple example."""
    colors = ("Red", "Green", "Blue")

    print("Tuple items:", colors)
    print("First color in tuple:", colors[0])


# ------------ SETS FUNCTIONS ------------
def sets_example():
    """Function for sets example."""
    numbers = {1, 2, 3, 4}

    numbers.add(5)
    numbers.remove(2)

    print("Set items:", numbers)


# ------------ MAIN FUNCTION ------------
def main():
    """Main function."""
    print("---------- LIST EXAMPLES -----------")
    list_example()

    print("\n---------- TUPLE EXAMPLES -----------")
    tuple_example()

    print("\n---------- SET EXAMPLES -----------")
    sets_example()

# ------------ Program execution start here ------------
main()