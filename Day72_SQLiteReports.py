import sqlite3
import csv
def export_to_csv():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    with open("student_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["ID", "Name", "Grade"])
        # Write data
        writer.writerows(rows)

    print("📊 Student records exported to student_report.csv")
print("8. Export Records to CSV")

choice = input("Enter choice (1-8): ")

if choice == "8":
    export_to_csv()

def average_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()[0]
    conn.close()
    print(f"📊 Class Average Grade: {avg:.2f}")

def highest_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC LIMIT 1")
    top = cursor.fetchone()
    conn.close()
    if top:
        print(f"🏆 Highest Grade: {top[1]} by {top[0]}")
    else:
        print("⚠️ No records found.")

def lowest_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade ASC LIMIT 1")
    low = cursor.fetchone()
    conn.close()
    if low:
        print(f"📉 Lowest Grade: {low[1]} by {low[0]}")
    else:
        print("⚠️ No records found.")
print("9. Show Average Grade")
print("10. Show Highest Grade")
print("11. Show Lowest Grade")

choice = input("Enter choice (1-11): ")

if choice == "9":
    average_grade()
elif choice == "10":
    highest_grade()
elif choice == "11":
    lowest_grade()

def grade_distribution():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    ranges = [
        ("90-100", 90, 100),
        ("80-89", 80, 89),
        ("70-79", 70, 79),
        ("60-69", 60, 69),
        ("Below 60", 0, 59)
    ]

    print("📊 Grade Distribution:")
    for label, low, high in ranges:
        cursor.execute("SELECT COUNT(*) FROM students WHERE grade BETWEEN ? AND ?", (low, high))
        count = cursor.fetchone()[0]
        print(f"{label}: {count} student(s)")

    conn.close()
print("12. Show Grade Distribution")

choice = input("Enter choice (1-12): ")

if choice == "12":
    grade_distribution()

def top_students(n):
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC LIMIT ?", (n,))
    top_list = cursor.fetchall()
    conn.close()

    print(f"\n🏆 Top {n} Students:")
    for i, (name, grade) in enumerate(top_list, start=1):
        print(f"{i}. {name} - {grade}")
print("13. Show Top N Students")

choice = input("Enter choice (1-13): ")

if choice == "13":
    n = int(input("Enter how many top students to display: "))
    top_students(n)

def failing_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students WHERE grade < 60")
    fails = cursor.fetchall()
    conn.close()

    print("\n⚠️ Failing Students (grade < 60):")
    if fails:
        for name, grade in fails:
            print(f"{name} - {grade}")
    else:
        print("✅ No failing students found.")
print("14. Show Failing Students")

choice = input("Enter choice (1-14): ")

if choice == "14":
    failing_students()
