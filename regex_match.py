"""Password validation program using regular expressions."""

import re

def check_password(password):
    """Check whether password is strong."""

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'

    if re.match(pattern, password):
        return "String password"
    return "Week password"

# Imput from user
def main():
    """Read a password and display the validation result"""

    pwd = input("Enter password: ")
    result = check_password(pwd)
    print(result)

if __name__=="__main__":
    main()
