import sqlite3

def rolling_sum_grades():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               SUM(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
               ) AS rolling_sum
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Rolling Sum of Grades (Last 3 Rows):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Rolling Sum: {row[3]}")

    conn.close()

rolling_sum_grades()

def range_sum_grades():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               SUM(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   RANGE BETWEEN 10 PRECEDING AND CURRENT ROW
               ) AS range_sum
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Range-Based Sum of Grades (Within 10 Points):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Range Sum: {row[3]}")

    conn.close()

range_sum_grades()

def custom_frame_analysis():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade,
               AVG(sub.grade) OVER (
                   PARTITION BY sub.subject 
                   ORDER BY sub.grade 
                   ROWS BETWEEN 3 PRECEDING AND 2 FOLLOWING
               ) AS custom_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Custom Frame Analysis (3 Before, 2 After):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Custom Avg: {row[3]:.2f}")

    conn.close()

custom_frame_analysis()
