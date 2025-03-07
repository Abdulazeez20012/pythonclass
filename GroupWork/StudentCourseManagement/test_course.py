import unittest
from GroupWork.StudentCourseManagement.course import Course

class TestCourse(unittest.TestCase):
    def test_create_course(self):
        course = Course("Biology 101", "instructor@example.com")
        self.assertEqual(course.course_name, "Biology 101")
        self.assertEqual(course.instructor, "instructor@example.com")
        self.assertEqual(course.students, [])
        self.assertEqual(course.grades, {})

    def test_add_student(self):
        course = Course("Chemistry 101", "instructor@example.com")
        course.add_student("student@example.com")
        self.assertIn("student@example.com", course.students)
        # Adding the same student should not duplicate
        course.add_student("student@example.com")
        self.assertEqual(len(course.students), 1)

if __name__ == '__main__':
    unittest.main()
