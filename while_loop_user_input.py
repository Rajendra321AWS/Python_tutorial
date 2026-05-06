"""Writing program on while loop with user input"""

def user_input_loop():
    """while loop for user input"""
    user_input = ""
    while user_input != "exit":
        user_input = input("Type something OR type 'exit' to quit): ")
        print("you types:", user_input)

user_input_loop()
