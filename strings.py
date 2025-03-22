strings = ["madam,"apple","racecar"]
result = [s for s in strings if (lambda s == s[::-1])(s)]
print(result)
writev a  programme in python that takes out numbers in a list were letters number are in forloop using lambda