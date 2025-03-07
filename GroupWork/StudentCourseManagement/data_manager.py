import json
import os

USER_FILE = 'users.txt'
COURSE_FILE = 'courses.txt'

class DataManager:
    @staticmethod
    def save_user(user_dict):
        try:
            with open(USER_FILE, 'a') as f:
                f.write(json.dumps(user_dict) + "\n")
        except Exception as e:
            print(f"Error saving user: {e}")

    @staticmethod
    def email_exists(email):
        if not os.path.exists(USER_FILE):
            return False
        try:
            with open(USER_FILE, 'r') as f:
                for line in f:
                    try:
                        user = json.loads(line)
                        if user.get('email') == email:
                            return True
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error checking email: {e}")
        return False

    @staticmethod
    def get_user(email):
        if not os.path.exists(USER_FILE):
            return None
        try:
            with open(USER_FILE, 'r') as f:
                for line in f:
                    try:
                        user = json.loads(line)
                        if user.get('email') == email:
                            return user
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error reading user: {e}")
        return None

    @staticmethod
    def save_course(course_dict):
        try:
            with open(COURSE_FILE, 'a') as f:
                f.write(json.dumps(course_dict) + "\n")
        except Exception as e:
            print(f"Error saving course: {e}")

    @staticmethod
    def get_all_courses():
        courses = []
        if not os.path.exists(COURSE_FILE):
            return courses
        try:
            with open(COURSE_FILE, 'r') as f:
                for line in f:
                    try:
                        course = json.loads(line)
                        courses.append(course)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            print(f"Error reading courses: {e}")
        return courses

    @staticmethod
    def get_student_courses(student_email):
        courses = []
        for course in DataManager.get_all_courses():
            if student_email in course.get('students', []):
                courses.append(course)
        return courses

    @staticmethod
    def assign_grade(course_name, student_email, grade):
        courses = DataManager.get_all_courses()
        updated = False
        try:
            with open(COURSE_FILE, 'w') as f:
                for course in courses:
                    if course.get('course_name') == course_name:
                        if student_email in course.get('students', []):
                            course.setdefault('grades', {})[student_email] = grade
                            updated = True
                    f.write(json.dumps(course) + "\n")
            if not updated:
                print("No matching course or student found for grade assignment.")
        except Exception as e:
            print(f"Error assigning grade: {e}")

    @staticmethod
    def get_courses_by_instructor(instructor_email):
        courses = []
        for course in DataManager.get_all_courses():
            if course.get('instructor') == instructor_email:
                courses.append(course)
        return courses

    @staticmethod
    def get_course_by_name(course_name):
        for course in DataManager.get_all_courses():
            if course.get('course_name') == course_name:
                return course
        return None

    @staticmethod
    def enroll_student(course_name, student_email):
        courses = DataManager.get_all_courses()
        updated = False
        try:
            with open(COURSE_FILE, 'w') as f:
                for course in courses:
                    if course.get('course_name') == course_name:
                        if student_email not in course.get('students', []):
                            course.setdefault('students', []).append(student_email)
                            updated = True
                    f.write(json.dumps(course) + "\n")
            return updated
        except Exception as e:
            print(f"Error enrolling student: {e}")
            return False
