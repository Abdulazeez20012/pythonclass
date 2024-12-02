def get_scores_for_subject(subject, student_names):
    scores = {}
    for name in student_names:
        while True:
            try:
                score = int(input(f"Enter the score for {name} in {subject}: "))
                if 0 <= score <= 100:
                    scores[name] = score
                    break
                else:
                    print("Score should be between 0 and 100. Please enter again.")
            except ValueError:
                print("Invalid input. Please enter a valid score (numeric).")
    return scores

def find_best_student(scores):
    best_student = max(scores, key=scores.get)
    return best_student, scores[best_student]
def main():
    student_names = []

    print("Enter the names of 10 students:")
    for i in range(10):
        name = input(f"Enter the name of student {i + 1}: ")
        student_names.append(name)

    subjects = ['java', 'python', 'design_thinking', 'data science']

    best_students = {}  

    for subject in subjects:
        print(f"\nEntering scores for {subject}:")
        scores = get_scores_for_subject(subject, student_names)
        best_student, best_score = find_best_student(scores)
        best_students[subject] = (best_student, best_score)  

    print("\nBest Students in Each Subject:")

    for subject, (best_student, best_score) in best_students.items():
        print(f"The best student in {subject} is {best_student} with a score of {best_score}.")



if __name__ == "__main__":
    main()


