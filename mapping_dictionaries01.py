"""Python program on mapping dictionaries using functions."""


def display_students(data):
    """Display dictionary items."""
    print("Student records:", data)


def add_student(data, roll_no, name):
    """Add student record."""
    data[roll_no] = name
    print(f"{name} added successfully.")


def search_student(data, roll_no):
    """Search students using roll number."""
    if roll_no in data:
        print("Student found:", data[roll_no])
    else:
        print("Student not found.")


def remove_student(data, roll_no):
    """Remove student from dictionary."""
    if roll_no in data:
        removed = data.pop(roll_no)
        print(f"{removed} removed successfully.")
    else:
        print("Student not found.")


def main():
    """Main functions."""
    students = {
        101: "Raj",
        102: "Kiran",
        103: "Madhu"
    }
    display_students(students)

    add_student(students, 104, "Ravi")
    display_students(students)

    search_student(students, 102)

    remove_student(students, 103)

    display_students(students)

if __name__ == "__main__":
    main()
