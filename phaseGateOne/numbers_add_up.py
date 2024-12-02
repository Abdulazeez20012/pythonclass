"""
prompt the user to enter a number between one and 100 
collect the number and store it as number_one 
prompt the user to enter another number between one and 100
collect the number and store the number as number_two 
prompt the user again to enter the sum of both numbers  that was entered 
input the correct answer by adding the number_one and number_two together 
and check or dtermine if user_answer is equal to correct_answer 
if it is equal print true b
if not equal print false 
"""
number_one = int(input("Enter a number between 1 and 100:  "))
number_two = int(input("Enter a number between 1 and 100:  "))

user_answer = int(input(f"What is the sum of {number_one} and {number_two}? "))

correct_answer = number_one + number_two


if user_answer == correct_answer:
    print("True")
else:
    print("False")
