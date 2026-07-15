import json

def combined_leaderboard(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort by Average first, then Attendance as a tiebreaker
        sorted_students = sorted(
            data,
            key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
            reverse=True
        )
        return sorted_students
    except Exception as e:
        return f"Error: {e}"

# Test
print(combined_leaderboard("class_reports.json"))

import json

def generate_combined_report(filename, output_file):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort by Average first, then Attendance
        sorted_students = sorted(
            data,
            key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
            reverse=True
        )
        # Save the sorted leaderboard into a new JSON file
        with open(output_file, "w") as outfile:
            json.dump(sorted_students, outfile, indent=4)
        return f"Report saved to {output_file}"
    except Exception as e:
        return f"Error: {e}"

# Test
print(generate_combined_report("class_reports.json", "combined_report.json"))

import json

def export_text_report(filename, output_file):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Sort by Average first, then Attendance
        sorted_students = sorted(
            data,
            key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
            reverse=True
        )
        # Write a text summary
        with open(output_file, "w") as outfile:
            outfile.write("=== Combined Leaderboard Report ===\n\n")
            for i, student in enumerate(sorted_students, start=1):
                outfile.write(
                    f"{i}. {student['Name']} | Average: {student['Average']} | Attendance: {student['Attendance']} | Status: {student['Status']}\n"
                )
        return f"Text report saved to {output_file}"
    except Exception as e:
        return f"Error: {e}"

# Test
print(export_text_report("class_reports.json", "combined_report.txt"))

import json

def honors_leaderboard(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        # Filter only students with Honors status
        honors_students = [s for s in data if s.get("Status") == "Honors"]
        # Sort by Average first, then Attendance
        sorted_honors = sorted(
            honors_students,
            key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
            reverse=True
        )
        return sorted_honors
    except Exception as e:
        return f"Error: {e}"

# Test
print(honors_leaderboard("class_reports.json"))
