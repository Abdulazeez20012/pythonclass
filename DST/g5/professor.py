from DST.g5.user import User

from typing import List

class Professor(User):
    def __init__(self, email: str, password: str, name: str, professor_id: str):
        super().__init__(email, password, name)
        self.professor_id = professor_id
        self.teaching_courses = []

    def create_course(self, course):
        if course not in self.teaching_courses:
            self.teaching_courses.append(course)

    def view_courses(self):
        if not self.teaching_courses:
            print(f"No courses for professor {self.name}.")
        else:
            print(f"Courses taught by {self.name}:")
            for c in self.teaching_courses:
                print(" -", c.course_name)
