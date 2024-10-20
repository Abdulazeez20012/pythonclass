largest = float('-inf')
smallest = float('inf')

while True:
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != 'y':
        break

print("Largest Number:", largest)
print("Smallest Number:", smallest)
