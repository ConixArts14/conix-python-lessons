import json

def add_student_json(filename, student_record):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Add new student record
        database.append(student_record)

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_record['Name']} added successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
new_student = {
    "Name": "Alex",
    "Average": 87,
    "Attendance": 90,
    "Status": "Regular",
    "Subjects": {
        "Math": 85,
        "Science": 88,
        "English": 89
    }
}

print(add_student_json("class_reports.json", new_student))

import json

def update_student_json(filename, student_name, field, new_value):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Find the student and update the chosen field
        for report in database:
            if report["Name"] == student_name:
                report[field] = new_value

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_name}'s {field} updated to {new_value}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(update_student_json("class_reports.json", "Alex", "Attendance", 95))

import json

def update_subject_json(filename, student_name, subject, new_score):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Find the student and update the subject score
        for report in database:
            if report["Name"] == student_name and "Subjects" in report:
                report["Subjects"][subject] = new_score

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_name}'s {subject} score updated to {new_score}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(update_subject_json("class_reports.json", "Alex", "Science", 92))

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

        return f"{student_name}'s record removed successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
print(remove_student_json("class_reports.json", "Alex"))
