age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Activity 1: Check if a number is positive or negative
print("\n=== Activity 1: Number Classification ===")
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
else:
    if number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Activity 2: Check if student passed or failed
print("\n=== Activity 2: Test Results ===")
score = int(input("Enter your test score: "))
if score >= 70:
    print("You passed the test! Great job!")
else:
    print("You did not pass. Keep trying!")

# Activity 3: Check access level
print("\n=== Activity 3: Access Level ===")
user_age = int(input("What is your age? "))
if user_age >= 13:
    print("You are old enough to access this content.")
else:
    print("You are too young. Come back when you are 13.")
