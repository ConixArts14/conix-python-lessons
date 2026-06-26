def greet(name="Guest"):

    print("Hello,", name)

greet("Conix")   # uses the argument you pass
greet()          # uses the default "Guest"

# Activity 1: Function with default values for numbers
print("\n=== Activity 1: Calculate with Defaults ===")
def power(base, exponent=2):
    result = base ** exponent
    print(str(base) + " to the power of " + str(exponent) + " = " + str(result))

power(5)
power(3, 4)
power(2, 8)

# Activity 2: Greetings with default language
print("\n=== Activity 2: Multilingual Greeting ===")
def greet_formal(name, language="English"):
    if language == "English":
        print("Hello, " + name + "!")
    elif language == "Spanish":
        print("Hola, " + name + "!")
    else:
        print("Greetings, " + name + "!")

greet_formal("Alice")
greet_formal("Jose", "Spanish")
greet_formal("Marco", "Italian")

# Activity 3: Multiple defaults
print("\n=== Activity 3: User Profile ===")
def create_profile(name, age=0, city="Unknown"):
    print("Name: " + name)
    print("Age: " + str(age))
    print("City: " + city)

create_profile("Conix")
create_profile("Luna", 15)
create_profile("Max", 20, "New York")
