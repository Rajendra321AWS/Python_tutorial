"""Simple file handling program to read a file"""

def read_file(file_name):
    """Read and display the comtents of the file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("\nFile contents:")
            print(file.read())

    except FileNotFoundError:
        print("Error: file not found.")

def main():
    """Main function."""

    file_name = input("Enter file name: ")
    read_file(file_name)

if __name__ == "__main__":
    main()
