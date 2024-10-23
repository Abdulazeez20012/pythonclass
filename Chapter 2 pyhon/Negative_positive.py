negative_count = 0
positive_count = 0
zero_count = 0

for i in range(5):
    num = float(input(f"Please enter number {i+1}: "))

    if num < 0:
        negative_count += 1
    elif num > 0:
        positive_count += 1
    else:
        zero_count += 1

print("\nResults:")
print(f"Negative numbers: {negative_count}")
print(f"Positive numbers: {positive_count}")
print(f"Zeros: {zero_count}")

