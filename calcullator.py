print("Welcome to the calculator")
num1 = int(input("Enter first number: "))
operator = input("Please select the operator '+', '-', '*', '/' ")
num2 = int(input("Enter second number: "))

def calc(num1, num2, operator):
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
            print("invalid operator")



calc(num1, num2, operator)

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")