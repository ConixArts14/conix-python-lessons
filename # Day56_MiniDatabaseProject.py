import json

def load_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)

def main_menu():
    while True:
        print("\nMini Database Menu")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            records = load_records()
            records.append({"name": name, "age": age})
            save_records(records)
            print("Record added successfully!")
        elif choice == "2":
            records = load_records()
            print("\nAll Records:")
            for r in records:
                print(r)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")


    print("Record deleted successfully!")

import json

def load_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)

def main_menu():
    while True:
        print("\nMini Database Menu")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")
        print("4. Update Record")
        print("5. Delete Record")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            records = load_records()
            records.append({"name": name, "age": age})
            save_records(records)
            print("Record added successfully!")

        elif choice == "2":
            records = load_records()
            print("\nAll Records:")
            for r in records:
                print(r)

        elif choice == "3":
            print("Exiting program...")
            break

        elif choice == "4":
            records = load_records()
            name = input("Enter the name to update: ")
            for r in records:
                if r["name"] == name:
                    new_age = input("Enter new age: ")
                    r["age"] = new_age
                    save_records(records)
                    print("Record updated successfully!")
                    break
            else:
                print("Record not found.")

        elif choice == "5":
            records = load_records()
            name = input("Enter the name to delete: ")
            records = [r for r in records if r["name"] != name]
            save_records(records)
            print("Record deleted successfully!")

        else:
            print("Invalid choice, try again.")

main_menu()
