"""Student model and grade calculations."""


class Student:
    def __init__(self, student_id, name, age, course, grades=None):
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.age = int(age)
        self.course = str(course).strip()
        self.grades = grades if grades is not None else []
    @property
    def average(self):
        """Return the average score, or None when no grades exist."""
        if not self.grades:
            return None
        return sum(item["score"] for item in self.grades) / len(self.grades)

    @property
    def letter_grade(self):
        """Convert the average score to a letter grade."""
        average = self.average
        if average is None:
            return "N/A"
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def add_grade(self, subject, score):
        subject = str(subject).strip()
        score = int(score)
        if not subject:
            raise ValueError("Subject cannot be empty.")
        if not 0 <= score <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append({"subject": subject, "score": score})

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            grades=data.get("grades", []),
        )
