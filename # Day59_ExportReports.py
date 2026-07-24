def export_json(students):
    with open("student_report.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Report exported to student_report.json")
import csv

def export_csv(students):
    with open("student_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Address", "Contact"])
        for s in students:
            writer.writerow([s["id"], s["name"], s["age"], s["details"]["address"], s["details"]["contact"]])
    print("Report exported to student_report.csv")
import csv

def export_csv(students):
    with open("student_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Address", "Contact"])
        for s in students:
            writer.writerow([s["id"], s["name"], s["age"], s["details"]["address"], s["details"]["contact"]])
    print("Report exported to student_report.csv")
elif choice == "6":
    students = load_students()
    export_json(students)

elif choice == "7":
    students = load_students()
    export_csv(students)


def export_summary(students):
    total = len(students)
    avg_age = sum(int(s["age"]) for s in students) / total if total > 0 else 0
    youngest = min(students, key=lambda x: int(x["age"]))["name"]
    oldest = max(students, key=lambda x: int(x["age"]))["name"]

    with open("student_summary.txt", "w") as file:
        file.write(f"Total Students: {total}\n")
        file.write(f"Average Age: {avg_age:.2f}\n")
        file.write(f"Youngest Student: {youngest}\n")
        file.write(f"Oldest Student: {oldest}\n")

    print("Summary report exported to student_summary.txt")
