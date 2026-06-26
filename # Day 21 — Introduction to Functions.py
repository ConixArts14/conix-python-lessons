count = 1

while count <= 5:
    print("Loop number:", count)
    count = count + 1

# Activity 1: Simple greeting function
print("\n=== Activity 1: Simple Greeting ===")
def say_hello():
    print("Hello from a function!")

say_hello()

# Activity 2: Function that does calculation
print("\n=== Activity 2: Calculate Double ===")
def double_number():
    num = 10
    result = num * 2
    print("Double of 10 is:", result)

double_number()

# Activity 3: Reusable function
print("\n=== Activity 3: Reusable Pattern ===")
def print_stars():
    print("*" * 10)

print_stars()
print_stars()
print_stars()
