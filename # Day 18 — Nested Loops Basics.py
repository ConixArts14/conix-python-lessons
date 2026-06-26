# Activity 1: Simple nested loops with conditions
print("=== Activity 1: Grade Check ===")
score = 70
if score >= 90:
    print("Excellent!")
elif score >= 75:
    print("Good job!")
else:
    print("Keep practicing!")

# Activity 2: Nested loop - multiplication table
print("\n=== Activity 2: Multiplication Tables ===")
score = 88

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Activity 3: Nested loops creating a grid pattern
print("\n=== Activity 3: Grid Pattern ===")
for i in range(1, 4):
    for j in range(1, 4):
        print("(" + str(i) + "," + str(j) + ")", end=" ")
    print()

print("\nBonus - Number pyramid:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()