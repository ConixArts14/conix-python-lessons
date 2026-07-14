import json

def sort_by_average(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort students by Average, highest first
        sorted_students = sorted(data, key=lambda s: s.get("Average", 0), reverse=True)
        return sorted_students
    except Exception as e:
        return f"Error: {e}"

# Test
print(sort_by_average("class_reports.json"))

import json

def sort_by_attendance(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort students by Attendance, highest first
        sorted_students = sorted(data, key=lambda s: s.get("Attendance", 0), reverse=True)
        return sorted_students
    except Exception as e:
        return f"Error: {e}"

# Test
print(sort_by_attendance("class_reports.json"))

import json

def top_5_students(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort by Average, highest first
        sorted_students = sorted(data, key=lambda s: s.get("Average", 0), reverse=True)
        # Take only the top 5
        return sorted_students[:5]
    except Exception as e:
        return f"Error: {e}"

# Test
print(top_5_students("class_reports.json"))

import json

def top_5_attendance(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort by Attendance, highest first
        sorted_students = sorted(data, key=lambda s: s.get("Attendance", 0), reverse=True)
        # Take only the top 5
        return sorted_students[:5]
    except Exception as e:
        return f"Error: {e}"

# Test
print(top_5_attendance("class_reports.json"))
