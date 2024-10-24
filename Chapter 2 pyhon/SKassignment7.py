binary = input("Enter a binary number: ")

while not set(binary).issubset({"0", "1"}):
    print("Invalid binary number. Please try again.")
    binary = input("Enter a binary number: ")

decimal = int(binary, 2)

print(f"The decimal representation of {binary} is: {decimal}")





