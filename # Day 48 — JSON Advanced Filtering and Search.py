import json

def filter_honors_students(filename):
    try:
        with open(filename, "r") as file:
            data = json. load(file)
        honors = [s for s in data if s.get("Status") == "Honors"]
        return honors
    except Exception as e:
        return f"Error: {e}"
    
# Test
print(filter_honors_students("class_reports.json"))

def filter_high_attendance(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        high_attendance = [s for s in data if s.get("Attendance", 0) > 90]
        return high_attendance
    except Exception as e:
        return f"Error: {e}"

# Test
print(filter_high_attendance("class_reports.json"))

def filter_honors_high_attendance(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        filtered = [s for s in data if s.get("Status") == "Honors" and s.get("Attendance", 0) > 90]
        return filtered
    except Exception as e:
        return f"Error: {e}"

# Test
print(filter_honors_high_attendance("class_reports.json"))

def filter_probation_low_attendance(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        filtered = [s for s in data if s.get("Status") == "Probation" and s.get("Attendance", 0) < 60]
        return filtered
    except Exception as e:
        return f"Error: {e}"

# Test
print(filter_probation_low_attendance("class_reports.json"))
