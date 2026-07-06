def save_report(report, filename):
    try:
        with open(filename, "w") as file:
            file.write(str(report))
        return "Report saved successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
report = {"Name": "Conix", "Average": 85.25, "Attendance": 85, "Status": "Eligible"}
print(save_report(report, "student_report.txt"))

def load_report(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error: {e}"

# Test
print(load_report("student_report.txt"))

def save_class_reports(database, filename):
    try:
        with open(filename, "w") as file:
            for report in database:
                file.write(str(report) + "\n")
        return "Class reports saved successfully."
    except Exception as e:
        return f"Error: {e}"

# Example usage
database = [
    {"Name": "Conix", "Average": 93, "Attendance": 92, "Status": "Honors"},
    {"Name": "Leonald", "Average": 71.75, "Attendance": 75, "Status": "Probation"},
    {"Name": "Alex", "Average": 62.25, "Attendance": 70, "Status": "Probation"}
]

print(save_class_reports(database, "class_reports.txt"))

def load_class_reports(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return [eval(line.strip()) for line in lines]
    except Exception as e:
        return f"Error: {e}"

# Test
reports = load_class_reports("class_reports.txt")
print(reports)
