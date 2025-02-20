class Calculator:
     def __init__(self, model, brand,colour):
         self.model = model
         self.brand = brand
         self.colour = colour

     def addition(self,operand1,operand2):
         return operand1 + operand2
     def subtraction(self,operand1,operand2):
         return operand1 - operand2
     def multiplication(self,operand1,operand2):
         return operand1 * operand2
     def division(self,operand1,operand2):
         if operand2 == 0:
             return "Error: division by zero"
         else:
             return operand1 / operand2

calculator = Calculator("fx","Casio","White")
print(calculator.addition(2,3))
print(calculator.division(6,2))