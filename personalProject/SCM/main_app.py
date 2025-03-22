import json
import os
import sys
from personalProject.SCM.student import Student
from personalProject.SCM.facilitator import Facilitator
from personalProject.SCM.course import Course

STUDENTS_FILE = "students.json"
FACILITATORS_FILE = "facilitators.json"
COURSES_FILE = "courses.json"

def load_data(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def save_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving {filename}: {e}")

def find_user(email, users):
    for user in users:
        if user["email"] == email:
            return user
    return None

def register_user(user_type):
    try:
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        if user_type == "student":
            user = Student(email, password)
            students = load_data(STUDENTS_FILE)
            if find_user(email, students):
                print("A user with that email already exists.")
                return

            students.append({"email": user.email, "password_hash": user.password_hash, "courses": {}})
            save_data(STUDENTS_FILE, students)
            print("Student registered successfully!")
        elif user_type == "facilitator":
            user = Facilitator(email, password)
            facilitators = load_data(FACILITATORS_FILE)
            if find_user(email, facilitators):
                print("A user with that email already exists.")
                return
            facilitators.append({"email": user.email, "password_hash": user.password_hash, "courses": []})
            save_data(FACILITATORS_FILE, facilitators)
            print("Facilitator registered successfully!")
    except Exception as e:
        print(f"Registration error: {e}")

def login_user(user_type):
    try:
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        if user_type == "student":
            users = load_data(STUDENTS_FILE)
            user_data = find_user(email, users)
            if not user_data:
                print("No student found with that email.")
                return None
            # Create a temporary Student object for password verification and loading courses
            temp = Student(email, password)
            temp.password_hash = user_data["password_hash"]
            if not temp.verify_password(password):
                print("Incorrect password.")
                return None
            # Load courses from file into the Student object\n
            temp.courses = user_data.get("courses", {})
            print("Student logged in successfully!")
            return temp
        elif user_type == "facilitator":
            users = load_data(FACILITATORS_FILE)
            user_data = find_user(email, users)
            if not user_data:
                print("No facilitator found with that email.")
                return None
            temp = Facilitator(email, password)
            temp.password_hash = user_data["password_hash"]
            if not temp.verify_password(password):
                print("Incorrect password.")
                return None
            temp.courses = user_data.get("courses", [])
            print("Facilitator logged in successfully!")
            return temp
    except Exception as e:
        print(f"Login error: {e}")
        return None

def save_student(student):
    students = load_data(STUDENTS_FILE)
    for i, s in enumerate(students):
        if s["email"] == student.email:
            students[i]["courses"] = student.courses
            break
    save_data(STUDENTS_FILE, students)

def save_facilitator(facilitator):
    facilitators = load_data(FACILITATORS_FILE)
    for i, f in enumerate(facilitators):
        if f["email"] == facilitator.email:
            facilitators[i]["courses"] = facilitator.courses
            break
    save_data(FACILITATORS_FILE, facilitators)

def load_courses():
    courses = load_data(COURSES_FILE)
    return courses

def save_course(course):
    courses = load_data(COURSES_FILE)
    for i, c in enumerate(courses):
        if c["name"] == course.name:
            courses[i] = {"name": course.name, "facilitator": course.facilitator.email, "students": course.get_students()}
            break
    else:
        courses.append({"name": course.name, "facilitator": course.facilitator.email, "students": course.get_students()})
    save_data(COURSES_FILE, courses)

def student_menu(student):
    while True:
        print("\nStudent Menu:")
        print("1. View enrolled courses")
        print("2. View grades")
        print("3. Enroll in a new course")
        print("4. Logout")
        choice = input("Select an option: ").strip()
        try:
            if choice == "1":
                courses = student.view_courses()
                if courses:
                    print("Enrolled courses:")
                    for course, grade in courses.items():
                        print(f"- {course} | Grade: {grade}")
                else:
                    print("You are not enrolled in any courses.")
            elif choice == "2":
                grades = student.view_grades()
                if grades:
                    print("Your grades:")
                    for course, grade in grades.items():
                        print(f"- {course}: {grade}")
                else:
                    print("No grades available yet.")
            elif choice == "3":
                    # display_available_course():
                    #     passJ
                course_name = input("Enter course name to enroll: ").strip()
                try:
                    student.enroll(course_name)
                    save_student(student)
                    print(f"Enrolled in {course_name} successfully!")
                except Exception as e:
                    print(f"Error enrolling: {e}")
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

def facilitator_menu(facilitator, student_data=None):
    while True:
        print("\nFacilitator Menu:")
        print("1. Create a new course")
        print("2. Assign grade to a student")
        print("3. Logout")
        choice = input("Select an option: ").strip()
        try:
            if choice == "1":
                course_name = input("Enter course name to create: ").strip()
                try:
                    facilitator.create_course(course_name)
                    course = Course(course_name, facilitator)
                    save_course(course)
                    save_facilitator(facilitator)
                    print(f"Course {course_name} created successfully!")
                except Exception as e:
                    print(f"Error creating course: {e}")
            elif choice == "2":
                student_email = input("Enter student email: ").strip()
                course_name = input("Enter course name: ").strip()
                grade_input = input("Enter grade: ").strip()
                try:
                    grade = float(grade_input)
                except ValueError:
                    print("Invalid grade format. Grade must be a number.")
                    continue


                students = load_data(STUDENTS_FILE)
                student_data = find_user(student_email, students)
                if not student_data:
                    print("Student not found.")
                    continue

                temp_student = Student(student_data["email"], "DummyPass1!")  # password not used\n
                temp_student.password_hash = student_data["password_hash"]
                temp_student.courses = student_data.get("courses", {})
                try:
                    facilitator.assign_grade(temp_student, course_name, grade)
                    save_student(temp_student)
                    print(f"Assigned grade {grade} to {student_email} for {course_name}.")
                except Exception as e:
                    print(f"Error assigning grade: {e}")
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    while True:
        print("\n=== Student Course Management System ===")
        print("1. Register as Student")
        print("2. Register as Facilitator")
        print("3. Login as Student")
        print("4. Login as Facilitator")
        print("5. Exit")
        option = input("Select an option: ").strip()
        try:
            if option == "1":
                register_user("student")
            elif option == "2":
                register_user("facilitator")
            elif option == "3":
                student = login_user("student")
                if student:
                    student_menu(student)
            elif option == "4":
                facilitator = login_user("facilitator")
                if facilitator:
                    facilitator_menu(facilitator)
            elif option == "5":
                print("Exiting... Goodbye!")
                sys.exit(0)
            else:
                print("Invalid option. Please select from the menu.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
