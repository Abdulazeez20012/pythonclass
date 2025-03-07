import unittest
import os
from DST.g5.student_management import StudentManagement
from DST.g5.student import Student
from DST.g5.professor import Professor
from DST.g5.exceptions import (
    UserNotFoundException,
    CourseNotFoundException,
    GradeOutOfRangeException
)

class TestStudentManagement(unittest.TestCase):

    def setUp(self):

        self.mgmt = StudentManagement()
        self.mgmt.storage.user_file = 'data/test_users.json'
        self.mgmt.storage.course_file = 'data/test_courses.json'

        with open(self.mgmt.storage.user_file, 'w') as f:
            f.write("[]")
        with open(self.mgmt.storage.course_file, 'w') as f:
            f.write("[]")

        self.mgmt.users = []
        self.mgmt.courses = []

    def test_register_and_login_user(self):
        s = Student("alice@example.com", "pass123", "Alice", "S001")
        self.mgmt.register_user(s)
        user = self.mgmt.login_user("alice@example.com", "pass123")
        self.assertEqual(user, s, "Login should return the same student object.")

        with self.assertRaises(UserNotFoundException):
            self.mgmt.login_user("wrong@example.com", "pass123")

    def test_create_course_and_enroll_student(self):
        prof = Professor("profjohn@example.com", "prof123", "Prof John", "P100")
        self.mgmt.register_user(prof)

        # Create a course
        self.mgmt.create_course("C101", "Intro to Python", "profjohn@example.com")
        self.assertEqual(len(self.mgmt.courses), 1)

        # Register a student
        s = Student("bob@example.com", "pass456", "Bob", "S002")
        self.mgmt.register_user(s)

        # Enroll student
        self.mgmt.enroll_student_in_course("bob@example.com", "C101")
        course = self.mgmt.get_course_by_id("C101")
        self.assertIn(s, course.students_enrolled, "Student should be enrolled in the course.")

    def test_assign_grade(self):
        prof = Professor("profjohn@example.com", "prof123", "Prof John", "P100")
        self.mgmt.register_user(prof)
        self.mgmt.create_course("C101", "Intro to Python", "profjohn@example.com")

        s = Student("bob@example.com", "pass456", "Bob", "S002")
        self.mgmt.register_user(s)
        self.mgmt.enroll_student_in_course("bob@example.com", "C101")

        # Assign a valid grade
        self.mgmt.assign_grade("profjohn@example.com", "bob@example.com", "C101", 95)
        self.assertAlmostEqual(s.grades[0].numeric_grade, 95)

        # Grade out of range
        with self.assertRaises(GradeOutOfRangeException):
            self.mgmt.assign_grade("profjohn@example.com", "bob@example.com", "C101", 120)

    def tearDown(self):
        """
        Remove temporary test files after each test if you want to clean up.
        """
        if os.path.exists(self.mgmt.storage.user_file):
            os.remove(self.mgmt.storage.user_file)
        if os.path.exists(self.mgmt.storage.course_file):
            os.remove(self.mgmt.storage.course_file)

if __name__ == '__main__':
    unittest.main()
