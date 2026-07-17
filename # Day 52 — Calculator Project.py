# Day 52 — Calculator Project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

# Test
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

# Day 52 - Calculator Project (Activity 2)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def calculator():
    print("=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1-4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."

    if choice == "1":
        return f"Result: {add(num1, num2)}"
    elif choice == "2":
        return f"Result: {subtract(num1, num2)}"
    elif choice == "3":
        return f"Result: {multiply(num1, num2)}"
    elif choice == "4":
        return f"Result: {divide(num1, num2)}"
    else:
        return "Error: Invalid choice."

# Test run
print(calculator())

# Day 52 - Calculator Project (Activity 3)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose operation (1-5): ")

        if choice == "5":
            print("Exiting calculator... Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Error: Invalid choice.")

# Day 52 - Calculator Project (Activity 4)

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        return "Error: Cannot take square root of negative number"

def calculator():
    while True:
        print("\n=== Enhanced Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (a^b)")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Choose operation (1-7): ")

        if choice == "7":
            print("Exiting calculator... Goodbye!")
            break

        try:
            if choice == "6":
                num = float(input("Enter number: "))
                print(f"Result: {square_root(num)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == "1":
                    print(f"Result: {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
                elif choice == "5":
                    print(f"Result: {power(num1, num2)}")
                else:
                    print("Error: Invalid choice.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
