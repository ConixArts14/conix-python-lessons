score = int(input("Enter your score: "))
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")

# Activity 1: Classify age groups
print("\n=== Activity 1: Age Group Classification ===")
age_input = int(input("Enter your age: "))
if age_input < 13:
    print("You are a child.")
elif age_input < 18:
    print("You are a teenager.")
elif age_input < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Activity 2: Water temperature states
print("\n=== Activity 2: Water Temperature States ===")
temp = int(input("Enter water temperature in Celsius: "))
if temp < 0:
    print("Water is frozen (ice).")
elif temp < 100:
    print("Water is liquid.")
else:
    print("Water is boiling (steam).")

# Activity 3: Speed category
print("\n=== Activity 3: Speed Category ===")
speed = int(input("Enter the speed in km/h: "))
if speed < 40:
    print("Slow speed")
elif speed < 80:
    print("Normal speed")
elif speed < 120:
    print("Fast speed")
else:
    print("Very fast speed")
