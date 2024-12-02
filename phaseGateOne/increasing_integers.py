"""
Prompt the user to enter first integers
collect it and store as first_integer
Prompt the user to enter second integer
collect it and store as second_integer
Prompt the user to enter third integer
collect it and store as third_integer
Compare the numbers to sort them in increasing order using the conditional statement

 if first_integer greater than second_integer:
   first_integer, second_integer = second_integer,first_integer
if first_integer greater than third_integer:
    first_integer, third_integer = third_integer,first_integer
if second_integer is greater than  third_integer:
    second_integer, third_integer = third_integer, second_integer

Display the numbers in increasing order
"""
first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))
third_integer = int(input("Enter the third integer: "))

if first_integer > second_integer:
   first_integer, second_integer = second_integer,first_integer
if first_integer > third_integer:
    first_integer, third_integer = third_integer,first_integer
if second_integer > third_integer:
    second_integer, third_integer = third_integer, second_integer

print("The numbers in increasing order are:", first_integer, second_integer, third_integer)
