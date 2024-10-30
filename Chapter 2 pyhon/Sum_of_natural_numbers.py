def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = 10
print("Sum of first", n, "natural numbers:", sum_of_natural_numbers(n))
