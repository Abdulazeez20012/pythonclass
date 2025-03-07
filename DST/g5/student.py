from DST.g5.user import User
from DST.g5.grade import Grade
from typing import List

class Student(User):
    def __init__(self, email: str, password: str, name: str, student_id: str):
        super().__init__(email, password, name)
        self.student_id = student_id
        self.enrolled_courses = []
        self.grades: List[Grade] = []

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def view_courses(self):
        if not self.enrolled_courses:
            print(f"No courses for student {self.name}.")
        else:
            print(f"Courses for student {self.name}:")
            for c in self.enrolled_courses:
                print(" -", c.course_name)

    def add_grade(self, grade: Grade):
        existing = next((g for g in self.grades if g.course == grade.course), None)
        if existing:
            existing.set_numeric_grade(grade.numeric_grade)
        else:
            self.grades.append(grade)

    def view_grades(self):
        if not self.grades:
            print(f"No grades for student {self.name}.")
        else:
            print(f"Grades for {self.name}:")
            for g in self.grades:
                g.view_grade()

    def calculate_gpa(self) -> float:
        if not self.grades:
            return 0.0
        total = 0.0
        for g in self.grades:
            total += g.letter_grade.value
        return total / len(self.grades)
