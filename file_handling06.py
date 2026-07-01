"""Program to demonstrate CSV file handling in Python."""

import csv


def write_csv():
    """Write student data to a CSV file."""
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age"])
        writer.writerow([1, "Alice", 21])
        writer.writerow([2, "Bob", 22])
        writer.writerow([3, "Charlie", 20])

    print("CSV file created successfully.")


def read_csv():
    """Read and display student data from a CSV file."""
    print("\nContents of the CSV file:")

    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def main():
    """Run the program."""
    write_csv()
    read_csv()


if __name__ == "__main__":
    main()
