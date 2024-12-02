def enter_grades_for_students(subjects, students):
    grades = {} 
    for subject in subjects:
        subject_grades = {}
        print(f"Enter grades for {subject}:")
        for student in students:
            grade = input(f"Grade for {student}: ")
            subject_grades[student] = grade
        grades[subject] = subject_grades
    return grades

def print_grades(grades, subjects):
    for subject in subjects:
        print(f"\nGrades for {subject}:")
        for student, grade in grades[subject].items():
            print(f"{student}: {grade}")


	
