# Activity 1: Comprehensive review - User validation
print("=== Activity 1: User Registration System ===")
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

if len(username) >= 3 and len(password) >= 6 and age >= 13:
    print("Account created successfully!")
else:
    if len(username) < 3:
        print("Username must be at least 3 characters.")
    if len(password) < 6:
        print("Password must be at least 6 characters.")
    if age < 13:
        print("You must be 13 years old.")

# Activity 2: Review - Grade calculator with loops
print("\n=== Activity 2: Grade Calculator ===")
scores = []
for i in range(1, 4):
    score = int(input("Enter score " + str(i) + ": "))
    scores.append(score)

average = sum(scores) / len(scores)
print("Average score: " + str(average))

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade: " + grade)

# Activity 3: Master challenge - Game system
print("\n=== Activity 3: Number Guessing Game ===")
secret = 7
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    
    if guess == secret:
        print("Correct! You guessed it in " + str(attempts) + " attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempts >= 5:
        print("Game over! The number was " + str(secret))
        break