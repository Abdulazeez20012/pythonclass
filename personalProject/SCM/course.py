class Course:
    def __init__(self, name, facilitator):
        self.name = name
        self.facilitator = facilitator
        self.students = []

    def enroll_student(self, student):
        if student in self.students:
            raise ValueError("Student already enrolled")
        self.students.append(student)

    def get_students(self):
        return [student.email for student in self.students]
