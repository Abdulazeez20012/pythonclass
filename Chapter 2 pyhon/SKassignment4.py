weight_pounds = float(input("Enter your weight (in pounds): "))
height_inches = float(input("Enter your height (in inches): "))

weight_kg = weight_pounds * 0.45359237
height_meters = height_inches * 0.0254

bmi = weight_kg / (height_meters ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your weight: {weight_kg:.2f} kg")
print(f"Your height: {height_meters:.2f} meters")
print(f"Your BMI: {bmi:.2f}")
print(f"Your BMI category: {category}")


