"""Writing a square numbers program using list fuction"""

def square_numbers(numbers):
    """calculating number with same number"""
    
    return [num ** 2 for num in numbers]
num = [1, 2, 3, 4]
result = square_numbers(num)
print("squared numbers:", result)

