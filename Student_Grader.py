def get_scores_for_subject(subject, student_names):
    scores = {}
    for name in student_names:
 
        while True:
            try:
                score = float(input(f"Enter the score for {name} in {subject}: "))
                if 0 <= score <= 100:
                    scores[name] = score
                    break
                else:
                    print("Score should be between 0 and 100. Please enter again.")
            except ValueError:
                print("Invalid input. Please enter a valid score (numeric).")
    return scores



