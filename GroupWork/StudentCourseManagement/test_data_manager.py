import os
import json
import unittest
from GroupWork.StudentCourseManagement.data_manager import DataManager, USER_FILE, COURSE_FILE

class TestDataManager(unittest.TestCase):
    def setUp(self):
        if os.path.exists(USER_FILE):
            os.remove(USER_FILE)
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)

    def test_save_and_get_user(self):
        user_data = {'email': 'test@example.com', 'password': 'test', 'role': 'student'}
        DataManager.save_user(user_data)
        fetched = DataManager.get_user('test@example.com')
        self.assertEqual(fetched, user_data)

    def test_save_and_get_course(self):
        course_data = {
            'course_name': 'History 101',
            'instructor': 'instructor@example.com',
            'students': ['student@example.com'],
            'grades': {}
        }
        DataManager.save_course(course_data)
        courses = DataManager.get_all_courses()
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0]['course_name'], 'History 101')

    def test_enroll_student(self):
        course_data = {
            'course_name': 'Math 101',
            'instructor': 'instructor@example.com',
            'students': [],
            'grades': {}
        }
        DataManager.save_course(course_data)
        enrolled = DataManager.enroll_student('Math 101', 'student@example.com')
        self.assertTrue(enrolled)
        courses = DataManager.get_all_courses()
        self.assertIn('student@example.com', courses[0]['students'])

if __name__ == '__main__':
    unittest.main()
