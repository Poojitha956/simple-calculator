import math
operation = input("Choose (+, -, *, /, ^, sqrt): ")
if operation == "sqrt":
    num = float(input("Enter number: "))
    print("Square root:", math.sqrt(num))
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        print("Result is: ", num1 + num2)
    elif operation == "-":
        print("Result is: ", num1 - num2)
    elif operation == "*":
        print("Result is: ", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Result is: ", num1 / num2)
        else:
            print("Cannot divide by zero")
    elif operation == "^":
        print("Result is: ", num1 ** num2)
    else:
        print("Invalid operation")

