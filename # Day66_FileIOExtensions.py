4# Day66_FileIOExtensions.py

students = [
    {"Name": "Jacob", "Age": 10, "City": "Tagum"},
    {"Name": "Leonard", "Age": 18, "City": "Davao"},
    {"Name": "Alex", "Age": 15, "City": "Manila"}
]

while True:
    print("\n--- Student Report Menu ---")
    print("1. Export to Text")
    print("2. Export to CSV")
    print("3. Export to JSON")
    print("4. Exit")
    print("5. Show Summary")
    print("6. Detailed Summary")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        with open("student_report.txt", "w") as file:
            for student in students:
                file.write(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}\n")
        print("Report saved to student_report.txt")

    elif choice == "2":
        import csv
        with open("student_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "City"])
            for student in students:
                writer.writerow([student["Name"], student["Age"], student["City"]])
        print("Report saved to student_report.csv")

    elif choice == "3":
        import json
        with open("student_report.json", "w") as file:
            json.dump(students, file, indent=4)
        print("Report saved to student_report.json")

    elif choice == "4":
        print("Exiting program...")
        break

    elif choice == "5":
        total_students = len(students)
        avg_age = sum(student["Age"] for student in students) / total_students
        with open("student_summary.txt", "w") as file:
            file.write(f"Total Students: {total_students}\n")
            file.write(f"Average Age: {avg_age:.2f}\n")
        print("Summary saved to student_summary.txt")

    elif choice == "6":
        total_students = len(students)
        avg_age = sum(student["Age"] for student in students) / total_students
        cities = {student["City"] for student in students}
        with open("student_detailed_summary.txt", "w") as file:
            file.write(f"Total Students: {total_students}\n")
            file.write(f"Average Age: {avg_age:.2f}\n")
            file.write(f"Cities Represented: {', '.join(cities)}\n")
        print("Detailed summary saved to student_detailed_summary.txt")

    else:
        print("⚠️ Invalid choice. Please enter 1–6.")


7. Export All Formats
elif choice == "7":
    # Export to Text
    with open("student_report.txt", "w") as file:
        for student in students:
            file.write(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}\n")

    # Export to CSV
    import csv
    with open("student_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        for student in students:
            writer.writerow([student["Name"], student["Age"], student["City"]])

    # Export to JSON
    import json
    with open("student_report.json", "w") as file:
        json.dump(students, file, indent=4)

    # Export Summary
    total_students = len(students)
    avg_age = sum(student["Age"] for student in students) / total_students
    with open("student_summary.txt", "w") as file:
        file.write(f"Total Students: {total_students}\n")
        file.write(f"Average Age: {avg_age:.2f}\n")

    print("All reports exported: Text, CSV, JSON, and Summary.")
