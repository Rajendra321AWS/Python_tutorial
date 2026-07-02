"""Basic error handling sysntax."""

try:
    print(a)  # Resky code
except NameError:
    print("Error")
else:
    print("No error")
finally:
    print("always")
