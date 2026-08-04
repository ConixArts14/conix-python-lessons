elif choice == "8":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)
            print("\n--- Student Report (from JSON) ---")
            for student in data:
                print(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}")
    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")


9. Update Student Record
elif choice == "9":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        name_to_update = input("Enter the name of the student to update: ").strip()

        found = False
        for student in data:
            if student["Name"].lower() == name_to_update.lower():
                new_age = input("Enter new age (leave blank to keep current): ").strip()
                new_city = input("Enter new city (leave blank to keep current): ").strip()

                if new_age:
                    student["Age"] = int(new_age)
                if new_city:
                    student["City"] = new_city

                found = True
                break

        if found:
            with open("student_report.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"✅ Record for {name_to_update} updated successfully.")
        else:
            print("⚠️ Student not found in report.")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")


10. Delete Student Record
elif choice == "10":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        name_to_delete = input("Enter the name of the student to delete: ").strip()

        new_data = [student for student in data if student["Name"].lower() != name_to_delete.lower()]

        if len(new_data) < len(data):
            with open("student_report.json", "w") as file:
                json.dump(new_data, file, indent=4)
            print(f"🗑️ Record for {name_to_delete} deleted successfully.")
        else:
            print("⚠️ Student not found in report.")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")
