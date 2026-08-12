import sqlite3

def inner_join_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade
        FROM students s
        INNER JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Student Subjects and Grades (INNER JOIN):")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | Grade: {row[2]}")

    conn.close()

inner_join_report()

def left_join_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject, sub.grade
        FROM students s
        LEFT JOIN subjects sub ON s.id = sub.student_id
    """)

    print("\n📊 Student Subjects and Grades (LEFT JOIN):")
    for row in cursor.fetchall():
        subject = row[1] if row[1] else "No Subject"
        grade = row[2] if row[2] else "N/A"
        print(f"{row[0]} | {subject} | Grade: {grade}")

    conn.close()

left_join_report()

def cross_join_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.subject
        FROM students s
        CROSS JOIN subjects sub
    """)

    print("\n📊 Student and Subject Combinations (CROSS JOIN):")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]}")

    conn.close()

cross_join_report()

def multi_join_report():
    conn = sqlite3.connect("student_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name,
               sub.subject,
               sub.grade,
               t.teacher_name
        FROM students s
        LEFT JOIN subjects sub ON s.id = sub.student_id
        LEFT JOIN teachers t ON sub.teacher_id = t.id
    """)

    print("\n📊 Student, Subject, Grade, and Teacher Report (Multi‑Join):")
    for row in cursor.fetchall():
        subject = row[1] if row[1] else "No Subject"
        grade = row[2] if row[2] else "N/A"
        teacher = row[3] if row[3] else "No Teacher"
        print(f"{row[0]} | {subject} | Grade: {grade} | Teacher: {teacher}")

    conn.close()

multi_join_report()
