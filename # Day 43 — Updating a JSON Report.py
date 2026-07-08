import json

def update_report_json(filename, student_name, new_data):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Update the matching student
        for report in database:
            if report["Name"] == student_name:
                report.update(new_data)

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_name}'s report updated successfully."
    except Exception as e:
        return f"Error: {e}"

import json

def add_student_json(filename, new_student):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Add the new student
        database.append(new_student)

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{new_student['Name']} added successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
new_student = {"Name": "Maya", "Average": 88.5, "Attendance": 90, "Status": "Eligible"}
print(add_student_json("class_reports.json", new_student))

import json

def remove_student_json(filename, student_name):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Filter out the student
        database = [report for report in database if report["Name"] != student_name]

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_name} removed successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
print(remove_student_json("class_reports.json", "Alex"))

import json

def search_student_json(filename, student_name):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Search for the student
        for report in database:
            if report["Name"] == student_name:
                return report

        return f"{student_name} not found."
    except Exception as e:
        return f"Error: {e}"

# Test
print(search_student_json("class_reports.json", "Maya"))
