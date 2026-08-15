import sqlite3

def grouping_sets_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY GROUPING SETS ((s.name), (sub.subject), ())
    """)

    print("\n📊 GROUPING SETS Report (Student, Subject, Overall):")
    for row in cursor.fetchall():
        print(f"Student: {row[0]} | Subject: {row[1]} | Avg Grade: {row[2]:.2f}")

    conn.close()

grouping_sets_report()

def rollup_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, SUM(sub.grade) AS total_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY ROLLUP(s.name, sub.subject)
    """)

    print("\n📊 ROLLUP Report (Subtotals and Grand Totals):")
    for row in cursor.fetchall():
        print(f"Student: {row[0]} | Subject: {row[1]} | Total Grade: {row[2]}")

    conn.close()

rollup_report()

def cube_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, SUM(sub.grade) AS total_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY CUBE(s.name, sub.subject)
    """)

    print("\n📊 CUBE Report (All Combinations of Groupings):")
    for row in cursor.fetchall():
        print(f"Student: {row[0]} | Subject: {row[1]} | Total Grade: {row[2]}")

    conn.close()

cube_report()

def grouping_sets_simulation():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, NULL AS subject, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name

        UNION ALL

        SELECT NULL AS name, sub.subject, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY sub.subject

        UNION ALL

        SELECT NULL AS name, NULL AS subject, AVG(sub.grade) AS avg_grade
        FROM subjects
    """)

    print("\n📊 Simulated GROUPING SETS Report:")
    for row in cursor.fetchall():
        print(f"Student: {row[0]} | Subject: {row[1]} | Avg Grade: {row[2]:.2f}")

    conn.close()

grouping_sets_simulation()

import csv

def export_grouping_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name, sub.subject
    """)
    rows = cursor.fetchall()

    with open("Day81_GroupingReports.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student", "Subject", "Avg Grade"])
        writer.writerows(rows)

    conn.close()
    print("\n📂 Exported grouping reports to Day81_GroupingReports.csv")

export_grouping_reports()
