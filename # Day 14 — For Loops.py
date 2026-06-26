for i in range(1, 6):
    print(i)

# Activity 1: Print multiplication table
print("\n=== Activity 1: Multiplication Table ===")
table_num = 5
for i in range(1, 11):
    result = table_num * i
    print(str(table_num) + " x " + str(i) + " = " + str(result))

# Activity 2: Sum of numbers
print("\n=== Activity 2: Sum of Numbers ===")
sum_total = 0
for num in range(1, 21):
    sum_total += num
print("Sum of 1 to 20:", sum_total)

# Activity 3: Print pattern
print("\n=== Activity 3: Star Pattern ===")
for i in range(1, 6):
    print("*" * i)
