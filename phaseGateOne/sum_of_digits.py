"""
Prompt the user to enter an integer between 0 and 1000
collect it and store it as number 
Check if the number is in the valid range(0-1000)
Loop through each digit in the number
Add the last digit to the sum
Remove the last digit from the number
Display the sum of the digits
"""
number = int(input("Enter an integer between 0 and 1000: "))
if 0 <= number <= 1000:
    sum_of_digits = 0

    while number > 0:
       
        sum_of_digits += number % 10
       
        number = number // 10


    print("The sum of the digits is:", sum_of_digits)
else:
    print("Please enter a number between 0 and 1000.")
