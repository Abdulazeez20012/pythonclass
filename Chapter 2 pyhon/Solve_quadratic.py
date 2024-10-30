import math

def solve_quadratic(a, b, c):
    determinant = b**2 - 4*a*c

    if determinant > 0:
        root1 = (-b + math.sqrt(determinant)) / (2*a)
        root2 = (-b - math.sqrt(determinant)) / (2*a)
        return f"Roots are real and distinct.\nRoot 1: {root1}\nRoot 2: {root2}"
    elif determinant == 0:
        root = -b / (2*a)
        return f"Roots are real and equal.\nRoot: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-determinant) / (2*a)
        return f"Roots are complex.\nRoot 1: {real_part} + {imaginary_part}i\nRoot 2: {real_part} - {imaginary_part}i"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

print(solve_quadratic(a, b, c))


