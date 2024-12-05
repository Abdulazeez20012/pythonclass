def get_student_scores(num_students, num_subjects):
    
    scores = []
    totals = []
    averages = []

  
    subject_totals = [0] * num_subjects
    subject_passes = [0] * num_subjects
    subject_fails = [0] * num_subjects
    subject_highest = [-1] * num_subjects
    subject_lowest = [-1] * num_subjects

  
    for i in range(num_students):
        student_scores = []
        total_score = 0
        print(f"Enter scores for student {i + 1}")

        for j in range(num_subjects):
            while True:
                score = int(input(f"Enter score for subject {j + 1}: "))
                if 0 <= score <= 100:
                    student_scores.append(score)
                    total_score += score

                  
                    subject_totals[j] += score
                    if score >= 50:
                        subject_passes[j] += 1
                    else:
                        subject_fails[j] += 1

                  
                    if subject_highest[j] == -1 or score > scores[subject_highest[j]][j]:
                        subject_highest[j] = i
                    if subject_lowest[j] == -1 or score < scores[subject_lowest[j]][j]:
                        subject_lowest[j] = i
                    break
                else:
                    print("Invalid score. Score must be between 0 and 100.")

        scores.append(student_scores)
        totals.append(total_score)
        averages.append(total_score / num_subjects)

    return scores, totals, averages, subject_totals, subject_passes, subject_fails, subject_highest, subject_lowest


def display_student_summary(scores, totals, averages, num_subjects):
    print("\nStudent \t" + "\t".join([f"Sub{i + 1}" for i in range(num_subjects)]) + "\tTot \tAve \tPos")
    for i in range(len(scores)):
        print(f"Student{i + 1}\t" + "\t".join(map(str, scores[i])) + f"\t{totals[i]}\t{averages[i]:.2f}\t{i + 1}")


def subject_summary(scores, subject_totals, subject_passes, subject_fails, subject_highest, subject_lowest, num_subjects):
    for j in range(num_subjects):
        highest_score = scores[subject_highest[j]][j]
        lowest_score = scores[subject_lowest[j]][j]
        total_score = subject_totals[j]
        average_score = total_score / len(scores)

        print(f"\nSubject {j + 1}")
        print(f"Highest scoring student is: Student {subject_highest[j] + 1} scoring {highest_score}")
        print(f"Lowest scoring student is: Student {subject_lowest[j] + 1} scoring {lowest_score}")
        print(f"Total score is: {total_score}")
        print(f"Average score is: {average_score:.2f}")
        print(f"Number of passes: {subject_passes[j]}")
        print(f"Number of fails: {subject_fails[j]}")


def class_summary(totals, num_students):
    class_total_score = sum(totals)
    class_average_score = class_total_score / num_students
    best_student_index = totals.index(max(totals))
    worst_student_index = totals.index(min(totals))

    print(f"\nClass Total Score: {class_total_score}")
    print(f"Class Average Score: {class_average_score:.2f}")
    print(f"\nBest Graduating Student is: Student {best_student_index + 1} scoring {totals[best_student_index]}")
    print(f"Worst Graduating Student is: Student {worst_student_index + 1} scoring {totals[worst_student_index]}")


def main():
   
    num_students = int(input("How many students do you have? "))
    num_subjects = int(input("How many subjects do they offer? "))

    
    scores, totals, averages, subject_totals, subject_passes, subject_fails, subject_highest, subject_lowest = get_student_scores(num_students, num_subjects)

    
    print("\nSaving >>>>>>>>>>>>>>>>>>>>>>>>\nSaved Successfully.")
    
    
    display_student_summary(scores, totals, averages, num_subjects)

    
    subject_summary(scores, subject_totals, subject_passes, subject_fails, subject_highest, subject_lowest, num_subjects)

    
    class_summary(totals, num_students)


if __name__ == "__main__":
    main()
