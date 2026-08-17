import sqlite3

def subquery_students():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, AVG(sub.grade) AS avg_grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        GROUP BY s.name
        HAVING avg_grade > (
            SELECT AVG(grade) FROM subjects
        )
    """)

    print("\n📊 Students with Above-Average Grades:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()

subquery_students()

def derived_table_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT dt.name, dt.avg_grade
        FROM (
            SELECT s.name, AVG(sub.grade) AS avg_grade
            FROM students s
            JOIN subjects sub ON s.id = sub.student_id
            GROUP BY s.name
        ) AS dt
        WHERE dt.avg_grade >= 85
    """)

    print("\n📊 Students with Avg Grade >= 85 (Derived Table):")
    for row in cursor.fetchall():
        print(f"{row[0]} | Avg Grade: {row[1]:.2f}")

    conn.close()

derived_table_report()

def correlated_subquery():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
        WHERE sub.grade > (
            SELECT AVG(sub2.grade)
            FROM subjects sub2
            WHERE sub2.subject = sub.subject
        )
    """)

    print("\n📊 Students with Grades Above Their Subject Average:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]}")

    conn.close()

correlated_subquery()

def subquery_in_select():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               sub.subject,
               sub.grade,
               (SELECT AVG(sub2.grade)
                FROM subjects sub2
                WHERE sub2.subject = sub.subject) AS subject_avg
        FROM students s
        JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Students with Grades and Subject Averages:")
    for row in cursor.fetchall():
        print(f"{row[0]} | Subject: {row[1]} | Grade: {row[2]} | Subject Avg: {row[3]:.2f}")

    conn.close()

subquery_in_select()
