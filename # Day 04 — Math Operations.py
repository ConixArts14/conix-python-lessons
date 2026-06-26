# Day 4 review: Python math
# Math operations: addition, subtraction, multiplication, division

coins = 10
bonus = 5
score = 20

print("Math Practice")
print(coins + bonus)
print(coins - bonus)
print(coins * bonus)
print(coins / bonus)

score = score + 10
print(score)

# Activity 1: Calculate total points and health
print("\n=== Activity 1: Game Points ===")
initial_points = 100
points_earned = 35
points_lost = 10
total_points = initial_points + points_earned - points_lost
print("Initial Points: " + str(initial_points))
print("Points Earned: " + str(points_earned))
print("Points Lost: " + str(points_lost))
print("Total Points: " + str(total_points))

# Activity 2: Calculate area and dimensions
print("\n=== Activity 2: Geometry Calculations ===")
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Rectangle Length: " + str(length))
print("Rectangle Width: " + str(width))
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))

# Activity 3: Money calculations
print("\n=== Activity 3: Shopping Budget ===")
item1_price = 25
item2_price = 15
item3_price = 30
total_cost = item1_price + item2_price + item3_price
average_price = total_cost / 3
print("Item 1: $" + str(item1_price))
print("Item 2: $" + str(item2_price))
print("Item 3: $" + str(item3_price))
print("Total Cost: $" + str(total_cost))
print("Average Price: $" + str(average_price))