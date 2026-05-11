"""Function to find the sum of numbers"""
def find_sum(numbers):
    total = 0
    # return the sum of all numbers in list
    for num in numbers:
        total += num

    return total

# list of elements
my_list = [10, 30, 50, 70]

# calling the function
RESULT = find_sum(my_list)

# Display results
print("sum of list elements", RESULT)
