import random

print("Guess a number between 1 and 100!")

random_number = random.randint(1, 100)
attempts = 0

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess < random_number:
        print("Too low, try again!")
    elif user_guess > random_number:
        print("Too high, try again!")
    else:
        print(f"Congratulations! You found the number in {attempts} attempts.")
        break



