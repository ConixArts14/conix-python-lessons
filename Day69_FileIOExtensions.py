15. Export Student Records to CSV
elif choice == "15":
    import json, csv
    try:
        with open("student_report.json", "r") as file:
            data = json.load(file)

        with open("student_report.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            # Write header row
            writer.writerow(["Name", "Age", "City"])
            # Write student records
            for student in data:
                writer.writerow([student["Name"], student["Age"], student["City"]])

        print("✅ Student records exported to student_report.csv")

    except FileNotFoundError:
        print("⚠️ No JSON report found. Please export first.")
Enter your choice (1-15): 15
✅ Student records exported to student_report.csv


16. Import Student Records from CSV
elif choice == "16":
    import json, csv
    try:
        with open("student_report.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        # Convert Age back to integer
        for student in data:
            student["Age"] = int(student["Age"])

        with open("student_report.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Student records imported from student_report.csv into student_report.json")

    except FileNotFoundError:
        print("⚠️ No CSV file found. Please export first.")
Enter your choice (1–16): 16
✅ Student records imported from student_report.csv into student_report.json

17. Sync CSV and JSON
elif choice == "17":
    import json, csv, os

    json_exists = os.path.exists("student_report.json")
    csv_exists = os.path.exists("student_report.csv")

    if not json_exists and not csv_exists:
        print("🚫 No files found. Please export first.")
    elif json_exists and not csv_exists:
        print("🔄 CSV missing. Regenerating from JSON...")
        # Step 3 goes here
    elif csv_exists and not json_exists:
        print("🔄 JSON missing. Regenerating from CSV...")
        # Step 4 goes here
    else:
        print("✅ Both files exist. Sync check complete.")
        with open("student_report.json", "r") as file:
            data = json.load(file)

        with open("student_report.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Age", "City"])
            for student in data:
                writer.writerow([student["Name"], student["Age"], student["City"]])

        print("✅ student_report.csv regenerated from JSON")

Enter your choice (1-17): 17
✅ Both files exist. Sync check complete.
Enter your choice (1-17): 17
🔄 CSV missing. Regenerating from JSON...
✅ student_report.csv regenerated from JSON


18. Enhanced Sync (Update Outdated File)
elif choice == "18":
    import json, csv, os, time

    json_file = "student_report.json"
    csv_file = "student_report.csv"

    json_exists = os.path.exists(json_file)
    csv_exists = os.path.exists(csv_file)

    if not json_exists and not csv_exists:
        print("🚫 No files found. Please export first.")
    elif json_exists and csv_exists:
        json_time = os.path.getmtime(json_file)
        csv_time = os.path.getmtime(csv_file)

        if json_time > csv_time:
            print("🔄 JSON is newer. Updating CSV...")
            with open(json_file, "r") as file:
                data = json.load(file)

            with open(csv_file, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Age", "City"])
                for student in data:
                    writer.writerow([student["Name"], student["Age"], student["City"]])

            print("✅ student_report.csv updated from JSON")

        elif csv_time > json_time:
            print("🔄 CSV is newer. Updating JSON...")
            with open(csv_file, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader]

            for student in data:
                student["Age"] = int(student["Age"])

            with open(json_file, "w") as file:
                json.dump(data, file, indent=4)

            print("✅ student_report.json updated from CSV")

        else:
            print("✅ Both files are already in sync.")
    elif json_exists and not csv_exists:
        print("📄 CSV missing. Regenerating from JSON...")
        # reuse logic from Activity 3
    elif csv_exists and not json_exists:
        print("📄 JSON missing. Regenerating from CSV...")
        # reuse logic from Activity 3
Enter your choice (1-18): 18
🔄 JSON is newer. Updating CSV...
✅ student_report.csv updated from JSON
Enter your choice (1-18): 18
🔄 CSV is newer. Updating JSON...
✅ student_report.json updated from CSV
