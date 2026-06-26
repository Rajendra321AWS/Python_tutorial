"""
File handling example

This program demonstrates:

1. Writing to and reading from a .txt file.
2. Writing to and reading from a .csv file.
"""

import csv

def write_text_file(filename, content):
    """
    Write content to a text file.

    args:
    filename(str): Name of the text file
    content(str): content to write
    """

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Text written to {filename}")
    except OSError as error:
        print(f"Error writing text file: {error}")

def read_text_file(filename):
    """
    Read and display content from a text file

    Args:
    filename (str): Name of the text file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print("\nText file content:")
        print(content)
    except FileNotFoundError:
        print(f"{filename} not found.")
    except OSError as error:
        print(f"Error reading a text file: {error}")

def write_csv_file(filename, data):
    """
    Write data to a .csv file.

    Args:
    filename (str): Name of the .csv file.
    data(list): list of rows to write.
    """
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"CSV data written to {filename}")
    except OSError as error:
        print(f"Error writing CSV file: {error}")

def read_csv_file(filename):
    """
    Read and display data from a CSV file.

    Args:
    filename (str): Name of the CSV file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            print("\nCSV file content:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"{filename} not found.")
    except OSError as error:
        print(f"Error reading CSV file: {error}")

def main():
    """Main function to execute file handling program.
    """
    # text file operations
    text_filename = "sample.txt"
    text_content = "Hello, Welcome to python file handling."

    write_text_file(text_filename, text_content)
    read_text_file(text_filename)

    # CSV file operation .
    csv_filename = "students.csv"
    csv_data = [
        ["ID", "Name", "Marks"],
        [101, "Raj", 40],
        [102, "Ram", 36],
        [103, "Madhu", 45]
    ]

    write_csv_file(csv_filename, csv_data)
    read_csv_file(csv_filename)

if __name__ == "__main__":
    main()
