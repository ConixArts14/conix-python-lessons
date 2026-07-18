import json

def add_subjects_json(filename, student_name, subjects):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Find the student and add subjects
        for report in database:
            if report["Name"] == student_name:
                report["Subjects"] = subjects

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{student_name}'s subjects added successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
subjects_list = {
    "Math": 92,
    "Science": 88,
    "English": 95
}
print(add_subjects_json("class_reports.json", "Conix", subjects_list))

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
print(update_subject_json("class_reports.json", "Conix", "Science", 91))
 
import json

def remove_subject_json(filename, student_name, subject):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Find the student and remove the subject
        for report in database:
            if report["Name"] == student_name and "Subjects" in report:
                if subject in report["Subjects"]:
                    del report["Subjects"][subject]

        # Save back to JSON
        with open(filename, "w") as file:
            json.dump(database, file)

        return f"{subject} removed from {student_name}'s record."
    except Exception as e:
        return f"Error: {e}"

# Test
print(remove_subject_json("class_reports.json", "Conix", "English"))

import json

def search_subject_json(filename, student_name, subject):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Find the student and subject
        for report in database:
            if report["Name"] == student_name and "Subjects" in report:
                if subject in report["Subjects"]:
                    return f"{student_name}'s {subject} score is {report['Subjects'][subject]}"

        return f"{subject} not found for {student_name}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(search_subject_json("class_reports.json", "Conix", "Math"))

