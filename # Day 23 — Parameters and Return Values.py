for i in range(10, 0, -2):
    print("Number:", i)

for i in range(1, 10):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print("Odd number:", i)

