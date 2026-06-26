# Activity 1

colors = ["red", "green", "blue", "yellow"]

for color in colors:
    print("Color is:", color)

# Activity 2

for number in range(1, 6):
    print("Number is:", number)

# Activity 3: Combined list and range operations
print("\n=== Activity 3: List with Index ===")
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits in our collection:")
for i in range(len(fruits)):
    print("Index " + str(i) + ": " + fruits[i])

print("\nMultiplying numbers 1-5 by 2:")
for num in range(1, 6):
    result = num * 2
    print(str(num) + " * 2 = " + str(result))
