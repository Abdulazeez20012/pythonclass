from typing import List

class Course:
    def __init__(self, course_id: str, course_name: str, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor 
        self.students_enrolled: List = []

    def add_student(self, student):
        if student not in self.students_enrolled:
            self.students_enrolled.append(student)

    def remove_student(self, student):
        if student in self.students_enrolled:
            self.students_enrolled.remove(student)

    def get_students(self):
        return self.students_enrolled
