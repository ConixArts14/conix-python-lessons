with open("notes.txt", "w") as file:
    file.write("Hello, this is my first text file!\n")
    file.write("Day 62 Activity 1 complete.\n")
with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)
with open("notes.txt", "a") as file:
    file.write("Adding another line at the end.\n")

    import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Conix", 10, "Tagum"])
    writer.writerow(["Leonald", 18, "Davao"])
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["New Student", 15, "Manila"])

import json

students = [
    {"Name": "Conix", "Age": 10, "City": "Tagum"},
    {"Name": "Leonald", "Age": 18, "City": "Davao"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
with open("students.json", "r") as file:
    data = json.load(file)
    print("JSON data:", data)
with open("students.json", "r") as file:
    data = json.load(file)

data.append({"Name": "New Student", "Age": 15, "City": "Manila"})

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
