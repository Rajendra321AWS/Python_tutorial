"""Writing greeting wishes program."""

import time

def greet_user(name: str) -> None:
    """Print greeting based on current time."""
    hour = time.localtime().tm_hour

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    print(f"Hello {name}, {greeting}")

if __name__ == "__main__":
    greet_user("Raj")
