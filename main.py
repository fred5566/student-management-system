"""Command-line Student Management System.

Features:
- Add, list, search, update, and delete students
- Add and remove grades
- Calculate each student's average and letter grade
- Generate class reports
- Persist data in a JSON file
"""

from student_manager import StudentManager
from utils import read_int, read_non_empty, confirm


def show_menu():
    print("\n" + "=" * 44)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 44)
    print("1. Add a student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student information")
    print("5. Add a grade")
    print("6. Remove a grade")
    print("7. Delete a student")
    print("8. View student report")
    print("9. View class report")
    print("0. Exit")
    print("-" * 44)


def display_student(student):
    average = student.average
    average_text = f"{average:.2f}" if average is not None else "No grades"
    print(
        f"ID: {student.student_id} | Name: {student.name} | "
        f"Age: {student.age} | Course: {student.course} | "
        f"Average: {average_text} | Letter: {student.letter_grade}"
    )


def add_student(manager):
    print("\n--- Add a student ---")
    student_id = read_non_empty("Student ID: ")
    if manager.get_student(student_id):
        print("A student with that ID already exists.")
        return

    name = read_non_empty("Full name: ")
    age = read_int("Age: ", minimum=1, maximum=120)
    course = read_non_empty("Course / program: ")

    try:
        manager.add_student(student_id, name, age, course)
        print("Student added successfully.")
    except ValueError as error:
        print(f"Could not add student: {error}")


def view_students(manager):
    print("\n--- All students ---")
    students = manager.list_students()
    if not students:
        print("No students have been registered yet.")
        return
    for student in students:
        display_student(student)


def search_student(manager):
    print("\n--- Search ---")
    query = read_non_empty("Enter student ID or name: ")
    matches = manager.search_students(query)
    if not matches:
        print("No matching students found.")
        return
    for student in matches:
        display_student(student)


def update_student(manager):
    print("\n--- Update student ---")
    student_id = read_non_empty("Student ID: ")
    student = manager.get_student(student_id)
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{student.name}]: ").strip() or student.name
    age_text = input(f"Age [{student.age}]: ").strip()
    course = input(f"Course [{student.course}]: ").strip() or student.course

    if age_text:
        try:
            age = int(age_text)
            if not 1 <= age <= 120:
                raise ValueError
        except ValueError:
            print("Age must be a whole number between 1 and 120. No changes made.")
            return
    else:
        age = student.age

    manager.update_student(student_id, name=name, age=age, course=course)
    print("Student information updated.")


def add_grade(manager):
    print("\n--- Add a grade ---")
    student_id = read_non_empty("Student ID: ")
    if not manager.get_student(student_id):
        print("Student not found.")
        return
    subject = read_non_empty("Subject: ")
    grade = read_int("Grade (0-100): ", minimum=0, maximum=100)
    manager.add_grade(student_id, subject, grade)
    print("Grade added successfully.")


def remove_grade(manager):
    print("\n--- Remove a grade ---")
    student_id = read_non_empty("Student ID: ")
    student = manager.get_student(student_id)
    if not student:
        print("Student not found.")
        return
    if not student.grades:
        print("This student has no grades.")
        return

    for index, item in enumerate(student.grades, start=1):
        print(f"{index}. {item['subject']}: {item['score']}")
    choice = read_int("Select the grade number to remove: ", minimum=1, maximum=len(student.grades))
    manager.remove_grade(student_id, choice - 1)
    print("Grade removed.")


def delete_student(manager):
    print("\n--- Delete student ---")
    student_id = read_non_empty("Student ID: ")
    student = manager.get_student(student_id)
    if not student:
        print("Student not found.")
        return
    display_student(student)
    if confirm("Are you sure you want to delete this student? (y/n): "):
        manager.delete_student(student_id)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


def student_report(manager):
    print("\n--- Student report ---")
    student_id = read_non_empty("Student ID: ")
    student = manager.get_student(student_id)
    if not student:
        print("Student not found.")
        return

    print(f"\nReport for {student.name}")
    print("-" * 34)
    print(f"ID: {student.student_id}")
    print(f"Age: {student.age}")
    print(f"Course: {student.course}")
    print("Grades:")
    if student.grades:
        for item in student.grades:
            print(f"  - {item['subject']}: {item['score']}/100")
    else:
        print("  No grades recorded.")
    average = student.average
    print(f"Average: {average:.2f}" if average is not None else "Average: N/A")
    print(f"Letter grade: {student.letter_grade}")


def class_report(manager):
    print("\n--- Class report ---")
    students = manager.list_students()
    if not students:
        print("No student data available.")
        return

    graded = [student for student in students if student.average is not None]
    print(f"Total students: {len(students)}")
    print(f"Students with grades: {len(graded)}")
    print(f"Students without grades: {len(students) - len(graded)}")

    if not graded:
        print("No grades have been recorded yet.")
        return

    class_average = sum(student.average for student in graded) / len(graded)
    top_student = max(graded, key=lambda item: item.average)
    print(f"Class average: {class_average:.2f}")
    print(f"Top student: {top_student.name} ({top_student.average:.2f})")


def main():
    manager = StudentManager()
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": add_grade,
        "6": remove_grade,
        "7": delete_student,
        "8": student_report,
        "9": class_report,
    }

    print("Welcome! Student records are saved automatically.")
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid option. Please choose a number from 0 to 9.")


if __name__ == "__main__":
    main()
