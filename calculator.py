import math

def addition():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    print("Result is:", sum(numbers))

def subtraction():
    numbers = list(map(float, input("Enter two numbers separated by spaces: ").split()))
    print("Result is:", numbers[0] - numbers[1])

def multiplication():
    numbers = list(map(float, input("Enter two numbers separated by spaces: ").split()))
    print("Result is:", numbers[0] * numbers[1])

def division():
    numbers = list(map(float, input("Enter two numbers separated by spaces: ").split()))
    if numbers[1] != 0:
        print("Result is:", numbers[0] / numbers[1])
    else:
        print("Cannot divide by zero")

def power():
    numbers = list(map(float, input("Enter base and exponent separated by spaces: ").split()))
    print("Result is:", numbers[0] ** numbers[1])

def modulus():
    numbers = list(map(float, input("Enter two numbers separated by spaces: ").split()))
    if numbers[1] != 0:
        print("Result is:", numbers[0] % numbers[1])
    else:
        print("Cannot divide by zero")

def square_root():
    numbers = list(map(float, input("Enter one number: ").split()))
    if numbers[0] >= 0:
        print("Square root:", math.sqrt(numbers[0]))
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