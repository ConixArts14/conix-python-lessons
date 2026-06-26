# Activity 1
for x in range(1, 4):
    for y in range(1, 3):
        print("x =", x, "y =", y)

# Activity 2
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)

# Activity 3: Create patterns with nested loops
print("\n=== Activity 3: Pattern Creation ===")
print("Star Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\nNumber Triangle:")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
