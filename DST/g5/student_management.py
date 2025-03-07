from DST.g5.storage import Storage
from DST.g5.student import Student
from DST.g5.professor import Professor
from DST.g5.course import Course
from DST.g5.exceptions import UserNotFoundException, CourseNotFoundException, GradeOutOfRangeException

class StudentManagement:
    def __init__(self):
        self.storage = Storage()
        self.users = self.storage.load_users()
        self.courses = []
        self.courses = self.storage.load_courses(self.users)

    def register_user(self, user):
        if any(u.email == user.email for u in self.users):
            print(f"User with email {user.email} already exists.")
            return
        self.users.append(user)
        self.save_all()

    def login_user(self, email, password):
        for u in self.users:
            if u.login(email, password):
                return u
        raise UserNotFoundException(f"No user found or invalid password for {email}")

    def create_course(self, course_id, course_name, professor_email):
        prof = self.get_professor_by_email(professor_email)
        if not prof:
            raise UserNotFoundException(f"No professor found with email {professor_email}")

        new_course = Course(course_id, course_name, prof)
        prof.create_course(new_course)
        self.courses.append(new_course)
        self.save_all()

    def enroll_student_in_course(self, student_email, course_id):
        student = self.get_student_by_email(student_email)
        if not student:
            raise UserNotFoundException(f"No student found with email {student_email}")

        course = self.get_course_by_id(course_id)
        if not course:
            raise CourseNotFoundException(f"No course found with ID {course_id}")

        student.enroll_course(course)
        course.add_student(student)
        self.save_all()

    def assign_grade(self, professor_email, student_email, course_id, numeric_grade):
        if numeric_grade < 0 or numeric_grade > 100:
            raise GradeOutOfRangeException("Grade must be between 0 and 100.")

        prof = self.get_professor_by_email(professor_email)
        student = self.get_student_by_email(student_email)
        course = self.get_course_by_id(course_id)

        if not prof:
            raise UserNotFoundException(f"No professor found with email {professor_email}")
        if not student:
            raise UserNotFoundException(f"No student found with email {student_email}")
        if not course:
            raise CourseNotFoundException(f"No course found with ID {course_id}")

        if course not in prof.teaching_courses:
            raise CourseNotFoundException(f"This course is not taught by professor {prof.name}.")

        if student not in course.students_enrolled:
            print(f"Student {student.name} is not enrolled in {course.course_name}.")
            return

        from DST.g5.grade import Grade
        new_grade = Grade(course, student, numeric_grade)
        student.add_grade(new_grade)
        print(f"Assigned grade {numeric_grade} to {student.name} for {course.course_name}")
        self.save_all()

    def get_professor_by_email(self, email):
        for u in self.users:
            if isinstance(u, Professor) and u.email == email:
                return u
        return None

    def get_student_by_email(self, email):
        for u in self.users:
            if isinstance(u, Student) and u.email == email:
                return u
        return None

    def get_course_by_id(self, course_id):
        for c in self.courses:
            if c.course_id == course_id:
                return c
        return None

    def save_all(self):
        self.storage.save_users(self.users)
        self.storage.save_courses(self.courses)
