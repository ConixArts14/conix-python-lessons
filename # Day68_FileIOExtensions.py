Enter your choice (1-11): 11
--- Students Under 18 ---
Name: Jacob, Age: 10, City: Tagum
Name: Alex, Age: 15, City: Manila
✅ Report saved to student_under18.txt
12. Show Students by City

12. Show Students by City
elif choice == "12":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        city_to_filter = input("Enter the city to filter: ").strip()

        filtered = [student for student in data if student["City"].lower() == city_to_filter.lower()]

        if filtered:
            print(f"\n--- Students from {city_to_filter} ---")
            for student in filtered:
                print(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}")

            filename = f"student_{city_to_filter.lower()}.txt"
            with open(filename, "w") as file:
                for student in filtered:
                    file.write(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}\n")

            print(f"✅ Report saved to {filename}")
        else:
            print(f"⚠️ No students found from {city_to_filter}.")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")
