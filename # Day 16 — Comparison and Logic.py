a = 12
b = 15

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Activity 1: Combine comparison and conditional
print("\n=== Activity 1: Score Range Check ===")
score = 85
if score >= 80 and score <= 100:
    print("Excellent performance!")
elif score >= 60 and score < 80:
    print("Good performance!")
else:
    print("Needs improvement!")

# Activity 2: Using multiple conditions
print("\n=== Activity 2: Age and Membership ===")
age = 25
has_membership = True
if age >= 18 and has_membership:
    print("You have full access!")
elif age >= 18:
    print("You need membership for full access.")
else:
    print("Too young to access.")

# Activity 3: Complex logical conditions
print("\n=== Activity 3: Weekend Check ===")
day = "Saturday"
temperature = 25
if (day == "Saturday" or day == "Sunday") and temperature > 20:
    print("Perfect day for outdoor activities!")