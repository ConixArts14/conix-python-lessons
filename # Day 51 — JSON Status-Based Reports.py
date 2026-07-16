import json

def status_leaderboards(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Group students by Status
        grouped = {}
        for student in data:
            status = student.get("Status", "Unknown")
            if status not in grouped:
                grouped[status] = []
            grouped[status].append(student)

        # Sort each group by Average, then Attendance
        for status in grouped:
            grouped[status] = sorted(
                grouped[status],
                key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
                reverse=True
            )

        return grouped
    except Exception as e:
        return f"Error: {e}"

# Test
print(status_leaderboards("class_reports.json"))

import json

def export_status_reports(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Group students by Status
        grouped = {}
        for student in data:
            status = student.get("Status", "Unknown")
            if status not in grouped:
                grouped[status] = []
            grouped[status].append(student)

        # Sort each group and export to separate files
        for status, students in grouped.items():
            sorted_group = sorted(
                students,
                key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
                reverse=True
            )
            output_file = f"{status.lower()}_report.json"
            with open(output_file, "w") as outfile:
                json.dump(sorted_group, outfile, indent=4)
            print(f"{status} report saved to {output_file}")

        return "All status reports generated successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
print(export_status_reports("class_reports.json"))

import json

def export_status_text_reports(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Group students by Status
        grouped = {}
        for student in data:
            status = student.get("Status", "Unknown")
            if status not in grouped:
                grouped[status] = []
            grouped[status].append(student)

        # Sort each group and export to separate text files
        for status, students in grouped.items():
            sorted_group = sorted(
                students,
                key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
                reverse=True
            )
            output_file = f"{status.lower()}_report.txt"
            with open(output_file, "w") as outfile:
                outfile.write(f"=== {status} Leaderboard Report ===\n\n")
                for i, student in enumerate(sorted_group, start=1):
                    outfile.write(
                        f"{i}. {student['Name']} | Average: {student['Average']} | Attendance: {student['Attendance']} | Status: {student['Status']}\n"
                    )
            print(f"{status} text report saved to {output_file}")

        return "All status text reports generated successfully."
    except Exception as e:
        return f"Error: {e}"

# Test
print(export_status_text_reports("class_reports.json"))

import json

def status_summary_report(filename, output_file):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        # Group students by Status
        grouped = {}
        for student in data:
            status = student.get("Status", "Unknown")
            if status not in grouped:
                grouped[status] = []
            grouped[status].append(student)

        # Write one master summary file
        with open(output_file, "w") as outfile:
            outfile.write("=== Status Summary Report ===\n\n")
            for status, students in grouped.items():
                outfile.write(f"--- {status} Leaderboard ---\n")
                sorted_group = sorted(
                    students,
                    key=lambda s: (s.get("Average", 0), s.get("Attendance", 0)),
                    reverse=True
                )
                for i, student in enumerate(sorted_group, start=1):
                    outfile.write(
                        f"{i}. {student['Name']} | Average: {student['Average']} | Attendance: {student['Attendance']} | Status: {student['Status']}\n"
                    )
                outfile.write("\n")
        return f"Summary report saved to {output_file}"
    except Exception as e:
        return f"Error: {e}"

# Test
print(status_summary_report("class_reports.json", "status_summary.txt"))
