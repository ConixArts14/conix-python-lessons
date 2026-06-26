# Day 8 — If Else with Numbers

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Activity 1: Check temperature
print("\n=== Activity 1: Temperature Check ===")
temperature = int(input("What is the temperature in Celsius? "))
if temperature > 25:
    print("It's hot! Wear light clothes.")
else:
    print("It's cool. You might need a jacket.")

# Activity 2: Divide numbers evenly
print("\n=== Activity 2: Divisibility Test ===")
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
if first_num % second_num == 0:
    print(str(first_num) + " is divisible by " + str(second_num))
else:
    print(str(first_num) + " is NOT divisible by " + str(second_num))

# Activity 3: Grade based on score
print("\n=== Activity 3: Pass or Fail ===")
quiz_score = int(input("Enter your quiz score (0-100): "))
if quiz_score >= 60:
    print("You passed the quiz!")
else:
    print("You failed. Try again next time.")
