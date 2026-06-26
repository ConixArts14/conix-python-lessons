i = 1
while i <= 5:
    print(i)
    i += 1

# Activity 1: Count backwards
print("\n=== Activity 1: Countdown ===")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blastoff!")

# Activity 2: Sum numbers using while loop
print("\n=== Activity 2: Sum Numbers ===")
num = 1
total = 0
while num <= 10:
    total = total + num
    num += 1
print("Sum of 1 to 10:", total)

# Activity 3: User input validation
print("\n=== Activity 3: Password Entry ===")
password = ""
attempts = 0
while password != "python123":
    password = input("Enter password: ")
    attempts += 1
    if password != "python123":
        print("Wrong password. Try again.")
print("Access granted! Attempts:", attempts)
