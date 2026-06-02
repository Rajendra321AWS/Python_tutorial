"""Program to demonstrate string methods."""

def string_methods(text):
    """Display various string methods"""

    print("Upper case:", {text.upper()})
    print("Lower case:", {text.lower()})
    print("Title case:", {text.title()})
    print("Capitalized:", {text.capitalize()})
    print("Length of string:", {len(text)})
    print("Replace 'Python' with 'Java'", {text.replace("Python", "Java")})
    print("Count of o:", {text.count("o")})
    print("Starts with P:", {text.startswith("P")})
    print("End with N:", {text.endswith("n")})
    print("Split string:", text.split())


# main Function

user_text = input("Enter a string: ")
string_methods(user_text)
