from personalProject.SCM.user import User

class Facilitator(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.courses = []

    def create_course(self, course_name):
        if course_name in self.courses:
            raise ValueError("Course already exists")
        self.courses.append(course_name)

    def assign_grade(self, student, course_name, grade):
        if course_name not in student.courses:
            raise ValueError("Student is not enrolled in this course")
        student.courses[course_name] = grade
