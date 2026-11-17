"""Business logic and JSON persistence for student records."""

import json
from pathlib import Path

from student import Student


class StudentManager:
    def __init__(self, data_file="data/students.json"):
        self.data_file = Path(data_file)
        self.students = {}
        self._load()

    def _load(self):
        """Load saved records. Start with an empty list if no file exists."""
        if not self.data_file.exists():
            self.students = {}
            return

        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                records = json.load(file)
            self.students = {
                record["student_id"]: Student.from_dict(record)
                for record in records
            }
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            raise RuntimeError(
                f"Could not read {self.data_file}. Check that the JSON file is valid."
            ) from error

    def _save(self):
        """Write all records to JSON, creating the data directory if needed."""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        temporary_file = self.data_file.with_suffix(".tmp")
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(
                [student.to_dict() for student in self.students.values()],
                file,
                ensure_ascii=False,
                indent=4,
            )
        temporary_file.replace(self.data_file)

    def add_student(self, student_id, name, age, course):
        student_id = str(student_id).strip()
        name = str(name).strip()
        course = str(course).strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        if student_id in self.students:
            raise ValueError("Student ID already exists.")
        if not name or not course:
            raise ValueError("Name and course cannot be empty.")
        if not 1 <= int(age) <= 120:
            raise ValueError("Age must be between 1 and 120.")

        self.students[student_id] = Student(student_id, name, age, course)
        self._save()

    def list_students(self):
        return sorted(self.students.values(), key=lambda item: item.name.lower())

    def get_student(self, student_id):
        return self.students.get(str(student_id).strip())

    def search_students(self, query):
        query = str(query).strip().lower()
        return [
            student
            for student in self.list_students()
            if query in student.student_id.lower() or query in student.name.lower()
        ]

    def update_student(self, student_id, name=None, age=None, course=None):
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found.")

        if name is not None:
            if not str(name).strip():
                raise ValueError("Name cannot be empty.")
            student.name = str(name).strip()
        if age is not None:
            if not 1 <= int(age) <= 120:
                raise ValueError("Age must be between 1 and 120.")
            student.age = int(age)
        if course is not None:
            if not str(course).strip():
                raise ValueError("Course cannot be empty.")
            student.course = str(course).strip()
        self._save()

    def add_grade(self, student_id, subject, score):
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        student.add_grade(subject, score)
        self._save()

    def remove_grade(self, student_id, grade_index):
        student = self.get_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        if not 0 <= grade_index < len(student.grades):
            raise IndexError("Grade number is out of range.")
        student.grades.pop(grade_index)
        self._save()

    def delete_student(self, student_id):
        student_id = str(student_id).strip()
        if student_id not in self.students:
            raise ValueError("Student not found.")
        del self.students[student_id]
        self._save()
