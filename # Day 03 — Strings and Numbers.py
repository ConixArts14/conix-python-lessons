# Day 3 review: strings and numbers
# Strings are text, numbers are values we can do math with

name = "Conix"
age = 10
favorite_language = "Python"

print(name)
print(age)
print(favorite_language)

print("My name is " + name)
print("I am " + str(age) + " years old")
print("I am learning " + favorite_language)

# Activity 1: Work with string and number conversions
print("\n=== Activity 1: String and Number Conversions ===")
student_name = "Alice"
student_age = 12
points = 350
print("Student: " + student_name)
print("Age: " + str(student_age))
print("Points earned: " + str(points))
print(student_name + " is " + str(student_age) + " years old with " + str(points) + " points!")

# Activity 2: Combine multiple strings and numbers
print("\n=== Activity 2: Game Stats ===")
player = "Hero"
health = 100
level = 5
experience = 2500
print("Player: " + player)
print("Health: " + str(health))
print("Level: " + str(level))
print("Experience: " + str(experience))

# Activity 3: Create a profile card
print("\n=== Activity 3: Profile Card ===")
profile_name = "Jordan"
profile_age = 14
favorite_book = "Python Adventure"
rating = 5
print("Name: " + profile_name)
print("Age: " + str(profile_age))
print("Favorite Book: " + favorite_book)
print("Rating: " + str(rating) + "/5")
print("Profile: " + profile_name + ", age " + str(profile_age) + ", loves " + favorite_book)