# Activity 4: Multiple Functions Together
def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("Multiply 3 and 4:", multiply(3, 4))
print("Divide 10 by 2:", divide(10, 2))
print("Divide 5 by 0:", divide(5, 0))



