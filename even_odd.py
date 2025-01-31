numbers = [1, 2, 3, 6, 8, 10, 1]


odd_count = 0
even_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)
