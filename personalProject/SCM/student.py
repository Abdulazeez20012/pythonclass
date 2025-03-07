from personalProject.SCM.user import User

class Student(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.courses = {}

    def enroll(self, course_name):
        if course_name in self.courses:
            raise ValueError("Already enrolled in this course")
        self.courses[course_name] = None

    def view_courses(self):
        return self.courses

    def view_grades(self):
        return {course: grade for course, grade in self.courses.items() if grade is not None}
