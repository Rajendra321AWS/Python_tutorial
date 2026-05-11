"""Writing program for demonstrate defining functions"""

# Simple program to prints message
def greet():
    print("Hello welcome to python functions")

# function with parameters
def add_numbers(a,b):
    """return sum of a and b """
    result = a + b
    return result

# Function with default parameters
def power(number, exponent=2):
    """Return 'number' raised to 'exponent' (default is 2)."""
    return number ** exponent

# Function that performs multi operations
def calculator(x, y):
    """
    Return the sum, difference, and product of x and y.
    
    Returns:
        tuple: (sum, difference, product)
    """
    sum_result = x + y
    diff_result = x - y
    prod_result = x * y
    return sum_result, diff_result, prod_result

# ******************calling the functions ****************
# call greet function
greet()

# call add number function
num1 = 10
num2 = 5
sum_value = add_numbers(num1, num2)
print(f"the sum of {num1} and {num2} is {sum_value}")

# call power function
print(f"5 squared is {power(5)}")
print(f"2 rainsed to the power 5 is {power(2, 5)}")


# call calculater function
sum_res, diff_res, prod_res = calculator(8, 3)
print(f"sum_res: {sum_res}, Difference: {diff_res}, product: {prod_res}")
