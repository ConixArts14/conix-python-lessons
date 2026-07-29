students = [
    {"Name": "Conix", "Age": 10, "City": "Tagum"},
    {"Name": "Leonald", "Age": 18, "City": "Davao"},
    {"Name": "Aeg", "Age": 15, "City": "Manila"}
]
with open("student_report.txt", "w") as file:
    for student in students:
        file.write(f"Name: {student['Name']}, Age: {student['Age']}, City: {student['City']}\n")

print("Report saved to student_report.txt")


import csv

with open("student_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # header row
    for student in students:
        writer.writerow([student["Name"], student["Age"], student["City"]])

print("Report saved to student_report.csv")


import json

with open("student_report.json", "w") as file:
    json.dump(students, file, indent=4)

print("Report saved to student_report.json")
