import sqlite3

def cumulative_sum_grades():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               SUM(sub.grade) OVER (ORDER BY sub.subject, sub.grade DESC) AS cumulative_total
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Cumulative Grade Totals by Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Cumulative Total: {row[3]}")

    conn.close()

cumulative_sum_grades()

def moving_average_grades():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               AVG(sub.grade) OVER (PARTITION BY sub.subject ORDER BY sub.grade ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Moving Average of Grades by Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Moving Avg: {row[3]:.2f}")

    conn.close()

moving_average_grades()

def count_students_per_subject():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               COUNT(*) OVER (PARTITION BY sub.subject) AS subject_count
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Student Count per Subject:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Subject Count: {row[3]}")

    conn.close()

count_students_per_subject()

def combined_aggregates_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               SUM(sub.grade) OVER (PARTITION BY sub.subject ORDER BY sub.grade) AS cumulative_total,
               AVG(sub.grade) OVER (PARTITION BY sub.subject ORDER BY sub.grade ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg,
               COUNT(*) OVER (PARTITION BY sub.subject) AS subject_count
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Combined Window Aggregates Report:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Cumulative: {row[3]} | Moving Avg: {row[4]:.2f} | Count: {row[5]}")

    conn.close()

combined_aggregates_report()
