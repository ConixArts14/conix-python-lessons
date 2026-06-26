for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")

# Activity 1: Skip multiples of 3
print("\n=== Activity 1: Skip Multiples of 3 ===")
for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)

# Activity 2: Break when reaching limit
print("\n=== Activity 2: Stop at Number ===")
for i in range(1, 50):
    if i > 10:
        break
    if i % 2 == 1:
        print("Odd:", i)

# Activity 3: Filter and print
print("\n=== Activity 3: Numbers Greater Than 5 ===")
for x in range(1, 11):
    if x > 5:
        print(x, "is greater than 5")
