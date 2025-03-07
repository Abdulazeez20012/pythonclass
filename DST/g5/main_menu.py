from DST.g5.student_management import StudentManagement
from DST.g5.student import Student
from DST.g5.professor import Professor
from DST.g5.exceptions import UserNotFoundException, CourseNotFoundException, GradeOutOfRangeException

class InvalidMenuChoice(Exception):
    pass

def get_valid_input(prompt, error_message):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print(error_message)

def print_menu():
    print("\n---WELCOME TO MEA PROGRAMMING INSTITUTE---")
    print("\nWhere Passion for Code Transforms into Innovation.")
    print("\n--- Main Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Login")
    print("4. Create Course")
    print("5. Enroll Student in Course")
    print("6. Assign Grade")
    print("7. View User Details")
    print("8. View All Registered Students")
    print("9. Exit")

def main():
    mgmt = StudentManagement()
    logged_in_user = None

    while True:
        try:
            print_menu()
            choice = get_valid_input("Enter your choice (1-9): ", "Invalid menu option. Please select a valid option (1-9).")

            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                raise InvalidMenuChoice("Invalid menu option. Please select a valid option (1-9).")

            if choice == '1':
                print("\n-- Register Student --")
                email = get_valid_input("Email: ", "Email cannot be empty.")
                password = get_valid_input("Password: ", "Password cannot be empty.")
                name = get_valid_input("Name: ", "Name cannot be empty.")
                student_id = get_valid_input("Student ID: ", "Student ID cannot be empty.")
                student = Student(email, password, name, student_id)
                mgmt.register_user(student)
                print("Student", name, "registered successfully.")

            elif choice == '2':
                print("\n-- Register Professor --")
                email = get_valid_input("Email: ", "Email cannot be empty.")
                password = get_valid_input("Password: ", "Password cannot be empty.")
                name = get_valid_input("Name: ", "Name cannot be empty.")
                professor_id = get_valid_input("Professor ID: ", "Professor ID cannot be empty.")
                professor = Professor(email, password, name, professor_id)
                mgmt.register_user(professor)
                print("Professor", name, "registered successfully.")

            elif choice == '3':
                print("\n-- Login --")
                email = get_valid_input("Email: ", "Email cannot be empty.")
                password = get_valid_input("Password: ", "Password cannot be empty.")
                try:
                    logged_in_user = mgmt.login_user(email, password)
                    print("Login successful. Welcome,", logged_in_user.name + "!")
                except UserNotFoundException as e:
                    print("Error:", e)

            elif choice == '4':
                print("\n-- Create Course --")
                if logged_in_user is None or not hasattr(logged_in_user, 'professor_id'):
                    print("Only a logged-in professor can create a course.")
                else:
                    course_id = get_valid_input("Course ID: ", "C ourse ID cannot be empty.")
                    course_name = get_valid_input("Course Name: ", "Course Name cannot be empty.")
                    try:
                        mgmt.create_course(course_id, course_name, logged_in_user.email)
                        print("Course", course_name, "created successfully.")
                    except UserNotFoundException as e:
                        print("Error:", e)

            elif choice == '5':
                print("\n-- Enroll Student in Course --")
                student_email = get_valid_input("Student Email: ", "Student Email cannot be empty.")
                course_id = get_valid_input("Course ID: ", "Course ID cannot be empty.")
                try:
                    mgmt.enroll_student_in_course(student_email, course_id)
                    print("Student", student_email, "enrolled in course", course_id, "successfully.")
                except (UserNotFoundException, CourseNotFoundException) as e:
                    print("Error:", e)

            elif choice == '6':
                print("\n-- Assign Grade --")
                if logged_in_user is None or not hasattr(logged_in_user, 'professor_id'):
                    print("Only a logged-in professor can assign grades.")
                else:
                    student_email = get_valid_input("Student Email: ", "Student Email cannot be empty.")
                    course_id = get_valid_input("Course ID: ", "Course ID cannot be empty.")
                    while True:
                        try:
                            numeric_grade = float(get_valid_input("Numeric Grade (0-100): ", "Grade must be a number."))
                            if numeric_grade < 0 or numeric_grade > 100:
                                raise GradeOutOfRangeException("Grade must be between 0 and 100.")
                            mgmt.assign_grade(logged_in_user.email, student_email, course_id, numeric_grade)
                            break
                        except ValueError:
                            print("Please enter a valid number for the grade.")
                        except GradeOutOfRangeException as e:
                            print("Error:", e)

            elif choice == '7':
                print("\n-- View User Details --")
                email = get_valid_input("Enter user email to view details: ", "Email cannot be empty.")
                found = next((user for user in mgmt.users if user.email == email), None)
                if found:
                    print("Name:", found.name, "| Email:", found.email)
                else:
                    print("User not found.")

            elif choice == '8':
                print("\n-- All Registered Students --")
                students = [user for user in mgmt.users if hasattr(user, 'student_id')]
                if students:
                    for student in students:
                        print("Name:", student.name, "| Email:", student.email, "| Student ID:", student.student_id)
                else:
                    print("No students have been registered yet.")

            elif choice == '9':
                print("Exiting... Goodbye!")
                break
        except InvalidMenuChoice as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
