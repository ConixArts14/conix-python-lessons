import json

def load_records():
    try:
        with open("nested_records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_records(records):
    with open("nested_records.json", "w") as file:
        json.dump(records, file, indent=4)

def main_menu():
    while True:
        print("\nNested Database Menu")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            address = input("Enter address: ")
            contact = input("Enter contact number: ")

            records = load_records()
            records.append({
                "name": name,
                "age": age,
                "details": {
                    "address": address,
                    "contact": contact
                }
            })
            save_records(records)
            print("Record added successfully!")

        elif choice == "2":
            records = load_records()
            print("\nAll Records:")
            for r in records:
                print(f"Name: {r['name']}, Age: {r['age']}, Address: {r['details']['address']}, Contact: {r['details']['contact']}")

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

main_menu()

print("4. Update Record")
elif choice == "4":
    records = load_records()
    name = input("Enter the name to update: ")
    for r in records:
        if r["name"] == name:
            new_age = input("Enter new age: ")
            new_address = input("Enter new address: ")
            new_contact = input("Enter new contact number: ")
            r["age"] = new_age
            r["details"]["address"] = new_address
            r["details"]["contact"] = new_contact
            save_records(records)
            print("Record updated successfully!")
            break
    else:
        print("Record not found.")
print("5. Delete Record")
elif choice == "5":
    records = load_records()
    name = input("Enter the name to delete: ")
    records = [r for r in records if r["name"] != name]
    save_records(records)
    print("Record deleted successfully!")
