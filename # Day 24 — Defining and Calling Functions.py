# Activity 1
def add_numbers():
    a = 5
    b = 7
    print("Sum:", a + b)

add_numbers()

# Activity 2
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)
add_numbers(3, 7)

# Activity 3: Create and call multiple functions
print("\n=== Activity 3: Various Functions ===")
def greet_user(name):
    print("Hello, " + name + "!")

def show_info(name, age):
    print("Name: " + name)
    print("Age: " + str(age))

def farewell():
    print("Goodbye!")

greet_user("Bob")
show_info("Charlie", 15)
farewell()
