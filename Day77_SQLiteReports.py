import sqlite3

def generate_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Count subjects per student
    cursor.execute("""
        SELECT s.name, COUNT(sub.subject) AS subject_count
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)
    print("\n📊 Subjects per student:")
    for row in cursor.fetchall():
        print(f"{row[0]} has {row[1]} subjects")

    # Average grade per student
    cursor.execute("""
        SELECT s.name, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)
    print("\n📊 Average grade per student:")
    for row in cursor.fetchall():
        print(f"{row[0]} average grade: {row[1]:.2f}")

    # Highest grade per student
    cursor.execute("""
        SELECT s.name, MAX(sub.grade) AS max_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)
    print("\n📊 Highest grade per student:")
    for row in cursor.fetchall():
        print(f"{row[0]} highest grade: {row[1]}")

    conn.close()
generate_reports()


def grouped_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Students with average grade above 90
    cursor.execute("""
        SELECT s.name, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
        HAVING AVG(sub.grade) > 90
    """)
    print("\n🏆 Students with average grade above 90:")
    for row in cursor.fetchall():
        print(f"{row[0]} average grade: {row[1]:.2f}")

    conn.close()
grouped_reports()

def totals_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    # Total number of subjects in database
    cursor.execute("SELECT COUNT(*) FROM subjects")
    total_subjects = cursor.fetchone()[0]
    print(f"\n📊 Total subjects in database: {total_subjects}")

    # Sum of all grades
    cursor.execute("SELECT SUM(grade) FROM subjects")
    total_grades = cursor.fetchone()[0]
    print(f"📊 Sum of all grades: {total_grades}")

    # Overall average grade across all students
    cursor.execute("SELECT AVG(grade) FROM subjects")
    overall_avg = cursor.fetchone()[0]
    print(f"📊 Overall average grade: {overall_avg:.2f}")

    conn.close()
totals_reports()


def complex_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               COUNT(sub.subject) AS subject_count,
               AVG(sub.grade) AS avg_grade,
               MAX(sub.grade) AS max_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)
    print("\n📊 Full student performance report:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subjects: {row[1]} | Avg: {row[2]:.2f} | Max: {row[3]}")

    conn.close()
complex_reports()


import csv

def export_reports_to_csv():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               COUNT(sub.subject) AS subject_count,
               AVG(sub.grade) AS avg_grade,
               MAX(sub.grade) AS max_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)

    rows = cursor.fetchall()

    with open("student_reports.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Subjects", "Average Grade", "Highest Grade"])
        writer.writerows(rows)

    conn.close()
    print("\n📂 Reports exported to student_reports.csv")
export_reports_to_csv()