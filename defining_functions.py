"""Writing program for demonstrate defining functions"""

# Simple program to prints message
def greet():
    """Print a welcome message to the user."""
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
NUM1 = 10
NUM2 = 5
SUM_VALUE = add_numbers(NUM1, NUM2)
print(f"the sum of {NUM1} and {NUM2} is {SUM_VALUE}")

# call power function
print(f"5 squared is {power(5)}")
print(f"2 rainsed to the power 5 is {power(2, 5)}")


# call calculater function
sum_res, diff_res, prod_res = calculator(8, 3)
print(f"sum_res: {sum_res}, Difference: {diff_res}, product: {prod_res}")
