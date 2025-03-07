import json
import os
from typing import List
from DST.g5.student import Student
from DST.g5.professor import Professor
from DST.g5.course import Course

class Storage:
    def __init__(self, user_file='data/users.json', course_file='data/courses.json'):
        self.user_file = user_file
        self.course_file = course_file

        os.makedirs(os.path.dirname(user_file), exist_ok=True)
        os.makedirs(os.path.dirname(course_file), exist_ok=True)
        if not os.path.exists(user_file):
            with open(user_file, 'w') as f:
                json.dump([], f)
        if not os.path.exists(course_file):
            with open(course_file, 'w') as f:
                json.dump([], f)

    def save_users(self, users: List):
        data = []
        for u in users:
            user_type = 'Student' if isinstance(u, Student) else 'Professor'
            data.append({
                'type': user_type,
                'email': u.email,
                'password': u.password,
                'name': u.name,
                'id': u.student_id if user_type == 'Student' else u.professor_id
            })
        with open(self.user_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_users(self) -> List:
        with open(self.user_file, 'r') as f:
            data = json.load(f)

        users = []
        for item in data:
            if item['type'] == 'Student':
                s = Student(item['email'], item['password'], item['name'], item['id'])
                users.append(s)
            else:
                p = Professor(item['email'], item['password'], item['name'], item['id'])
                users.append(p)
        return users

    def save_courses(self, courses: List[Course]):
        data = []
        for c in courses:
            data.append({
                'course_id': c.course_id,
                'course_name': c.course_name,
                'instructor_email': c.instructor.email,
                'students': [s.email for s in c.students_enrolled]
            })
        with open(self.course_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_courses(self, users: List) -> List[Course]:
        with open(self.course_file, 'r') as f:
            data = json.load(f)

        email_to_user = {u.email: u for u in users}

        courses = []
        for item in data:
            instructor = email_to_user.get(item['instructor_email'])
            if not isinstance(instructor, Professor):
                # If the instructor is not found or not a professor, skip
                continue

            course = Course(item['course_id'], item['course_name'], instructor)
            instructor.create_course(course)

            for stud_email in item['students']:
                s = email_to_user.get(stud_email)
                if s and hasattr(s, 'enroll_course'):
                    s.enroll_course(course)
                    course.add_student(s)
            courses.append(course)

        return courses
