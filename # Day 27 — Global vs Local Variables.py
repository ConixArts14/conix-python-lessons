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

# Activity 3: Global and local variable interactions
print("\n=== Activity 3: Score Tracker ===")
total_score = 0

def add_points(points):
    global total_score
    total_score = total_score + points
    print("Points added: " + str(points))
    print("Total score: " + str(total_score))

def display_score():
    print("Current total: " + str(total_score))

add_points(10)
add_points(20)
display_score()
add_points(15)
display_score()
