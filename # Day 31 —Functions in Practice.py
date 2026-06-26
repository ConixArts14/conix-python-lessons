# Activity 1: Basic arithmetic functions
print("=== Activity 1: Arithmetic Functions ===")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Add 5 + 3 =", add(5, 3))
print("Subtract 10 - 4 =", subtract(10, 4))

# Activity 2: String manipulation functions
print("\n=== Activity 2: String Functions ===")
def create_greeting(name):
    return "Hello, " + name + "!"

def repeat_text(text, times):
    return text * times

greeting = create_greeting("Conix")
print(greeting)
print(repeat_text("Ha", 3))

# Activity 3: Multiple Functions Together
print("\n=== Activity 3: Calculator System ===")
def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def power(base, exponent):
    return base ** exponent

print("Multiply 3 and 4:", multiply(3, 4))
print("Divide 10 by 2:", divide(10, 2))
print("Divide 5 by 0:", divide(5, 0))
print("2 to the power of 5:", power(2, 5))



