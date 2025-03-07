class Course:
    def __init__(self, course_name, instructor_email):
        self.course_name = course_name
        self.instructor = instructor_email
        self.students = []
        self.grades = {}

    def add_student(self, student_email):
        if student_email not in self.students:
            self.students.append(student_email)
        else:
            print(f"Student {student_email} is already enrolled in {self.course_name}.")

    def to_dict(self):
        return {
            'course_name': self.course_name,
            'instructor': self.instructor,
            'students': self.students,
            'grades': self.grades
        }
