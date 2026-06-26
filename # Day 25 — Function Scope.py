# Activity 1
def multiply(a, b):
    return a * b

x = multiply(4, 3)
y = multiply(2, 6)
print("x:", x)
print("y:", y)
print("Total:", x + y)

# Activity 2
def square(x):
    return x * x

a = square(5)
b = square(8)
print("a:", a)
print("b:", b)
print("Sum of squares:", a + b)

# Activity 3: Working with local and return values
print("\n=== Activity 3: Function Return Practice ===")
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = 10
width = 5
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print("Rectangle dimensions: " + str(length) + " x " + str(width))
print("Area: " + str(area))
print("Perimeter: " + str(perimeter))
