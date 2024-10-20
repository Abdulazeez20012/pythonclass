def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

print(base, "raised to the power of", exponent, "is:", calculate_power(base, exponent))
