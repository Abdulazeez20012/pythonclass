first_number = int(input("enter the three number:"))
first_digit = first_number%10
second_digit = (first_number//10) % 10
third_digit = (first_number//100) % 10

print(first_digit , second_digit , third_digit)
print(third_digit , second_digit , first_digit)

if (first_digit % 2) == 0 :
	print(first_digit," is a even number")
else : print(first_digit,"is not a even number")

if (second_digit % 2) == 0 :
print(second_digit," is a even number")
else : print(second_digit,"is not a even number")

if (third_digit % 2) == 0 :
	print(third_digit," is a even number")
else : print(third_digit,"is not a even number")





