Student_Scores = {
    'Gloria': 88,
    'Divine': 78,
    'Esther': 65,
    'Mercy': 75,
    'Uzo': 71
}

student_grades = {}

for student, score in Student_Scores.items():
    if score  >=90 :
        grade = "Outstanding"
    elif score >= 80:
        grade = "Exceeds Expectation"
    elif score >= 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    
    student_grades[student] = grade

print(student_grades)
