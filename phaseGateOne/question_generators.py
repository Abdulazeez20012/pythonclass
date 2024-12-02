import random
import time

# Initialize score and total questions
score = 0
total_questions = 10

# Record the start time
start_time = time.time()

# Ask the user up to 10 questions
for i in range(1, total_questions + 1):
    # Generate two random numbers where minuend > subtrahend
    minuend = random.randint(10, 100)  # Minuend between 10 and 100
    subtrahend = random.randint(0, minuend - 1)  # Subtrahend must be less than minuend
    
    # Display the subtraction problem
    print(f"Question {i}: {minuend} - {subtrahend} = ?")
    
    # Get the user's answer
    user_answer = int(input("Your answer: "))
    
    # Check if the answer is correct
    if user_answer == minuend - subtrahend:
        print("Correct!")
        score += 1  # Increment score if the answer is correct
    else:
        print(f"Wrong! The correct answer is {minuend - subtrahend}.")
    
    print()  # Print a blank line for readability

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Display the final score and the time taken
print(f"Your final score is: {score}/{total_questions}")
print(f"Time taken: {total_time:.2f} seconds")
