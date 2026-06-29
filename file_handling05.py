"""Student file handling program."""

def main():
    """Read, write and update student records."""
    try:
        student_name = input("Enter student name: ")
        student_marks = input("Enter student marks: ")

        # Write to file
        with open("student.txt", "w", encoding="utf-8") as file:
            file.write(f"Name: {student_name}\n")
            file.write(f"Marks: {student_marks}\n")

        # Read file
        with open("student.txt", "r", encoding="utf-8") as file:
            print("\nStudent Record:")
            print(file.read())

        # Append data
        new_name = input("Enter another student name: ")

        with open("student.txt", "a", encoding="utf-8") as file:
            file.write(f"\nName: {new_name}")

        # Read updated file
        with open("student.txt", "r", encoding="utf-8") as file:
            print("\nUpdated file records: ")
            print(file.read())

    except FileNotFoundError:
        print("File not found. ")

    except PermissionError:
        print("Permission denied")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()
