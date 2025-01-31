School_records = {
    "class_1": {
        "students": [
            {"name": "Harry", "scores": {"Math": 88, "English": 76}},
            {"name": "Solomon", "scores": {"Math": 95, "English": 89}},
        ]
    },
    "class_2": {
        "students": [
            {"name": "Daniel", "scores": {"Math": 78, "English": 72}},
            {"name": "Samuel", "scores": {"Math": 85, "English": 80}},
        ]
    }
}


for class_name, class_2 in School_records.items():
    for student in class_2["students"]:
        if student["name"] == "Samuel":
            print(student)


total_maths_score = 0
total_students = 0

for class_1, class_2 in School_records.items():
    for student in class_2["students"]:
        total_maths_score += student["scores"]["Math"]
        total_students += 1




average_maths_score = total_maths_score / total_students
print(f"The average Math score of all students is: {average_maths_score:}")


































