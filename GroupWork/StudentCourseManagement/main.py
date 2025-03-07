from GroupWork.StudentCourseManagement.user import Student, Instructor, User
from GroupWork.StudentCourseManagement.data_manager import DataManager

def instructor_menu(user):
    while True:
        print("\nInstructor Options:")
        print("1. Create Course")
        print("2. Assign Grade")
        print("3. View My Courses")
        print("4. View Enrolled Students in a Course")
        print("5. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            course_name = input("Enter course name: ").strip()
            course = user.create_course(course_name)
            if course:
                print("Course created successfully!")
            else:
                print("Failed to create course.")
        elif choice == '2':
            course_name = input("Enter course name: ").strip()
            student_email = input("Enter student email: ").strip()
            grade = input("Enter grade: ").strip()
            user.assign_grade(course_name, student_email, grade)
            print("Grade assigned!")
        elif choice == '3':
            courses = user.view_my_courses()
            if courses:
                print("Your Courses:")
                for course in courses:
                    print(f"Course: {course.get('course_name')} | Enrolled Students: {len(course.get('students', []))}")
            else:
                print("No courses created yet.")
        elif choice == '4':
            course_name = input("Enter course name: ").strip()
            course = DataManager.get_course_by_name(course_name)
            if course and course.get('instructor') == user.email:
                students = course.get('students', [])
                if students:
                    print("Enrolled Students:")
                    for s in students:
                        print(s)
                else:
                    print("No students enrolled yet.")
            else:
                print("Course not found or you are not the instructor for this course.")
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def student_menu(user):
    while True:
        print("\nStudent Options:")
        print("1. View Enrolled Courses")
        print("2. Enroll in a Course")
        print("3. Check Grade for a Course")
        print("4. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            courses = user.view_courses()
            if courses:
                print("Your Enrolled Courses:")
                for course in courses:
                    print(f"Course: {course.get('course_name')} | Instructor: {course.get('instructor')}")
            else:
                print("You are not enrolled in any courses.")
        elif choice == '2':
            course_name = input("Enter course name to enroll: ").strip()
            user.enroll_in_course(course_name)
        elif choice == '3':
            course_name = input("Enter course name: ").strip()
            course = DataManager.get_course_by_name(course_name)
            if course and user.email in course.get('grades', {}):
                print(f"Your grade for {course_name} is: {course['grades'][user.email]}")
            else:
                print("Grade not found for this course.")
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    print("Welcome to the Student Course Management System")
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            role = input("Are you a student or instructor? (s/i): ").strip().lower()
            try:
                if role == 's':
                    user = Student(email, password)
                elif role == 'i':
                    user = Instructor(email, password)
                else:
                    print("Invalid role selection.")
                    continue
            except ValueError as ve:
                print(ve)
                continue
            if user.register():
                print("Registration successful!")
            else:
                print("Registration failed. Email may already be registered.")
        elif choice == '2':
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            user = User.login(email, password)
            if user:
                print("Login successful!")
                if isinstance(user, Student):
                    student_menu(user)
                elif isinstance(user, Instructor):
                    instructor_menu(user)
            else:
                print("Invalid credentials!")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
