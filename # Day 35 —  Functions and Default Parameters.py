# Day 35 - Functions and Default Parameters
# Activity 1: Using Default Parameters

#def greet(name="Guest"):
    #print(f"Hello, {name}!")

# Calling with an argument
#greet("Conix") # prints: Hello, Conix!

# Calling without an argument
#greet()  # prints: Hello, Guest!

# Activity 2: Multiple defult Parameters 

#def welcome(name="Guest", city="Digos"):
    #print(f"Welcome {name} to {city}!")

# Calling with both arguments
#welcome("Conix", "Manila") # prints: Welcome Conix to Manila!

# Calling with one arguments
#welcome("Conix") # prints: Welcome Conix to Digos!

# Calling with no arguments
#welcome() # prints: Welcome Guest to Digos!

# Activity 3: Overriding Default with Keywords

#def welcome(name="Guest", city="Digos"):
    #print(f"Welcome {name} to {city}!")

# Using Keyword arguments
#welcome(city="Cebu")   # prints: Welcome Guest to Cebu!
#welcome(name="conix", city="Tokyo")  # prints: Welcome conix to Tokyo!

# Day 35 - Functions and Defult Parameters
# Activity 4: Defults + Keywords + Returns

def calculate_total(price=100, tax=0.05, discount=0):
    total = price + (price * tax) - discount
    return total

# Using all defults
print(calculate_total())
# Expected: 105.0 (100 + 5% tax)

# Overriding with keywords
print(calculate_total(price=200, tax=0.1))
# Expected: 220.0 (200 + 10% tax)

# Overriding discount only
print(calculate_total(discount=20))
# Expected: 85.0 (100 + 5% tax - 20 discount)