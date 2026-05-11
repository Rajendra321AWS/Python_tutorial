"""Function to find the sum of numbers"""
def find_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

# list of elements
my_list = [10, 30, 50, 70]

# calling the function
result = find_sum(my_list)

# Display results
print("sum of list elements", result)
