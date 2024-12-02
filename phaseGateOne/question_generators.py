"""
Initialize score to 0 and total questions to 10
ask the user up to 10 question
Generate two random numbers where minuend > subtrahend
Minuend between 10 and 100
Subtrahend must be less than minuend
Display the subtraction problem
Get the user's answer
Check if the answer is correct
Increment score if the answer is correct
Display the final score 


"""
import random

score = 0
total_questions = 10

for i in range(1, total_questions + 1):
   
    minuend = random.randint(10, 100)  
    subtrahend = random.randint(0, minuend - 1) 
    
   
    print(f"Question {i}: {minuend} - {subtrahend} = ?")
    
    user_answer = int(input("Your answer: "))
    
    if user_answer == minuend - subtrahend:
        print("Correct")
        score += 1 
    else:
        print(f"Wrong The correct answer is {minuend - subtrahend}.")
    
    print() 
print(f"final score is: {score}/{total_questions}")
