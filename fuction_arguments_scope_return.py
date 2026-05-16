"""Writing python program using function, arguments, scope and return."""

# Global variable

COMPANY = "Open_AI"

# Function without arguments

def welcome():
    """Function without arguments."""
    print("Welcome to python functions")

# Function with single arguments

def greet(name):
    """Function with single arguments."""
    print("Hello", name)

# Function with multiple arguments and return type

def add(a, b):
    """Function with multiple arguments with return."""
    result = a + b
    return result

# Function showing local scope

def local_scope_example():
    """Local scope example."""
    message = "I am local variable"
    print(message)

# Function using global variable

def show_company():
    """Access global variable inside function."""
    print("Company name is", COMPANY)

# Function modifying global variable

count = 0

def increment():
    """Modifying global variable."""
    global count
    count += 1
    print("Count value:", count)

# Function with default arguments

def show_country(name="India"):
    """Default argument example."""
    print("Your country name:", name)

# Main function

def main():
    """Calling main function."""

    # Calling function without arguments

    welcome()

    print("_" * 45)
    
    # Function calling with single arguments

    greet("Raj")

    print("_" * 45)

    # Function calling to add numbers

    total = add(10, 20)
    print("Addition of given numbers:", total)

    print("_" * 45)

    # Function with local scope example

    local_scope_example()

    print("_" * 45)

    # Global scope example

    show_company()

    print("_" * 45)

    # Global key word example

    increment()

    print("_" * 45)

    # Default arguments

    show_country()
    show_country("USA")

# Program execution starts here

if __name__ == "__main__":
    main()
