
for i in range(0, 20, 3):
    print("Skip count:", i)

# Activity 1: Function with parameters
print("\n=== Activity 1: Greet with Name ===")
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
greet("Charlie")

# Activity 2: Function with multiple parameters
print("\n=== Activity 2: Add Two Numbers ===")
def add(x, y):
    sum_result = x + y
    print(str(x) + " + " + str(y) + " = " + str(sum_result))

add(5, 3)
add(20, 10)
add(100, 50)

# Activity 3: Function with different operations
print("\n=== Activity 3: Basic Operations ===")
def subtract(a, b):
    print(str(a) + " - " + str(b) + " = " + str(a - b))

def multiply(a, b):
    print(str(a) + " * " + str(b) + " = " + str(a * b))

subtract(10, 3)
multiply(4, 5)