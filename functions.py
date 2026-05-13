"""Writing a program using functions"""
# Function 01
def great():
    """Writing Basic fuction """
    print("Hello Word")

def great_01(name):
    """ Function with arguments"""
    print("Hello", name)

def add(a, b):
    """Fuction with multi arguments"""
    result = a + b
    print("sum of a and b:", result)

def multiply(a, b):
    """ Function returning value"""
    return a * b
    result = multiply(5, 4)
    print("multiplication", result)




great()
great_01("Raj")
add(10, 20)
multiply(5, 4)
