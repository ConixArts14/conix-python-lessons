for i in range(10, 0, -2):
    print("Number:", i)

for i in range(1, 10):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print("Odd number:", i)

# Activity 1: Functions that return values
print("\n=== Activity 1: Simple Return Values ===")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

result1 = add(10, 5)
result2 = subtract(10, 5)
print("10 + 5 = " + str(result1))
print("10 - 5 = " + str(result2))

# Activity 2: Return different types of values
print("\n=== Activity 2: Return Strings and Numbers ===")
def create_message(name, age):
    return name + " is " + str(age) + " years old"

def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

message = create_message("Alice", 12)
discounted = calculate_discount(100, 20)
print(message)
print("Discounted price: $" + str(discounted))

# Activity 3: Multiple return statements
print("\n=== Activity 3: Conditional Returns ===")
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

grade1 = check_grade(95)
grade2 = check_grade(75)
grade3 = check_grade(65)
print("Score 95 = Grade " + grade1)
print("Score 75 = Grade " + grade2)
print("Score 65 = Grade " + grade3)