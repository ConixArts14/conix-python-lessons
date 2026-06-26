# Activity 1
a = 100

def test_scope():
    b = 50
    print("Inside function, a:", a)
    print("Inside function, b:", b)

test_scope()
print("Outside function, a:", a)
print("Outside function, b:", b)

# Activity 2
count = 0

def increase():
    global count
    count = count + 1
    print("Inside function, count:", count)

increase()
increase()
print("Outside function, count:", count)
