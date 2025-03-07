from DST.g5.grade_type import GradeType

class Grade:
    def __init__(self, course, student, numeric_grade: float):
        self.course = course
        self.student = student
        self.numeric_grade = numeric_grade
        self.letter_grade = GradeType.from_numeric(numeric_grade)

    def set_numeric_grade(self, new_grade: float):
        self.numeric_grade = new_grade
        self.letter_grade = GradeType.from_numeric(new_grade)

    def view_grade(self):
        print(f"{self.course.course_name}: {self.numeric_grade} ({self.letter_grade.name})")
