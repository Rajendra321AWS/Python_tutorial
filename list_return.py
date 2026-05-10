"""Writing program using list and return"""

def square_numbers(nums):
    """Square the numbers which are given in the list"""
    return[x * x for x in nums]

numbers = [1, 3, 5, 6, 8]
print(square_numbers(numbers))