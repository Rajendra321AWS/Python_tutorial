"""Employ attendence management system."""

import os
from datetime import datetime

FILENAME = "attendence.txt"

def mark_attence() -> None:
    """Record employe attendence with timestamp."""
    emp_id = input("Enter employee ID: ").strip()
    name = input("Enter Employee name").strip()

    timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{emp_id}, {name}, {timestamp}\n")

    print("Attendence marked successfully.")

def view_attendence() -> None:
    """Display all attendence records."""
    if not os.path.exists(FILENAME):
        print("No attendence records found.")
        return
    with open(FILENAME, "r", encoding="utf-8") as file:
        records = file.readlines()

    if not records:
        print("Attendence is empty.")
        return

    print("\nAttendence Records.")
    print("_" * 50)

    for record in records:
        emp_id, name, timestamp = record.strip().split(",")
        print(
            f"ID: {emp_id} | "
            f"Name: {name} | "
            f"time: {timestamp}"
        )

def display_menu() -> None:
    """Display the application menu."""
    print("\n1. Mark attendence")
    print("2. View attendence")
    print("3. Exit")

def main() -> None:
    """Run the attendence management system."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            mark_attence()
        elif choice == "2":
            view_attendence()
        elif choice == "3":
            print("Exiting ....")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
