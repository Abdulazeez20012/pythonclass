def add_numbers():
while True:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
      print("Sum:", sum)

  repeat = input("Do you want to repeat? (y/n): ")
   if repeat.lower() != 'y':
   break

add_numbers()

