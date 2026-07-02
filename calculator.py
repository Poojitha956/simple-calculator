import math

def addition():
    numbers = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, numbers.split()))
    print("Result is:", sum(numbers))

def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result is:", num1 - num2)

def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result is:", num1 * num2)

def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 != 0:
        print("Result is:", num1 / num2)
    else:
        print("Cannot divide by zero")

def power():
    num1 = float(input("Enter base number: "))
    num2 = float(input("Enter exponent: "))
    print("Result is:", num1 ** num2)

def modulus():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 != 0:
        print("Result is:", num1 % num2)
    else:
        print("Cannot divide by zero")

def square_root():
    num = float(input("Enter number: "))

    if num >= 0:
        print("Square root:", math.sqrt(num))
    else:
        print("Square root of a negative number is not possible.")

operation = input("Choose (+, -, *, /, ^, %, sqrt): ")

if operation == "+":
    addition()

elif operation == "-":
    subtraction()

elif operation == "*":
    multiplication()

elif operation == "/":
    division()

elif operation == "^":
    power()

elif operation == "%":
    modulus()

elif operation == "sqrt":
    square_root()

else:
    print("Invalid operation")