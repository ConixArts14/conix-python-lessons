x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Activity 1: Combining conditions with AND
print("\n=== Activity 1: Combining with AND ===")
age = 16
has_license = True
if age >= 16 and has_license:
    print("You can drive!")
else:
    print("You cannot drive yet.")

license_active = False
if age >= 16 and license_active:
    print("Drive safely!")
else:
    print("Your license is not active.")

# Activity 2: Using OR for multiple conditions
print("\n=== Activity 2: Using OR ===")
day = "Saturday"
is_holiday = False
if day == "Saturday" or day == "Sunday" or is_holiday:
    print("No school today!")
else:
    print("School day!")

weather = "rainy"
if weather == "rainy" or weather == "snowy":
    print("Stay indoors!")
else:
    print("You can go outside!")

# Activity 3: Using NOT to negate conditions
print("\n=== Activity 3: Using NOT ===")
is_student = True
if not is_student:
    print("You must be a student.")
else:
    print("Welcome, student!")

is_blocked = False
if not is_blocked:
    print("Account is active!")
else:
    print("Account is blocked.")
