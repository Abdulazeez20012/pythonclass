class Calculator:
    def __init__(self, model, brand, colour):
        self.model = model
        self.brand = brand
        self.colour = colour

    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        if num2 == 0:
            return "SYNTAX ERROR"
        else:
            return num1 / num2

my_calculator = Calculator("2324", "kapa", "black")
print(my_calculator.addition(2, 3))
print(my_calculator.subtraction(2, 3))
print(my_calculator.multiplication(2, 3))
print(my_calculator.division(2, 0))
