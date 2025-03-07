import re
from GroupWork.StudentCourseManagement.data_manager import DataManager
from GroupWork.StudentCourseManagement.course import Course

EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class User:
    def __init__(self, email, password):
        if not re.match(EMAIL_PATTERN, email):
            raise ValueError("Invalid email format.")
        self.email = email
        self.password = password

    def register(self):
        if DataManager.email_exists(self.email):
            print("Email already registered.")
            return False
        user_dict = {
            'email': self.email,
            'password': self.password,
            'role': self.__class__.__name__.lower()
        }
        DataManager.save_user(user_dict)
        return True

    @classmethod
    def login(cls, email, password):
        user_data = DataManager.get_user(email)
        if user_data and user_data.get('password') == password:
            role = user_data.get('role')
            if role == 'student':
                return Student(email, password)
            elif role == 'instructor':
                return Instructor(email, password)
        print("Invalid credentials.")
        return None

class Student(User):
    def __init__(self, email, password):
        super().__init__(email, password)

    def view_courses(self):
        return DataManager.get_student_courses(self.email)

    def enroll_in_course(self, course_name):
        if DataManager.enroll_student(course_name, self.email):
            print("Enrollment successful!")
            return True
        else:
            print("Enrollment failed.")
            return False

class Instructor(User):
    def __init__(self, email, password):
        super().__init__(email, password)

    def create_course(self, course_name):
        course = Course(course_name, self.email)
        DataManager.save_course(course.to_dict())
        return course

    def assign_grade(self, course_name, student_email, grade):
        DataManager.assign_grade(course_name, student_email, grade)

    def view_my_courses(self):
        return DataManager.get_courses_by_instructor(self.email)
