import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Sine")
print("6. Cosine")
print("7. Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
    elif choice in ('5', '6', '7'):
        num = float(input("Enter angle in radian: "))

        if choice == '5':
            print("sin(", num, ") =", sine(num))

        elif choice == '6':
            print("cos(", num, ") =", cosine(num))

        elif choice == '7':
            print("tan(", num, ") =", tangent(num))
    else:
        print("Invalid Input")
