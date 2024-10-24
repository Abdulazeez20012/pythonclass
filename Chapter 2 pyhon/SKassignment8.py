import math

n = int(input("Enter the number of sides (n): "))
s = float(input("Enter the length of each side (s): "))

# Calculate area using formula: (n * s^2) / (4 * tan(π/n))
area = (n * s**2) / (4 * math.tan(math.pi/n))

print(f"The area of the {n}-sided polygon with side length {s} is: {area:.2f}")






