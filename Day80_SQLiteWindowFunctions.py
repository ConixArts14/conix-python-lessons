import sqlite3

def rank_students_row_number():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               AVG(sub.grade) AS avg_grade,
               ROW_NUMBER() OVER (ORDER BY AVG(sub.grade) DESC) AS row_num
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)

    print("\n📊 Student Ranking with ROW_NUMBER:")
    for row in cursor.fetchall():
        print(f"Rank {row[2]} | {row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()

rank_students_row_number()

def rank_students_rank():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               AVG(sub.grade) AS avg_grade,
               RANK() OVER (ORDER BY AVG(sub.grade) DESC) AS rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)

    print("\n🏆 Student Ranking with RANK:")
    for row in cursor.fetchall():
        print(f"Rank {row[2]} | {row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()


def rank_students_dense_rank():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               AVG(sub.grade) AS avg_grade,
               DENSE_RANK() OVER (ORDER BY AVG(sub.grade) DESC) AS dense_rank_pos
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
    """)

    print("\n🥇 Student Ranking with DENSE_RANK:")
    for row in cursor.fetchall():
        print(f"Dense Rank {row[2]} | {row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()


rank_students_rank()
rank_students_dense_rank()

def running_totals():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               sub.subject,
               sub.grade,
               SUM(sub.grade) OVER (PARTITION BY s.name ORDER BY sub.subject) AS running_total
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Running Totals of Grades per Student:")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | Grade: {row[2]} | Running Total: {row[3]}")

    conn.close()

running_totals()

def moving_averages():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               sub.subject,
               sub.grade,
               AVG(sub.grade) OVER (
                   PARTITION BY s.name 
                   ORDER BY sub.subject 
                   ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
               ) AS moving_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Moving Average of Grades per Student:")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | Grade: {row[2]} | Moving Avg: {row[3]:.2f}")

    conn.close()

moving_averages()

import csv

def export_window_reports():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               AVG(sub.grade) AS avg_grade,
               RANK() OVER (ORDER BY AVG(sub.grade) DESC) AS rank_pos,
               DENSE_RANK() OVER (ORDER BY AVG(sub.grade) DESC) AS dense_rank_pos,
               SUM(sub.grade) OVER (PARTITION BY s.name ORDER BY sub.subject) AS running_total,
               AVG(sub.grade) OVER (
                   PARTITION BY s.name 
                   ORDER BY sub.subject 
                   ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
               ) AS moving_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name, sub.subject
    """)

    rows = cursor.fetchall()

    with open("Day80_WindowReports.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Avg Grade", "Rank", "Dense Rank", "Running Total", "Moving Avg"])
        writer.writerows(rows)

    conn.close()
    print("\n📂 Exported window function reports to Day80_WindowReports.csv")
