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

13. Show Students Under 18 from a Specific City
elif choice == "13":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        city_to_filter = input("Enter the city to filter: ").strip()

        filtered = [
            student for student in data
            if student["Age"] < 18 and student["City"].lower() == city_to_filter.lower()
        ]

        if filtered:
            print(f"\n--- Students under 18 from {city_to_filter} ---")
            for student in filtered:
                print(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}")

            filename = f"student_under18_{city_to_filter.lower()}.txt"
            with open(filename, "w") as file:
                for student in filtered:
                    file.write(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}\n")

            print(f"✅ Report saved to {filename}")
        else:
            print(f"⚠️ No students under 18 found from {city_to_filter}.")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")

14. Export All Status Reports
elif choice == "14":
    import json
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        # Export students under 18
        under18 = [s for s in data if s["Age"] < 18]
        with open("student_under18.txt", "w") as file:
            for s in under18:
                file.write(f"Name: {s['Name']}, Age: {s['Age']}, City: {s['City']}\n")

        # Export students by city
        cities = set([s["City"].lower() for s in data])
        for city in cities:
            city_students = [s for s in data if s["City"].lower() == city]
            filename = f"student_{city}.txt"
            with open(filename, "w") as file:
                for s in city_students:
                    file.write(f"Name: {s['Name']}, Age: {s['Age']}, City: {s['City']}\n")

        # Export students under 18 by city
        for city in cities:
            city_under18 = [s for s in data if s["Age"] < 18 and s["City"].lower() == city]
            if city_under18:
                filename = f"student_under18_{city}.txt"
                with open(filename, "w") as file:
                    for s in city_under18:
                        file.write(f"Name: {s['Name']}, Age: {s['Age']}, City: {s['City']}\n")

        print("✅ All status reports exported successfully.")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")
