numbers = [1, 5, 8, 12, 15, 8]
result = [x for x in numbers if (lambda x: x > 10)(x)]
print(result)




strings = ["madam,"apple","racecar"]
result = [s for s in strings if (lambda s == s[::-1])(s)]
print(result)
