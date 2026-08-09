import sqlite3

def join_group_by_subject():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subjects.subject, AVG(subjects.grade)
        FROM students
        INNER JOIN subjects ON students.id = subjects.student_id
        GROUP BY subjects.subject
    """)
    results = cursor.fetchall()
    conn.close()

    print("\n📊 Average Grade per Subject (JOIN + GROUP BY):")
    for subject, avg in results:
        print(f"{subject}: {avg:.2f}")
join_group_by_subject()


import sqlite3

def join_having_subjects():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subjects.subject, AVG(subjects.grade)
        FROM students
        INNER JOIN subjects ON students.id = subjects.student_id
        GROUP BY subjects.subject
        HAVING AVG(subjects.grade) >= 85
    """)
    results = cursor.fetchall()
    conn.close()

    print("\n🏆 High Performing Subjects (JOIN + HAVING, avg ≥ 85):")
    for subject, avg in results:
        print(f"{subject}: {avg:.2f}")
join_having_subjects()


def complex_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.name, subjects.subject, AVG(subjects.grade)
        FROM students
        INNER JOIN subjects ON students.id = subjects.student_id
        GROUP BY students.name, subjects.subject
        HAVING AVG(subjects.grade) >= 85
    """)
    results = cursor.fetchall()
    conn.close()

    print("\n🏆 Complex Report — High Performers by Subject:")
    for name, subject, avg in results:
        print(f"{name} - {subject}: {avg:.2f}")
complex_reports()

import csv

def export_complex_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT students.name, subjects.subject, AVG(subjects.grade)
        FROM students
        INNER JOIN subjects ON students.id = subjects.student_id
        GROUP BY students.name, subjects.subject
        HAVING AVG(subjects.grade) >= 85
    """)
    results = cursor.fetchall()
    conn.close()

    with open("complex_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student", "Subject", "Average Grade"])
        writer.writerows(results)

    print("\n📂 Complex Report exported successfully to complex_report.csv")
export_complex_reports()
