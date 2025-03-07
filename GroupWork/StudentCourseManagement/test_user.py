import os
import unittest
from GroupWork.StudentCourseManagement.user import Student, Instructor, User
from GroupWork.StudentCourseManagement.data_manager import USER_FILE

class TestUser(unittest.TestCase):
    def setUp(self):
        if os.path.exists(USER_FILE):
            os.remove(USER_FILE)

    def test_email_pattern(self):
        with self.assertRaises(ValueError):
            Student("invalid-email", "pass123")

    def test_register_and_login_student(self):
        student = Student("student@example.com", "pass123")
        self.assertTrue(student.register())
        # Duplicate registration should fail.
        duplicate = Student("student@example.com", "pass123")
        self.assertFalse(duplicate.register())
        logged_in = User.login("student@example.com", "pass123")
        self.assertIsNotNone(logged_in)
        self.assertEqual(logged_in.email, "student@example.com")

    def test_register_and_login_instructor(self):
        instructor = Instructor("instructor@example.com", "pass456")
        self.assertTrue(instructor.register())
        logged_in = User.login("instructor@example.com", "pass456")
        self.assertIsNotNone(logged_in)
        self.assertEqual(logged_in.email, "instructor@example.com")

if __name__ == '__main__':
    unittest.main()
