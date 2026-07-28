import json

with open("students.json", "r") as file:
    data = json.load(file)
name_to_search = input("Enter student name: ")

found = False
for student in data:
    if student["Name"].lower() == name_to_search.lower():
        print("Student found:", student)
        found = True
        break

if not found:
    print("No student found with that name.")



age_limit = int(input("Enter age limit: "))
for student in data:
    if student["Age"] >= age_limit:
        print(student)
city_to_search = input("Enter city: ")
for student in data:
    if student["City"].lower() == city_to_search.lower():
        print(student)


name_to_update = input("Enter student name to update: ")
new_age = int(input("Enter new age: "))
new_city = input("Enter new city: ")

for student in data:
    if student["Name"].lower() == name_to_update.lower():
        student["Age"] = new_age
        student["City"] = new_city
        print("Student updated:", student)

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
name_to_delete = input("Enter student name to delete: ")
data = [student for student in data if student["Name"].lower() != name_to_delete.lower()]

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("Student deleted if found.")


try:
    with open("students.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: students.json not found.")
try:
    age_limit = int(input("Enter age limit: "))
except ValueError as e:
    with open("error_log.txt", "a") as log:
        log.write(f"ValueError: {e}\n")
    print("Invalid input. Please enter a number.")
