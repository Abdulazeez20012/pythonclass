def compare_floats(num1, num2):
    return round(num1, 3) == round(num2, 3)

num1 = float(input("Enter first floating-point number: "))
num2 = float(input("Enter second floating-point number: "))

if compare_floats(num1, num2):
    print(f"{num1} and {num2} are the same up to three decimal places.")
else:
    print(f"{num1} and {num2} are not the same up to three decimal places.")


