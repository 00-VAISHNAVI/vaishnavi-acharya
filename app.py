# Student Management System
# Simple Python Project

students = []


def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


def display_students():
    print("\n--- Student Details ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-----------------------------")
        print("Roll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("Marks       :", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter Roll Number to search: ")

    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("-----------------------------")
            print("Roll Number :", student["roll_no"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Marks       :", student["marks"])
            found = True
            break

    if not found:
        print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nCurrent Student Details:")
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            print("Marks  :", student["marks"])

            print("\nEnter new details:")

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("\nStudent details updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_grade():
    print("\n--- Calculate Grade ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            marks = student["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\nStudent Name :", student["name"])
            print("Marks        :", marks)
            print("Grade        :", grade)

            return

    print("Student not found.")


def show_total_students():
    print("\n--- Total Students ---")
    print("Total Students:", len(students))


def main():
    while True:

        print("\n===================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Grade")
        print("7. Show Total Students")
        print("8. Exit")

        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            calculate_grade()

        elif choice == "7":
            show_total_students()

        elif choice == "8":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()