positive _ count = 0
negative _ count = 0


print("Enter integers")

    user _ input = input("Enter a number: ")

    try:
        number = int(user _ input)
        if number > 0:
            positive _ count += 1
        el if number < 0:
            negative _count += 1
    except Value  Error:
        print("That's not a valid integer. Please enter a valid number or 'done' to finish.")

print(f" Positive: {positive_  count}")
print(f " Negative : {negative _ count}")
