"""
Program: Basic Error Handling Example
Description: Demonstrates exception handling using a main() function.
Author: Raj
"""

def divide_numbers(num1, num2):
    """Return the result of dividing two numbers."""
    return num1 / num2


def main():
    """Main function to execute the program."""
    try:
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))

        result = divide_numbers(num1, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter a valid numeric value.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    finally:
        print("Program execution completed.")


if __name__ == "__main__":
    main()
