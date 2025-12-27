
class Calculator:
    def __init__(self):
        print("Welcome to the calculator")
    def calculate(self):
         num1 = int(input("Enter first number: "))
         operator = input("Please select the operator '+', '-', '*', '/' ")
         num2 = int(input("Enter second number: "))

         match operator:
             case "+":
                 print(num1 + num2)
             case "-":
                 print(num1 - num2)
             case "*":
                 print(num1 * num2)
             case "/":
                 print(num1 / num2)
             case _:  # Default case
                 print("invalid operat0r")
calc=Calculator()
calc.calculate()







