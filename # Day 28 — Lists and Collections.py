fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[2])
print("All fruits:", fruits)

colors = ["red", "green", "blue"]
print("Original list:", colors)

colors.append("yellow")
print("After append:", colors)

colors.remove("green")
print("After remove:", colors)

# Activity 1: Create and modify a shopping list
print("\n=== Activity 1: Shopping List ===")
shopping_list = ["milk", "bread", "eggs"]
print("Original shopping list:", shopping_list)
shopping_list.append("cheese")
shopping_list.append("butter")
print("After adding items:", shopping_list)
shopping_list.remove("bread")
print("After removing bread:", shopping_list)

# Activity 2: Student grades list
print("\n=== Activity 2: Student Grades ===")
grades = [95, 87, 92, 88, 91]
print("All grades:", grades)
print("First grade:", grades[0])
print("Last grade:", grades[-1])
print("First three grades:", grades[0:3])
grades.append(89)
print("After adding new grade:", grades)

# Activity 3: Mixed list operations
print("\n=== Activity 3: Book Collection ===")
books = ["Python 101", "Web Development", "Data Science"]
print("Original collection:", books)
books.append("Game Development")
books.insert(1, "Mobile Apps")
print("After insertions:", books)
print("Number of books:", len(books))
print("First book:", books[0])
print("Last book:", books[-1])