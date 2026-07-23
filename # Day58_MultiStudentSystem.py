import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def main_menu():
    while True:
        print("\nMulti-Student System Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        print("4. Search Student by ID")
        print("5. Sort Students by Name")

        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            address = input("Enter address: ")
            contact = input("Enter contact number: ")

            students = load_students()
            students.append({
                "id": student_id,
                "name": name,
                "age": age,
                "details": {
                    "address": address,
                    "contact": contact
                }
            })
            save_students(students)
            print("Student added successfully!")

        elif choice == "2":
            students = load_students()
            print("\nAll Students:")
            for s in students:
                print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Address: {s['details']['address']}, Contact: {s['details']['contact']}")

        elif choice == "3":
            print("Exiting program...")
            break

        elif choice == "4":
            students = load_students()
            search_id = input("Enter student ID to search: ")
            for s in students:
                if s["id"] == search_id:
                    print(f"Found: {s['name']}, Age: {s['age']}, Address: {s['details']['address']}, Contact: {s['details']['contact']}")
                    break
            else:
                print("Student not found.")

        elif choice == "5":
            students = load_students()
            sorted_students = sorted(students, key=lambda x: x["name"])
            print("\nStudents Sorted by Name:")
            for s in sorted_students:
                print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")

        else:
            print("Invalid choice, try again.")

main_menu()
