
# Activity 1: Countdown using range with step
print("=== Activity 1: Countdown ===")
score = 85

if score >= 75:
    print("You passed the test!")
else:
    print("You need to study more.")

# Counting backwards
for i in range(5, 0, -1):
    print(i)

# Activity 2: Skipping numbers with step
print("\n=== Activity 2: Skipping Every 3rd Number ===")
for i in range(0, 20, 3):
    print(i)

# Even numbers using range
print("\nEven numbers 0-20:")
for i in range(0, 21, 2):
    print(i)

# Activity 3: While loop with custom step
print("\n=== Activity 3: While Loop Decrement ===")
i = 10
while i > 0:
    print(i)
    i -= 2

print("\nBonus - Counting by 5s from 50 down to 0:")
count = 50
while count >= 0:
    print(count, end=" ")
    count -= 5
print()
