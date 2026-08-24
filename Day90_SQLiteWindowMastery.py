import sqlite3

def mastery_review_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               ROW_NUMBER() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS row_num,
               RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS rank_pos,
               DENSE_RANK() OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS dense_rank_pos,
               NTILE(4) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade DESC
               ) AS quartile,
               CAST(100.0 * 
                    RANK() OVER (
                        PARTITION BY sub.subject 
                        ORDER BY sub.grade DESC
                    ) 
                    / COUNT(*) OVER (PARTITION BY sub.subject) 
               AS INT) AS percentile,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_avg,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject
               ) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Mastery Review Report:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Row#: {row[3]} | RANK: {row[4]} | DENSE_RANK: {row[5]} | Quartile: {row[6]} | Percentile: {row[7]}% | Rolling Avg: {row[8]:.2f} | Subject Avg: {row[9]:.2f}")

    conn.close()

mastery_review_report()

import csv

def export_mastery_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               NTILE(4) OVER (PARTITION BY sub.subject ORDER BY sub.grade DESC) AS quartile,
               CAST(100.0 * RANK() OVER (PARTITION BY sub.subject ORDER BY sub.grade DESC) 
                    / COUNT(*) OVER (PARTITION BY sub.subject) AS INT) AS percentile,
               AVG(sub.grade) OVER (PARTITION BY sub.subject ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg,
               AVG(sub.grade) OVER (PARTITION BY sub.subject) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    rows = cursor.fetchall()
    with open("Day90_MasterReport.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Subject", "Grade", "Quartile", "Percentile", "Rolling Avg", "Subject Avg"])
        writer.writerows(rows)

    conn.close()

export_mastery_report()
