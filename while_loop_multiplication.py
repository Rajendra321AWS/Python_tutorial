"""multiplication table printing using while function"""

def multiplication_table(num):
    """while loop for multiplication"""
    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i);
        i += 1

multiplication_table(5)

