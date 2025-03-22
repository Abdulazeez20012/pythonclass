positive_count = 0
negative_count = 0


print("Enter integers")
user_input = input("Enter a number: ")
try:
        number = int(user_input)
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
except Value  Error:
        print("That's not a valid integer.")

print(f" Positive: {positive_  count}")
print(f " Negative : {negative _ count}")
