num = int(input("Enter a number: "))
if num > 0:
    if num < 10:
        print("Positive single-digit number")
    else:
        print("Positive number")
else:
    print("Non-positive number")

# Activity 1: Access level check
print("\n=== Activity 1: Access Level ===")
age = int(input("Enter your age: "))
if age >= 18:
    membership = input("Do you have membership? (yes/no): ")
    if membership == "yes":
        print("Welcome! You have full access.")
    else:
        print("Welcome! But membership required for premium features.")
else:
    print("You are too young to access this service.")

# Activity 2: Grade and GPA requirement
print("\n=== Activity 2: Scholarship Eligibility ===")
final_score = int(input("Enter your final score: "))
if final_score >= 80:
    gpa = float(input("Enter your GPA: "))
    if gpa >= 3.5:
        print("Congratulations! You are eligible for the scholarship.")
    else:
        print("You need a higher GPA for the scholarship.")
else:
    print("You need a higher score to qualify.")

# Activity 3: Login verification
print("\n=== Activity 3: Login System ===")
username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("Username not found!")
