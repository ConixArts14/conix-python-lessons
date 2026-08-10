import sqlite3
import csv

def auto_export_csv():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    with open("student_report_auto.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Grade"])
        writer.writerows(rows)

    print("✅ Auto-export complete: student_report_auto.csv")

# Run automatically when script starts
auto_export_csv()

import sqlite3
import csv

def auto_export_csv():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    with open("student_report_auto.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Grade"])
        writer.writerows(rows)

    print("✅ Auto-export complete: student_report_auto.csv")

def auto_average_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(grade) FROM students")
    avg = cursor.fetchone()[0]   # ✅ use index 0, not [2]
    conn.close()
    print(f"📊 Class Average Grade: {avg:.2f}")

def auto_highest_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC LIMIT 1")
    top = cursor.fetchone()
    conn.close()
    if top:
        print(f"🏆 Highest Grade: {top[1]} by {top[0]}")

def auto_lowest_grade():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade ASC LIMIT 1")
    low = cursor.fetchone()
    conn.close()
    if low:
        print(f"📉 Lowest Grade: {low[1]} by {low[0]}")

# ✅ Run automatically when script starts
auto_export_csv()
auto_average_grade()
auto_highest_grade()
auto_lowest_grade()

def auto_grade_distribution():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    ranges = [
        ("A (90-100)", 90, 100),
        ("B (80-89)", 80, 89),
        ("C (70-79)", 70, 79),
        ("D (60-69)", 60, 69),
        ("E (50-59)", 50, 59),
        ("F (0-49)", 0, 49)
    ]

    print("\n📊 Grade Distribution:")
    for label, low, high in ranges:
        cursor.execute("SELECT COUNT(*) FROM students WHERE grade BETWEEN ? AND ?", (low, high))
        count = cursor.fetchone()[0]
        print(f"{label}: {count} student(s)")

    conn.close()

def auto_top_students(n=3):  # default to Top 3
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, grade FROM students ORDER BY grade DESC LIMIT ?", (n,))
    top_list = cursor.fetchall()
    conn.close()

    print(f"\n🏆 Top {n} Students:")
    if top_list:
        for i, (name, grade) in enumerate(top_list, start=1):
            print(f"{i}. {name} - {grade}")
    else:
        print("⚠️ No students found.")

def auto_failing_students():
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
