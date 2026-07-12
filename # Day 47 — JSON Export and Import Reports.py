import json

def export_class_data(source_file, backup_file):
    try:
        # Load existing database
        with open(source_file, "r") as file:
            database = json.load(file)

        # Save to backup file
        with open(backup_file, "w") as file:
            json.dump(database, file)

        return f"Data exported successfully to {backup_file}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(export_class_data("class_reports.json", "class_backup.json"))

import json

def import_class_data(backup_file, target_file):
    try:
        # Load backup database
        with open(backup_file, "r") as file:
            backup_data = json.load(file)

        # Restore into target file
        with open(target_file, "w") as file:
            json.dump(backup_data, file)

        return f"Data imported successfully from {backup_file} to {target_file}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(import_class_data("class_backup.json", "class_reports.json"))

import json

def export_selected_students(source_file, backup_file, student_names):
    try:
        # Load existing database
        with open(source_file, "r") as file:
            database = json.load(file)

        # Filter only selected students
        selected = [student for student in database if student["Name"] in student_names]

        # Save to backup file
        with open(backup_file, "w") as file:
            json.dump(selected, file)

        return f"Selected students exported successfully to {backup_file}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(export_selected_students("class_reports.json", "selected_backup.json", ["Conix", "Alex"]))

import json

def import_selected_students(backup_file, target_file):
    try:
        # Load backup data (selected students)
        with open(backup_file, "r") as file:
            selected_data = json.load(file)

        # Load existing class database
        with open(target_file, "r") as file:
            database = json.load(file)

        # Merge selected students into main database
        database.extend(selected_data)

        # Save updated database
        with open(target_file, "w") as file:
            json.dump(database, file)

        return f"Selected students imported successfully from {backup_file} into {target_file}."
    except Exception as e:
        return f"Error: {e}"

# Test
print(import_selected_students("selected_backup.json", "class_reports.json"))
