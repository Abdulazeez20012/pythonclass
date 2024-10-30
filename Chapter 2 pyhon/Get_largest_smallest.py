def get_largest_smallest():
    largest = float('-inf')
    smallest = float('inf')

    while True:
        number = float(input("Enter a number: "))

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        response = input("Do you want to continue? (yes/no): ").lower()

        if response != "yes":
            break

    print("Largest number:", largest)
    print("Smallest number:", smallest)

get_largest_smallest()


