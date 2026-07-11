import json

def class_average(filename):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Collect averages from all students
        total = 0
        count = 0
        for student in database:
            if "Average" in student:
                total += student["Average"]
                count += 1

        # Compute class average
        if count > 0:
            return f"Class Average: {total / count:.2f}"
        else:
            return "No student averages found."
    except Exception as e:
        return f"Error: {e}"

# Test
print(class_average("class_reports.json"))

import json

def count_pass_fail(filename, pass_mark=75):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        # Counters
        passed = 0
        failed = 0

        # Check each student average
        for student in database:
            if "Average" in student:
                if student["Average"] >= pass_mark:
                    passed += 1
                else:
                    failed += 1

        return f"Passed: {passed}, Failed: {failed}"
    except Exception as e:
        return f"Error: {e}"

# Test
print(count_pass_fail("class_reports.json"))

import json

def class_attendance_summary(filename):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        total_attendance = 0
        count = 0

        # Collect attendance from all students
        for student in database:
            if "Attendance" in student:
                total_attendance += student["Attendance"]
                count += 1

        # Compute average attendance
        if count > 0:
            return f"Class Attendance Average: {total_attendance / count:.2f}%"
        else:
            return "No attendance records found."
    except Exception as e:
        return f"Error: {e}"

# Test
print(class_attendance_summary("class_reports.json"))

import json

def honors_probation_summary(filename):
    try:
        # Load existing database
        with open(filename, "r") as file:
            database = json.load(file)

        honors = 0
        probation = 0

        # Count based on Status field
        for student in database:
            if "Status" in student:
                if student["Status"] == "Honors":
                    honors += 1
                elif student["Status"] == "Probation":
                    probation += 1

        return f"Honors: {honors}, Probation: {probation}"
    except Exception as e:
        return f"Error: {e}"

# Test
print(honors_probation_summary("class_reports.json"))
