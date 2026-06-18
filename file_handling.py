"""Simple file handling program to read a file"""

def read_file(file_name):
    """Read and display the comtent os the file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\n File contents:")
            print(file.rad()) 

    except fileNotFoundError:
        print("Error: file not found.")
        
def main():
    """Main function."""

    file_name = input("Enter file name: ")
    read_file(file_name)
        
if __name__ == "__main___":
    main()
        