"""writing python program using functions and arguments"""

def add_numbers(a, b):
    """Return the sum of two numbers"""
    result = a + b
    return result

# calling the fuction with arguments
NUM1 = 10
NUM2 = 20

SUM = add_numbers(NUM1, NUM2)

# Display the result
print("The sum =", SUM)
